#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""What the prose charges the reader that the argument does not need.

The taxonomy is not invented here. It is read off the author's own hand edits
to eight randomly sampled pages, applied between 331f0a5 and fc65cd5, and every
class below cites the edit it comes from. The author's account of what he was
doing: not conciseness for its own sake, but not annoying the reader and not
wasting their time.

Each class is a FLAG, not a verdict -- the same footing as style.md sections 3
and 3a. A hit means read the sentence; it does not mean cut it.

    finishing/tools/reader_tax.py                 counts by class and chapter
    finishing/tools/reader_tax.py --class meta    every hit in one class
    finishing/tools/reader_tax.py --section 8.3   every hit in one section
    finishing/tools/reader_tax.py --tsv           reports/reader_tax.tsv
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

# Each class: (key, description, [(pattern, note)]). Patterns run over the
# rendered prose of one sentence, case-insensitive.
CLASSES = [
    ("meta", "The book narrating itself instead of its subject", [
        (r"\bthis (?:book|chapter|section)(?:'s)? (?:is|was|exists|does|spends?|"
         r"contains?|needs?|takes?|turns?|opens?|closes?|sets? out|argues?|"
         r"proposes?|describes?|covers?|treats?)\b",
         "07.tex: 'This chapter exists because the book kept making the same "
         "discovery' -> the claim itself"),
        (r"\b(?:is|are) what this (?:book|chapter|section) is about\b",
         "08_03_01: 'the gap between the two is what this section is about' cut"),
        (r"\bnone of (?:that|this) is this (?:section|chapter)'s job\b",
         "06_04_04: cut outright"),
        (r"\bthis (?:chapter|section) (?:contains|has) (?:none|no) \w+",
         "07_04: 'and this chapter contains none of it' cut"),
        (r"\bwhat follows is (?:not|the)\b",
         "11_05: 'What follows is not another method...; it is' -> 'Below I "
         "describe'"),
        (r"\bthe (?:version|kind|sort) (?:this|the) book needs\b", ""),
        (r"\bthis book'?s? (?:design |governance |technical )?chapters?\b",
         "11_04: 'the fairness metrics and reward penalties this book's design "
         "chapters describe' -> 'penalties.'"),
        (r"\b(?:close to|about|roughly|nearly) a (?:third|quarter|half) of its "
         r"(?:length|words)\b",
         "03.tex: 'close to a third of its length' cut"),
        (r"\bthe rest of the (?:chapter|section|book) turns on\b",
         "03.tex: the whole announcing sentence cut"),
    ]),
    ("origin", "How the author came to see it, which the reader did not ask", [
        (r"\bit took me\b", "07_04: 'and it took me most of this book to see it' cut"),
        (r"\bI (?:kept|came to see|only later|had been assuming|realized)\b", ""),
        (r"\bin the course of writing\b", ""),
        (r"\bas I (?:wrote|drafted|worked)\b", ""),
        (r"\b(?:this|that) (?:book|chapter) kept\b", "07.tex"),
    ]),
    ("selfassess", "The prose grading its own claim", [
        (r"\bdoes real work\b", "03.tex: 'That reframing does real work in this book. It'"),
        (r"\bwhich is correct\b", "07_04: cut"),
        (r"\bthe (?:harder|more useful|more interesting|real|serious) "
         r"(?:and \w+ )?(?:problem|question|point) is\b",
         "08_02_03: 'The harder and more useful problem is' -> 'but what about'"),
        (r"\b(?:much )?(?:harder|deeper) and more \w+\b",
         "03.tex: 'two much harder and more answerable questions'"),
        (r"\bit cuts against most of what\b", "08_02_03: cut"),
        (r"\bis worth more than it sounds\b", ""),
        (r"\bshould be made out loud\b", "03.tex: cut"),
        (r"\b(?:doing|has been doing) silent work\b", "03.tex: cut"),
    ]),
    ("echo", "The negated restatement that repeats the clause before it", [
        (r"\band never (?:beneath|below|above|under) it\b",
         "03.tex: 'operating above it and never beneath it' -> 'above it'"),
        (r"\bit is not\.\s", "11_08: 'built on the assumption that it does. It is "
                             "not.' -> 'is not settled.'"),
        (r"\bis not hypothetical\b", "06_04_04: 'It is not hypothetical elsewhere.' cut"),
        (r"\bor only looks like it does\b", "11_04: cut"),
        (r"\bwith a confidence its output gives no sign of\b", "11_08: cut"),
        (r"\brather than a one-time (?:order|policy|event)\b",
         "06_04_04: contrastive tail cut"),
        (r",\s*not a \w+ of it,", "08_03: 'not a side effect of it,' cut"),
    ]),
    ("filler", "Intensifiers that add emphasis and no information", [
        (r"\bit is exactly the\b", "09_03_02: 'it is exactly the graded-versus-"
                                   "bright-line question' -> 'it is the'"),
        (r"\bis not actually\b", "09_03_02: 'is not actually silent' -> 'is not silent'"),
        (r"\b(?:close to|about|nearly) \d+ documented instances\b",
         "11_04: '60 documented instances' -> '60 instances'"),
        (r"\bthree specific \w+", "11_05: 'three specific difficulties' -> "
                                  "'three unsolved difficulties'"),
        (r"\bcase too:", "09_03_02: 'for that case too:' -> 'for that case:'"),
        (r"\bvulnerable to exactly this\b", "11_04: -> 'this antipattern'"),
    ]),
    ("deixis", "A demonstrative whose referent the reader has to reconstruct", [
        (r"^(?:This|That|It) (?:is|has|was|does|makes|leaves|gives) ",
         "07_04 'This is not an objection' -> 'This observation is not'; "
         "11_08 'That is not a complaint' -> 'That verdict is not'; "
         "11_08 'This has already reshaped' -> 'This result has'"),
        (r"\bwhat supplies them\b", "07_04: -> 'what supplies those protections'"),
        (r"\bexcluding it\b", "09_03_04: -> 'excluding affect'"),
    ]),
    ("pointer", "A cross-reference standing in for the thing it points at", [
        (r"section~\\ref\{sec:[\d.]+\}'s\b",
         "seven sites: \"section 2.1.2's structural signature\" -> "
         "'the four features section 2.1.2 uses to define fascism'"),
        (r"\bstructural signature\b",
         "the phrase the author replaced everywhere it stood for the definition"),
    ]),
    ("nominal", "A noun where the sentence had a verb available", [
        (r"\b(?:been )?implicated in the\b",
         "08_03_01: 'implicated in the spread of misinformation and the hardening "
         "of political polarization' -> 'spread misinformation and hardened'"),
        (r"\bthe (?:spread|hardening|erosion|creation|application|deployment|"
         r"introduction) of\b", ""),
        (r"\bdoes most of the work in \w+ing\b",
         "08_03_01: 'does most of the work in determining' -> 'mostly determines'"),
        (r"\bplays? an? (?:key|central|important|major)? ?role in\b", ""),
        (r"\bis a matter of\b", ""),
        (r"\beverything the \w+ does is what that situation needs\b",
         "09_03_02: -> 'That situation calls for'"),
    ]),
]

