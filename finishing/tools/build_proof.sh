#!/usr/bin/env bash
# Regenerate the whole-book proof, both formats, into finishing/reports/, and,
# when asked, the proofs of translated editions.
#
# The repository carries a readable copy of the book and not only its sources:
# a PDF, which is the typeset book, and an HTML file, which is the book to read
# in a browser and search. They are generated together so the pair cannot drift
# apart -- an HTML proof a week older than the PDF beside it would be worse
# than none, because nothing about it would say so.
#
# Translated editions (manuscript/<code>/, D-808) are built only when named:
# "proofs please" is the English alone; "proofs please plus Ukrainian, French"
# is --langs uk,fr; "proofs please all languages" is --all-languages. Each
# edition is a PDF, finishing/reports/edition-proof-<code>_<date>.pdf, and
# carries its own date, so an English-only run leaves the editions' files as
# they are. Bringing an edition's stale translations up to date is the agent's
# work before this runs; a section still stale here prints in English, and the
# edition's title page names it.
#
# Usage: build_proof.sh [--langs CODE,CODE | --all-languages] [DATE]
#        DATE defaults to today, as YYYY-MM-DD
set -euo pipefail
repo="$(git rev-parse --show-toplevel)"; cd "$repo"

langs=""
while [ $# -gt 0 ]; do
  case "$1" in
    --langs) langs="${2//,/ }"; shift 2 ;;
    --all-languages)
      langs="$(ls manuscript/*/translations.tsv 2>/dev/null | xargs -r -n1 dirname | xargs -r -n1 basename | tr '\n' ' ')"
      shift ;;
    *) break ;;
  esac
done
for code in $langs; do
  [ -f "manuscript/$code/book.tex" ] || { echo "no edition: manuscript/$code/book.tex"; exit 1; }
done

date="${1:-$(date +%F)}"
[[ "$date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || { echo "not a YYYY-MM-DD date: $date"; exit 1; }

scratch="${TMPDIR:-/tmp}/es-proof"
rm -rf "$scratch"; mkdir -p "$scratch/pdf" "$scratch/html"

finishing/tools/build_tex.sh  "$scratch/pdf"
finishing/tools/build_html.sh "$scratch/html"
for code in $langs; do
  mkdir -p "$scratch/$code"
  finishing/tools/build_edition.sh "$code" "$scratch/$code"
done

stem="finishing/reports/whole-book-proof_$date"
cp "$scratch/pdf/book.pdf"   "$stem.pdf"
cp "$scratch/html/book.html" "$stem.html"
echo
echo "wrote $stem.pdf  ($(du -h "$stem.pdf"  | cut -f1))"
echo "wrote $stem.html ($(du -h "$stem.html" | cut -f1))"
keep="^$stem\\."
for code in $langs; do
  ed="finishing/reports/edition-proof-${code}_$date.pdf"
  cp "$scratch/$code/book.pdf" "$ed"
  echo "wrote $ed ($(du -h "$ed" | cut -f1))"
done

# The proof is one pair, replaced each time, not a series, and each edition one
# file. Say what is left over rather than delete it: removing a committed file
# is the author's call. Only the formats built this run are looked at.
old=$(ls finishing/reports/whole-book-proof_* 2>/dev/null | grep -v "$keep" || true)
for code in $langs; do
  old="$old
$(ls finishing/reports/edition-proof-${code}_* 2>/dev/null | grep -v "_$date\\.pdf$" || true)"
done
old=$(echo "$old" | sed '/^$/d')
if [ -n "$old" ]; then
  echo
  echo "earlier proofs still present -- remove them in the same commit:"
  echo "$old" | sed 's/^/  git rm /'
fi
