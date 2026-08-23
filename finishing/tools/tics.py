#!/usr/bin/env python3
"""Census the generation's verbal tics and voice markers.

Under a revise-only pass (D-007) this is the main body of prose work, so the
list has to be concrete enough to edit against. Writes reports/tics.tsv and
reports/voice.tsv (per-section voice markers).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

TICS = [
    ("foster", r"\bfoster(?:s|ed|ing)?\b"),
    ("crucial", r"\bcrucial(?:ly)?\b"),
    ("robust", r"\brobust(?:ness|ly)?\b"),
    ("pivotal", r"\bpivotal\b"),
    ("paramount", r"\bparamount\b"),
    ("multifaceted", r"\bmulti-?faceted\b"),
    ("landscape", r"\blandscape\b"),
    ("realm", r"\brealm\b"),
    ("delve", r"\bdelv(?:e|es|ed|ing)\b"),
    ("harness", r"\bharness(?:es|ed|ing)?\b"),
    ("navigate", r"\bnavigat(?:e|es|ed|ing|ion)\b"),
    ("underscore", r"\bunderscor(?:e|es|ed|ing)\b"),
    ("leverage", r"\bleverag(?:e|es|ed|ing)\b"),
    ("intricate", r"\bintricat(?:e|ely|ies|y)\b"),
    ("nuanced", r"\bnuance[ds]?\b"),
    ("holistic", r"\bholistic(?:ally)?\b"),
    ("tapestry", r"\btapestry\b"),
    ("myriad", r"\bmyriad\b"),
    ("encapsulate", r"\bencapsulat(?:e|es|ed|ing)\b"),
    ("amalgamation", r"\bamalgamat(?:e|ed|ion)\b"),
    ("indispensable", r"\bindispensable\b"),
    ("imperative (adj)", r"\bimperative\b"),
    ("cornerstone", r"\bcornerstone\b"),
    ("in essence", r"\bin essence\b"),
    ("ultimately", r"\bultimately\b"),
    ("moreover", r"\bmoreover\b"),
    ("furthermore", r"\bfurthermore\b"),
    ("additionally", r"\badditionally\b"),
    ("it is important to note", r"\bit is (?:important|worth) (?:to note|noting)\b"),
]

VOICE = [
    ("this report", r"\bthis report\b"),
    ("this work/document", r"\bthis (?:work|document|volume)\b"),
    ("we (subject)", r"\bwe\b"),
    ("our", r"\bour\b"),
    ("we propose/recommend/argue", r"\bwe (?:propose|recommend|argue|believe|advocate|urge|suggest)\b"),
    ("in this section, we", r"\bin this (?:section|chapter), we\b"),
    ("closer: in conclusion", r"^\s*In conclusion\b"),
    ("closer: in summary", r"^\s*In summary\b"),
]


def bodies():
    _, order = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    order.sort(key=lambda r: common.numkey(r["num"]))
    for r in order:
        with open(os.path.join(common.REPO, r["path"]), encoding="utf-8", newline="") as f:
            lines = f.readlines()
        keep, quote = [], 0
        for line in lines[1:]:
            s = line.strip()
            if s == "<<quote>>":
                quote += 1
                continue
            if s == "<</quote>>":
                quote -= 1
                continue
            if s.startswith("<<h>>") and s.endswith("<</h>>"):
                keep.append(s[5:-6].strip() + "\n")
                continue
            if quote > 0 or s.startswith(("#", "<<", "<</")):
                continue  # box tags are skipped here but their text is kept
            keep.append(line)
        yield r["num"], r["title"], "".join(keep)


def main():
    secs = list(bodies())
    total_words = sum(len(t.split()) for _, _, t in secs)
    trows = []
    for name, pat in TICS:
        rx = re.compile(pat, re.I | re.M)
        n = sum(len(rx.findall(t)) for _, _, t in secs)
        insec = sum(1 for _, _, t in secs if rx.search(t))
        trows.append({"tic": name, "count": n, "sections": insec,
                      "per_10k": "%.1f" % (10000.0 * n / total_words)})
    trows.sort(key=lambda r: -r["count"])
    common.write_tsv(os.path.join(common.REPORTS, "tics.tsv"),
                     ["tic", "count", "sections", "per_10k"], trows)

    vrows = []
    for num, title, text in secs:
        row = {"num": num, "title": title, "words": len(text.split())}
        for name, pat in VOICE:
            row[name] = len(re.compile(pat, re.I | re.M).findall(text))
        vrows.append(row)
    cols = ["num", "title", "words"] + [n for n, _ in VOICE]
    common.write_tsv(os.path.join(common.REPORTS, "voice.tsv"), cols, vrows)

    print("%d sections, %d body words" % (len(secs), total_words))
    print("\ntop tics (count / sections / per 10k words):")
    for r in trows[:14]:
        print("  %-26s %5d  %3d  %5s" % (r["tic"], r["count"], r["sections"], r["per_10k"]))
    print("\nvoice markers, book-wide:")
    for name, _ in VOICE:
        n = sum(r[name] for r in vrows)
        ins = sum(1 for r in vrows if r[name])
        print("  %-28s %5d in %3d sections" % (name, n, ins))


if __name__ == "__main__":
    main()
