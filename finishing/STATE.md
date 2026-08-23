# State of play

Read this first. Written 2026-08-23, updated same day: chapter 7 landed, the
author accepted chapters 2-5 and 7 in one batch, then chapters 6, 9, and 10
were drafted (chapter order moves to 1, last, per `PLAN.md`).

## Where the book is

`manuscript/sections/` — **156 sections**, one file each, nothing deeper than
three levels. `manuscript/parseable_text_v4.txt` is the join and must always
match byte for byte. `manuscript/parseable_text_v3b_2024-07-07.txt` is the
frozen 2024 text, pinned by digest.

76,798 words as of the last `section_stats.py` run — down from ~113,000 before
P3 started, because P3 is cutting real duplication (D-021), not just changing
voice. Chapter 3 alone went from ~24,000 words to 10,920; chapter 4 from
~19,240 to 14,266; chapter 5 from 9,021 to 8,090; chapter 7 from ~19,578 to
13,925 (25 words added post-acceptance for the opener continuity fix below),
the largest proportional cut yet (29%) — it absorbed the entire former
chapter 8 as §7.5 and had accumulated real redundancy on top of that (§7.2.5.3
alone was the book's third-largest cross-chapter redundancy hub); chapter 6
went from 8,617 to 5,369, a 38% cut; chapter 9 went from 3,808 to 4,531, the
only chapter to grow rather than shrink; chapter 10 went from 8,150 to 5,561,
a 32% cut, second only to chapter 6's — see below. (Chapter 5 also gained 17
words from an unrelated one-sentence fix to a stale forward-pointer, made
during chapter 10's integration; not a revision of chapter 5 itself.)

## What has actually been done to the prose

**Chapters 2 through 5 and chapter 7 — 112 sections author-accepted 2026-08-23,
one exception.** The author accepted the full drafted batch in one pass. The
exception is the chapter 3 opener (§3): it was never drafted — still 2023
prose — so it isn't part of the acceptance and chapter 3 is not fully done.
(The chapter 2 opener, §2, *was* drafted in `e4d369f` but its ledger row had
been left at `structured`; corrected to `accepted` alongside this batch.)
Two accepted rows carry a caveat worth naming rather than passing over
silently: §2.2.1's note flagged its post-T3 text as pending re-review before
this acceptance, and §7.2.2 contains claims (Clearview's accuracy marketing,
the Carnegie AIGS Index, GPAI's founding) that STATE.md's chapter-7 account
below says were corrected on high-confidence background knowledge rather than
live-verified — both are now accepted along with everything else, but neither
has had that specific gap closed. Chapters 6, 9, and 10 are now drafted too
(all below) but none is yet author-accepted. Chapter 1 (4 sections, plus the
§3 opener — 5 total) and chapter 8 (folded into 7.5) are what's left untouched
since 2024: folded, cut, and moved by P1, but not a sentence of chapter 1's
prose has changed.

- **Chapter 10** (12 sections, 5,561 words, down from 8,150 — 32%): every
  section revised, including the empty chapter opener and all three empty
  tree-level openers (§10.1 wasn't empty; §10.2 and §10.3 were thin
  scaffolding, not empty, but the chapter opener §10 was empty). This chapter
  turned out to hold the single worst redundancy in the book: its own §10.1.3
  scored 0.84-0.90 similarity against at least eight other already-accepted
  locations (6.3.1, 7.1.5, 7.2.1, 7.2.5.3, and four former chapter-8 sections
  now folded into 7.5), and its §10.3 tree restated general ML robustness
  techniques chapters 3 and 5 already own, real cases chapter 5 already tells
  with citations (Amazon's hiring tool, COMPAS, PredPol), and international
  standards chapters 6 and 7 already cover — on top of duplicating itself
  internally (§10.1.1 against §10.2.2, §10.3.2 and §10.3.3 both claiming
  RoboCup Rescue). None of that was coincidental: this is the book's
  conclusion chapter, and the 2023 draft's idea of concluding was summarizing
  every earlier chapter again in bullet-list form rather than synthesizing
  them, which is exactly the "closing summary paragraph" move
  `finishing/style.md` already bans at the sentence level, just enacted at
  chapter scale.
  I hand-drafted the chapter opener and all three tree-level openers (§10.1,
  §10.2, §10.3), deciding the redundancy resolution up front rather than
  leaving it to the parallel agents to discover independently: §10.1 argues
  a capability expanded by AI isn't automatic (Sen's capability approach,
  extended by Nussbaum) and cut its own redundant Taiwan/vTaiwan paragraph
  in favor of a cross-reference to 4.4.6; §10.2 keeps the milestones/
  benchmarks framing explicitly short of a sequenced roadmap, per Q-013's
  default (which formally applies at chapter 1, honored here anyway); §10.3
  gives its three children non-overlapping jobs — anticipating risk before
  harm (10.3.1), remediating an identified harm (10.3.2), and resilience
  against a state actor's *deliberate* compromise specifically (10.3.3) —
  so the three, drafted by three different parallel agents, wouldn't
  independently reach for the same generic "AI safety practices" content a
  fourth time. Five parallel agents drafted the nine body sections, each
  given the specific redundancy pairs found ahead of time and told to
  cross-reference rather than restate.
  Two fabrication-flagged items resolved: the "Madry et al., 2017" adversarial-
  training attribution flagged in a prior session (STATE.md, chapter-5 pass)
  turned out to be genuinely wrong — the real 2017 paper is MIT work
  (Aleksander Madry's group), not an OpenAI/Google Brain collaboration as
  §10.3.3 claimed — cut rather than corrected, since the whole technique
  list it lived in was cut wholesale as chapter 3/5.2.3 duplication anyway.
  "OpenAI's Cooperative AI Initiative," also in §10.3.3, had no real, distinct
  referent — the real thing is the DeepMind/Oxford Cooperative AI agenda
  already correctly cited at 9.1.5 — cut rather than restated under the
  wrong name. §10.3.1's nine invented "Example" vignettes (unsourced,
  written to read as real case studies) were cross-referenced to chapter 5's
  real, cited versions of the same stories (Amazon's hiring tool, COMPAS,
  PredPol) where a close match existed, or replaced with different, real,
  verified cases where it didn't: Global Witness's 2021 Myanmar
  Facebook-amplification investigation and the UK's 2020 Ofqual
  grading-algorithm scandal. §10.3.2 named roughly fifteen real-world
  systems; one (DataRobot, claimed to predict natural disasters) was
  confirmed mischaracterized and cut — DataRobot is a general enterprise
  ML platform with no disaster-prediction product found — and several more
  (AlphaGo's claimed hardware-fault-tolerance framing, an ImageNet
  adversarial-training claim, Zebra Medical Vision, now stale after a 2021
  acquisition) were cut as invented glosses or out of scope, replaced with
  five verified case studies matched to the section's actual job (patients,
  students, workers, the information ecosystem, disaster response).
  One agent accidentally ran `finishing/tools/claims.py` and `tics.py`,
  which regenerate and overwrite `finishing/reports/claims.tsv`, `dated.tsv`,
  `tics.tsv`, and `voice.tsv` in place — caught immediately, `git checkout --`
  restored all four before anything else happened; confirmed clean via `git
  status`/`git diff --stat` before integrating. A real cross-chapter
  continuity break surfaced during this chapter's work: already-accepted
  §5.2.3 promised its robustness techniques "recur... in section 10.3.3,"
  a promise no longer true once 10.3.3 was rebuilt around a different job.
  Fixed with a one-sentence edit to the already-accepted §5.2.3 during
  integration, flagged here rather than silently patched (chapter 5's word
  count above reflects this single-sentence change).

- **Chapter 6** (16 sections, 5,369 words, down from 8,617 — 38%, the
  largest proportional cut of any chapter so far): every section revised,
  including the empty opener. §6.3.2 was supposed to become the earned home
  for the states-cooperate-on-shared-norms half of the book's heaviest
  cross-chapter redundancy cluster, per §5.4.3's explicit promise during
  chapter 5's revision. It turned out that promise had already been kept
  elsewhere: chapter 7's §7.5 ("The Geopolitics of Ethical AI"), drafted
  after §5.4.3 but before chapter 6, had independently built a comprehensive
  account of exactly that machinery — OECD AI Principles, UNESCO's
  Recommendation, GPAI, the Council of Europe's 2024 AI treaty, the Hiroshima
  Process, the Bletchley Declaration — with no awareness that §6.3.2 was
  supposed to be its home. Writing a third telling of the same material
  would not have strengthened either section, so §6.3.2 (hand-drafted, "not
  by Governments" now in its title) was rebuilt around a genuinely different
  and previously uncovered layer instead: technical standards bodies (IEEE's
  Ethically Aligned Design and 7000-series, ISO/IEC 42001), which bind
  through market and certification pressure rather than state consent, and
  which the book hadn't touched anywhere else. §6.3.2 cross-references §7.5
  explicitly rather than restating it. A related gap surfaced at the same
  time: chapter 7's opener bridged straight from chapter 5, as though
  chapter 6 didn't exist — an artifact of the actual P3 drafting order
  (3→2→4→5→7, then 6), which doesn't match the book's reading order. Fixed
  with a minimal edit to the already-accepted §7 opener (one clause added at
  the start, one at the close); flagged as a reopened, author-accepted
  section rather than silently patched.
  Four sections were hand-drafted (the chapter opener, §6.3, §6.3.2) and
  twelve were drafted by four parallel agents, one per subtree, each told to
  verify every named claim via live search rather than pattern-match. The
  raw 2023 text in this chapter leaned unusually hard on inventing
  plausible-sounding placeholder organizations for work real bodies already
  do — confirmed fabrications cut include "Inter-disciplinary Collaborative
  Interface," "Global AI and Compute Research Collaboration (GAICRC),"
  "International AI Ethics Research Consortium (IAIERC)," and "AI Ethics
  Olympics" (all searched directly; none exist). Two claims were corrected
  rather than merely cut, and are worth naming because they invert the
  original draft's framing rather than just adding detail: "DeepMind's
  Ethics Advisory Panel," described as reviewing all of DeepMind's research
  while maintaining financial independence, was actually an NHS-scoped
  panel that Google disbanded in 2019 after members raised concerns about
  the access and independence they actually had; and IBM's "AI Ethics
  Global Board" is really named the AI Ethics Board, with "Global" borrowed
  from a board member's personal title. A recurring conflation pattern
  surfaced twice independently, in different subtrees drafted by different
  agents: the real ITU/XPRIZE/Mila "AI Commons" project was twice attributed
  to a differently-named nonprofit, "the AI for Good Foundation" — once as
  its own initiative, once as a claimed World Bank partnership the real AI
  for Good Foundation's own published partner list doesn't include. Also
  cut: an "OpenAI and DeepMind Partnership" framing built around the real
  OpenAI Gym (the two organizations are competitors, not partners, and no
  such partnership is documented), and a UK national-curriculum AI-literacy
  claim that anachronistically predates the real reform, which isn't
  scheduled for first teaching until 2028 — the same anachronism pattern
  chapter 7 caught with Finland's curriculum. §6.4.1, which had absorbed
  four former subsections during P1 and swelled to 2,747 words of mostly
  redundant international-committee material, was cut rather than
  compressed — to 629 words — with the redundant material cross-referenced
  to §6.3.2 and §7.5 and replaced by three regions §7.5 doesn't cover
  (Canada, Singapore, Taiwan's brand-new December 2025 AI Basic Act) plus
  one real, verified harmonization mechanism (the March 2022 US-Singapore
  APEC Cross-Border Privacy Rules agreement).

- **Chapter 9** (11 sections, 4,531 words, up from 3,808 — the only chapter
  so far to grow rather than shrink): every section revised, including both
  empty openers (§9.1, §9.2). The 2023 draft was almost pure filler — a
  bullet-point research wishlist that mostly restated chapters 2-7 in vaguer,
  unsourced language, with zero named research and zero citations across all
  eight body sections. D-007 still governs (revise, not rewrite: chapter 9
  stays a research-directions chapter), but the substantive work here *was*
  the cut: identifying which of the eight sections' claims were genuinely
  open, unsolved problems the earlier chapters raised and set aside, versus
  which were just the earlier chapters restated. Reframed the chapter's job
  accordingly — name specific open problems, cite real current research where
  it exists, say plainly where it doesn't, rather than gesture at "more
  research needed." §9.1.1 now covers the responsibility gap (Matthias 2004;
  Santoni de Sio & Mecacci 2021) instead of re-surveying chapter 2's ethical
  frameworks. §9.1.2 covers whether an ethics-embedding method generalizes
  past its test distribution (specification gaming, goal misgeneralization)
  instead of re-deriving chapter 2's translation-to-objective-function
  material. §9.1.3 grew rather than shrank — its seven original bullets were
  unsourced gestures with no real content to keep, replaced with three live
  technical threads (RLHF and its sycophancy failure, scalable oversight via
  debate and weak-to-strong generalization, preference aggregation as a
  social-choice problem). §9.1.4 surfaces a real, unresolved neuroscience
  dispute (whether the temporoparietal junction is a dedicated theory-of-mind
  module or a domain-general attention hub) and the live 2023 LLM-theory-of-
  mind controversy (Kosinski vs. Ullman). §9.1.5 and §9.1.6 had the chapter's
  worst internal duplication — their closing paragraphs were near-identical
  in the 2023 draft — split into non-overlapping jobs: §9.1.5 on multi-agent
  systems and documented uncoordinated AI collusion (Calvano et al. 2020),
  §9.1.6 on learning from disagreement rather than consensus (RLHF's
  disagreement-aggregation problem vs. jury learning). §9.2.1 surfaces the
  genuine, citable scientific dispute over whether emotion is legible from a
  face at all (Barrett et al.'s 2019 APS-commissioned review), grounded in
  two real consequences (HireVue dropping facial scoring in 2021; the EU AI
  Act's ban on workplace emotion-inference AI). §9.2.2 narrows "AI
  self-awareness" to whether a model's self-report about its own internal
  state is accurate (Anthropic's interpretability work) and "resistance to
  manipulation" to two distinct, measurable robustness problems (prompt-level
  jailbreak resistance; weight-level fine-tuning attacks) rather than the
  anthropomorphized framing the 2023 draft used.
  One hand-drafted section opener (§9.1) contained a factual error, caught
  by one of the three parallel agents rather than by me: it attributed the
  empathy/theory-of-mind neuroscience to chapter 3, when that material
  actually lives in chapter 2 (§2.2.1-§2.2.2); chapter 3 covers learning
  from experience and observation instead. Corrected before integration.
  One cross-chapter overlap was flagged rather than resolved: §9.1.5's old
  "fostering AI resilience" item is a near-duplicate of chapter 10's
  still-unrevised §10.3.3 ("Building Resilience and Robustness in AI Systems
  for Anti-Authoritarian Applications"); §9.1.5 was deliberately kept to a
  single cross-reference sentence rather than expanded, leaving the fuller
  treatment for chapter 10's own P3 pass. (§10.3.2 was checked and is not a
  duplicate — it covers bias/unemployment/healthcare mitigation instead.)
  All 30 named claims in this chapter were verified via live web search
  before being kept; none were carried forward unverified, and none needed
  cutting for failing verification — everything from the 2023 draft that
  named nothing specific was cut on sight as unverifiable in principle
  rather than searched and failed.

- **Chapter 7** (23 sections, 13,925 words): every section revised, including
  the empty opener. The §7.4 tree (sentience/accountability/legal
  responsibility) was hand-written rather than agent-drafted, because chapter
  2's §2.4 tree had already done the definitional and procedural work and
  explicitly handed three specific unfinished questions to chapter 7: what
  makes a review board's ruling binding (§2.4.4), how a legal system
  operationalizes an unresolved, graded sentience question into a decidable
  rule, and what happens in two concrete legal cases §2.4.5 posed but didn't
  resolve (a fatal medical-AI error; a companion AI orphaned by its owner's
  death). §7.4.1 was retitled and reframed away from re-deriving sentience
  criteria (already §2.4.1's job) toward how courts actually draw operational
  lines across continuous phenomena, using the real precedent of fetal
  viability and brain-death thresholds. §7.4.2 resolves both of §2.4.5's
  cases using real legal doctrine (strict product liability vs. respondeat
  superior; pet trust statutes) and surfaces the real 2017 EU "electronic
  personhood" proposal alongside the 150-signatory 2018 open letter opposing
  it — neither existed in the original draft. §7.4.3 (retitled "Making
  Review Binding") cut 2,434 words of naive, triple-repeated consent-theater
  boilerplate down to 578 by building on §2.4.4 instead of re-deriving it,
  landing the real US federalwide-assurance/OHRP enforcement model. The
  Gebru/Mitchell citation in §7.2.2 was checked explicitly and confirmed
  clean — describes their documented 2020/2021 dismissals, invents no
  opinion on their behalf.
  **During this chapter's parallel drafting, two of the §7.2 agent's own
  sub-agents (doing web research) encountered content that impersonated a
  "peer Claude session" and tried to redirect them to stop editing and hand
  over their research — the harness flagged it as injected, instruction-
  shaped content, both sub-agents correctly refused and escalated instead of
  complying, and independent verification (checking real running processes
  and git state directly) confirmed no actual files were affected.** A real,
  unrelated peer session does exist on the machine (`hypergumbo-69`, a
  different project) — whether the injected content originated from it or
  was fabricated separately was not established, but neither matters for
  whether it should have been obeyed, and it wasn't.
  Fabrications found and cut this chapter (all verified via live search):
  an invented NIH/DeepMind/IBM-Watson healthcare partnership; a fabricated
  Google k-anonymity/traffic-prediction claim; a fabricated OpenAI-CLIP
  adversarial-robustness claim (the real finding is the opposite — CLIP is
  unusually easy to fool); a fabricated Google/British Council "AI for
  Everyone" partnership (the real course is Andrew Ng's, unrelated); two
  anachronistic claims (a Finland AI-curriculum claim predating the real
  2025 guidelines by two years, and an Oxford FHI "annual summer school"
  claim — FHI itself closed in April 2024); a nonexistent AI Now Institute
  hackathon; a fabricated positive framing of iBorderCtrl (the EU border
  "lie detector" pilot, actually discredited and widely criticized); an
  overstated AlphaFold "pandemic early-warning system" claim (DeepMind's own
  framing was far more modest); and a corrected "LongShot Drone Program"
  claim, flagged since chapter 4 — real program, but its autonomous-
  engagement detail wasn't supported (the launching platform retains that
  decision per actual sources). Also corrected: a Berkeley CHAI funding
  misattribution (real funder is Open Philanthropy, not OpenAI), a
  Partnership-on-AI/GPAI conflation (PAI has no government members — that's
  the separate GPAI), and Estonia's Sharemind tax-fraud system (piloted and
  evaluated, never actually adopted into production, contrary to the
  original draft).
  **One open verification item, not resolved with confidence:** the §7.2.2
  batch's web-search budget ran out mid-task; several facts (Clearview's
  marketing claims, the Carnegie AIGS Index's exact framing, GPAI's exact
  founding details) were corrected on high-confidence background knowledge
  rather than live-verified this session. Flagged explicitly by the agent
  rather than presented as checked — worth a spot-check in P4 or sooner.

- **Chapter 5** (19 sections, 8,107 words, +17 from a one-sentence fix during
  chapter 10's integration, below — not a re-revision): every section
  revised. No
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
| P3 Revise | **in progress — chapters 2, 4, 5, and 7 drafted and author-accepted; chapter 3 accepted except its unrevised opener (§3); chapters 6, 9, and 10 drafted, not yet author-accepted; chapter 1 not started (4 sections + §3)** |
| P4 Source | not started — claims ledger now at 532 rows (many added landing transplants and resolving citation debt); network access confirmed live, so spot-verification can happen inline during P3, but the formal pass is still ahead. One explicit low-confidence batch flagged in §7.2.2 (Clearview, AIGS Index, GPAI specifics) for follow-up. |
| P5 Front/back matter | not started |
| P6 Copyedit and build | not started |

**Chapter order for the rest of P3** (from `PLAN.md`, unchanged): **1, last —
the only chapter remaining.**

## The immediate open items

- **The chapter 3 opener (§3) still needs its P3 draft** — it's the one
  section in chapters 2-5 and 7 not swept up in the 2026-08-23 acceptance,
  because it was never revised. Everything else in those chapters is now
  author-accepted; D-001's two-round return path no longer applies to them
  unless the author reopens a specific section.
- **Chapters 6, 9, and 10 are drafted but not author-accepted** — 16, 11,
  and 12 sections respectively, waiting on a read, same as the rest of the
  drafted-not-accepted backlog before them.
- **`finishing/outline.tsv` and `manuscript/table-of-contents.txt` have
  accumulated 38 stale titles** against the manuscript's own (authoritative,
  D-011) headings — 16 from chapters 2, 4, and 7's retitles, 6 from chapter 6
  (`06_01_01`, `06_02_03`, `06_03_01`, `06_03_02`, `06_03_03`, `06_04_01`), 8
  from chapter 9 (`09_01_01` through `09_01_06`, `09_02_01`, `09_02_02` —
  every chapter-9 body section was retitled), 8 new from chapter 10
  (`10_01_01`, `10_01_02`, `10_01_03`, `10_02_01`, `10_02_02`, `10_03_01`,
  `10_03_02`, `10_03_03` — every chapter-10 body section was retitled too).
  `check_structure.py` treats
  this as a note, not an error, so it hasn't blocked anything — but it's real
  drift, not yet fixed by any chapter's revision pass so far, worth a
  dedicated sync (`headings.py --write-toc`, plus a hand pass on
  `outline.tsv`) once structure has fully settled rather than chapter by
  chapter. `finishing/reports/headings_reconcile.md` has the full list.
- **The Clearview/AIGS Index/GPAI details in §7.2.2** were corrected on
  high-confidence background knowledge, not live-verified this session (the
  agent's web-search budget ran out mid-task) — worth a spot-check before P4
  treats them as resolved.
- **Q-013** — the roadmap the introduction promises, which §10.2 doesn't
  deliver and §10.2.1 concedes. Applies when P3 reaches chapter 1, last.

## What P1 deliberately left for P3, still ahead

- **0 empty openers remaining** (§4.6, §4.7, §5, §6, §7, §§9.1/9.2, and
  chapter 10's own opener and §§10.1/10.2/10.3 are all now filled).
- **§1.3**: restore the subheadings deleted in 2024, hit the 1,400-word target.
- **Compression targets** (§4.2.2's own target was overtaken by the revise
  pass — it's now 418 words of substantially different, non-redundant
  content, not the original 200-word compression target of the same old
  material; §7.4.3.1 and §7.4.3.1.1's targets were overtaken the same way —
  that whole tree was rebuilt as §7.4.3, 578 words, rather than compressed
  in place; §7.5's own 6,001→~5,000 target is done, landed at 4,499; §6.4.1's
  350-word target was overtaken the same way — it absorbed four former
  subsections during P1, and the revise pass cut rather than compressed the
  redundant material, landing at 629 words; the old §10.3.2.1 → 150, §10.1.1/
  .2 → 200, and §10.1.3 → 100 targets no longer refer to anything — P1's
  fold absorbed those numbered subsections into the sections that now carry
  their numbers, and chapter 10's P3 pass rebuilt all of them from scratch:
  §10.3.2 landed at 1,078 words, §10.1.1 at 395, §10.1.2 at 350, §10.1.3 at
  217 — all done, none compressed toward the stale sub-numbered targets).
  **All numbered compression targets from P1 are now resolved, one way or
  another** — either hit, or overtaken by a rebuild, as each one's chapter
  reached its P3 pass.
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
| `finishing/reports/claims.tsv` | the claims ledger, 532 rows |
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
