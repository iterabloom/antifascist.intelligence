# P153 — Q-109 closed on option 2: the quorum keeps the record of a refused attempt

Author ruling on Q-109: **option 2** — one clause naming the quorum as the keeper.
(The instruction read "22"; there is no option 22, and 2 was the recommendation.)

## The gap this closes

`09_01_05.tex:33`'s second amendment condition requires that an attempt reach the
record **whether it carries or fails**. `:31` lists the five terms it is built on:
contents published before deployment, weights held against single-party
retraining, the running model attested, a quorum adverse in interest, a bond
forfeited when the record shows the floor gone.

**None of the five registers a proposal that was refused.** §3.3 `:29`'s witnessed
sequence signs *each change to the weights* and counts it from the published one —
and a proposal the quorum declined changes none, so there is nothing to sign. The
attestation reports what is running. The bond is forfeited on a removal that
happened.

## The edit

One clause, on the condition sentence:

> The attempt has to reach the record whether it carries or fails, and a proposal
> that fails moves no weights, so the parties who had to agree are the ones who
> record that they were asked.

**It states the gap and closes it in one movement**, which is why the clause carries
*a proposal that fails moves no weights* rather than naming the keeper bare. Without
the reason, putting the record in the quorum's hands reads as arbitrary.

## Two wording constraints

***Refusal* was unavailable.** The natural phrasing is *a refusal moves no weights*,
and in this book *refusal* is what a system does — the load-bearing term of
chapters~2 and 3. A second sense, a quorum declining a proposal, would collide with
it. *A proposal that fails* is the replacement.

***The parties who had to agree* rather than *the quorum*.** It is condition one's
own phrase — *The number of parties who must agree to a change* — one sentence
earlier, so the two conditions now tie together, and §9.1.5 does not have to import
§3.3's *quorum* to say who keeps the record.

## What was not claimed

**Nothing says the arrangement is secure.** The quorum is the only party to the five
positioned to keep this record, and §3.3 `:39` is explicit that the parties to a
threshold scheme are selected by whoever assembles the deployment and that **nobody
has implemented adverse interest for a floor.** The clause says who would record it,
not that the record would be honest. **The custody objection is untouched** and
`:39` of this section already says the procedure is no route of appeal.

**Q-109's option 3 was not taken.** Naming the mechanism unbuilt would have added a
second unbuilt item to a section whose argument depends on the procedure being
runnable, which is the cost that option carried when it was filed.

## Verification

Suite green. `refresh_order_shas.py` run. Scratchpad lualatex build: **196 pages, 0
undefined references and 0 undefined citations**; the clause reads back out of
`pdftotext` in position.

§9.1.5's censuses are unchanged against HEAD: **8 antithesis sentences, 0 clusters,
7 `deixis --hard` hits.** **0 new shared six-word runs**, 1,622 book-wide before and
after — checked because *the parties who had to agree* is close to `:31`'s *how many
parties had to agree*.

## Figures

133 sections, **1 changed**. 99,547 → **99,571** words (+24); §9.1.5 1,939 → 1,963.
**196 pages unchanged.** **231 cross-references unchanged.** 324 bibliography
entries unchanged. 0 `\textit`.
