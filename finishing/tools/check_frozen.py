#!/usr/bin/env python3
"""Assert that every file registered as frozen is byte-for-byte unchanged.

Nothing is registered. FROZEN is empty, so this check passes without reading
anything, and it is kept as the place a frozen file would be registered.

History, because the empty map is otherwise unreadable. Until D-065 this file
was check_roundtrip.py and asserted that join(sections) was byte-identical to
manuscript/parseable_text_v4.txt; the move to LaTeX ended that invariant, since
the .tex section files are the source and there is no joined artifact left to
compare against. From D-065 to D-088 it guarded the two dialect reference
files -- parseable_text_v3b_2024-07-07.txt, the 2024 text as imported, and
parseable_text_v4.txt, the last state of the manuscript before the migration.
Both were removed from the repository at D-088 on the author's instruction.
Git holds them: they are reachable at any commit before that one.

To freeze a file again, add its repository-relative path and the sha256 of its
current contents to FROZEN.
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

FROZEN = {}


def main():
    if not FROZEN:
        print("frozen OK: no file is registered as frozen")
        return 0
    bad = 0
    for rel, want in sorted(FROZEN.items()):
        path = os.path.join(common.REPO, rel)
        if not os.path.exists(path):
            print("FROZEN FILE MISSING: %s" % rel)
            bad += 1
            continue
        with open(path, "rb") as f:
            got = hashlib.sha256(f.read()).hexdigest()
        if got != want:
            print("FROZEN FILE CHANGED: %s\n  expected %s\n  got      %s"
                  % (rel, want, got))
            bad += 1
    if bad:
        return 1
    print("frozen OK: %d registered file(s) unchanged" % len(FROZEN))
    return 0


if __name__ == "__main__":
    sys.exit(main())
