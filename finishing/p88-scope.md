# P88 — an outside review checked against the source, and its bibliography defects repaired

**The instruction.** The author supplied `reviews/author-discussion_2026-09-02.md` — an editorial
review of the 2026-09-02 proof and the discussion after it, from a model given the HTML and nothing
else — and asked for an analysis of it. Then, in order: *yes on fixing the bib issues*; *re the two
notes-to-self, don't touch those*; agreement with the substantive findings and with the caution
about the model's framing; *do it*, on the one text change offered.

**What this pass is.** Not a revision pass. Every claim in the review that could be checked against
the manuscript was checked, and the checkable half of its bibliography audit was repaired. The
argument findings became Q-071 through Q-074 and nothing was rewritten on them.

## What the review got right, verified

| Claim | Verdict |
|---|---|
| §10.1's IEEE→OECD causal link is disclaimed by its own source note | **Held, verbatim.** Repaired, D-181 |
| `cfpb2025funding` ends mid-sentence at *Judge Edward J.* | **Held.** Repaired |
| Duplicate Chinese State Council plan entries | **Held**, and cited adjacently at §10.2. Repaired |
| EU AI Act split across authorities | **Held and understated** — four entries, not two. Repaired |
| Kitwood's page number rests on convergent secondary citations | **Held**, and stale as well. Q-074 |
| Annotation printing between journal metadata and pages | **Held**, 10 instances. Repaired |
| Adjacent citations at §2.2.3, §5.5, §6.2 | **Held and understated** — five sites. Repaired |
| `no one` / `no-one` inconsistent | **Held**, 6 against 2. Not done, prose |
| Chapter 3 is ~17,600 words, nearly one-fifth of the body | **Held**: 17,478 and 19.5 percent |
| Body ~90,500 words | **Close**: 89,854 by `section_stats.py`, which excludes the epigraphs |
| §4.3.1's play disposition is *not written down anywhere* and so uneditable | **Held, and it contradicts §3.8** |

## What did not survive checking

**The DOI is not a bibliography defect.** `refs.bib` carries
`10.1007/978-3-662-47854-7_14` correctly and **the PDF sets it correctly**; only tex4ht's HTML
display text is wrong, and its own href is right beside it. Escaping the underscore in the `.bib`
**broke the href and made the display worse**, which was tested and reverted. The repair belongs in
`html_single_file.py` and went there. A reviewer reading the HTML could not have seen this.

**The cross-reference density is understated, not overstated.** The review reports about 304 section
and 89 chapter references, one pointer per 230 words. The source carries **462 `\ref{sec:}`**, 428
of them outside the glossary, which is **one per 207 body words**. The review's split does not match
the source's forms because 156 references are a bare `~\ref{}` after a noun.

**The four technical objections in chapters 4--6 are each about roughly one sentence.** All four
topics exist — `predictive coding` 1, `Friston` 1, `homeostatic` 1, `curriculum learning` 1,
`catastrophic forgetting` 1 — so none is invented, but presented as a block they read structural and
are line edits. **The exception is §4.3.1**, whose claim that a disposition acquired by exploration
*is not written down anywhere, and what is not written down cannot be edited* is load-bearing for
play as antifascist design, and **is contradicted by §3.8**, which says a bearer with plastic weights
is shaped by what it is given to learn from — chapter 7's pipeline running for the length of the
deployment. Recorded here; no ruling sought this pass.

## What the review missed, and what the record already held

**Two author notes-to-self typeset in both committed proofs**, in §2.3.2 — the section the review
named as its first revision. The review did not mention them. **They are not unrecorded**: Q-069 and
Q-070 carry one each, verbatim, and say they were *moved here because it would otherwise typeset*.
**The move out of the manuscript never happened**, so that sentence in `QUESTIONS.md` is false as it
stands. The author's instruction was to leave both notes alone; the discrepancy is noted in the
`QUESTIONS.md` header rather than repaired.

The convergence is worth keeping: an outside reader's most important substantive revision landed on
the paragraph the author had already flagged in the text as suspect, and on the loophole two
paragraphs after it.

## The discussion half, and the one finding that had to be corrected

Three gaps, all measured, all now Q-071 to Q-073. **One of them was first reported to the author in
a stronger form than the record supports, and the correction is the useful part.**

**Q-071 was first put as "the book never connects the jobs guarantee to bearer exit."** That is
wrong. **D-109 (P45) made the connection on the author's own instruction** — *compute floor is the
same shape as the human jobs guarantee* — and §11.2 carries it. What is true is narrower and
sharper: `outside option` occurs **twice in the book and both are in §11.2**, chapter 3 has neither,
and **§3.8 calls the bearer's Hirschman set *narrower and still complete* with nothing local to
complete it**. §3.8's five references do not include §11.2. The discussion's own proposal — an
outside option that is a public institution rather than an allocation — is genuinely beyond D-109.

**Q-072**, chapter 3's missing vocabulary for culture: `culture` 0, `cultural` 0, `community` 0,
`sociality` 0, `peers` 0 in chapter 3, and its six references to chapters 4 and 5 are all the same
move. **Q-073**, the one-sided ledger: `suffer*` 52, `welfare` 27, `joy` 0, `delight` 0, and
`flourish*` once — in §12.1's title, about humans.

**Where the model overreached, and it is on the record because the author agreed with the caution.**
*That suggests the book may locate the floor one level too low* is the model's phrasing, not the
author's, and states more than the argument earns: the book has a reason for putting the floor in an
individual bearer, which is that chapter 7 is an account of a culture being recuperated. The model's
own best line cuts against its enthusiasm — affect, sociality and culture keep terrible things
together too — and that tension is left unresolved in the transcript.

## Numbers

**89,854 words and 183 pages, both unchanged.** `refs.bib` **305 → 301**. 0 undefined references, 0
undefined citations, `check_all.sh` green. **The manuscript diff is eight citation edits and one
clause** — the IEEE/OECD restatement — and no other prose word changed. `., pp.` collisions **10 →
0**. ORDER.tsv shas refreshed for the nine files touched.

## Left undone, named

- **The proof pair is stale after this pass** and was not rebuilt; the date has not rolled over, so
  a rebuild would be in place and the README's links would not move.
- `no one` vs `no-one`, and the heading-capitalization pass: prose, not bibliography, and outside
  what was authorized.
- The review's structural recommendations — cut chapter 3 by 25--30 percent, the proposition map,
  moving legitimacy forward — were not acted on and are not carried as questions. They are
  recommendations, not findings, and each is a pass.
- §4.3.1's contradiction with §3.8 is recorded above and nowhere else.
