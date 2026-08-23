#!/usr/bin/env python3
"""Structural invariants for manuscript/sections and the ledger.

  1. every section file's first line is its own heading, and the filename's
     number matches that heading's number
  2. the heading set equals finishing/outline.tsv (numbers), with title
     differences reported (not fatal; the manuscript text wins)
  3. sorted(glob) order == ORDER.tsv numeric order
  4. <<quote>>/<<list>>/<<box>> tags are balanced and unnested within each file
  5. ledger.tsv (if present) has exactly one row per section
"""
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def main():
    errs, notes = [], []
    order_path = os.path.join(common.SECTIONS, "ORDER.tsv")
    if not os.path.exists(order_path):
        sys.exit("no ORDER.tsv; run split_manuscript.py")
    _, rows = common.read_tsv(order_path)
    rows.sort(key=lambda r: common.numkey(r["num"]))

    files = sorted(glob.glob(os.path.join(common.SECTIONS, "ch*", "*.txt")))
    if files != [os.path.join(common.REPO, r["path"]) for r in rows]:
        errs.append("sorted(glob) order != ORDER.tsv numeric order")

    for r in rows:
        p = os.path.join(common.REPO, r["path"])
        with open(p, encoding="utf-8", newline="") as f:
            lines = f.readlines()
        if not lines:
            errs.append("%s is empty" % r["path"])
            continue
        h = common.parse_heading(lines[0])
        if not h:
            errs.append("%s: first line is not a heading: %r" % (r["path"], lines[0][:60]))
            continue
        if h[0] != r["num"]:
            errs.append("%s: heading number %s != ORDER.tsv %s" % (r["path"], h[0], r["num"]))
        stem = os.path.basename(p)[:-4].replace("_", ".")
        if tuple(int(x) for x in stem.split(".")) != common.numkey(r["num"]):
            errs.append("%s: filename does not encode %s" % (r["path"], r["num"]))
        depth = {"quote": 0, "list": 0, "box": 0}
        for i, line in enumerate(lines, 1):
            s = line.strip()
            if "<<h>>" in line or "<</h>>" in line:
                if not (s.startswith("<<h>>") and s.endswith("<</h>>")
                        and len(s) > 11):
                    errs.append("%s:%d malformed run-in head: %r"
                                % (r["path"], i, s[:60]))
                continue
            for tag in ("quote", "list", "box"):
                if s == "<<%s>>" % tag:
                    if depth[tag]:
                        errs.append("%s:%d nested <<%s>>" % (r["path"], i, tag))
                    depth[tag] += 1
                elif s == "<</%s>>" % tag:
                    depth[tag] -= 1
                    if depth[tag] < 0:
                        errs.append("%s:%d unopened <</%s>>" % (r["path"], i, tag))
        for tag, d in depth.items():
            if d:
                errs.append("%s: unclosed <<%s>>" % (r["path"], tag))

    _, ol = common.read_tsv(common.OUTLINE_TSV)
    ol_map = {r["num"]: r["title"] for r in ol}
    ms_map = {r["num"]: r["title"] for r in rows}
    if set(ol_map) != set(ms_map):
        errs.append("heading numbers differ from outline.tsv: only-sections=%s only-outline=%s"
                    % (sorted(set(ms_map) - set(ol_map)), sorted(set(ol_map) - set(ms_map))))
    for n in sorted(set(ol_map) & set(ms_map), key=common.numkey):
        if ol_map[n] != ms_map[n]:
            notes.append("title differs at %s (manuscript wins): %r vs outline %r"
                         % (n, ms_map[n], ol_map[n]))

    if os.path.exists(common.LEDGER_TSV):
        _, led = common.read_tsv(common.LEDGER_TSV)
        lnums = [r["num"] for r in led]
        if sorted(set(lnums), key=common.numkey) != sorted(ms_map, key=common.numkey):
            errs.append("ledger.tsv rows do not match the section set (%d rows, %d sections)"
                        % (len(lnums), len(ms_map)))
        if len(lnums) != len(set(lnums)):
            errs.append("ledger.tsv has duplicate num rows")
    else:
        notes.append("ledger.tsv not present yet")

    print("check_structure: %d sections" % len(rows))
    for n in notes:
        print("  note: %s" % n)
    if errs:
        print("FAIL:")
        for e in errs:
            print("  %s" % e)
        sys.exit(1)
    print("  structure OK")


if __name__ == "__main__":
    main()
