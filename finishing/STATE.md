# State of play

Read this first. Written 2026-08-23, after P1.

## Where the book is

`manuscript/sections/` — **156 sections**, one file each, nothing deeper than
three levels. `manuscript/parseable_text_v4.txt` is the join and must always
match byte for byte. `manuscript/parseable_text_v3b_2024-07-07.txt` is the
frozen 2024 text, pinned by digest.

~113,000 words, plus ~10,400 of transplants still to land.

## What has actually been done to the prose

**Four sections, out of 156. One accepted, three drafted and awaiting review.**

- **§3.1.2.3.1.1 Attention** — revised, transplant T11 landed, author accepted. Now folded into §3.1.2 as a run-in head.
- **§2.2.1** — transplant T4 (the mirror-neuron box) drafted, not yet author-accepted. T3 will later replace the surrounding prose.
- **§3.1 Incorporating Human Cognitive Models…** — P3 revise drafted (380 → ~208 words), not yet author-accepted. First section of the P3 pass proper.
- **§3.1.1 Cognitive Architectures** — P3 revise drafted, transplant T15 landed as a boxed passage adjudicating ACT-R vs. Society of Mind via the predictive-processing frame (484 → ~410 body words + a ~330-word box), not yet author-accepted. Two new claim placeholders for the named systems (C0281 ACT-R, C0282 Society of Mind) plus one for the transplanted frame (C0283).

Everything else has been *structured*, not written: folded, cut, moved,
renumbered. No other sentence in the book has changed since 2024.

**§3.1.2 is next and is the largest single piece of work in the book**: 12,149
words, 24 absorbed subsections carrying run-in heads (one already revised —
the Attention pilot), and five more transplants still to land (T5, T12, T13,
T14, T16). It will not go in one session; expect it revised run-in-head by
run-in-head across several.

## Passes

| Pass | State |
|---|---|
| P0 Setup | done — split, tools, checks, tags |
| P1 Structure | **done** — 102 folds, 9 cuts, chapter 8 → §7.5, 92 run-in heads |
| P2 Cut/dedupe | **dropped, D-021** — folded into P3; what remained (RoboCup duplicate, §8.4.1's halves, compression targets) travels with the section it belongs to |
| P3 Revise | **started, chapter 3** — 3 sections drafted (§3.1, §3.1.1, plus the earlier §2.2.1), 1 accepted (§3.1.2.3.1.1); 152 sections untouched |
| P4 Source | not started — ~282 claim placeholders (3 added landing T15) |
| P5 Front/back matter | not started |
| P6 Copyedit and build | not started |

## The immediate open item

**§3.1 and §3.1.1 are drafted and waiting on the author's read** (max 2 rounds
per D-001). Neither is Accepted yet. §3.1.2 — 12,149 words, 24 run-in heads,
five transplants — is next and will need several sessions.

## What P1 deliberately left for P3

Carried on the ledger rows:

- **8 empty openers**: chapters 5, 6, 7, 10, and §§4.6, 4.7, 9.1, 9.2 have no opening text.
- **§1.3**: restore the subheadings deleted in 2024, and hit the 1,400-word target.
- **Compression targets**: §6.4.1 → 350, §7.4.3.1 → 150, §7.4.3.1.1 → 80, §10.3.2.1 → 150, §4.2.2 → 200, §10.1.1/.2 → 200, §10.1.3 → 100.
- **§7.5** to be trimmed from 6,001 words to ~5,000.
- **Run-in heads** exist in 15 sections; the other 141 have none and mostly do not need them.

## Open with the author

- **Q-011** — does chapter 2 keep its title, given that it now argues compassion is the design target and empathy is not. Default is to retitle; applies when P3 reaches chapter 2.
- **Q-013** — the roadmap the introduction promises §10.2 does not deliver, and §10.2.1 concedes it. Under D-007 building one is out of scope, so either the promise changes or D-007 gets an exception. Applies when P3 reaches chapter 1.

## Where everything lives

| File | What |
|---|---|
| `finishing/DECISIONS.md` | D-000…D-020, append-only. **Read before assuming anything.** |
| `finishing/PLAN.md` | the passes, their entry/exit criteria |
| `finishing/style.md` | the operative spec for P3 — voice, tics, run-in heads, boxes, citations |
| `finishing/transplants.md` | the 16 transplants: source lines, targets, register edits |
| `finishing/triage.tsv` | every section's fate, with the reason |
| `finishing/toc_v4.tsv` | the outline, with what each section absorbed |
| `finishing/ledger.tsv` | per-section work state |
| `finishing/estimate.md` | 30–85 author hours, parametric in minutes-per-section |
| `finishing/reports/` | claims, dated, redundancy, tics, voice, lists, triage summary, pilots |
| `finishing/tools/check_all.sh` | **run at session start** |

## Two rules that bite

**Named persons (D-017):** the hazard is the persona device, not citation.
Naming researchers behind published findings is fine and expected. `names_guard.py`
tests for the persona-device shape.

**Commit messages:** `git commit -s` always. The hook silently deletes body
lines containing vendor or brand words within the first or last ten body lines,
and rewrites vendor-named trailers. Check with `finishing/tools/msgcheck.sh`
before committing anything with a long body.
