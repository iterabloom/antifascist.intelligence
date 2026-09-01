# P83 — the paragraphs over 200 words split, one left standing on an earlier decision

**The instruction.** Mean paragraph is ~100 words; 129 paragraphs (15 percent) exceed
150, 42 exceed 200, the longest is 437 and the two longest are both in §11.2. Long
paragraphs and long sentences compound: a 400-word paragraph made of 45-word sentences
gives the eye nowhere to rest. Splitting the 42 over 200 words would help more than any
amount of sentence-level editing.

**Every count is right. The mechanism named for why they are bad is not, and the
correction makes the remedy easier rather than harder.**

## The counts

| | Finding | Measured |
|---|---|---|
| Mean paragraph | ~100 | **102.0** |
| Over 150 words | 129 (15%) | **133 (15.0%)** |
| Over 200 words | 42 | **43** |
| Longest | 437 | **433** prose (453 counting a list) |
| Two longest both in §11.2 | yes | **yes**, 433 and 431 |

**Seven of the 43 are `enumerate` or `itemize` blocks and not walls of text**, including
the 453-word block that is the longest thing in the book. A list gives the eye rest by
construction. **The real target was 36.**

## The compounding claim does not hold in the form stated

| Paragraph size | n | mean sentence in them | sentences per paragraph |
|---|---|---|---|
| ≤150 words | 755 | 26.3 | 3.3 |
| 150–200 | 89 | 30.6 | 5.9 |
| >200 words | 36 | 30.7 | **9.0** |

**Correlation between paragraph length and mean sentence length is r = 0.297** over 880
prose paragraphs. Long paragraphs do carry longer sentences, by about four words, and
**the effect plateaus above 150** — the >200 group is not worse than the 150–200 group.

**No paragraph in the book is the one the finding describes.** The 400-word paragraph
(§3.1) is built from **25.0-word sentences, below the book average of 25.9**. The 433 has
28.9 and the 431 has 33.2. The single highest mean sentence length in the set, 47.5, is
§10.4's 285-word paragraph — and that is the one paragraph this pass did not split, for
an unrelated reason.

**What makes these paragraphs long is sentence count, not sentence length: 9.0 against
3.3.** That is the finding's remedy vindicated by a different mechanism, and it makes the
work easier — nine sentences offer eight candidate seams, where five very long ones would
have offered four and each cut would have been a judgment.

## The one that was not split, and why

**§10.4's 285-word paragraph is the product of D-156.** P75 merged four paragraphs into
it — the EU paragraph, the US paragraph, the UK paragraph and the *which-structural-bet*
paragraph — on the author's own finding that *the EU/US/UK comparison can be one
paragraph*. `p75-scope.md` §"The EU/US/UK comparison, four paragraphs to one" is the
record.

**Splitting it would reverse a decision seven passes old without being asked to.** It is
left whole and the conflict is the author's to rule on. It is the only paragraph in the
book still over 200 words.

The record was searched for other deliberate merges before anything was cut. P29's is
§2.1.4's seven-strategy list, in a section P61 renumbered out of existence; P9's is in a
section this pass did not touch. **§10.4 is the only collision.**

## Splitting strands demonstratives, and it did

**Two paragraph openers had to be rewritten because the split put a pronoun across a
boundary from its referent** — P82's class, created by P83's remedy:

- **§3.1** *These are real, they work, and there is nobody home* → ***Those four** are
  real*. *These* pointed back nine sentences, to *constrained optimization,
  tamper-resistant training, capability ablation, a verified interlock*, and the split
  put two paragraph breaks between them.
- **§6** *Her account separates four ways a system produces the result* →
  ***Benjamin's** account*. *Her* was adjacent inside the paragraph and became a
  paragraph-opening pronoun.

**Both were caught by reading each new opener, not by a tool.** The check is now on the
record: after splitting, read the first sentence of every paragraph created.
`deixis.py --census` confirms the para-initial pool did not grow — 35 before, 35 after.

## Measurements

| | Before | After |
|---|---|---|
| Prose paragraphs | 880 | **930** |
| Mean, prose | 100.1 | **94.7** |
| Mean, all blocks | 102.0 | **96.6** |
| Over 150, prose | 125 (14.2%) | **107 (11.5%)** |
| Over 200, prose | 36 | **1** |
| Over 200, all blocks | 43 | **8** (7 lists and §10.4) |
| Longest prose paragraph | 433 | **285** (§10.4), then 199 |

**Fifty splits across 22 sections.** Book 90,491 → **90,492 words**, the one word being
*Those four* for *These*. **182 pages, unchanged**: 50 paragraph breaks add about half a
page of vertical space, and the book did not cross a boundary.

## What this pass did not do

**The seven list blocks over 200 words were left.** A numbered list of six frameworks is
not the reading experience the finding describes, and breaking one would damage the
parallel it exists to carry.

**Nothing was cut.** Every split is a paragraph break; no sentence was removed, and the
word count moved by one. The finding asked for splitting and not compression.

**The 107 paragraphs still over 150 words were left.** The finding named 200 as the
threshold to act on and 150 only as a count. Acting on 150 would be a second pass over
three times as many paragraphs, and it is not what was asked.

**The claim that this helps more than any amount of sentence-level editing was not
tested.** It is a comparison against work not done, and nothing here measures it.

**No new question was opened**, but §10.4 needs a ruling and is recorded above.
