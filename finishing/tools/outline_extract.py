#!/usr/bin/env python3
"""Copy column A of the v3b assignment spreadsheet into finishing/outline.tsv.

Column A holds section numbers and titles. Later columns hold persona names and
are never read into any output (AGENTS.md named-persons rule).

Run once. After that outline.tsv is hand-maintained and this script refuses to
overwrite it unless --force is given.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import odsread  # noqa: E402

HEADER = ["num", "title", "level", "parent"]


def main():
    force = "--force" in sys.argv
    if os.path.exists(common.OUTLINE_TSV) and not force:
        sys.exit("outline.tsv exists; refusing to overwrite (use --force)")
    rows, bad = [], []
    for raw in odsread.first_column(common.OUTLINE_ODS):
        raw = raw.strip()
        if not raw:
            continue
        h = common.parse_heading(raw)
        if not h:
            bad.append(raw)
            continue
        num, title = h
        rows.append({"num": num, "title": title,
                     "level": common.level(num), "parent": common.parent(num)})
    if bad:
        sys.exit("unparseable outline rows: %r" % bad[:5])
    rows.sort(key=lambda r: common.numkey(r["num"]))
    common.write_tsv(common.OUTLINE_TSV, HEADER, rows)
    print("wrote %s with %d entries" % (common.OUTLINE_TSV, len(rows)))


if __name__ == "__main__":
    main()
