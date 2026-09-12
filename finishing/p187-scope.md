# P187 — the September 12 Overleaf return, imported with its structure

Author instruction: **import `~/book-scratch/Sep12.zip`**, a round trip of the
2026-09-10 export edited in Overleaf. The dry run refused it, the scale was put
to the author with the numbers below, and the author confirmed the edit is
intended and asked for the structural work the import will not do.

## What the package was

95 files against the 138 that went out. The manifest inside it is byte-identical
to `antifascist-intelligence_2026-09-10.zip`, exported `2026-09-10T22:57Z` from
commit `af0f127`, so the lineage is the right one and the repository had not
moved since: **0 conflicts.** Internally the package is consistent — every
`\ref` resolves, every `\autocite` key has an entry — so it compiled in Overleaf
as it stood.

**The scale, measured on both packages by the same method before anything was
applied: 112,551 words out, 65,635 back.** Against the canonical count
`section_stats.py` produces, the book goes **110,842 words to 64,530** and
**214 pages to 137**. Chapter~3 loses 65 percent, chapter~11 73, chapter~5 68,
chapter~6 61, chapter~4 60, chapter~10 40 and chapter~9 20. Chapters~2, 7, 8
and 12 come back substantially as they went.

**It is a rewrite and not a compression.** Of the returned sentences over 60
characters, the share appearing nowhere in the exported text is **98 percent in
chapter~3, 100 in chapters~4 and~5, 85 in chapter~11**, against 1 to 6 percent
in chapters~2, 7, 8 and 12. The skeleton of chapter~3 survives — the four ways,
the bearer, the annealing figure, the ladder — carried by different prose.

## The four things the import refuses, and what each needed

The tool detects and reports a delete, an add, a renumber and a depth change,
and writes nothing when it finds one. Three of the four were present.

**One renumber was already in the returned text.** `06_01_01.tex` came back
labelled `sec:6.1` where `ORDER.tsv` said 6.1.1 — 6.1.1 promoted into the slot
its cut parent vacated. That single mismatch is what stopped the import; setting
the cell to 6.1 first, and passing `--no-sync-titles` so the three title copies
could be rewritten coherently rather than one cell at a time, let the prose land.

**43 section files were absent**, and the import deletes nothing. They were
removed with `git rm` and their rows taken out of all three TSVs.

**The cut left holes in the numbering, and holes are what a renumber is for.**
`\ref` regenerates every printed number since D-066, so a hole does not break a
reference — it breaks the correspondence between the label, `ORDER.tsv`, the
contents file and the number the reader sees. Nine sections moved:

| old | new | |
|---|---|---|
| 3.9 | 3.7 | subject moved into the vacated slot |
| 3.10 | 3.8 | subject moved into the vacated slot |
| 6.1.1 | 6.1 | the author's own promotion, already in the label |
| 6.3 | 6.2 | |
| 6.4 | 6.3 | |
| 6.4.1 | 6.3.1 | |
| 6.4.4 | 6.3.2 | |
| 9.1.3 | 9.1.1 | |
| 10.6 | 10.5 | |

`renumber-map_2026-09-12.tsv` carries those nine and the 43 cuts. Chapter~3's
two are a subject move and not a file move: `03_07.tex` and `03_08.tex` keep
their names and now carry what §3.9 and §3.10 carried, which is why the ledger
rows for 3.9 and 3.10 became the rows for 3.7 and 3.8 and the old 3.7 and 3.8
rows went out with the cut sections.

**Two compatibility aliases came back and were removed.** `06_01.tex` carried
`\label{sec:6.1.1}` beside `\label{sec:6.1}` and `09_01.tex` carried
`\label{sec:9.1.5}` beside `\label{sec:9.1}`, each keeping an old number
resolvable. The second had one live reference, at `08_03_04.tex:19`, which names
"§9.1.5's uniform error." **The claim survives in the new §9.1** — *the same
fact about deployment that makes a single bearer's error uniform* — so the
pointer was retargeted rather than cut. 14 references were remapped in all.

## Typography, and one repair that is not from this zip

The suite went green for the first time since D-263. Seven violations stood after
the prose landed, six of them arriving with the zip: four ASCII en dashes
(`Input--output`, `appearance--reality` twice, `reward--aversion`) and three
ASCII em dashes.

Two more classes are not in `check_typography.py` and were repaired on the
D-189 precedent, which is an unwritten uniform practice that an Overleaf edit
violates and the import repairs: **78 curly apostrophes** against `style.md`
§8's rule that the apostrophe stays straight — all 78 are possessives, and the
manuscript contains no opening single quote — and **19 unspaced em dashes**,
where the exported book had none in 112,551 words.

**The seventh violation is the author's own and predates the zip**: the straight
double quote at `01.tex:22`, last of the three `STATE.md` called a small fix
somebody should make. The other two were in files this edit rewrote. It was
fixed, which is a change outside the import and is recorded here for that reason.

## The bibliography

The cut stopped citing 147 sources. Following D-111's convention — refs.bib
corresponds to the book, and an entry that loses its citation moves rather than
disappears — **refs.bib goes 341 entries to 192, all cited, and
`unused_bibliography.bib` 60 to 209.**

**The Overleaf edit deleted two entries outright rather than leaving them
uncited**: `patterson1982slavery` and `hartman1997scenes`, the sources for
social death and for fungibility. Both were restored from `HEAD` into the unused
file so the record keeps them; neither term now appears anywhere in the book.

## What was checked, and what was not

`check_all.sh` passes: structure, the generated `sections.tex` and contents file,
233 cross-references resolving against 89 labels with none written out in prose,
typography, and the named-persons guard. `build_tex.sh` builds **137 pages with
zero undefined references and zero undefined citations.**

**The prose was not read.** Four chapters came back as new text and this pass
applied them, measured them and made the structure consistent around them. A
green suite says the structure survived the trip.

Three things were read and are recorded as findings rather than repaired:

**Chapter~11 uses `\textbf` as a run-in label** — `\textbf{Test.}`,
`\textbf{Unresolved issue.}`, `\textbf{Required access or authority.}` — 41
instances across 7 of its 8 sections. `style.md` §8 says `\textbf` is not used
in the prose at all and that its one use is a table header in §2.2. The device
is consistent enough across the new chapter to look deliberate, so it was left
for the author.

**Two sections now have a single child.** §9.1 keeps only 9.1.1 of its five
subsections, and §6.3 keeps two of four. Both are legal and both read oddly in a
contents list.

**Chapter~0's title came back as *Foreward***, which is a misspelling of
*Foreword*. It was applied as returned, the heading being authoritative (D-011).

## The record that is now stale

`xref-paragraphs-{related,unrelated}.md` are hand reads keyed to paragraphs, and
roughly 47,000 words of those paragraphs are gone. The same is true of
`claims.tsv`, `epigram.tsv`, `xref_shapes.tsv`, `negatives.tsv` and
`redundancy_*.tsv` in `reports/`. None was regenerated: the tool-made ones are
cheap to rerun when something needs them, and the two hand reads are not
regenerable at all. `QUESTIONS.md`'s forty-one open questions were not checked
against the new structure; several name sections that no longer exist.
