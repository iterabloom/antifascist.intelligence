# P66 — four tables of contents cut, three of them out of their section numbers

**The author's finding.** Four sections are vestigial *because they are actually
tables of contents wearing section numbers*: §6.3.3 *Strategies for AI Safety and
Risk Mitigation*, four practices of which three point at other sections for their
substance; §9.1.3 *Public-Private Partnerships*, whose live claim is two
sentences and the rest preamble; §8.2.1 *Engaging Diverse Stakeholders*, saved
only by its final move, cut to that; and §9.1.1 *National Policy Guidelines*,
which diagnoses itself — *“the list is not where national policies differ”* — and
whose list is the vestige.

**All four hold on reading.** The measurements differ slightly from the finding's
and change nothing: §6.3.3 is **309** words rather than 250, §9.1.3 **215**
rather than 233, §8.2.1 **197** rather than 203. `section_stats.py` counts
heading words, which is most of the gap.

**The count of three is exact.** §6.3.3's four practices are *learn the
objective*, which §4.2.3 carries; *quantify uncertainty*, which points nowhere;
*constrain the search*, which §5.6.2 carries with the same claim and the same
citation; and *keep the oversight live*, which §9.3.5 carries. Three of four.

## What the instruction did not name, and had to be handled with it

### §6.3.3's closing paragraph is the paragraph P64 cut a different section on

P64's own table records that the old §6.3.4's opener was cut **because §6.3.3's
closing paragraph already said it, in the same words**: *“The account is a claim
to check against the process, not a window onto it.”* Cutting §6.3.3 entire would
have removed that sentence from the book by way of two passes, each of which
looked correct alone and neither of which would show the loss.

This is the third time the pattern has appeared in three passes — P64 cut the
accuracy-versus-explainability tradeoff and P65 the accuracy-versus-fairness
tradeoff, and the book now states neither. **It is the first time it was caught
before the fact**, and it was caught only because `p64-scope.md` recorded the
dependency in a table. The standing check that follows: **before cutting a
section, read the scope files of passes that cut something else on the strength
of what is in it.** No tool in the suite can find this; both ends of the
dependency are ordinary prose.

The paragraph moved into §6.3's opener, where it is now **the third of the
mechanisms that carry weight later**, and *“Two mechanisms”* becomes *“Three.”*

### Chapter 9's roadmap promised §9.1.3 by name

*“First the frameworks — what national guidelines require, what industry
self-regulation enforces once honoring a commitment costs something, and **what a
public-private partnership buys and gives up**.”* The clause was removed. The
roadmap now names two of §9.1's four children where it named three of five.

**This is P64's parent-map check returning with the opposite result.** At P64 and
P65 the parent's map was independent evidence *for* the cut, because it never
mentioned the section going. Here it was a repair the cut required — and the map
that named the section was **a level above the parent**, in the chapter opener,
not in §9.1. The check has to run at both levels.

§9.1's own opener also named it, in *“Joint funding addresses a narrower
problem.”* That one is self-repairing: the cut section's claim went into that
paragraph, so what was a promise is now the treatment.

### §8.2.2's backward pointer at the cut section

*“it is the answer to the question the previous section leaves open”* became
*“it is the answer to what happens the first time a board says no,”* which is the
line the setup now ends on one heading earlier. Restated rather than repointed,
which is what D-118 and D-133 did with backward signposts that stand without the
pointer.

### Two citations orphaned, and this time nothing survives that needs them

`nsf2020airesearch` and `itu2017aiforgood` were cited only in §9.1.3 and moved to
`unused_bibliography.bib`; `refs.bib` **308 → 306**, unused **29 → 31**.
**Checked against P65's finding, which was the reverse case.** The NSF appears
elsewhere in the book — §8.1.1's Fairness in Artificial Intelligence program —
on its own separate citation. *AI for Good* appears nowhere else at all. No claim
anywhere is left holding a named institution without a source.

`achiam2017constrained` was **not** orphaned: §5.6.2 cites it for the same
technique, which is also why §4.2.2's pointer at §6.3.3 could be repointed there
rather than cut.

