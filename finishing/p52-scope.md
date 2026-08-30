# P52 — the reader-cost pass, generalized from the author's own hand edits

**Instruction.** The author sampled eight pages at random with
`finishing/tools/choose-a-random-page.py`, edited them by hand, and applied the
result between `331f0a5` and `fc65cd5`. Then: *"The task now is to generalize
them so that you improve the rest of the manuscript in the same manner… my
improvements tended to improve conciseness. But I was not targeting conciseness
per se. I was focusing on not annoying the reader and not wasting their time."*

**Method.** The eight before/after pairs were ignored as such; the pass reads
the range `331f0a5..fc65cd5` instead, which is what the author actually applied.
Thirty-eight paragraphs changed there across seventeen section files. Every
edit was classified, and the classes below are the taxonomy the rest of the
manuscript was then read against — 153 sections, in `ORDER.tsv` order, read
whole rather than grepped. `finishing/tools/reader_tax.py` locates candidates in
the four classes a regular expression can find; it did not decide anything.

## The taxonomy, each class with the author's edit it comes from

| Class | What it is | The author's instance |
|---|---|---|
| **meta** | The book narrating itself instead of its subject | `07.tex`: *"This chapter exists because the book kept making the same discovery in two places"* → the claim itself |
| **origin** | How the author came to see it | `07_04`: *"and it took me most of this book to see it"* cut |
| **selfassess** | The prose grading its own claim | `03.tex`: *"That reframing does real work in this book. It gives…"* → *"That reframing gives…"* |
| **announce** | The sentence that says the next sentence is coming | `03.tex`: *"One distinction has been doing silent work in all three of those arrivals, and it should be made out loud"* cut entire |
| **echo** | The negated restatement of the clause before it | `03.tex`: *"operating above it and never beneath it"* → *"above it"* |
| **filler** | Intensifiers carrying emphasis and no information | `09_03_02`: *"it is exactly the"* → *"it is the"*; *"is not actually silent"* → *"is not silent"* |
| **deixis** | A demonstrative whose referent the reader must reconstruct | `07_04`: *"This is not an objection"* → *"This observation is not an objection"* |
| **pointer** | A cross-reference standing in for the thing it points at | seven sites: *"section 2.1.2's structural signature"* → *"the four features section 2.1.2 uses to define fascism"* |
| **nominal** | A noun where the sentence had a verb | `08_03_01`: *"implicated in the spread of misinformation and the hardening of political polarization"* → *"spread misinformation and hardened political polarization"* |
| **inventory** | A series of three where one example does the work | `08_02_03`: *"a course to enroll in, a curriculum to sit through, a public MOOC to find"* → *"a course to enroll in"* |

**The two moves that spend words rather than saving them**, and the reason the
instruction is not about conciseness. **Pointer** costs words at every one of
its seven sites and buys the reader a lookup they no longer have to make.
**Vividness**: *"concludes a group should be surveilled"* → *"concludes an
entire demographic should be surveilled, deported, imprisoned, or otherwise
scapegoated."* Both were applied here where the same conditions held.

## What was done

**100 files, 371 insertions, 381 deletions. 95,095 → 94,017 words**, a cut of
1,078, or 1.1 percent — against the 7.8 percent the author cut from the eight
pages he read. The difference is the point: his pages were sampled at random and
carried the tax at its ordinary density, and this pass cut only where a
particular sentence was doing the thing, not to a quota.

Ninety-eight of the 153 sections changed. Of the seventeen section files the
author had already edited, only three were touched again, and none of his
sentences was revised.

**Four defects were found by reading rather than by the taxonomy**, and they are
worth more than the class edits:

- **Section 12.3, the book's last section, said "The rest of this chapter is
  what the project is for and how anyone would know it was working."** Sections
  12.1 and 12.2 are what that describes, and both are behind the reader by then.
  A forward pointer at content already passed. Now names them.
- **Section 12.1.1 referred twice to "the old list"** — the list four sentences
  above it, called old because a revision replaced it. Editorial archaeology of
  the class D-099 cut, surviving in the conclusion.
- **Three prose cross-references used the glossary's `§` locator form** where
  the other 363 in the manuscript use `section~\ref`. One of them, at 9.3.2,
  mixes both inside a single clause: *"once §2.4.1's threshold work in
  section 9.3.1 has been done."* This is the `§` class the author's own commit
  message records repairing; these three survived it.
- **Section 6.1 cited `benjamin2019race` twice in two adjacent sentences**, the
  second time inside a clause that also called the account *"more useful to this
  chapter than a coinage."* Both went.

**One structural cut.** Section 6.3.4's six-item bulleted list of explainability
challenges lost two items — *complexity and nonlinearity*, and *legal and
ethical exposure* — because the paragraph immediately above the list already
states both. Nothing else in the manuscript lost a list item.

**Run-in heads renamed, where a heading stated a conclusion or named the book
rather than its subject** (style.md §10's rule, applied to the book): *"The
rationalist objection, which is the strongest thing said against all of this"* →
*"The rationalist objection"*; *"Two independence claims the rest of the chapter
turns on"* → *"Two independence claims"*; *"The scale problem, and what this book
does about it"* → *"…and what to do about it"*; *"Why this chapter is here"* →
*"Structure, not indictment"*; *"Why this is not a footnote"* →
*"Permissibility"*; *"What This Geopolitics Means for the Rest of the Book"* →
*"What the geopolitics leaves to design"*.

## What this pass did not do

- **No claim changed anywhere.** Every edit is a cut, a substitution of a word,
  or a rewrite of a sentence into the same assertion. Where a cut would have
  taken content with it, the sentence was left standing.
- **No citation was checked against its source**, and none was added or removed
  except the duplicate at 6.1.
- **The measurement in the detector is not a defect count.** `reader_tax.py`
  reports 285 hits after the pass against 310 before, and most of what remains
  is legitimate: `deixis` at 232 was always a candidate pool rather than a
  finding, since a demonstrative whose referent is the previous sentence is
  fine. The `meta` class, which is the one that tracks the author's central
  edit, went from 63 to 45.
- **Run-in head capitalization was left alone.** The manuscript mixes sentence
  case and Title Case (chapter 9's heads are Title Case, chapter 3's are not).
  That is a real inconsistency and a separate ruling.
- **The proof pair was rebuilt after this pass** and is current at 191 pages.
  The page count did not move: the 1,078 words came out without the book
  losing a page.

`check_all.sh` green. `ORDER.tsv` checksums refreshed. 98 ledger rows tagged
D-117.
