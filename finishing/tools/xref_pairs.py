#!/usr/bin/env python3
"""Put every cross-reference's citing sentence next to what it points at.

Q-041's failure class is a reference that *resolves* and still names a claim its
target does not make.  `check_xrefs.py` resolves and cannot read;
`xref_content.py` fires only where the citing sentence carries a proper noun, an
acronym or a year.  Neither reads the pair.  Nothing but a person reading the two
sentences together finds this, and chasing 800-odd pointers through the
manuscript is why nobody has.

This writes the pairs into one file so the reading is linear instead.  For each
`\\ref{sec:N}` in the section files it emits the sentence containing the
reference, then the first prose sentence of section N -- which in this book is
where a section states its claim, so a mismatch shows up as "the citing sentence
says the target does X; the target opens by doing Y."

Padding, per the author's specification (D-111): if either sentence is under 15
words, the preceding sentence comes with it; if either is under 10, both the
preceding and the following one do.  A short sentence carries too little to judge
alone.

Sentence splitting is a heuristic over prose that has already had its LaTeX
stripped by `common.tex_prose_line`.  Abbreviations that end in a period are the
known failure -- the splitter protects a short list of them and will still be
wrong occasionally.  It is wrong in the direction of splitting too often, which
costs a reader context and does not hide anything.

Read-only: writes one report and touches nothing else.

    python3 finishing/tools/xref_pairs.py [--out PATH] [--only SECTION]
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common

REF_RE = re.compile(r"\\(?:ref|autoref)\{sec:([0-9.]+)\}")
TOKEN_RE = re.compile(r"Zx([0-9p]+)xZ")
# Abbreviations whose period does not end a sentence.  Python's `re` will not
# take a variable-width lookbehind, so the split is done naively and then undone
# wherever the piece before the break ends in one of these.
ABBREV = set("""Mr Mrs Ms Dr Prof St Jr Sr vs etc cf al No no Vol vol pp Inc
Ltd Co Rep Sen Gov Art Fig Ch ed eds trans approx ca c J JJ Cir Cal Fla Tex
Mass Conn Ariz Wash Ore Colo Minn Wis""".split())
CUT_RE = re.compile(r'(?<=[.!?])["\'\u201d\u2019]?\s+(?=["\u201c\u2018(]?[A-Z\u201c])')
TAIL_RE = re.compile(r'([A-Za-z.]+)\.["\'\u201d\u2019]?\s*$')


def prose_of(path):
    """The file's prose as one string, LaTeX stripped, headings dropped.

    `common.tex_prose_line` renders a reference as the number it prints, which
    loses which section was meant.  So each reference is swapped for an opaque
    token first, and the tokens are read back out of the prose afterwards.
    """
    out = []
    for line in open(path, encoding="utf-8"):
        if line.lstrip().startswith(("\\chapter", "\\section", "\\subsection",
                                     "\\subsubsection", "\\label", "\\epigraph")):
            continue
        line = REF_RE.sub(lambda m: " Zx%sxZ " % m.group(1).replace(".", "p"), line)
        t = common.tex_prose_line(line).strip()
        if t:
            out.append(t)
    return " ".join(out)


def sentences(text):
    """Split into sentences, rejoining across protected abbreviations."""
    parts = CUT_RE.split(text)
    out = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if out:
            m = TAIL_RE.search(out[-1])
            tail = m.group(1) if m else ""
            # e.g. / i.e. / U.S. and friends end in a dotted fragment
            if tail in ABBREV or (tail and "." in tail) or len(tail) == 1:
                out[-1] = out[-1] + " " + part
                continue
        out.append(part)
    return out


def render(text):
    """Put the reference tokens back as readable section numbers."""
    text = re.sub(r"(\u00a7+) ?Zx([0-9p]+)xZ ?",
                  lambda m: m.group(1) + m.group(2).replace("p", "."), text)
    return re.sub(r" ?Zx([0-9p]+)xZ ?",
                  lambda m: "\u00a7" + m.group(2 - 1).replace("p", "."), text)


def context(sents, i):
    """The sentence at i, padded per the author's rule if it is short."""
    n = len(sents[i].split())
    lo = hi = i
    if n < 15:
        lo = max(0, i - 1)
    if n < 10:
        hi = min(len(sents) - 1, i + 1)
    return " ".join(sents[lo:hi + 1]), (lo != i or hi != i)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(common.REPORTS, "xref_pairs.txt"))
    ap.add_argument("--only", help="restrict to references made from this section")
    args = ap.parse_args()

    files = {}     # section number -> path
    sources = []   # extra files that cite but cannot be cited
    for dirpath, _, names in os.walk(common.SECTIONS):
        for name in sorted(names):
            if not name.endswith(".tex"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8") as fh:
                head = fh.read(4000)
            m = re.search(r"\\(?:unnumbered)?label\{sec:([0-9.]+)\}", head)
            if m:
                files[m.group(1)] = path
            else:
                sources.append(path)

    # Cache each section's prose and its opening sentence.
    for path in sources:
        files.setdefault(os.path.splitext(os.path.basename(path))[0], path)
    prose = {num: prose_of(path) for num, path in files.items()}
    sents = {num: sentences(text) for num, text in prose.items()}

    pairs, unresolved, empty = [], [], []
    def order(k):
        try:
            return (0,) + tuple(common.numkey(k))
        except Exception:
            return (1, k)

    for num in sorted(files, key=order):
        if args.only and num != args.only:
            continue
        ss = sents[num]
        for i, s in enumerate(ss):
            for target in TOKEN_RE.findall(s):
                target = target.replace("p", ".")
                if target not in files:
                    unresolved.append((num, target, s))
                    continue
                citing, cpad = context(ss, i)
                ts = sents.get(target) or []
                if not ts:
                    empty.append((num, target))
                    continue
                cited, tpad = context(ts, 0)
                pairs.append((num, target, citing, cited, cpad, tpad))

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("# Cross-reference pairs\n#\n")
        fh.write("# Generated by finishing/tools/xref_pairs.py. Do not edit; regenerate.\n")
        fh.write("# For each reference: the citing sentence, then the opening sentence of\n")
        fh.write("# the section it points at. Short sentences are padded with their\n")
        fh.write("# neighbours; a padded block is marked (+context).\n#\n")
        fh.write("# What to look for: the citing sentence saying the target does something\n")
        fh.write("# the target does not open by doing. That is Q-041's class, and no tool\n")
        fh.write("# finds it.\n#\n")
        fh.write("# %d pairs from %d sections.\n\n" % (pairs and len(pairs) or 0, len(files)))
        last = None
        for num, target, citing, cited, cpad, tpad in pairs:
            if num != last:
                fh.write("\n" + "=" * 78 + "\n== FROM %s\n" % num + "=" * 78 + "\n")
                last = num
            fh.write("\n--- %s -> %s\n" % (num, target))
            citing = render(citing)
            cited = render(cited)
            fh.write("  CITING%s: %s\n" % (" (+context)" if cpad else "", citing))
            fh.write("  CITED %s: %s\n" % ("(+context)" if tpad else "         ", cited))
        if unresolved:
            fh.write("\n\n" + "=" * 78 + "\n== UNRESOLVED (%d)\n" % len(unresolved) + "=" * 78 + "\n")
            for num, target, s in unresolved:
                fh.write("  %s -> %s :: %s\n" % (num, target, s[:200]))
        if empty:
            fh.write("\n\n== TARGET HAS NO PROSE (%d)\n" % len(empty))
            for num, target in empty:
                fh.write("  %s -> %s\n" % (num, target))

    print("xref_pairs: %d pairs, %d sections, %d unresolved, %d empty targets"
          % (len(pairs), len(files), len(unresolved), len(empty)))
    print("wrote %s" % os.path.relpath(args.out, common.REPO))


if __name__ == "__main__":
    main()
