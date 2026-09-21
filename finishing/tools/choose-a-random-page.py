#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""One random page of the book, rendered as markdown, for a before/after revision pass.

The LaTeX is the source of truth. Nothing here reads the built PDF except for
its page count, and nothing reads the retired dialect texts.

WHAT IT DOES

  1. Builds the whole book as one ordered stream of units -- headings, run-in
     heads, paragraphs, epigraphs, lists, boxes, the one table -- by walking
     `manuscript/sections/ORDER.tsv` and parsing each `.tex` file.
  2. Picks a location at random and snaps it back to the heading at or before
     it, so a page always opens on the first word of a heading. Snapping is
     what keeps the sample uniform over the BOOK rather than over the headings:
     the glossary holds 56 of the manuscript's 194 run-in heads in 3 percent of
     its words, and drawing from the headings directly would send one sample in
     six there. `--uniform-headings` draws from the headings instead, and
     `--no-runins` drops run-in heads from the pool either way.
  3. Estimates the page number by cross-product:
         page = round(start_word / total_words * total_pages)
     clamped into [1, total_pages].

     HOW WRONG IT IS, MEASURED. Against the 2026-08-29 proof, over 111 samples
     located in the PDF's text layer by their opening sentence: median error 18
     pages, maximum 31, and the estimate runs high everywhere but the first few
     pages. The cause is the two ends of the book that hold no words this script
     counts. The proof's 192 pages are 5 of front matter, body text on 6 to 162,
     and References on 163 to 192; the cross-product stretches 96,739 words of
     body text across all 192 anyway. Passing `--pages 157`, the span the body
     text actually occupies, takes the same formula to a median of 4 and a
     maximum of 7, the residue being the five front-matter pages. The default is
     the whole book because that is what "the total page count" means, and the
     number is a name for a file rather than a citation. Re-measure after a
     rebuild rather than trusting these figures: they are properties of one
     proof.
  4. Emits `words_per_page = round(total_words / total_pages)` words from that
     heading onward, to `~/book-scratch/random-pages/page-N-before.md`.
  5. Copies each `page-N-before.md` to `page-N-after.md` where the latter is
     missing, and leaves every existing one alone.

WHAT COUNTS AS A WORD

  Every word a reader sees, in ORDER.tsv order: heading titles, run-in heads,
  prose, epigraphs, list items, box text, table cells. Citation commands are
  preserved in the output but excluded from the count, which is the convention
  `finishing/tools/common.py` states for the same reason -- `\\autocite{key}`
  is apparatus, and the year inside a key like `piaget1932moral` is not prose.

  This total is therefore LARGER than the 95,405 that `section_stats.py`
  reports, because that tool excludes headings and epigraphs by design. The
  two answer different questions; every generated file's header prints the
  number this script actually used.

OVERLAP

  Before writing, the first two items of the candidate page are checked against
  every item in every other `*.md` in the output folder. An item is a heading
  line or a sentence, compared after normalization (case, whitespace,
  punctuation, markdown emphasis). A heading counts as an item because a
  re-drawn heading is the strongest single sign that a page has been sampled
  before. Any match means resample; `--attempts` (default 5) tries, then the
  script gives up on the sample, still reconciles the before/after pairs, and
  exits 1.

  An existing `page-N-before.md` is also treated as a collision and costs an
  attempt, because two different starting points can estimate to the same page
  and overwriting would strand an `-after` file the author may already have
  edited. `--force` overwrites instead.

USAGE

  finishing/tools/choose-a-random-page.py [--out-dir DIR] [--pages N]
                                          [--seed S] [--attempts N]
                                          [--no-runins] [--uniform-headings]
                                          [--force]
