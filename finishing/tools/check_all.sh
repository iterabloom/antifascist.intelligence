#!/usr/bin/env bash
# Run every invariant check. Do this before each commit and at session start.
set -uo pipefail
repo="$(git rev-parse --show-toplevel)"; cd "$repo"
fail=0
run() { echo; echo "== $1"; shift; "$@" || { echo "  ^^ FAILED"; fail=1; }; }
run "round-trip: join(sections) == reference" python3 finishing/tools/check_roundtrip.py "$@"
run "structure: headings, order, markup, ledger parity" python3 finishing/tools/check_structure.py
run "TOC is generated output, and current" python3 finishing/tools/headings.py --check
run "named-persons guard" python3 finishing/tools/names_guard.py
echo
[ "$fail" = 0 ] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
exit "$fail"
