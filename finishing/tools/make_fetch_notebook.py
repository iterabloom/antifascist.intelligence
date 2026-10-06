#!/usr/bin/env python3
"""Write finishing/fetch_sources.ipynb, the Google Colab form of fetch_sources.py.

The notebook carries fetch_sources.py inside it (a %%writefile cell), so it
runs from Colab with nothing but refs.bib uploaded. That copy is this
directory's fetch_sources.py at the time this was run: edit the script, then
run this again. Editing the notebook's copy by hand is lost the next time.

    make_fetch_notebook.py            write it
    make_fetch_notebook.py --check    exit 1 if it is stale
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "fetch_sources.py")
NOTEBOOK = os.path.join(os.path.dirname(HERE), "fetch_sources.ipynb")

INTRO = """\
# Retrieve the bibliography's full texts

For each entry in `refs.bib` this tries the arXiv eprint, the `url`, then the
`doi`, and keeps the first full text:

- **a PDF**, saved as `KEY.pdf`, following a publisher page's
  `citation_pdf_url` where there is one;
- **a web page**, from a `url` field and with at least 2,000 characters of
  text, saved twice: `KEY.pdf`, printed by headless Chromium, and `KEY.html`,
  one self-contained file made by SingleFile (`single-file-cli`, the
  command-line build of the Chrome extension).

A DOI that lands on an abstract page, and an entry with no link, are failures.

**What you get:** `successfully-retrieved_<date>.zip`, and two lists,
`successfully-retrieved.txt` and `failed-retrieval.txt`, each `@key` then the
URL. They download at the end, and can be copied to Google Drive.

**Run the cells in order.** Setup takes a few minutes; the full run takes
much longer (two seconds between requests to any one site, and a browser
render for every web page). Try `LIMIT = 20` first.

**While it runs**, every 30 seconds it prints what is still in progress, at
which step and for how long. Nothing can run unbounded: a download gives up
after 120 seconds, a browser render after 120. **To stop it**, use the cell's
stop button: the run ends, and the two lists keep every entry that finished.
**To carry on**, set `RESUME = True` and run the Retrieve cell again; it skips
every key already in either list.

**Expect more failures than from a home connection.** Many publishers refuse
requests from cloud addresses like Colab's.

**The zip holds other people's copyrighted work.** It is for your reading. Keep
it out of the public repository."""

SETTINGS = """\
# Settings
LIMIT = None        # e.g. 20 to try the first 20 entries; None for all
ONLY = []           # e.g. ["abraham2024lavender"] to fetch just these keys
WORKERS = 8         # parallel fetches
REFS_BIB_URL = ""   # a raw URL for refs.bib; leave "" to upload the file
SAVE_TO_DRIVE = False  # also copy the results to My Drive/source-texts/
RESUME = False      # True: carry on from a stopped run, skipping keys already done"""

SETUP = """\
%%bash
# Chromium (prints the PDFs, and drives SingleFile), with its system libraries
set -e
pip install -q playwright
python -m playwright install --with-deps chromium > /tmp/playwright-install.log 2>&1 \\
  || { tail -20 /tmp/playwright-install.log; exit 1; }

# Node 22 or later for single-file-cli
major=$(node -v 2>/dev/null | sed 's/^v\\([0-9]*\\).*/\\1/')
if [ -z "$major" ] || [ "$major" -lt 22 ]; then
  curl -fsSL https://deb.nodesource.com/setup_22.x | bash - > /dev/null
  apt-get install -y -qq nodejs > /dev/null
fi
echo "node $(node -v)"

# single-file-cli, in /content/sf, pinned to the version this was tested with.
# Version 2 asks for Node 24; on 22 it lacks only the global CloseEvent, which
# the shim below supplies (a no-op on 24).
mkdir -p /content/sf && cd /content/sf
[ -f package.json ] || npm init -y > /dev/null
npm install -q --no-audit --no-fund single-file-cli@2.0.83 > /dev/null
cat > closeevent.mjs <<'EOF'
if (typeof globalThis.CloseEvent === "undefined") {
  globalThis.CloseEvent = class CloseEvent extends Event {
    constructor(type, init = {}) {
      super(type, init);
      this.code = init.code ?? 0; this.reason = init.reason ?? ""; this.wasClean = init.wasClean ?? false;
    }
  };
}
EOF
cat > single-file <<'EOF'
#!/bin/sh
exec node --import /content/sf/closeevent.mjs /content/sf/node_modules/single-file-cli/single-file-node.js "$@"
EOF
chmod +x single-file
echo "single-file-cli $(node -p "require('/content/sf/node_modules/single-file-cli/package.json').version")"
echo "setup done\""""

