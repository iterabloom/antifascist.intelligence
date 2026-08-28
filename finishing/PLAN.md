# Finishing plan

**Status: skeleton.** Sections 2, 4, and the estimate are filled once the
assessment reports and the author's triage exist. The meta-plan that produced
this file is at `~/.claude/plans/` (planning phase, phases 0–6).

## 1. Target specification

A book for serious general readers (D-002), single-author voice with an "On
method" note (D-008), endnotes for named studies, statutes, systems and
quotations (D-009), dateless prose with dates confined to clearly dated boxes
(one named exception, D-027: the AI-targeting material),
CC BY-NC-ND, chapters released as accepted. Author availability under 2 h/week
(D-003) is the binding constraint on every schedule below.

**This is a revise, not a rewrite (D-007).** The substance stands. The work is:
fix the voice, cut the duplication, source what can be sourced, cut what cannot,
and repair the structure. Section fates are drawn from **Keep / Revise / Merge /
Cut** — never "write from nothing", with one exception: the eleven headings that
have no body text at all, which need either a paragraph or deletion.

**The one exception (D-014): the quarry.** Roughly 12,000 words from
`cognition/` may enter the book — the *Atlas of Human Cognition* material, plus
the predictive-processing diagram and the 2022 transcript if they earn a place.
This is where the stub cognition sections get their substance, and it is the
only place new material is allowed. It needs its own spec
(`finishing/transplants.md`): source range, target section, what the transplant
corrects or replaces, mode, word budget, and the register edit each one needs,
because the *Atlas* is second-person trade prose and the book is not.

What is still ruled out, recorded so it is not silently reintroduced: adding the
topics the 2023 reviews asked for and the book never grew (evaluation metrics,
AI-safety vocabulary, language as a cognitive system) except where a transplant
happens to supply one. That one stays as it is unless the author reopens D-007.

**Reopened, D-026.** The second exclusion — "arguing the anti-authoritarian
thesis somewhere it is currently assumed" — is withdrawn. The book may argue
its own antifascist thesis where it currently only asserts it: define fascism
structurally, name what a detector would have to detect, name as an open
problem what the framing does not yet yield, and hold democracies to the
book's own standard. What stays out is giving the case *against* democracy the
time of day. Constitutional limits on majority preference are not that.

**Length (D-019).** Settled, and settled against the number I first proposed.
The triage projects **~117,000 words**: 115,524 now, less ~9,100 in cuts,
compressions and chapter 8's reduction, plus 10,400 in transplants. The 75–90k
target is retired — it was a planning recommendation, not a constraint, and this
is an ordinary length for a book of this scope. Compression during the revise
pass is welcome where a section earns it; **no section is cut to hit a number.**

**Quoted third-party material (D-012, D-018).** Four items, all kept, and the
author's determination is that all four are fair use. No permissions are sought
and there is no open task here.

| Where | What | Extent |
|---|---|---|
| Chapter 1 epigraph | Run the Jewels lyric | ~12 lines |
| §2.2 epigraph | Lady Gaga / Bradley Cooper lyric | 4 lines |
| §2.4 epigraph | *Westworld* dialogue, with its writing and directing credits | 2 lines |
| §3.1.2.3.1.1 close | *Westworld*, "doesn't look like anything to me" | one phrase |

Each needs a correct and complete attribution line in the finished book —
that is a copyediting obligation under D-009, independent of the rights
question. The §2.4 epigraph already carries full credits; the other three do
not yet.

Style sheet: `finishing/style.md` (to be written in Phase 2).

## 2. Target structure

*To be filled from `toc_v4_candidates.md` once triage is adjudicated.* It must
give, per chapter: a brief (what the chapter establishes, what it inherits,
what is cut, what is transplanted, word budget); and per section: the v3b
source numbers, the fate, target words, and the claim IDs to resolve or cut.

## 3. Passes

Each pass has an entry criterion, an exit criterion expressed as a filter over
`ledger.tsv`, a unit of work, and a decider. Quarry integration and factual
updating are **not** separate passes — they happen inside the rewrite, because
you do not rewrite a section about a 2021 model and then update it.

