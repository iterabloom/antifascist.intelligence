#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Negative claims made next to a citation: what a source does *not* say.

Built for Q-056's fourth mechanism, found at D-125. A claim that a source
says something can be checked by opening the source. A claim that a source
does *not* say something cannot: confirming an absence means reading the whole
document, and the document may not be readable at all -- the case that
prompted this was an eight-page audit report behind a legal agreement.

So the class is not one an audit catches. The only defence is to notice the
sentence being written, which is what this looks for.

Two tiers, both FLAGS and not verdicts:

    cited     a negation inside a sentence that carries a citation
    adjacent  a negation and a source-word in a sentence whose neighbour in
              the same paragraph carries a citation

Most hits in both tiers are negations about the world, not about a source --
"the model does not refuse", "a floor does not hold" -- and those are ordinary
prose. The one to read for is a negation whose subject is the cited work: the
paper, the study, the report, the ruling, its findings, its authors.

    finishing/tools/negatives.py                counts by tier and chapter
    finishing/tools/negatives.py --tier cited   every hit in one tier
    finishing/tools/negatives.py --section 12.1 every hit in one section
    finishing/tools/negatives.py --tsv          reports/negatives.tsv
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

OUT = os.path.join(common.REPORTS, "negatives.tsv")

# A negation that could be about a source. Deliberately wide: the cost of a
# false positive is one sentence read, and the cost of a miss is D-125.
NEGATIONS = [
    (r"\b(?:does|do|did) not\b", "does-not"),
    (r"\b(?:was|were|is|are) not among\b", "not-among"),
    (r"\bnowhere in\b", "nowhere-in"),
    (r"\b(?:says?|said) nothing about\b", "says-nothing"),
    (r"\b(?:makes?|made|contains?|carr(?:ies|y|ied)|offers?|"
     r"gives?|gave|names?|named|reports?|reported) no\b", "makes-no"),
    (r"\bno (?:mention|record|evidence|finding|analysis|version|account) of\b",
     "no-mention-of"),
    (r"\bnever (?:says?|said|claims?|claimed|mentions?|mentioned|"
     r"addresses|addressed|argues?|argued|finds?|found)\b", "never-verb"),
    (r"\b(?:is|are|was|were) absent (?:from|in)\b", "absent-from"),
    (r"\bnot (?:in|part of|within) (?:the|its|his|her|their)\b", "not-in"),
    (r"\bfails? to\b|\bfailed to\b", "fails-to"),
    (r"\bstops? short of\b|\bstopped short of\b", "stops-short"),
    (r"\bneither\b[^.]{0,80}\bnor\b", "neither-nor"),
    (r"\bnot what\b", "not-what"),
    (r"\bwithout (?:saying|claiming|finding|addressing|naming)\b",
     "without-verb"),
]

# Words that make a negation likely to be about the cited work rather than
# about the world. Used to promote an adjacent-sentence hit; a cited-sentence
# hit is listed whether or not one is present.
SOURCE_WORDS = re.compile(
    r"\b(?:paper|papers|study|studies|report|reports|audit|article|essay|"
    r"opinion|ruling|decision|guidance|complaint|meta-analysis|review|"
    r"survey|source|sources|author|authors|researchers|finding|findings|"
    r"document|documents|text|statute|act|recital|dissent|concurrence|"
    r"transcript|dataset|corpus|abstract|preprint|entry|book)\b",
    re.I)

CITE = re.compile(r"@@T?CITE:([^@]*)@@")
AUTOCITE = re.compile(r"\\(autocite|textcite)\{([^}]*)\}")
SENT = re.compile(r"(?<=[.!?…])\s+(?=[A-Z“‘(])")


def sentences_of(path):
    """[(paragraph_index, sentence, [cite keys])] for one section file."""
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    out, para = [], 0
    envs = []
    for raw in lines:
        line = raw.rstrip("\n")
        for m in re.finditer(r"\\(begin|end)\{(\w+\*?)\}", line):
            if m.group(1) == "begin":
                envs.append(m.group(2))
            elif envs:
                envs.pop()
        if any(e in common.TEX_QUOTE_ENVS for e in envs):
            continue                                   # epigraph, not ours
        if re.match(r"^\\(chapter|section|subsection)\*?\{", line) or \
           re.match(r"^\\(label|unnumberedlabel|addcontentsline)", line):
            continue
        if not line.strip():
            continue
        marked = AUTOCITE.sub(lambda m: " @@%sCITE:%s@@ " % (
            "T" if m.group(1) == "textcite" else "", m.group(2)), line)
        text = common.tex_prose_line(marked).strip()
        if not text:
            continue
        para += 1
        for s in SENT.split(text):
            keys = [k for m in CITE.findall(s) for k in m.split(",")]
            clean = re.sub(r"\s+", " ", CITE.sub("", s)).strip()
            if clean:
                out.append((para, clean, keys))
    return out


def hits():
    rows = []
    for num, _title, path in common.section_headings():
        sents = sentences_of(os.path.join(common.REPO, path))
        for i, (para, sent, keys) in enumerate(sents):
            found = [name for pat, name in NEGATIONS
                     if re.search(pat, sent, re.I)]
            if not found:
                continue
            src = bool(SOURCE_WORDS.search(sent))
            if keys:
                tier = "cited"
                near = ",".join(sorted(set(keys)))
            else:
                nb = [k for j in (i - 1, i + 1)
                      if 0 <= j < len(sents) and sents[j][0] == para
                      for k in sents[j][2]]
                if not (nb and src):
                    continue
                tier = "adjacent"
                near = ",".join(sorted(set(nb)))
            rows.append({"num": num, "tier": tier, "classes": " ".join(found),
                         "source_word": "yes" if src else "no",
                         "cites": near, "sentence": sent})
    return rows


HEADER = ["num", "tier", "classes", "source_word", "cites", "sentence"]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--tier", choices=("cited", "adjacent"))
    ap.add_argument("--section")
    ap.add_argument("--tsv", action="store_true")
    a = ap.parse_args()

    rows = hits()
    if a.tsv:
        common.write_tsv(OUT, HEADER, rows)
        print("wrote %s: %d rows" % (OUT, len(rows)))
        return
    if a.tier or a.section:
        sel = [r for r in rows
               if (not a.tier or r["tier"] == a.tier)
               and (not a.section or r["num"] == a.section)]
        for r in sel:
            print("%-8s %-8s %-14s %s" % (r["num"], r["tier"], r["classes"],
                                          r["cites"]))
            print("    %s" % r["sentence"])
        print("\n%d of %d rows" % (len(sel), len(rows)))
        return

    by = {}
    for r in rows:
        by.setdefault((r["tier"], r["num"].split(".")[0]), 0)
        by[(r["tier"], r["num"].split(".")[0])] += 1
    for tier in ("cited", "adjacent"):
        n = sum(v for (t, _), v in by.items() if t == tier)
        print("%s: %d" % (tier, n))
        for ch in sorted({c for (t, c) in by if t == tier}, key=int):
            print("   ch%-3s %d" % (ch, by[(tier, ch)]))
    print("\n%d rows. Candidates for a hand read, not defects." % len(rows))


if __name__ == "__main__":
    main()
