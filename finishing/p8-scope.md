# P8 — second editorial review response

Opened 2026-08-23. Scope is the four items the author ruled on, and nothing
else. D-007 is lifted again for this pass only (D-033), on the same terms
D-029 set for P7: new prose where an item calls for it, no reopening of
sections the items do not name, every change disclosed per-row in
`ledger.tsv`.

The review arrived as prose, unnumbered. Its six items were checked against
the manuscript before any ruling was sought; two did not survive that check
and are recorded below as declined, with what the check found.

## The rulings

| Question | Ruling |
|---|---|
| Is there a P8, and is D-007 lifted for it? | **D-033** — yes, scoped to the four items below |
| The molar/molecular fork | **D-034** — branch (a): molecular fascism is fascism, not a precursor to it |
| May chapter 1 be reopened to surface the persistence argument? | **D-035** — yes; §2.4.4 retitled in the same item |
| May the false-positive argument move from §7.1.7 into §2.1.4? | **D-036** — yes |

## The items

**Four rulings, six rows.** D-033 scoped the pass to four items; the table
below has six. The difference is bookkeeping, not scope creep: the §2.1.4
work splits into the scale collision (P8-1) and the material moved forward
into it from §7.1.7 (P8-2), which D-034 and D-036 ruled on separately; and
§7.1.7's own rewrite (P8-3) is the other half of D-036. P8-6, the §2.4.4
retitle, was ruled on inside D-035 as part of the persistence item rather
than as a fifth item. Mapping: D-034 → P8-1; D-036 → P8-2 and P8-3;
D-033's third item → P8-4; D-035 → P8-5 and P8-6.

**What it cost, measured against `fa1a719`:** §2.1.4 +556 words (1,329 →
1,885), chapter 1's opener +160 (378 → 538), §7.1.6 +107, §7.1.7 +93 net
(about 250 words of the old false-positive block removed, about 340 of new
argument in), §5.1.1 +36, §2.4.4 +0 (title only). Book total +952, 83,932 →
84,884.

| # | Where | What | Done |
|---|---|---|---|
| P8-1 | §2.1.4 | **The scale collision, and branch (a).** The review's sharpest finding, and correct: every discriminating feature of fascism-proper (mass mobilization, leader cult, scapegoat, contempt for legality) is a property of a mass political movement, while an AI deployment exists only at the molecular scale. So at the scale the book's systems occupy, the discriminators are unavailable and only the four-feature signature remains — the signature §2.1.4 itself says "will flag every badly run organization on earth." The book had both halves and never collided them. New `<<h>>` block, "The scale problem, and what this book does about it," resolving on D-034's branch (a) and stating what that branch costs: on this reading "antifascist" names the political inheritance of a structural claim and does not mark off a narrow class a classifier separates from ordinary decay. The dilution objection is stated and answered rather than avoided. | yes |
| P8-2 | §2.1.4 ← §7.1.7 | **The weaponization asymmetry moved forward.** The half of §7.1.7's false-positive argument that the design chapters need to carry — a tool whose output is an accusation is a weapon handed to the actor it was built to constrain (§4.4.6's dual-use problem at its sharpest); the opposite failure supplies false assurance and is no safer; neither is fixed by better engineering, both are governed by what the tool may output and to whom. This is the reviewer's item 1a, taken as a split rather than the wholesale move it asked for — see "Taken differently than asked" below. | yes |
| P8-3 | §7.1.7 | **Rewritten around what actually remains.** The old false-positive block argued a precursor/unmistakable calibration tradeoff that branch (a) partly dissolves: firing on ordinary institutional decay is no longer miscalibration. Replaced with the problem that genuinely survives — separating a recuperated dissent mechanism from a merely mediocre one when both produce identical paperwork — plus a new observation the pass turned up: a records-based detector is most confident about the institutions that keep the best records, so its legibility bias runs in exactly the wrong direction. Opener and closer retuned to §2.1.4's new content. | yes |
| P8-4 | §2.1.4, §5.1.1, §7.1.6 | **The dissent through-line named.** The review's second-best item, and correct. Three places where a channel collects disagreement and is built so that none of it can move anything: recuperation as §2.1.4's first feature, the annotation pipeline in §5.1.1, RLHF's averaging in §7.1.6. They were three unconnected observations. Now each names the pattern where it appears. Deliberately **not** done with numbered cross-references in every direction — see the note on the review's internal conflict below. | yes |
| P8-5 | §1 opener | **The persistence argument surfaced.** Verified before acting: only three files in the whole manuscript contain the word "persist" (§2.4.1, §2.4.4, §7.1.6), and chapter 1 never mentioned it. One paragraph now names the book's two standards for itself — one hard question about machine subjects with an answer checkable from outside, one central term that does not yet cash out as an instrument — and tells the reader to carry both through the design chapters. This also delivers what the review's item 1a actually wanted (the limitation carried forward rather than discovered late) without moving §7.1.7 out of the chapter built for open problems. | yes |
| P8-6 | §2.4.4 | **Retitled** from "Establishing Guidelines for AI Subject Research and Consent" to "When Consent Is Inapplicable: Guardianship and Research Oversight." The old title advertised boilerplate over the argument the section actually carries. Live files updated: section heading, `ORDER.tsv`, `outline.tsv`, `ledger.tsv`, and the regenerated `table-of-contents.txt`. `section_stats.tsv` and `headings_reconcile.md` were regenerated and carry the new title. The historical reports (`triage.tsv`, `toc_v4.tsv`, `voice.tsv`, `redundancy_*`) keep the old one: they record what was true when they were generated, and were not regenerated. | yes |

