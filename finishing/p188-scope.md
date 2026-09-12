# P188 — the af0f127/07ccef5 comparison, and the repairs it produced

Author instruction: **compare the manuscript at `af0f127` with the manuscript at
`07ccef5`**, then, on the findings, three follow-up instructions — restore one
title, cut one sentence, and repair the places where surviving text rests on
material the September 12 return cut, keeping the book lean.

This pass reads in the opposite direction from P187. P187 applied the return and
made the structure consistent around it. This one asks what the cut left behind
in the text that was not rewritten.

## What the comparison measured

Both trees were extracted and compared whole: every section file read or diffed,
per-section and per-chapter word counts, the renumber maps checked against the
files, the full bibliography delta, and every cross-reference from an untouched
chapter into a rewritten one read against its new target.

| | af0f127 | 07ccef5 |
|---|---|---|
| Sections | 132 | 90 |
| Words | 110,747 | 66,845 |
| Pages | 214 | 142 |
| Cross-references | 315 | 238 |
| `refs.bib` entries | 341 | 210 |

The word and page figures are **−40 percent and −34 percent**, not the −42
percent `STATE.md` and `PLAN.md` still carry: those were written before the three
restoring commits of September 12, which put five and then seven passages back.

**The bibliography total is conserved exactly.** 401 entries across `refs.bib` and
`unused_bibliography.bib` at both commits, 131 moved from cited to uncited, **none
authored**. Standing rule 1 held through the whole trip.

## How much of the book is new prose

Measured as the share of each chapter's surviving sentences over 60 characters
that appear nowhere in the old text:

- **New prose: chapter~3 (99 percent), 4 (100), 5 (100), 11 (87).** Rewritten, not
  compressed.
- **Partly rewritten: 10 (38), 6 (32), 9 (31).** Surviving sections largely kept,
  others cut wholesale.
- **Essentially untouched: 7 and 12 (0), 8 (3), 2 (6), 13 (12).** Their only
  changes are renumbering, two rewritten forward pointers, and the §8.3.4
  restorations.

Whole book: **44 percent of surviving sentences are new.** This independently
confirms D-288's figure and extends it past the restorations.

## The six places surviving text rested on cut material

Every one resolves, and `check_all.sh` passed on all six. **A reference can
resolve and still credit its target with a claim the target no longer makes**,
which is the gap `check_xrefs.py` disclaims and `xref_content.py` reaches only
where a sentence names a proper noun, acronym or year. Four of the six name none,
so the tool found neither them nor anything else real — its 13 candidates on this
tree were read and all 13 were false positives.

**Five were attribution rather than argument**, so the repair was deletion and
the book got leaner. That is P110's default: drop the number, let the sentence
carry the claim. Restoring all six targets instead would have cost about **2,850
words and fifteen bibliography entries**.

| Where | What it claimed | Repair |
|---|---|---|
| §12.2.1 | "the only one of §3.2's three gaps" | The new §3.2 enumerates no gaps. → "the only gap here" |
| §2.3.2 | "the same property that §11.2 values in it" | The new §11.2 does not mention a trust. Clause cut |
| §13, *democratic dividend* | cites §10.2 | The argument was in the old §10.2. Repointed to §12.1.1 alone |
| §9.2 | "§11.2 argues that a continuing record…" | The new §11.2 does not. Asserted in §9.2's own voice and folded into the sentence before it |
| §12.1.2 | "the one framework convention… which §10.4 reaches" | **The author ruled the count kept.** §10.4 gains a paragraph naming the convention, so the pointer is true again |
| §12.3 | four levers, and three safeguard categories | Lifted from old §6.3.4; two of four cases gone, all three categories cut. Rewritten onto surviving cases |

**§12.3 was the only one that needed writing.** The book's final section argues
that what separates a real commitment from a stated one is what a party has
already paid, and its evidence was a near-verbatim lift from old §6.3.4's closing
sentence. Proctorio and the WhatsApp forwarding limit are not in the book now.
Substituted from chapter~6: Ofqual's five-year non-disclosure agreement and the
reversal that followed, *Bartz* on acquisition, and the use policy held through a
threatened contract termination, a supply-chain-risk designation and litigation —
which sits directly under the sentence about having already paid. The NAACP suit
over the Memphis turbines was considered and left out: it is pending, and the
plaintiff is an organization rather than the residents, so listing it among fixes
would have overstated it twice.

