# P211 — the same list's Tier 2 and Tier 3, and §2.1 dissolved

Items 16 through 22, which the list says run last so the compression standard
reaches P210's additions, followed by the author's call on the container item
17 left empty. `renumber-map_2026-09-14.tsv` records both this pass's chapter~2
moves and P210's insertion of §3.7.

**One mapping trap, and it caught nothing only because it was checked.** The
list predates P210's renumber, so its *§3.7* in items 16 and 22 means the
population section, which is now **§3.8**. Item 12 had already confirmed that
reading at P210.

## The five items that went in whole

**Item 16.** Four compressions, the item's keep-list honored entire: §3.8's
fourth-way restatement to a clause and a cross-reference, §4.3's re-derivation,
§8.3.4's incorporation instance, and §9.1.1's re-derivation with the sentence
kept. §8.3.4's had duplicated §9.1.1's sentence verbatim, which is why it went
rather than compressed.

**Item 17.** Forward references **121 → 32**. Chapter~1's route paragraph 238 →
202 words with chapter~7 still named and still characterized as the book's one
self-test. §2.1's map paragraph cut, which is what led to the dissolution
below. **Two latent tense errors repaired**: §3.4 said §5.2 and §4.2 *has
already shown*, of sections that come later.

**Item 18.** The sincerity line moved so it lands on the reader's first
encounter with the verdict; the old-test run cut to two sentences; the
three-absent discriminators to four; *Structure, not indictment* halved. The
item asked that one consequence be checked, and it holds: §7.3's transfer
passage still opens on *I cannot show that this transfers* and closes on a
limited *What I can say is*, with the structural note after it, so it reads as
a concession rather than as the chapter's conclusion.

**Item 19.** The data-center box dissolved into the paragraph below it, which
also repaired a dangling referent — *within a few miles of the turbines* had no
antecedent once the box was gone. Gaza and Maven kept, which is what makes them
read as parallel.

**Item 21.** §3.3's cryptography cluster, Balkin and multi-principal assistance
games from five paragraphs to three, with the custody sentence at full weight.
James, Pekrun and Winkielman reduced to Pekrun; `winkielman2001mind` left the
bibliography with it.

## The two that came out short of their targets

**Item 20 is partial.** Nine section-ending cadences were cut on the item's own
delete-and-reread test. Chapters~9 through~12 yielded almost nothing: their
final sentences carry content, and the per-chapter designation the item asks
for is not realized there.

**Item 22's first pass converted 5 of 173 hits, not the fifth the item
targets.** The census was run whole and the item's own test applied to every
hit: *is the negated half something a reader might actually have thought?* In
the large majority it is, and it is usually the sentence immediately before
that put it there — *fascism as a costume*, *a residue engineers would strip
out*, *a function added to a system that would otherwise sit there inertly*.
The repository's own `reader_tax.py --class echo` finds 2 hits book-wide. The
colon pass came out the same way: 453 colons that specify rather than restate,
which the item says to keep. **If the frequency is to come down regardless of
the strawman test, that is a different instruction and it has not been run.**

**Item 22's fourth pass went in whole**, and it is the only part of Tier 3 that
adds. Three cases, each built from material already in the book: the
crossed-out swastika as §4.1's two settings on their two objects inside one
judgment; a new run-in at §5.3 taking §3.6's first prohibition through all six
steps with a passing and a failing trajectory; and §9.3.5 reading §8.1's
headcount series as level against slope, with its limit stated in the same
breath — what that record measures is the channel's capacity, not the price of
using it.

## §2.1 dissolved

Item 17 emptied the container and the author ruled on the result. Deleting the
heading alone would have orphaned two subsections, so both were promoted:
**2.1.1 → 2.1 under the container's title, 2.1.2 → 2.2**, and 2.2 through 2.3.2
displaced to 2.3 through 2.4.2. Fifty label and reference rewrites in one
simultaneous pass across 21 files — sequential would have collided, since 2.1.1
becomes the number 2.1 was using.

**The resulting shape is not an anomaly.** Two flat sections then two
containers is chapter~6's and chapter~9's shape, and chapter~3 is flat
throughout. `headings.py` reports `empty=0` again.

**One pointer was repaired by the move rather than by an edit.** The glossary's
**Floor** entry says the term is *introduced in section~2.1*. It had been
pointing at the empty container; it now resolves to the frameworks section,
where the floor comes off a deontological footing onto an ethological one.

**Two titles became one.** *Six Theories, None of Which Will Save Us* and *Six
Ethical Frameworks, and Where Each One Runs Out* were near-duplicates. The
container's survives. What it drops is *and Where Each One Runs Out*, which
names the section's method, and swapping back is one line.

**What was deliberately not repointed.** `STATE.md`'s superseded pass entries
describe passes as they stood, and rewriting them would falsify the record —
the renumber map is the mechanism. `style.md` §8's claim that `\textbf`'s only
use is a table header in §2.2 is already recorded at `STATE.md:295` as false
and deliberately left alone; repointing it would make it differently false. The
other two stale pointers in `style.md` are repointed.

**Measured:** 88 sections, 78,977 body words, 159 pages, 232 cross-references
against 88 labels, 223 bibliography entries, 0 undefined references and 0
undefined citations.
