#!/usr/bin/env python3
r"""Cross-reference invariants for the manuscript (D-046, rewritten at D-066).

Until D-066 a cross-reference was a number typed into the prose, and this
check existed because that arrangement had two failure modes, both of which
P11's renumbering actually produced:

  DANGLING  a reference to a section number that does not exist.
  BARE      a section number with no "section"/"chapter"/"§" in front of it,
            invisible to the renumber script, silently keeping its old value.

References are \ref{sec:N} now, so LaTeX generates the number and neither
failure can survive a build: an unresolved \ref prints "??" and warns, and
there is no typed number left to go stale. What is checked here is therefore
different, and cheaper than a build:

  DANGLING  a \ref whose target is not a section in ORDER.tsv.
  BARE      a section or chapter number still written out in the prose. These
            are not errors in themselves -- the number is right today -- but
            each one is a place the next renumber would have to find by hand,
            which is the problem \ref was adopted to end.

What this does NOT check: whether a reference points at the RIGHT section.
That is a semantic question; the full read is recorded in finishing/p13-scope.md
and has to be redone by hand after any renumbering.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORDER = os.path.join(ROOT, 'manuscript/sections/ORDER.tsv')

# D-406: new chapters carry named ch: labels, so a reference to one has to be
# resolved here too. Without this the prefix was invisible and a \ref{ch:typo}
# would have reached the build unchecked.
REF = re.compile(r'\\ref\{(?:sec|ch):([^}]*)\}')
LABEL = re.compile(r'\\(?:label|unnumberedlabel)\{(?:sec|ch):([^}]*)\}')
# A number still typed into the prose, with a reference word in front of it.
BARE = re.compile(r'(?:[Ss]ections?|[Cc]hapters?|§)\s*(\d{1,2}(?:\.\d{1,2}){0,2})(?![\d])')
MASK = re.compile(r'\\(?:label|unnumberedlabel|ref|autocite|cite|input|addcontentsline)\*?\{[^}]*\}')


def load_numbers():
    nums = set()
    with open(ORDER) as fh:
        for line in fh:
            p = line.rstrip('\n').split('\t')
            if len(p) > 1 and re.fullmatch(r'\d+(\.\d+)*', p[1]):
                nums.add(p[1])
    return nums


def main():
    files = sorted(glob.glob(os.path.join(ROOT, 'manuscript/sections/ch*/*.tex')))

    # D-406: a reference is now checked against the labels the manuscript actually
    # DEFINES, in two passes, rather than against ORDER.tsv's num column. The old
    # test assumed every label was a section number -- so it could not see
    # \label{ch:authority} at all, and rejected sec:3.8a because the number has a
    # letter in it. Checking the definitions is also the stronger test: it catches
    # a reference to a label nobody wrote, which a num-set check cannot.
    labels = set()
    for f in files:
        for ln in open(f).read().split('\n'):
            labels.update(LABEL.findall(ln))

    dangling, bare, nrefs = [], [], 0
    for f in files:
        rel = os.path.relpath(f, ROOT)
        for i, ln in enumerate(open(f).read().split('\n'), 1):
            for m in REF.finditer(ln):
                nrefs += 1
                if m.group(1) not in labels:
                    dangling.append((rel, i, m.group(1),
                                     ln[max(0, m.start() - 60):m.end() + 25]))
            masked = MASK.sub(' ', ln)
            for m in BARE.finditer(masked):
                bare.append((rel, i, m.group(1),
                             masked[max(0, m.start() - 60):m.end() + 25]))

    for label, rows in (('DANGLING', dangling), ('BARE', bare)):
        for rel, ln, n, ctx in rows:
            print(f'  {label} {rel}:{ln}  -> {n}\n     ...{ctx.strip()}...')

    # Every file that has a heading must define a label, or nothing can point at
    # it. check_structure.py checks that the OPENING label is the file's identity;
    # this is the weaker, file-level version of the same thing, kept because it
    # names the file rather than the number.
    missing = []
    for r in common.order_rows():
        if not r["num"]:
            continue                      # a continuation has no heading to label
        body = open(os.path.join(ROOT, r["path"])).read()
        if not LABEL.search(body):
            missing.append(r["path"])
    if missing:
        print('  NO LABEL in file(s): %s' % ', '.join(missing))

    if dangling or bare or missing:
        print(f'check_xrefs: FAILED — {len(dangling)} dangling, {len(bare)} bare, '
              f'{len(missing)} unlabelled')
        return 1
    print(f'  cross-references OK: {nrefs} \\ref resolve, {len(labels)} labels, '
          f'none left in prose')
    return 0


if __name__ == '__main__':
    sys.exit(main())
