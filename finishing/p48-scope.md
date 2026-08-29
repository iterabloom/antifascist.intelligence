# P48 — the misdirected references the pairing tool exposed

**Author's instruction, 2026-08-29:** read `reports/xref_pairs.txt` and identify
any obvious instances of the citer citing the wrong thing, from that file alone;
follow up holistically only on the cases that look obvious while reading it. Then
*"go, and then proofs."*

**Decision row:** D-112. **Branch:** `pass/48-misdirected-references`.

## What the reading was

All 829 pairs, in order, in one sitting. The file gives the citing sentence and
the opening sentence of the section it points at, so what it can expose is a
pointer aimed at the wrong section or a citing sentence that misdescribes its
target's subject. It cannot expose a citing sentence that names a claim made in
the *middle* of a target section that the section does not make — Q-041's
original class. That distinction is worth keeping: this pass closes a class the
tool can see, and not the class the tool was built to help with.

Most apparent mismatches are artifacts of the method and were discarded as such.
A chapter-level reference lands on the chapter's epigraph — chapter 6's is the
Lavender quotation, so every reference to chapter 6 appears to point at a line
about targets per day. A chapter-11 section opens by recapping a *different*
section, so section 11.6's opener names section 5.5.1. Neither is a defect.

## The six defects, and how each was confirmed

Each was checked against the target section itself, not against the pairing.

**1. The Partnership on AI cited to a chapter that never mentions it.**
`ch06/06_04_03.tex` sent a reader to section 5.6.2 for the Partnership on AI as a
standard-setting venue. Section 5.6.2 is *Balancing AI Autonomy and Alignment with
Humane Values*. The string "Partnership on AI" appears in chapters 6, 7, 9, 10 and
13 and **nowhere in chapter 5**. The book's own standing treatment is section
9.1.2, which section 7.4 names as such. Repointed to 9.1.2.

**2. A glossary entry for a term the book does not contain.** The *AlphaGo Zero*
entry called it "the book's standard example of generalization that comes from
scale and self-play rather than labeled human data," and pointed at section 2.4.1,
which is the nociception-to-suffering ladder. `AlphaGo`, `AlphaGo Zero`,
`AlphaZero` and `self-play` occur **nowhere in the manuscript outside that entry**.
The claim about the book was false and the pointer was wrong, and the book's actual
recurring example of generalization from scale is GPT-3, which has its own entry.
**Entry cut**; 57 glossary terms to 56, 2,979 words to 2,934.

**3. Differential privacy cited to the ethical frameworks.** The glossary gave
`(§2.1.1, §6.4.2, §9.2.1)`. Section 2.1.1 is *Six Ethical Frameworks, and Where
Each One Runs Out*; its only occurrence of "privacy" is inside deontology's list of
obligations. Differential privacy is at 6.4.2 and 9.2.1 and nowhere else. The
2.1.1 pointer is dropped.

**4. The Moral Machine's second pointer is dead.** The glossary gave
`(§4.2.1, §5.3.3)`. Section 4.2.1 has it. Section 5.3.3 is *AI Systems Learning
from Moral Disagreements and Conflicts* — Project Debater and negotiation
simulation — with no Moral Machine, no autonomous-vehicle dilemma, and no
cross-cultural judgment data. The 5.3.3 pointer is dropped.

**5. Chapter 3 twice named the wrong one of section 2.1.2's four features.**
Section 2.1.2 enumerates them, and the first is *recuperation of dissent*. Sections
3.1 and 3.2 both said the first structural feature is a constraint that survives
while the reason for it dies. That description comes from section 2.1.2's
**Two scales** paragraph on the molecular case — "the constraint remains, its
reason dies, and asking why becomes the deviant act" — and is nearest the *third*
feature, coding of exception as betrayal. Section 6.1.1, chapter 7, section 7.2 and
the glossary all use "first feature" to mean recuperation, so the book contradicted
itself about its own definition, in the two sections that set up the floor. Both
sentences now name the scale rather than a feature number, which is what the
argument actually needs and what section 2.1.2 actually says.

**6. And a number that was off by one in the other direction.** Section 9.3.4 used
"first structural feature" for an institution that "has adopted a selection rule
that admits whatever it already measures." That is the *second* feature,
aestheticization of the metric — the measure substituting for the thing measured,
so that what falls outside the number is unnamed. Corrected to second, with the
trailing clause rewritten to describe the metric rather than a rule outliving its
reason. Section 9.3.4's *other* use of "first feature," for a body that can keep
every defense and metabolize all of them, was already right and is untouched.

**A seventh was reported to the author and turned out weaker than reported.**
`ch06/06_04_02.tex` cited section 5.6.2 for "independent third-party audits, the
kind section 5.6.2 argues for as routine practice rather than crisis response." I
told the author this was close to the opposite of section 5.6.2's argument, on the
strength of that section's one use of the word audit — "an audit reading the record
of what already happened." That was too strong. Section 5.6.2 does list
"red-teaming the design under adversarial pressure while it can still absorb the
answer" and "keeping people other than a system's own developers in the process"
among the safeguards it asks for from the start. The citing sentence was loose, not
wrong. It is sharpened anyway, to quote what section 5.6.2 actually asks for.

## What was checked and found sound

Named because a later session should not re-open them.

- **Section 11.1**, which takes seven inbound references about tamper-resistance
  while opening on "AI self-awareness." Its title is *Interpretability,
  Self-Reports, and Resistance to Tampering*. Every one of the seven is correct.
- **Section 9.3.4 as the slope instrument**, eleven inbound references.
- **Section 5.5.1 for open-source tooling** (8.1.1) — "Open tooling lets
  researchers outside a lab inspect and replicate what the lab claims."
- **Section 11 for the consumer-finance bureau instance** (8.3.3) — it is in the
  chapter opener, which carries `sec:11`.
- **Section 2.1.1 for value-conflict machinery and metric compilation** (5.3.3,
  11.4) — both are in it, under two run-in heads.
- **Section 6.4.1 for the twenty-seconds-per-name case**, five inbound citers.
- **Section 5.6.2 for red-teaming and safeguards from the start** (13, 9.1.5).
- **Section 6.1.1's own "first feature" claim** — an annotation pipeline built so
  the annotator cannot dissent. That is recuperation, correctly numbered.

## Measurements

| | before | after |
|---|---|---|
| cross-reference pairs | 829 | 826 |
| glossary terms | 57 | 56 |
| manuscript words | 94,432 | 94,415 |
| glossary words | 2,979 | 2,934 |
| pages | 191 | 191 |
| undefined references in the build | 0 | 0 |

Three pairs fewer because three references were removed and none added.

## What this pass does not do

Group 4 is untouched and remains the reading: Q-035's vocabulary measurement over
chapter 5, Q-038's "rather than" sweep of chapters 2 to 4, Q-043's sweep by
subject, and Q-045's whole read of chapter 3 and section 11.2. Q-041's own class —
a reference that resolves but names a claim its target does not make — is narrowed
by this pass and not closed by it, because the pairing file shows only the target's
opening sentence.
