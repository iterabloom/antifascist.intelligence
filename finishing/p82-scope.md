# P82 — the bare demonstrative opening, censused, graded, and repaired where the referent is hard

**The instruction.** 272 sentences (8.1 percent) open with *That is*, *This is*, *It has
to be*, *They were*, no noun following. Where the preceding sentence runs 50 words and
carries three clauses the reader has to reconstruct what the pronoun points at. Naming
the referent costs two words. Mechanical, findable by search, and probably the
highest-value pass in the book.

**The count is right and the yield is not what the count implies.** The mechanical half
of the tell selects **299 sentences, 8.7 percent**, confirming the finding. The
discriminating half — *the preceding sentence runs 50 words and contains three clauses* —
is the author's own, it is stated in the same paragraph, and **it selects 18**.

## One of the two examples had already been cut

**\"They were written as the learned half sitting above the floor\" is not in the book.**
It was the seventh sentence of the introduction's roadmap paragraph, which P81 removed
about an hour before this finding arrived. The finding was written against the
pre-P81 text. Nothing else in it depends on that paragraph, and the other example,
§3.4's *That is refusal tracking its own rationale*, is live and is in the census.

## What the tell selects, in halves

`deixis.py` was built for this pass. Every hit is graded by what the reader has to do:

| Tier | What it is | Count |
|---|---|---|
| `para-initial` | opens its paragraph; the referent is in the paragraph before | 35 |
| `after-long` | preceding sentence 40+ words | 39 |
| `after-short` | preceding sentence under 40 words | 225 |
| | **mechanical pool** | **299** |
| | the author's condition, literally (50+ words, 3+ clauses) | **18** |

**The mechanical half selects 17 times what the author's own condition does.** This is
P79's finding arriving again in a different class, and it was found the same way — by
measuring the mechanical half before running it.

**`reader_tax.py` already carried a narrower version of this class**, 232 hits from one
anchored pattern, and D-117 recorded that most of that pool is fine. That prior holds:
22 instances of `after-short` were read and **none needed a noun**. In most the referent
is the whole of a short preceding sentence, which is what a demonstrative is for, and in
several — *The open research question is not how to build a more accurate classifier. It
is whether any face-to-feeling mapping survives* — the bare pronoun is the second half of
a deliberate contrastive pair that naming would break.

## The read, and the eleven of eighteen

All 18 were read in place. **Eleven were repaired and seven were kept**, each keep for a
stated reason.

| Repaired | Was | Now |
|---|---|---|
| §2.1.1 | That is evidence of who finds the floor inconvenient | **That pattern is** |
| §2.2.3 | That is not a system anyone has built | **That architecture is not** |
| §3.5 | That does not settle where the dial goes | **That arrangement does not** |
| §3.8 | That is slow renormalization | **That adjustment is** |
| §3.8 | That gives the vocabulary of leaving some of its purchase back | **That plasticity gives** |
| §5.1.3 | It requires no access to the model | **The ratio requires** |
| §5.3.2 | That puts the values into the system ahead of time | **That design puts** |
| §8.3.3 | That is evidence for exactly the embedded, paid, in-post training | **That contrast is** |
| §8.3.5 | That took a national government deciding | **That funding took** |
| §10.4 | It is a foundation binding AI law can be built on | **The convention is** |
| §11.2 | It is forgeable | **The identifier is** |

**Two more were taken from the adjacent tier** because the noun was sitting in the
previous sentence and the pronoun could bind to the wrong one: §4.2.2's *It is a
substantial simplification* → **The method is**, where the preceding sentence ends on
*the preference pairs themselves*; and §9.1.2's *It is a useful test case* → **The
coalition is**, where the nearest preceding nouns are *Amazon, Apple and Google* and then
*the commitment*, neither of them the referent.

**Thirteen repairs, thirteen words.** The finding's estimate of the cost was exact.

## The seven keeps, and why each

- **§2.1.1 *It is defeated by conflicts between duties*** — an `\item` in a list of six,
  each opening *It is defeated by*, the referent being the framework the item names in
  its first word. The parallel is the structure. Nine of the pool's hits are inside a
  list and six of them are this one series.
- **§2.3.2 *They are the instruments…*** — the referent, *the Three Rs and the pet-trust
  form*, is the last thing in the preceding sentence.
- **§3.5 *This is not deference installed as a rule but deference derived: …*** — the
  colon supplies the content locally, which is `style.md` §7's own test and the shape
  P80 found reverses most candidates.
- **§3.5 *That is a good reason not to believe such a scheme*** — the referent is the
  assurance's advance timing, and no noun of two words names it. The repair cost more
  than the defect.
- **§1 *That means some sections explain machinery a specialist already knows and others
  make demands a general reader will find heavy*** — self-repairing: the sentence names
  both halves of what *that* refers to.
- **§10.6 *That is a co-equal branch of government reduced to expense-account
  leverage*** — the figure is *what I have just described amounts to X*, and every
  candidate noun produces a category error (a provision is not a branch).
- **§10.6 *That is not an argument against democracy*** — an 82-word preceding sentence,
  and the referent is the whole argument rather than anything in it. A short disclaimer
  whose job is to be quick.

**Four of the seven keeps are shapes a wider sweep would have damaged**, which is the
argument against running the mechanical half.

## Measurements

| | Before | After |
|---|---|---|
| Mechanical pool | 299 (8.7%) | **286 (8.3%)** |
| `after-long` | 39 | **26** |
| The author's literal condition | 18 | **7** |
| Book words | 90,478 | **90,491** |

**The strict set is exhausted.** The seven that remain at 50 words and three clauses are
the seven keeps above, each with its reason on the record.

## What this pass did not do

**The 225 `after-short` instances were sampled at 22 and left.** Reading found none that
needed a noun. They were not read exhaustively, and the sample is the evidence.

**The 35 `para-initial` instances were read and none was repaired.** The referent of a
paragraph-opening demonstrative is the paragraph before it, and a noun that names a whole
paragraph is longer and vaguer than the pronoun — *That is the load-bearing claim of this
chapter*, *Those are detection targets*, *This would*. §11.3's three consecutive
paragraphs opening *It would need* are a deliberate anaphoric series on *a detector worth
building*, named one paragraph up; naming it three times would destroy the parallel.
**This is the one tier where the finding's two-word repair is not available**, and it is
12 percent of the pool.

**The remaining 21 `after-long` instances were read and two were taken.** The other 19
either explain themselves with a colon, continue a running subject, or sit in an
idiom — *That is why*, *That is the shape of the thing* — where the pronoun is not
standing in for a noun.

**No new question was opened.** The finding needed no ruling.
