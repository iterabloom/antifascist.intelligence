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
