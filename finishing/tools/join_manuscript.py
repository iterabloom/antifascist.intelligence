#!/usr/bin/env python3
"""Concatenate manuscript/sections/** in ORDER.tsv order to stdout or a file."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def join():
    _, rows = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    rows.sort(key=lambda r: common.numkey(r["num"]))
    parts = []
    for r in rows:
        with open(os.path.join(common.REPO, r["path"]), encoding="utf-8", newline="") as f:
            parts.append(f.read())
    return "".join(parts)


if __name__ == "__main__":
    text = join()
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if args:
        with open(args[0], "w", encoding="utf-8", newline="") as f:
            f.write(text)
        print("wrote %s (%d bytes)" % (args[0], len(text.encode("utf-8"))))
    else:
        sys.stdout.write(text)
