#!/usr/bin/env python3
"""Per-section statistics, and (with --seed-ledger) the initial work ledger.

Counts words, paragraphs, marked/unmarked list lines, and the generation's
signature tells: 'this report', 'In this section, we', 'In conclusion/summary'
closers, first-person plural density, cross-references, latest year mentioned,
dated system names.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

OUT = os.path.join(common.REPORTS, "section_stats.tsv")

LIST_ITEM = re.compile(r"^\s*(\(\d+\)|\d+[.)]|[-•*]|[a-z][.)])\s+\S")
CLOSER = re.compile(r"^\s*(In conclusion|In summary|In essence|Ultimately)\b", re.I)
YEAR = re.compile(r"\b(19[89]\d|20[0-4]\d)\b")
DATED = re.compile(r"\b(GPT-[234]|BERT|AlphaGo(?: Zero)?|AlphaZero|AlphaFold|Agent57|"
                   r"Watson|Rekognition|PredPol|GPT)\b")
TEMPORAL = re.compile(r"\b(currently|recent(?:ly)?|state-of-the-art|cutting-edge|"
                      r"latest|emerging|is being developed|in progress|proposed)\b", re.I)
# Matches both "see section 4.2" and a bare "Section 4.2 expounds ..." as the
# sentence subject. The first version missed the latter, which is the form the
# author actually writes, so cross-references were being under-counted.
XREF = re.compile(r"\b(?:see|in|per)\s+(?:section|chapter)\s+\d|"
                  r"\b(?:section|chapter)\s+\d+(?:\.\d+)*\b|"
                  r"previous section|subsequent chapters|earlier chapter", re.I)

HEADER = ["num", "title", "level", "chapter", "words", "paras", "list_marked",
          "list_unmarked", "closers", "we", "this_report", "in_this_section",
          "xrefs", "max_year", "dated_names", "temporal", "quotes", "hash_notes"]

LEDGER_HEADER = ["num", "title", "level", "words_v3b", "status", "action",
                 "quarry_src", "evidence", "decisions", "owner", "notes"]


def stats_for(path):
    with open(path, encoding="utf-8", newline="") as f:
        lines = f.readlines()
    body, quote, lst = [], 0, 0
    marked = unmarked = quotes = notes = 0
    for line in lines[1:]:
        s = line.strip()
        if s == "<<quote>>":
            quote += 1
            quotes += 1
            continue
        if s == "<</quote>>":
            quote -= 1
            continue
        if s == "<<list>>":
            lst += 1
            continue
        if s == "<</list>>":
            lst -= 1
            continue
        if s.startswith("<<h>>") and s.endswith("<</h>>"):
            body.append(s[5:-6].strip() + "\n")
            continue
        if s in ("<<box>>", "<</box>>"):
            continue  # a box is the author's own prose; its content counts
        if s.startswith("#"):
            notes += 1
            continue
        if quote > 0:
            continue  # epigraphs are third-party text, not the author's word count
        if lst > 0:
            # inside <<list>>: still prose for word-count purposes
            if LIST_ITEM.match(line):
                marked += 1
            body.append(line)
            continue
        body.append(line)
        if LIST_ITEM.match(line):
            unmarked += 1
    text = "".join(body)
    paras = [p for p in text.split("\n") if p.strip()]
    years = [int(y) for y in YEAR.findall(text)]
    return {
        "words": len(text.split()), "paras": len(paras),
        "list_marked": marked, "list_unmarked": unmarked,
        "closers": sum(1 for p in paras if CLOSER.match(p)),
        "we": len(re.findall(r"\bwe\b", text, re.I)),
        "this_report": len(re.findall(r"\bthis report\b", text, re.I)),
        "in_this_section": len(re.findall(r"\bin this section\b", text, re.I)),
        "xrefs": len(XREF.findall(text)),
        "max_year": max(years) if years else "",
        "dated_names": len(DATED.findall(text)),
        "temporal": len(TEMPORAL.findall(text)),
        "quotes": quotes, "hash_notes": notes,
    }


def main():
    _, order = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    order.sort(key=lambda r: common.numkey(r["num"]))
    rows = []
    for r in order:
        st = stats_for(os.path.join(common.REPO, r["path"]))
        st.update({"num": r["num"], "title": r["title"],
                   "level": common.level(r["num"]), "chapter": r["num"].split(".")[0]})
        rows.append(st)
    os.makedirs(common.REPORTS, exist_ok=True)
    common.write_tsv(OUT, HEADER, rows)
    tot = sum(r["words"] for r in rows)
    print("wrote %s: %d sections, %d words" % (OUT, len(rows), tot))
    by_ch = {}
    for r in rows:
        by_ch.setdefault(r["chapter"], [0, 0])
        by_ch[r["chapter"]][0] += r["words"]
        by_ch[r["chapter"]][1] += 1
    for ch in sorted(by_ch, key=int):
        print("  ch%-2s %6d words  %3d sections" % (ch, by_ch[ch][0], by_ch[ch][1]))

    if "--seed-ledger" in sys.argv:
        if os.path.exists(common.LEDGER_TSV):
            sys.exit("ledger.tsv exists; refusing to overwrite")
        led = [{"num": r["num"], "title": r["title"], "level": r["level"],
                "words_v3b": r["words"], "status": "untouched", "action": "",
                "quarry_src": "", "evidence": "", "decisions": "",
                "owner": "", "notes": ""} for r in rows]
        common.write_tsv(common.LEDGER_TSV, LEDGER_HEADER, led)
        print("seeded %s with %d rows" % (common.LEDGER_TSV, len(led)))


if __name__ == "__main__":
    main()
