#!/usr/bin/env python3
"""Retrieve the full texts of the bibliography's sources, where a bot can.

Reads finishing/refs.bib and, for each entry, tries in order:

    eprint (arXiv)   https://arxiv.org/pdf/<id>
    url              the entry's own link
    doi              https://doi.org/<doi>

and takes the first that yields a full text:

    a PDF                  saved as KEY.pdf
    an HTML page           its <meta name="citation_pdf_url"> is followed if it
                           has one. Otherwise the page counts only from a `url`
                           field and only with at least MIN_TEXT characters of
                           visible text, and is saved twice:
                             KEY.pdf   printed by headless Chrome/Chromium
                             KEY.html  one self-contained file, by SingleFile
                           A DOI that lands on a publisher's page with no PDF
                           behind it is a failure: that page is the abstract.
    anything else          saved under the extension its media type implies

SingleFile here is single-file-cli, the command-line build of the Chrome
extension, by the same author; the extension itself can't be driven from a
script. Install it with `npm install -g single-file-cli` (version 2 wants
Node 24 or later, or Deno), or pass its path with --single-file. Without it,
or where it fails, the page is saved as fetched, KEY.raw.html, with its
images and styles still remote. Without Chrome, there is no KEY.pdf, and
the run says so at the start. Pass --chrome PATH if it isn't found.

Entries with no link at all are failures too: the books, mostly.

Writes, into finishing/source-texts/ (or --out):

    successfully-retrieved/              the files, KEY.<ext>; zipped at the end
                                         and then removed (--keep keeps it)
    successfully-retrieved_<date>.zip
    successfully-retrieved.txt           @KEY, then the URL the file came from
    failed-retrieval.txt                 @KEY, then the URL tried first, or
                                         "none" where refs.bib gives no link

The folder and the zip are gitignored and must stay so. They hold other
people's copyrighted work, and this repository is public. The two lists are
plain text and safe to commit.

"Retrieved" means a file came back that passed the checks above. It does not
mean anyone has read it, that it is the edition cited, or that an HTML page is
the whole article rather than a paywall's first screen. A human check of the
entry is still what refs_ledger.py --mark records.

    fetch_sources.py                     every entry
    fetch_sources.py --only KEY [KEY..]  just these
    fetch_sources.py --limit 20          the first 20, to try it out
"""
import argparse
import concurrent.futures
import datetime
import html
import mimetypes
import os
import re
import shutil
import subprocess
import tempfile
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
BIB = os.path.join(REPO, "finishing", "refs.bib")
OUT = os.path.join(REPO, "finishing", "source-texts")

UA = ("antifascist-intelligence-source-fetch/1.0 "
      "(+https://github.com/iterabloom/antifascist.intelligence)")
TIMEOUT = 45          # seconds per request
MAX_BYTES = 150 << 20  # 150 MB per file
MIN_TEXT = 2000       # visible characters an HTML page needs to count
HOST_GAP = 2.0        # seconds between requests to the same host
RENDER_TIMEOUT = 180  # seconds for one Chrome print or SingleFile save
RENDERERS = threading.Semaphore(2)  # browsers at once

CHROME_NAMES = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"]
CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/opt/pw-browsers/chromium",
]

ENTRY_RE = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,")
FIELD_RE = re.compile(r"(\w+)\s*=\s*")
PDF_META_RE = re.compile(
    r"""<meta[^>]+name=["']citation_pdf_url["'][^>]*content=["']([^"']+)["']"""
    r"""|<meta[^>]+content=["']([^"']+)["'][^>]*name=["']citation_pdf_url["']""",
    re.I)


def read_value(text, i):
    """The field value starting at text[i]: {braced}, "quoted" or bare. Returns (value, end)."""
    if text[i] == "{":
        depth, j = 0, i
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    return text[i + 1:j], j + 1
            j += 1
        return text[i + 1:], len(text)
    if text[i] == '"':
        j = text.index('"', i + 1)
        return text[i + 1:j], j + 1
    m = re.match(r"[^,}\s]+", text[i:])
    return m.group(0), i + m.end()


def entries():
    """[(key, {field: value})] in file order; @string/@comment/@preamble skipped."""
    text = open(BIB, encoding="utf-8").read()
    starts = [(m.start(), m.group(1).lower(), m.group(2), m.end()) for m in ENTRY_RE.finditer(text)]
    out = []
    for n, (start, kind, key, body) in enumerate(starts):
        if kind in ("string", "comment", "preamble"):
            continue
        end = starts[n + 1][0] if n + 1 < len(starts) else len(text)
        chunk, fields, i = text[body:end], {}, 0
        while True:
            m = FIELD_RE.search(chunk, i)
            if not m or m.end() >= len(chunk):
                break
            value, i = read_value(chunk, m.end())
            fields[m.group(1).lower()] = " ".join(value.split())
        out.append((key, fields))
    return out


