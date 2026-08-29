# P47 — the author's rulings on the open questions, groups 1 to 3

**Author's instruction, 2026-08-29:** a question-by-question walkthrough of all
eighteen open entries, with a ruling on each, then *"Groups 1–3 now, group 4
after."*

**Decision row:** D-111. **Branch:** `pass/47-question-rulings`.

## The rulings

| | ruling | done here |
|---|---|---|
| Q-026 cross-references | defer indefinitely | — |
| Q-027 chapters 4–5 | leave open | — |
| Q-030 dead bibliography entries | move to a new file | yes |
| Q-031 chapter 11's gap list | restore the notes | yes |
| Q-032 bibliography notes | keep only descriptive; cap at 2× a bare entry | yes |
| Q-033 bias taxonomy | add the run-in | yes |
| Q-034 §4.2's width | leave | — |
| Q-035 chapter 5 | run the measurement | group 4 |
| Q-036 chapter 3's length | leave, and close | — |
| Q-037 the plural arrangement | leave, carried as research | — |
| Q-038 "rather than" | sweep chapters 2, 3 and 4 | group 4 |
| Q-039 recurring conclusions | stop at 2,051 | — |
| Q-040 inventories | adopt the positional rule, drop the metric | — |
| Q-041 false references | build the pairing tool | yes |
| Q-042 the removal cases | leave, re-read at each proof | — |
| Q-043 cross-chapter contradictions | sweep by subject | group 4 |
| Q-044 the assembly | rewrite §3.1 functionally | yes |
| Q-045 concentration | read chapter 3 and §11.2 whole | group 4 |

## Group 1 — the manuscript

**§11 (Q-031).** Each of the eight ranked gaps regains a *Nearest work* clause
naming the closest existing research and where it stops: tamper-resistant
training and concept injection, which establish that a behavior persists rather
than that a reason did; institutional review and the pet-trust form, untried on a
subject whose function is to refuse the institution reviewing it; the
backsliding-indicator literature, which measures institutions rather than the
mechanisms inside them; the specification-gaming catalog and the
goal-misgeneralization results, which describe the failure afterward; RLHF and
its sycophancy failure, which leaves untouched whose preferences are collected;
the pricing-algorithm cartel, which documents emergence and resists nothing; the
temporoparietal dispute and behaviorally trained false-belief models; and the
in-group-advantage meta-analysis, whose answer is the least usable of three. 840
→ 1,180 words.

**§6.1.1 (Q-033).** Target choice added to the opening list and given a
`Target and Label Choice` run-in ahead of `Algorithm Design`, pointing at the
Obermeyer case rather than restating it, and saying why the class is invisible to
every method that takes the target as given.

**§3.1 (Q-044).** The parts list P44 wrote — *weights, the prompt standing in
front of them, the memory they read, the tools they can reach, and the layer that
decides what reaches a person* — is cut. **The author's objection was that it
reifies today's practice: too vague to bind, or precise and therefore wrong when
the paradigm moves.** What replaces it is functional. What a floor has to be kept
from is not a component but a position: anything that can come between a refusal
and the person the refusal protects. The book declines to say what occupies that
position, on the ground that the answer is a fact about how systems happen to be
assembled at the time of writing; the enumeration is pushed to the deployment, in
advance and in public, which is the demand §3.5 already makes of the floor's
contents.

**§3.7.** Not a ruling — a defect the new tool found on its first run. §3.7's
opening sentence quoted §3.5's dial as *"when the operator loses the off
switch,"* which is what §3.5 said until P45 changed it to *"when the operator's
use of the off switch stops being free."* Q-041's class exactly, caught by the
instrument built for it in the same pass.

## Group 2 — the bibliography

**Q-030.** The 23 uncited entries moved to `finishing/unused_bibliography.bib`,
which is deliberately not `\addbibresource`d. `refs.bib` is 326 → 303 and now
corresponds to the book.

**Q-032.** Sorted by the rule agreed on the page: a note stays if it says what
the source **says or is**, and goes if it records what was done to check it.
**167 of 191 notes were already purely descriptive and were not touched.** Six
were pure verification: four had a descriptive core and were rewritten to it
(zkLLM's parameter count and proof time, deep-leakage's recovery claim,
backdoor watermarking, rank-one model editing); two had none and were deleted.
Eighteen were mixed and were trimmed to their descriptive core.

Then the cap. The average entry without a note is **401 characters**, so an
annotated entry may run to **802**. Twenty-nine exceeded it; twenty-six were
trimmed to fit, over two passes and then a mechanical one that drops trailing
sentences until the entry fits.

**Three cannot comply and are left as they are:** `ganguli2022redteaming` (993),
`casper2023open` (903) and `maslej2025index` (765) exceed the cap **on their
bibliographic fields alone**, before any note — they carry 19-, 32- and
23-author bylines. Deleting their notes would not bring them under and would
lose real description, so the cap is applied where it can bind and reported
where it cannot.

Notes: 198 entries, 6,432 words, down from 210 and 8,695.

## Group 3 — the tool

`finishing/tools/xref_pairs.py`, written to the author's specification: for every
cross-reference, the citing sentence followed by the opening sentence of the
section it points at; if either is under 15 words the preceding sentence comes
with it, and if either is under 10 both neighbours do. Output at
`finishing/reports/xref_pairs.txt` — **829 pairs across 153 sections, 0
unresolved, 0 empty targets**, about 325KB.

Two things the build required and the specification did not say. **The cited
sentence is the target section's first prose sentence**, because that is where
this book's sections state their claim, so a mismatch reads as "the citing
sentence says the target does X; the target opens by doing Y." And
`common.tex_prose_line` renders a reference as the number it prints, which loses
which section was meant, so each reference is swapped for an opaque token before
the prose is extracted and read back afterwards.

## Numbers

93,911 → 94,432 words; 191 pages, unchanged; cross-references 826 → 829.
`refs.bib` 326 → 303 entries. Sections 3.1, 3.7, 6.1.1 and 11.

## What was checked, and what was not

Checked: `check_all.sh` green; the PDF builds clean with zero undefined
references after every step, including after 23 entries left `refs.bib`. The
sorting of all 191 notes was done by reading the 24 that carried any
verification language and leaving the rest, so the descriptive/verification
split was applied by reading rather than by pattern alone.

Not checked: the 829 pairs themselves — the tool exists and its output has not
been read, which is group 4's work and the point of building it. The sentence
splitter is a heuristic and errs toward splitting too often, which costs a reader
context and hides nothing. Whether the three non-compliant entries could be
brought under the cap by shortening their author lists was not considered, since
that would falsify the bibliographic record.
