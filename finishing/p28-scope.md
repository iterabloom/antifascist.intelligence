# P28 — the cross-reference density pass (D-089)

The author's judgment, 2026-08-28: the manuscript carries roughly 690 explicit
chapter or section references, about one every 140 words, the accumulation makes
the prose feel like a navigated repository, and cutting half would improve
continuity.

The diagnosis is right and the count was low. **This pass cut 79 references, 10
percent, not the 50 percent the instruction named.** Why it stopped there is the
substance of this file, and the shortfall is recorded rather than papered over.

## What is actually there

Counted from the rendered prose, the way a reader meets a reference:

| | words | references | density |
| --- | --- | --- | --- |
| Prose, chapters 0–10 | 94,590 | **791** | 1 per 120 words |
| — collapsing "chapters 4 and 5" to one gesture | | 742 | 1 per 127 |
| Glossary (chapter 11) | 2,928 | 125 | locator apparatus, counted apart |

So the density was worse than the estimate, not better: one per 120 words against
the one per 140 the instruction assumed. The gesture rate, 1 per 127, is the
figure the estimate was closest to, and 690 is near the gesture count once the
glossary is excluded — the two numbers were measuring different things.

**A correction inside this pass.** The first opener/leaf split reported to the
author was wrong. It classified any two-level file as an opener, which made
chapter 3's and chapter 7's leaf sections into openers, and produced "openers are
23 percent of the prose and carry 43 percent of the references." An opener is a
section with children. Corrected:

| | words | references | density |
| --- | --- | --- | --- |
| Openers (40 files) | 11,356 | 221 | **1 per 51 words** |
| Leaves (122 files) | 83,234 | 570 | 1 per 146 words |

The concentration is real and it is three times the leaf rate, but it lives in
221 references, not 339. The leaves at 1 per 146 are not, on their own, a fault.

## The rule this pass applied

Two standing decisions run against a uniform cut, and the second is eight days
old:

- **D-013** built the cross-reference regime deliberately. Before it, one
  argument appeared nine times without anyone noticing; the surviving instance is
  the one place it is made, and every other location gets a pointer instead. The
  references are the mechanism that paid for the deduplication.
- **D-078 (P26)** raised chapters 4 and 5's references into chapter 3 from 5 of
  100 outbound to 33 of 162, because a model given only the PDF read those
  chapters as a survey. There are 32 such references now. A uniform halving
  reverses a third of that pass.

So the cut went by class, not by rate:

**Cut** — a reference whose sentence's only work is to say where something is:

1. *Child roadmaps at section and subsection openers.* A linear reader meets a
   map at the chapter opener, a second at the section opener, and a third at the
   subsection — three prose tables of contents before the argument starts. The
   chapter-level map is a convention readers want and it stays. The ones below it
   go.
2. *Parenthetical filing labels* — "Reinforcement learning (section 4.2.1) makes
   the reward the whole of what a system wants." The sentence names the method;
   the number files it.
3. *Signpost sentences* whose entire content is a location.
4. *Appended locators* — "…is the standard technical response and is covered at
   section 4.2.2."
5. *Restated content plus a pointer* — the sentence gives the material and also
   says where else it lives.

**Kept** — a reference the sentence cannot lose:

- Anything that **imports a result**: the sentence borrows a finding and has to
  say whose it is.
- Anything that **marks a boundary or a limitation** — where the book says a
  claim is contested elsewhere, or that a topic belongs to another chapter. These
  are the book's own error-correction links and cutting them makes it read as
  more confident than it is.
- Every chapter-4-and-5-into-chapter-3 reference (D-078).
- Sections whose **connective work is their subject**. Section 3.7, "What Follows
  for the Rest of the Book," carries 13 references in 618 words and every one is
  the content: the section exists to say what changes where. Chapter 3's opener
  carries 20 in 1,002 words and they are the argument — the chapter opens by
  showing that the same requirement arrives independently at sections 5.6.3,
  8.7.7, 8.7.10 and 10.1.2, and without the numbers there is no argument. Chapter
  9's gap list announces in its own lead-in that each item comes "with the section
  that runs into it," so its eight parentheses are promised.
