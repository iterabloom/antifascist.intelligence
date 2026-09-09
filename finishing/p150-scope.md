# P150 — §12.2.1's third milestone requirement set off from the other two

Author note: the item covered under the falsifier reordering is P144's and is not
redone. The additional item: *against pressures its trainers did not write* is the
whole difficulty of the milestone and sits as one prepositional phrase among
several. Set it off.

## What it was

`12_02_01.tex:11`'s milestone sentence carried three requirements in one breath:

> What meets the milestone is holding all three under sustained pressure from the
> party that trains the system, across a schedule long enough for a slow
> renormalization to show, and against a held-out set of pressures the trainers did
> not write.

**The third arrived last, coordinated with *and*, after a 20-word phrase and an
11-word one.** Nothing in the sentence said it was the hard one.

## The edit

The sentence stops after the second requirement, and the third takes its own:

> The marks also have to hold against a held-out set of pressures the system's
> trainers did not write, and that is the requirement that makes the milestone hard.

**Placed immediately after the milestone sentence rather than at the paragraph's
end.** The alternative — closing the paragraph with it, which is what P148 did in
§11.1 — would have put the falsifier sentence between the milestone and the
requirement that qualifies it. Here the reader gets the milestone and then the part
that makes it hard, with nothing in between.

## Three drafting constraints

**No numeral.** The first draft read *and that is the hard one of the three*. The
paragraph already has *three marks*, so *the three* would have been a second
unlabelled three inside four sentences — the exact ambiguity P144 was run to remove
from §11.1, recreated here.

**No restatement of why it is hard.** P148 gave §11.1 the mechanism — *the party
holding the model is the party that wrote what it was trained on* — and §11.1 is
where the experiment lives. This section states the milestone, so it says the
requirement is the hard one and leaves the argument where it is made. **A second
statement of the mechanism is Q-104's shape.**

***the trainers* became *the system's trainers*.** With the requirement standing as
its own sentence, the bare *the trainers* had no noun in that sentence to attach
to. **Checked against the collision this risks**: §11.1 and §3.3 both carry *pressures
the model's trainers did not write*, and *the system's* keeps it clear of them — **0
new shared six-word runs** across every section pair. The pre-existing overlap on
*held-out set of pressures the* is unchanged and was not introduced here.

## What was not done

**No cross-reference.** 233. Q-108 is live on whether a forward address earns its
cost, and §11.2 already has the one reference this paragraph's section spends, at
`:15`.

**The falsifier gloss was not touched.** *Read the other way, that same result is
the falsifier chapter~\ref{sec:3} states against its own central inference* still
follows, and *that same result* now sits one sentence further from its antecedent.
**It still binds**, because both preceding sentences describe the milestone-meeting
result, and tightening it would have meant rewriting a sentence the note did not
raise.

## Verification

Suite green. `refresh_order_shas.py` run. Scratchpad lualatex build: **196 pages, 0
undefined references and 0 undefined citations**; the passage reads back out of
`pdftotext` in position.

§12.2.1's censuses are unchanged against HEAD: **3 antithesis sentences, 0
clusters, 1 `deixis --hard` hit.**

## Figures

133 sections, **1 changed**. 99,511 → **99,527** words (+16); §12.2.1 511 → 527.
**196 pages unchanged.** **233 cross-references unchanged.** 324 bibliography
entries unchanged. 0 `\textit`. 0 new shared six-word runs, 1,622 book-wide before
and after.
