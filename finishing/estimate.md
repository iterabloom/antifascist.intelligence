# Effort estimate

Built from the pilot's measured unit costs and the triage counts. Revise-only
(D-007), agent drafts and author accepts (D-001), author availability under two
hours a week (D-003).

## What the pilot measured

One section, §3.1.2.3.1.1, the *easiest* transplant in the set.

| | |
|---|---|
| Rounds to accept | **1** — accepted with edits, not returned |
| Author edits | 6, all one pattern (cut the announcing sentence) |
| Words: original → agent draft → accepted | 589 → 781 → **734** |
| Net growth | **+25%** |
| New citation placeholders | 5, plus 1 permissions item |
| Style rules that needed inventing mid-edit | 0 (one added *from* the author's edits, afterward) |

Two things this establishes. **The style sheet works** — the agent draft needed
no rule that did not already exist, and the author's edits were all one rule,
now written down, which should reduce edits per section going forward. And
**sections grow even when the fate is "replace"**: the length arithmetic in
`PLAN.md` §1 is a floor.

The number the pilot did **not** produce is wall-clock author minutes. The table
below is therefore parametric in that one unknown.

## The work

| Fate | Sections | Words | Author involvement |
|---|---|---|---|
| revise | 141 | 55,610 | full read, accept or return |
| fold | 101 | 46,870 | seam check only — the heading goes, the text stays |
| move | 13 | 6,001 | read once, in the chapter-7 context |
| cut | 9 | 3,552 | confirm the cut, do not read |
| merge? | 7 | 3,344 | decide which instance survives |
| fill-or-cut | 11 | 0 | write or delete a paragraph |

Plus: 16 transplants (inside the 141), ~273 citation placeholders to resolve,
and the D-013 cluster rulings.

## Author time, parametrically

The binding constraint is not agent capacity. It is that **every section needs
one careful author read**, and at under two hours a week that is the whole
budget.

| Minutes per section read | 141 revise | + 101 folds at ⅓ | + the rest | Total author hours | Weeks at 2 h |
|---|---|---|---|---|---|
| 5 | 12 h | 3 h | 3 h | **18 h** | 9 |
| 10 | 24 h | 6 h | 5 h | **35 h** | 17 |
| 15 | 35 h | 8 h | 7 h | **50 h** | 25 |
| 20 | 47 h | 11 h | 9 h | **67 h** | 34 |

Then add, outside the per-section reads:

- **Triage adjudication:** 270 rows still unruled, roughly 20–40 minutes a chapter → **4–6 h**.
- **Citation resolution (P4):** ~273 placeholders. Runs in a networked session, but the author spot-checks a sample and rules on what cannot be sourced → **5–10 h**, and this is the least compressible item.
- **Permissions (D-012):** three epigraphs plus the *Westworld* line now closing §3.1.2.3.1.1. Outside your control once the letters go out; start early → **2–4 h** of your time, unbounded calendar.
- **Front matter, method note, glossary (P5):** **3–5 h**.

**Realistic total: 30–85 author hours, so roughly 15 to 40 weeks at two hours a
week** — four months at the optimistic end, ten at the pessimistic. The spread is
dominated by one number, minutes per section read, which one more accepted
section will pin down.

## What would actually shorten it

Ranked by hours saved per unit of regret:

1. ~~**Cut more.**~~ Considered and declined (D-019, D-020): the length target was retired rather than the book cut down to meet it. The lever that remains is shipping some *fine* sections with a lighter read, which is the author's to pull and nobody else's.
2. **Batch the folds.** 101 seam checks reviewed a chapter at a time rather than a section at a time.
3. **Accept the citation ceiling.** If ~273 placeholders is too many to resolve, the rule from D-009 already covers it: what cannot be sourced is cut. Applying that aggressively converts citation hours into cut hours, which are cheaper.
4. **Do not add scope.** The transplant budget is 12k words; the pilot suggests the real cost of a transplant is not its words but the join paragraph that has to be written for each one.

## What the second pilot changed

T4 (mirror neurons → §2.2.1) was run precisely because it was the hard case: six
personal names to scrub, and a mode — `boxed-case` — the markup could not yet
express.

- **The name rule costs about a third again**, not double, and the cost is judgment rather than time. Three name instances needed three different decisions; a script can find them but cannot make the call.
- **Most of the overhead was one-time.** The `<<box>>` construct and two renderer fixes are now done for all sixteen transplants.
- **Two rendering faults passed every automated check** and were caught only by looking at the page. Budget a visual proof read per chapter, not per section.

So the per-section figures above stand, with a modifier: **the six transplants
carrying heavy name or second-person load cost roughly 1.3× a plain one**, and
the sixteen transplants together are perhaps two to three author-hours more than
the flat estimate implies. That does not move the headline range.

## Confidence

Moderate now, rather than low-to-moderate. Two sections, chosen as the easiest
and one of the hardest transplants in the set, landed within the same cost band.
The remaining unknowns are the author's minutes per section read — still the
dominant term, still unmeasured — and the transplants with heavy second-person
dependence (T5, T9), where the conversion loses force rather than names and no
pilot has tested that yet.
