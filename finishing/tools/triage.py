#!/usr/bin/env python3
"""Propose a fate for every section, with the evidence behind it.

Fates under D-007 (revise, not rewrite):
  keep        leave substantially as is
  revise      voice, tics, closers, citations, dating  (the default)
  fold        heading disappears; text joins its nearest surviving ancestor
              (forced by the D-010 three-level cap)
  move        relocates to another chapter (D-010 folds chapter 8 into 7)
  merge?      candidate to merge into a named twin; the author picks which
              instance survives (D-013)
  cut         removed (D-010 explicit cuts)
  fill-or-cut heading with no body text: give it a paragraph or delete it

The author's ruling goes in the `fate` column of finishing/triage.tsv; this
tool only writes `proposed`. Rerunning never overwrites a decided row.
"""
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

OUT = os.path.join(common.REPO, "finishing", "triage.tsv")
MIRROR = os.path.join(common.REPORTS, "triage")
MAXLEVEL = 3

CLUSTER_A = {"5.4.3", "7.2.5.3", "4.6.3.1.2", "10.1.3", "8.2.1", "8.2.3",
             "8.3.1", "6.4.1.12", "10.3.2.1"}
CLUSTER_B = {"2.3.1", "2.3.2", "4.2.2", "4.2.2.1", "3.1.2.3.1.10", "9.2.3"}
HEADER = ["num", "title", "level", "words", "proposed", "fate", "target", "why", "evidence"]


def ancestor(num, level=MAXLEVEL):
    return ".".join(num.split(".")[:level])


def main():
    _, stats = common.read_tsv(os.path.join(common.REPORTS, "section_stats.tsv"))
    _, ledger = common.read_tsv(common.LEDGER_TSV)
    ev = {r["num"]: r["evidence"] for r in ledger}
    prior = {}
    if os.path.exists(OUT):
        _, old = common.read_tsv(OUT)
        prior = {r["num"]: r for r in old}

    rows = []
    for s in stats:
        num, lvl, words = s["num"], int(s["level"]), int(s["words"])
        e = ev.get(num, "")
        parts = num.split(".")
        cut_range = (num.startswith("6.4.1.") and len(parts) == 4
                     and parts[3].isdigit() and 1 <= int(parts[3]) <= 9)
        if cut_range:
            fate, why = "cut", "D-010 cuts the per-country survey 6.4.1.1-.9"
        elif words == 0:
            fate, why = "fill-or-cut", "heading with no body text at all"
        elif parts[0] == "8":
            fate, why = "move", "D-010 folds chapter 8 into chapter 7 as one geopolitics section"
        elif lvl > MAXLEVEL:
            fate, why = "fold", "D-010 caps the outline at 3 levels; text joins %s" % ancestor(num)
        elif num in CLUSTER_A:
            fate, why = "merge?", "one of 9 sections making the democracy-cooperation argument (D-013)"
        elif num in CLUSTER_B:
            fate, why = "merge?", "one of 6 sections making the emotional-intelligence argument (D-013)"
        elif "parallel:2.4-vs-7.4" in e:
            fate, why = "merge?", "part of the 2.4/7.4 parallel treatment (D-013)"
        elif lvl == 1:
            fate, why = "revise", "chapter opener" if words else "chapter heading"
        else:
            fate, why = "revise", "voice, tics, closers, citations, dating"

        # A section can need a structural fate AND still be one instance of a
        # repeated argument. The structural fate wins the column; the cluster
        # note is appended so the author still sees the second decision.
        extra = []
        if num in CLUSTER_A and fate != "merge?":
            extra.append("also 1 of 9 making the democracy-cooperation argument (D-013)")
        if num in CLUSTER_B and fate != "merge?":
            extra.append("also 1 of 6 making the emotional-intelligence argument (D-013)")
        if "parallel:2.4-vs-7.4" in e and fate != "merge?":
            extra.append("also part of the 2.4/7.4 parallel treatment (D-013)")
        if extra:
            why = why + "; " + "; ".join(extra)

        row = {"num": num, "title": s["title"], "level": lvl, "words": words,
               "proposed": fate, "fate": "", "target": "", "why": why, "evidence": e}
        if num in prior and prior[num].get("fate"):
            row["fate"] = prior[num]["fate"]
            row["target"] = prior[num].get("target", "")
        rows.append(row)

    common.write_tsv(OUT, HEADER, rows)

    os.makedirs(MIRROR, exist_ok=True)
    by_ch = collections.OrderedDict()
    for r in rows:
        by_ch.setdefault(r["num"].split(".")[0], []).append(r)
    for ch, rs in by_ch.items():
        lines = ["# Chapter %s triage" % ch, "",
                 "%d sections, %d words. Proposed fates below — change any you disagree with."
                 % (len(rs), sum(r["words"] for r in rs)), "",
                 "`revise` = voice/tics/citations only. `fold` = heading goes away, text stays.",
                 "`merge?` = you pick which instance of a repeated argument survives.", "",
                 "| # | Title | Words | Proposed | Why |", "|---|---|---|---|---|"]
        for r in rs:
            lines.append("| `%s` | %s | %d | **%s** | %s |"
                         % (r["num"], r["title"][:70], r["words"], r["proposed"], r["why"]))
        with open(os.path.join(MIRROR, "ch%02d.md" % int(ch)), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

    tally = collections.Counter(r["proposed"] for r in rows)
    words = collections.Counter()
    for r in rows:
        words[r["proposed"]] += r["words"]
    print("wrote %s and %d chapter mirrors\n" % (OUT, len(by_ch)))
    print("%-12s %6s %9s" % ("proposed", "count", "words"))
    for k, v in tally.most_common():
        print("%-12s %6d %9d" % (k, v, words[k]))
    decided = sum(1 for r in rows if r["fate"])
    print("\nauthor has ruled on %d of %d rows" % (decided, len(rows)))


if __name__ == "__main__":
    main()
