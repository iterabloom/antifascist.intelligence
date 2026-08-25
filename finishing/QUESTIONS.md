# Open questions

**Current as of 2026-08-24, after D-052.** For orientation read
`finishing/STATE.md`; for the sixth review's disposition read `p11-scope.md`.

All section numbers here use the **post-D-043 numbering** (chapters 3 and 7 are
new; old 3–9 became 4–11).

Nothing here blocks work. Each item has a default and the moment it applies.

---

### Q-018 — Chapter 8's compression was only partly implementable

The sixth review asked that chapters 8's §§8.1–8.3 be compressed on the grounds
that they read as annotated inventory. **That premise no longer describes the
text**, because C3 (D-032) already ran that pass: those sections now average
about 300 words and carry two dated references between thirteen of them, each
built around one argument rather than a list. P11 did the structural compression
that still applied — three sections merged away, no argument dropped — and stopped
there rather than cutting prose that had already been converted from inventory to
argument.

This is recorded because it is the **second** review to ask for a chapter-6/8 cut
that C3 had largely already made, and because the honest report is a partial
implementation. Chapter 8 is 22,707 words, 24.5% of the book, and the bulk is now
in §8.7.6 (4,769) and §8.3.3 (3,157) — the jobs-guarantee material the review
itself wanted carrying the chapter.

- **(a) Default — accept the partial implementation and say so.** Done in
  `p11-scope.md`.
- (b) Cut §8.7.6 further; at 4,769 words it is the book's longest section.
- (c) Ask the reviewer which proof was read, which is the question Q-014 raised
  and which P11 executed past rather than answering.

*Default applies now; (b) and (c) are live if the author wants the chapter smaller.*

---

### Q-019 — The glossary defines a term the book never uses

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

### Q-020 — §8.7.4 opens on a forward pointer

The author flagged §8.7.4's reference to §8.7.6 as backward-pointing at content
that follows. **The reference itself is sound** — §8.7.6 does compare the EU, US,
UK and China as §8.7.4 describes, and does cover the human-rights treaty — so
nothing was repaired. What is real: §8.7.4's *first sentence* summarizes four
regulatory regimes the reader will not meet for two more sections, then argues on
top of that summary ("Those four already diverge sharply"). A reader going
straight through meets the premise before the evidence.

This is the fourth review's complaint — the book optimized for dipping in at the
cost of reading linearly (D-037) — in a place that pass did not reach.

- **(a) Default — leave it.** The sentence is accurate and the section is
  self-contained enough to follow.
- (b) Rewrite §8.7.4's opener to state the divergence in its own right and demote
  the §8.7.6 pointer to a parenthetical. Cheapest fix; one sentence.
- (c) Reorder §8.7.4 after §8.7.6. Cleanest for a linear reader; renumbers two
  sections and every reference to them, which is the operation D-046 exists
  because of.

*Default applies now; (b) is the low-cost option if the author wants it fixed.*

---

### Q-021 — §3.6's title promises what its body does not do

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

## Resolved

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
