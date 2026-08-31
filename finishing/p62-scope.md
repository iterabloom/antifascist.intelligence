# P62 — chapter 12's milestones taken from chapter 3

**The author's finding.** Section 12.2 used a five-area survey framing — theory
of mind, moral reasoning, robustness, transparency, applications — that shows no
trace of the floor or the bearer, and reads as material from a 2023 version of
the book. Chapter 3 generates two milestones better than anything in it. The
first: *has the deployment tried the two non-affective constructions first, and
published what it tried?* Section 3.3 makes it a requirement under Replacement,
it is checkable, and it is the only milestone in the book that could stop
something. The second: the falsifier stated as an evaluation — refusal reaching
an unanticipated case, lifting on correct defeat, pricing its own cost, under
sustained pressure from the training party, against a held-out set of pressures
the trainers did not write. **As written, the book's strongest chapter generated
no success criteria.**

## What the measurement found first

| Claim in the old 12.2.1 | Status |
|---|---|
| “The preceding chapters built five separate design cases — theory of mind, moral reasoning, robustness, transparency, applications” | **False since P61.** Theory of mind has no design case in the book; section 11.7 is an open-questions entry and the glossary carries the term. The other four are real |
| The five areas do not rank or sequence against each other | Holds; kept |
| The milestone is the independently checked evidence, not the developer's account | Holds; **moved up into section 12.2's opener**, where it governs all four subsections instead of one |
| Any statement of what the five instruments do not reach | **Absent.** The section named no limit at all |

The author's diagnosis is confirmed by the citation map rather than only by
reading. Chapter 3 is the most-cited chapter in the book and section 12.2 cited
it **nowhere**, in 1,218 words about what would count as evidence the project is
working.

## What the section now does

Section 12.2 goes from two subsections to three.

- **12.2 (opener)** carries the one standard, which was buried in the middle of
  a subsection, and says two of the milestones come from chapter 3. 59 → 101
  words.
- **12.2.1 *What the Floor Would Have to Show*** is new, 793 words, two run-in
  heads.
- **12.2.2 *Where the Existing Instruments Reach*** is the old 12.2.1,
  renumbered and retitled, 642 → 573 words.
- **12.2.3** is the old 12.2.2 renumbered. No prose changed.

**The first milestone is stated as a document, not a measurement.** Which of
section 3.3's two untried constructions was attempted, at what scale, against
which test, and where it failed. That form is what makes it checkable from
outside: it is about a published record and not an internal state, and the
answer *nothing was tried* is a finding anyone can establish. The section says
plainly that nothing else in chapter 12 has a consequence attached to failing
it, and states the limit with it — an order is all it fixes, and nothing in the
book prices a delay against a subject built too early.

**The second is stated in section 3.2's vocabulary and read in both
directions.** The three properties — novel pressure, correct defeat, a priced
cost — are the success criterion for everything the design chapters propose. The
same result with one condition added about how the system was made is the
falsifier chapter 3 states against its own central inference. Both readings run
on one measurement, which is why the pair belongs in a section about milestones
rather than in two places.

**Three limits are carried rather than left for the reader to find.** Section
3.2's warning that the instrument is not clean, a system trained on enough cases
being able to produce all three marks without the mechanism. Section 3.9's
separation of *can this constraint be edited out* from *will this constraint
hold*, which is why a refusal that survives an attack has not met this
milestone. And the method condition, which cannot be checked from outside at
all — Q-047's subject, closed at D-116 by conceding it in section 3.3 and
section 11.1, and now conceded a third time where the milestone is stated,
because a milestone that omitted it would present the falsifier as fully
checkable.

**The five cases keep their evidence and lose their frame.** FANToM,
MACHIAVELLI, the red-teaming measure, CertifAIEd and the EU AI Act, and the four
named deployments are unchanged. What went is the two opening paragraphs
explaining why there are not five milestones, and what arrived is a closing
paragraph saying what the five do not reach: each scores what a system does
against conditions its testers chose, and separating a mechanism that tracks the
rationale from one that does not is what none of them is built for. Robustness
comes nearest and stops in a definite place, durability being a fact about the
constraint's custody rather than about the system.

