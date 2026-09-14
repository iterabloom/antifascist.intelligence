# P214 — the author's 50-item list against navigational and self-referential commentary

The author supplied a numbered list of 50 edits in four batches, each item
giving find-text, a replacement or a delete instruction, and a one-line reason.
**This is P213's list continued against an adjacent habit.** P213 removed the
sentence that credits the book with a virtue. P214 removes the sentence that
tells the reader what the book is about to do, grades an example before giving
it, or announces that a conclusion has arrived here from somewhere else in the
book.

**Every item was applied as written.** Where an item specified a replacement,
the replacement is the author's text and not drafted here. No item was added,
skipped, or altered, and **no independent search for the class was run this
pass** — unlike P213, every edit here came from the list.

## Shapes the list removes

**The staged introduction.** *There is a name for an apparatus that works this
way, and it was not coined about software* (item 22), *The mechanisms that
combine them are easy to name and easy to overrate* (34), *Assembling that list
is easy, and the assembling hides what separates the items on it* (35), *The
word* independent *does the work* (9), *The general form is worth stating once,
because the book meets it repeatedly* (3). In each case the next sentence
performs the introduction. What went was the announcement of it.

**The announced arrival.** *That is section 3.5's halt in institutional form*
(36), *It is section 3.5's guardianship argument arriving in a new place* (40),
*That is section 9.3.5's slope instrument … turned on this book's own proposal*
(39), *The worked case thus produces the hybrid described in section 3.5* (10),
*Custody reproduces here at the scale of the population, as section 3.1 said it
would* (16), *That is the guardianship problem arriving as an engineering
requirement* (46), *This is the failure section 9.3.4 is built to prevent … at
the top of the state* (49). **This shape is the reason the pass moves the
cross-reference count**: eight of these carried a `\ref`, and the replacement
states the local consequence instead of naming its origin.

**The graded example.** *and the second instance is the purer one* (29), *RLHF
is the purest technical instance available* (31), *The revenue is the
uninteresting half* (41), *The more interesting effect is nearer* (15). The
author's reasons say the evidence follows in the next sentence and can be
assessed there.

**The navigational aside.** *That bears on the difficulty two paragraphs above*
(43), *Run the fourth interception position backwards* (11), *That is one
direction to read the fact in. There is another.* (5), *That distinction matters
because the two gaps have different fixes, and only one of them has a fix at
all* (47).

**The converted lament.** *Calling it fixable converts a lament into a
specification* (48), *Take that as philosophy and it is arguable. Take it as a
description of the software above and it is a specification* (23), *That
disposes of a framing running through the whole field* (2), *The chapter has
been documenting the axiom being added and measuring it with a ruler that reads
the addition as evidence of health* (33). Each states that an argument has
landed, beside the argument.

## What the pass does to the cross-reference apparatus

**Ten `\ref`s were removed and one added; 230 → 221.** The removals are items 4
(§2.2), 10 and 14 (§3.5), 16 (§3.1), 18 (§3.2), 36 (§3.5), 39 (§9.3.5), 40
(§3.5), 45 (chapter 3) and 49 (§9.3.4). The addition is item 44's pointer to
§9.1.2, which the replacement text names. All 221 resolve against 88 labels.

**One section lost its last inbound reference: §9.3.5.** Item 39's sentence in
§8.3.3 was the only `\ref{sec:9.3.5}` in the book. **The section's content is
not orphaned** — §9.3.5 defines the slope instrument under its own run-in head,
*Measure the slope, not the level*, and §8.3.3's surviving sentence makes the
comparison in its own terms — but nothing now points a reader from the
application to the definition. **This was not repaired**: restoring a reference
is the shape the item removed.

**Item 39 also took out the book's only inline gloss of the instrument at that
site**, *measure whether the cost of dissent is rising, not whether a channel
exists*. §9.3.5 still carries the definition.

## Downstream effects checked

**§2.4.1's *The two readings do not conflict* survives item 5's deletion.** The
deleted pair, *That is one direction to read the fact in. There is another*, was
what labelled the two readings as two. Both readings are still on the page —
`02_04_01.tex:11` rules out suffering, `:13` establishes owner-controlled
continuity — and the two sentences after the phrase name each one. The phrase
now resolves forwards rather than backwards. **No wording was added.**

**§9.1.1 still refers to chapter 3 after item 45.** The count goes 4 → 3, at
`09_01_01.tex:38`, `:41` and `:56`; `:41` is the paragraph immediately before
the one item 45 rewrote. An earlier report from inside this run said item 45
removed the section's only chapter-3 reference. **That was wrong.**

**§9.3.5's own slope definition, §7.2's use of *recuperation* after item 30, and
the `\runin` heads left adjacent to items 23, 27 and 29's paragraph deletions
were checked on the page.** The remaining sections were checked by the exact
find-text match and the invariant suite, not re-read whole.

## A committed report was found corrupted, and restored

**`finishing/toc_v4.tsv` and `reports/toc_v4.md` were regenerated at commit
`30d548b` earlier today, and the regeneration destroyed what they record.**
`toc_v4.py` applies the P0–P1 triage rulings to the 282-section v3b outline and
joins word counts **by section number**. Run today, it attaches the current
manuscript's per-section words to historical rows that mean different sections:
the file now read *Chapter 1: Introduction — 971 w* where v3b's chapter 1 is 370
words, and *§1.1 — 0 w* for a section that had 167. The projected total went
105,688 → 50,824, which projects nothing.

**The repository's own rules say not to run it.** `finishing/README.md:27` lists
`toc_v4.py` among the one-shot P0–P1 instruments "kept because they record how
the structure was decided and not because anything should run them again," and
D-075 records `toc_v4.tsv` and `reports/toc_v4.md` among the files that "record
what was true when generated," on the renumber-map convention.

**Both files are restored to their state at `30d548b^`**, verified against
`ledger.tsv`'s `words_v3b` column: chapter 1 reads 370 w again. **This pass did
not rerun them.** They belong on the stale list permanently, which brings it to
seven.

## Reports

**Every report a tool regenerates was rerun, except `toc_v4.md` above.**
**Eight moved**: `claims.tsv`, `dated.tsv`, `epigram.tsv`, `section_stats.tsv`,
`voice.tsv`, `xref_content.tsv`, `xref_pairs.txt` and `xref_shapes.tsv`.
**Three regenerated byte-identical**: `tics.tsv`, `negatives.tsv` and
`headings_reconcile.md`. **Seven stay stale and none can be fixed here**: the four
`redundancy*` files need a package this machine does not have,
`list_candidates.tsv` and `triage-summary.md` are one-shot P0–P1 instruments,
and `toc_v4.md` is one that must not be rerun.
`xref-paragraphs-{related,unrelated}.md` are hand reads keyed to paragraphs this
pass cut, and were not re-read.

**Measured:** 88 sections, **77,279 body words** (from 78,249; 970 removed),
**159 pages, unchanged**, 221 cross-references
against 88 labels, 226 bibliography entries all cited, 0 undefined references
and 0 undefined citations. Suite green.

**The page count did not move and that is worth flagging.** 970 words is about
two and a half pages of body text at this book's density, and the book built at
159 pages before and after. The deleted text is confirmed absent from the PDF —
`pdftotext` finds none of items 2, 41 or 48's sentences — so the build is
current. **Why the count held was not investigated.** The cuts are spread over
28 sections, and a book with 88 section heads has slack that absorbs them, but
that is a guess and not a measurement.