### §9.1.1's two locators were the only inbound references their targets had

The cut clause ended *“on which sections~\ref{sec:9.1.4} and \ref{sec:9.3} carry
the specifics.”* Nothing else in the book pointed at either. **§9.1.4 — now
§9.1.3, *Legal and ethical implications of AI systems gaining personhood* — and
§9.3 are referenced from nowhere after this pass**, and §9.1's opener does not
name §9.1.3 either. Not repaired, because re-adding an appended locator is the
class D-089 cut and the instruction is for fewer tables of contents, not more.
Recorded as a fact about the book's structure.

## Two structural checks, both clean

- **§6.3's opener never promised §6.3.3, and was already doing its work.** The
  opener's first mechanism — *“the human who can intervene… the check has to be
  continuous rather than applied once”* — **is** §6.3.3's fourth practice, *“a
  reviewer with the standing to override”* as a deployment property. The parent
  carried the child's content, which is what a table of contents wearing a
  section number looks like from above.
- **Chapter 8's roadmap and chapter 6's reach no lower than they need to.**
  Chapter 8 names §8.2 by theme and by the limit §8.2.2 closes on; chapter 6
  works at failure-mode level. Neither needed repair. Read rather than assumed.

## What this reverses

**D-101 (P37) kept both of the lists this pass cuts, and kept them for the same
reason.** The ledger notes are explicit: §8.2.1's *“four-mechanism list kept,
because the next paragraph takes it apart”*; §9.1.1's *“six-item ‘predictable
shape’ list shortened but kept, because the section's move is to dismiss it.”*
The author's finding rejects that principle in both places it was applied — a
list a section then dismisses is still a list the reader had to read.

D-101's other keep-the-list ruling used a different reason (*“the listing is
itself the argument”*, at §10.9 and §10.7) and is untouched by this.

## Where each survivor went, and why not where the instruction reads literally

- **§6.3.3's explanation paragraph → §6.3's opener.** Not into §6.1.2, the
  explainability section P64 and P65 built, whose Explainability Tools block
  already closes on its own strongest limit; a second limit stacked behind it
  deflates the first. That is the placement judgment P64 made inside this same
  section, applied again.
- **§8.2.1's final move → §8.2's opener, and the section goes.** The move cannot
  travel without its list — *“three of the four”* needs the four — and list plus
  move is about 160 words, which would have left one of the three thinnest leaf
  subsections in the book standing as a setup for the next one. **§8.2's opener
  already carried the cut section's opening claim** in its own second sentence,
  so the merge removed a duplication rather than making one. §8.2 goes 82 → 235.
- **§9.1.3's mandate argument → §9.1's opener**, attached to the joint-funding
  sentence that had been its promise. §9.1 goes 168 → 247.
- **§9.1.1's list stays in §9.1.1**, reduced from the section's opening move to a
  five-noun aside inside the sentence that dismisses it. Cut to nothing, *“most
  of the same list”* is the unspecified demonstrative D-117 spent a pass
  removing. 271 → 252, and the section keeps its number: the author named only
  the list as the vestige, and the two paragraphs on where policies do differ are
  not that.

## What was lost, named rather than repaired

- **Uncertainty quantification as a safety practice.** Bayesian methods and
  ensembles, and a system that *“can recognize an input unlike anything in its
  training data”*, appear **nowhere else in the manuscript**. §3.5 treats
  uncertainty in the off-switch sense, which is a different claim about a
  different thing. This is precisely the one of §6.3.3's four practices that
  pointed nowhere, and it goes with the section. **Not moved**, because the
  paragraph that was moved has a documented dependency in another pass's decision
  and this has none; moving both would be rebuilding the section the author cut.
  §6.3's opener is where it would go back, in a sentence, on a word from the
  author.
- **The robot-arm image** — learning to handle fragile objects without breaking
  one, against learning by breaking several. §5.6.2 has the claim without it.
- **The NSF AI Research Institutes and the ITU's AI for Good platform** as worked
  examples of the partnership model, with their two citations.
