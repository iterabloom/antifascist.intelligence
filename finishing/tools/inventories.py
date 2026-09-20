#!/usr/bin/env python3
"""Find the inventory: a series of three or more items, none of them worked.

D-101's instruction names a shape rather than a rate, so this reports
candidates and not defects. An inventory sentence here is one carrying a
series of three or more coordinated items -- "X, Y, and Z", "X, Y, or Z" --
which is a syntactic test and catches plenty of prose that is doing real
work. The column that separates them is `cites`: a series with a citation
inside it is usually a worked case wearing a list's punctuation, and a series
with none is usually the shape the instruction is about. Neither is reliable
alone. Read the sentence.

Explicit `enumerate`/`itemize` items are counted separately, because those are
inventories by construction whether or not the prose inside them is worked.

What it cannot see: an inventory spread over consecutive sentences rather than
punctuated as a series -- "Retraining is one answer. Social insurance is
another. Wage subsidies are a third." -- which is the same shape and scores
zero here. Those were found by reading.

Usage:
    finishing/tools/inventories.py            # every chapter, summary
    finishing/tools/inventories.py 8 9 10     # those chapters, sentence by
                                              # sentence, to stdout
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

# A series of 3+ items: two or more commas before a coordinator, no sentence
# boundary between them. Deliberately requires the Oxford comma the style
# sheet uses, so "X, Y and Z" is missed rather than guessed at.
SERIES_RE = re.compile(r"[^,;:]+,[^,;:]+,\s*(?:and|or)\s+")
CITE_MARK = "CITEMARKER"
CITE_RE = re.compile(r"\\autocite\*?(?:\[[^\]]*\])*\{[^}]*\}")
# Sentence split: a terminator, a space, then a capital or a quote. Decimals
# and "U.S." survive; an abbreviation followed by a capitalized word does not.
SENT_RE = re.compile(r"(?<=[.!?])\s+(?=[\"\u201c(]?[A-Z])")


def sentences(paras):
    for p in paras:
        for s in SENT_RE.split(p):
            s = s.strip()
            if s:
                yield s


def scan(path):
    with open(path, encoding="utf-8") as fh:
        lines = [CITE_RE.sub(" " + CITE_MARK + " ", ln) for ln in fh]
    paras, st = common.tex_sections_of(lines)
    hits = []
    for s in sentences(paras):
        if SERIES_RE.search(s):
            plain = s.replace(CITE_MARK, "").split()
            hits.append({"words": len(plain),
                         "cites": s.count(CITE_MARK),
                         "text": " ".join(s.split())})
    return hits, st


def main(argv):
    want = set(argv[1:])
    rows = []
    # The locator is the label and the chapter comes from the path (D-470).
    # `ch` was the label's first dotted part, which stopped being a chapter
    # number when D-463 named the labels: int('opening').
    chapters = common.chapter_numbers()
    for label, title, path in common.section_headings():
        ch = chapters[path]
        if want and ch not in want:
            continue
        hits, st = scan(path)
        rows.append((label, title, ch, hits, st))

    if want:
        for label, title, ch, hits, st in rows:
            if not hits and not st["list_items"]:
                continue
            print("=" * 78)
            print(f"{label}  {title}   [list items: {st['list_items']}]")
            for h in hits:
                print(f"  -- {h['words']}w, {h['cites']} cite(s)")
                print(f"     {h['text']}")
        return 0

    per_ch = {}
    for label, title, ch, hits, st in rows:
        d = per_ch.setdefault(ch, {"secs": 0, "words": 0, "sents": 0,
                                   "inv": 0, "invwords": 0, "uncited": 0,
                                   "items": 0})
        with open(_path_of(label), encoding="utf-8") as fh:
            paras, _ = common.tex_sections_of(fh.readlines())
        d["secs"] += 1
        d["words"] += sum(len(p.split()) for p in paras)
        d["sents"] += sum(1 for _ in sentences(paras))
        d["inv"] += len(hits)
        d["invwords"] += sum(h["words"] for h in hits)
        d["uncited"] += sum(1 for h in hits if h["cites"] == 0)
        d["items"] += st["list_items"]

    print(f"{'ch':>3} {'secs':>5} {'words':>7} {'sents':>6} "
          f"{'inv':>5} {'uncited':>8} {'inv w':>7} {'inv%w':>6} "
          f"{'listitems':>10}")
    tot = {}
    for ch in sorted(per_ch, key=common.numkey):
        d = per_ch[ch]
        pct = 100.0 * d["invwords"] / d["words"] if d["words"] else 0.0
        print(f"{ch:>3} {d['secs']:>5} {d['words']:>7} {d['sents']:>6} "
              f"{d['inv']:>5} {d['uncited']:>8} {d['invwords']:>7} "
              f"{pct:>5.1f}% {d['items']:>10}")
        for k, v in d.items():
            tot[k] = tot.get(k, 0) + v
    pct = 100.0 * tot["invwords"] / tot["words"]
    print(f"{'all':>3} {tot['secs']:>5} {tot['words']:>7} {tot['sents']:>6} "
          f"{tot['inv']:>5} {tot['uncited']:>8} {tot['invwords']:>7} "
          f"{pct:>5.1f}% {tot['items']:>10}")
    return 0


_PATHS = None


def _path_of(label):
    global _PATHS
    if _PATHS is None:
        _PATHS = {n: p for n, _, p in common.section_headings()}
    return _PATHS[label]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