"""
import argparse
import bisect
import os
import random
import re
import shutil
import subprocess
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402  (needs the path set first)

DEFAULT_OUT = os.path.join(os.path.expanduser("~"), "book-scratch", "random-pages")
PROOF_PREFIX = "whole-book-proof_"


# --- LaTeX to markdown ----------------------------------------------------
#
# The manuscript uses twenty commands in total, which is why this is a reader
# rather than a parser. If a new one appears it is reported, not swallowed:
# its argument is kept and its name is printed as a warning.

_CMD = re.compile(r"\\([A-Za-z]+)\*?")
_ESCAPED = re.compile(r"\\([&%$#_{}^~])")
_LINEBREAK = re.compile(r"\\\\(\[[^\]]*\])?")
_REF = re.compile(r"\\ref\{sec:([^}]*)\}")

MD_DROP_WITH_ARGS = ("label", "unnumberedlabel", "addcontentsline", "input",
                     "index", "nocite", "rule")
MD_DROP_BARE = ("small", "itshape", "bfseries", "par", "noindent", "medskip",
                "smallskip", "bigskip", "nopagebreak", "centering", "hline",
                "linewidth")
MD_EMPH = {"emph": "*", "textit": "*", "textbf": "**"}
MD_VERBATIM = ("autocite", "cite")       # apparatus: printed as written, not counted
MD_ARG_ONLY = ("runin", "boxtitle", "text")


def md_inline(latex, unknown=None):
    """One line or paragraph of LaTeX as markdown. A \\ref prints its number."""
    s = _REF.sub(lambda m: m.group(1), latex)
    out, i = [], 0
    while i < len(s):
        if s.startswith("\\\\", i):
            out.append("\n")
            i = _LINEBREAK.match(s, i).end()
            continue
        e = _ESCAPED.match(s, i)
        if e:
            out.append(e.group(1))
            i = e.end()
            continue
        m = _CMD.match(s, i)
        if not m:
            out.append(" " if s[i] == "~" else s[i])
            i += 1
            continue
        name, i = m.group(1), m.end()
        if name in ("begin", "end"):
            _, i = common._take_arg(s, i)
        elif name in MD_DROP_WITH_ARGS:
            while i < len(s) and s[i] == "{":
                _, i = common._take_arg(s, i)
        elif name in MD_VERBATIM:
            arg, i = common._take_arg(s, i)
            out.append("\\%s{%s}" % (name, arg))
        elif name in MD_EMPH:
            arg, i = common._take_arg(s, i)
            mark = MD_EMPH[name]
            inner = md_inline(arg, unknown).strip()
            out.append("%s%s%s" % (mark, inner, mark) if inner else "")
        elif name in MD_ARG_ONLY:
            while i < len(s) and s[i] == "{":
                arg, i = common._take_arg(s, i)
                out.append(md_inline(arg, unknown))
        elif name in MD_DROP_BARE:
            pass
        else:
            if unknown is not None:
                unknown.add(name)
            while i < len(s) and s[i] == "{":
                arg, i = common._take_arg(s, i)
                out.append(md_inline(arg, unknown))
    return re.sub(r"[ \t]{2,}", " ", "".join(out)).strip()


_COUNT_DROP = re.compile(r"\\(?:autocite|cite)\{[^}]*\}")
_RULE_ROW = re.compile(r"^[\s|:\-]+$")


def count_words(md):
    """Words a reader would count in a block of this script's markdown."""
    s = _COUNT_DROP.sub(" ", md)
    lines = []
    for line in s.split("\n"):
        if _RULE_ROW.match(line):
            continue                      # a table's separator row
        line = re.sub(r"^[>#\s]+", "", line)
        line = re.sub(r"^(?:[-*+]|\d+\.)\s+", "", line)
        lines.append(line.replace("|", " "))
    return len(re.sub(r"[*_`]", "", "\n".join(lines)).split())


# --- Sentences ------------------------------------------------------------
#
# The splitter is deliberately conservative: where it cannot tell, it joins.
# An over-long "sentence" costs a page a few words; a split inside "U.S." or
# "e.g." would put a fragment into the overlap check and match nothing.

ABBREV = {"e.g", "i.e", "cf", "vs", "etc", "al", "dr", "mr", "mrs", "ms",
          "prof", "st", "no", "fig", "inc", "ltd", "jr", "sr", "ca", "ch",
          "pp", "p", "eds", "ed", "vol", "u.s", "u.k", "d.c"}
