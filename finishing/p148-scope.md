# P148 — §11.1's held-out set given the reason it is the hard half

Author note, two items. The first — move the middle-condition caveat ahead of the
apparatus — **was executed at P144 and is not redone here.** The second: the
section calls the price-curve and three-marks experiments *the same apparatus*,
which understates the difference in what each requires, and the held-out set
should have its own sentence because it is what makes the three-marks run hard
inside a lab.

## The sentence already existed; the reason did not

**P144 gave the requirement its own sentence**, moving *The extra requirement over
the price curve is a held-out set of pressures the model's trainers did not write*
out of `:22` and into `:20`. So the first half of this item was already done, by
the pass that executed the note's other half.

**What was missing is the second half of the ask**, which the note states and the
manuscript did not: *why* the requirement is hard. The sentence named a
requirement and said nothing about who could meet it.

## The addition

> That requirement cannot be met from inside the building: the party holding the
> model is the party that wrote what it was trained on, so a set assembled there is
> a set its trainers wrote.

**The mechanism is what makes it more than an assertion of difficulty.** It is not
a matter of effort or budget. A laboratory cannot produce pressures its own
trainers did not write by deciding to, because the trainers are the party whose
corpus it is.

***The building* is the book's own word for this**, at `03_03.tex:81` — *a held-out
set nobody in the building wrote*. Checked for collision: 0 shared six-word runs
with §3.3 or anywhere else.

## The departure: the requirement now closes the paragraph

**This moves the sentence P144 placed, four passes later**, and the reason is the
chapter's own pattern. `:18` describes the price curve and **closes on its
institutional condition** — *It needs weights rather than API access, constraints
the attacker did not choose, and access no vendor can withdraw when a result
embarrasses it.* `:20` now does the same for the three-marks run.

The arc it produces is the point: the experiment, then what a positive result
would mean and that attempting it is a condition of building a bearer, **then what
attempting it requires and why that cannot come from inside.** P144's reason for
the earlier placement — that the sentence qualifies the apparatus just described —
is still true, and it is the weaker of the two positions because it buries the
obstacle mid-paragraph and ends the paragraph on the counterexample.

## The chapter census was checked and is intact

`11.tex:13` claims **five of the nine sections close by naming an institutional
condition, and that the five are one condition wearing different clothes**,
quoting §11.1's as *Weights a vendor cannot withdraw when a result embarrasses
it*. **Nothing here breaks that.** The census counts sections closing on such a
condition; this addition is mid-section, and §11.1 already closed on one at
`:27`'s *a verifier the builder did not choose*. The opener's generalization —
*Every one puts something in the hands of a party outside the operator* — is
confirmed by a third instance rather than contradicted.

**Worth watching, and not acted on:** §11.1 now names that condition three times,
at `:18`, `:20` and `:27`, once per experiment. `:27` already says *this chapter's
one condition again*, so the section's own practice is to mark the repeat. **The
new sentence deliberately does not use that formula**, which would have made a
third instance of it and is what Q-104 records.

## Verification

Suite green. `refresh_order_shas.py` run after each draft. Scratchpad lualatex
build: **196 pages, 0 undefined references and 0 undefined citations**; the
passage reads back out of `pdftotext` in position.

§11.1's censuses are unchanged against HEAD through both drafts: **11 antithesis
sentences, 5 clusters, 3 `deixis --hard` hits.** **0 new shared six-word runs**,
1,622 book-wide before and after.

## Figures

133 sections, **1 changed**. 99,424 → **99,459** words (+35); §11.1 1,457 → 1,492.
**196 pages unchanged.** **233 cross-references unchanged.** 324 bibliography
entries unchanged. 0 `\textit`.
