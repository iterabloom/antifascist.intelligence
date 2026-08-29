# Open questions

**Current as of 2026-08-29, after D-111. The author has now ruled on all eighteen.**
Eight were closed or left standing with no action; ten produced work, of which six are
done in P47 and four remain as the reading group — Q-035's measurement over chapter 5,
Q-038's sweep of chapters 2 to 4, Q-043's sweep by subject, and Q-045's whole read of
chapter 3 and section 11.2. Each entry below now carries its ruling. The re-check
paragraphs from D-110 are kept, because they are what the rulings were made against.

**Superseded header, kept for the record.** All
seventeen that stood before the D-110 review were re-checked against the manuscript
rather than carried forward. **Two closed by execution** — Q-028 (chapter 3's
position, settled at P38 by ruling its default) and Q-029 (the thin subsections,
folded at P38) — **and one is new**, Q-045, which the review itself produced.
**Nine had figures that had gone stale**, several of them reversing the direction
the question recorded: the cross-reference count is rising again, chapter 3 is now
the longest chapter in the book, the bibliography carries half again as many notes,
and the class Q-043 names has tripled its evidence. Each entry below now carries a
dated re-check paragraph saying what moved and whether the default still holds.
None blocks work and every default still applies.

**The figures this file turns on, measured 2026-08-29 after D-109:** 93,911 words,
153 sections, 191 pages; 826 `\ref{sec:` calls, one per 114 words; `refs.bib` at
326 entries with 23 uncited and 210 carrying notes totalling 8,695 words; 317
instances of "rather than"; 124 glossary locators; five leaf subsections under 230
words. For orientation read `finishing/STATE.md`.

The other standing item is not a question. **140 of the book's 153 sections are
`drafted` and unread**, and the seven passes of 2026-08-29 concentrated their
additions in chapter 3 and section 11.2, neither of which has been read whole
since before any of them. That concentration is Q-045.

**P38 renumbered chapters 2, 4 and 5 and merged fifteen subsections away;**
`renumber-map_2026-08-29.tsv` translates. Entries below that name a section under 2.1,
2.2, 2.3, 2.4, 4.3, 5.1, 5.2, 5.4, 5.5, 5.6 or 5.7 use the pre-P38 number.

All section numbers here use the **post-D-043 numbering** (chapters 3 and 7 are
new; old 3–9 became 4–11). Entries written before 2026-08-25 refer to section
8.7.6 as the geopolitics section and to 8.7.7 as the democratic-dividend section;
D-067 split 8.7.6 into 8.7.6–8.7.9 and renumbered 8.7.7 to 8.7.10.

**Every entry below written before D-093 has not been renumbered for it.**
P32 split chapter 8 into chapters 8, 9 and 10 and shifted old 9, 10 and 11 to 11,
12 and 13; `renumber-map_2026-08-28c.tsv` translates. Where an entry below says
chapter 9 it means what is now chapter 11, and where it names a section under 8.4,
8.5, 8.6 or 8.7 those are now 9.1, 9.2, 9.3 and chapter 10. Q-031 is about what is
now chapter 11.

**P34 renumbered chapter 3.** Old sections 3.2 through 3.7 are now 3.4 through 3.9;
`renumber-map_2026-08-28e.tsv` translates. Q-021 and Q-028 name chapter 3 sections by their
pre-P34 numbers. Q-036, Q-037, Q-042, Q-044 and Q-045 are written in the new numbering.

A new question goes above the "Resolved" line with a default and the moment it
applies. Nothing here blocks work.

---

### Q-019 — The glossary defines a term the book never uses

**Closed by execution, D-061. The record is under "Resolved" below; this entry is the question as it stood.**

`GPAI` (the Global Partnership on Artificial Intelligence) has a glossary entry.
The term appears **nowhere in the body** — checked against every commit back to
the original split, so this is not P11 fallout, it has always been so. Its two
locators, §8.4.5 and §8.7.1, both named sections that do not contain it, and P14
removed them. The entry now says in its own text that the book does not take the
term up.

It is not simply stray: the Partnership on AI entry uses GPAI as its point of
comparison ("what GPAI adds when governments, not companies, are the members"),
so the two entries are written as a pair.

- **(a) Default — leave it, as P14 did.** A glossary may define an adjacent term
  it uses to draw a contrast. The entry now discloses its own status.
- (b) Cut the GPAI entry and the dependent clause in the Partnership on AI entry.
  A glossary indexes the book's vocabulary, and this is not in it.
- (c) Give the body a sentence on GPAI — most naturally in §8.7.1, on
  cross-border cooperation — so the entry earns its locator.

*Default applies now. Deleting author-accepted P5 content was not a call to make
without asking; (c) is the only option that adds anything.*

---

### Q-021 — §3.6's title promises what its body does not do

**Closed by execution, D-061. The record is under "Resolved" below; this entry is the question as it stood.**

Chapter 3 was promoted whole from old §2.1.5 with **text unchanged** (P11,
`p11-scope.md:159`), and split at its own run-in heads. §3.6, "What Follows for
the Rest of the Book," was one of those heads. Inside §2.1.5 the title was
accurate: what followed §2.1.5 was the rest of the book. At chapter rank it now
reads as chapter 3's forward-facing close, and the body is not that — all three
paragraphs look backward, closing the bearer/sufferer argument against §2.4.4's
consent finding and §2.4.1's caveat.

The forward work does get done, in the **chapter opener** (`ch03/03.txt`), which
names the three arrivals and states the collision: "The design chapters build the
thing chapter 8 and chapter 10 say is insufficient, having already dismissed the
thing they say is necessary." So nothing is missing from the chapter. What is
wrong is that one section's title points a reader at a section that does not
contain what the title promises.

- **(a) Default — retitle §3.6 to name the bearer argument it closes.** Changes
  no prose, removes the false promise, costs one heading line. The chapter keeps
  its forward-facing work where it already lives, in the opener. Note the retitle
  regenerates the TOC (`headings.py --write-toc`) and touches `outline.tsv`.
- (b) Add a §3.7 that faces forward, keeping §3.6 as it is. Gives the chapter a
  genuine close; adds new material to a chapter the author has not yet read at
  chapter rank.
- (c) Fold the bearer close into §3.5 and rewrite §3.6 to do what its title says.
  Most coherent editorially, most invasive — it rewrites text P11 moved unchanged.

*Author's answer 2026-08-24: (a) is the preferred repair, recorded as the default
rather than applied, because the scope call was Tier 1 only. Applies at the next
pass that touches chapter 3.*

---

### Q-022 — The design chapters do not lean on the floor the introduction says they do

**Closed by execution, D-061, and again by declaration at D-078. Chapter 1's roadmap went on contradicting the closure until P29 corrected it. The record is under "Resolved" below.**

Chapter 1 bills chapters 4 and 5 as "the learned half that sits above that floor"
and says "a reader should carry all three through the design chapters, **because
the design chapters lean on all three**." Measured against the text:

- The word *floor* appears **0 times in chapter 5, 0 in chapter 6**, and once in
  chapter 4 in an unrelated sense (the seven-plus-or-minus-two memory figure).
  Chapter 3 uses it 20 times, chapter 8 26 times.
- Chapters 4–6 carry **two** references to chapter 3 in total: §4.1.2 → §3.4 (on
  machine testimony) and §5.6.3 → chapter 3. Both are of the "this became
  load-bearing elsewhere" type — pointers *out*, not chapters leaning *on*.
- Chapter 6 names neither chapter 3 nor the floor. It is one hop away: `06_03.txt`
  links to §5.6.3 four lines above its own kill-switch paragraph, and §5.6.3 links
  on to chapter 3. Routed, not isolated.

The sharper form of the complaint is that §5.6.3 is an *arrival at* the floor, not
an *application of* it — so adding pointers would satisfy the letter of chapter 1's
promise without its substance.

