#!/usr/bin/env bash
# Build the Ukrainian edition: lualatex -> biber -> lualatex x2, from
# manuscript/uk/book.tex, run from manuscript/ so its \input paths are the
# English build's. Regenerates uk/sections.tex first. Untranslated sections are
# set in English, so the edition always builds whole.
set -euo pipefail
repo="$(git rev-parse --show-toplevel)"; cd "$repo"

TEXLIVE_BIN="${TEXLIVE_BIN:-$HOME/texlive/2026/bin/x86_64-linux}"
export PATH="$TEXLIVE_BIN:$PATH"
command -v lualatex >/dev/null || { echo "lualatex not on PATH (looked in $TEXLIVE_BIN)"; exit 1; }
command -v biber    >/dev/null || { echo "biber not on PATH (looked in $TEXLIVE_BIN)"; exit 1; }

python3 finishing/tools/uk_edition.py >/dev/null

out="${1:-${TMPDIR:-/tmp}/es-build-uk}"
mkdir -p "$out"
out="$(cd "$out" && pwd)"

cd "$repo/manuscript"
run() { lualatex -interaction=nonstopmode -halt-on-error -jobname=book -output-directory="$out" uk/book.tex >/dev/null; }
run
biber --input-directory "$out" --output-directory "$out" book >/dev/null
run
run

pages=$(pdfinfo "$out/book.pdf" 2>/dev/null | awk '/^Pages:/{print $2}' || true)
echo "built $out/book.pdf (${pages:-?} pages)"
python3 "$repo/finishing/tools/uk_edition.py" --stale

if grep -q "undefined" "$out/book.log"; then
  echo "WARNING: undefined references or citations:"
  grep -n "undefined" "$out/book.log" | head -20
fi
