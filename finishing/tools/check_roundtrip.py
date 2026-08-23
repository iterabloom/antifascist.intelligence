#!/usr/bin/env python3
"""Assert join(sections) is byte-identical to a reference file.

Default reference: the frozen v3b. Once normalization lands, the reference
becomes manuscript/parseable_text_v4.txt (pass --ref).
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
from join_manuscript import join  # noqa: E402


def main():
    ref = common.V3B
    if "--ref" in sys.argv:
        ref = sys.argv[sys.argv.index("--ref") + 1]
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
    print("round-trip OK: join(sections) == %s (%d bytes, sha256 %s)"
          % (os.path.relpath(ref, common.REPO), len(want), hg[:16]))


if __name__ == "__main__":
    main()
