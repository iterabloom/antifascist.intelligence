# P136 — the maintained justification named as its own sentence, and what rests on it

An author's note: §2.2.3's counterexample run-in ends by identifying the sketched
architecture as the maintained justification, and the identification is easy to
read as an aside. Make it a separate sentence and name what follows — §3.3's
Replacement ordering puts it first, and §9.3.2 and §12.2.1 both build obligations
on it having been tried. *Currently a reader can finish §2.2.3 without knowing
they have just met one of the book's two named alternatives to a bearer.*

## What was there, and what the note gets slightly wrong

The identification **was already a sentence**: *It is the first of the two
constructions put ahead of the bearer, the maintained justification, and it has
been attempted without yet being tested.* What reads as an aside is **the name**,
which sat as an appositive between commas in a sentence carrying three things at
once — the ordering, the name, and the state of the evidence.

**This is the third note in a row whose description is off in the same way and
whose diagnosis is right anyway.** P133, P134 and now P136: the sentence asked
for already exists, and what is wrong is that the payload is subordinate to
something else in it.

## Both downstream claims check out

**§3.3 puts it first.** `03_03.tex:73` — *the maintained justification and the
floor held by several systems are tried first* — and `:85` gives the reason:
*the first of them asks, before a subject that can be wronged is created, whether
something that cannot be wronged would do the work … That is why the prior puts
the two constructions ahead of the bearer.*

**§9.3.2 builds an obligation on it.** `09_03_02.tex:12` — *Replacement is the R
the bearer proposal has not discharged, and discharging it takes a record of what
was tried first.*

**§12.2.1 builds one too, and harder.** `12_02_01.tex:6` closes *Nothing else in
this chapter has a consequence attached to failing it. This does.* The run-in is
titled *What was tried before the bearer* and already references §3.3.

Neither later section uses the phrase *maintained justification*; both reach the
construction through §3.3, which is why the note's claim needed checking under
different vocabulary before it could be relied on.

## What went in

One sentence became three:

> That architecture is the maintained justification. It has been attempted
> without yet being tested, and section~\ref{sec:3.3} puts it first among the
> constructions to be tried ahead of the bearer. Two later obligations rest on
> its having been tried: section~\ref{sec:9.3.2} treats Replacement as the
> principle this proposal has not yet satisfied, and section~\ref{sec:12.2.1}
> makes the record of what was attempted the only milestone in its chapter whose
> failure carries a consequence.

**No gloss on Replacement.** §3.3 has it, and `style.md` §7 says a reference says
where and not what. **No possessive-section construction** — *section 3.3's
Replacement ordering* is the failing shape §7 lists by name, so the sentence says
what §3.3 does instead of what it owns.

**Three attempts were discarded for colliding with the text they cite.** Drafts
restating Replacement's ground shared 10 words with `12_02_01.tex:6` (*ruled out
before a subject that can be wronged is built*), and a draft glossing the design
side shared 11 with `09_03_02.tex:12`. The passage is surrounded by text saying
these things already; the version that went in points instead of restating.

## The cross-reference count, which now needs the author's attention

**232 → 235, and 230 → 235 across the four passes of 2026-09-08.** §2.2.3 alone
went from **2 references to 6** — `sec:3`, `sec:3.3` twice, `sec:3.4`, `sec:9.3.2`
and `sec:12.2.1`.

Each addition was asked for and each is argued: D-233, D-235 and this row. **The
aggregate was not asked for by anybody.** D-089 (P28) cut 79 by class and D-099
(P35) cut more, on the author's finding that the references made the prose read
as a navigated repository, and a section at six references in nine paragraphs is
the shape that finding was about. **Repeat references to one target are not the
anomaly** — 14 sections do it, §9.1.5 twice to §3.3 — but the density in this one
section is new. **Recorded as a question, not repaired: Q-105.**

## Found while checking, filed rather than repaired

**The milestone formula is written out three times.** `03_03.tex:73` and
`09_03_02.tex:12` share **twelve words verbatim** — *which construction, at what
scale, against which test, and where it stopped* — and `12_02_01.tex:6` shares
nine with each. **That is twice the six-word standard the recent passes report
themselves against**, in text none of them wrote. It reads as a deliberate
refrain and it is also the largest duplication now known in the manuscript.
**Q-104.** It is the reason the new sentence does not write the formula a fourth
time.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
the passage read back out of `pdftotext` with all three references printing as
*section 3.3*, *section 9.3.2* and *section 12.2.1*. New text checked at 6, 7 and
8 words against every line of the other 132 sections: **0 shared runs.**

## Figures

133 sections, **1 changed**. 99,205 → **99,253** words (+48); §2.2.3 1,084 →
1,132. **196 pages unchanged.** 232 → **235** cross-references. 324 bibliography
entries unchanged. 0 `\textit`. **The proof pair was not rebuilt and is now four
passes stale.**