- The glossary's 125 locators. It is a reference apparatus; a reader consults it
  rather than reading through it.

## What changed

36 sections. **791 → 712 references, 1 per 120 words → 1 per 132.** Openers went
from 1 per 51 to 1 per 69.

| where | cut | what |
| --- | --- | --- |
| ch 1 | 3 | a parenthetical, a third naming of chapter 3 in one paragraph, one signpost in 1.3 |
| ch 2 | 9 | 2.3's "what the rest of this section does" pointers, three signposts, two parentheticals, 2.4.7's closing signpost |
| ch 4 | 5 | 4.2's four parenthetical method labels, one signpost |
| ch 5 | 19 | chapter opener's restated table of contents (7), 5.2's four child parentheses, 5.3 and 5.5's child roadmaps, 5.6's two |
| ch 6 | 8 | 6.4's three child parentheses, three appended locators, two signposts |
| ch 8 | 17 | 8.3's four child parentheses, 8.7's and 8.2's child roadmaps, 8.5's two, four leaf signposts |
| ch 9 | 10 | 9.1's opener — 15 references in 237 words, the worst instance in the book — plus 9.2's child roadmap and one restatement |
| ch 10 | 4 | 10.3's child roadmap, one forward signpost |
| ch 3, ch 7 | 0 | see "Kept" above |

Four opener paragraphs needed their sentence subjects repaired after the numbers
came out, because a sentence beginning "Section 9.1.3 covers…" has no subject
once the reference goes. They now run on ordinals — "The third covers value
learning and alignment as active technical research." That is sentence-level
revision, which is within D-007's "Revise" fate; **no argument was altered and no
claim was added or removed**, and D-007 was not lifted for this pass.

## The shortfall, and why

The instruction was half. This pass delivered a fifth of that.

The projection given to the author before execution — about 250 references, 32
percent — came from hand-judging a random sample of 40 reference-bearing
sentences and finding 15 of roughly 46 removable. **That method overestimated
removability by about threefold**, and the reason is worth recording: a sentence
read on its own looks self-sufficient, because the work its reference is doing is
usually to the paragraph around it rather than to the sentence carrying it. Three
of the sample's clearest "removable" calls did not survive being read in place.
Section 6.1.1's COMPAS reference, marked removable as a restatement, is an
ordinary inline reference to a source of bias. Two others were section openers
establishing a cross-chapter link that nothing else in the section supplies.

Reaching 50 percent means going into the 467 leaf-inline references, where the
reference is a term in the sentence rather than an ornament on it. Those are
concentrated in chapter 3, chapter 7, section 9.1.7 and section 10.2.1 — the
spine P27 rewrote on 2026-08-28 and the two synthesis chapters. It is a real
option and it is a different pass: it would need D-007 lifted, and it would be
reversing D-013 and part of D-078 rather than tidying around them. **It is left
with the author, not taken.**

## What was not checked

- **Whether any reference the reader wants is missing.** Nothing in this
  repository checks that, and this pass only removed.
- **Whether the surviving references point at the right sections.** That is
  `xref_content.py` and it was not re-run; `check_xrefs.py` confirms all 837
  `\ref` still resolve, which is a different and weaker claim.
- **Chapters 3 and 7 were read for removable shapes and not read in full.** The
  claim that their density is earned rests on section 3.7, chapter 3's opener and
  the section list above, not on a reading of all 137 of their references.
- **The proof was built, not page-proofed.** 199 pages, 0 undefined references,
  both formats clean; nobody has looked at the pages where four opener paragraphs
  changed shape.

## The tool

`finishing/tools/xref_shapes.py`, written for this pass, sorts every reference by
the shape of its sentence and writes `finishing/reports/xref_shapes.tsv`. It is
not in `check_all.sh`: its output is a candidate list needing judgment, the P14
precedent. Its own accuracy was the limiting factor rather than the reader's — it
found 117 candidates where hand-reading found 79 real ones and missed others it
had classified as `inline`. A verb list cannot tell a sentence that borrows a
result from one that names a topic, and that distinction is the whole of the
question.