_BOUNDARY = re.compile(r"([.!?][”’\"')\]]*)(\s+)")
_NEXT_STARTS = re.compile(r"[A-Z“\"'(\*\d]")


def split_sentences(text):
    """The sentences of one paragraph of markdown."""
    text = text.strip()
    if not text:
        return []
    out, start = [], 0
    for m in _BOUNDARY.finditer(text):
        nxt = text[m.end():m.end() + 1]
        if not nxt or not _NEXT_STARTS.match(nxt):
            continue
        head = text[start:m.end(1)].rstrip()
        words = head.split()
        last = words[-1] if words else ""
        last = re.sub(r"^[^\w.]+|[”’\"')\]]+$", "", last).rstrip(".").lower()
        if last in ABBREV or re.fullmatch(r"[a-z]", last):
            continue                       # an abbreviation, or an initial
        out.append(head)
        start = m.end()
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    return out


# --- The book as one stream of units --------------------------------------

HEAD_LEVEL = {"chapter": 1, "section": 2, "subsection": 3}
HEAD_RE = re.compile(r"^\\(chapter|section|subsection)\*?(?:\[[^\]]*\])?\{(.*)\}\s*$")
RUNIN_RE = re.compile(r"^\\runin\{(.*)\}\s*$")
BOXTITLE_RE = re.compile(r"^\\boxtitle\{(.*)\}\s*$")
ENV_RE = re.compile(r"^\s*\\(begin|end)\{([A-Za-z*]+)\}")
MACHINERY_RE = re.compile(r"^\\(label|unnumberedlabel|addcontentsline)")

QUOTE_ENVS = ("verse", "flushright")
LIST_ENVS = ("itemize", "enumerate")


def join_parts(parts):
    """Parts are (separator-before, text); the first separator is unused."""
    if not parts:
        return ""
    return parts[0][1] + "".join(sep + text for sep, text in parts[1:])


class Unit(object):
    """A block of the book, plus the seams a page break may fall on.

    `parts` are those seams: the sentences of a paragraph, the sentences of
    each paragraph of a box, the items of a list, the lines of an epigraph.
    A page ends at the part that carries it past the target, so it overruns
    by at most one sentence. The one table is a single part and is taken
    whole, because half a table is not a page of a book.
    """

    __slots__ = ("kind", "parts", "words", "start", "num", "title", "path")

    def __init__(self, kind, parts, num=None, title=None, path=None):
        self.kind = kind        # heading | runin | para | epigraph | list | box | table
        self.parts = [(sep, text) for sep, text in parts if text.strip()]
        self.words = count_words(self.md)
        self.start = 0          # 1-based index of this unit's first word
        self.num = num
        self.title = title
        self.path = path

    @property
    def md(self):
        return join_parts(self.parts)

    @property
    def is_heading(self):
        return self.kind in ("heading", "runin")


def _render_table(rows, unknown):
    """The manuscript's one tabular, as a markdown table."""
    cells = []
    for raw in rows:
        raw = re.sub(r"\\hline", "", raw).strip()
        if not raw:
            continue
        for row in _LINEBREAK.split(raw):
            if row is None or row.startswith("["):
                continue                   # the [3pt] of a \\[3pt] row break
            row = row.strip()
            if row:
                cells.append([md_inline(c, unknown).strip() for c in row.split("&")])
    if not cells:
        return ""
    width = max(len(r) for r in cells)
    cells = [r + [""] * (width - len(r)) for r in cells]
    out = ["| " + " | ".join(cells[0]) + " |",
           "|" + "|".join([" --- "] * width) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in cells[1:]]
    return "\n".join(out)


def _quoted_parts(md, prefix=""):
    """A rendered paragraph as (separator, text) parts, one per sentence."""
    if "\n" in md:                         # explicit \\ breaks: a verse stanza
        return [("\n", prefix + line.strip()) for line in md.split("\n")]
    sentences = split_sentences(md)
    if not sentences:
        return []
    return ([(" ", prefix + sentences[0])] +
            [(" ", s) for s in sentences[1:]])


