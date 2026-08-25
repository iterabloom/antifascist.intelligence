#!/usr/bin/env python3
"""One-shot: rewrite manuscript/sections/**.txt as .tex and repoint ORDER.tsv.

Run once, on 2026-08-25, to make the manuscript LaTeX-native (D-065). Kept in
the tree as the record of how the conversion was done, not as a tool to re-run:
after it runs the .txt sources are gone and it has nothing left to convert.

The conversion is mechanical -- no prose is reread or rewritten -- and it is
verified by finishing/tools/check_tex_roundtrip.py, which inverts it and diffs
the result against the dialect sources.

Usage: migrate_to_tex.py [--dry-run]
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common      # noqa: E402
import render_tex  # noqa: E402


def main():
    dry = "--dry-run" in sys.argv
    keys = render_tex.load_bib_keys()
    missing = set()

    order_path = os.path.join(common.SECTIONS, "ORDER.tsv")
    header, rows = common.read_tsv(order_path)
    rows.sort(key=lambda r: common.numkey(r["num"]))

    written = []
    for r in rows:
        src = os.path.join(common.REPO, r["path"])
        with open(src, encoding="utf-8", newline="") as f:
            lines = f.readlines()
        body = render_tex.render_section(r["num"], r["title"], lines, keys, missing)
        if not body.endswith("\n"):
            body += "\n"
        dst = src[:-4] + ".tex"
        if not dry:
            with open(dst, "w", encoding="utf-8", newline="") as f:
                f.write(body)
            os.unlink(src)
        r["path"] = os.path.relpath(dst, common.REPO)
        r["sha256"] = hashlib.sha256(body.encode("utf-8")).hexdigest()
        written.append((dst, len(body)))

    if missing:
        sys.exit("ABORT: %d cite ids with no bib_key: %s"
                 % (len(missing), ", ".join(sorted(missing))))
    if not dry:
        common.write_tsv(order_path, header, rows)

    print("%s %d sections (%d bytes of LaTeX)"
          % ("would write" if dry else "wrote", len(written), sum(n for _, n in written)))


if __name__ == "__main__":
    main()
