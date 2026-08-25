#!/usr/bin/env bash
# Build the book: lualatex -> biber -> lualatex x2, from manuscript/book.tex.
#
# TeX Live lives under $HOME (there is no root on this machine, so it was
# installed user-space rather than from apt). Set TEXLIVE_BIN to override.
set -euo pipefail
repo="$(git rev-parse --show-toplevel)"; cd "$repo"

TEXLIVE_BIN="${TEXLIVE_BIN:-$HOME/texlive/2026/bin/x86_64-linux}"
export PATH="$TEXLIVE_BIN:$PATH"
command -v lualatex >/dev/null || { echo "lualatex not on PATH (looked in $TEXLIVE_BIN)"; exit 1; }
command -v biber    >/dev/null || { echo "biber not on PATH (looked in $TEXLIVE_BIN)"; exit 1; }

out="${1:-${TMPDIR:-/tmp}/es-build}"
mkdir -p "$out"
out="$(cd "$out" && pwd)"

# -output-directory keeps aux files out of the source tree; the source stays
# manuscript/book.tex so \input paths resolve relative to manuscript/.
cd "$repo/manuscript"
run() { lualatex -interaction=nonstopmode -halt-on-error -output-directory="$out" book.tex >/dev/null; }
run
biber --input-directory "$out" --output-directory "$out" book >/dev/null
run
run

pages=$(pdfinfo "$out/book.pdf" 2>/dev/null | awk '/^Pages:/{print $2}' || true)
echo "built $out/book.pdf (${pages:-?} pages)"

# Undefined citations and references are warnings, not errors, so lualatex
# exits 0 on them. Surface them here or they go unnoticed.
if grep -q "undefined" "$out/book.log"; then
  echo "WARNING: undefined references or citations:"
  grep -n "undefined" "$out/book.log" | head -20
fi