## The redundancy check, and what it changed

`redundancy.py` **cannot run on this machine** — neither `sentence_transformers`
nor `sklearn` is installed, so both its backends fail. The check was done by hand
instead, on shared 8-grams between the new section and every section it draws
from.

The first draft shared **57 eight-word runs with section 3.3**, including whole
clauses lifted from it: the two errors neither of which is free, the
tamper-resistance sentence, the *question with the engineering filled in*
formulation, and the paragraph on training provenance. That is the failure D-013
exists to prevent — the surviving instance of an argument is the one place it is
made. Rewritten, the overlap is **17**, and what remains is the criterion itself:
*installs nothing answering to affective concern*, *lifts when the rationale is
genuinely defeated*, *a held-out set of pressures the trainers did not write*.
Those have to be quoted exactly or the milestone stops meaning what chapter 3
means. Overlap with section 12.3 is **zero**, which matters most: the book's
closing section already carries the ordering in one sentence and the two do not
now collide.

## Figures

**141 sections**, up 1. **96,258 words**, up 766 on P61's 95,492; 92,984 outside
the glossary. Chapter 12 3,384 → 4,150, and section 12.2 with its children 1,218
→ 1,984. **193 pages**, up 1. All `\ref{sec:}` 532 → **547**, of which 13 are in
the new section — high for 793 words, and every one names the source of a claim
the section is assembling from four chapters rather than sending the reader out
for the meaning. Two were cut on that test before the count was taken.
**`refs.bib` unchanged at 309**: the new section adds no citation, its material
being compressed from sections 3.2, 3.3, 9.3.2, 11.1 and 11.2. 0 undefined
references, 0 undefined citations, `check_all.sh` green. **Renumbering:** 12.2.1
→ 12.2.2 and 12.2.2 → 12.2.3; `renumber-map_2026-08-31c.tsv` translates, and the
glossary's scalable-oversight locator follows it.

**Pages read in the rendered PDF:** printed 144 and 145, the whole of the new
section and the seam on either side of it.

## Errors caught before the build, and one before the commit

- A first draft said section 11.2's third question is **the one entry in that
  chapter with no near-term experiment**. Chapter 11's own opener says three
  entries have none. Corrected to *one of three*.
- Two sentences borrowed section 3.3's phrasing for arguments chapter 3 has
  already made rather than for criteria; both rewritten, and the redundancy
  measurement above is the check.
- The ledger was first edited by round-tripping it through Python's `csv`
  module, which **silently dropped quote characters from unrelated rows** and
  rewrote all 141 lines. Reverted and redone as a line-oriented edit that touches
  five lines; the diff is 5 added and 4 removed.

## Not done

- **The committed proof pair is stale**, and the README's two links and its page
  figure with it.
- **Section 12.3 was not touched.** Its closing paragraph carries the ordering in
  one sentence — *“a deployment that goes straight to the bearer owes an account
  of what it tried first”* — which is now the milestone stated four pages
  earlier. Zero 8-gram overlap, so the two do not read as a repetition, but
  whether the closing section should keep its version is the author's call and
  is Q-059.
- **The ledger rows are `drafted`.** The author has not read any of this in
  position.
- **`section_stats.py` warns that `hline`, `linewidth` and `rule` are untaught,**
  and that warning is older than this pass: the tabular in section 2.2 puts six
  spurious tokens into the word count — the column spec, three `\\[3pt]` row
  breaks — which the figures above therefore carry. Measured, not estimated. The
  fix is not two lines like P59's, because `\begin{tabular}`'s spec argument and
  the `\\[…]` row break are both tokenizer gaps rather than unknown macros.
- **Section 12.2.2's five cases were not re-verified against their sources.**
  FANToM, MACHIAVELLI, CertifAIEd, the EU AI Act and the four named deployments
  stand as P3 and P36 left them; this pass reframed the section and did not audit
  it.
