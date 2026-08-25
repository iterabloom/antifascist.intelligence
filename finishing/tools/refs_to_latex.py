#!/usr/bin/env python3
r"""One-shot: turn prose cross-references into \ref (D-066).

"section 6.1.3" becomes "section~\ref{sec:6.1.3}". The word stays prose; only
the number becomes a reference, so LaTeX generates it and a renumber can no
longer leave a stale number behind. The tie is deliberate: it stops a reference
splitting across a line break, which a plain space allows.

The predicate is check_xrefs.py's, deliberately -- the same REF/QTY/PROT rules
decide what is a reference here as decide what that check enforces, so the
conversion cannot disagree with the checker about what it is converting.
LaTeX commands are masked to equal-length filler first, so a number inside
\label{sec:10.3.2} or an \autocite key is invisible while offsets stay true.

Usage: refs_to_latex.py [--dry-run]
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

REF = re.compile(r'(?<![\w.$])(\d{1,2}(?:\.\d{1,2}){1,2})(?![\w%]|\.\d)')
# A bare chapter number. The lookahead must reject 8 inside 8.3.3 while
# still allowing a sentence-final "chapter 8.", so it bars only a dot
# that a digit follows.
CHAP = re.compile(r'(?<![\w.$])(\d{1,2})(?![\w%]|\.\d)')
# A prefix word directly before the number, or a list continuing from one:
# "sections 8.1 and 8.2", and equally "chapters 3, 7 and 8" -- the third item
# needs the repeat, which check_xrefs.py's narrower version did not have.
PROT = re.compile(
    r'(?:[Ss]ections?|[Cc]hapters?|§)\s*$'
    r'|(?:[Ss]ections?|[Cc]hapters?|§)\s*'
    r'(?:\d{1,2}(?:\.\d{1,2}){0,2}\s*(?:,|and|through|to|or|–|-)\s*)+$')
DIRECT = re.compile(r'(?:[Ss]ections?|[Cc]hapters?|§)\s*$')
QTY = re.compile(r'(million|billion|trillion|percent|per cent|%|GPT|GDP|\$)', re.I)
LATEX = re.compile(r'\\(?:label|unnumberedlabel|ref|autocite|cite|input|addcontentsline)\*?\{[^}]*\}')


def mask(line):
    """Blank out LaTeX command calls, preserving every offset."""
    return LATEX.sub(lambda m: " " * len(m.group(0)), line)


def convert_line(line, nums):
    masked = mask(line)
    out, last, n = [], 0, 0
    for m in list(REF.finditer(masked)) + list(CHAP.finditer(masked)):
        pass
    # Longer (dotted) matches first so 8.7.7 is not seen as chapter 8.
    spans = []
    for m in REF.finditer(masked):
        spans.append((m.start(), m.end(), m.group(1)))
    taken = [(a, b) for a, b, _ in spans]
    for m in CHAP.finditer(masked):
        if not any(a <= m.start() < b for a, b in taken):
            spans.append((m.start(), m.end(), m.group(1)))
    spans.sort()

    for a, b, num in spans:
        before, after = masked[:a], masked[b:b + 14]
        if QTY.search(after) or QTY.search(before[-14:]):
            continue
        if num not in nums or not PROT.search(before):
            continue
        out.append(line[last:a])
        # "section 6.1.3" -> "section~\ref{...}"; a continuation such as
        # "and 8.2" keeps its ordinary space.
        if DIRECT.search(before) and out and out[-1].endswith(" "):
            out[-1] = out[-1][:-1] + "~"
        out.append(r"\ref{sec:%s}" % num)
        last = b
        n += 1
    out.append(line[last:])
    return "".join(out), n


def main():
    dry = "--dry-run" in sys.argv
    _, rows = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    nums = {r["num"] for r in rows}
    total, touched, samples = 0, 0, []
    for f in sorted(glob.glob(os.path.join(common.SECTIONS, "ch*", "*.tex"))):
        lines = open(f, encoding="utf-8").read().split("\n")
        new, n_file = [], 0
        for i, ln in enumerate(lines):
            if i == 0:
                new.append(ln)
                continue
            conv, n = convert_line(ln, nums)
            if n and len(samples) < 12:
                j = conv.index(r"\ref{")
                samples.append((os.path.relpath(f, common.REPO), i + 1,
                                conv[max(0, j - 55):j + 45]))
            new.append(conv)
            n_file += n
        if n_file and not dry:
            open(f, "w", encoding="utf-8").write("\n".join(new))
        total += n_file
        touched += 1 if n_file else 0
    print("%s %d references in %d files"
          % ("would convert" if dry else "converted", total, touched))
    for rel, ln, ctx in samples:
        print("  %s:%d  ...%s..." % (rel, ln, ctx))


if __name__ == "__main__":
    main()
