#!/usr/bin/env python3
"""Rewrite ORDER.tsv's sha256 column from the section files' actual contents.

Run after any content edit. check_structure.py fails on a stale digest; this
is the only thing that clears it. The column is a tamper/drift record, not a
build input -- refreshing it is bookkeeping, not a change to the manuscript.
"""
import csv
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

path = os.path.join(common.SECTIONS, "ORDER.tsv")
rows = list(csv.reader(open(path, encoding="utf-8"), delimiter="\t"))
hdr = rows[0]
pi, si = hdr.index("path"), hdr.index("sha256")
changed = 0
for r in rows[1:]:
    digest = hashlib.sha256(open(os.path.join(common.REPO, r[pi]), "rb").read()).hexdigest()
    if digest != r[si]:
        r[si] = digest
        changed += 1
with open(path, "w", encoding="utf-8", newline="") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("refreshed %d of %d sha256 rows in %s" % (changed, len(rows) - 1, path))