BIB = """\
# refs.bib: fetched from REFS_BIB_URL, or uploaded
import os, urllib.request
os.chdir("/content")
if REFS_BIB_URL:
    urllib.request.urlretrieve(REFS_BIB_URL, "refs.bib")
else:
    from google.colab import files
    print("Choose finishing/refs.bib from your copy of the repository.")
    up = files.upload()
    name = next(iter(up))
    if name != "refs.bib":
        os.replace(name, "refs.bib")
n = open("refs.bib", encoding="utf-8").read().count("\\n@")
print("refs.bib:", os.path.getsize("refs.bib"), "bytes, about", n, "entries")"""

RUN = """\
# Run it
import shlex, subprocess, sys
chrome = subprocess.run(
    [sys.executable, "-c",
     "from playwright.sync_api import sync_playwright as s; p = s().start(); "
     "print(p.chromium.executable_path); p.stop()"],
    capture_output=True, text=True, check=True).stdout.strip()
args = ["--bib", "/content/refs.bib", "--out", "/content/source-texts",
        "--chrome", chrome, "--single-file", "/content/sf/single-file",
        "--workers", str(WORKERS)]
if LIMIT:
    args += ["--limit", str(LIMIT)]
if ONLY:
    args += ["--only", *ONLY]
if RESUME:
    args += ["--resume"]
print("python fetch_sources.py", " ".join(shlex.quote(a) for a in args), "\\n")
p = subprocess.Popen([sys.executable, "-u", "/content/fetch_sources.py", *args],
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
try:
    for line in p.stdout:
        print(line, end="")
except KeyboardInterrupt:
    # The stop button interrupts this cell, not the script; pass it on, so the
    # script kills its browsers and exits, rather than running on unseen.
    p.terminate()
    for line in p.stdout:
        print(line, end="")
print("exit", p.wait())"""

GET = """\
# Download the results (and copy them to Drive if SAVE_TO_DRIVE)
import glob, os, shutil
out = "/content/source-texts"
results = sorted(glob.glob(out + "/successfully-retrieved_*.zip"))[-1:] + [
    out + "/successfully-retrieved.txt", out + "/failed-retrieval.txt"]
if SAVE_TO_DRIVE:
    from google.colab import drive
    drive.mount("/content/drive")
    dest = "/content/drive/MyDrive/source-texts"
    os.makedirs(dest, exist_ok=True)
    for f in results:
        shutil.copy(f, dest)
    print("copied to My Drive/source-texts/:", ", ".join(os.path.basename(f) for f in results))
from google.colab import files
for f in results:
    files.download(f)"""


def cell(kind, text):
    lines = text.split("\n")
    src = [l + "\n" for l in lines[:-1]] + [lines[-1]]
    c = {"cell_type": kind, "metadata": {}, "source": src}
    if kind == "code":
        c.update(execution_count=None, outputs=[])
    return c


def notebook():
    script = open(SCRIPT, encoding="utf-8").read().rstrip("\n")
    cells = [
        cell("markdown", INTRO),
        cell("code", SETTINGS),
        cell("markdown", "## Setup: Chromium, Node and SingleFile"),
        cell("code", SETUP),
        cell("markdown", "## The script\n\n`fetch_sources.py` from the repository, written to `/content`."),
        cell("code", "%%writefile /content/fetch_sources.py\n" + script),
        cell("markdown", "## The bibliography"),
        cell("code", BIB),
        cell("markdown", "## Retrieve"),
        cell("code", RUN),
        cell("markdown", "## Results"),
        cell("code", GET),
    ]
    nb = {"cells": cells, "metadata": {
        "colab": {"provenance": [], "name": "fetch_sources.ipynb"},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"}},
        "nbformat": 4, "nbformat_minor": 0}
    return json.dumps(nb, indent=1, ensure_ascii=False) + "\n"


def main():
    text = notebook()
    if "--check" in sys.argv[1:]:
        current = os.path.exists(NOTEBOOK) and open(NOTEBOOK, encoding="utf-8").read() == text
        print("fetch_sources.ipynb", "current" if current else "STALE: run make_fetch_notebook.py")
        sys.exit(0 if current else 1)
    with open(NOTEBOOK, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote", os.path.relpath(NOTEBOOK, os.getcwd()))


if __name__ == "__main__":
    main()
