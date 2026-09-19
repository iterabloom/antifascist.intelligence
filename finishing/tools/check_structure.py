#!/usr/bin/env python3
r"""Structural invariants for manuscript/sections and the ledger.

  0. ORDER.tsv's sha256 column matches each file's actual contents. Nothing
     checked this before P7 C3, and every one of the 157 digests had gone
     stale: they were written once at the v4 split and never regenerated
     through P1-P7's edits, so the column silently stopped being evidence
     of anything. Refresh with tools/refresh_order_shas.py.
  1. every section file opens with its own heading command and \label, the
     filename's number matches the label's number, and the heading's title
     matches ORDER.tsv's title column. Two D-406 exemptions, both counted in
     the output so the number of exempt files is visible rather than implied:
     a file with a **named** label (`ch:custody`, a new chapter whose printed
     number will move again) has no number in its label to compare, and a
     **continuation** row -- empty `num`, a file with no heading that prints
     under the heading before it -- has no heading, title or number at all.
     For the other 88 files the chain filename -> label -> ORDER.tsv num is
     checked exactly as it was; what `num` no longer claims is the number
     LaTeX prints, which `headings.py` computes and the TOC carries.
     Since D-065 the .tex heading is what is typeset, so ORDER.tsv is the copy
     that can go stale rather than the other way round; it is still checked,
     because gen_book.py generates the \input list from it.
  2. the heading set equals finishing/outline.tsv (numbers), with title
     differences reported (not fatal; the manuscript text wins)
  3. the set of .tex files on disk == the set ORDER.tsv lists. This was an
     ORDER-ORDER comparison until D-406, when the restructure separated a
     file's identity from its position: reading order is now ORDER.tsv's `seq`
     column, so sorted(glob) has no reason to reproduce it and the invariant
     that is left is that neither side has a file the other does not.
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

ENV = re.compile(r"\\(begin|end)\{([A-Za-z*]+)\}")


def main():
    errs, notes = [], []
    continuations = named_labels = 0
    order_path = os.path.join(common.SECTIONS, "ORDER.tsv")
    if not os.path.exists(order_path):
        sys.exit("no ORDER.tsv; run split_manuscript.py")
    rows = common.order_rows()

    files = set(glob.glob(os.path.join(common.SECTIONS, "ch*", "*.tex")))
    listed = set(os.path.join(common.REPO, r["path"]) for r in rows)
    for f in sorted(files - listed):
        errs.append("%s is on disk and not in ORDER.tsv" % os.path.relpath(f, common.REPO))
    for f in sorted(listed - files):
        errs.append("%s is in ORDER.tsv and not on disk" % os.path.relpath(f, common.REPO))

    for r in rows:
        h = None
        p = os.path.join(common.REPO, r["path"])
        with open(p, encoding="utf-8", newline="") as f:
            lines = f.readlines()
        if not lines:
            errs.append("%s is empty" % r["path"])
            continue
        if not r["num"]:
            # A continuation: no heading, no identity, no title. Its contents are
            # still digested and its environments still have to balance, so the
            # checks below this block run; the heading checks cannot.
            continuations += 1
        else:
            h = common.tex_heading(lines)
            if not h:
                errs.append("%s: does not open with a heading command and \\label: %r"
                            % (r["path"], lines[0][:60]))
                continue
            if not re.search(r"\d", h[0]):
                named_labels += 1      # ch:custody and the like; nothing to compare
            elif h[0] != r["num"]:
                errs.append("%s: heading number %s != ORDER.tsv %s" % (r["path"], h[0], r["num"]))
        if h and h[1] != r["title"]:
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
        # D-464: the filename encodes the file's POSITION, not ORDER.tsv's num.
        # This compared the two, which was the same test while num was position;
        # D-406 made num an identity that stays put while a file moves, so the
        # comparison would now fail on 75 of 97 files that are exactly where
        # they belong. The property worth holding is the one the filenames are
        # for, and it is checked once over the whole set below rather than file
        # by file: sorting the paths reproduces reading order.
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
    ms_map = {r["num"]: r["title"] for r in rows if r["num"]}
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

    # D-464: byte-order sorting over the paths reproduces reading order. The
    # filenames exist to carry position, and this is that property stated once
    # over the whole set instead of inferred from each name. It went false at
    # D-406 and nothing noticed for thirteen days, because the per-file rule it
    # replaces compared a filename against an identity rather than a position.
    seq_order = [r["path"] for r in rows]
    if sorted(seq_order) != seq_order:
        first = next(i for i, (a, b) in enumerate(zip(seq_order, sorted(seq_order)))
                     if a != b)
        errs.append("byte-order sorting no longer reproduces reading order; "
                    "first divergence at position %d: reading order has %s, "
                    "sorted order has %s"
                    % (first, seq_order[first], sorted(seq_order)[first]))

    print("check_structure: %d files (%d with a heading, %d continuations); "
          "%d named labels exempt from the number comparison"
          % (len(rows), len(rows) - continuations, continuations, named_labels))
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
