# P42 — the legal claims a second reader checked, and the cross-chapter contradictions behind four of them

**Author's instruction, 2026-08-29:** forwarded feedback that spot-checked
"several high-impact legal claims," two named as needing correction and five as
needing specialist review; then *"go"*, and *"and then proofs."*

**Decision row:** D-106. **Branch:** `pass/42-legal-claims-and-cross-chapter-contradictions`.

## The feedback, and the finding on each

| item | section | verdict | what was done |
|---|---|---|---|
| EU AI Act "does nothing" about government uses | 10.8 | **right, and an internal contradiction** — 6.4.3 records Article 5's ban on government social scoring and its limits on police biometrics | rewritten to the narrower true claim: the Act reaches public authorities, excludes military, defence and national security by its own terms — where 6.4.1's applications live — and is enforced against a member state's agencies by that member state |
| Council of Europe convention "binds a signatory" | 10.8, 12.1.2 | **right on the conclusion**; the reviewer's "no ratifications" is wrong — the EU deposited its ratification 15 May 2026 — but no primary source found says the threshold is met | "would bind a party, once in force, which at this writing it is not"; the EU ratification cited, with the bibliography note recording exactly what could and could not be reached |
| "Three companies," two named | 10.6 | **right — a defect from P3** (2026-08-23); the third was never in the text | "Two companies" |
| predictive processing "the dominant account" | 4.1.1 | right; 4.1.2 already frames it as a falsifiable bet | "the most ambitious unifying account … contested on exactly the question of whether one mechanism can carry this much," pointed at 4.1.2 |
| federated learning ensures nothing can be seized / updates reveal nothing | 6.4.2, 6.4.4 | **half right, and the right half is an internal contradiction** — 6.4.4's "structural limit on what a government can seize" against 6.4.2's own "can still demand raw data at the source" | 6.4.4 reconciled with 6.4.2; 6.4.2's "only that update" qualified with gradient leakage (Zhu, Liu and Han 2019, verified) |
| product liability applies "exactly" | 9.3.2 | right; whether software is a product is unsettled | the contested step stated, with the Restatement's tangible-property definition and the first AI case to reach the question (*Garcia*, M.D. Fla. 2025) |
| "a system that can say why it decided is a system whose failures are visible" | 6.3.3 | **right, and the book's own stronger argument is against it** — 11.1, 4.2.5, 2.4.1 | "contestable," not "visible," with the limit stated and the two sections cited |

## The class

Four of the seven are one chapter stating flatly what another chapter has already
qualified: 10.8 against 6.4.3, 6.4.4 against 6.4.2, 6.3.3 against 11.1, and
12.1.2 against 10.8's own previous sentence. That is Q-041's shape in a new
form — not a reference resolving to a weaker target, but a claim made without a
reference to the section that weakens it. No tool finds it; Q-043 records it.

## Numbers

91,443 → 91,785 words by `section_stats.py`; 187 pages, unchanged;
cross-references 798 → 803; four bibliography entries added. Sections 4.1.1,
6.3.3, 6.4.2, 6.4.4, 9.3.2, 10.6, 10.8, 12.1.2.

## What was checked, and what was not

Checked: the AI Act's scope against the EUR-Lex summary (public and private
sectors; military and defence excluded; law enforcement, migration, justice and
benefits as high-risk; social scoring banned; police live biometrics
restricted). The convention's status against every source that could be
reached — the Council's own treaty chart returned 403 on three URL forms, and
the bibliography note lists what stood in for it. *Deep Leakage from Gradients*
against arXiv and dblp. *Garcia* against two reports of the order; the order
itself was not opened and the docket number is omitted. `check_all.sh` green;
PDF clean, zero undefined references, all four keys in the `.bbl`.

Not checked: the Restatement (Third) §19 wording against a database — cited
from its standard text; whether the Act's national-security exclusion (Article
2(3)) is worded exactly as the book paraphrases it — the summary confirms
military and defence and the book adds national security from the regulation's
own text as remembered; whether other chapters make the federated-learning
overclaim beyond 6.4.2 and 6.4.4; the HTML build, which the proofs will do.
