# Style sheet

The operative document for the revise pass (D-007). Every section is edited
against this list. Counts come from `reports/tics.tsv` and `reports/voice.tsv`
over 115,377 body words.

Draft. The pilot section will test it, and what the pilot teaches gets folded
back in before the pass proper begins.

## 1. Person and stance (D-008)

| Now | Becomes |
|---|---|
| "This report" (6×) | "This book" |
| Institutional "we" as author (258× in 131 sections) | "I" where the author speaks |
| "We propose / recommend / argue" (36×) | **drop the frame and make the claim** |
| "Our" as the authors' (130×) | "my", or recast |
| "In this section, we…" (22×) | delete; say the thing |

On that last row the author is explicit: not "I argue that X" but simply *X*.
"We propose an array of strategies" becomes the strategies. The hedging frame is
not replaced with a first-person frame; it is removed.

"We" survives only as reader-inclusive — "we can now ask", "what we call
attention" — where it means *you and I*, not *the authors*. When in doubt,
substitute "you and I" and see whether the sentence still means what it should.

This is not a search-and-replace. Most of the 258 instances sit in sentences
built around a committee that did not exist, and the sentence has to be recast.
Expect this to be the bulk of the editing time.

## 2. Section shape

Delete on sight:

- **Closing summary paragraphs.** 31 sections end with "In conclusion" or "In summary". A section of 400–900 words does not need to summarize itself.
- **Opening signposts.** "In this section, we will explore…" Start with the content.
- **The concluding-restatement move** generally: "Ultimately", "In essence" as paragraph openers (7 and 6 respectively).

**Cut the sentence that announces what the next sentence will do.** This is the
rule the pilot produced, and every one of the author's six edits was an instance
of it:

| Drafted | Accepted |
|---|---|
| "The conclusion is uncomfortable and important. What we experience is not…" | "What we experience is not…" |
| "Nor is this a defect. The visual system did not evolve…" | "The visual system did not evolve…" |
| "That reframing matters for machine perception, because it changes what an attention mechanism is for." | "The implication for machine perception?" |
| "…are the most consequential instance, and they make the point about blind spots concrete." | "…illustrate the point about blind spots." |
| "That claim is taken up in the discussion of machine self-models in section 2.3.3, where…" | "Section 2.3.3 expounds on this point in discussing machine self-models, where…" |
| "the design question is not how to allocate attention efficiently. It is whether a system can be built to notice…" | "the design question is how it will notice…" |

Three corollaries:

- **Prefer the positive construction to "not X. It is Y."** The contrastive frame is announcing in another costume: it spends a clause on the wrong answer.
- **Prefer an active subject to a nominalized one.** "Section 2.3.3 expounds" over "That claim is taken up in the discussion of".
- **A rhetorical question is permitted** where it replaces a paragraph of throat-clearing. "The implication for machine perception?" does the work of two sentences.
- **Drop the superlative you cannot defend.** "the most consequential instance" became "illustrate".

Keep and strengthen: the concrete example. Where a section already has one
("Consider an AI system created for customer service…"), it is the best thing in
the section and usually deserves to come first rather than fourth.

## 3. Word-level lint

Highest-frequency tics, with counts. None is forbidden; each is a flag that the
sentence is doing less work than it appears to.

| Word | Count | Sections | Per 10k |
|---|---|---|---|
| foster / fostering | **278** | 149 | 24.1 |
| robust / robustness | 148 | 88 | 12.8 |
| crucial | 118 | 93 | 10.2 |
| nuanced | 71 | 54 | 6.2 |
| navigate | 67 | 54 | 5.8 |
| leverage | 59 | 51 | 5.1 |
| intricate | 47 | 38 | 4.1 |
| harness | 34 | 28 | 2.9 |
| pivotal | 33 | 28 | 2.9 |
| landscape | 29 | 24 | 2.5 |
| realm | 28 | 26 | 2.4 |

"Foster" is the signature: it appears once every 415 words and in 53% of
sections. It almost always means *encourage*, *build*, *cause*, or nothing at
all. Prefer the specific verb; if no specific verb fits, the claim is probably
empty and the sentence should go.

Connective tics — "Moreover" (34), "Furthermore" (32), "Additionally" (30) — are
usually a paragraph pretending to follow from the one before it. Cut the word;
if the paragraph no longer follows, that is the real problem.

## 4. Lists

585 enumerated items in 102 sections sit outside the `<<list>>` markup, in four
different styles: `(n)` 380, bullet 97, `n)` 95, alpha 13. Chapters 2–10 all
have them; chapter 3 has 117.

Rule: `<<list>>` markup for anything that is genuinely a list; `(n)` inline
enumeration only where the items are short and the sentence needs them numbered.
A run of five paragraph-length items each beginning "(3)" is prose wearing a
list's clothes — either make it a real list of short items or write it as
paragraphs.

## 4a. Boxes

`<<box>>` … `<</box>>`, first line taken as the title. For a case study or a
self-contained episode that would derail the paragraph it sits next to — the
mirror-neuron overshoot in §2.2.1 is the model. A box is the author's own prose
and counts toward the word count, unlike an epigraph.

Use sparingly. A box is a promise that the material is worth stepping out of the
argument for.

## 5. Dates and currency (D-008 dating policy)

Prose is dateless. The book does not say "currently", "recently", "state of the
art", or "is being developed" — 117 flagged instances in 49 sections, in
`reports/dated.tsv`, each with a proposed remediation.

Where a specific date or system genuinely matters, it goes in a clearly dated
box, so a reader in 2030 can see what was true when and the surrounding prose
does not rot with it.

## 6. Citations (D-009)

Endnotes for named studies, statutes, systems, and quotations. Nothing else.

While revising, a factual assertion gets `[[cite:CNNNN]]` keyed to
`reports/claims.tsv` (268 items in 91 sections at the start of the pass).

**Transplanted material brings its own citation debt, and its placeholders are
allocated at transplant time, not deferred.** The pilot appended five rows to
`claims.tsv` as it went; doing that retroactively across sixteen transplants
would mean re-reading all of them. Expect the debt to rise during P3, not fall —
imported material makes specific empirical claims where the original made
general ones. **The agent never writes a
reference entry.** An assertion nobody can source is cut during the revise pass,
not carried forward with a placeholder — that is the rule that stops the
citation backlog from becoming the project.

## 7. Cross-references

The book currently contains one backward reference and one forward reference in
115k words, which is why the same argument can appear nine times without anyone
noticing. Under D-013 the surviving instance of each repeated argument is the
one place it is made; every other location that needs it gets a cross-reference
instead. Target: at least one real cross-reference per section, where honest.

## 8. Mechanics

- Apostrophes and quotation marks: straight, consistently. Currently 734 straight to 38 curly, 178 straight double to 6 curly. Normalize in P0, not by hand.
- Em dashes: keep; the text uses 70 and they mostly work.
- "AI" as a mass noun ("an AI system", not "an AI") except where the book means an individual system, which it sometimes does deliberately — that distinction is load-bearing in chapters 2 and 7 and should be made consistently.
- Spelling: US.
- Section titles: sentence-shaped, under about ten words. The current set includes titles of 20+ words.

## 9. What this pass does not do (D-007)

Not rewriting the argument. Not filling the stub sections. Not adding topics the
book lacks. Not arguing the anti-authoritarian thesis where it is currently
assumed. If a section is wrong rather than badly written, the fate is Cut or
Merge, not a rewrite — and if that turns out to be true of many sections, that
is evidence to bring back to D-007, not a licence to start writing.
