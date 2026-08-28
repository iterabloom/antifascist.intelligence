#!/usr/bin/env bash
# Run every invariant check. Do this before each commit and at session start.
set -uo pipefail
repo="$(git rev-parse --show-toplevel)"; cd "$repo"
fail=0
run() { echo; echo "== $1"; shift; "$@" || { echo "  ^^ FAILED"; fail=1; }; }
run "frozen files unchanged (none registered)" python3 finishing/tools/check_frozen.py
run "structure: headings, order, environments, ledger parity" python3 finishing/tools/check_structure.py
run "sections.tex is generated output, and current" python3 finishing/tools/gen_book.py --check
run "TOC is generated output, and current" python3 finishing/tools/headings.py --check
run "cross-references: resolve, and prefixed" python3 finishing/tools/check_xrefs.py
run "typography: quotes and dashes are the characters" python3 finishing/tools/check_typography.py
run "named-persons guard" python3 finishing/tools/names_guard.py
echo
[ "$fail" = 0 ] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
exit "$fail"