**One restoration, and it is the author's ruling.** `coe2024framework` and
`coe2026euratifies` moved back so §10.4 carries the Framework Convention.
`refs.bib` 210 → 212, all cited; unused 191 → 189; total 401.

## The two prose instructions

**§4.3 retitled** *It Takes a Village to Deploy a Self-Aware Email Server*, the
author's own title, given to the old §5.4 at D-262 and removed by the return. It
did not go back to §5.4: that number now carries evaluator independence, and the
subject moved to §4.3. The Bronfenbrenner rings paragraph was **not** restored
with it — the proverb does not need the citation, and the new §5.1 disclaims the
developmental framing the rings would reintroduce.

**§5.1's closing disclaimer cut**, 26 words. It is the residue of old §5.1.1, 942
words arguing the Kohlberg critique on three fronts with three sources now in the
unused file. As a summary it had nothing left to summarise, and as an assertion it
restated the *only* already in the sentence before it. Its third clause is the
chapter's own later argument, made properly at §5.3 and §5.5.

## Found and not repaired

- **Both sentences `style.md` §1 protects as the author's own voice are gone.**
  *We need nothing beyond reasons-responsive refusal* and *the route by which we
  achieve reasons-responsive refusal*, ruled part of the book's voice at D-198 and
  Q-079 with the instruction "Do not report it, and do not recast it." Neither
  survives anywhere in the manuscript, and `style.md` still carries the rule.
- **The irreverent title register of D-261 was partly reversed**, and the book is
  now mixed. Chapter~0 from *Sup* to *Foreward*, still misspelled; chapter~1 from
  *This Is a Long-Ass Book With No Protagonist and No Personal Anecdotes*;
  chapter~11 from *Everything I Couldn't Figure Out, Ranked*; §6.1 from *Garbage
  In, Bigotry Out*. Chapter~12's survive.
- **The book reversed its position on the developmental material without saying
  so.** Old §3.10 held that the growth mindset and the developmental sequence
  "turn out to be the material the floor is made of." The new §5.1 treats the
  distinction as a taxonomy only.
- **Global inequality is gone with nothing left behind.** Old §10.5, *Built for
  the Rich Parts of the World*, was cut, and the new book contains no mention of
  the global South, low-income countries, or the connectivity gap.
- **Two named book concepts were retired with their sections**, the *moral
  ecosystem approach* and *humane values*, and their glossary entries with them.
- **§12.2.2 names four instruments with no citation anywhere in the book** —
  Perspective API, the Carnegie surveillance index, the UNESCO Recommendation, and
  vTaiwan, whose source went to the unused file. Against `style.md` §6, which
  wants an endnote for a named system or instrument.

## What was not checked

The new prose was read for what it asserts, **not as an editor** — no judgement is
recorded here on whether it is better prose. **No citation was verified against
its source.** `claims.py`, `epigram.py`, `xref_shapes.py` and `negatives.py` were
not rerun, and the two `xref-paragraphs` hand reads remain keyed to paragraphs
that no longer exist. **`QUESTIONS.md`'s forty-one open questions were not checked
against the new structure**, a second pass after P187 left them unchecked. And the
defect hunt ran **from surviving text toward cut material**, which is the opposite
direction from auditing the new chapters~3, 4, 5 and 11 for claims that are newly
unsupported. Nobody has done that.

## The record

The three commits between P187 and this pass — `c8b1a97`, `c0b24bd` and
`0fcf381`, which made seven mechanical repairs and restored twelve cut passages —
**have no `DECISIONS.md` row, no `STATE.md` lead and no scope file**, and each says
so in its own message. They are recorded in their commit bodies only. This pass
does not retroactively author rows for work it did not do.

`ledger.tsv`'s decisions column now carries D-289 on the eight rows this pass
touched and **remains silent on D-259 through D-288**.
