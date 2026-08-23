# Pilot: transplant T11 into §3.1.2.3.1.1 Attention

Branch `pass/pilot`. One section, revised end to end under `style.md`,
`transplants.md` (T11) and D-009. Nothing else in the book was touched.

`attention_before.txt` and `attention_after.txt` are the two versions; read them
side by side. What follows is what the exercise measured and what it taught.

## Measurements

| | Before | After |
|---|---|---|
| Words | 589 | 781 |
| Paragraphs | 12 | 10 |
| Closing summary paragraph | 1 ("In essence…") | 0 |
| Authorial "we" | 0 | 1 (reader-inclusive) |
| Cross-references | 0 | 1 (to §2.3.3) |
| Citation placeholders | 0 | 5 |
| Style-sheet tics | 6 (pivotal, harness, leverage, instrumental ×2, in essence) | 0 |
| Typos | 1 ("neccessary") | 0 |

Five new claims were appended to `reports/claims.tsv` as C0269–C0273, all
`unverified`, all marked as introduced by the pilot. The transplant *raises* the
citation debt, which is expected: the imported material makes specific empirical
claims where the original made general ones.

## What changed, structurally

The old section opened with a definition ("Attention remains a vital cognitive
function, instrumental in sieving through a barrage of stimuli") and reached its
concrete example — transformers — in the ninth paragraph. The new one opens with
the 1999 gorilla experiment and reaches the same transformer material in the
same place, but by then the reader has a reason to care about it.

Three things were kept: the two-mode account (goal-directed and stimulus-driven,
with the anatomy), the transformer payoff, and attention schema theory. Two
things were cut: the "roadmaps for integrating Attention Schema Theory" paragraph,
which proposed a "meta-attention" layer without saying what it would do, and the
closing summary.

One thing was added that is neither transplant nor original: the paragraph
connecting inattentional blindness to machine attention — that a system which has
learned which inputs reward processing has thereby learned which to be blind to,
and that such blind spots are invisible from the inside. The Atlas does not say
this, because the Atlas is not about machines; the manuscript did not say it,
because it treated attention as resource allocation. **The pilot's most useful
finding is that this is where the value is.** Transplanting the science alone
would have produced a better-written section about human attention sitting inside
a book about AI. The join has to be written, and it is the part that cannot be
copied from either source.

## What this teaches about the estimate

- **A transplant is not a paste.** T11 was chosen as the *easiest* in the set: zero second-person instances, no person-characterization to scrub, replace rather than argue. It still required deciding what the imported material was *for* in this book, which is authorial work.
- **The register held.** The Atlas's case-first prose survived the move without carrying its second person, and the result does not read like two books.
- **Sections grow.** 589 → 781 words, and this was a *replace*. The length arithmetic in `PLAN.md` §1 should be treated as a floor, not an estimate.
- **The style sheet was sufficient.** No rule needed inventing mid-edit. One amendment follows.

## Amendment to style.md

Add, under §6 (Citations): *transplanted material brings its own citation debt,
and the placeholders are allocated at transplant time, not deferred to P4.* The
pilot appended five rows to `claims.tsv` as it went; doing this retroactively
across sixteen transplants would mean re-reading all of them.

## Outcome: accepted with edits, one round

The author accepted the draft and returned six edits. Every one was the same
move — **cutting the sentence that announces what the next sentence will do** —
and that rule is now in `style.md` §2 with the six before/after pairs as its
worked examples. It is the most valuable thing the pilot produced.

Word count: 589 original → 781 agent draft → **734 accepted**. The author's
edits removed 47 words of the agent's scaffolding, so the real growth for a
replace-mode transplant is **+25%**, not +33%.

The author also closed the section with a quoted line from *Westworld*, threading
back to the epigraph already in §2.4. Logged as C0274 and added to the D-012
permissions list — it is the fourth piece of third-party quoted material in the
book, and short quotations still belong on that list rather than being waved
through.

## A measurement bug the edits exposed

The author's rephrasing — "Section 2.3.3 expounds on this point" rather than
"in section 2.3.3" — was scored as **zero** cross-references by
`section_stats.py`, whose pattern required a preposition. Fixed. The book-wide
count goes from 2 to 4, which does not change the conclusion (four
cross-references in 115k words) but does mean the metric was wrong in the
direction that flatters the tooling.

## Still not measured

Wall-clock author minutes per section, which is the one number the effort
estimate is parametric in. See `finishing/estimate.md`.
