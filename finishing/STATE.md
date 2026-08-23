# State of play

Read this first. Written 2026-08-23, after P1.

## Where the book is

`manuscript/sections/` — **156 sections**, one file each, nothing deeper than
three levels. `manuscript/parseable_text_v4.txt` is the join and must always
match byte for byte. `manuscript/parseable_text_v3b_2024-07-07.txt` is the
frozen 2024 text, pinned by digest.

~113,000 words, plus ~10,400 of transplants still to land.

## What has actually been done to the prose

**Two sections, out of 156.**

- **§3.1.2.3.1.1 Attention** — revised, transplant T11 landed, author accepted. Now folded into §3.1.2 as a run-in head.
- **§2.2.1** — transplant T4 (the mirror-neuron box) drafted, not yet author-accepted. T3 will later replace the surrounding prose.

Everything else has been *structured*, not written: folded, cut, moved,
renumbered. No other sentence in the book has changed since 2024.

## Passes

| Pass | State |
|---|---|
| P0 Setup | done — split, tools, checks, tags |
| P1 Structure | **done** — 102 folds, 9 cuts, chapter 8 → §7.5, 92 run-in heads |
| P2 Cut/dedupe | **open question** — most of it was absorbed into P1's folds and the cluster homes; what remains is section-level work that arguably belongs to P3. See below. |
| P3 Revise | not started — 154 sections |
| P4 Source | not started — ~279 claim placeholders |
| P5 Front/back matter | not started |
| P6 Copyedit and build | not started |

## The immediate open question

**Does P2 survive as a separate pass?** The triage resolved most duplication
into folds and cluster homes, so what is left is: the RoboCup example duplicated
across §10.3.2 and §10.3.3, §8.4.1's two self-restating halves (now inside
§7.5), and the compression targets. All of those are edits to a specific
section, which is what P3 does. My recommendation is to drop P2 and fold its
items into P3, but that changes the plan, so it needs the author's word.

## What P1 deliberately left for P3

Carried on the ledger rows:

- **8 empty openers**: chapters 5, 6, 7, 10, and §§4.6, 4.7, 9.1, 9.2 have no opening text.
- **§1.3**: restore the subheadings deleted in 2024, and hit the 1,400-word target.
- **Compression targets**: §6.4.1 → 350, §7.4.3.1 → 150, §7.4.3.1.1 → 80, §10.3.2.1 → 150, §4.2.2 → 200, §10.1.1/.2 → 200, §10.1.3 → 100.
- **§7.5** to be trimmed from 6,001 words to ~5,000.
- **Run-in heads** exist in 15 sections; the other 141 have none and mostly do not need them.

## Open with the author

- **Q-011** — does chapter 2 keep its title, given that it now argues compassion is the design target and empathy is not. Default is to retitle; applies when P3 reaches chapter 2.
- **The roadmap promise** — the introduction promises a roadmap §10.2 does not deliver, and §10.2.1 concedes it. Under D-007 building one is out of scope, so either the promise changes or D-007 gets an exception.
- **P2** — see above.

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
