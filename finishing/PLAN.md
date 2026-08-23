# Finishing plan

**Status: skeleton.** Sections 2, 4, and the estimate are filled once the
assessment reports and the author's triage exist. The meta-plan that produced
this file is at `~/.claude/plans/` (planning phase, phases 0–6).

## 1. Target specification

A book for serious general readers (D-002), single-author voice with an "On
method" note (D-008), endnotes for named studies, statutes, systems and
quotations (D-009), dateless prose with dates confined to clearly dated boxes,
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
happens to supply one; and arguing the anti-authoritarian thesis somewhere it is
currently assumed. Those stay as they are unless the author reopens D-007.

**Length.** Starting from 115,377 body words: D-010's cuts remove ~3.5k
(§6.4.1.1–.9) plus whatever chapter 8's fold into chapter 7 sheds, the
duplication rulings perhaps 5–8k, and D-014 *adds* ~12k. That lands near
110–115k against D-002's 75–90k. The gap is now large enough that D-002 should
be treated as aspirational unless the author wants deeper cuts; it is the one
place the decisions genuinely pull against each other, and it is flagged rather
than resolved.

**Epigraphs (D-012).** All three are kept at the author's direction. They are
third-party copyrighted text — two song lyrics and a television script — so a
permissions task is live: identify each rights holder, request print and ebook
permission, and record the outcome. This must resolve before any public
distribution, and it is the one open item that an outside party controls.

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
| P1 Structure | heading | Apply the v4 outline: move, merge, retitle, split at heading granularity only. No sentence rewriting. Reflow §1.3, whose subheadings were deleted in 2024 without reflowing the text | P0 | every v3b section has exactly one recorded fate and location | author decides, agent applies |
| P2 Cut | section / paragraph | Cut sections; apply the single-home merges from the redundancy map (§2.4 vs §7.4 above all); country listings; drafting artifacts; epigraphs; "In conclusion" closers | P1 | word count within the ceiling; no redundancy pair above threshold remains; compliance flags cleared | author |
| P3 Revise | v4 section | Agent edits the existing text to the style sheet: voice to first person, "report" to "book", closers and signposts out, `[[cite:ID]]` placeholders in, unverifiable claims cut, dated claims generalized or boxed. The argument stays. Author Accepts or returns (max 2 rounds) | P2; style sheet approved; pilot accepted | every section Accepted; tic lint clean; cross-references present | author accepts |
| P4 Source | claim | Placeholders resolved: verified reference, replacement, or cut. Runs in a networked session; agent formats only from supplied references | chapter Accepted at P3 | zero placeholders in the chapter | author |
| P5 Front/back matter | whole | Chapter 1 opener written **last**, because it describes the book that now exists; "On method" note; glossary | all chapters past P4 | author Accepts | author |
| P6 Copyedit and build | whole | Terminology consistency, tic lint, HTML → ODT → PDF locally; other formats elsewhere | P5 | clean build; author's final read | author |

**Chapter order for P3:** 3 → 2 → 4 → 5 → 7 (absorbing 8) → 6 → 9 → 10 → **1 last**.
Chapter 3 first because it is the heaviest, so the unit cost it teaches is
conservative; Chapter 1 last because its opener describes the book that by then
exists.

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
- **The commit hook eats body lines** containing brand words. Use `msgcheck.sh`.

## 7. Definition of done

The book is done when every v4 section is Accepted, every claim placeholder is
resolved or cut, front and back matter exist, the terminology check passes, and
the build produces the agreed formats from `manuscript/sections/` alone.
