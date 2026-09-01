#!/usr/bin/env python3
"""Census the corrective antithesis, and locate every instance for a hand read.

The shape is *X rather than Y*, *not X but Y*, *that is not a P, it is a Q* --
a claim made by discarding an alternative. Q-038 tracked one of its forms,
"rather than", from P35 through P49; this covers the family.

WHAT THIS IS FOR, AND WHAT IT CANNOT DO. The author's test is not whether an
instance is defensible. Two sweeps have already asked that -- P12 over chapter 5
and P49 over chapters 2 to 4 -- and both found the instances defensible at a
repair rate near 1 in 30. The test is narrower: **was the discarded alternative
one a reader would actually have reached for?** That is a judgment about what a
reader arrives at a sentence expecting, and no regular expression reaches it.
So the hits below are CANDIDATES FOR A HAND READ, NOT DEFECTS, and this tool is
deliberately not in check_all.sh.

What it does do is find the density, which is the author's actual diagnosis:
per-section rate per 1,000 words, so a reading can start where the ear flattens
rather than at chapter 1.

What the reading found, and why --clusters exists. Applied one instance at a
time the author's test yields about 1 in 30, which is what P12 and P49 both
measured and what a third sample confirmed. The complaint it does not reach is
density: an isolated antithesis reads as a correction and two inside sixty words
do not, so the audible unit is the PAIR, not the instance. P49 recorded the same
threshold from the other direction, at about 120 words. --clusters finds them.

  --census      per-section rates, highest first (default)
  --list SEC    every instance in a section, with its sentence
  --clusters    sentences carrying two or more, and pairs within --window words
  --window N    proximity threshold for --clusters (default 60)
  --chapter N   restrict any mode to one chapter
"""
import argparse, glob, io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import tex_prose_line

SHAPES = [
    ("rather-than", re.compile(r"\brather than\b", re.I)),
    ("not-but",     re.compile(r"\bnot\b[^.;:]{1,60}?\bbut\b", re.I)),
    ("is-not-a",    re.compile(r"\b(?:is|was|are|were)\s+not\s+(?:a|an|the)\b", re.I)),
    ("and-not",     re.compile(r"\band not\b", re.I)),
    ("instead-of",  re.compile(r"\binstead of\b", re.I)),
    ("as-against",  re.compile(r"\bas against\b", re.I)),
]
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")


def sections(chapter=None):
    for f in sorted(glob.glob(os.path.join(ROOT, "manuscript/sections/ch*/*.tex"))):
        src = io.open(f, encoding="utf-8").read()
        m = re.search(r"\\label\{sec:([^}]*)\}", src)
        num = m.group(1) if m else os.path.basename(f)
        if chapter and num.split(".")[0] != str(chapter):
            continue
        body = re.sub(r"\s+", " ",
                      "\n".join(tex_prose_line(l) or "" for l in src.split("\n")))
        yield num, f, body


def constructions(s):
    """Distinct antitheses in one sentence.

    Overlapping matches are ONE construction, not two: *not a weak version of
    one somebody can but a different kind of object* fires both `is-not-a` and
    `not-but` over the same words. Counting patterns rather than constructions
    overstated the doubled sentences by 14 out of 47 when this was first run.
    """
    spans = []
    for k, p in SHAPES:
        for m in p.finditer(s):
            spans.append((m.start(), m.end(), k))
    spans.sort()
    merged = []
    for a, b, k in spans:
        if merged and a < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(b, merged[-1][1]), merged[-1][2] + "/" + k)
        else:
            merged.append((a, b, k))
    return merged


def hits(body):
    for s in re.split(r"(?<=[.!?]) +", body):
        found = [k for _, _, k in constructions(s)]
        if found:
            yield found, s.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--census", action="store_true")
    ap.add_argument("--list", metavar="SEC")
    ap.add_argument("--clusters", action="store_true")
    ap.add_argument("--window", type=int, default=60)
    ap.add_argument("--chapter", type=int)
    a = ap.parse_args()

    if a.list:
        for num, _, body in sections():
            if num != a.list:
                continue
            n = 0
            for found, s in hits(body):
                n += 1
                print("[%2d] %-24s %s" % (n, ",".join(found), s))
            print("\n%s: %d sentences carrying the shape, %d words"
                  % (num, n, len(body.split())))
            return
        sys.exit("no section %s" % a.list)

    if a.clusters:
        n_dbl = n_pair = 0
        for num, _, body in sections(a.chapter):
            marks, pos = [], 0
            for s in re.split(r"(?<=[.!?]) +", body):
                k = len(constructions(s))
                if k:
                    marks.append((pos, k, s.strip()))
                pos += len(s.split())
            for i, (p0, k, s) in enumerate(marks):
                if k > 1:
                    n_dbl += 1
                    print("\n%-7s DOUBLED (%d in one sentence)\n    %s" % (num, k, s))
                if i + 1 < len(marks) and marks[i + 1][0] - p0 <= a.window:
                    n_pair += 1
                    print("\n%-7s PAIR (%d words apart)\n    %s\n    %s"
                          % (num, marks[i + 1][0] - p0, s, marks[i + 1][2]))
        print("\n%d doubled sentences, %d pairs within %d words."
              % (n_dbl, n_pair, a.window))
        print("Candidates for a hand read, not defects.")
        return

    rows, tot_n, tot_w = [], 0, 0
    for num, _, body in sections(a.chapter):
        w = len(body.split())
        n = sum(len(f) for f, _ in hits(body))
        tot_n += n
        tot_w += w
        if w >= 150:
            rows.append((1000.0 * n / w, n, w, num))
    rows.sort(reverse=True)
    print("%-9s %5s %7s %8s" % ("section", "hits", "words", "per1k"))
    for r, n, w, num in rows:
        print("%-9s %5d %7d %8.2f" % (num, n, w, r))
    print("\n%d instances over %d words = %.2f per 1,000."
          % (tot_n, tot_w, 1000.0 * tot_n / tot_w))
    print("Sections under 150 words are counted in the total and omitted above.")
    print("Candidates for a hand read, not defects.")


if __name__ == "__main__":
    main()
