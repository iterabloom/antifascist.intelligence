#!/usr/bin/env bash
# Regenerate the whole-book proof, both formats, into finishing/reports/.
#
# The repository carries a readable copy of the book and not only its sources:
# a PDF, which is the typeset book, and an HTML file, which is the book to read
# in a browser and search. They are generated together so the pair cannot drift
# apart -- an HTML proof a week older than the PDF beside it would be worse
# than none, because nothing about it would say so.
#
# Usage: build_proof.sh [DATE]     # DATE defaults to today, as YYYY-MM-DD
set -euo pipefail
repo="$(git rev-parse --show-toplevel)"; cd "$repo"

date="${1:-$(date +%F)}"
[[ "$date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || { echo "not a YYYY-MM-DD date: $date"; exit 1; }

scratch="${TMPDIR:-/tmp}/es-proof"
rm -rf "$scratch"; mkdir -p "$scratch/pdf" "$scratch/html"

finishing/tools/build_tex.sh  "$scratch/pdf"
finishing/tools/build_html.sh "$scratch/html"

stem="finishing/reports/whole-book-proof_$date"
cp "$scratch/pdf/book.pdf"   "$stem.pdf"
cp "$scratch/html/book.html" "$stem.html"
echo
echo "wrote $stem.pdf  ($(du -h "$stem.pdf"  | cut -f1))"
echo "wrote $stem.html ($(du -h "$stem.html" | cut -f1))"

# The proof is one pair, replaced each time, not a series. Say what is left
# over rather than delete it: removing a committed file is the author's call.
old=$(ls finishing/reports/whole-book-proof_* 2>/dev/null | grep -v "^$stem\." || true)
if [ -n "$old" ]; then
  echo
  echo "earlier proofs still present -- remove them in the same commit:"
  echo "$old" | sed 's/^/  git rm /'
fi
