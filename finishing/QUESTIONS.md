# Open questions

**Current as of 2026-08-24, after P11 and D-043.** For orientation read
`finishing/STATE.md`; for the sixth review's disposition read `p11-scope.md`.

All section numbers here use the **post-D-043 numbering** (chapters 3 and 7 are
new; old 3–9 became 4–11).

Nothing here blocks work. Each item has a default and the moment it applies.

---

### Q-015 — Should `check_all.sh` run from a pre-commit hook?

D-042 made the TOC an enforced invariant, but `check_all.sh` still has to be run
by hand. A commit that skips it goes through. A pre-commit hook would close that,
and it is the same class of gap D-042 fixed one level down.

`.githooks/**` changes need explicit author approval (`AGENTS.md`), which is why
this is a question rather than a task. Raised 2026-08-24, unanswered, and P11
made it more pressing: this pass rewrote every cross-reference in the book by
script, and the only thing standing between a bad regex and a committed manuscript
was that I chose to run the checks.

- **(a) Default — leave it manual.** The hook runs on every commit, including
  doc-only ones, and the suite takes a few seconds.
- (b) Add a pre-commit hook running `check_all.sh`.

*Default applies if unanswered; reversible either way.*

### Q-017 — The prose tic is in chapter 5, and nobody has asked for a pass there

**New, and it is a finding rather than a request.** The sixth review asked for a
rhythm-breaking pass in the chapters that are now 4 and 8. Measured, those are
near the bottom of the book. Contrastive negation per 1,000 words after P11:

| ch5 | ch11 | ch10 | ch2 | ch6 | ch9 | ch4 | ch8 | ch7 | ch1 | ch3 | ch0 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9.9 | 12.7 | 7.8 | 6.5 | 6.0 | 5.3 | 5.7 | 5.4 | 4.7 | 4.4 | 3.5 | 2.6 |

Chapter 11 is the glossary, where "X rather than Y" is definitional and the
number is expected. **Chapter 5 (Moral Psychology and AI) is the real outlier at
roughly one per 101 words, against D-025's band of one per 216.** No review has
mentioned it. The pass was not run because the review did not ask for it and the
author's instruction was to implement the review.

Caveat on the measurement: this counts one of the three patterns the review named
("rather than", ", not", "instead of", "not because"). Tricolon and the two-beat
close were not measured and I make no claim about them.

- **(a) Default — do a D-025 pass on chapter 5 when it is next opened.**
- (b) Do it now as its own pass.
- (c) Leave it; the band is a guideline and chapter 5 is argumentative prose where
  the construction earns its place.

*Default applies when chapter 5 is next opened for any reason.*

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

## Resolved

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