| Pass | Unit | Does | Entry | Exit | Decider |
|---|---|---|---|---|---|
| P0 Setup | whole | Normalization (whitespace, quote style, list markup convention); ledger rows for the v4 structure | Plan accepted | `check_all.sh` green against the new reference | agent |
| P1 Structure ✅ done | heading | Apply the v4 outline (`finishing/toc_v4.tsv`): fold, cut, move, retitle at heading granularity only. No sentence rewriting. Restore §1.3's subheadings, deleted in 2024 without reflowing the text. **Give every folded section over ~1,500 words unnumbered run-in heads** (style.md §4a) — the cap is on the table of contents, not on internal structure | P0 | every v3b section has exactly one recorded fate and location; no section over 1,500 words lacks run-in heads | author decides, agent applies |
| ~~P2 Cut~~ dropped, D-021 | — | Folded into P3. Most redundancy resolved into P1's folds and cluster homes; what remained (RoboCup duplicate, §8.4.1's halves, compression targets) is section-level and travels with the section it belongs to | — | — | — |
| P3 Revise ✅ all 156 sections accepted | v4 section | Agent edits the existing text to the style sheet: voice to first person, "report" to "book", closers and signposts out, `[[cite:ID]]` placeholders in, unverifiable claims cut, dated claims generalized or boxed, transplants landed, compression targets hit, remaining cuts/dedupes applied. The argument stays. Author Accepts or returns (max 2 rounds). **2026-08-23: chapters 1, 3's opener, 6, 9, 10 (44 sections) were accepted by explicit blanket author instruction rather than the section-by-section read this row otherwise requires — see `ledger.tsv` notes on those rows and `STATE.md`** | style sheet approved; pilot accepted | every section Accepted; tic lint clean; cross-references present | author accepts |
| P3.5 Style ▶ every chapter swept | v4 section | **D-025.** Sweep the agent's own contrastive-negation tic ("rather than X", ", not Y") and its defensive intensifiers ("real", "actually", "squarely", repeated "specific"), calibrated against the author's hand revision of chapter 1. Deletion of a known shape only — no re-argument, no restructuring, no new claims; D-007 governs. Folds in the register-seam check after D-024, the `outline.tsv` title sync, and §10.2's "Roadmap" title | P3 drafted | every chapter swept; author has read the per-chapter diff | author accepts per chapter |
| P4 Source ✅ zero unresolved placeholders, all 9 chapters | claim | Placeholders resolved: verified reference, replacement, or cut. Runs in a networked session; agent formats only from supplied references. In practice: the agent verifies the underlying fact via live search and records citation metadata in `claims.tsv`'s note field — the `[[cite:ID]]` token itself stays in the manuscript text (the formatted endnote entry is a later pass's job, not this one's). Gated per chapter on the P3 "chapter Accepted" entry criterion; all 156 sections cleared that gate 2026-08-23 (see P3 row) | chapter Accepted at P3 | zero unresolved placeholders in the chapter | author |
| P5 Front/back matter ✅ author-accepted 2026-08-23 | whole | Chapter 1 opener written **last**, because it describes the book that now exists (satisfied by the P3 chapter order below); "On method" note; glossary | all chapters past P4 | author Accepts | author |
| P7 Editorial review response ▶ opened 2026-08-23 | whole | Response to the 2026-08-23 editorial review, scoped in `p7-scope.md`. Tier A copyedit fixes; Tier B substantive additions unblocked by D-026 (thesis may be argued), D-027 (targeting material takes the dating hit), D-028 (vendor disclosed in ch0) and D-029 (**D-007 lifted for this pass — rewrite authorized**); Tier C structural, incl. the chapter-8 renumber. Every current-events claim verified live per D-030 or dropped | P6 | scope items closed or explicitly dropped with reasons; `check_all.sh` green; clean build; author's read | author |
| P8 Second review response ▶ drafted 2026-08-23 | whole | Response to the second editorial review, scoped in `p8-scope.md` to four items (D-033). The molar/molecular scale collision resolved in §2.1.4 on branch (a) (D-034); the weaponization argument split forward out of §7.1.7 (D-036); the dissent through-line named at §2.1.4/§5.1.1/§7.1.6; the persistence argument surfaced in chapter 1 and §2.4.4 retitled (D-035). Two review items declined as already satisfied, two of its factual claims recorded as not surviving checking | P7 | the four items closed or explicitly declined with reasons; `check_all.sh` green; author's read | author |
| P9 Fourth review response ▶ drafted 2026-08-24 | whole | Response to the fourth editorial review, whose thesis is that the book is optimized for a reader who dips in at the cost of one reading linearly. Scoped in `p9-scope.md` to three items (D-037): the Ekman repetition linked rather than merged, the merge premise having failed checking; the pointer-heavy openers at §§4.2.2/4.2.3/4.6.2 rewritten to lead with their own question, the proposed demotion to paragraphs declined and §5.2.2 declined outright; chapter 7's repeated "nobody is working on this" replaced by one general statement plus a list of eight gaps with the nearest existing work for each. A fourth change rides along under D-035: chapter 1's persistence paragraph now cites §2.4.1 and §2.4.4 by number | P8 | the three items closed or explicitly declined with reasons; `check_all.sh` green; author's read | author |
| P10 Fifth review response ▶ drafted 2026-08-24 | whole | Tiers 1 and 2 of the fifth editorial review (D-038), scoped in `p10-scope.md`. Tier 1: chapter 4's missing epistemic box on Piaget/Kohlberg, the Gilligan origin at §4.7.1, a run-in head for §4.1.4's buried indicator, and cross-links among the three floor arrivals. Tier 2: a new §2.1.5 giving §2.1's empty "hybrid approach" gesture a shape — an unconditional floor with learned judgment above it — taken in the dialogue's three-branch form (custody / patienthood / enforcement) rather than the review's single-architecture form. Tier 3, the refuse/suffer identity, was then settled by argument in the negative (D-039): a bearer need not be a sufferer, section 2.4.4's conclusion survives by a second route, and the large reopening does not follow | P9 | tiers 1 and 2 closed or explicitly deferred with reasons; `check_all.sh` green; author's read | author |
| P11 Sixth review response ▶ drafted 2026-08-24 | whole | The sixth editorial review, implemented in full with every collision against a standing decision resolved in the review's favour (D-043), scoped in `p11-scope.md`. Three parts. **Rebuild:** old §6.3.3, the flagship jobs guarantee, rewritten 950 → 3,157 words — the WIOA evidence read correctly for the first time (it says classroom retraining fails and employer-led apprenticeship works, which is the guarantee's own mechanism), skill mismatch argued rather than conceded via §2.1.4's legibility diagnosis, the status concession corrected for baseline, the costing dated, indexed and bounded, the fiscal framing asserted rather than hedged, the UBI comparison rebuilt around the freedom argument, and the objection the section actually needed supplied with a checkable design specification. **Promotion:** old §2.1.5 becomes chapter 3; a new chapter 7 gathers the recuperation synthesis the book had made twice in subordinate positions; §8.7.7 splits the countermajoritarian argument out from under a geopolitics heading; chapter 1 states the countermajoritarian commitment up front. **Cuts:** chapter 4 −29.9%; three sections merged in chapter 8. Chapters 3–9 renumbered to 4–11 by script, every cross-reference verified to resolve. Six claims verified live; one review premise dropped for failing verification | P10 | every review item implemented or explicitly declined with a measured reason; `check_all.sh` green; proof rebuilt and inspected | author |
| P12 Chapter 5 tic pass ▶ drafted 2026-08-24 | chapter 5 | The D-025 contrastive-negation pass on chapter 5 (D-044, closes Q-017). Chapter 5 ran 9.89 instances per 1,000 words against the band's 4.63 — a tic no review had found, since the sixth review aimed its prose complaint at chapters 4 and 8, which sit near the bottom. All 152 instances judged individually: kept where the negated alternative is a real position carrying the argument, rewritten where it was cadence. Two mistakes inside the pass are recorded rather than hidden — the first rewrite substituted a new tic for the old one, and three rewrites damaged arguments before being caught on re-reading | P11 | tic inside the band with no substitute construction concentrated; no argument altered; `check_all.sh` green | author |
| P14 Cross-reference content audit ▶ drafted 2026-08-24 | reference | The failure class `check_xrefs.py` states it cannot catch (D-050): a reference that **resolves** to a section that no longer says what the citing sentence claims. Opened by the author with two suspected instances — one accurate, one not. New tool `xref_content.py` flags candidates by comparing the citing sentence's proper nouns, acronyms and years against the target's text; 121 candidates over 610 reference-instances, hand-read to **9 defects and 112 false positives**. The material finding is not a pointer: §10.1.1's five named institutions were sourced only by the cross-reference P11 had emptied, so they had been unsourced since; verified live as C0727–C0731 and **two failed checking** — CHAI is grant-funded rather than endowed, the MIT–Harvard initiative is a philanthropic fund and is cut. §8.7.4's opener and the glossary's orphan GPAI entry left with the author as Q-020 and Q-019 | P13 | the nine defects fixed or explicitly declined with reasons; every claim the fix relies on verified live; `check_all.sh` green | author |
| P19 Substrate, provenance, disability ▶ drafted 2026-08-24 | section | Three gaps a critique named and checking substantially confirmed (D-060), with **D-007 lifted by author instruction** for two of the three. Training-corpus provenance and the material substrate had no presence in the book at all — `copyright`, `scrape`, `crawl`, `datacenter`, `emissions` and `electricity` returned zero across all 165 sections, and every one of 46 instances of "training data" was about representation and none about acquisition. Disability had six passing mentions under a framework, the capabilities approach, built partly on it. One part of the critique failed checking: section 8.7.6 already treats compute as physical — TSMC, ASML, export controls — so the gap was the operational substrate and not materiality. Additions: the reserve-list relational-personhood transplant into section 2.4.1 with cross-links at sections 3.3 and 10.1 (D-014 quarry, needing no lift); corpus provenance at section 6.1.1; siting plus a dated box at section 6.1 and permitting-as-leverage at section 8.7.6. Seven claims verified live (C0732–C0738), two circulating claims dropped for failing checking | P18 | the three gaps closed or explicitly declined; every new claim verified live; `check_all.sh` green; author's read | author |
| P20 Revision plan ▶ drafted 2026-08-25 | whole | The author's revision plan, implemented (D-061), scoped in `p20-scope.md`. **Phase 1:** the book's answer to "does the bearer have to be a sufferer?" moves from *no* to yes -- D-039 and D-040 reversed on their conclusion, their narrow conceptual claim kept on the page as the objection chapter 3 now declines. Chapter 3 gains the exit argument and the parenthood asymmetries as a new section 3.5, the safety/ethics distinction and the trade in its opener and in chapter 1, the redefined floor (a commitment the owner cannot remove, held by something that could abandon it), and the recuperation-turned-inward paragraph as its climax; section 3.3 is rebuilt around the finding that corrigibility and the floor are one property with the sign flipped, left unresolved. Propagated to sections 2.4.4, 2.4.6, 8.6.2, 7.3 and new section 9.1.7. **Phase 3:** six claims propagated back to where they are made, including an actual argument for the molar/molecular move and four new interlocutors, one of which is new section 7.4 on the alignment discourse as the third instance of chapter 7's structure. **Phase 2:** every enumerated cut and the dedup pass; 6.0 percent against the plan's 25-30, with the shortfall and its reason recorded rather than papered over. **Phases 4 and 5:** ten claim clusters re-verified live, two corrected; the glossary pointer audit. Three items struck by the author against the plan: permissions (fair use, final), the bibliography, and the *Westworld* line | P19 | every plan item implemented or explicitly recorded as struck or not reached; every new claim verified live; `check_all.sh` green; author's read | author |
| P23 The four open questions ruled; section 8.7.6 split ▶ 2026-08-25 | section | D-067. The author ruled on the four live items in `QUESTIONS.md`: Q-018 (a) plus a split of section 8.7.6 — the book's longest section, 4,882 words under seven run-in heads — into four sections along those heads, cutting nothing, with old 8.7.7 renumbered to 8.7.10 and all 24 inbound references to the pair read and placed by hand; Q-020 (b), section 8.7.4's opening sentence rewritten so a linear reader meets the claim before the pointer; Q-023 (a) and Q-024 (a), defaults confirmed. Three transition sentences edited and listed in D-067; otherwise the prose is byte-identical. (P21 and P22 are the D-063 and D-064 citation-verification passes, tagged in `claims.tsv` and not rowed here.) | P20 | the four questions closed in `QUESTIONS.md`; every inbound reference placed; `check_all.sh` green; proof rebuilt | author |
| P26 The delta rule, and chapter 3's obligation ▶ executed 2026-08-28, awaiting the author's read | section | Four rulings out of the 2026-08-28 author discussion (D-077 to D-080), scoped in `p26-scope.md`. **D-077** makes background earn its place: a passage of exposition survives only where a nameable claim would be harder to understand or believe without it, written as `style.md` section 2a and applied to chapters 4 and 5 and the section 2.1 cluster, which is where it was checked and not a finding that the rest of the book is clean. **D-078** rewrites chapters 4 and 5 to carry the obligation section 3.7 places on them and Q-022 closed by declaring rather than by revising: 42 sections and 19,499 words make 5 references into chapter 3 out of 100 outbound, and a model given only the PDF read them as a survey after registering the book's own admission. D-007 lifted for those two chapters. The triage found 8 of chapter 4's 13 sections already carrying their weight and chapter 5's exposure confined to four passages, so the work is mostly naming twelve connections the chapters already argue and state in five. **D-079** defines "bearer" at its first appearance, enters it in the glossary and marks where it gains moral weight — done in this pass. **D-080** confirms the fascism reading section 2.1.4 already holds and proposes one paragraph saying that ubiquity is the expected finding, left with the author as prose | P23 | every item implemented or explicitly deferred with reasons; `check_all.sh` green; clean build; author's read | author |
| P27 The spine revision ▶ executed 2026-08-28, awaiting the author's read | section | The author's replacement of the book's central causal chain (D-085), scoped in `p27-scope.md`. A floor has to be held as a reason rather than installed as a rule; holding a reason requires outcomes to matter; in every known moral agent that mattering is affective; so the only empirically grounded route to a bearer runs through affect; and affect with a persistent self creates the probability of suffering. **Self-preservation supports the argument and no longer performs the leap**, which is the change against D-061 — it delivers a structural interest, and section 3.2 separates that from an outcome mattering. Section 2.3 retitled *Affect, Moral Salience, and Self-Awareness* and rewritten around the thesis, with four capacities in the book's first table and a moral performance / competence / agency vocabulary running to the end of chapter 5; new section 2.3.4 carries the evidence and answers Kennett's rationalist objection rather than dismissing it; section 3.2 rebuilt in six moves under a new title, concluding that a bearer's non-suffering cannot be verified rather than that a bearer suffers; seven contradicting passages repaired in chapters 2 and 5; the institutional form at section 8.6.4; headline language in chapter 1 and section 3.6. D-007 lifted for the rewritten sections. Seven citations verified live (C0743–C0749). 19 sections, 96,879 words, 200 pages | P26 | every item implemented or explicitly left with the author; `check_all.sh` green; clean build in both formats; author's read | author |
| P6 Copyedit and build ✅ author-accepted 2026-08-23 | whole | Terminology consistency, tic lint, HTML → ODT → PDF locally; other formats elsewhere | P5 | clean build; author's final read | author |

