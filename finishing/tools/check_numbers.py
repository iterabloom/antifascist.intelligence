#!/usr/bin/env python3
r"""Every label's name is the number LaTeX will print beside it.

WHY THIS EXISTS. The invariant broke once, in chapter 11, and was caught only by
reading `book.aux` by hand (D-296). D-295's Overleaf import left a second
`\section` inside `11_05.tex`, labelled `sec:11.5a` on the author's own in-file
note that the label was temporary. **The book printed nine sections in chapter 11
while every record file knew eight**, and `sec:11.6` through `sec:11.8` printed
one number above their own names. Nothing in the suite saw it: `check_structure.py`
reads each file's *first* heading through `common.tex_heading` and stops, so a
second heading further down the file is invisible to it, and a cross-reference to
`sec:11.6` resolved perfectly -- to the wrong section.

WHAT IT DOES. Walks the files in `ORDER.tsv` order, simulates the chapter, section
and subsection counters the way LaTeX increments them, and checks each
`\label{sec:N}` against the number its heading will actually print. No build is
needed and none is done: the printed number is a function of document order and
heading depth, both of which are in the source. That matters because the built
`book.aux` is not committed, so a checker that read it could only run after a
build.

  * `\chapter` increments and resets section and subsection; `\section` increments
    and resets subsection; `\subsection` increments.
  * The starred forms print no number and increment nothing. All nine
    `\subsection*` in chapter 11 are deliberate, which is why a count of headings
    per file is not the check -- two files hold six and five of them.
  * `\unnumberedlabel{sec:N}{N}` is the manuscript's macro for a heading that
    prints no number and still has to be referred to: the Foreword as 0 and the
    glossary as 13. Those are checked differently -- the declared number must not
    collide with a chapter LaTeX actually numbers.

WHAT IT CANNOT SEE. A `\setcounter` in the preamble or inside a section, which
would move the counters under it; the preamble has none and this tool does not
read it, so adding one silently breaks this check. `secnumdepth` is 2, so a
`\subsubsection` would print no number at all and is not looked for. And it says
nothing about whether a reference points at the section a reader wanted -- that is
`check_xrefs.py` for resolution and `xref_content.py` for aim.

Usage:
  check_numbers.py            check, exit 1 on any mismatch
  check_numbers.py --list     print every heading with its computed number
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

HEAD = re.compile(r"^\\(chapter|section|subsection|subsubsection)(\*?)\s*\{")
LABEL = re.compile(r"\\label\{sec:([^}]*)\}")
UNNUM = re.compile(r"\\unnumberedlabel\{sec:([^}]*)\}\{([^}]*)\}")

LEVEL = {"chapter": 0, "section": 1, "subsection": 2, "subsubsection": 3}


def walk():
    """Yield (path, lineno, kind, starred, number_or_None) in document order."""
    order = os.path.join(common.SECTIONS, "ORDER.tsv")
    _, rows = common.read_tsv(order)
    rows.sort(key=lambda r: common.numkey(r["num"]))
    counters = [0, 0, 0, 0]
    for r in rows:
        path = os.path.join(common.REPO, r["path"])
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        rel = os.path.relpath(path, common.REPO)
        current = None          # the number the last heading prints, or None
        for i, line in enumerate(lines, 1):
            m = HEAD.match(line)
            if m:
                kind, star = m.group(1), m.group(2)
                lvl = LEVEL[kind]
                if star:
                    current = None
                    yield rel, i, kind, True, None, r["num"]
                else:
                    counters[lvl] += 1
                    for d in range(lvl + 1, 4):
                        counters[d] = 0
                    current = ".".join(str(counters[d]) for d in range(lvl + 1))
                    yield rel, i, kind, False, current, r["num"]
                continue
            u = UNNUM.search(line)
            if u:
                yield rel, i, "unnumberedlabel", True, (u.group(1), u.group(2)), r["num"]
                continue
            lab = LABEL.search(line)
            if lab:
                yield rel, i, "label", False, (lab.group(1), current), r["num"]


def main():
    listing = "--list" in sys.argv[1:]
    errs, headings, labels, numbered_chapters = [], 0, 0, set()
    unnum = []
    for rel, i, kind, star, val, ordernum in walk():
        if kind == "label":
            labels += 1
            name, printed = val
            if printed is None:
                errs.append("%s:%d  \\label{sec:%s} follows no numbered heading "
                            "-- a starred heading prints nothing to match"
                            % (rel, i, name))
            elif name != printed:
                errs.append("%s:%d  \\label{sec:%s} but the heading above it "
                            "prints %s" % (rel, i, name, printed))
            if listing:
                print("  %-40s %-8s label %s -> prints %s"
                      % (rel, "", name, printed))
        elif kind == "unnumberedlabel":
            unnum.append((rel, i, val[0], val[1]))
            if val[0] != val[1]:
                errs.append("%s:%d  \\unnumberedlabel{sec:%s}{%s}: the label name "
                            "and the declared number differ" % (rel, i, val[0], val[1]))
        else:
            headings += 1
            if kind == "chapter" and not star:
                numbered_chapters.add(val)
            if listing and not star:
                print("  %-40s %-8s %s" % (rel, val, kind))
            elif listing:
                print("  %-40s %-8s %s* (prints no number)" % (rel, "--", kind))

    for rel, i, name, declared in unnum:
        if declared in numbered_chapters:
            errs.append("%s:%d  \\unnumberedlabel declares %s, which LaTeX also "
                        "prints for a numbered chapter" % (rel, i, declared))

    print("check_numbers: %d headings, %d labels, %d unnumbered, "
          "%d numbered chapters" % (headings, labels, len(unnum),
                                    len(numbered_chapters)))
    if errs:
        print("FAIL:")
        for e in errs:
            print("  %s" % e)
        sys.exit(1)
    print("  every label's name is the number its heading prints")


if __name__ == "__main__":
    main()
