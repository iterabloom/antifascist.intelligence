# Open questions

**Current as of 2026-08-24, after P10 and D-042.** For orientation read
`finishing/STATE.md`; for the fifth review's disposition read `p10-scope.md`.

Nothing here blocks work. Each item has a default and the moment it applies.

---

### Q-014 — Chapter 6's length: does the fifth review's second cut happen?

**This is the one substantive item of the fifth review that was neither done nor
formally declined.** Tiers 1, 2 and 3 were ruled on and executed (D-038 through
D-041); this was analyzed and never scoped, and it is recorded here so it does
not vanish.

The review: chapter 6 "needs to lose a third of its length." The recurring move —
this body exists, here is its founding year, it binds nobody — "is made something
like thirty times. Three times with the best examples would land harder, and
§8.1.3 would then arrive as a conclusion the reader has earned."

Its specific instructions, kept verbatim in substance: **keep whole** §6.2.2's
closing ("one of the book's two or three best passages"), §6.6.4, and §6.7.6
("the strongest chapter in the second half"). **Compress** the institution
inventories in §6.1, §6.3.5, §6.3.6 and §6.7.1–6.7.3 into tables or an appendix.
**§6.4.4 and parts of §6.4.5** are connective tissue and could go.

What complicates it, measured 2026-08-24:

- **C3 already ran this pass yesterday** under the same criterion (D-032): keep the instance that shows a mechanism working or failing, cut the instance that only establishes a body exists. Chapter 6 went 22,014 → 20,023 words, dated references 88 → 35.
- Chapter 6 now runs **1.8 four-digit years per 1,000 words**, level with chapter 5's 1.7. **Chapter 8 is now the book's densest at 5.8** — if the complaint is about dated-catalogue register, it has moved to a chapter the review praised.
- Chapter 6 is 20,006 of 90,273 words, **22.2% of the book**.
- The ask is roughly 6,600 words, **three times what C3 cut**, and collides with D-019's "no section is cut to hit a number."

**Unresolved and cheap to settle: did the reviewer read a pre- or post-C3 proof?**
If pre-C3, much of this is already done and the item is largely spent. If post-C3,
C3 cut the dates and left the rhetorical move, and the second cut is a live ask.
These call for different responses.

- **(a) Default — establish which proof the reviewer read, then decide.** Costs one question.
- (b) Do the second cut as specified, with a D-019 carve-out.
- (c) Decline: C3 already applied the criterion and the density is now level with chapter 5.

*Default applies when chapter 6 is next opened for any reason.*

### Q-015 — Should `check_all.sh` run from a pre-commit hook?

D-042 made the TOC an enforced invariant, but `check_all.sh` still has to be run
by hand. A commit that skips it goes through. A pre-commit hook would close that,
and it is the same class of gap D-042 just fixed one level down.

`.githooks/**` changes need explicit author approval (`AGENTS.md`), which is why
this is a question rather than a task. Raised in conversation 2026-08-24 and
unanswered.

- **(a) Default — leave it manual.** The hook would also run on every commit, including doc-only ones, and `check_all.sh` takes a few seconds.
- (b) Add a pre-commit hook running `check_all.sh`.

*Default applies if unanswered; reversible either way.*

### Q-016 — §2.1.5 has quadrupled in a day and is unread

It went 1,261 → 2,085 → 2,547 → 3,701 words across four passes on 2026-08-24
(D-038, D-039, D-040, D-041) and is now the book's third-longest section, behind
§6.7.6 and §3.1.2. Every addition answers a real objection and the structure is
sound (6 run-in heads, contrastive negation 1 per 284), but nothing has been read
by the author at any of those lengths.

- **(a) Default — author reads it before it is extended again.**
- (b) Split it: the fork and its costs stay in §2.1.5, the bearer's upkeep and testimony move to a new §2.1.6.
- (c) Leave it.

*Default applies before any further work on the floor argument.*

### Q-011 — Does chapter 2 keep its title? **Resolved by application, 2026-08-24.**
Default (a) was applied at some point during the revise passes without being
recorded here: the chapter is now titled "Foundations of **Compassion and
Empathy** in Friendly AI," compassion leading, against the original "Empathy and
Compassion." Closed retroactively; noted rather than backdated to a decision ID,
since no ruling was sought at the time.

### Q-012 — Does P2 survive as a separate pass? **Resolved, D-021.**
Dropped. See `DECISIONS.md`.

### Q-013 — The roadmap the introduction promises. **Resolved, D-023.**
Neither original option. See `DECISIONS.md`: "roadmap" is the wrong word (it
wrongly insinuates turn-by-turn sequencing), but the fix is not to soften into
vague generality — concrete, practical, specific, and where warranted ambitious
ideas and proposals are what the introduction should promise. Applies when the
revise pass reaches chapter 1.