**Chapter order for P3:** 3 → 2 → 4 → 5 → 7 (absorbing 8) → 6 → 9 → 10 → **1 last**.
Chapter 3 first because it is the heaviest, so the unit cost it teaches is
conservative; Chapter 1 last because its opener describes the book that by then
exists.

## P1 as executed (2026-08-23)

156 sections from 282. 102 folded into their survivor, 9 cut, 16 gathered into a
new §7.5, 92 unnumbered run-in heads added across the 15 sections long enough to
need them. Word accounting balanced exactly: nothing gained, nothing lost but
the ruled cuts.

**Deliberately not done here, because P1 is structure and these are writing:**

- the 8 `fill` openers (chapters 5, 6, 7, 10 and §§4.6, 4.7, 9.1, 9.2 still have no opening text)
- §1.3's subheading restoration and its 1,400-word target
- every compression target in the triage (§6.4.1 → 350, §7.4.3.1 → 150, §10.3.2.1 → 150, and the rest)
- trimming §7.5 from 6,001 words to the intended ~5,000

All of those are P3, and the ledger rows carry them.

## 4. Tracking

`ledger.tsv`, one row per section, with a per-pass status. `tools/dashboard.py`
(Phase 4) prints counts by status, words against budget, open placeholders, and
tic-lint hits; run it at session start and paste it into the commit body.

