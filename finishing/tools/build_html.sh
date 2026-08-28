#!/usr/bin/env bash
# Build the HTML proof: make4ht (tex4ht) over the same manuscript/book.tex the
# PDF is built from, then assembled into one self-contained file.
#
# The PDF is the typeset book; this is the book to read in a browser, search
# with ctrl-F, and follow by link -- every section~\ref becomes an anchor and
# every \autocite a jump to its bibliography entry. It is not a page proof:
# there are no pages in it, so nothing about widows, breaks, or the shape of a
# page can be judged here. Use build_tex.sh for that.
#
# Same TeX Live as build_tex.sh; set TEXLIVE_BIN to override.
set -euo pipefail
repo="$(git rev-parse --show-toplevel)"; cd "$repo"

TEXLIVE_BIN="${TEXLIVE_BIN:-$HOME/texlive/2026/bin/x86_64-linux}"
export PATH="$TEXLIVE_BIN:$PATH"
command -v make4ht >/dev/null || { echo "make4ht not on PATH (looked in $TEXLIVE_BIN)"; exit 1; }
command -v biber   >/dev/null || { echo "biber not on PATH (looked in $TEXLIVE_BIN)"; exit 1; }

out="${1:-${TMPDIR:-/tmp}/es-build}"
mkdir -p "$out"
out="$(cd "$out" && pwd)"

# make4ht scatters roughly a dozen intermediate files -- .4ct, .idv, .lg, .xref
# and the rest -- so it gets its own directory, and only the finished page is
# lifted out of it. html.mk4 reads this to tell biber where the aux files are.
build="$out/html-build"
rm -rf "$build"; mkdir -p "$build"
export ES_BUILD_DIR="$build"

cd "$repo/manuscript"
make4ht -l -a status -B "$build" -e "$repo/finishing/tools/html.mk4" \
        -f html5 book.tex "" "" "" "-interaction=nonstopmode" > "$build/make4ht.out" 2>&1 || {
  echo "make4ht failed; last lines of its output:"; tail -20 "$build/make4ht.out"; exit 1; }

# lualatex exits 0 on undefined references, so check the log the way
# build_tex.sh does rather than trusting the exit status.
if grep -q "^! " "$build/book.log"; then
  echo "LaTeX errors in the tex4ht run:"; grep -n -A4 "^! " "$build/book.log" | head -40; exit 1
fi
if grep -q "undefined" "$build/book.log"; then
  echo "WARNING: undefined references or citations:"
  grep -n "undefined" "$build/book.log" | head -20
fi
# tex4ht rasterizes anything it cannot set as text, which a single file cannot
# carry. Nothing in this book needs it, so a request here means something new
# was written that tex4ht does not understand -- see pipeline.md.
if grep -q -- "--- needs ---" "$build/book.lg"; then
  echo "tex4ht wants to make an image, which the single-file page cannot hold:"
  grep -- "--- needs ---" "$build/book.lg"; exit 1
fi

cd "$repo"
python3 finishing/tools/html_single_file.py "$build" "$out/book.html"
