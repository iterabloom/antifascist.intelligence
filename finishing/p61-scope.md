# P61 — chapter 1 cut back to its opening, chapter 2 trimmed to what chapter 3 argues from

**The author's finding.** Chapter 1's unnumbered opening does the work — the three
advance notes, the safety-versus-ethics paragraph, *"holding a line against your
owner turns out to require a bearer that cares what becomes of somebody, and such
a party must be treated as able to be wronged."* Sections 1.1, 1.2 and 1.3 then
revert to generic AI-ethics framing and are about half the chapter, diluting it.

**The instruction.** Cut or radically compress 1.1–1.3, let the opening run
straight into chapter 2, and trim chapter 2 to what chapter 3 argues from. The
empathy and theory-of-mind material in 2.2 serves chapters 4, 5 and 11.7 rather
than chapter 3; 2.4.3 belongs next to 9.3.

**Two calls were put to the author before anything moved**, because both
renumber chapter 2 and doing it twice would have been waste. The 2.2 material
**compresses into its consumers**; 2.3.1 and 2.3.2 **stay**.

## What the measurement found first

| Section | Words | Who points at it |
|---|---|---|
| 1.1, 1.2, 1.3 | 668 | two glossary locators, nothing else |
| 2.2 (parent) | 97 | nothing |
| 2.2.1 | 652 | 2.3.3, 4.1.2, 5.1.1, 5.1.2, 5.2.1, 11.7, glossary — **chapter 3 never** |
| 2.2.2 | 562 | the glossary, and nothing else |
| 2.4.3 | 1,082 | 6.1.3, 9.3, 9.3.2, 9.3.3, 11.2, glossary — **chapter 3 never** |

**What chapter 3 argues from in chapter 2** is 2.1, 2.1.1, 2.3.3, 2.4, 2.4.1 and
2.4.2 — 4,473 words of 10,561.

**One section was kept against the instruction read literally, and the reason is
recorded rather than assumed.** Section 2.1.2, Antifascist Ethics, is 1,834 words
that chapter 3 never cites, and ten sections across chapters 5, 6, 7, 8, 9 and 11
do. It is the book's structural definition of fascism. Trimming chapter 2 to
chapter 3's premises does not license removing the definitional backbone of seven
other chapters, so it stays.

**And the citation map was not trusted on its own.** Section 3.8 says *"The point
made earlier about the self-model explains why the bearer cannot be the one to
raise the alarm"* — leaning on 2.3.2 with no `\ref`, invisible to every tool in
the suite, and chapter 1's roadmap makes the same promise. A cut driven by
reference counts alone would have taken it.

## Chapter 1

**1.1, 1.2 and 1.3 cut entirely**, 668 words. Their content already had homes:
Robinson's racial capitalism is developed at 6.1, Dweck at 5.1.1, intrinsic
motivation at 5.6.1, interdisciplinary collaboration at 8.1, and the five aims
restate the roadmap the opener already gives.

**One sentence was folded into the opener** — the only thing in the three with no
home elsewhere, and it is a reader service rather than an argument: the early
chapters argue and the governance chapters inventory, *because there the argument
is unavailable without the inventory.* **The opener is otherwise untouched**, the
finding being that it is already right.

The roadmap's description of chapter 2 was rewritten, chapter 2 no longer
covering compassion and empathy. Chapter 1 is now a chapter with no subsections,
which is a first for a numbered chapter and renders correctly.

## Chapter 2

**2.2, 2.2.1 and 2.2.2 cut, 1,311 words, compressed to 494 and placed at the
point of use.**

- **5.2.1 takes the compassion material** — the three-way split, the
  Singer–Klimecki training study, the design consequence — **and with it the
  empathic-concern/personal-distress dissociation and Bloom's spotlight
  argument.** That second half is **D-016's T7 transplant, which the author ruled
  in at full strength**, so cutting 2.2.2 outright would have reversed a standing
  decision. It is carried rather than dropped, and this is the place to say so if
  the author wants it gone.
- **The Lady Gaga epigraph travelled with it.** It sat over exactly that material
  in 2.2.2, and D-012 keeps the epigraphs; deleting one silently was not
  available. It now opens 5.2.1.
- **The fold repairs 5.2.1 rather than only relocating into it.** The section is
  titled *Moral Emotions: Empathy, Guilt, and Shame* and said almost nothing
  about empathy; it now leads with it. 666 → 1,058 words.
- **4.1.2 takes the mirror-neuron account** — the macaque finding, the
  interpretation that outran it, the human single-neuron evidence — where the
  borrowing from neuroscience is already the subject. It had been citing 2.2.1
  for it across two chapters.

**2.4.3 moved whole into chapter 9 as 9.3.2**, before *Legal Frameworks* and
*Making Review Binding*, both of which cited it.

**Renumbering:** 2.3.x → 2.2.x, 2.4.x → 2.3.x, and old 9.3.2–9.3.4 → 9.3.3–9.3.5.
`renumber-map_2026-08-31b.tsv` translates.

**The chapter is retitled *Ethics, Affect, and Machine Subjects*.** *Foundations
of Compassion and Empathy in Friendly AI* named material that has left it, and
`transplants.md` had already recorded that the title *"survives T7 only if
compassion is doing the load-bearing work."* Compassion is now in chapter 5. The
opener goes from four load-bearing results to three and picks up section 2.1's
job, which `transplants.md` recorded as missing from it since T7.

## A defect the move exposed

Section 2.4.3 opened *"Three of the six principles governing this research…"* and
**no section of the book contains six principles.** The likeliest cause is P38,
which merged five research-ethics subsections into one; the reference was
stranded then and read as fine because it sat near where the list used to be. In
chapter 9 it would have been baffling. It now names the three principles it uses.
**No tool reaches this class** — it carries no `\ref` and no number — and it is
the second instance in two passes of a bare backward reference surviving because
of where it sat.

## Figures

**140 sections**, down 6. **95,492 words**, down 1,454 on P60's 96,946.
**192 pages**, down 4 from 196. Chapter 1: 1,839 → 1,217 words and 4 → 1
sections. Chapter 2: 10,561 → 8,147, down 22.9 percent, and 15 → 11 sections.
Chapter 4 +102, chapter 5 +392, chapter 9 +1,092 — the three folds and the move.
All `\ref{sec:}` 541 → 532. **`refs.bib` unchanged at 309 with none newly
uncited**, every citation in the cut sections having survived in a fold. 0
undefined references, 0 undefined citations, `check_all.sh` green. Ledger
unchanged at 3 `accepted`: none of the three was touched.

**Pages read in the rendered PDF:** the chapter 1 to chapter 2 seam, the rendered
table of contents, and 5.2.1 with the epigraph and the folded material.

## Not done

- **The committed proof pair is stale**, and the README's links with it. **[Reconciled at P76: the pair has been rebuilt since, most recently at P75, and stands at 187 pages. P63's own reconciliation commit did not reach the scope files, so this line and the four like it in `p59`–`p62` went uncorrected until now.]**
- **Theory of mind now has no section of its own.** 2.2.2 defined it; the
  glossary entry and section 11.7 carry it, and 11.7 is where the open questions
  already live. The elderly-companion case and its line — *"An AI companion is not
  a policy"* — went with the cut and are recoverable from git if wanted.
- **Chapter 5 is now 10,023 words and 23 sections**, the widest in the book, and
  this pass added to it. Q-034 and Q-035 are the standing entries on chapter 5's
  width; neither was reopened here.
- **The three-way audit of what else chapter 2 no longer supplies was done by
  reference and by reading the six sentences that name chapter 2 as a whole**,
  not by re-reading the chapters that depend on it.
