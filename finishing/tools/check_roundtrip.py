#!/usr/bin/env python3
"""Assert join(sections) is byte-identical to the build output, and that the
2024 text is still frozen.

The reference is manuscript/parseable_text_v4.txt: the sections are the source,
the join is the build, and they must never drift. (Before any content edit the
join also equalled v3b; that stopped being true with the first revision, which
is the point of the separate frozen check.)

manuscript/parseable_text_v3b_2024-07-07.txt must never change. Its digest is
pinned below; if it moves, something has edited provenance.
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
from join_manuscript import join  # noqa: E402


V3B_SHA256 = "84b375f9848be91bcfa310049d3f58a8bdaeeca430f5f3e1fff6625f56b75a98"


def check_frozen():
    with open(common.V3B, "rb") as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if got != V3B_SHA256:
        print("FROZEN FILE CHANGED: %s\n  expected %s\n  got      %s"
              % (os.path.relpath(common.V3B, common.REPO), V3B_SHA256, got))
        return False
    return True


def main():
    ok = check_frozen()
    ref = os.path.join(common.REPO, "manuscript", "parseable_text_v4.txt")
    if "--ref" in sys.argv:
        ref = sys.argv[sys.argv.index("--ref") + 1]
    if not os.path.exists(ref):
        sys.exit("no build output at %s; run join_manuscript.py" % ref)
    with open(ref, encoding="utf-8", newline="") as f:
        want = f.read()
    got = join()
    hw = hashlib.sha256(want.encode("utf-8")).hexdigest()
    hg = hashlib.sha256(got.encode("utf-8")).hexdigest()
    if hw != hg:
        wl, gl = want.splitlines(), got.splitlines()
        print("MISMATCH ref=%s" % os.path.relpath(ref, common.REPO))
        print("  ref  %d bytes %d lines  %s" % (len(want), len(wl), hw))
        print("  join %d bytes %d lines  %s" % (len(got), len(gl), hg))
        for i in range(min(len(wl), len(gl))):
            if wl[i] != gl[i]:
                print("  first differing line %d:\n    ref:  %r\n    join: %r" % (i + 1, wl[i], gl[i]))
                break
        sys.exit(1)
    if not ok:
        sys.exit(1)
    print("round-trip OK: join(sections) == %s (%d bytes, sha256 %s); v3b still frozen"
          % (os.path.relpath(ref, common.REPO), len(want), hg[:16]))


if __name__ == "__main__":
    main()
