# P64 — section 6.3.4 cut, the counterfactual sentence moved to 6.1.3

**The author's instruction.** Cut §6.3.4, *AI Explainability and Transparency*,
entire. Move the one live sentence — counterfactual explanation as the smallest
change that would have flipped the decision — into §6.1.3.

## The section read against the instruction before it was cut

Eight paragraphs, checked one at a time against the sections that would have to
carry what they said.

| Paragraph | What it was | Where it already lived |
|---|---|---|
| Opener | Explanation as an account to check a decision against, with the limit that an account can be produced after the fact | §6.3.3's closing paragraph, in the same words: *“The account is a claim to check against the process, not a window onto it”* |
| Definitions | Explainability vs. transparency, a medical-diagnostic example, a recidivism example | §6.1.3 treats both, and COMPAS is worked there and at §6.1.1 |
| Limits | Black boxes; transparency's cost in privacy, IP and exploitability; GDPR | The cost clause is in §6.1.3 verbatim in substance — *“expose proprietary methods and hand bad actors a clearer map”* |
| *Challenges* itemize | Four generically stated obstacles | Nowhere, and it is the capability-list shape `style.md` §2a names |
| LIME and SHAP | Already reduced to a pointer at §6.1.3 by P51 | §6.1.3 |
| Decision trees and rule-based systems | Interpretability built in, at a cost in predictive power | **Nowhere. Lost** |
| **Counterfactual explanation** | The sentence the author names | **Moved** |
| Visualization and tooling | t-SNE, UMAP, interactive inspection | **Nowhere. Lost** |

**The parent section's own map is independent evidence for the cut.** §6.3's
opener names verification and validation, the human who can intervene,
interruptibility, *“finding a failure before it reaches anyone, and repairing one
that already has,”* and risk past the task. That is 6.3.1, 6.3.2, 6.3.3, 6.3.5,
6.3.6 and 6.3.7. **6.3.4 is the one subsection of the seven the opener never
mentions**, and the opener needed no repair when it went — the two sections it
promises next now follow §6.3.3 directly. Chapter 1's roadmap describes chapter 6
by its four failure modes and does not reach subsection level, so it is untouched.

## Where the sentence went, and the one change to what was already there

Into §6.1.3's `Explainability Tools` run-in, **before** the block's closing limit
rather than after it. Placed after, it would have followed the paragraph's
strongest sentence — that a tool taking a bad target as given will *“report
nothing amiss”* — and deflated it.

That placement costs two words in the author's existing close. **“Neither tool …
Both take the training target as given” becomes “None of the three … All take.”**
The limit is true of counterfactual explanation and is arguably tightest there,
since a counterfactual over a model aimed at the wrong thing returns the smallest
change that flips the wrong prediction and reads as actionable advice while doing
it. The sentence itself loses its opening *“in a credit-approval system,”* the
credit setting having been established one sentence earlier.

## What the cut orphaned, and what was done about each

- **A glossary entry whose only locator was the cut section.** *Explainability
  and transparency* — *“two distinct properties the book insists on keeping
  separate”* — pointed at §6.3.4 and nowhere else. The claim still holds:
  §6.1.3 sets the two out in separate run-in blocks, and §9.3.2 defines both in
  one sentence, documentation an outside body can audit on one side and *“a
  deployed system account for its outputs precisely enough for a person to
  contest them”* on the other. **Repointed to §6.1.3 and §9.3.2 rather than
  cut**, which is the opposite call from D-112's on the AlphaGo Zero entry,
  because that entry's claim appeared nowhere in the manuscript and this one's
  appears in two places.
- **The LIME/SHAP glossary entry** loses its second locator; §6.1.3 carries it.
- **`europeanunion2016general`**, cited only here, moved to
  `unused_bibliography.bib`. `refs.bib` 309 → 308, unused 28 → 29; no other
  entry became uncited and nothing cited is missing.

## What was lost, named rather than smuggled elsewhere

- **The GDPR right to an explanation** — the requirement of an account of the
  logic behind an automated decision that significantly affects an individual.
  The book still treats the GDPR in §9.2, §10.4 and §5.4.1, all on a different
  key (`eu2016gdpr`) and none on this point. Nothing in the book cites or depends
  on it, so it goes as a fact rather than as an argument. **§9.2 is where it would
  go back**, in a clause, on a word from the author; it was not added here because
  the instruction moved one sentence and this would be a second.
- **Decision trees and rule-based systems as interpretable by construction.** No
  argument in the book depends on it.
- **Visualization, t-SNE and UMAP.** Same.

## A finding not acted on

§6.1.3 says *“Section~\ref{sec:9.3.2}'s discussion of transparency sets out what
transparency requires in general.”* §9.3.2 is *What Oversight Would Have to
Cover*, about research on candidate sentient systems, and its transparency
sentence is one clause inside a list of four principles. The pointer resolves and
the clause does say what §6.1.3 reports, so it is not Q-041's class; whether a
sentence in a sentient-research oversight section should be the book's general
statement of transparency is a structural question, not a defect, and is left.

## Figures

**95,965 words**, down 620 on P63's 96,585. The cut section measured **669** words
by `section_stats.py`'s own convention; the difference is the 49 words of the
moved sentence as it now stands in §6.1.3, two of them the widened limit's.
Chapter 6 goes 10,734 → **10,114**, 19 → 18 sections, and §6.1.3 468 → 517.
Both the cut and the addition are inside chapter 6, so its fall and the book's
are the same 620. **140 sections**, down 1. **191 pages**, down 2 from 193.
All `\ref{sec:}` 557 → **556**: seven references were repointed by the renumber
and one was removed with the glossary locator, against no addition — the moved
sentence carries none. Glossary locators 117 → 116. **[Corrected at P65: the glossary locators did not move. They were 117 at P63 and are 117 now — this pass removed the LIME/SHAP entry's second locator and added §9.3.2 to the explainability entry, netting zero. The one reference this pass removed was in the cut section's own body, its pointer at §6.1.3, and not a glossary locator, so the sentence above is wrong in its reason as well as its figure. The book-wide 557 → 556 is right.]** 0 undefined references, 0
undefined citations, `check_all.sh` green. Pages 78 and 81 were rasterized and
read: the counterfactual sentence in place, and §6.3.3 running straight into
*Anticipating Risk Before It Causes Harm*.

`renumber-map_2026-08-31d.tsv` translates 6.3.5–6.3.7 down to 6.3.4–6.3.6.
Anything in the planning record naming 6.3.4 before this pass means the cut
section; anything naming 6.3.5, 6.3.6 or 6.3.7 means one number lower now.

## Not done

- **The committed proof pair is stale**, and the README's page figure with it.
  The date has not rolled over, so a rebuild would be in place and the links
  would not move.
- **Five ledger rows tagged; all five were `drafted` already** and none moved
  status. **3 `accepted`, 137 `drafted`.** The author has not read §6.1.3 in its
  new form.
- **The three losses above were not checked against the wider literature**, only
  against this manuscript. The judgment is that no argument in the book needs
  them, not that they are unimportant.