def candidates(f):
    """The links to try for one entry, best first, without duplicates."""
    urls = []
    eprint = f.get("eprint", "")
    kind = (f.get("eprinttype") or f.get("archiveprefix") or "").lower()
    if eprint and (kind == "arxiv" or re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", eprint)):
        urls.append(("eprint", "https://arxiv.org/pdf/" + eprint))
    if f.get("url"):
        urls.append(("url", f["url"].replace(r"\_", "_").replace(r"\%", "%").replace(r"\#", "#")))
    if f.get("doi"):
        doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", f["doi"], flags=re.I)
        urls.append(("doi", "https://doi.org/" + doi))
    seen, unique = set(), []
    for src, u in urls:
        if u not in seen:
            seen.add(u)
            unique.append((src, u))
    return unique


_host_lock = threading.Lock()
_host_next = {}


def wait_for_host(url):
    host = urllib.parse.urlsplit(url).netloc.lower()
    with _host_lock:
        now = time.monotonic()
        at = max(now, _host_next.get(host, 0.0))
        _host_next[host] = at + HOST_GAP
    if at > now:
        time.sleep(at - now)


def get(url):
    """(final_url, media_type, body) or raises."""
    wait_for_host(url)
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        body = r.read(MAX_BYTES + 1)
        if len(body) > MAX_BYTES:
            raise ValueError("larger than %d MB" % (MAX_BYTES >> 20))
        media = (r.headers.get_content_type() or "").lower()
        return r.geturl(), media, body


def is_pdf(media, body):
    return body[:5] == b"%PDF-" or (media == "application/pdf" and len(body) > 1000)


def visible_text(page):
    page = re.sub(r"(?is)<(script|style|noscript|header|footer|nav)\b.*?</\1>", " ", page)
    return " ".join(html.unescape(re.sub(r"(?s)<[^>]+>", " ", page)).split())


def fetch(key, f):
    """(ok, url, ext, body, why) for one entry."""
    tried = candidates(f)
    if not tried:
        return False, "none", None, None, "no link in refs.bib"
    why = []
    for src, url in tried:
        try:
            final, media, body = get(url)
        except (urllib.error.URLError, OSError, ValueError) as e:
            why.append("%s: %s" % (src, getattr(e, "code", None) or e))
            continue
        if is_pdf(media, body):
            return True, url, ".pdf", body, ""
        if media in ("text/html", "application/xhtml+xml"):
            page = body.decode("utf-8", "replace")
            m = PDF_META_RE.search(page)
            if m:
                pdf = urllib.parse.urljoin(final, html.unescape(m.group(1) or m.group(2)))
                try:
                    _, pmedia, pbody = get(pdf)
                    if is_pdf(pmedia, pbody):
                        return True, pdf, ".pdf", pbody, ""
                    why.append("%s: citation_pdf_url gave %s" % (src, pmedia or "?"))
                except (urllib.error.URLError, OSError, ValueError) as e:
                    why.append("%s: citation_pdf_url: %s" % (src, getattr(e, "code", None) or e))
            if src == "doi":
                why.append("doi: landing page, no PDF")
                continue
            n = len(visible_text(page))
            if n >= MIN_TEXT:
                return True, url, "web", body, ""
            why.append("%s: page has %d characters of text" % (src, n))
            continue
        ext = mimetypes.guess_extension(media) or ".bin"
        if len(body) > 1000:
            return True, url, ext, body, ""
        why.append("%s: %s, %d bytes" % (src, media or "?", len(body)))
    return False, tried[0][1], None, None, "; ".join(why)


def find_chrome(given):
    if given:
        return given
    for name in CHROME_NAMES:
        if shutil.which(name):
            return shutil.which(name)
    for path in CHROME_PATHS:
        if os.access(path, os.X_OK):
            return path
    return None


def browser_flags():
    # Chrome refuses to start sandboxed as root, which is how containers run.
    return ["--no-sandbox"] if hasattr(os, "geteuid") and os.geteuid() == 0 else []


def run(cmd):
    """True if cmd exits 0 within RENDER_TIMEOUT."""
    try:
        r = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                           timeout=RENDER_TIMEOUT)
        return r.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def save_web(url, raw, stem, chrome, single_file):
    """Write stem.pdf and stem.html (or stem.raw.html). Returns the names written."""
    wrote = []
    with RENDERERS:
        if chrome:
            pdf = stem + ".pdf"
            with tempfile.TemporaryDirectory() as profile:
                if run([chrome, "--headless=new", "--disable-gpu", *browser_flags(),
                        "--user-data-dir=" + profile, "--no-pdf-header-footer",
                        "--run-all-compositor-stages-before-draw", "--virtual-time-budget=15000",
                        "--print-to-pdf=" + pdf, url]) and os.path.getsize(pdf) > 1000:
                    wrote.append(os.path.basename(pdf))
                elif os.path.exists(pdf):
                    os.remove(pdf)
        if single_file:
            page = stem + ".html"
            cmd = [single_file, url, page]
            if chrome:
                cmd += ["--browser-executable-path=" + chrome]
            if browser_flags():
                cmd += ['--browser-args=["--no-sandbox"]']
            if run(cmd) and os.path.exists(page) and os.path.getsize(page) > 1000:
                wrote.append(os.path.basename(page))
                return wrote
            if os.path.exists(page):
                os.remove(page)
    with open(stem + ".raw.html", "wb") as fh:
        fh.write(raw)
    wrote.append(os.path.basename(stem) + ".raw.html")
    return wrote


