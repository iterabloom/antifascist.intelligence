# Open questions

**Current as of 2026-08-28, after D-093. Six questions are open**, raised by
P28 through P31, none of them blocking and each with a default that has already
applied: how much further to cut the cross-references, how much further to cut
chapters 4 and 5, whether chapter 3 should move earlier in the book, whether to
fold the subsections P29 left thin, whether to prune `refs.bib`, and whether
chapter 9's gap list should get its nearest-work notes back. For orientation read
`finishing/STATE.md`.

The other standing item is not a question. **116 of the book's 162 sections are
`drafted` and unread**, concentrated in chapter 2 and chapters 4 and 5, which P29
cut, chapter 3, which P27 rewrote, chapter 11 entire, which P31 reordered when it
was chapter 9, and the three chapters P32 made out of chapter 8. `ledger.tsv`
carries the per-section reason.

All section numbers here use the **post-D-043 numbering** (chapters 3 and 7 are
new; old 3–9 became 4–11). Entries written before 2026-08-25 refer to section
8.7.6 as the geopolitics section and to 8.7.7 as the democratic-dividend section;
D-067 split 8.7.6 into 8.7.6–8.7.9 and renumbered 8.7.7 to 8.7.10.

**Every entry below was written before D-093 and none has been renumbered for it.**
P32 split chapter 8 into chapters 8, 9 and 10 and shifted old 9, 10 and 11 to 11,
12 and 13; `renumber-map_2026-08-28c.tsv` translates. Where an entry below says
chapter 9 it means what is now chapter 11, and where it names a section under 8.4,
8.5, 8.6 or 8.7 those are now 9.1, 9.2, 9.3 and chapter 10. Q-031 is about what is
now chapter 11.

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

---

### Q-028 — Whether chapter 3 should move earlier in the book

P29 made chapter 3 the book's centre by what leads into it: chapter 1's roadmap
corrected, chapter 2's opener rewritten around the four results chapter 3 uses,
four chapter-5 openers stating what the floor takes from them. Its share of the
book went from 7.62 to 8.13 percent without a word changing in it. Position was
left alone.

- **(a) Default — leave it third.** Moving it reverses D-043's promotion, and the
  dependency runs the wrong way: chapter 3 argues from section 2.3.4's affect
  evidence and section 2.4.1's ladder, both of which precede it.
- (b) Promote it to chapter 2, folding the four load-bearing results of the
  present chapter 2 into it and demoting the rest. This is the version that makes
  the centre structural rather than rhetorical, and it is a chapter-scale rewrite
  plus a renumber of everything after it.

*Default applies now.*

---

### Q-029 — The subsections P29 left thin, and whether to fold them

Twelve leaf subsections are now under 230 words, and eight of them are P29's
work: 2.4.3 at 142, 5.5.2 at 162, 4.3.2 at 184, 2.2.2 at 186, 5.1.2 at 195, 5.4.1
at 201, 2.3.2 at 212, 2.4.5 at 220. The other four — 6.2.2, 6.3.2, 8.2.3, 8.4.3 —
were that short before this session and are not new. The book already carries much
shorter section openers; what makes these look odd is that they are leaves.

- **(a) Default — leave them.** Folding renumbers a chapter against 801 resolved
  references and needs a renumber map, and P28 rebuilt the reference regime days
  ago.
- (b) Fold them into their neighbours, with a renumber map on the
  D-031 / D-043 / D-091 model. P30 shows the cost: four sections moved, 16
  references repointed, five files of bookkeeping.

*Default applies now.*

---

### Q-030 — `refs.bib` has 20 entries nothing cites

P29 orphaned twelve `\autocite` keys by cutting the prose around them, and eight
were already uncited before that: 20 of the file's 289 entries are now reachable
from nothing in the manuscript. Nothing prints them, because biblatex only sets
what is cited, so this costs a reader nothing and costs the file its correspondence
with the book.

- **(a) Default — leave them.** An entry costs nothing where it sits, and one of
  them may be wanted again by whatever pass next touches the material it supported.
- (b) Prune the 20, recording them in the commit body so they can be restored from
  git.

*Default applies now.*

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
which is a large part of what made it read as a catalogue.

- **(a) Default — leave it.** Nothing is gone from the book; it is one place
  instead of two, and the place is the section that owns the material.
- (b) Restore the notes to the opener, at roughly 300 words, and let the chapter
  go over its previous count. The instruction's constraint was met once and
  arguably does not bind a later decision by the author.
- (c) Restore them and take the 300 words out of the sections, which means cutting
  argument rather than duplication, since the duplication is what already went.

*Default applies now. `p31-scope.md` has the full accounting of what paid for the
program.*

---

## Resolved

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
than its neighbours reads as a different hand is a question measurement cannot
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
