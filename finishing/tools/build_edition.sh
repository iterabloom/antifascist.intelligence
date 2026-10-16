#!/usr/bin/env bash
# Build one translated edition: lualatex -> biber -> lualatex x2, from
# manuscript/<code>/book.tex, run from manuscript/ so its \input paths are the
# English build's. Regenerates the edition's sections.tex and status.tex first.
# Untranslated and stale sections are set in English, so an edition always
# builds whole.
#
# Usage: build_edition.sh CODE [OUTDIR]      # OUTDIR defaults to /tmp/es-build-CODE
set -euo pipefail
repo="$(git rev-parse --show-toplevel)"; cd "$repo"
code="${1:?usage: build_edition.sh CODE [OUTDIR]}"
[ -f "manuscript/$code/book.tex" ] || { echo "no edition: manuscript/$code/book.tex"; exit 1; }

TEXLIVE_BIN="${TEXLIVE_BIN:-$HOME/texlive/2026/bin/x86_64-linux}"
export PATH="$TEXLIVE_BIN:$PATH"
command -v lualatex >/dev/null || { echo "lualatex not on PATH (looked in $TEXLIVE_BIN)"; exit 1; }
command -v biber    >/dev/null || { echo "biber not on PATH (looked in $TEXLIVE_BIN)"; exit 1; }

python3 finishing/tools/editions.py --lang "$code" >/dev/null

out="${2:-${TMPDIR:-/tmp}/es-build-$code}"
mkdir -p "$out"
out="$(cd "$out" && pwd)"

cd "$repo/manuscript"
run() { lualatex -interaction=nonstopmode -halt-on-error -jobname=book -output-directory="$out" "$code/book.tex" >/dev/null; }
run
biber --input-directory "$out" --output-directory "$out" book >/dev/null
run
run

pages=$(pdfinfo "$out/book.pdf" 2>/dev/null | awk '/^Pages:/{print $2}' || true)
echo "built $out/book.pdf (${pages:-?} pages)"
python3 "$repo/finishing/tools/editions.py" --lang "$code" --stale

# Not a bare "undefined": an edition's face may lack small caps, and the font
# warning that says so would set this off on every build.
pat="Reference .* undefined|Citation .* undefined|There were undefined"
if grep -Eq "$pat" "$out/book.log"; then
  echo "WARNING: undefined references or citations:"
  grep -En "$pat" "$out/book.log" | head -20
fi
