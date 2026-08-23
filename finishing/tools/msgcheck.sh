#!/usr/bin/env bash
# Dry-run the commit-msg hook against a draft message and show what it changes.
#
# The hook scrubs vendor and brand words from the subject, SILENTLY DELETES body
# lines containing them within the first or last 10 body lines, and rewrites
# vendor-named trailers. Run this before committing anything with a long body.
#
# The hook also requires a DCO sign-off, so this script appends the same
# Signed-off-by line `git commit -s` would add, then diffs against that baseline.
#
# Usage: finishing/tools/msgcheck.sh path/to/draft-message.txt
set -uo pipefail
src="${1:?usage: msgcheck.sh MSGFILE}"
repo="$(git rev-parse --show-toplevel)"
name="$(git config user.name)"; email="$(git config user.email)"
base="$(mktemp)"; tmp="$(mktemp)"; trap 'rm -f "$base" "$tmp"' EXIT

cp "$src" "$base"
if ! grep -q '^Signed-off-by: ' "$base"; then
  printf '\nSigned-off-by: %s <%s>\n' "$name" "$email" >> "$base"
fi
cp "$base" "$tmp"

if ! "$repo/.githooks/commit-msg" "$tmp"; then
  echo "msgcheck: hook REJECTED the message (see error above)"
  exit 1
fi

if diff -u "$base" "$tmp"; then
  echo "msgcheck: the hook would leave this message unchanged"
else
  echo
  echo "msgcheck: the hook WOULD REWRITE this message (diff above)."
  echo "Lines that vanish are brand-word hits inside the body scan window."
  exit 1
fi
