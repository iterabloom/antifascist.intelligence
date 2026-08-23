# State of play

Read this first. Written 2026-08-23, after chapters 2 and 3 of P3.

## Where the book is

`manuscript/sections/` — **156 sections**, one file each, nothing deeper than
three levels. `manuscript/parseable_text_v4.txt` is the join and must always
match byte for byte. `manuscript/parseable_text_v3b_2024-07-07.txt` is the
frozen 2024 text, pinned by digest.

93,453 words as of the last `section_stats.py` run — down from ~113,000 before
P3 started, because P3 is cutting real duplication (D-021), not just changing
voice. Chapter 3 alone went from ~24,000 words to 10,920.

## What has actually been done to the prose

**Chapters 2 and 3 in full — 38 sections, all drafted, none author-accepted
except the original pilot.** Chapters 1 and 4–10 (118 sections) are
untouched since 2024: folded, cut, and moved by P1, but not a sentence of
their prose has changed.

- **Chapter 3** (16 sections, 10,920 words): every section revised. All five
  outstanding transplants landed (T5, T12, T13, T14, T16 — the Miller-Cohen
  control model, predictive coding as the premise of AI perception, memory as
  reconstruction, working-memory capacity, and the amygdala/insula
  correction). §3.1.2, the largest single piece of the book at 12,149 words
  and 24 absorbed subsections, compressed to ~5,150 words. §3.1.3 (13
  subsections) compressed to ~1,450. A mirror-neuron/empathy claim repeating
  chapter 2's now-corrected error was cross-referenced instead.
- **Chapter 2** (21 sections + the chapter opener, ~10,900 words): every
  section revised. The remaining six transplants landed (T1, T3, T6, T7, T9,
  T10). §2.2.1 (pilot 2) is finished — the empathy/compassion dissociation
  argument (Singer & Klimecki) replaces "compassion is an evolutionary
  extension of empathy." §2.2.3 carries Bloom's case against empathy,
  unframed per D-016. §2.3.1 replaces Goleman's four components presented as
  fact with the genuinely unresolved basic-emotion-vs-constructed-emotion
  debate. §2.3.3 replaces a naive inner-observer account of AI self-awareness
  with Graziano's self-as-model argument and the rubber hand illusion. §2.4.1
  replaces a bare awareness/consciousness/qualia definition of sentience with
  the nociception-to-suffering ladder (Cassell) and Chalmers's hard problem —
  so "is it conscious" and "can it suffer" are no longer treated as the same
  question. **Chapter title changed** (Q-011 default applied): "Foundations
  of Compassion and Empathy in Friendly AI" — compassion now leads.

**Method that emerged today, worth keeping:** parallel agents draft
independent, non-transplant-bearing sections well and reliably surface
fabricated claims — this 2023 GPT-4 draft invents plausible-sounding named
systems, studies, and institutional claims at a real rate (roughly two dozen
found and cut across chapters 2 and 3: "CarpeDiem," "CASA," a fabricated
Hadfield-Menell robot demo, a misattributed FaceNet, invented MIT/Stanford/IBM
institutional claims, and more). Transplant-bearing and argument-critical
sections got done by hand instead — the stakes for getting the actual
argument right are higher there than parallel drafting's speed is worth.

**Network access exists in this session (D-022) — AGENTS.md's "no network
needed" premise, and D-009's assumption that citation verification requires a
separate session, were both wrong.** A verification pass today spot-checked
all 12 fabrication cuts and a 20-item sample of kept citations against live
search: 9 cuts confirmed outright, 2 reasonably cut on genuine unverifiable
vagueness, 1 cut was unnecessary (a real paper's actual subtitle, mistaken for
an invented acronym — no content was lost). All 20 sampled kept citations are
real; one had a wrong study-design detail, now fixed. P4 (Source) still exists
as the pass that formally resolves the whole claims ledger, but nothing now
blocks spot-checking a suspected fabrication during P3 itself.

## Passes