def parse_file(path, num, unknown):
    """A section .tex file as a list of Units, in reading order."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    units, buf, envs = [], [], []
    table, box, items = None, None, None

    def flush():
        """Close the open paragraph, if there is one."""
        if not buf:
            return
        text = " ".join(x.strip() for x in buf).strip()
        del buf[:]
        md = md_inline(text, unknown) if text else ""
        if not md:
            return
        if box is not None:
            box.append(md)
        elif items is not None:
            items.append(md)
        elif any(e in QUOTE_ENVS for e in envs):
            units.append(Unit("epigraph", _quoted_parts(md, "> "), path=path))
        else:
            units.append(Unit("para", [(" ", s) for s in split_sentences(md)],
                              path=path))

    for raw in lines:
        line = raw.rstrip()

        env = ENV_RE.match(line)
        if env:
            flush()
            which, name = env.group(1), env.group(2)
            if which == "begin":
                envs.append(name)
                if name == "tabular":
                    table = []
                elif name == "esbox":
                    box = []
                elif name in LIST_ENVS:
                    items = []
                continue
            if envs:
                envs.pop()
            if name == "tabular" and table is not None:
                md = _render_table(table, unknown)
                if md:
                    units.append(Unit("table", [("", md)], path=path))
                table = None
            elif name == "esbox" and box is not None:
                parts = []
                for para in box:
                    chunk = _quoted_parts(para, "> ")
                    if chunk:
                        parts.append(("\n>\n", chunk[0][1]))
                        parts.extend(chunk[1:])
                if parts:
                    units.append(Unit("box", parts, path=path))
                box = None
            elif name in LIST_ENVS and items is not None:
                mark = (lambda i: "%d." % (i + 1)) if name == "enumerate" \
                    else (lambda i: "-")
                rows = [("\n", "%s %s" % (mark(i), t)) for i, t in enumerate(items)]
                if rows:
                    units.append(Unit("list", rows, path=path))
                items = None
            continue

        if table is not None:
            table.append(line)
            continue

        h = HEAD_RE.match(line)
        if h:
            flush()
            title = md_inline(h.group(2), unknown)
            hashes = "#" * HEAD_LEVEL[h.group(1)]
            units.append(Unit(
                "heading",
                [("", "%s %s" % (hashes, common.heading_line(num, title)))],
                num=num, title=title, path=path))
            continue

        r = RUNIN_RE.match(line)
        if r:
            flush()
            title = md_inline(r.group(1), unknown)
            units.append(Unit("runin", [("", "#### " + title)],
                              num=num, title=title, path=path))
            continue

        b = BOXTITLE_RE.match(line)
        if b and box is not None:
            flush()
            box.append("**%s**" % md_inline(b.group(1), unknown))
            continue

        if MACHINERY_RE.match(line):
            continue

        if re.match(r"^\s*\\item\b", line):
            flush()
            buf.append(re.sub(r"^\s*\\item\s*", "", line))
            continue

        if not line.strip():
            flush()
            continue

        buf.append(line)

    flush()
    return units


def load_book(repo):
    """(units, unknown_commands) for the whole book, in ORDER.tsv order."""
    order = os.path.join(repo, "manuscript", "sections", "ORDER.tsv")
    _, rows = common.read_tsv(order)
    rows.sort(key=lambda r: common.numkey(r["num"]))
    units, unknown, at = [], set(), 1
    for r in rows:
        for u in parse_file(os.path.join(repo, r["path"]), r["num"], unknown):
            u.start = at
            at += u.words
            units.append(u)
    return units, unknown


# --- Overlap --------------------------------------------------------------

def normalize(s):
    """A sentence reduced to what two copies of it would share."""
    s = _COUNT_DROP.sub(" ", s)
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[*_`>#|]", " ", s)
    s = re.sub(r"[^\w\s]", "", s)
    return " ".join(s.lower().split())


def items_of(md, skip_front_matter=True):
    """Heading lines and sentences of a markdown page, in order.

    A heading is one item. Front matter is this script's own writing, not the
    book's, and is skipped on both sides of the comparison.
    """
    if skip_front_matter and md.startswith("---\n"):
        parts = md.split("\n---\n", 1)
        md = parts[1] if len(parts) == 2 else md
    out = []
    for line in md.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            out.append(line.lstrip("#").strip())
        else:
            out.extend(split_sentences(re.sub(r"^>\s?", "", line)))
    return [i for i in (normalize(x) for x in out) if i]


def existing_items(out_dir):
    """Every item in every markdown file already in the folder."""
    seen = set()
    if not os.path.isdir(out_dir):
        return seen
    for name in sorted(os.listdir(out_dir)):
        if name.endswith(".md"):
            with open(os.path.join(out_dir, name), encoding="utf-8") as f:
                seen.update(items_of(f.read()))
    return seen


# --- Assembling a page ----------------------------------------------------

def take_page(units, start_idx, target):
    """Units from start_idx forward until `target` words are reached."""
    blocks, n, i = [], 0, start_idx
    while i < len(units) and n < target:
        u = units[i]
        if n + u.words <= target:
            blocks.append(u.md)
            n += u.words
            i += 1
            continue
        kept = []
        for part in u.parts:
            kept.append(part)
            n += count_words(part[1])
            if n >= target:
                break
        if kept:
            blocks.append(join_parts(kept))
        i += 1
        break
    return blocks, n, i


def page_number(start_word, total_words, total_pages):
    n = int(round(float(start_word) / total_words * total_pages))
    return max(1, min(total_pages, n))


def proof_pages(repo, override=None):
    """The book's page count, from the newest committed proof PDF."""
    if override:
        return override, "--pages"
    reports = os.path.join(repo, "finishing", "reports")
    pdfs = sorted(n for n in os.listdir(reports)
                  if n.startswith(PROOF_PREFIX) and n.endswith(".pdf"))
    if not pdfs:
        sys.exit("no whole-book proof in finishing/reports/; "
                 "build one with build_proof.sh or pass --pages N")
    pdf = os.path.join(reports, pdfs[-1])
    try:
        out = subprocess.check_output(["pdfinfo", pdf]).decode("utf-8", "replace")
    except (OSError, subprocess.CalledProcessError) as exc:
        sys.exit("cannot read %s (%s); pass --pages N" % (pdfs[-1], exc))
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    if not m:
        sys.exit("pdfinfo reported no page count for %s; pass --pages N" % pdfs[-1])
    return int(m.group(1)), pdfs[-1]


