#!/usr/bin/env python3
r"""Structural invariants for manuscript/sections and the ledger.

  0. ORDER.tsv's sha256 column matches each file's actual contents. Nothing
     checked this before P7 C3, and every one of the 157 digests had gone
     stale: they were written once at the v4 split and never regenerated
     through P1-P7's edits, so the column silently stopped being evidence
     of anything. Refresh with tools/refresh_order_shas.py.
  1. every section file opens with its own heading command and \label, the
     filename's number matches the label's number, and the heading's title
     matches ORDER.tsv's title column. Since D-065 the .tex heading is what
     is typeset, so ORDER.tsv is now the copy that can go stale rather than
     the other way round; it is still checked, because gen_book.py and the
     TOC are generated from it.
  2. the heading set equals finishing/outline.tsv (numbers), with title
     differences reported (not fatal; the manuscript text wins)
  3. sorted(glob) order == ORDER.tsv numeric order
  4. LaTeX environments are balanced and correctly nested within each file
  5. ledger.tsv (if present) has exactly one row per section
"""
import glob
import hashlib
import re
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

ENV = re.compile(r"\\\\(begin|end)\{([A-Za-z*]+)\}")


def main():
    errs, notes = [], []
    order_path = os.path.join(common.SECTIONS, "ORDER.tsv")
    if not os.path.exists(order_path):
        sys.exit("no ORDER.tsv; run split_manuscript.py")
    _, rows = common.read_tsv(order_path)
    rows.sort(key=lambda r: common.numkey(r["num"]))

    files = sorted(glob.glob(os.path.join(common.SECTIONS, "ch*", "*.tex")))
    if files != [os.path.join(common.REPO, r["path"]) for r in rows]:
        errs.append("sorted(glob) order != ORDER.tsv numeric order")

    for r in rows:
        p = os.path.join(common.REPO, r["path"])
        with open(p, encoding="utf-8", newline="") as f:
            lines = f.readlines()
        if not lines:
            errs.append("%s is empty" % r["path"])
            continue
        h = common.tex_heading(lines)
        if not h:
            errs.append("%s: does not open with a heading command and \\label: %r"
                        % (r["path"], lines[0][:60]))
            continue
        if h[0] != r["num"]:
            errs.append("%s: heading number %s != ORDER.tsv %s" % (r["path"], h[0], r["num"]))
        if h[1] != r["title"]:
            # Before D-065 the built book took its titles from ORDER.tsv, so a
            # mismatch shipped a stale title with check_all.sh green (found
            # twice: D-024/10.2's 55 titles, then 2.3.3/3.3.1/7.2.3 at P6).
            # LaTeX now typesets the file's own heading, so the failure mode
            # inverts -- ORDER.tsv goes stale, and gen_book.py and the TOC are
            # built from it. Still fatal.
            errs.append("%s: heading title %r != ORDER.tsv title %r"
                        % (r["path"], h[1], r["title"]))
        if "sha256" in r:
            digest = hashlib.sha256(open(p, "rb").read()).hexdigest()
            if digest != r["sha256"]:
                errs.append("%s: ORDER.tsv sha256 is stale (%s != %s); "
                            "run tools/refresh_order_shas.py"
                            % (r["path"], r["sha256"][:12], digest[:12]))
        stem = os.path.basename(p)[:-4].replace("_", ".")   # .tex is 4 chars too
        if tuple(int(x) for x in stem.split(".")) != common.numkey(r["num"]):
            errs.append("%s: filename does not encode %s" % (r["path"], r["num"]))
        stack = []
        for i, line in enumerate(lines, 1):
            for m in ENV.finditer(line):
                kind, name = m.group(1), m.group(2)
                if kind == "begin":
                    stack.append((name, i))
                elif not stack:
                    errs.append("%s:%d \\end{%s} with nothing open"
                                % (r["path"], i, name))
                elif stack[-1][0] != name:
                    errs.append("%s:%d \\end{%s} closes \\begin{%s} from line %d"
                                % (r["path"], i, name, stack[-1][0], stack[-1][1]))
                    stack.pop()
                else:
                    stack.pop()
        for name, i in stack:
            errs.append("%s:%d unclosed \\begin{%s}" % (r["path"], i, name))

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
