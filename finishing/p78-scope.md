# P78 — the corrective antithesis cut for density, not for defensibility

**The author's finding.** *X rather than Y*, *not X but Y*, *that is not a P, it
is a Q* is the dominant sentence shape in the manuscript. **Each instance is
doing something** — almost always correcting a reading the reader might
plausibly have taken — **but at this density the correction stops registering as
correction.** Section~3.9's separation of what survives from what goes has to
compete with three hundred other antitheses. The proposed pass: find every
*rather than* and ask whether the discarded alternative was one a reader would
actually have reached for; where it was not, drop it.

**The diagnosis holds. The proposed instrument does not reach it, and the
measurement says so before the reading starts.**

## The instruction and the diagnosis point at different things

The test *was the discarded alternative live?* is a per-instance test. It has
been run twice: **P12 over chapter~5** (152 instances) and **P49 over chapters~2
to 4** (110 read), plus a 25-instance sample of chapter~6. **All three landed at
1 repair in 25 to 37.** A third sample taken here agrees:

| section | instances read | candidates |
|---|---|---|
| 3.9 | 17 | **1** |
| 11.5 | 7 | **0** |
| 12.2.2 | 6 | **0** |
| 9.3.2 | 11 | **0** |
| 9.3.3 | 7 | **0** on the test — 1 defect of another class |
| 10.6 | 4 | **0** |

Run book-wide over the never-swept instances that is roughly 13 repairs, and the
density moves 611 → 598. **The flattening the finding describes would be
untouched**, because the instances that survive four passes are the ones a
reading keeps. That is Q-038's own recorded prediction, now confirmed a fourth
time.

**What the reading does surface is proximity.** An isolated antithesis reads as a
correction; two inside sixty words do not. P49 recorded the same threshold from
the other direction — *the tic is audible where two instances sit inside about
120 words* — and then did nothing with it, because its brief was per-instance.
**The audible unit is the pair, not the instance**, and that is measurable.

**Put to the author before any edit was made.** The ruling was both, proximity
first, with section~3.9 exempt and the density taken out of its competition
instead.

## A correction to a figure this pass reported to the author

The first census said **40 doubled sentences**. It was **37**. Fourteen of the
forty-seven sentences matching two patterns match them **over the same words** —
*not a weak version of one somebody can but a different kind of object* fires
`is-not-a` and `not-but` across one construction. Counting patterns rather than
constructions overstates doubling by about a third. `antithesis.py` now merges
overlapping spans, and the docstring carries the number so the mistake is not
made again. **The corrected baseline is 611 instances, 37 doubled sentences and
143 pairs.**

## What was cut, and what it is not

25 conversions across 19 files, all of them in chapters~6 to 12. **In every case
both halves of the pair were live**, which is the point: the repair is not to
delete a bad antithesis but to state one of two good ones positively.

| | example |
|---|---|
| shape dropped, claim kept | *structural and not fixable with more data* → *structural, and more data does not reach it* |
| second statement of a contrast the sentence already made | *see how the verdict shifts depending on who is empaneled, instead of collapsing every annotator into one fixed ground truth* |
| word already carrying the contrast | *NIST's **voluntary** framework as a common technical reference ~~rather than a binding rule~~* |
| an echo, not a pair | 6.1.1 said *rather than merely inherit it* twice in 59 words |

**No claim was removed and no citation touched.** Section~3.9 and the whole of
chapter~3 are untouched, which the diff shows.

## Two defects of other classes, found by an instrument aimed at something else

**Section~9.3.3 said the same thing twice.** *A named successor guardian, decided
in advance rather than litigated after the fact by whoever happens to hold the
hardware*, and two paragraphs later *a named successor guardian decided in advance
rather than settled afterward by whoever holds the hardware*. **P71's class,
inside one section rather than across two.** Cut from the second on P71's own
rule — the paragraph that already carries the claim keeps it — leaving the
sentence its actual new content, the third-party obligation enforceable without
the beneficiary asserting anything.

**Section~8.3.1 had an unresolvable demonstrative.** *A system tuned to maximize
time-on-platform has no built-in reason to prefer accurate content over
inflammatory content — the two are not the same objective, and engagement
optimization only ever targets the first one.* **On one reading of *the two* the
sentence is true and on the other it is backwards**, and nothing in the sentence
picks. Named rather than guessed at: *engagement optimization only ever targets
engagement*.

## Measurements

| | before | after |
|---|---|---|
| instances | 611 | **583** |
| per 1,000 words | 6.69 | **6.40** |
| doubled sentences | 37 | **25** |
| pairs within 60 words | 143 | **126** |
| book | 91,151 | **90,981 words**, down 170 |
| pages | 182 | **182** |
| sections · `\ref{sec:}` · `refs.bib` | 136 · 463 · 300 | **unchanged** |

Calibration set for all contrastive constructions is 2.90 per 1,000. **The book
is still at 2.2 times it.**

`check_all.sh` green after `refresh_order_shas.py`; 0 undefined references and 0
undefined citations.

## What this pass did not do

**The per-instance test was applied to every instance read in the course of the
proximity pass — about 170 of them — and not to the roughly 300 isolated
instances in chapters 6 to 12.** On four passes of evidence those would yield
about ten repairs. Recorded as Q-060 rather than run.

**Section~3.9 is now among the densest sections in the book**, at 9.19 per 1,000
against a book at 6.40, because it was exempted while everything around it was
cut. That is the ruling working as intended — its antitheses land harder because
fewer compete — and it is also the reason a later reader should not take the
per-section table as a defect list.