- **Two live claims in §9.1.3 that the finding does not name.** That a
  partnership convened on *“AI for good”* produces work its members already
  wanted to do, filed under a heading nobody objects to; and that a partnership
  is a *better* venue for reputation-laundering than a voluntary code, because
  the government partner supplies credibility the company could not manufacture.
  Both are arguments rather than preamble. **The finding names the live claim as
  two sentences and I did not extend past it.**
- **The enumeration of what a national AI policy contains** at full length, and
  the two locators inside it.

## A correction to P65's record

`p65-scope.md`, D-146 and `STATE.md` all report *“all four were `drafted`
already”* and give the result as **3 `accepted`, 136 `drafted`**. Both halves are
wrong. The ledger at P64's commit held **3 `accepted` and 137 `drafted`**; at
P65's commit, **2 and 137**. The row that went was §6.1.2, *Ensuring Fairness and
Equity in AI Decision-Making*, and it was **`accepted`**.

**P65 cut an author-accepted section and reported that it had not touched one.**
That is a different fact about the pass than the one recorded, because an
accepted section is one the author has read and signed off. Corrected in place in
`p65-scope.md`; D-146 cannot be corrected, `DECISIONS.md` being append-only, so
the correction is carried here and in D-147.

**This pass touched one `accepted` row and did not edit it**: §8.2.3 *AI Literacy
Outside the Classroom* renumbers to §8.2.2, label line only, body untouched. The
three sections cut were all `drafted`.

## Figures

**95,285 words**, down **429** on P65's 95,714. The three cut sections were 309,
197 and 215 — **721 words** — against **317** moved into the three host openers,
19 out of §9.1.1's list, 8 out of chapter 9's roadmap, and 2 added by the two
pointer repairs. **136 sections**, down 3. **190 pages, unchanged**: the fall is
spread across three chapters and absorbed by pagination rather than showing.
Chapter 6 goes 9,863 → **9,639**, chapter 8 6,387 → **6,345**, chapter 9 7,529 →
**7,366**. §6.3 309 → 394, §8.2 82 → 235, §9.1 168 → 247, §9.1.1 271 → 252,
chapter 9's opener 164 → 156.

All `\ref{sec:}` **556 → 551**: four out with §6.3.3 and two of those four back in
with the moved paragraph, one out of the glossary, two out of §9.1.1. Glossary
locators **117 → 116**, with three more renumbered. `refs.bib` **308 → 306**,
`unused_bibliography.bib` **29 → 31**. 0 undefined references, 0 undefined
citations, `check_all.sh` green, 551 `\ref` resolving against 136 labels.
`renumber-map_2026-08-31f.tsv` translates all three cuts.

**The thin-leaf census moved but did not shrink.** §8.2.1 was one of three leaf
subsections under 200 words and is gone; there are still three under 230 — §6.3.2
at 195, §8.2.2 at 183, §8.3.1 at 211 — which is Q-029's class, closed by
execution at D-102 and not reopened here.

Printed pages 78 and 99 rasterized and read: §6.3's opener running *“Three
mechanisms here carry weight later”*, and §8.2's opener closing on *“the case
that settles it comes next”* directly above §8.2.1's DeepMind Health panel.

## Not done

- **The committed proof pair is stale after this pass.** It was built at P65 and
  is 190 pages, which is also this pass's page count, but its text is the
  pre-P66 text. **[Rebuilt at P73: the pair now stands at 187 pages, covering P66 through P73 together. The date had not rolled over, so it was rebuilt in place and the README's links did not move.]**
- **Fourteen ledger rows tagged D-147**; the three cut rows deleted with their
  titles and numbers carried into the hosts' notes. **2 `accepted`, 134
  `drafted`.**
- **The two claims listed above as lost from §9.1.3 were judged, not tested.**
  The judgment is that the finding's *“two sentences”* is the instruction's
  boundary, not that those claims are weak.
- **Nothing in the four sections was checked against the wider literature**, only
  against this manuscript. Where this file says a claim appears nowhere else, it
  means nowhere else in the book.
