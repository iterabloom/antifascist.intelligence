# P209 — §12.2.2 compressed to the concession and the two working benchmarks

The author's finding, given whole: *§12.2.2's five areas each name a benchmark
and then concede that none of them reaches the floor. Compress to the concession
plus FANToM and MACHIAVELLI, which are the two that do work.* **Executed.** The
book is **88 sections, 73,216 words and 152 pages**, suite green, 0 undefined
references and 0 undefined citations.

§12.2.2 goes **528 → 250 words**; five run-in areas become two.

## What survived, and how

**Theory of mind and Moral reasoning are carried over byte-identical.** The edit
extracted the two blocks from the original file and asserted their presence in
the rebuilt one, so the FANToM and MACHIAVELLI paragraphs are the same bytes
rather than the same text retyped. Both citations — `kim2023fantom`,
`pan2023machiavelli` — travel with them.

**The concession survives with two sentences removed** and two referents
repaired, below.

**The opening sentence is new and is this pass's.** The old one read *The areas
below do not rank or sequence against each other: a system meeting the bar in one
and lagging in another is not partway through a queue, because nothing
establishes an order for them to arrive in.* With three of five areas gone it had
nothing left to rank, so it was replaced rather than kept: *Two instruments do
work that bears on the floor, and both do it by applying pressure.*

## The cut areas were weaker than the finding said

The finding was that each area names a benchmark and concedes it does not reach
the floor. **Checking found a second defect in all three of the areas cut**: each
re-applies the standard §12.2 has already set, two sentences earlier, for every
milestone in the chapter — *the milestone is the independently checked evidence,
not the developer's account of having reached it.*

| Area | What it asked for |
|---|---|
| Robustness | *documented adversarial testing rather than the tests its own designers thought to run* |
| Transparency | verification by *an audit or review board… not when a developer's own documentation asserts it* |
| Applications | evaluation *by a body other than the one that deployed it* |

Three restatements of one rule, inside a subsection whose sibling, §12.2.3, is
**entirely** about who is qualified to check and what independence buys. Nothing
in the three was lost that the chapter does not already carry twice.

## Two sentences out of the concession

Cut from the closing paragraph:

> Robustness comes nearest and stops in a definite place. A commitment that
> survives an attack has been shown to be durable, and durability is a fact about
> the constraint's custody rather than about the system holding it.

**`12_02_01.tex:13` makes that claim one subsection earlier**: *a refusal that
survives an attack has passed a tamper-resistance test, which answers section~3.8's
other question and leaves this one open.* Same claim, adjacent subsections,
D-013's one-home rule — and §12.2.1 is the better site, since it is arguing about
what the milestone test can settle. It stays there.

## Two referents repaired

**“None of the five” → “Neither… and nothing else available does either.”** The
number was wrong after the cut, and the plain fix — *neither* — would have
narrowed a concession that was never only about the five. The replacement keeps
the original scope.

**“What the standard does not answer” → “What they leave unanswered.”** *The
standard* pointed back at the Transparency area's audit requirement, which is
gone.

**The closing sentence is now a bridge rather than a loose end.** It asks *who is
qualified to do the checking, and what happens when nobody with the competence to
check is also free of a stake in the result* — and §12.2.3, the next subsection,
is the answer to exactly that. The compression improved the join.

## Nothing was orphaned

**No `\ref` anywhere points at `sec:12.2.2`.** Neither §12.2 nor §12.2.3 promises
five areas or refers to the cut ones; §12.2's opener is general.

**The section's only two citations are the two the author kept**, so `refs.bib` is
untouched at 222 entries, all cited, verified after the edit.

## One sourcing gap leaves with the cut

The Applications area read:

> Perspective API, vTaiwan, the Carnegie Endowment's AI Global Surveillance
> Index, UNESCO's 2021 Recommendation on the Ethics of Artificial Intelligence:
> deployments and instruments rather than hypotheticals, and every one of them
> dual use.

**Four named instruments, no citation on any of them**, against D-009's rule that
named studies, statutes and systems take a source. Three of the four — Perspective
API, the Surveillance Index, the UNESCO Recommendation — appeared **nowhere else
in the book** and are now out of it. vTaiwan survives at §8.2 and §12.1.

**Recorded rather than treated as fixed.** The gap is gone from this section
because the sentence is gone, not because anybody sourced it, and **nothing in
`check_all.sh` tests for a named instrument carrying no source.** A later pass
should not read this as evidence the rest of the book is clean on the point.

## Files touched

| File | Change |
|---|---|
| `manuscript/sections/ch12/12_02_02.tex` | three areas and the ranking opener cut; two sentences out of the concession; two referents repaired; new opening sentence |
| `manuscript/sections/ORDER.tsv` | one sha256 refreshed |
| `finishing/DECISIONS.md`, `finishing/STATE.md`, `finishing/PLAN.md` | D-311, new lead, header figures |

No section added or removed, so `sections.tex`, the contents, `outline.tsv` and
`ledger.tsv` are unchanged at 88 rows.

## Measured after

88 sections, 73,216 words, 152 pages, 258 cross-references against 88 labels, 222
bibliography entries all cited, 0 undefined references and 0 undefined citations.
Suite green. Chapter~12 is 9 sections and 3,109 words; §12.2.2 is 250 of them.

**Five passes today have taken the book 157 → 152 pages** — D-307 through D-311,
every one an author finding about recap or inventory — **and none has been
proofed.** The committed pair is stale by five pages and `README.md` still says
157.