## Taken differently than asked

**The review asked for §7.1.7 to move wholesale into §2.1.4.** It was split
instead. The premise was overstated — §2.1.4 already carried a forward
pointer saying naming the targets was the easy half, so the limitation was
never a discovery made in the errata — and a wholesale move would have
broken things: §7.1.7 leans on §6.6 (slope, not level), §7.1.6
(disagreement as signal), §4.4.6 (dual-use) and §4.1.4, all of which follow
chapter 2. Moving it entire would have created four forward references
inside a §2.1.4 that already ran ~1,400 words with a seven-item list. The
portable half — the part the design chapters must carry, which depends on
nothing downstream — went forward as P8-2. The dependent half stayed.

## Declined, with what the check found

| # | Review's item | Why declined |
|---|---|---|
| — | "The word choice is doing rhetorical rather than analytical work; the book should say so once, plainly" | **Already satisfied, by the author's own D-024 sentence.** §2.1.4's first paragraph reads: "The word is chosen deliberately: fascism is the narrower and more charged term, and I use it because it is more honest about the politics in which this book is being written — but the target is authoritarian power in every form." The review came close to quoting it back. Residue not acted on and named here rather than left implicit: chapter 1 uses "antifascist" without explaining the choice, so a reader meets the term in the introduction and gets the account in §2.1.4. That is a smaller point than the review argued and was not ruled on. |
| — | Cross-reference density: "at most one or two pointers per section" | **Already swept, and the review shows no sign of knowing it.** A8 cut numbered cross-references from 297 to 145 across 157 sections. Measured at the start of this pass: worst offenders are §6.6.4 (6 in 789 words), §2.4.4 (5 in 911), §5.2.3 (5 in 541), §6.7.6 (6 in 5,442, which is fine). Fifteen sections exceed the review's rule. The review names no instance; the section it most plausibly had in mind, §7.2.4, was deleted by A8 for exactly this defect. There is perhaps a session of thinning available in those fifteen. There is no structural problem, and the rule as stated conflicts with the review's own item 4, which asks for three sites to be connected. |

## The review's factual errors, recorded

- **"The book's most original contribution sits in a fifth-level
  subsection."** It does not. The persistence argument is at §2.4.1
  (established) and §2.4.4 (applied), both level 3, in chapter 2. There is
  no fifth level anywhere in the book; D-010 caps the outline at three. The
  substance of the suggestion survived the error and was acted on as P8-5 —
  the argument genuinely was unsurfaced — but the stated reason was wrong.
- **"7.1.7 admits it too late... arrives after three chapters have spent the
  capability."** §2.1.4 already pointed forward to §7.1.7 by number and
  said naming the targets was the easy half. The limitation was flagged
  where the capability was introduced. The item still had a real core, which
  is why P8-2 and P8-5 exist.

## Checks

`check_all.sh` green: round-trip, structure (headings, order, markup, ledger
parity, ORDER.tsv digests), named-persons guard. TOC regenerated;
`headings.py` reports ms-vs-outline title diffs = 0.

**D-025, honestly.** New prose was written against the contrastive-negation
calibration and measured after: §2.1.4 1 per 209, §7.1.7 1 per 258, §5.1.1
1 per 420, §1 opener 1 per 269 — all inside the 1-per-216-or-better band P7
worked to, except §2.1.4, which is 7 words outside it. §7.1.6 measures 1 per
136, and **that is not this pass's prose**: all four hits are in paragraphs
P8 did not touch, and the paragraph P8 added contains none. Left alone per
the Tier B precedent, and named here rather than reported as clean. Chapter
6's untouched density, flagged in `STATE.md` since C3, is still not fixed
and is still not claimed as fixed.

## Not author-accepted

Every item above is drafted, not accepted. §7.1.7 was already `drafted`
before this pass and stays that way. §6.7 remains `drafted` from P7 and is
untouched by P8.