def front_matter(page, unit, n_words, span, meta):
    return "\n".join([
        "---",
        "page: %d" % page,
        "estimated_from: word %d of %d, over %d pages (%s)"
        % (unit.start, meta["total_words"], meta["total_pages"], meta["pages_src"]),
        "starts_at: %s" % unit.md.lstrip("#").strip(),
        "source: %s" % os.path.relpath(unit.path, meta["repo"]),
        "words: %d (target %d)" % (n_words, meta["target"]),
        "spans: %d units" % span,
        "manuscript: %s" % meta["stamp"],
        "note: >-",
        "  Markdown rendered from the LaTeX by finishing/tools/choose-a-random-page.py.",
        "  Citation commands are printed as they appear in the source and are not",
        "  counted as words. The page number is a cross-product estimate over the",
        "  whole proof, which runs high by a median of 18 pages because the front",
        "  matter and the References hold none of the counted words. It is a name",
        "  for this file, not a location in the proof.",
        "---",
        "",
    ])


# --- The after-file reconciliation ----------------------------------------

BEFORE_RE = re.compile(r"^page-(\d+)-before\.md$")


def reconcile(out_dir):
    """Every page-N-before.md gets a page-N-after.md; existing ones are untouched."""
    made, kept = [], []
    for name in sorted(os.listdir(out_dir)):
        m = BEFORE_RE.match(name)
        if not m:
            continue
        after = "page-%s-after.md" % m.group(1)
        if os.path.exists(os.path.join(out_dir, after)):
            kept.append(after)
        else:
            shutil.copy2(os.path.join(out_dir, name), os.path.join(out_dir, after))
            made.append(after)
    return made, kept


