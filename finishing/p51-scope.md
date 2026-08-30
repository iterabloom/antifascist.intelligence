# P51 — the rulings executed, and the four defects repaired

**Author's instruction, 2026-08-29:** a question-by-question walkthrough of Q-046 to
Q-052 with a ruling on each (D-115), then *"go."*

**Decision row:** D-116. **Branch:** `pass/51-rulings-and-defects`. **12 sections
changed.**

Two units, taken in that order. The five ruled edits and the four defects from
`p50-scope.md` are the first, because they are repairs to what the book already says.
Q-048 is the second, because it produces a finding rather than a repair.

## Unit one: the five ruled edits and the four defects

### Q-046 — the definition of a floor *holding* moves into chapter 3

Ruled (b). Section 5.1.1's criterion — a floor holds when the bearer can be shown to
have violated it in terms it accepts, so the violation registers as one and changes
what happens next — is now in section 3.8, in the paragraph where the threat model
doubles and *will this constraint hold* is added. Section 5.1.1 keeps the growth-mindset
argument and the engineering paragraph, with a bridge paragraph pointing at 3.8.

**Word accounting:** 3.8 +166, 5.1.1 −123. The move is roughly neutral book-wide and
is not neutral for chapter 3, which is the cost the ruling took knowingly — it is
recorded under the numbers below rather than left for a later pass to discover.

### Q-047 — the falsifier's middle condition, conceded

Ruled (a). Section 3.3 now says that whether a method installed nothing answering to
affective concern is a fact about how the system was made, that the same section has
already said there is no proof of a training history to publish beside the hash, and
that the condition therefore rests on the builder's account of their own method — the
evidence section 2.4.1 declines when a system offers it about itself. It points at
section 11.2's third question. Section 11.1's near-term work carries the same limit and
the same pointer, which it had not had.

### Q-049 and defect 4 — chapter 6's explanation claims

Ruled (a). Section 6.3.4's LIME and SHAP paragraphs are cut to a pointer at section
6.1.3, which carries the limit that neither tool can see a wrong training target.
Separately, 6.3.4's opening said explanation lets a reader inspect the reasoning that
produced a decision; it now carries section 6.3.3's limit, that an account of a decision
can be produced after it, so what the techniques deliver is a decision that can be
contested. **D-106 made that repair at 6.3.3 and stopped three heads short**, and this
is the propagation.

### Q-050 — the vendor named

Ruled (b). Section 10.7 names Anthropic for the commitment it paid for, and says it is
naming for section 6.1.1's reason applied in the direction that flatters the company.

### Q-052 — chapter 1's advance note

Ruled (b). The note now carries section 2.4.1's own caveat: the lower rungs of harm need
no persistence, so what the persistence result reaches is the top of the ladder and not
harm as such.

### Defect 1 — section 2.4.1's pointer

Repointed. It had credited section 3.5 with "standing held by parties outside it," which
is what 3.5 declines: that section dissolves the question and has the bearer guard its own
continuation from the structural interest, by a route that does not run through a quorum
somebody else selected. It now points at sections 2.4.2 and 11.2, which hold the claim,
and names 11.2's finding that guardian and operator are usually the same organization.

### Defect 2 — the section 2.4 epigraph

The raw `web.archive.org` URL and the line *also see Science Fiction, Disruption and
Tourism Ch 15* are removed from the attribution block. No prose change; the epigraph is
excluded from the word count as third-party text.

### Defect 3 — section 3.5's allusion

Glossed with a pointer to section 10.10, where the strike is documented and where the
reference names it. The sentence is unchanged otherwise, because it is exact once the
event is known.

## Unit two: Q-048, the five discriminators run

Ruled (b): run them and report whichever way it comes out.

**They clear all three instances**, which is the result the ruling was taken for. Section
7.4 carries the working under a new run-in head.

**Three of the five are absent outright** across the annotation pipeline and the rating
scheme. Nothing in either is personal, which disposes of the leader-cult test — section
7.2 is explicit that a comparison enters the fit without the standpoint that produced it,
which is the opposite of an exception granted by proximity. Neither shows participation
beyond what the rule requires, and section 6.1.1's record runs the other way. And neither
has a scapegoat in the sense the test means: the annotator bears a cost with no claim on
the outcome, which is the closest candidate, and the category exists to get labels
produced rather than to fall on anyone — adverse treatment minimized as a cost rather than
served as a purpose, which is the whole of what the five are for.

**Two of the five could not be settled**, and that is the finding underneath the finding.
Whether procedure is waived upward, and whether a practice disowned in policy is rewarded
in promotion, are facts about what an institution rewarded rather than what it wrote.
Section 2.1.2 says so when it introduces them. The artifact that would settle both is the
one section 7.3 asks for and nobody publishes.

**The discourse answers the same way, one step less clean.** Its scapegoat test is
contested rather than absent, on 7.4's own evidence. Its procedural test fails because
there is no procedure above the deciding party to waive — an absence rather than an
asymmetry. Deniability comes nearest of anything in the chapter and fits the firms rather
than the field.

**What the chapter now says**, in place of declining to deliver a verdict: it has been
describing a recuperation mechanism inside ordinary institutional decay, not fascism at
the molecular scale. Section 11.3 gains a pointer, because this is the measurement it
says has never been made — a detector on the four features flags all three instances and
the five-test filter passes all three. One measurement of an instrument's false-positive
behavior is not a validation, and it is more than the assertion the book had.

## Measurements

| | before | after |
|---|---|---|
| words | 94,488 | 95,405 |
| pages | 191 | 192 |
| sections | 153 | 153 |
| undefined references in the build | 0 | 0 |
| ledger `accepted` | 13 | 12 |

**Per section:** 3.8 +166, 3.3 +94, 3.5 +7, 5.1.1 −123, 1 +26, 2.4.1 +34, 6.3.4 −49,
7.4 +642, 10.7 +45, 11.1 +38, 11.3 +37. Section 2.4 changed without changing its word
count, because what came out was an epigraph's apparatus.

**Chapter 3 is 13,703 words and 14.36 percent of the book**, from 13,343 and 14.21. That
is Q-045's watch, and the addition was authorized rather than accumulated: Q-046 was ruled
with the cost stated. **Chapter 7 is 4,707 words and 4.93 percent**, from 4,054 — the
largest proportional gain in the pass, and the only chapter that gained a finding rather
than a repair.

Section 6.3.4 moves from `accepted` to `drafted`, the only status change; the other eleven
rows were already `drafted`.

## What this pass does not do

It does not rebuild the committed proof pair, which still reads 191 pages against a tree
that now builds 192. **The README's figure and the pair are stale until the proofs are
made.** It touches none of the four remaining group-4 items — Q-035 still needs a ruling on
chapter 5's citation age, and Q-043 and Q-045 stay open. And it checked no citation against
a source: the vendor named at section 10.7 is named from the title of the reference the
sentence already carried, and no new factual claim was added anywhere in the pass.