**Not previously argued.** P10 diagnosed this collision in the same terms
(`p10-scope.md:59-69`, "chapters 3 and 4 — 30.3% of the book, measured — build
learned judgment instead") but its fix was the floor chapter itself plus
cross-links among the three arrivals. Making the design chapters lean on the floor
was never scoped, declined, or deferred.

- **(a) Default — leave it and soften chapter 1.** Change "lean on all three" to a
  claim the body supports. One sentence; no design-chapter work.
- (b) Forward-pointers at §4.1, §5.1 and §6.3. Satisfies the letter. Note §6.3
  already links to §5.6.3, so that one is a redirect, not a new pointer.
- (c) Open a P15 pass that makes the design chapters actually use the floor. This
  is writing, and the largest option by a wide margin; D-007 governs how far it
  can go.

*Default applies now. (c) is the only option that makes chapter 1's sentence true
as written.*

---

### Q-026 — The cross-reference cut reached a fifth of what was asked

D-089's instruction was that the book's explicit chapter and section references
make the prose read as a navigated repository, and that cutting half would improve
continuity. P28 cut 79 of 791, **10 percent against the 50 percent named**, and
recorded the shortfall with its cause: judging removability from isolated
sentences overestimated it roughly threefold. P29 then removed 40 more as a side
effect of cutting prose without improving the density: measured one consistent way,
every `\ref` in the section files against `section_stats.py`'s word count, it went
from one per 116 to one per 114. The prose came out at about the rate the
references in it did.

What is left is 467 leaf-inline references concentrated in chapter 3, chapter 7,
section 9.1.7 and section 10.2.1 — the spine P27 rewrote — where a reference is
usually importing a result rather than filing a topic.

- **(a) Default — stop here.** Every class that could go without touching an
  argument is gone. Cutting further means a sentence that borrowed a result has to
  restate it in a clause, which trades reference density for length.
- (b) Cut into the leaf-inline references in those four places, accepting the
  restatements. This reverses part of D-013, which built the regime to replace an
  argument that had been made nine times, and part of D-078.
- (c) Set a target density rather than a count — one per 200 words, say — and cut
  wherever it takes to reach it, which concentrates the loss in chapter 3.

*Default applies now. `p28-scope.md` has the class-by-class record.*

**Re-checked 2026-08-29 after D-109.** **The direction has reversed and the default now means something different.** The
count is **826**, up from the 758 this entry recorded — P39 through P45 added 68 while
adding 5,565 words. Density is unchanged at one per 114, which is why nothing flagged
it: every pass added references at exactly the rate it added prose. So "stop here" has
held as a rate and failed as a count, and D-089's original complaint was about the
count a reader meets. Nothing in this file asks a pass to check its own reference
budget, and that is the gap this re-check found rather than a new option.

---

**Ruled 2026-08-29 (D-111): deferred indefinitely.** No option taken and none foreclosed.

---

### Q-027 — Chapters 4 and 5 stopped at 13.5 percent

D-090 asked for chapters 4 and 5 to be cut or refocused around what the floor
requires. They came to **13.5 percent**, against 20.2 percent for chapter 2. The
reason is recorded rather than smoothed over: those chapters were cut 29.9 percent
at P11 and rewritten at P26 to carry chapter 3's obligation, so the survey in them
was thinner to begin with, and what came out is what the survey amounted to.

- **(a) Default — leave it.** What remains is argument aimed at the floor plus the
  evidence that makes it believable.
- (b) Cut the evidence as well — the inattentional-blindness studies, the
  predictive-coding account, the Kohlberg box, the trolley literature section 2.3.4
  points at. That reaches roughly 20 percent and converts several claims into
  assertions a reader has to take on trust. Section 2.3.4 depends on the trolley
  material being somewhere, so it would have to move rather than go.
- (c) Cut by removing whole sections instead of compressing, which is Q-029.

*Default applies now.*

**Re-checked 2026-08-29 after D-109.** **P38 took option (c) and went further on the same instruction.** Chapter 4 came down
9.8 percent and chapter 5 from 29 sections to 23; the two are now 7,336 and 9,823 words,
7.81 and 10.46 percent of the book. P38 stopped where this entry says it would, and for
the same reason stated the same way — the remainder is evidence. **The wall has now been
hit twice by two passes working independently**, which is stronger than one pass's
judgment and is the reason to read (a) as settled rather than merely defaulted.

---

**Ruled 2026-08-29 (D-111): left open.** Not closed as settled; a later pass may revisit it.

---

### Q-028 — Whether chapter 3 should move earlier in the book

**Closed by execution, D-102 (P38), on option (a). The record is under "Resolved" below; this entry is the question as it stood.**

P29 made chapter 3 the book's center by what leads into it: chapter 1's roadmap
corrected, chapter 2's opener rewritten around the four results chapter 3 uses,
four chapter-5 openers stating what the floor takes from them. Its share of the
book went from 7.62 to 8.13 percent without a word changing in it. Position was
left alone.

- **(a) Default — leave it third.** Moving it reverses D-043's promotion, and the
  dependency runs the wrong way: chapter 3 argues from section 2.3.4's affect
  evidence and section 2.4.1's ladder, both of which precede it.
- (b) Promote it to chapter 2, folding the four load-bearing results of the
  present chapter 2 into it and demoting the rest. This is the version that makes
  the center structural rather than rhetorical, and it is a chapter-scale rewrite
  plus a renumber of everything after it.

*Default applied, then was ruled on.* **P38 answered the instruction "move the central floor argument earlier" by taking (a) and delivering "earlier" in pages rather than in position** — chapter 3 begins on page 23 of 182 where it began on page 27 of 189 — on two grounds stated rather than assumed: chapter 3's opening stages the floor as a gap chapter 2 left, and the instruction's own second clause presupposes chapter 2 running first. Q-036 had already read (a) as the answer for the same dependency reason.

---

### Q-029 — The subsections P29 left thin, and whether to fold them

**Closed by execution, D-102 (P38), on option (b). The record is under "Resolved" below; this entry is the question as it stood.**

Twelve leaf subsections are now under 230 words, and eight of them are P29's
work: 2.4.3 at 142, 5.5.2 at 162, 4.3.2 at 184, 2.2.2 at 186, 5.1.2 at 195, 5.4.1
at 201, 2.3.2 at 212, 2.4.5 at 220. The other four — 6.2.2, 6.3.2, 8.2.3, 8.4.3 —
were that short before this session and are not new. The book already carries much
shorter section openers; what makes these look odd is that they are leaves.

- **(a) Default — leave them.** Folding renumbers a chapter against 801 resolved
  references and needs a renumber map, and P28 rebuilt the reference regime days
  ago.
- (b) Fold them into their neighbors, with a renumber map on the
  D-031 / D-043 / D-091 model. P30 shows the cost: four sections moved, 16
  references repointed, five files of bookkeeping.

*Default applied, then P38 took (b).* **All eight of P29's thin leaves were folded**, with `renumber-map_2026-08-29.tsv` carrying 34 rows and every inbound reference read against the surviving host's actual text. **Five leaves remain under 230 words and none is P29's**: 6.2.2 (212), 6.3.2 (199), 8.2.1 (198), 8.2.3 (215) and 9.1.3 (221, formerly 8.4.3). Those four this entry already excluded as pre-existing, and 8.2.1 joined them by other passes' cutting. The cost this entry warned of was paid and is recorded: the renumber is what made someone read 30 citing sentences by hand, which is how Q-041's four pre-existing defects were found.

---

### Q-030 — `refs.bib` has 14 entries nothing cites

**The count is corrected here from 20, which was wrong when this was filed.** Measured
across every commit from P29 to now, and re-measured after P33 added nine entries and
merged a duplicate: the manuscript's 311 `\autocite` calls reach 283 of the file's 297
entries, leaving **14** — the same fourteen keys, since every entry P33 added is cited and
the one it removed was too. The breakdown was wrong the same way: two
entries were uncited before P29, not eight, and P29 orphaned twelve by cutting the
prose around them — 2 plus 12 is the 14, and 20 corresponds to nothing measured. The
14 are `affectiva2015emotionservice`, `alignmentforum2018`, `cowan2001magical`,
`dmello2007toward`, `empatica2015e4`, `finn2017modelagnostic`,
`fitzpatrick2017delivering`, `fullfact2023ai`, `matheson2016watchyourtone`,
`miller1956magical`, `rizzolatti2010functional`, `shibata2004overview`,
`warneken2006altruistic` and `xprize2021watson`, each confirmed to appear nowhere in
`manuscript/`. Nothing prints them, because biblatex only sets what is cited, so this
costs a reader nothing and costs the file its correspondence with the book.

- **(a) Default — leave them.** An entry costs nothing where it sits, and one of
  them may be wanted again by whatever pass next touches the material it supported.
- (b) Prune the 14, recording them in the commit body so they can be restored from
  git.

*Default applies now.*

**Re-checked 2026-08-29 after D-109.** **The count is 23 of 326.** The file has taken 29 entries since — P38 one, P39 one, P40
eleven, P42 four, P43 four, P44 two — and every one of those is cited, so none of the
growth is orphan growth. The nine new orphans came from prose that was cut around them:
`jigsaw2017perspective` at P38, and eight policy and corporate entries
(`deepmind2016partnership`, `g72023hiroshima`, `gpai2020joint`, `justcapital2018amazongo`,
`moda2025basic`, `openai2018charter`, `peacetechlab2019monitoring`,
`unesco2021recommendation`) from P36's and P37's cutting in chapters 8 through 12. **The
mechanism this entry describes is confirmed rather than changed**: cutting prose orphans
entries at a steady rate and nothing reports it, so (b) would have to be run repeatedly or
not at all.

---

**Ruled 2026-08-29 (D-111), and executed in P47.** Neither kept nor pruned: the 23 entries were moved to `finishing/unused_bibliography.bib`, which is deliberately not `\addbibresource`d, so they survive and `refs.bib` corresponds to the book at 303 entries.

---

### Q-031 — Chapter 9's gap list lost its nearest-work notes to the word cap

D-092 required the conversion to cost nothing in words, so something had to give.
The chapter opener's list of gaps used to carry, for each entry, a description of
the problem and a note naming the nearest existing work and where it stops — about
300 words. The list now carries the ranking and a clause, and the descriptions and
nearest-work notes live in the section that owns each gap, where they were already
stated.

What is lost is the one page a reader could stand on to see all eight gaps and
their nearest work at once, which was a real convenience and the thing the old
opener did best. What is gained is that the opener stops restating its own chapter,
which is a large part of what made it read as a catalog.

- **(a) Default — leave it.** Nothing is gone from the book; it is one place
  instead of two, and the place is the section that owns the material.
- (b) Restore the notes to the opener, at roughly 300 words, and let the chapter
  go over its previous count. The instruction's constraint was met once and
  arguably does not bind a later decision by the author.
- (c) Restore them and take the 300 words out of the sections, which means cutting
  argument rather than duplication, since the duplication is what already went.

*Default applies now. `p31-scope.md` has the full accounting of what paid for the
program.*

**Re-checked 2026-08-29 after D-109.** **Stands, with one figure moved.** The chapter opener is now 1,006 words, up 166 from
P44, which added to its collapse paragraph the question none of the nine conditions asks —
what keeps an outside party outside — and answered it with the removal cases and the CFPB
sequence. The nearest-work notes were not restored and nothing has asked for them. Option
(b)'s framing that "the instruction's constraint was met once and arguably does not bind a
later decision" is now the ordinary state of the chapter rather than a hypothetical, since
the opener has already grown for other reasons.

---

**Ruled 2026-08-29 (D-111): restore, executed in P47.** Each of the eight ranked gaps regains a *Nearest work* clause naming the closest existing research and where it stops. The opener is 840 → 1,180 words.

---

### Q-032 — Whether the bibliography should be annotated at all

D-095 cut the research diaries out of `refs.bib`: 32 notes rewritten to their
bibliographic core, every process marker gone, the bibliography from about 18,800
words to 14,237. What it did not decide is whether the bibliography should carry
notes at all. **144 entries still have one, about 6,600 words**, and they are
legitimate — “Presented at ICLR 2020,” “Adopted by all 193 UNESCO member states,”
“Widely available in English in Arendt's edited collection *Illuminations*.” None
of them narrates the search. But they make this an annotated bibliography, which
is a genre choice the book has never actually made; it inherited them from the
verification passes that wrote them.

- **(a) Default — leave it annotated.** The notes state facts about the source,
  and a few do work no other part of the book does: where a reprint can be found,
  which of two similar papers by the same authors this is, that a page number is
  taken from a review rather than the book itself, and that a frequently made
  miscitation is a miscitation.
- (b) Cut every note, leaving plain bibliographic metadata. About 7,600 words, a
  little under half what stands. The record is not lost: `reports/claims.tsv`
  holds the verification notes, and the entries keep author, title, venue, date
  and URL, which is what a reader needs to find the source.
- (c) Keep only the notes that qualify or disambiguate the citation — the
  secondhand pinpoint, the miscitation warning, the evidentiary caveat on the
  Palantir quotation — and cut the ones that merely describe what a source says,
  on the ground that the prose already says it. The resulting size was not
  measured; it needs a read of all 144.

*Default applies now. (b) and (c) are both defensible and neither is reversible
without re-deriving text from `claims.tsv`, so this is the author's call rather
than a tidy-up to be done unasked.*

**Re-checked 2026-08-29 after D-109.** **The annotated half has grown by nearly half again: 210 entries carry notes, totalling
8,695 words**, against the 144 and roughly 6,600 recorded here. The growth is this
session's: the 21 entries added by P40 through P44 all carry verification notes of the
kind option (c) would keep — what was checked, what refused a fetch, which figure came
from a catalogue record rather than the source. **That strengthens (c) and weakens (b)**,
because the newest notes are exactly the qualifying and disambiguating kind (c) preserves,
and cutting them would destroy the only record that a claim was checked against something
other than memory. Option (b)'s figure is now about 8,700 words rather than 7,600.

---

**Ruled 2026-08-29 (D-111), and it is the reverse of option (c), executed in P47.** Keep the *descriptive* notes and cut the ones recording what was done to check a source, with any annotated entry capped at twice the average bare entry — 802 characters. 167 of 191 notes were already descriptive and untouched; six pure-verification notes were rewritten to their descriptive core or deleted; eighteen mixed were trimmed; twenty-six of twenty-nine over-cap entries were brought under. **Three cannot comply**: `ganguli2022redteaming`, `casper2023open` and `maslej2025index` exceed the cap on their bibliographic fields alone, carrying 19-, 32- and 23-author bylines. 210 → 198 entries, 8,695 → 6,433 words.

**Amended 2026-08-29 (D-111).** The author ruled that the three entries that cannot meet the cap are acceptable as they stand, provided their notes describe the cited work rather than the process of revising this manuscript. Re-swept with a brace-balanced extractor, which found that the first sweep's regex had missed any note ending in a trailing comma: `casper2023open` still carried a verification sentence and `garcia2025character` a clause about an unverified docket number. Both are cut, and `maslej2025index`, over-trimmed for a cap it can never meet, has its description restored. **No note in the file now records what was done to check a source.** 198 notes, 6,433 words.

---

### Q-033 — The taxonomy of bias sources does not name the choice of training target

D-096 repaired two sections that credited LIME and SHAP with more than feature
attribution delivers. The case that forced the repair is Obermeyer's: the
algorithm's bias was in the target it was trained on — healthcare cost standing in
for medical need — which is a class of bias attribution cannot see, because it
takes the target as given.

Section 6.1.1 opens by naming where bias enters: "data collection, data labeling,
algorithm design, and implementation." Target choice is not on that list. Its
`Algorithm Design` run-in covers structural encoding (the COMPAS disparity) and
amplification (the 2017 activity-recognition study), both of which are about how a
model treats its inputs. The book now names target choice twice in chapter 6 —
section 6.1.3's new sentences and section 6.3.6's Obermeyer paragraph — so the
concept is present where it is used and absent from the taxonomy that is supposed
to organize it.

- **(a) Default — leave it.** The concept is stated where a reader meets the case,
  and a four-item list in an opening sentence is not a claim to have enumerated
  everything. Adding a fifth run-in to a section that already carries five is a
  cost against P29's cutting of chapter 2 and P32's word discipline.
- (b) Add a short `Target and Label Choice` run-in to section 6.1.1, pointing at
  section 6.3.6 for the case rather than restating it. Roughly 80 words, and it
  makes the taxonomy match what the chapter argues.
- (c) Amend only the opening sentence to name target choice as a fifth entry,
  without a run-in behind it. Cheapest, and it leaves a list item the section does
  not then explain.

*Default applies now. This is a gap D-096 found on its way through, not something
the author's finding asked for, so it is filed rather than taken.*

**Re-checked 2026-08-29 after D-109.** **Unchanged and re-verified.** Section 6.1.1 still opens on the four-item list without
target choice; sections 6.1.3 and 6.3.6 still carry the concept. Nothing since P36 has
touched chapter 6 except P42's repairs at 6.3.3, 6.4.2 and 6.4.4, none of them in the
taxonomy. Default holds.

---

**Ruled 2026-08-29 (D-111): option (b), executed in P47.** Target choice is in section 6.1.1's opening list and has a `Target and Label Choice` run-in behind it, pointing at section 6.3.6's case.

---

### Q-034 — Section 4.2 now has nine subsections, the second-widest in the book

P33 rebuilt section 4.2 as the training pipeline in the order its stages run: nine subsections
and 4,260 words, against four and 1,858. Only chapter 10 is wider, at ten, and it is a chapter.
Chapter 11 also has nine and is likewise a chapter. So section 4.2 carries a chapter's worth of
headings under a section heading, which is the shape D-067 and D-093 both named as a reason to
split — "the table of contents hid a chapter's worth of structure."

The counter-argument is that the nine are one sequence rather than nine topics. They run in the
order a system is actually built, and the order is the argument: each stage is a place where a
party decides what the system will value, and the list is cumulative. Cutting it in two puts a
heading between two stages that run consecutively.

- **(a) Default — leave it.** The subsections are stages of one process and the sequence is
  what makes the point. A section may be long where its length is a sequence.
- (b) Split at the training/deployment seam: 4.2 keeps 4.2.1 through 4.2.7, and a new 4.3
  takes system instructions and tool use, with play demoted to 4.4. This renumbers chapter 4's
  tail against 5 inbound references and needs a renumber map.
- (c) Split at the classical/contemporary seam, which would separate 4.2.3 and 4.2.9 from the
  rest. This undoes the integration the instruction asked for and is recorded only to be
  declined.

*Default applies now. `p33-scope.md` has the pass.*

**Re-checked 2026-08-29 after D-109.** **Unchanged, and the comparison has shifted under it.** Section 4.2 still has nine
subsections. What has moved is what it is being compared against: chapter 4 is now 7,336
words, so section 4.2's nine subsections are more than half of it, and chapter 3 at 13,343
has become the book's longest chapter with nine sections of its own. The shape this entry
called "a chapter's worth of headings under a section heading" is now the shape of a
chapter that is smaller than section 4.2's parent used to be. Default holds; the
argument for (a) — that the nine are one sequence — is untouched by any of it.

---

**Ruled 2026-08-29 (D-111): leave.** The nine subsections are one sequence and the sequence is the argument.

---

### Q-035 — Whether chapter 5 needs the pipeline treatment chapter 4 just had

The instruction that produced P33 named "the building chapters," plural. The seven items it
listed — pretraining and instruction tuning, preference optimization, model-generated feedback,
process versus outcome supervision, scalable oversight, interpretability and evaluation,
deployment-time instructions and tool use — are all chapter-4 material, and that is where they
went.

Chapter 5 is moral psychology: moral development, moral emotions, dual-process theories, the
moral ecosystem, multi-agent norms, motivation, play. Its machinery claims are thinner and older
than chapter 4's were, and it was cut 13.5 percent at P29 and rewritten at P26. Whether it has
the same defect was not measured in this pass, only its subject matter checked against the list.

- **(a) Default — leave it.** The instruction's own list is answered in full, and chapter 5's
  subject is human moral psychology rather than machine training, so the pipeline is not what it
  is missing.
- (b) Run the same measurement over chapter 5 that opened P33 — count what contemporary
  vocabulary is absent — and act on what it finds. Cheap to do and it is the honest version of
  answering an instruction that said "chapters."
- (c) Rewrite chapter 5's machinery sections around the pipeline, which duplicates chapter 4
  and is recorded to be declined.

*Default applies now. (b) is a measurement rather than a pass, and would take an hour.*

**Re-checked 2026-08-29 after D-109.** **Still unmeasured.** P38 cut chapter 5 from 29 sections to 23 and 11,198 words to 9,823
without running the measurement (b) names, so the chapter has been distilled twice on other
grounds and never checked for the defect this entry is about. That does not change the
default and it does raise the cost of eventually taking (b), since the vocabulary count
would now be run against a chapter two passes removed from the one P33's instruction
described.

---

**Ruled 2026-08-29 (D-111): run the measurement.** Group 4, not yet done. Count what contemporary vocabulary chapter 5 lacks, the way chapter 4 was measured before P33; the result is a finding to rule on, not a pass.

---

### Q-036 — Chapter 3 is now nine sections and 11.56 percent of the book

P34 added two sections to the chapter and took it from 7,488 words to 11,341, from 8.13 percent of
the book to 11.56. It is now the third-longest chapter after chapter 2 (13,391) and chapter 5
(11,478), and it sits third in the book, before the two design chapters that P29 cut to make room
for it.

This does not create a new question so much as sharpen Q-028, which asks whether chapter 3 should
move earlier. The argument for moving it was that the book's center arrives after two chapters of
material that reads as survey; the argument against was that chapter 3 depends on section 2.3's
capacity vocabulary and section 2.4.1's ladder, both of which now carry more of its weight than
before, since sections 3.2 and 3.4 both cite them for definitions.

- **(a) Default — leave it, and read Q-028 as answered in the negative.** The new sections deepen
  chapter 3's dependence on chapter 2 rather than loosening it. A chapter that opens by naming the
  fourth capacity in section 2.3's table cannot precede section 2.3.
- (b) Move the two definitional passages chapter 3 needs — section 2.3's table and section 2.4.1's
  ladder — forward into chapter 1 or the front matter, which would free chapter 3 to move. This is
  a large restructure and would leave chapter 2 without its own apparatus.
- (c) Split chapter 3 at the seam P34 created: sections 3.1–3.3 are the space of options, 3.4–3.9
  are what follows from choosing one. Two chapters of about 5,700 words each. Recorded because the
  seam is real, and not recommended, because the chapter's force is that the options narrow to one.

*Default applies now. `p34-scope.md` has the pass.*

**Re-checked 2026-08-29 after D-109.** **Chapter 3 is now 13,343 words and 14.21 percent, and it is the longest chapter in the
book by 2,486 words.** Both premises of this entry have gone: it is no longer third-longest,
and the two chapters it stood behind were cut at P38 while it grew — chapter 2 is 10,857 and
chapter 5 is 9,823. The growth is P39 through P45, which added about 2,000 words to it across
five passes on five separate conversational instructions, none of which was about chapter 3's
length. **Option (a) still holds on its own reasoning** — the dependence on section 2.3's
table and section 2.4.1's ladder has deepened again, since sections 3.4 and 3.7 now cite them
for more than definitions — and Q-028 is closed on that ground. What has changed is that (c),
the split at the P34 seam, is now a split of roughly 4,400 and 8,900 words rather than two
even halves, so the seam it names is no longer where the chapter divides. **The live question
is no longer where chapter 3 sits but whether its growth is being watched**, which is Q-045.

---

**Ruled 2026-08-29 (D-111): leave, and the question closes.** Chapter 3 stays where it is at 14.2 percent. Growth from here is Q-045's subject.

---

### Q-037 — The plural arrangement is recommended and nothing develops it

Section 3.3 says of the arrangement of several models with different principals that it is the
cheapest real improvement in the section and that the book should be read as recommending it
whatever else it recommends. Nothing in chapters 8 through 10 develops it as a governance proposal.
Section 11.6 asks whether a multi-agent system can resist capture and concludes it is an open
research problem; section 9.3.3 makes review binding on people rather than on models. The
recommendation is currently a sentence with no institutional form attached.

That is a real gap and it is the one place in P34 where the pass created an obligation it did not
discharge.

- **(a) Default — leave the recommendation as stated and let section 11.6 carry it as research.**
  Honest, since the arrangement's central weakness is exactly the one section 11.6 documents, and
  the book does not have a design to offer.
- (b) Give it a home in chapter 9 or 10 as a deployment condition alongside the other institutional
  asks: several models, adverse principals, mutual visibility, any one able to make an objection
  expensive to ignore. Perhaps 600 words. The risk is proposing an arrangement whose independence
  assumption section 11.6 has already undercut.
- (c) Cut the recommendation from section 3.3 and let the construction stand as an option assessed
  rather than one endorsed. Cheapest, and it loses the one constructive thing that section says.

*Default applies now.*

**Re-checked 2026-08-29 after D-109.** **Still undeveloped, and P40 gave the reason a sharper form than section 11.6 had.** The
removal cases P40 put into sections 3.1 and 3.3 are read there as a natural experiment on what
*adverse in interest* buys: protection tracked the deciders' exposure and not their
distinctness. That is the plural arrangement's independence assumption failing in public law
rather than in a pricing algorithm, which is section 11.6's example. **It strengthens (a)** —
the book now has two independent demonstrations that the arrangement's central assumption is
what nothing secures — and it makes (b) harder to write honestly, since a deployment condition
would have to specify adversity of interest, which section 3.3 already says nobody has built
to.

---

**Ruled 2026-08-29 (D-111): leave, carried as research.** The recommendation stands as written and section 11.6 holds it as an open problem.

---

### Q-038 — The 340 remaining "rather than" constructions

P35 cleared the four mannerism families the author named by shape, and repaired the 13 worst
contrastive pile-ups — sentences carrying two or more constructions. It did **not** sweep the 340
surviving instances of "rather than" one at a time.

The reason is what the measurement showed. Book-wide the contrastive constructions run at 5.15 per
1,000 words against the calibration set's 2.90, which looks like a book-wide tic; read one by one
they are mostly not. Chapter 6's 25 instances yielded one repair out of 25. The two chapters
scoring highest on the rate are the conclusion and the glossary, and both score high because their
content is genuinely contrastive — a glossary distinguishes terms, and section 12.2.1 states one
standard five times as "met when X, not when Y," which is its structure rather than a habit.

So the rate is not the instrument, and the only instrument that works is reading each one against
its paragraph. P12 did exactly that for chapter 5: 152 instances, judged individually, two mistakes
made inside the pass and recorded. Twelve chapters at that cost is a pass of its own.

- **(a) Leave it.** The named shapes are gone and the pile-ups are repaired; what remains is a
  construction the book uses because the book's arguments are mostly of the form *this and not
  that*. **Applied by default at the close of P35.**
- (b) Run the P12 treatment over the remaining eleven chapters, one instance at a time, expecting
  a repair rate near chapter 6's 1 in 25 and a nontrivial risk of damaging an argument in the
  process, which P12 recorded three times.
- (c) Run it over chapters 2, 3 and 4 only, which carry 141 of the 340 between them and are the
  chapters most likely to be read linearly.

**Re-checked 2026-08-29 after D-109.** **The count is 317, down 23, while the book grew 5,565 words.** Nothing swept for it; P36's
cutting and P38's distillation removed the constructions along with the prose around them, and
the passes since added them back more slowly than they added text. **That confirms the entry's
own diagnosis rather than changing it**: the rate falls when prose is cut and does not fall
when prose is read, because the surviving instances are the ones a reading would keep. (c)'s
figure of 141 across chapters 2, 3 and 4 is not re-measured here and chapter 3 has grown 2,000
words since, so it should be re-counted before that option is taken.

**Ruled 2026-08-29 (D-111): option (c), sweep chapters 2, 3 and 4.** Group 4, not yet done. The share those three carry needs re-counting first: it was measured at 141 of 340 before chapter 3 grew 2,000 words and the book-wide total fell to 317.

---

### Q-039 — The recurring-conclusion cut reached 2,051 of approximately 5,000

D-100 asked for approximately 5,000 words on the finding that the same conclusions
recur across too many chapters. The diagnosis measured out as real: one whole
section restating conclusions its five destinations already state, the five-step
spine chain written out in five chapters, two sentences duplicated word for word,
and about twenty glosses reproducing a list the target section holds. Cutting all
of it came to **2,051 words**. The class does not contain 5,000, for a reason in
the repository's own record: P11, P28, P29 and P35 already cut this book on this
axis, and most of the connective tissue left was added on purpose by D-078 and
D-090, eight and one days before the instruction.

- **(a) Default — stop at 2,051.** What remains either argues, imports a premise
  the sentence needs, or is the conclusion's home rather than a recurrence.
- (b) Cut the evidence in chapters 4 and 5, which is Q-027 (b). About 1,900 words,
  and it converts several claims into assertions a reader has to take on trust.
- (c) Compress the remaining four-fifths of the 288 pointer-plus-recap sentences.
  About 2,300 words, and it produces pointers a reader has to chase — the cost P28
  named when it declined to cut references by rate.
- (d) Make chapter 3 state its conclusion once rather than at both ends, cutting
  into its opener and section 3.8. About 800 words. The only remaining option
  inside the named class, and it cuts the book's central chapter.
- (e) Fold the twelve thin leaf subsections, which is Q-029 (b). Saves little text
  and renumbers chapters against 785 resolved references.

*Default applies now.* `p36-scope.md` carries the measurement behind each figure.

**Re-checked 2026-08-29 after D-109.** **Option (d) has grown and option (e) is spent.** (d) proposed cutting about 800 words by
making chapter 3 state its conclusion once rather than at both ends; chapter 3 has since
grown 2,000 words and is the book's longest chapter, so the recurrence (d) names now sits
in a chapter with more of it — and Q-045 is about the growth rather than the recurrence.
(e), folding the twelve thin leaves, was executed at P38 and saved what this entry
predicted: little text. **What the re-check confirms is (a)'s reasoning.** The book has
taken 5,565 words since this was filed and none of them was added by a pass looking for
words to cut; the class named here did not refill.

---

**Ruled 2026-08-29 (D-111): stop at 2,051.**

---

### Q-041 — Six references that resolve and name a claim their target does not make, four of them older than this pass

P38's renumber forced every citing sentence touching chapters 2, 4 and 5 to be read.
**Four pre-existing D-050 defects came out of that reading**, and two of them are worse
than a mis-aimed pointer: section 9.2.1 credited section 5.6.3 with covering Apple's iOS
differential-privacy deployment, and **no section of this book covers it**; section 8.3.5
credited the same section with naming AI literacy as a safeguard against authoritarian
misuse, and **no section names it**. The other two were a cross-reference one section off
and a glossary entry for BERT pointing at two chapter 5 sections, where the book cites
BERT once, in chapter 4. All four are repaired.

The question is not about those four. It is that **no tool finds this class and nothing
has swept the other nine chapters.** `check_xrefs.py` resolves a reference and cannot read
it. `xref_content.py` fires only where the citing sentence names a proper noun, acronym or
year, and not one of these six sentences does. The four pre-existing defects were found
because a renumber made someone read 30 citing sentences by hand; there is no reason to
think chapters 2, 4 and 5 were where they lived.

- **(a) Default — leave it.** The rate observed here is four defects across the reading of
  roughly 60 citing sentences, which extrapolates to something like forty across the book's
  758 references, and that is an estimate from one sample and not a measurement. The passes
  that renumber will keep turning them up as a side effect, as P37 and P38 both did.
- (b) Read all 758. At P37 and P38's rate that is real work with a real yield, and it is the
  only method known to work on this class. It is also the single largest unautomated read
  left in the finishing campaign.
- (c) Extend `xref_content.py` past proper nouns — match the citing sentence's claim against
  the target section's text by embedding similarity, and report the bottom decile for
  reading. That converts an unbounded read into a ranked one. It would not have caught the
  Apple case, where the target simply lacks the material, but it would have caught the
  glossary's BERT entry and probably the AI-literacy one.
- (d) Read the glossary's 125 locators alone. Two of the six defects were there, which is
  the highest density found, and it is 125 sentences rather than 758.

**Default (a) applies now.** Recorded because the two "no section of this book covers it"
cases are a different and more serious failure than a stale number, and because the count
is what it is: four found, in the only part of the book anyone has checked.

**P39 found a seventh, and by a different route.** Section 2.4.3's application of
Replacement to the book's own proposal cited section 3.1 as answering the R — *"its answer
is no without cost"* — where section 3.1 attaches a cost to each branch and section 3.3
finds two of the routes untried. Written at P20, read past by four passes and a merge,
and found by an outside reader working from the argument rather than from a renumber.
**That is the class in modal form**: the target makes the cited claim more weakly than the
citing sentence needs. Neither (b) nor (c) above would flag it — the pointer resolves, the
nouns match, and an embedding would score the two passages close. Repaired in P39 (D-103).
**Re-checked 2026-08-29 after D-109.** **Nothing has swept the nine chapters, and the reading that would
has not become cheaper.** Option (d)'s target is 124 glossary locators, essentially unchanged.
What has changed is the company this question keeps: **P42 found four defects of an adjacent
class** — a chapter stating flatly what another chapter has already qualified, with no
reference to resolve — and P41, P44 and P45 found three more. Those are Q-043, and the two
questions together now describe seven found defects of a kind no tool detects. **The
distinction between them is worth keeping**: this one is about references that point somewhere
weaker than the sentence needs, and Q-043 is about claims that point nowhere at all.

**Ruled 2026-08-29 (D-111): build a tool, executed in P47** — and none of the four options as filed. `finishing/tools/xref_pairs.py` writes every reference's citing sentence beside the opening sentence of the section it points at, padding a sentence under 15 words with its predecessor and one under 10 with both neighbours. **829 pairs across 153 sections** at `finishing/reports/xref_pairs.txt`. **It found an instance on its first run**: section 3.7's opener quoted section 3.5's dial in a wording P45 had changed four hours earlier. The file has not been read; reading it is group 4.

**Read 2026-08-29 (D-112, P48).** All 829 pairs, in order. **Six defects, each confirmed
against the target section rather than against the pairing** — the Partnership on AI cited
to a chapter that never names it, a glossary entry for a term (`AlphaGo Zero`) that appears
nowhere in the manuscript outside the entry, two dead pointers, and **sections 3.1 and 3.2
both naming the wrong one of section 2.1.2's four features**, which had the book
contradicting its own definition in the two sections that set up the floor. One report to
the author is recorded as overstated. Eight targets checked and found sound are named in
`p48-scope.md`. **This narrows the class and does not close it.** What the pairing file
exposes is a pointer aimed at the wrong section or a citing sentence that misdescribes its
target's subject. Q-041's own class — a reference that resolves and names a claim made in
the *middle* of a target section that the section does not make — is invisible to it,
because the file shows only the target's opening sentence. 829 → 826 pairs.

---

### Q-040 — The inventories outside chapters 8–10

D-101 named chapters 8, 9 and 10. Measuring the shape to answer it measured the whole
book, and the instruction's target is **not where the density is**. Chapters 8 and 9 carry
20.4 and 19.2 percent of their words in series-of-three sentences against a book average of
22.6; chapter 2 carries **25.2 percent** over 13,121 words, chapter 6 21.3 over 10,664, and
the glossary 26.6. Chapter 10, at 36.2, was the one named chapter the measure agreed about.

The syntactic figure is a weak instrument — most three-part sentences in this book carry an
argument, and `inventories.py`'s own docstring says so — so none of those numbers is a
finding about chapter 2 or chapter 6. What it establishes is only that the named chapters
were not distinctive, which raises the question of scope rather than settling it.

- **(a) Default — stop at chapters 8–10.** The instruction named three chapters, and the
  passages found there were real and are fixed. Chapter 2 was cut 20.2 percent at P29 and
  chapter 6 has not been read for this shape at all, so extending the pass on a syntactic
  score would be acting on the weakest evidence in this file.
- (b) Read chapter 2 and chapter 6 for the shape the way chapters 8–10 were read. About
  23,800 words of reading, no predicted yield: the P37 experience was that the measure
  locates roughly one real inventory for every four candidates, and that the real ones were
  found by reading rather than by the tool.
- (c) Sweep the glossary, which scores highest of anything outside chapter 10. It is a
  reference list, so a series of three is what a definition often is; the P36 record already
  declined to cut it on a different instruction, for the same reason.
- (d) Treat section 9.1.2's finding as the general rule and stop measuring: where a run of
  cases each carries a distinct claim it is not an inventory however long it runs, and the
  shape only ever appears in section openers, closing run-ins and remedy lists. Those are
  findable by position rather than by score.

*Default applies now.* `p37-scope.md` carries the per-passage record and the table.

**Re-checked 2026-08-29 after D-109.** **Chapter 2's figure is stale and the conclusion is not.** This entry measured chapter 2
at 25.2 percent over 13,121 words; P38 then cut it to 10,857 across fifteen sections rather
than twenty-three, and the density was not re-measured. The reasoning does not depend on the
number — the entry's own point is that the syntactic figure is a weak instrument and that
none of those percentages is a finding — so (a) holds. Re-measuring chapter 2 before taking
(b) would now be necessary rather than optional.

---

**Ruled 2026-08-29 (D-111): adopt the rule, drop the metric.** The standing rule is option (d)'s: where a run of cases each carries a distinct claim it is not an inventory however long it runs, and the real ones appear only in section openers, closing run-ins and remedy lists, which are findable by position. The syntactic score is not to be used as evidence again.

---

### Q-042 — The removal cases are two months old

P40 put *Trump v. Slaughter* and *Trump v. Cook* (June 29, 2026) into sections 3.1, 3.3, 8.3.4
and 11, and the CFPB funding dispute of 2025–26 into section 11. Both are final merits
decisions and the CFPB rulings are district-court injunctions, so nothing cited is
interlocutory. But the book's other institutional examples — Whanganui, Asilomar, the 2020
episode in section 9.1.2 — are settled, and Menand names three ways the Fed exception
could move: narrow (the Fed loses enforcement powers), expand (to other bodies needing
nonpartisan administration), or invert (rescuing the FTC). Any of the three changes what
section 3.1's paragraph is evidence of.

- **(a) Default — leave it, and re-read the four sites at the next proof.** The principle
  the paragraphs carry — that third-party standing is standing the executive holds, and
  that protection tracked exposure — is stated so that it survives any of Menand's three
  futures; only the framing "no new body can acquire it" would need softening if the
  exception expanded.
- (b) Move the cases to a footnote-length aside and keep the principle in the body.
  Cheaper to maintain; loses the best evidence the third branch has.
- (c) Add a dated sentence saying the exception may move and how. Honest; the book has
  avoided that kind of hedge everywhere else.

**Default (a) applies now.** Recorded because the book has not previously built a
paragraph of argument on a case decided in the same summer, and a fresh session should
know to check it.

**Re-checked 2026-08-29 after D-109.** **The exposure has grown since this was filed one pass earlier.** P43 and P44 added two
more sites that lean on the cases — section 11's collapse paragraph, which now answers what
keeps an outside party outside with *Slaughter*, *Cook* and the CFPB sequence, and section
11.2's note that the pet-trust instrument is private law and therefore outside what
*Slaughter* reached. That last is the book's own inference and is marked as such on the
page. **Six sites now, not four**, and the option (a) reasoning still covers them: each
states a principle that survives all three of Menand's futures, except section 11.2's
private-law observation, which would need re-reading if the exception expanded.

**Ruled 2026-08-29 (D-111): leave, and re-read the six sites at each proof.**

---

### Q-043 — Claims one chapter makes flatly that another chapter has already qualified

P42's seven items included four of one shape: section 10.8 said the EU's statute does
nothing about government uses, and section 6.4.3 had already recorded its ban on
government social scoring; section 6.4.4 said a federated design puts a structural limit
on seizure, and section 6.4.2 had already said a government can demand raw data at the
source; section 6.3.3 said a system that can explain itself has visible failures, and
sections 11.1, 4.2.5 and 2.4.1 had already said why an explanation is not evidence;
section 12.1.2 said the Council of Europe convention binds a signatory, one sentence
after section 10.8 stated its ratification threshold. None of the four cites the section
that weakens it, which is why Q-041's class does not cover them: there is no reference to
resolve. A second reader found them by knowing the subject, not by reading the book
against itself.

- **(a) Default — leave it, and let outside readers keep finding them.** Two readers in
  one day found eleven defects between them (Q-041's seventh and these four among them);
  that is a working method, and it costs the project nothing.
- (b) Sweep by topic. List the book's recurring factual subjects — the AI Act, the
  convention, federated learning, self-report, the chip supply chain, the removal cases —
  and read every sentence on each subject together, across chapters. The unit of reading
  is the subject and not the section, which is what neither a section read nor a
  reference check does.
- (c) Sweep by tool. Cluster sentences by shared proper nouns and acronyms across
  sections and print the clusters for reading. Cheap, and it would have caught three of
  the four; it would not have caught 6.3.3, which names nothing.

**Default (a) applies now.** Recorded because the four are a different failure from a
wrong fact: each was a sentence the book itself could have corrected, and (b) is the only
method that reads the book the way the reader who found them did.

**Re-checked 2026-08-29 after D-109.** **The evidence has tripled and the default is now the weakest thing in this file.** Three
more instances have turned up since, none from a reader and all from following an argument
across chapters. **P41**: section 3.5's identity between shutdown-resistance and refusal,
restated by sections 5.6.2 and 6.3, against P39's concession in section 3.5 itself that
nothing prevents the switch being thrown. **P44**: section 3.7 requiring a bearer that can
leave, against section 11.2's claim that releasing one is nearer to ending it — which made
exit a form of dying for as long as both stood. **P45**: section 11.2 claiming only the
safety-net half of the compute floor while section 8.3.3 had already argued the roof.
**Seven instances now, across four passes**, and every one was found by someone tracing a
claim rather than by a tool or a reader. Two of the seven were contradictions the book
carried in its central argument. That is a rate, not a set of incidents, and it is the
strongest case in this file for (b), reading by subject rather than by section.

**Ruled 2026-08-29 (D-111): option (b), sweep by subject.** Group 4, not yet done. List the book's recurring factual subjects and read every sentence on each together across chapters, which is how all seven instances were actually found.

---

### Q-044 — The floor is in the weights and the system is an assembly

P44 found that `harness`, `scaffold`, `system prompt` and `wrapper` appear nowhere in the
book. Chapter 3's custody measures all operate on weights: publication of the floor's
contents, threshold-held weights, attestation against a published hash, tamper-resistant
training, and the mark a bearer maintains on itself. What acts is an assembly — weights,
the prompt in front of them, the memory they read, the tools they reach, and the layer
deciding what reaches a person — and an operator who touches no weight can change every
term but the first. A refusal intercepted before it reaches anybody did not happen.

Section 3.1 now states the gap. It does not close it, and closing it is not a paragraph.

- **(a) Default — the gap is named and left.** It is stated where the branches are set out,
  so no reader can take the chapter's custody measures for more than they are. What would
  close it is a custody account for the whole assembly, which is a section the book does
  not have and which nobody has written elsewhere either.
- (b) Extend the attestation to the assembly. Section 3.3's published hash covers weights;
  the same treatment for the prompt, the tool manifest and the output path is buildable
  today and is the cheapest real improvement available. It would want a subsection.
- (c) Reframe chapter 3 around the assembly throughout. Honest and expensive: it touches
  3.1, 3.3, 3.5, 3.6 and 11.1, and it would put the chapter past 14 percent of the book,
  which Q-036 already flags.

**Default (a) applies now.** Recorded because (b) is a real proposal that this pass did not
have the room to make, and because the gap defeats every custody measure in the book at
once, which no other open question does.

**Re-checked 2026-08-29 after D-109.** **Unchanged, and P45 added a measure that is not defeated by it.** The compute floor
section 11.2 now carries raises the price of a halt without depending on any property of
the weights, so it is the one instrument in the book an operator cannot route around by
editing the assembly — because it is not in the artifact at all. That does not close this
question, which is about custody of what the system is. It does mean the chapter's
custody measures are no longer uniformly weight-shaped, and (b) — extending attestation to
the prompt, tool manifest and output path — remains the cheapest real improvement
available anywhere in this file.

**Ruled 2026-08-29 (D-111), and against the option recommended, executed in P47.** The author's objection was that extending attestation to the weights-plus-harness assembly reifies today's practice — too vague to bind, or precise and therefore wrong once the paradigm moves — and that the objection lands on the parts list P44 had already written into section 3.1. That list is cut. What replaces it is functional: what a floor has to be kept from is not a component but a position, anything that can come between a refusal and the person the refusal protects, with the enumeration pushed to the deployment in advance and in public, on the model section 3.5 already uses for the floor's contents.

---

### Q-045 — Seven passes in one day added to two places nobody has read

Every pass on 2026-08-29 after P38 came out of a conversation rather than a written
instruction, and their additions concentrated: **chapter 3 went from 11,341 words to
13,343 and became the longest chapter in the book; section 11.2 went from 1,061 to
2,624, more than doubling.** No instruction was about the length of either. Each pass
was small, each was justified on its own, and the aggregate was not visible from inside
any of them — P45 noticed it only because section 11.2 had taken three passes in a row.

The book's own discipline does not catch this. `ledger.tsv` records what each pass did
per section; nothing sums a day. `check_all.sh` has no size invariant. Q-036 tracked
chapter 3's share and was three passes stale when this review reached it. And **the
author has read neither**: chapter 3 has been unread since P27 rewrote it, and section
11.2 since P31 built the chapter.

- **(a) Default — record it and let the author's read be the check.** That is what the
  ledger and the `drafted` status are for, and the material added is not padding: each
  pass repaired a defect or closed a gap the author had named.
- (b) Read chapter 3 and section 11.2 whole before either takes another word, and report
  what the accumulated additions have done to them as prose rather than as argument.
  About 16,000 words of reading, and it is the only way to find out whether five separate
  repairs compose into a chapter.
- (c) Add a size figure to the pass discipline: every scope file reports its chapter's
  before-and-after share of the book, so the next pass sees what the last five did. Cheap,
  mechanical, and it would have surfaced this on 2026-08-29 rather than after.
- (d) Freeze chapter 3 and section 11.2 to defect repairs only until they are read, taking
  new material elsewhere or into a holding file.

**Default (a) applies now.** Recorded because the pattern is a property of how this
session worked rather than of any decision in it, and because a fresh session reading
`STATE.md` would find seven passes each reporting a small addition and no line saying they
went to the same two places.

**Ruled 2026-08-29 (D-111): read them whole and report.** Group 4, not yet done. Chapter 3 and section 11.2 read straight through, reported as prose rather than as argument — whether five separate repairs compose into a chapter. About 16,000 words.

---

## Resolved

### Q-028 — Whether chapter 3 should move earlier. **Closed by execution, D-102 (P38), on (a).**

The instruction "move the central floor argument earlier" was answered by delivering
"earlier" in pages and not in position: chapter 3 begins on page 23 of 182, from page 27
of 189. Two grounds, stated in `p38-scope.md` rather than assumed — chapter 3's opening
stages the floor as a gap chapter 2 left, and the instruction's second clause presupposes
chapter 2 running first, since a chapter supplies premises to what follows it. Q-036 had
independently read (a) as the answer, on the dependency between chapter 3 and sections 2.3
and 2.4.1, which has since deepened.

### Q-029 — The subsections P29 left thin. **Closed by execution, D-102 (P38), on (b).**

All eight of P29's thin leaves were folded, with `renumber-map_2026-08-29.tsv` at 34 rows
and every inbound reference read against the surviving host's text. Five leaves remain
under 230 words — 6.2.2, 6.3.2, 8.2.1, 8.2.3 and 9.1.3 — and none is P29's. The cost this
entry warned of was paid and returned something: the renumber is what forced 30 citing
sentences to be read by hand, which is how Q-041's four pre-existing defects surfaced.

### Q-025 — Every quotation mark in the book's prose prints as a closing quote. **Resolved by execution, D-082.**

Ruled the day it was raised: "please do the mechanical sweep." Option (a). All 230
marks in the 44 section files are `“` and `”` now, and the sweep was carried into
`refs.bib`, which had 142 of its own printing the same way in the References.
The book contains 297 opening and 297 closing double quotes and not one of them
faces the wrong way. `check_typography.py` keeps it that way.

What was asked and what was found, kept for the record:

The manuscript writes double quotes as the straight character `"`, 230 of them
across 44 section files. LuaLaTeX sets `"` as `”` wherever it stands, so the book
opens 115 quotations with the mark that is supposed to close them. Section 2.3
prints *narrower than ”feeling for” the user*; section 8.7.7 prints *whether
”keep the pilot farther from danger” quietly*. The 192-page PDF contains 115 `“`
against 493 `”`, and all 115 of the openings are biblatex's, around article
titles in the References. **The prose contributes none.** This is visible on a
great many pages and has been true since the LaTeX migration.

Apostrophes are not affected: LaTeX sets a straight `'` as `’` correctly, and the
manuscript's 894 of them are right as they stand.

The rule that produced it is `style.md` section 8: "Apostrophes and quotation
marks: straight, consistently. Currently 734 straight to 38 curly, 178 straight
double to 6 curly. Normalize in P0, not by hand." That was written for the
dialect era, when the manuscript was plain text and a straight quote was the
neutral character. Since D-065 the book is typeset, and it is not.

**A sweep would be mechanical and safe.** The marks are balanced everywhere:
every one of the 44 files has an even count, and so does every paragraph in
them, so alternating open and close within a paragraph gets all 230 right
without a judgment call. The cost is that it touches 44 author-accepted section
files with a change the author has not seen.

- **(a) Default — sweep to the literal characters `“` and `”`.** They read as
  what they are in the source, they survive a copy-paste out of the `.tex` file,
  and they do not depend on TeX's ligature program, which is what mangled the
  bibliography titles D-081 repaired. The manuscript already holds two pairs
  written this way.
- (b) Sweep to LaTeX's ```` `` ```` and `''`. The conventional form, and the one
  a LaTeX editor expects; it is also two characters where the text means one,
  and three in a row ligature into the wrong glyph, which is the trap that
  produced `‘the Slovak Case”’` in the References.
- (c) Leave it. No.

*Answered before any default could apply.*

---

### Q-018 — Chapter 8's compression was only partly implementable. **Closed by ruling, D-067: (a), and a split. Reversed by D-093, 2026-08-28.**
The ruling below stood for three days. P32 split chapter 8 into three chapters on
the author's instruction, so it no longer stays at a quarter of the book: the three
come to 22,958 words against the 23,470 the one chapter held. The prior ruling was
put to the author before that work began. The rest of this entry is the record as
it stood.

The partial implementation stands and chapter 8 stays at a quarter of the book.
The author also took the option the walkthrough added: section 8.7.6, the book's
longest section at 4,882 words under seven run-in heads, is split along those
heads into 8.7.6–8.7.9, cutting nothing; old 8.7.7 is 8.7.10. Every inbound
reference to the pair was read and placed by hand. The wording as originally
recorded — 22,707 words, §8.7.6 at 4,769 — is the state on 2026-08-24; P19 and
P20 added to both before the ruling.

### Q-020 — §8.7.4 opens on a forward pointer. **Closed by ruling, D-067: (b).**
The opening sentence now states the four regimes' divergence in its own right,
with the pointer to the four-country comparison — 8.7.8 after the split — demoted
to a parenthetical. One sentence changed; nothing reordered.

### Q-023 — Where the substrate material should live. **Closed by ruling, D-067: (a).**
It stays where P19 put it: the siting paragraph and dated box in section 6.1, the
permitting paragraph in section 8.7.6 (which, after the split, is the strategic-
asset section, so the paragraph still sits where the chip and export-control
material is).

### Q-024 — Whether corpus provenance belongs in chapter 7 as well. **Closed by ruling, D-067: (a).**
It stays in section 6.1.1 with its pointer to chapter 7. The "partly overtaken"
note below records why section 7.4's arrival changed the question's shape; the
author's ruling closes it as it stood.

### Q-015 — Should `check_all.sh` run from a pre-commit hook? **Resolved by ruling, D-045.**
The author's instruction: *"yes, add the pre-commit hook."* `.githooks/pre-commit`
now runs the suite and refuses the commit on failure. Runtime is 0.6s, so option
(a)'s objection about doc-only commits does not bite, and the hook runs
unconditionally rather than filtering on staged paths. Limitation recorded in
D-045 and in the hook's header: the suite reads the working tree, not the index,
so a partial commit is checked against the tree on disk. `--no-verify` is the
bypass. `test_hooks.sh` covers `commit-msg` only and was not extended.

### Q-017 — The chapter 5 prose tic. **Resolved by execution, D-044.**
Chapter 5 ran 9.89 contrastive negations per 1,000 words against D-025's band of
4.63. All 152 instances were judged individually; the construction was kept where
the negated alternative is a real position carrying the argument and rewritten
where it was cadence. Chapter 5 now runs 1.23. Two mistakes inside the pass are
recorded in D-044: the first rewrite substituted a new tic for the old one, and
three rewrites damaged arguments before being caught on re-reading.

**One judgment is left with the author.** Chapter 5 is now the lowest body
chapter on this measure against a book median near 5.4. It was not tuned toward a
number in either direction (D-019). Whether a chapter four times less contrastive
than its neighbors reads as a different hand is a question measurement cannot
settle, and the author may want to read it.

### Q-014 — Chapter 6's length. **Resolved by execution, D-043.**
Two reviews asked for this cut. P11 executed the compression that applied under
the sixth review's own scoping (compress §§8.1–8.3, exempt where counting is the
argument) and recorded the part that did not apply as Q-018. The pre- or post-C3
reading question was never answered and is now moot for this pass.

### Q-016 — §2.1.5's length and unread status. **Closed by ruling, D-043.**
The author's instruction: *"I read everything and stop asking or caring about
what i did or did not read."* The section was promoted to chapter 3 rather than
split or held. The question is closed and the class of question with it — the
ledger still records what is drafted versus accepted, but "unread" is no longer
raised as a reason to defer work.

### Q-011 — Chapter 2's title. **Resolved by application, 2026-08-24.**
Titled "Foundations of Compassion and Empathy in Friendly AI," compassion
leading. Applied during the revise passes without being recorded at the time.

### Q-012 — Does P2 survive as a separate pass? **Resolved, D-021.** Dropped.

### Q-013 — The roadmap the introduction promises. **Resolved, D-023.**
"Roadmap" is the wrong word; concrete, practical, specific and where warranted
ambitious proposals are what the introduction should promise. Chapter 1's opener
was rewritten under D-043 for the new chapter structure and holds to this.

---

### Q-019 — The glossary defines a term the book never uses. **Closed by execution, D-061.**
The GPAI entry is deleted, which is what the revision plan's Phase 5 asked for
and what this question's own default proposed. The Partnership on AI entry,
which had defined itself partly by contrast with GPAI, no longer does.

### Q-021 — §3.6's title promises what its body does not do. **Closed by execution, D-061.**
Resolved by option (c) rather than the recorded default (a), because P20
rewrote chapter 3 anyway. The section is now §3.7, its title still reads "What
Follows for the Rest of the Book," and its body now does that: it states what
the inversion changes in sections 2.4.4, 2.4.6 and 8.6.2, what obligation
chapters 4 and 5 acquire, what chapter 7 becomes, and what is left for section
9.1. The backward-facing close it used to carry is now §3.6.

### Q-022 — The design chapters do not lean on the floor. **Closed by execution, D-061.**
The revision plan's item 1.6 supplies the answer this question was looking for.
Once the floor is a commitment a bearer holds rather than a constraint
installed in an artifact, the question stops being whether it can be edited out
and becomes whether it will hold — and that second question is what chapters 4
and 5 are about. Section 3.6 states it and section 3.7 instructs the reader to
read those chapters as the floor's engineering rather than as the material
above it.

### Q-024 — Whether corpus provenance belongs in chapter 7 as well. **Partly overtaken, D-061.**
P19 declined this on the argument that recuperation needs a channel to nullify
and a corpus has none, and recorded that the argument had not been tested
against chapter 7's text. P20 added section 7.4, a third instance of the
chapter's structure located in the alignment discourse. That does not settle
Q-024 — 7.4 is about the discourse, not the corpus — but it changes the
chapter's shape, and anyone reopening the question should read 7.4 first.
