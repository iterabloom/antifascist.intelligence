# State of play

Read this first. Written 2026-08-23, updated same day after chapter 5 of P3.

## Where the book is

`manuscript/sections/` — **156 sections**, one file each, nothing deeper than
three levels. `manuscript/parseable_text_v4.txt` is the join and must always
match byte for byte. `manuscript/parseable_text_v3b_2024-07-07.txt` is the
frozen 2024 text, pinned by digest.

87,548 words as of the last `section_stats.py` run — down from ~113,000 before
P3 started, because P3 is cutting real duplication (D-021), not just changing
voice. Chapter 3 alone went from ~24,000 words to 10,920; chapter 4 from
~19,240 to 14,266; chapter 5 from 9,021 to 8,090 — a smaller cut than 3 or 4,
since chapter 5's problem was mostly missing citations and unmarked lists
rather than duplicated argument.

## What has actually been done to the prose

**Chapters 2 through 5 in full — 90 sections, all drafted, none
author-accepted except the original pilot.** Chapters 1, 6–10 (66 sections)
are untouched since 2024: folded, cut, and moved by P1, but not a sentence of
their prose has changed.

- **Chapter 5** (19 sections, 8,090 words): every section revised. No
  transplants target this chapter. The one empty opener (§5) was filled by
  hand. §5.4.3 sits at the center of the book's heaviest cross-chapter
  redundancy cluster (13 flagged pairs) — rather than re-deriving a fate for
  it, the agent doing that batch found the project's own existing triage
  ruling (`triage.tsv`/`triage-brief.md`) already split the cluster's
  argument in two: the design claim (build systems/policy resistant to
  authoritarian capture) belongs at §5.4.3, the governance claim (states
  cooperating on shared norms) belongs at §6.3.2, not yet revised. It
  independently spot-verified that ruling against the highest-similarity
  matches before building §5.4.3 out with real policy levers (the EU's
  dual-use export control, AI Act Article 5 and the Clearview AI case, the
  Toronto Declaration) it didn't have before. Five more fabrications found
  and cut, all verified via live search rather than pattern-matching alone: a
  claim conflating a real finding (Zhao et al. 2017's gender-labeling bias)
  with the wrong dataset (ImageNet instead of MS-COCO/imSitu), a
  GPT-3-specific OpenAI explainability initiative search couldn't
  substantiate, a nonexistent "International Cooperation for AI Safety"
  organization (the real analog didn't launch until Nov. 2024, after this
  2023 draft), an unsupported Gabon "deepfake" coup claim (forensics never
  confirmed it was a deepfake), and an overstated Nagorno-Karabakh
  "AI-enhanced drones" claim. Also corrected: the COMPAS mechanism (doesn't
  take race as a direct input; the real problem is differential error
  rates), the PredPol methodology (arrest data reflects policing patterns,
  not drug-use rates), and the popular misconception that China's Social
  Credit System is one unified national score rather than a fragmented
  patchwork.
- **Chapter 4** (33 sections, 14,266 words): every section revised. The
  outstanding transplant (T8) landed in §4.3.1, retitled "Two Systems, or
  One?" — replaces dual-process theory presented as settled fact with
  Kahneman/Greene/Evans-Stanovich and the VMPFC-patient evidence, ending on a
  warning against literal fast-heuristic/slow-override AI architectures;
  §4.3.2 was reworked to pick up that warning rather than propose exactly the
  architecture it cautions against. Both empty openers (§4.6, §4.7) were
  filled by hand; §4.7's explicitly distinguishes itself from §3.3 per D-020
  rather than re-arguing curiosity/exploration. Six more fabrications found
  and cut: a fake "DeepMind Agent57 multi-agent" claim with a mismatched
  citation, a fake "ACAI framework" attributed to Badia et al., a fake "Moral
  Machine AI" reward-trained agent misattributed to Kleiman-Weiner (the real
  Moral Machine is Awad et al.'s unrelated survey study), a fabricated
  Waymo/Cruise/Argo-AI joint data-sharing claim, a misattribution (the AI
  Alignment Forum credited to MIRI; it was built by LessWrong), and a
  DeepMind/NHS partnership presented as an ethics exemplar when it was
  actually ruled unlawful by the UK ICO in 2017 — all verified via live
  search, not just pattern-matched. §4.4's Bronfenbrenner ecological-systems
  scaffold was kept whole per D-020; §4.4.6 resolved two real cross-chapter
  overlaps by pointing to chapter 5's actual countermeasures sections instead
  of re-arguing an 8-item policy list a third time.
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

**Method that's now been validated across two chapters:** parallel agents
draft independent, non-transplant-bearing sections well and reliably surface
fabricated claims — this 2023 GPT-4 draft invents plausible-sounding named
systems, studies, and institutional claims at a real rate (roughly three dozen
found and cut across chapters 2–4: "CarpeDiem," "CASA," two separate
fabricated Hadfield-Menell/CIRL demo details, a misattributed FaceNet, a fake
DeepMind Agent57 multi-agent claim, a fake "ACAI framework," a fake "Moral
Machine AI" agent, a fabricated Waymo/Cruise/Argo-AI initiative, invented
MIT/Stanford/IBM institutional claims, and more). Transplant-bearing and
argument-critical sections got done by hand instead — the stakes for getting
the actual argument right are higher there than parallel drafting's speed is
worth. For chapter 4, each of the 7 parallel agents was told to web-search
anything that looked like a specific named claim before keeping or cutting it,
not just pattern-match — this caught misattributions (MIRI/AI Alignment
Forum) and factual problems (DeepMind/NHS) that pattern-matching alone would
have missed either direction.

**Network access exists in this session (D-022) — AGENTS.md's "no network
needed" premise, and D-009's assumption that citation verification requires a
separate session, were both wrong.** A verification pass on chapters 2–3
spot-checked all 12 fabrication cuts and a 20-item sample of kept citations
against live search: 9 cuts confirmed outright, 2 reasonably cut on genuine
unverifiable vagueness, 1 cut was unnecessary (a real paper's actual subtitle,
mistaken for an invented acronym — no content was lost). All 20 sampled kept
citations are real; one had a wrong study-design detail, now fixed. Chapter 4
built verification into the drafting pass itself rather than a separate
after-the-fact spot-check. P4 (Source) still exists as the pass that formally
resolves the whole claims ledger, but nothing now blocks spot-checking a
suspected fabrication during P3 itself.

## Passes

| Pass | State |
|---|---|
| P0 Setup | done — split, tools, checks, tags |
| P1 Structure | done — 102 folds, 9 cuts, chapter 8 → §7.5, 92 run-in heads |
| P2 Cut/dedupe | dropped, D-021 — folded into P3 |
| P3 Revise | **in progress — chapters 2, 3, 4, and 5 done (90 sections), chapters 1, 6–10 not started (66 sections)** |
| P4 Source | not started — claims ledger now at 378 rows (many added landing transplants and resolving citation debt); network access confirmed live, so spot-verification can happen inline during P3, but the formal pass is still ahead |
| P5 Front/back matter | not started |
| P6 Copyedit and build | not started |

**Chapter order for the rest of P3** (from `PLAN.md`, unchanged): **7
(absorbing 8) → 6 → 9 → 10 → 1 last.**

## The immediate open items

- **Nothing in chapters 2 through 5 is author-accepted** except the original
  §3.1.2.3.1.1 Attention pilot. 90 sections are drafted and waiting on a read.
  D-001 allows up to two rounds before the author hand-edits instead.
- **§6.3.2 needs to earn the "governance/cooperation" home** it was just
  assigned. Chapter 5's §5.4.3 rebuild explicitly deferred the
  states-should-cooperate-on-shared-norms half of the book's heaviest
  redundancy cluster to §6.3.2 (still unrevised, raw 2023 text) — when P3
  reaches chapter 6, that section needs real, citable content, not just an
  assertion that it's the designated home.
- **An unverified "LongShot Drone Program" DARPA claim** was spotted sitting
  in unrevised chapter 7 (§07_02_01 or §07_05) while a chapter-4 agent was
  checking cross-references — not touched, out of scope at the time. Check it
  for fabrication when P3 reaches chapter 7.
- **An unverified "Madry et al. 2017" OpenAI/Google-Brain attribution** was
  spotted in unrevised §10.3.3 while a chapter-5 agent was resolving a
  redundancy against it — not touched, out of scope at the time. Check it for
  fabrication when P3 reaches chapter 10.
- **Chapter 7's §7.4 tree overlaps chapter 2's §2.4 tree** (both cover ethics
  of experimenting on sentient AI subjects — §2.4 the definitional/principles
  side, §7.4 the legal/accountability side). §2.4.2–§2.4.7 already carry
  forward cross-references into chapter 7; when P3 reaches chapter 7, those
  need to resolve into something concrete rather than restating §2.4's
  content a second time.
- **Q-013** — the roadmap the introduction promises, which §10.2 doesn't
  deliver and §10.2.1 concedes. Applies when P3 reaches chapter 1, last.

## What P1 deliberately left for P3, still ahead

- **5 empty openers remaining**: chapters 6, 7, 10, and §§9.1, 9.2 (§4.6,
  §4.7, and §5 are now filled).
- **§1.3**: restore the subheadings deleted in 2024, hit the 1,400-word target.
- **Compression targets**: §6.4.1 → 350, §7.4.3.1 → 150, §7.4.3.1.1 → 80,
  §10.3.2.1 → 150, §10.1.1/.2 → 200, §10.1.3 → 100 (§4.2.2's own target was
  overtaken by the revise pass — it's now 418 words of substantially
  different, non-redundant content, not the original 200-word compression
  target of the same old material).
- **§7.5** trim from 6,001 words to ~5,000.
- All 16 transplants are now landed (T8 was the last one, in §4.3.1).

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
| `finishing/reports/claims.tsv` | the claims ledger, 378 rows |
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

**`finishing/reports/ch2-3-proof_2026-08-23.pdf` is a one-off exception** to
`pipeline.md`'s "build products stay in the scratchpad" rule — the author
asked for it committed. It is already stale (chapter 4 isn't in it) and will
not be kept in sync; don't treat its presence as a new convention, and don't
regenerate/recommit it reflexively as chapters finish unless asked again.