SENT_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z“\"'(\d])")


def sentences(text):
    return [s.strip() for s in SENT_END.split(text) if s.strip()]


def scan():
    """[(chapter, num, path, class, note, sentence)] over the whole book."""
    _, rows = common.read_tsv(
        os.path.join(common.SECTIONS, "ORDER.tsv"))
    rows.sort(key=lambda r: common.numkey(r["num"]))
    hits = []
    for r in rows:
        path = os.path.join(common.REPO, r["path"])
        with open(path, encoding="utf-8") as f:
            lines = f.read().split("\n")
        paras, _ = common.tex_sections_of(lines)
        ch = r["num"].split(".")[0]
        for para in paras:
            for sent in sentences(para):
                for key, _desc, pats in CLASSES:
                    for pat, note in pats:
                        if re.search(pat, sent, re.I):
                            hits.append((ch, r["num"], r["path"], key, note, sent))
                            break
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--class", dest="klass")
    ap.add_argument("--section")
    ap.add_argument("--chapter")
    ap.add_argument("--tsv", action="store_true")
    args = ap.parse_args()

    hits = scan()
    if args.klass:
        hits = [h for h in hits if h[3] == args.klass]
    if args.section:
        hits = [h for h in hits if h[1] == args.section]
    if args.chapter:
        hits = [h for h in hits if h[0] == args.chapter]

    if args.tsv:
        out = os.path.join(common.REPORTS, "reader_tax.tsv")
        common.write_tsv(out, ["chapter", "num", "path", "class", "sentence"],
                         [{"chapter": h[0], "num": h[1], "path": h[2],
                           "class": h[3], "sentence": h[5]} for h in hits])
        print("wrote %s (%d rows)" % (out, len(hits)))
        return 0

    if args.klass or args.section or args.chapter:
        for ch, num, _p, key, note, sent in hits:
            print("\n%-10s %-9s %s" % (num, key, sent[:400]))
            if note:
                print("           from: %s" % note[:150])
        print("\n%d hits" % len(hits))
        return 0

    by_class = {}
    by_chapter = {}
    for ch, num, _p, key, _n, _s in hits:
        by_class[key] = by_class.get(key, 0) + 1
        by_chapter.setdefault(ch, {}).setdefault(key, 0)
        by_chapter[ch][key] += 1
    keys = [k for k, _d, _p in CLASSES]
    print("%-12s %s" % ("class", "hits"))
    for k, desc, _p in CLASSES:
        print("  %-11s %4d   %s" % (k, by_class.get(k, 0), desc))
    print("\n%-4s %s" % ("ch", "  ".join("%-9s" % k for k in keys)))
    for ch in sorted(by_chapter, key=int):
        print("%-4s %s" % (ch, "  ".join("%-9d" % by_chapter[ch].get(k, 0)
                                         for k in keys)))
    print("\ntotal %d hits" % len(hits))
    return 0


if __name__ == "__main__":
    sys.exit(main())
