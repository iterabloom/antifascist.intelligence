# P109 — the cross-reference audit worked through: 376 references removed on rulings, 494 to 118

**The instruction.** The author supplied `~/book-scratch/xref-audit.md`, a table of every in-text
cross-reference in the 2026-09-05 proof with a `keep?` column, nineteen rows TRUE, and read it as
*the nuclear option. what it is saying is "delete all of the xrefs except for these 19"*. Then:
*there's got to be some ratio. I can tell you that right now it is too dense with xrefs. it is
unnatural. but I don't know what a reader-friendly ratio is. has anyone published scholarly work on
that?* Then *find 30 more*, ten at a time from memory, each ten assessed by an Opus subagent on one
question: *is this crossref either enlightening or otherwise helpful to the reader? or conversely,
is it more trouble than it is worth?* Then, for every row neither kept nor ruled on: Sonnet
subagents, chunked by paragraph, each answering *what is the most reader-friendly version of this
passage that does not send the reader anywhere*, in three classes, target checked before any gloss.
Then, bucket by bucket: *please investigate each … and tell me whether each is or is not an
improvement*; *apply to the manuscript the eleven that were not improvements WITH their repair*;
*apply the fifteen neutrals WITH their suggested tightenings*; *apply the 94 that are improvements*;
*make the proofs*; the same for the other three buckets; *and then we're done! with this part
anyway*. Every application was on the author's instruction; every verdict was mine and is recorded
per row.

## The audit

