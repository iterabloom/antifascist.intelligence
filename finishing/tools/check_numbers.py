#!/usr/bin/env python3
r"""Labels are unique, and the number every heading prints is knowable without a build.

WHY THIS EXISTS. The invariant broke once, in chapter 11, and was caught only by
reading `book.aux` by hand (D-296). D-295's Overleaf import left a second
`\section` inside `11_05.tex`, labelled `sec:11.5a` on the author's own in-file
note that the label was temporary. **The book printed nine sections in chapter 11
while every record file knew eight**, and `sec:11.6` through `sec:11.8` printed
one number above their own names. Nothing in the suite saw it: `check_structure.py`
reads each file's *first* heading and stops, so a second heading further down the
file is invisible to it, and a cross-reference to `sec:11.6` resolved perfectly --
to the wrong section.

WHAT CHANGED AT D-406, AND WHERE THE GUARANTEE WENT. Until then this tool checked
that every `\label{sec:N}`'s name was the number LaTeX would print beside it, and
that single comparison caught D-296's bug: a stray heading shifts the counters, so
the names stop matching. The restructure retires the premise. A file now keeps the
`num` its filename, its label, its `ledger.tsv` row and four hundred decision rows
know it by, while its position in the book moves -- `03_03.tex` is labelled
`sec:3.3` and prints as section 6.1 -- so a label name is an identity and no
longer a claim about a printed number.

**D-296's bug is still caught, one step to the left.** `headings.py` generates
`table-of-contents.txt` from the numbers this file's walk computes, in reading
order, and `check_all.sh` runs `headings.py --check`. A stray extra heading
renumbers everything under it, the generated TOC changes, and that check fails on
a diff that names the first heading to move. What this tool keeps is the part the
TOC cannot see: that no two labels share a name, and that an unnumbered chapter's
pinned number does not collide with a chapter LaTeX numbers.

WHAT IT REPORTS RATHER THAN ENFORCES. The identity-to-printed-number map, and how
many legacy `sec:N` labels no longer name their own printed number. After a
restructure that figure is expected to be large; what matters is that it is
**stated**, because the alternative is a reader assuming `sec:3.3` means section
3.3. `--list` prints the whole mapping.

WHAT IT CANNOT SEE. A `\setcounter` in the preamble or inside a section, which
would move the counters under it; the preamble has none and this tool does not
read it, so adding one silently breaks the computed numbers here and in the TOC.
`secnumdepth` is 2, so a `\subsubsection` prints no number and is not looked for.
And it says nothing about whether a reference points at the section a reader
wanted -- that is `check_xrefs.py` for resolution and `xref_content.py` for aim.

Usage:
  check_numbers.py            check, exit 1 on a duplicate label or a collision
  check_numbers.py --list     print every heading and label with its number
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

LABEL = re.compile(r"\\label\{(sec|ch):([^}]*)\}")
UNNUM = re.compile(r"\\unnumberedlabel\{(?:sec|ch):([^}]*)\}\{([^}]*)\}")


def main():
    listing = "--list" in sys.argv[1:]
    errs, notes = [], []

    # The printed numbers, computed by simulating LaTeX's counters in reading
    # order. This is the same walk headings.py generates the TOC from.
    printed = common.printed_headings()
    numbered_chapters = {num for num, _t, _p, _l, nb in printed
                         if nb and "." not in num}

    # Every label in the book, with the file it sits in.
    labels, unnum = [], []
    for r in common.order_rows():
        rel = r["path"]
        with open(os.path.join(common.REPO, rel), encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                u = UNNUM.search(line)
                if u:
                    unnum.append((rel, i, u.group(1), u.group(2)))
                    continue
                m = LABEL.search(line)
                if m:
                    labels.append((rel, i, m.group(1), m.group(2), r["num"]))

    # 1. No two labels may share a name. A duplicate makes every \ref to it
    #    resolve to whichever LaTeX saw last, silently.
    seen = {}
    for rel, i, prefix, name, _num in labels + [(a, b, "sec", c, "") for a, b, c, _d in unnum]:
        key = name
        if key in seen:
            errs.append("%s:%d  label %s:%s duplicates %s"
                        % (rel, i, prefix, name, seen[key]))
        else:
            seen[key] = "%s:%d" % (rel, i)

    # 2. An unnumbered chapter pins its own number. It must not be one LaTeX
    #    prints for a chapter it does number, or every \ref to it is ambiguous
    #    to a reader even though it resolves.
    for rel, i, name, declared in unnum:
        if declared in numbered_chapters:
            errs.append("%s:%d  \\unnumberedlabel declares %s, which LaTeX also "
                        "prints for a numbered chapter" % (rel, i, declared))

    # 3. Report: which legacy sec:N labels no longer name their printed number.
    #    Expected after D-406; the point is that the count is stated.
    file_printed = {}
    for num, _t, rel, _l, _nb in printed:
        file_printed.setdefault(rel, num)
    # Every legacy file holds exactly one numbered heading, so the file's first
    # printed number is the one its label sits under. A file with several -- the
    # contingency chapter, which carries its own sections -- gives its labels
    # names rather than numbers, so nothing here compares them.
    drifted = [(rel, i, name, file_printed.get(rel))
               for rel, i, prefix, name, ident in labels
               if prefix == "sec" and re.match(r"^[\d.]+$", name)
               and file_printed.get(rel) and name != file_printed[rel]]

    if listing:
        print("  printed headings, in reading order:")
        for num, title, rel, line, _nb in printed:
            print("    %-8s %-46s %s:%d" % (num, title[:46], rel, line))
        print("  labels:")
        for rel, i, prefix, name, ident in labels:
            print("    %s:%-4s prints %-8s %s:%d"
                  % (prefix, name, file_printed.get(rel, "?"), rel, i))

    print("check_numbers: %d printed headings, %d labels, %d unnumbered, "
          "%d numbered chapters" % (len(printed), len(labels), len(unnum),
                                    len(numbered_chapters)))
    if drifted:
        print("  note: %d legacy sec: labels no longer name their printed number "
              "(identity, not a defect -- D-406):" % len(drifted))
        for rel, i, name, p in drifted[:12]:
            print("    %s:%d  sec:%s prints %s" % (rel, i, name, p))
        if len(drifted) > 12:
            print("    ... %d more (--list for all)" % (len(drifted) - 12))
    for n in notes:
        print("  note: %s" % n)
    if errs:
        print("FAIL:")
        for e in errs:
            print("  %s" % e)
        sys.exit(1)
    print("  labels are unique and no pinned number collides with a printed one")


if __name__ == "__main__":
    main()