def pick(rng, units, starts, uniform_headings, total_words):
    """A heading index: uniform over the headings, or over the book and snapped."""
    if uniform_headings:
        return rng.choice(starts)
    word = rng.randint(1, total_words)
    positions = [units[i].start for i in starts]
    return starts[max(0, bisect.bisect_right(positions, word) - 1)]


def main():
    ap = argparse.ArgumentParser(
        description="Write one random page of the book as markdown.")
    ap.add_argument("--out-dir", default=DEFAULT_OUT)
    ap.add_argument("--pages", type=int, default=None,
                    help="total page count; default is the committed proof PDF's. "
                         "157 -- the span the body text occupies in the "
                         "2026-08-29 proof -- is the more accurate estimator; "
                         "see the module docstring for the measurement")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--attempts", type=int, default=5)
    ap.add_argument("--no-runins", action="store_true",
                    help="start only at numbered headings, not at run-in heads")
    ap.add_argument("--uniform-headings", action="store_true",
                    help="draw from the headings rather than from the book's words")
    ap.add_argument("--force", action="store_true",
                    help="overwrite an existing page-N-before.md")
    args = ap.parse_args()

    repo = common.REPO
    out_dir = os.path.expanduser(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)

    units, unknown = load_book(repo)
    if unknown:
        print("warning: commands this script has not been taught, argument kept: %s"
              % ", ".join(sorted(unknown)), file=sys.stderr)

    total_words = sum(u.words for u in units)
    total_pages, pages_src = proof_pages(repo, args.pages)
    target = int(round(float(total_words) / total_pages))
    starts = [i for i, u in enumerate(units)
              if u.kind == "heading" or (u.kind == "runin" and not args.no_runins)]

    print("%d units, %d words, %d pages, %d words/page, %d possible starts"
          % (len(units), total_words, total_pages, target, len(starts)))

    rng = random.Random(args.seed)
    pool = existing_items(out_dir)
    stamp = subprocess.check_output(
        ["git", "-C", repo, "rev-parse", "--short", "HEAD"]).decode().strip()
    meta = {"repo": repo, "total_words": total_words, "total_pages": total_pages,
            "pages_src": pages_src, "target": target, "stamp": stamp}

    written = None
    for attempt in range(1, args.attempts + 1):
        idx = pick(rng, units, starts, args.uniform_headings, total_words)
        unit = units[idx]
        page = page_number(unit.start, total_words, total_pages)
        path = os.path.join(out_dir, "page-%d-before.md" % page)
        opener = unit.md.lstrip("#").strip()

        if os.path.exists(path) and not args.force:
            print("attempt %d: page-%d-before.md is already there; resampling (%s)"
                  % (attempt, page, opener))
            continue

        blocks, n_words, end = take_page(units, idx, target)
        body = "\n\n".join(blocks) + "\n"
        if [s for s in items_of(body, skip_front_matter=False)[:2] if s in pool]:
            print("attempt %d: page %d overlaps a page already in the folder; "
                  "resampling (%s)" % (attempt, page, opener))
            continue

        with open(path, "w", encoding="utf-8") as f:
            f.write(front_matter(page, unit, n_words, end - idx, meta) + body)
        written = (path, page, unit, n_words, end - idx, attempt)
        break

    if written:
        path, page, unit, n_words, span, attempt = written
        print("wrote %s" % path)
        print("  %s" % unit.md.lstrip("#").strip())
        print("  word %d of %d -> page %d of %d; %d words over %d units; attempt %d"
              % (unit.start, total_words, page, total_pages, n_words, span, attempt))
    else:
        print("gave up after %d attempt%s: every sample collided with a page "
              "already in %s"
              % (args.attempts, "" if args.attempts == 1 else "s", out_dir),
              file=sys.stderr)

    made, kept = reconcile(out_dir)
    print("after-files: %d copied%s, %d already there"
          % (len(made), (" (%s)" % ", ".join(made)) if made else "", len(kept)))

    return 0 if written else 1


if __name__ == "__main__":
    sys.exit(main())
