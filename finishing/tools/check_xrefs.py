#!/usr/bin/env python3
"""Cross-reference invariants for the manuscript (D-046).

Two failure modes, both of which P11's renumbering actually produced and its
verification missed:

  DANGLING  a reference to a section number that does not exist. P11's check
            only confirmed each reference resolved; a reference rewritten to a
            number that happened to exist passed even when it was wrong.

  BARE      a section number with no "section"/"chapter"/"§" in front of it.
            The P11 renumber script keyed on those words, so a bare number was
            invisible to it and silently kept its pre-renumber value. Requiring
            the prefix is what makes the next renumber safe.

What this does NOT check: whether a reference that exists points at the RIGHT
section. That is a semantic question; the full 499-reference read is recorded
in finishing/p13-scope.md and has to be redone by hand after any renumbering.
"""
import re, sys, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORDER = os.path.join(ROOT, 'manuscript/sections/ORDER.tsv')

REF = re.compile(r'(?<![\w.$])(\d{1,2}(?:\.\d{1,2}){1,2})(?![\w%]|\.\d)')
# prefixed directly, or continuing a prefixed list: "sections 8.1 and 8.2"
PROT = re.compile(
    r'(?:[Ss]ections?|[Cc]hapters?|§)\s*$'
    r'|(?:[Ss]ections?|[Cc]hapters?|§)\s*\d{1,2}(?:\.\d{1,2}){0,2}\s*'
    r'(?:,|and|through|to|or|–|-)\s*$')
# a number that is a quantity, not a reference
QTY = re.compile(r'(million|billion|trillion|percent|per cent|%|GPT|GDP|\$)', re.I)
# LaTeX commands whose arguments carry numbers that are not references.
LATEX = re.compile(r'\\(?:label|ref|autocite|cite|input|addcontentsline)\*?\{[^}]*\}')


def load_numbers():
    nums = set()
    with open(ORDER) as fh:
        for line in fh:
            p = line.rstrip('\n').split('\t')
            if len(p) > 1 and re.fullmatch(r'\d+(\.\d+)*', p[1]):
                nums.add(p[1])
    return nums


def main():
    nums = load_numbers()
    if not nums:
        print('check_xrefs: no section numbers in ORDER.tsv'); return 1
    dangling, bare = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, 'manuscript/sections/ch*/*.tex'))):
        rel = os.path.relpath(f, ROOT)
        lines = open(f).read().split('\n')
        for i, ln in enumerate(lines):
            if i == 0:
                continue          # the heading is a number, not a reference
            # Section numbers also appear inside the LaTeX machinery a section
            # file now carries -- \label{sec:10.3.2} most of all. Those are the
            # anchors these references point AT, not references themselves.
            ln = LATEX.sub(' ', ln)
            for m in REF.finditer(ln):
                n = m.group(1)
                before, after = ln[:m.start()], ln[m.end():m.end() + 14]
                if QTY.search(after) or QTY.search(before[-14:]):
                    continue
                ctx = ln[max(0, m.start() - 60):m.end() + 30]
                if n not in nums:
                    dangling.append((rel, i + 1, n, ctx))
                elif not PROT.search(before):
                    bare.append((rel, i + 1, n, ctx))
    for label, rows in (('DANGLING', dangling), ('BARE', bare)):
        for rel, ln, n, ctx in rows:
            print(f'  {label} {rel}:{ln}  -> {n}\n     ...{ctx}...')
    total = len(dangling) + len(bare)
    if total:
        print(f'check_xrefs: FAILED — {len(dangling)} dangling, {len(bare)} bare')
        return 1
    refs = sum(1 for f in glob.glob(os.path.join(ROOT, 'manuscript/sections/ch*/*.tex'))
               for i, ln in enumerate(open(f).read().split('\n')) if i
               for m in REF.finditer(ln)
               if m.group(1) in nums and not QTY.search(ln[m.end():m.end() + 14]))
    print(f'  cross-references OK: {refs} resolve, all prefixed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
