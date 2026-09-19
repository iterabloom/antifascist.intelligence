#!/usr/bin/env python3
"""Per-section statistics, and (with --seed-ledger) the initial work ledger.

Counts words, paragraphs, list items, and the generation's signature tells:
'this report', 'In this section, we', 'In conclusion/summary' closers,
first-person plural density, cross-references, latest year mentioned, dated
system names.

Ported to LaTeX at D-070. It had gone on counting dialect envelopes after
D-065 removed them, which made every structural column meaningless -- the
xrefs column read 0 across all 162 sections against 773 real references --
and left the word count wrong in 142 of 162 sections. The prose extraction
now lives in common.tex_sections_of, shared with xref_content.py, and its
conventions are documented there.

The word count is the words a reader reads: epigraphs are excluded as
third-party text, citations are apparatus and do not count, a reference
counts as the one number it prints, and run-in heads and box titles count
because they are read.

The `paras` column counts blocks, and a run-in head is a block. Prose
paragraphs are `paras` minus `runins`. Until D-384 the column was a line count
and read 1,527 against a true 1,114, inflated by 413 across the 28 files that
hold hard-wrapped prose (D-344 measured 359 across 21 files, on a smaller book).
The word count did not change by a single word when this was fixed, the sum over
lines being the sum over paragraphs, which is the check that the repair touched
the grouping and nothing else.

D-344 also put section 6.4.1's true paragraph count at 19. That figure was a
hand estimate and is wrong: the section has 21 blocks, of which 1 is a run-in
head, and the estimate merged the opening paragraph into the heading's block
because the heading, its label and the first paragraph sit on consecutive lines
with no blank line between them.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

OUT = os.path.join(common.REPORTS, "section_stats.tsv")

# Enumeration typed into a paragraph rather than set as a list -- style.md
# section 4's "prose wearing a list's clothes". Real \item lines are counted
# separately, by common.tex_sections_of.
LIST_ITEM = re.compile(r"^\s*(\(\d+\)|\d+[.)]|[-•*]|[a-z][.)])\s+\S")
CLOSER = re.compile(r"^\s*(In conclusion|In summary|In essence|Ultimately)\b", re.I)
YEAR = re.compile(r"\b(19[89]\d|20[0-4]\d)\b")
DATED = re.compile(r"\b(GPT-[234]|BERT|AlphaGo(?: Zero)?|AlphaZero|AlphaFold|Agent57|"
                   r"Watson|Rekognition|PredPol|GPT)\b")
TEMPORAL = re.compile(r"\b(currently|recent(?:ly)?|state-of-the-art|cutting-edge|"
                      r"latest|emerging|is being developed|in progress|proposed)\b", re.I)
# Cross-references are \ref now and are counted from the markup, not matched
# in the prose (common.tex_sections_of). What is left for a regex is the
# vaguer prose gesture, which \ref cannot express and check_xrefs.py does not
# see either.
XREF_VAGUE = re.compile(r"previous section|subsequent chapters|earlier chapter",
                        re.I)

HEADER = ["num", "title", "level", "chapter", "words", "paras", "list_items",
          "list_unmarked", "closers", "we", "this_report", "in_this_section",
          "xrefs", "vague_xrefs", "cites", "max_year", "dated_names",
          "temporal", "epigraphs", "boxes", "runins"]

LEDGER_HEADER = ["num", "title", "level", "words_v3b", "status", "action",
                 "quarry_src", "evidence", "decisions", "owner", "notes"]


def stats_for(path, unknown=None):
    with open(path, encoding="utf-8", newline="") as f:
        lines = f.readlines()
    paras, st = common.tex_sections_of(lines, unknown)
    text = "\n".join(paras)
    years = [int(y) for y in YEAR.findall(text)]
    return {
        "words": sum(len(p.split()) for p in paras), "paras": len(paras),
        "list_items": st["list_items"],
        "list_unmarked": sum(1 for p in paras if LIST_ITEM.match(p)),
        "closers": sum(1 for p in paras if CLOSER.match(p)),
        "we": len(re.findall(r"\bwe\b", text, re.I)),
        "this_report": len(re.findall(r"\bthis report\b", text, re.I)),
        "in_this_section": len(re.findall(r"\bin this section\b", text, re.I)),
        "xrefs": st["refs"], "vague_xrefs": len(XREF_VAGUE.findall(text)),
        "cites": st["cites"],
        "max_year": max(years) if years else "",
        "dated_names": len(DATED.findall(text)),
        "temporal": len(TEMPORAL.findall(text)),
        "epigraphs": st["epigraphs"], "boxes": st["boxes"],
        "runins": st["runins"],
    }


def main():
    _, order = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    order.sort(key=lambda r: common.numkey(r["num"]))
    rows, unknown = [], set()
    for r in order:
        st = stats_for(os.path.join(common.REPO, r["path"]), unknown)
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
    if unknown:
        # A macro this tool has never been taught is dropped, which silently
        # skews every count in the file that uses it. D-065 is what happens
        # when that goes unnoticed, so it is loud.
        print("  WARNING: unknown LaTeX commands, dropped from the prose: %s"
              % ", ".join(sorted(unknown)))
        print("  Teach them to common.tex_prose_line before trusting these numbers.")

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