490 rows, extracted from the plain text of the proof by the pattern `section N` or `chapter N`.
Reconciled against the manuscript: 468 body rows, 15 glossary and appendix rows mislabeled §12.3,
and 7 bibliography annotations counted as references (the Restatement's §19, Frankfurt's "chapter
7"); 26 body references missed, the second and later items of lists like *chapters 4 and 5*. The
manuscript held 494 body references and 530 in all. The nineteen keeps were set by a *reader's
report, section 10* that is not on this machine and is not the 2026-09-02 review.

## The ratio

No study varies the number of cross-references in a book and measures reading. What exists gives
a band. Hyland's corpus tables (*Metadiscourse*, Continuum 2005, Tables 5.2, 7.1, 7.5) put
endophoric markers, expressions pointing at another part of the same text, at 0.3 per 1,000 words in
philosophy textbooks, 0.8 in sociology, 2.5 in applied-linguistics articles, 4.6 to 9.2 in the
sciences, where they are figure and table references. Public-domain argument books, measured here on
in-paragraph references to their own chapters with headings excluded: Darwin's *Origin* one per
4,100 words, his *Descent* one per 5,000, Smith's *Wealth of Nations* one per 16,600, Hume's
*Treatise* five numbered references in 226,000 words and a phrase back-reference every 4,000. The
one study that isolates cross-references (Lasky 2019, the Internal Revenue Code, 75 readers) found
references that change what was just read hurt badly and references that add help modestly; the
hypertext experiment that tested link count directly (Madrid, Van Oostendorp and Puerta Melguizo
2009, 3 against 8 links per page) found no effect on learning; Camiciottoli 2003 found more
metadiscourse did not hurt. Style manuals say *with discretion* and give no number. The book stood at
5.3 per 1,000, one per 187 words; an outside reader at 4.3 per 1,000 had called it *a map of the
book*. It now stands at about 1.3 per 1,000, one per 770 words. Sources are in the session record;
one tool summary reported the opposite result for the 2009 experiment and was corrected from the
paper's own text.

## The keep list

Thirty candidates named from memory in three tens and ruled on by three Opus readers, each opening
the citing paragraph and the target. Rulings, per reference: batch one 4 helpful of 10 items; batch
two 9 helpful and 6 trouble across 15; batch three 10 helpful and 5 trouble across 15. Thirteen
items wholly helpful, 18 audit rows, were flipped TRUE, so the audit now carries 37. The prose of
every ruling is in `helpful.txt`, `mixed.txt` and `trouble.txt`. **Eight of the roughly forty-five
references read closely pointed at a target that does not say what the sentence credits it with**:
§9.3.2 crediting §3.1 with Replacement's discharge condition, which §3.3 states; §6.2 crediting
§3.8 with the word *accommodation*, which §3.8 never uses; §6.4.1 crediting §10.2 with a criterion
set it does not give; §3.3 crediting §4.2.3 with an identity §4.2.3 credits to §3.5; §5.1.2
crediting §2.1.2 with requirements on mentors it does not contain; §9.1.5 crediting chapter 10 with a
case that appears in one line of §10.6; §4.1.2 crediting chapter 6 with a mechanism it never
describes; §3.1 crediting chapter 7 with a framing §3.9 supplies.

## The files

`xrefs-that-have-issues.md`, every non-TRUE row with `status` and `finding / action` in place of
the two audit columns, was split: `shovel-ready.md`, 34 rows the Opus readers ruled on (11
keep-after-repair, 8 misdirected, 15 trouble), each with its finding and the repair it implies;
`unread.md`, the rest; then spun off from it `collateral.md`, 7 rows whose paragraph holds a kept or
ruled reference, `roadmaps.md`, 18 (chapter 1's roadmap, chapter 11's opening, chapter 6's opener
pointing into its own chapter), `near-roadmaps.md`, 12 (section openers pointing at their own
subsection, chapter openers mapping neighbouring chapters), and `out-of-scope.md`, the 22 glossary,
appendix and bibliography rows. That left 360 rows in `unread.md`, every one resolving to a unique
paragraph line in the tex.

## The rewrite pass

Eighteen Sonnet subagents, launched in waves of five, each with a brief listing its paragraphs and
one shared instruction file: three classes in order of preference, *mechanical* (drop the number
and change nothing else), *gloss* (a few words in the book's vocabulary), *paraphrase* (only if the
argument does not run without the claim); no claim the paragraph does not already make and no new
citation; the target opened before any gloss and *target mismatch* returned where it does not say
what it is credited with; `style.md` §§1, 2, 2a, 3, 3a, 7 and 8 read first; LaTeX-ready text with
`current` an exact substring of the tex line. 297 paragraph entries came back; every row covered,
every `current` found in its line, no reference left in a proposal, no straight quote, ASCII dash,
`\textit`, new *we* or new citation. By row: 310 mechanical, 44 gloss, 2 paraphrase, 4 target
mismatch. The four mismatches, all in chapter 3: row 60, §3.1 crediting §3.8 with *no dissonance, no
shame*; row 75, §3.3 crediting chapter 7 with the claim about who is in the room when a quorum is
chosen; row 98, §3.4 crediting §2.3.1 with a verdict on a builder's self-interested finding; row 118,
§3.8 saying §2.3.2's guardianship runs on the parenthood analogy when §2.3.2 chose the research
animal at D-199. **Twelve misdirected pointers in this pass, ten of them in chapter 3**, the chapter
the fortnight before this one revised most.

**Another session applied the six flagged items** (the four mismatches and the two paraphrases,
seven references) on the author's rulings at `316f7a4`, and rebuilt the proofs at `e40e676`, while
this one was running the chunks; its commit message records each ruling. It marked the seven rows
applied in `unread.md`, and the tables and the tree agree.

## The rulings and the four batches

*Mechanical* was not one thing: only 8 of 251 entries were a pure drop. The rest were bucketed by
words changed beyond the dropped number and every entry read one by one against one test, whether
the sentence reads as well or better without the number with nothing lost that the reader needs.

| Bucket | Entries | Rows | Improvement | Neutral | Not | References out | Work commit | Proofs |
|---|---|---|---|---|---|---|---|---|
| 0 to 3 words | 120 | 122 | 94 | 15 | 11 | 126 | `0ebbbb2` | `fc4001a` |
| 4 to 10 words | 103 | 129 | 82 | 17 | 4 | 136 | `44fa4a1` | `e753802` |
| 11 or more | 28 | 48 | 20 | 4 | 4 | 52 | `514424d` | `a2283df` |
| Glosses | 40 | 54 | 33 | 7 | 0 | 55 | `7b75cf5` | `be248b2` |

Improvements went in as proposed. Neutrals went in with the tightening the review named where it
named one (a passive given its agent, a definite article pointing at nothing on the page made
indefinite, a term of art kept marked as one, a caveat given its source, a stipulation of the
book's kept as *this book defines* rather than asserted as fact) and as proposed otherwise. The
nineteen not improvements went in with the repair in place of the proposal. The ones that carry a
claim: §3.8's *the previous section* was three sections wrong and now names the halt argument;
§10.6 exists to limit the democratic dividend and the proposal made it assert the dividend, so it
now reads *the credit given to a state with*; §5.1.2 keeps *Recuperation is what happens when that
hazard is industrialized* in place of a cut pointer; §11.3's opening said the four sites that lean
on a detector *send the reader here*, and after the batch none of them does, so the clause is gone,
and the opening now says *This book gives fascism a structural definition* and names the
recuperation argument rather than *another* chapter; §8.1.1's *the clearest case* and §9.1.4's
*working examples* were claims the book had not made. The full list, one line per row with the
reason, is the `REVIEW:` note in each row of `unread.md`.

**Two consequences beyond wording.** §3.10's second question no longer hands the slow drift of a
role to chapters 4 and 5, which was P104's largest unruled item; the sentence ends on the learned
half doing the floor's work. And §11.3's opening was brought to what the book says after the cuts,
which is D-203's rule met at the commit that made it necessary.

## Numbers

**494 → 118 body references; 530 → 154 in all, the glossary's 34 and the appendix's 2 untouched;
92,514 → 91,207 words; 188 → 187 pages; 0 undefined references; 20 → 19 overfull boxes; 138
sections; 111 sections changed; 319 bibliography entries, none of which lost its last citation;
suite green at every commit; the proof pair rebuilt in place four times, the README's links
standing.** Commit `514424d`'s message says 54 references and 171 where the tree said 52 and 173;
`7b75cf5`'s message records the correction.

## Left undone, named

- **`shovel-ready.md`, 34 rows**, the Opus readers' rulings with a repair specified for each: the
  author's word is that the next session does these.
- **The rows set aside**: `roadmaps.md` 18, `near-roadmaps.md` 12, `collateral.md` 7. The
  out-of-scope 22 need nothing. The audit's own preamble still says nineteen TRUE.
- **Nobody has read the 111 changed sections end to end**, and no page was looked at. The checks on
  the rewrites were mechanical.
- **`reports/xref_shapes.tsv`, `reports/xref_pairs.txt` and `xref-paragraphs-*.md`** describe a
  manuscript with 395 to 494 body references and are stale.
- The reader's report the audit cites is not on the machine; the nineteen keeps rest on it unread.
- P103's four, the rest of P104's list, P105's one, Q-070 and Q-074 are as they were.
