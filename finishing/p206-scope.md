# P206 — §8.2.1 folded up into §8.2

The author's ruling on the one item P205 flagged and declined to decide:
*Folding §8.2.1 up into §8.2 would close it — please do.* **Done.** The book is
**88 sections, 74,121 words and 155 pages**, suite green, 0 undefined references
and 0 undefined citations.

## What the ruling closes

D-307's cut of §8.2.2 left §8.2 with exactly one child. **No other parent in the
book has fewer than two**, so the shape was a first. It is closed: the minimum
child count across the outline is two again, and §8.2 *Ask the People It Happens
To* is one section of **995 words** carrying no subsections.

§8.2.1's title, *Public Deliberation and Participatory AI Governance*, is retired
along with its number. It was the more generic of the two — an inventory label
against a sentence in the book's own voice — and the parent's title is what a
merge keeps.

## Why the merge needed no prose

**Nothing was rewritten and nothing was lost.** The book measures 74,121 words
before and after; what left the file is one `\subsection` line and one `\label`.
Three things were already true of the text and are the reason a straight merge
reads:

**The pivot sentence was already a pivot.** §8.2.1 opened on *What governance adds
to development is machinery for bringing public input to bear on a decision at a
single point in time instead of through an ongoing relationship.* That sentence
takes *development* from §8.2's own list of development-stage mechanisms —
cross-sector funding, design workshops held while a system is still a prototype,
advisory boards, development conducted with a community. Written as a subsection
opener, it functions as a paragraph transition, which is what the merge needs it
to be.

**The run-in head already spanned both halves.** `\runin{What none of these
mechanisms does}` names *citizen assemblies, standing consultations, inclusive
design workshops, participatory design, the vTaiwan model* — the first and third
from §8.2.1's enumerate, the middle two from §8.2's prose list. The limiting
argument was always about the union of the two sections, and the subsection
boundary sat inside its scope.

**The setup and its payoff are now adjacent.** §8.2 ends on *A board's worth is
therefore measured by what happens the first time it says no.* The enumerate's
third item answers it: *The panel's short life is the governance lesson, and it
is the answer to what happens the first time a board says no.* That question and
that answer were separated by a heading and are not now.

## What was checked

**Nothing pointed at either label.** Zero `\ref` resolve to `sec:8.2.1`, and zero
to `sec:8.2`. The merge cost no repointing, and **no renumber map was written,
because no number changed meaning** — §8.2.1 was §8.2's only remaining child and
§8.3 onward is untouched.

**Both rows were `drafted`, `revise`, `agent-drafted`**, so no status question
arose. The book's one `accepted` row is chapter~6; D-307 cut the other.

**The run-in count is right for the length.** At 995 words the merged section is
under the 1,500 at which `style.md` §4a wants run-in heads, and it carries one.
No head was added at the seam: §4a's rule is that paragraphs are enough below the
threshold, and the pivot sentence is doing the work a head would do.

## The ledger row was folded, not dropped

§8.2's row now carries, for the merged section:

| Column | Value |
|---|---|
| `words_v3b` | 880 — §8.2's 389 plus §8.2.1's 491 |
| `evidence` | the union: `claims:2;unmarked-list-items:5`, which was §8.2.1's |
| `decisions` | the union, thirteen IDs |
| `notes` | §8.2's own, then this pass's entry, then §8.2.1's entire note history |

Carrying the note history matters because §8.2.1's row holds the record of work
now sitting inside §8.2 — the P3 correction of a fabricated *financially
independent* claim about the DeepMind panel, rewritten into the governance lesson
the section still turns on, among others. Dropping the row would have deleted the
provenance of text the book keeps.

## One thing observed and left alone

The merged section runs **two mechanism lists in sequence**: §8.2's prose list of
four development-stage mechanisms, then the enumerate's three governance ones.
**§8.2's *ethics advisory boards* and the enumerate's *AI ethics committees* are
the same object.** The subsection break used to hide the adjacency and does not
now.

**Left as it stands**, on the reading that this is setup and treatment rather than
repetition: the first list exists to make the point that three of the four
mechanisms inform a system and one can stop it, and the enumerate's third item is
where the one that can stop it gets its case. **Recorded because a later reader
may weigh it differently**, and because it is the kind of adjacency P205 was
opened to deal with elsewhere in the same chapter.

## Files touched

| File | Change |
|---|---|
| `manuscript/sections/ch08/08_02.tex` | §8.2.1's body appended, unchanged |
| `manuscript/sections/ch08/08_02_01.tex` | deleted |
| `manuscript/sections/ORDER.tsv` | one row removed; one sha256 refreshed |
| `manuscript/sections.tex` | regenerated, 88 inputs |
| `manuscript/table-of-contents.txt` | regenerated, 88 entries |
| `finishing/outline.tsv` | one row removed |
| `finishing/ledger.tsv` | one row folded into §8.2's and removed |
| `finishing/DECISIONS.md`, `finishing/STATE.md`, `finishing/PLAN.md` | D-308, new lead, header figures |

## Measured after

88 sections, 74,121 words, 155 pages, 258 cross-references against 88 labels, 222
bibliography entries all cited, 0 undefined references and 0 undefined citations.
Suite green. Chapter~8 is 8 sections and 5,753 words, its subsection level
surviving only under §8.3.

**The committed proof pair is still stale** — 157 pages against the book's 155,
and `README.md` still says 157. Not rebuilt this pass.
