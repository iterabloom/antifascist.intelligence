# P195 — §11.5a given its own number, and chapter 11's numbering closed

P194 imported the September 13 Overleaf return and left the one thing in it that
the invariant suite could not see: a second `\section` inside `11_05.tex`,
labelled `sec:11.5a`, carrying the author's own note that the label was temporary
and the renumber belonged to a proofreading pass. **The author read that finding
and asked for the fix.** This is it.

**The whole renumber cost one cross-reference.** `02_02_01.tex` was the only place
in the manuscript pointing into the shifted range, and it pointed at the
face-reading section.

## What was done

**The file was split.** `11_05.tex` keeps *Can a Multi-Agent Floor Resist Collusive
Capture?* and ends where its fourth rubric ends. The second section moved to a new
`11_06.tex` as *Can a Population Coordinate Without Converging?*, and its label
became `sec:11.6`. **The author's comment block came out with it** — it described a
state that no longer exists.

**Three files were renamed and their labels shifted**, in reverse order so no name
collided:

| was | is | label |
|---|---|---|
| `11_06.tex` | `11_07.tex` | `sec:11.6` → `sec:11.7` |
| `11_07.tex` | `11_08.tex` | `sec:11.7` → `sec:11.8` |
| `11_08.tex` | `11_09.tex` | `sec:11.8` → `sec:11.9` |

Renamed with `git mv`, so the history follows the content rather than the number.

**One cross-reference moved.** `02_02_01.tex:25` — *This is why section~\ref{sec:11.7}
states the open question as one about the instrument* — now points at `sec:11.8`,
which is *What Does a Face-Reading System Measure?*, the section it always meant.
It prints as *section 11.8*.

**`renumber-map_2026-09-13.tsv`** records the four moves. Notes written before
today keep the old numbers and this file is the translation, which is why the
record files were not rewritten: `STATE.md`, `DECISIONS.md` and the earlier scope
files still say §11.7 for the face-reading section, correctly, as of when they
were written.

**The three record files gained a row and lost three numbers.** `ORDER.tsv`,
`outline.tsv` and `ledger.tsv` all carry 91 rows. The new ledger row is
`author-drafted` — a value this column has not held before, its 89 other rows all
reading `agent-drafted`; the prose is the author's, written in Overleaf, and
nothing in `tools/` reads the column for logic. `action` is `new` and `words_v3b`
is empty, there being no 2023 ancestor, which matches §10.3 and §10.4.

`gen_book.py` regenerated `sections.tex` at 91 inputs, `headings.py --write-toc`
regenerated the contents, `refresh_order_shas.py` cleared the digests.

## The markup defect underneath it

Splitting the file put the new section beside its siblings on one page, and they
did not match. **§11.6's four rubrics used `\runin` and every other rubric in
chapter~11 uses a bare `\textbf`.** `\runin` expands to
`\par\medskip\noindent\textbf{#1}\par\nopagebreak\smallskip`, so it sets the label
on its own line with the body indented beneath it; a bare `\textbf` on its own
source line runs the label into the paragraph it opens. **On printed page 111 the
two shapes sat one above the other**, §11.5's *Unresolved issue.* inline and
§11.6's alone on a line.

**The counts point the other way from the fix, and the fix is still right.**
Book-wide `\runin` is the convention — 124 uses in 35 files against 50 `\textbf`
in 8 — so the author's markup followed the book and chapter~11 is the holdout.
But the two commands are not doing one job. Chapter~11 marks its display
sub-heads with `\subsection*` and its four rubric labels with inline `\textbf`,
and the rubrics are lead-ins rather than headings. **§11.6 was converted to
`\textbf`, matching the seven sections it sits among**, and the page was
re-rasterized and read: it now reads as one chapter.

**`style.md` §8 is wrong about this and was left alone.** It says `\textbf` "is
not used in the prose at all: its only use is a table header in §2.2." There are
50 uses; 49 are chapter~11's rubrics and one is that table header. Correcting the
style sheet is a decision about which convention chapter~11 should end up in, not
a typo fix, and it is not made here.

## What was verified

**Every label's name now equals the number LaTeX assigns it.** Read out of
`book.aux`, where `\newlabel` records the resolved value: **91 labels, 0
divergences.** That is the invariant that was broken — references always resolved
and always landed correctly, and it was the label names that had come loose — and
**no tool in the repository checks it.** `check_xrefs.py` verifies that references
resolve and that no number is typed into prose, which is a different thing.

The printed contents and `table-of-contents.txt` agree on all nine chapter~11
entries. The build is **156 pages with 0 undefined references and 0 undefined
citations**, and the suite is green at 91 sections.

## One measurement moved, and it is not prose

**`section_stats.py` reports 74,608 words against P194's 74,648.** The 40 words
are exactly the author's comment block, counted word for word: `tex_prose_line`
strips commands and unknown macros but **does not strip `%` comments**, so
commented text has been counting as prose. Nothing was cut. **P194's figure was
inflated by 40** for as long as the comment was in the tree, and any earlier
figure taken while a comment sat in a section file carries the same error.

## What was not done

**The seven sections in chapter~11 still using `\textbf` were not swept to
`\runin`**, nor `style.md` §8 corrected — see above; that is a ruling.

**The renumber was not propagated into the record files** and must not be: they
are dated records and `renumber-map_2026-09-13.tsv` is how they are read.

**Nothing else in the September 13 return was revisited.** The prose is still read
rather than audited, chapters~4, 5 and~11 are still unread as prose — §11.6 is
new prose inside one of them — and `QUESTIONS.md`'s forty-one open questions have
now gone eight passes unchecked.