def write_list(path, rows):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join("@%s\n%s\n" % r for r in rows))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--only", nargs="+", metavar="KEY", help="just these entries")
    ap.add_argument("--limit", type=int, help="the first N entries only")
    ap.add_argument("--out", default=OUT, help="output directory (default %(default)s)")
    ap.add_argument("--workers", type=int, default=8, help="parallel fetches (default 8)")
    ap.add_argument("--keep", action="store_true", help="keep the folder after zipping it")
    ap.add_argument("--chrome", help="Chrome or Chromium executable (default: looked for)")
    ap.add_argument("--single-file", help="single-file-cli executable (default: `single-file` on PATH)")
    a = ap.parse_args()

    chrome = find_chrome(a.chrome)
    single_file = a.single_file or shutil.which("single-file")
    print("web pages: PDF by %s; HTML by %s" % (
        chrome or "nobody (no Chrome found; pass --chrome)",
        single_file or "nobody (no single-file found; pages saved as fetched, .raw.html)"))

    todo = entries()
    if a.only:
        unknown = set(a.only) - {k for k, _ in todo}
        if unknown:
            sys.exit("not in refs.bib: " + " ".join(sorted(unknown)))
        todo = [(k, f) for k, f in todo if k in a.only]
    if a.limit:
        todo = todo[:a.limit]

    out = os.path.abspath(a.out)
    folder = os.path.join(out, "successfully-retrieved")
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

    def one(key, f):
        ok, url, ext, body, why = fetch(key, f)
        files = []
        if ok and ext == "web":
            files = save_web(url, body, os.path.join(folder, key), chrome, single_file)
        elif ok:
            with open(os.path.join(folder, key + ext), "wb") as fh:
                fh.write(body)
            files = [key + ext]
        return ok, url, files, why

    results = {}
    with concurrent.futures.ThreadPoolExecutor(a.workers) as pool:
        jobs = {pool.submit(one, k, f): k for k, f in todo}
        for n, job in enumerate(concurrent.futures.as_completed(jobs), 1):
            key = jobs[job]
            ok, url, files, why = job.result()
            results[key] = (ok, url)
            print("%4d/%d  %s  %s  %s" % (n, len(todo), "ok  " if ok else "FAIL", key,
                                          " ".join(files) if ok else "(" + why + ")"), flush=True)

    order = [k for k, _ in todo]
    good = [(k, results[k][1]) for k in order if results[k][0]]
    bad = [(k, results[k][1]) for k in order if not results[k][0]]
    write_list(os.path.join(out, "successfully-retrieved.txt"), good)
    write_list(os.path.join(out, "failed-retrieval.txt"), bad)

    zpath = os.path.join(out, "successfully-retrieved_%s.zip" % datetime.date.today().isoformat())
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(os.listdir(folder)):
            z.write(os.path.join(folder, name), os.path.join("successfully-retrieved", name))
    if not a.keep:
        shutil.rmtree(folder)

    print("\n%d retrieved, %d failed, of %d entries" % (len(good), len(bad), len(todo)))
    print("wrote", zpath)
    print("wrote", os.path.join(out, "successfully-retrieved.txt"))
    print("wrote", os.path.join(out, "failed-retrieval.txt"))


if __name__ == "__main__":
    main()
