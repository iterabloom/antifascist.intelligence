# P213 — the author's 43-item list against one habit, and two items added on the finding

The author supplied a numbered list of 43 edits, delivered in five batches, each
item giving find-text, replacement-or-delete, and a one-line reason. **The
reasons name a single habit**: a sentence that credits the book with a virtue
the reader has not asked it to demonstrate — restraint, consistency, courage in
conceding — placed next to the substance it is commenting on. The list does not
use a word for it. What the items have in common is that each removes the
comment and keeps the substance.

**Every item was applied as written.** Where an item specified a replacement,
the replacement is the author's text, not drafted here. Two further cuts were
made on the author's instruction after the list was exhausted, both of them
findings reported from inside the run rather than items on it.

## Shapes the list removes

**The announced concession.** *Two concessions belong inside the argument rather
than after it* (item 2), *Two boundaries are worth marking* (item 10), *Two
qualifications belong with the case* (item 25), *One limit is plain and a second
takes longer to state* (item 40). In each the next sentence states the thing.
The count and its placement were the whole of the removed content.

**The pre-certified reply.** *The parity claim invites a reply, and the reply is
correct* (item 19); *Those two concessions together make the rule look
ceremonial, and the reason it is not is section~2.4.2's* (item 15). The reply is
still there; it now has to work rather than be introduced as working.

**The instructed feeling.** *Borrowing either answer should be uncomfortable and
it is worth saying why* (item 11), *That is uncomfortable and it is the best
finding here* (item 21), *The cost arrives immediately and it is serious* (item
23). The author's reasons say the reader can assess seriousness from the
conflict described.

**The claimed self-test.** Items 9, 26, 27, 28, 32, 34, 35, 36 and 43 take out
every statement that chapter~7's self-application is *the only test the
definition gets*, that the reading *produced a result its holder did not get to
choose*, and that *an instrument does that; a weapon never has to*.

## What the sweep did to chapter 7

**§7.4's final paragraph is gone entire** (items 34, 35, 36), and the section —
which is the chapter's last — now ends on the preceding paragraph: *everything
published under the heading of alignment, including this book, is being
collected by a channel whose owners decide what it moves.*

**Nothing was lost with the two summaries removed at items 32 and 35.** Both
results are worked out earlier in the same section: the four features entry by
entry from `07_04.tex:8`, and the five discriminators at `:23`, *Run against all
three instances, they clear all three.* What the summaries carried was the
framing.

## The two cuts that were not on the list

**Chapter~1's *one test* clause** (`01.tex:32`). Items 9, 28, 32 and 43 between
them removed every other statement that chapter~7 is the definition's only test,
leaving chapter~1 asserting book-wide what the book no longer said anywhere.
Reported, and the author ruled it out.

**§9.2's *the temptation to supply one is worth naming rather than following***
(`09_02.tex:25`). Found on the first search of the run, reported before any item
touched it, cut last on the author's instruction. The paragraph now opens
*Nothing on that list needs a chassis* and the two sentences after it do the
work the clause announced.

## Found while cutting, and left standing

**§2.2 now states chapter~7's task a third time.** Item 9 replaced a
self-certifying sentence with a description of the chapter's work; the same
tripartite list — the machinery, the field, the book — is already in the
Foreword at `00.tex:11` and in chapter~1's route paragraph at `01.tex:32`.
Removing chapter~1's trailing clause made the first two near-identical, differing
in two verbs. The sentence before §2.2's, *Chapter~7 is where this book does it,
and does it at length*, already points there. **Deleting §2.2's is one line and
was not done**: it is a judgment about which of three sites to keep, and the
author has not made it.

**Item 16's rationale is not met by item 16.** Its note says *if the conclusion
has changed, its new wording should show that.* The deletion removed the
announcement; nothing in the surviving §3.3 paragraph shows the conclusion
moved. No wording was added.

**`06_04_01.tex:52` still reads *What survives both qualifications is the
shape*** three sentences after item 25's cut. Both qualifications are still
stated, so *both* resolves.

**`07_04.tex:31`'s *It is also the only time…*** now takes its subject from the
sentence before rather than from the one item 31 deleted. It resolves; it is
looser than it was.

## Two figures in the record disagree, and this pass did not reconcile them

**`STATE.md`'s lead and `p212-scope.md` both give 79,081 body words for the
tree at `5c80425`. `section_stats.py` run on that same commit sums to 78,940** —
141 fewer. Which is right, and how the record's figure was derived, was not
established here. **The figures below are `section_stats.py`'s**, and the
before-figure is the tool's 78,940 and not the record's 79,081, so that the
delta is measured by one instrument throughout.

## Reports

**Every report a tool regenerates was rerun.** Six moved: `section_stats.tsv`,
`tics.tsv`, `voice.tsv`, `epigram.tsv`, `xref_shapes.tsv` and `xref_pairs.txt` —
the last coming off the previous lead's stale list, being a tool's output rather
than a hand read. `claims.tsv`, `dated.tsv`, `negatives.tsv`, `xref_content.tsv`
and `headings_reconcile.md` regenerated byte-identical. **Six stay stale and cannot be fixed on
this machine**: the four `redundancy*` files need a package that is not
installed, and `list_candidates.tsv` and `triage-summary.md` are one-shot
P0-P1 instruments. `xref-paragraphs-{related,unrelated}.md` are hand reads keyed
to paragraphs this pass cut, and were not re-read.

**Measured:** 88 sections, **78,249 body words** (from 78,940; 691 removed),
**159 pages** (from 160), 230 cross-references against 88 labels, 226
bibliography entries, 0 undefined references and 0 undefined citations. Suite
green.