| Pass | State |
|---|---|
| P0 Setup | done — split, tools, checks, tags |
| P1 Structure | done — 102 folds, 9 cuts, chapter 8 → §7.5, 92 run-in heads |
| P2 Cut/dedupe | dropped, D-021 — folded into P3 |
| P3 Revise | **in progress — chapters 2 and 3 done (38 sections), chapters 1, 4–10 not started (118 sections)** |
| P4 Source | not started — claims ledger now at ~315 rows (many added landing transplants); network access confirmed live, so spot-verification can happen inline during P3, but the formal pass is still ahead |
| P5 Front/back matter | not started |
| P6 Copyedit and build | not started |

**Chapter order for the rest of P3** (from `PLAN.md`, unchanged): **4 → 5 →
7 (absorbing 8) → 6 → 9 → 10 → 1 last.**

## The immediate open items

- **Nothing in chapters 2 or 3 is author-accepted** except the original
  §3.1.2.3.1.1 Attention pilot. 38 sections are drafted and waiting on a read.
  D-001 allows up to two rounds before the author hand-edits instead.
- **Chapter 7's §7.4 tree overlaps chapter 2's §2.4 tree** (both cover ethics
  of experimenting on sentient AI subjects — §2.4 the definitional/principles
  side, §7.4 the legal/accountability side). §2.4.2–§2.4.7 already carry
  forward cross-references into chapter 7; when P3 reaches chapter 7, those
  need to resolve into something concrete rather than restating §2.4's
  content a second time.
- **Q-013** — the roadmap the introduction promises, which §10.2 doesn't
  deliver and §10.2.1 concedes. Applies when P3 reaches chapter 1, last.

## What P1 deliberately left for P3, still ahead

- **8 empty openers**: chapters 5, 6, 7, 10, and §§4.6, 4.7, 9.1, 9.2.
- **§1.3**: restore the subheadings deleted in 2024, hit the 1,400-word target.
- **Compression targets**: §6.4.1 → 350, §7.4.3.1 → 150, §7.4.3.1.1 → 80,
  §10.3.2.1 → 150, §4.2.2 → 200, §10.1.1/.2 → 200, §10.1.3 → 100.
- **§7.5** trim from 6,001 words to ~5,000.
- Chapter 4's §4.3.1 still needs T8 (the dual-process critic transplant).

## Where everything lives

| File | What |
|---|---|
| `finishing/DECISIONS.md` | D-000…D-022, append-only. **Read before assuming anything.** |
| `finishing/PLAN.md` | the passes, their entry/exit criteria |
| `finishing/style.md` | the operative spec for P3 — voice, tics, run-in heads, boxes, citations |
| `finishing/transplants.md` | the 16 transplants: source lines, targets, register edits |
| `finishing/triage.tsv` | every section's fate, with the reason |
| `finishing/toc_v4.tsv` | the outline, with what each section absorbed |
| `finishing/ledger.tsv` | per-section work state |
| `finishing/reports/claims.tsv` | the claims ledger, ~315 rows |
| `finishing/reports/` | claims, dated, redundancy, tics, voice, lists, triage summary, pilots, section_stats |
| `finishing/tools/check_all.sh` | **run at session start** |

## Rules that bite

**Named persons (D-017):** the hazard is the persona device, not citation.
Naming researchers behind published findings is fine and expected.
`names_guard.py` tests for the persona-device shape.

**Fabrication (new, from today):** this draft invents plausible named
systems/studies/institutions at a meaningful rate. An unfamiliar-sounding
named thing is not automatically fake (see the CDE-SSP false positive above)
— but D-009's rule stands: if it can't be confidently placed as real, cut it
rather than carry it forward with a placeholder.

**Commit messages:** `git commit -s` always. The hook silently deletes body
lines containing vendor or brand words within the first or last ten body
lines, and rewrites vendor-named trailers. Check with
`finishing/tools/msgcheck.sh` before committing anything with a long body.

**Shell heredocs and `<<list>>`/`<<box>>`/`<<h>>` markup:** a bash heredoc
writing a file containing this literal markup silently truncated content once
today. Use the Write tool for any file containing this markup, not `cat >
file << 'EOF'`.