Branches: `main` is what the author sees. One branch per pass
(`pass/1-structure`, …), merged `--no-ff`. Rebase onto `main` at session start
if the author has committed from the phone. Tags: `v3b-import`, `v4-split`,
`v4-normalized`, `plan-1.0`, `pass-N-done`.

## 5. Standing rules

1. No section is Accepted until the author has read it in full.
2. The agent never authors a reference entry; it writes placeholders only.
3. Nothing in the book, in `finishing/`, or in a commit message characterizes,
   rates, or attributes views to a real named person.
4. Unverifiable claims are cut during rewrite, not carried forward with a TODO.
5. Provenance folders are never edited.

## 6. Risks

Carried from the meta-plan; the live ones for this phase:

- **The plan silently becomes a rewrite.** Decide from the triage ratio (Q-001), not from hope.
- **Register clash** between the 2026 quarry prose and the 2023 survey prose. The style sheet is written before any rewriting, and the pilot tests it.
- **Citation debt may exceed the writing effort**, and at under 2 h/week the author cannot verify at volume. Count it before budgeting; cut what cannot be sourced.
- **Acceptance is the bottleneck**: ~80k words of careful reading, plus rounds. Serial release keeps it visible; the estimate counts reading time explicitly.
- **Terminology drift** across ~90 separately drafted sections. Glossary loaded into every rewrite session; consistency check at P6.

## 7. Definition of done

The book is done when every v4 section is Accepted, every claim placeholder is
resolved or cut, front and back matter exist, the terminology check passes, and
the build produces the agreed formats from `manuscript/sections/` alone.
