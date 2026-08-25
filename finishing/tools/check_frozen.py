#!/usr/bin/env python3
"""Assert the frozen dialect references have not been touched.

Until D-065 this file was check_roundtrip.py, and it asserted that
join(sections) was byte-identical to manuscript/parseable_text_v4.txt. That
invariant ended with the move to LaTeX: the .tex section files are the source,
book.tex pulls them in directly, and there is no joined build artifact left to
compare against.

What remains is provenance. Two dialect files are frozen and must never move:

  parseable_text_v3b_2024-07-07.txt  the 2024 text exactly as imported.
  parseable_text_v4.txt              the last state of the dialect manuscript,
                                     immediately before the LaTeX migration.

v4 was a generated artifact and is now a historical one. It is the other end of
the chain from v3b: together they bracket everything the dialect era did. The
migration itself was verified by check_tex_roundtrip.py, which inverted the
conversion and diffed 1342 prose lines against these sources; that check is a
one-shot and cannot be re-run now that the .txt sections are gone.
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

FROZEN = {
    "manuscript/parseable_text_v3b_2024-07-07.txt":
        "84b375f9848be91bcfa310049d3f58a8bdaeeca430f5f3e1fff6625f56b75a98",
    "manuscript/parseable_text_v4.txt":
        "86df4e2c70849773267f12a6e19c04d123569543e91cfa77608fd5c417aa0c03",
}


def main():
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
    print("frozen OK: %d dialect reference files unchanged" % len(FROZEN))
    return 0


if __name__ == "__main__":
    sys.exit(main())
