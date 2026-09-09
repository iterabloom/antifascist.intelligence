# P149 — §11.3 given the half of §2.1.2's finding it had dropped

Author note, two items. The second — the feature-4 limit, that a detector tuned to
drift will not register a movement that announces itself — **was executed at P143
and is not redone here**; `11_03.tex:11` has carried it since, as *An institution
that announces its decoupling has no slope to measure, and a detector built this
way would not see it.* The first item is what this pass does.

## What §11.3 had, what it lacked, and where the overstatement was

§2.1.2 `:53` is the finding, in four moves: a tool reporting the four features
accuses everybody; **the opposite failure is no safer**, a tool tuned until it
reports nothing supplying false assurance; better engineering fixes neither; and
**both are governed by what the tool may output and to whom, which the
specification has to carry.**

**§11.3 carried the first move and none of the rest.** `:22` restates the
accusation problem and says the four-then-five ordering *disposes of* it.
**Grepped: 0 occurrences of *assurance*, *reports nothing*, *absence of warning*,
*no safer* or *tuned until* in 1,735 words.** So a researcher starting here reads
that over-flagging was the design problem and that a second gate settled it.

**The note's other clause is half-present, and the half that is present is in the
wrong register.** §11.3's opening sentence already names output governance — *says
what the resulting tool must never be permitted to output* — but as the third item
in an inventory of what the book has already settled, which a reader takes as
background rather than as a constraint on what follows. **It is named and not
carried forward.**

## The addition

At the end of `:22`, after the worked instance:

> The ordering reaches only one of the two failures: an instrument tuned down until
> it stops flagging produces reassurance nobody has checked, and no second gate
> reaches that. Both directions are governed by who may be told what the tool
> found, which is a constraint the deployment carries and the classifier cannot.

**Two sentences where the note asked for one**, and the reason is that one would
have had to carry the limit, the mechanism and the governance point in a single
breath; the second sentence is the punchline the note identifies — that the design
problem is neither sensitivity nor specificity.

**The wording is deliberately not §2.1.2's.** That site says *A tool tuned until it
reports nothing supplies false assurance* and *what the tool may output and to
whom* — **ten and eight words that would have come across verbatim.** This one says
*tuned down until it stops flagging*, *reassurance nobody has checked*, and *who
may be told what the tool found*. **0 new shared six-word runs**, measured across
every section pair.

**It also does not import the note's word *disclosure*.** The book states this
constraint twice, at §2.1.2 `:53` and §11.3 `:3`, and neither uses that term;
adding a third vocabulary for one constraint is what Q-104 exists to record.

## Why the end of `:22` and not beside the overstatement

Putting it directly after *it disposes of the objection that the instrument accuses
everybody* would interrupt the explanation of how the second gate works, which the
next two sentences give. At the paragraph's end it qualifies the whole ordering
argument including its worked instance, and **the section's habit is to close a
paragraph on its limit** — `:33` on legibility bias, `:38` on the gap between the
narrow case and an early-warning system.

## What was not done

**No cross-reference was added.** 233. The sentence carries the claim itself, and
§2.1.2 is where it is argued; Q-108 is live on exactly this trade and this pass
does not add to it.

**§2.1.2 is untouched.** Its `:53` is the home of the finding and stays so.

**The third failure §11.3 already names was left as it stands** — `:33`'s
legibility bias, that a tool shipped anyway speaks confidently about whichever
institutions keep good records. It is a separate failure from either of §2.1.2's
two and the note did not ask about it.

## Verification

Suite green. `refresh_order_shas.py` run. Scratchpad lualatex build: **196 pages, 0
undefined references and 0 undefined citations**; the passage reads back out of
`pdftotext` in position.

§11.3's censuses are unchanged against HEAD: **12 antithesis sentences, 5 clusters,
8 `deixis --hard` hits.** The addition carries none of `antithesis.py`'s shapes,
which mattered because `:22` already holds one — *an accusation rather than a
finding* — and a second inside sixty words would have been a new pair.

## Figures

133 sections, **1 changed**. 99,459 → **99,511** words (+52); §11.3 1,735 → 1,787.
**196 pages unchanged.** **233 cross-references unchanged.** 324 bibliography
entries unchanged. 0 `\textit`. 0 new shared six-word runs, 1,622 book-wide before
and after.
