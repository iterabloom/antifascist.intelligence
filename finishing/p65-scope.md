# P65 — section 6.1.2 cut to its one live sentence

**The author's finding.** §6.1.2, *Ensuring Fairness and Equity in AI
Decision-Making*, is 295 words under three domain heads — Hiring, Credit
Scoring, Healthcare — each a paragraph of unobjectionable generality. The Amazon
résumé tool is narrated here and again in §6.3.5 as an example of something else.
The only sentence doing work is the one about a rejected applicant's right to
know why, which sets up §6.1.3. Cut to that sentence.

**Every part of it holds.** The section measures **285** words by
`section_stats.py` rather than 295, which changes nothing. The three heads are as
named. The one live sentence is as named. **The second Amazon narration is now
§6.3.4, not §6.3.5** — P64 renumbered it yesterday's numbering ago, and the
finding was written against the numbering before that pass.

## What the instruction did not name, and had to be repaired with it

**The Reuters citation was in the cut section and nowhere else.**
`dastin2018amazon` appeared once in the book, in §6.1.2. §6.3.4's narration —
*“Amazon's own résumé-screening tool, scrapped after the company discovered
internally that it had learned to downgrade résumés containing the word
‘women's’”* — carried no source of its own. Cutting §6.1.2 and stopping there
would have left a named company accused of a documented failure with nothing
behind it, and moved the citation to `unused_bibliography.bib` as uncited.

**The citation moved with the narration that survives, and two details came with
it**: the penalized phrase, and the two all-women's colleges. §6.3.4 goes 925 →
939 words. That is the whole of the addition; the narration's own framing —
Amazon as the case where anticipation worked, if slowly — is untouched.

This is D-123's class arriving from the other direction. There the cut severed a
description from the cross-reference that would have corrected it. Here it would
have severed a claim from its source. **Both are invisible to the tools**, which
begin from a reference or a citation that still exists.

## Two structural checks, both clean

- **§6.1's opener does not map its children.** It names three fronts —
  representation in training data, transparency in algorithmic decision-making,
  continuous performance evaluation — and then develops all three in its own
  body. Nothing in it named the cut section, so it needed no repair. This is the
  check P64 established after §6.3's opener turned out to be the evidence for
  that cut.
- **§6.1.1's *“the entries below are not the whole list”*** refers to its own
  run-in heads — Data Collection, Data Labeling, Target and Label Choice,
  Algorithm Design, Implementation — and not to the subsections under §6.1. Read
  rather than assumed, because a sentence naming the book's own structure is the
  class P59, P61, P62 and P64 each turned up one of.

**No `\ref{sec:6.1.2}` existed anywhere in the book**, and no glossary entry
pointed at it.

## Where the sentence went, and why not where the instruction reads literally

Into the close of §6.1's post-deployment paragraph, whose previous sentence
already names credit-scoring and hiring systems, so *“a rejected applicant”* is
anchored without the cut section's *Credit Scoring* head:

> …which is what regular audits of credit-scoring and hiring systems are for. **A
> rejected applicant has a right to know why, which is what the explainability
> tools of section~\ref{sec:6.1.2} make possible.** And involving the people an AI
> system's decisions affect…

**Not into §6.1.2 itself**, the section it points at. The finding says the
sentence *sets up* §6.1.3, and a sentence absorbed into the section it sets up
stops setting anything up — the pointer becomes self-reference and the sentence
becomes part of what it was introducing. At the close of §6.1 it still stands
before what it announces. **One word moves it** if that reading is wrong.

Taking *“cut to that sentence”* literally — §6.1.2 surviving as its one
sentence — would leave a numbered subsection of 22 words, the thinnest in the
book by a wide margin and several times under the 230-word threshold Q-029
tracks. That is why the section went and the sentence moved.

## What was lost, named rather than repaired

**The book's only statement of formal group-fairness criteria.** Equalized odds,
equal opportunity, fairness-aware learning, re-sampling, re-weighting, fairness
constraints on an output, and adversarial training against a protected-attribute
predictor appear **nowhere else in the manuscript** — the adversarial training in
§6.2 is the robustness technique, a different use of the term. Nor does transfer
learning or domain adaptation as a remedy for thin data on a population; the
glossary entry for those terms points at §4.1.3 and §4.2.9.

**This costs an antecedent.** §6.1.1 says target-choice bias *“is invisible to
every method that takes the target as given, which is most of them.”* After this
cut the only named instances of *most of them* are LIME and SHAP in §6.1.2, which
are explainability tools rather than fairness methods. The claim keeps two
instances and loses the family it was mainly about. **Not repaired**, because
repairing it means writing back some part of what the instruction cut.

**And the accuracy-versus-fairness tradeoff goes with it** — *“weighing accuracy
against fairness explicitly rather than optimizing for one and hoping the other
follows.”* P64 cut the accuracy-versus-explainability tradeoff out of the old
§6.3.4 the day before. **The book now states neither tradeoff anywhere**, which
is a two-pass effect neither pass would show on its own.

## A correction to P64's record

`p64-scope.md`, D-145 and `STATE.md` all report the glossary going **117 → 116**
locators. **It did not move.** It was 117 at P63 and is 117 now. P64 removed the
LIME/SHAP entry's second locator and added §9.3.2 to the explainability entry,
netting zero. The single reference P64 removed was in the **cut section's own
body** — its pointer at §6.1.3 — and not a glossary locator, so the sentence
explaining the fall is wrong in its reason as well as its figure. The book-wide
total, 557 → 556, was right.

## Figures

**95,714 words**, down 251 on P64's 95,965: the cut section 285, less 20 words
into §6.1 and 14 into §6.3.4. **139 sections**, down 1. **190 pages**, down 1.
Chapter 6 goes 10,114 → **9,863**; §6.1 892 → 912, §6.3.4 925 → 939. All
`\ref{sec:}` **556, unchanged** — one out with the cut section's pointer, one
added in §6.1 — with the glossary **unchanged at 117**, three of its locators
renumbered. `refs.bib` **unchanged at 308**: the citation moved rather than being
orphaned, and no entry became uncited. 6.1.3 renumbers to 6.1.2, with
`renumber-map_2026-08-31e.tsv` translating. 0 undefined references, 0 undefined
citations, `check_all.sh` green. Printed pages 75 and 81 rasterized and read.

## Not done

- **The proof pair was rebuilt in place afterwards and is current**, the date not
  having rolled over: 190 pages, 0 undefined references and 0 undefined citations,
  1,039 internal links over 1,545 ids with none broken and none duplicated. It
  covers P64 and P65 together, both having been stale.
- **Four ledger rows tagged; all four were `drafted` already.** **3 `accepted`,
  136 `drafted`.**
- **The surviving Amazon narration was not re-verified against the Reuters
  article.** The citation was moved because the cut section carried it for the
  same claim, not because the source was opened here. The two details added to
  §6.3.4 are the cut section's own wording.
