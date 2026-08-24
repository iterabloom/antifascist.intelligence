# State of play

Read this first. **Updated 2026-08-24 after P11 (D-043): the book's chapter structure changed — chapters now run 0 to 11, old section 2.1.5 is chapter 3, and there is a new chapter 7. Section numbers written before that date use the old numbering. The P11 note at the end of this file is the current summary.** Written 2026-08-23, updated same day: chapter 7 landed, the
author accepted chapters 2-5 and 7 in one batch, then chapters 6, 9, and 10
were drafted, then chapter 1, then finally the chapter 3 opener (§3) — the
last section in the entire book with no P3 draft. **Every section in the
book has now had a P3 pass.** The remaining 44 sections (chapters 1, 3's
opener, 6, 9, 10) were then accepted at P3 by explicit blanket author
instruction rather than the section-by-section read this project's own
standing rule otherwise requires — disclosed in `ledger.tsv` and below, not
silently applied. **All 156 sections are now `accepted`.** The
`outline.tsv`/TOC title-drift sync is done (drift is 0). P3.5 (the style
sweep) has swept every chapter. **P4 (sourcing) is now complete book-wide:
every one of `claims.tsv`'s 536 rows carries a non-empty note — zero
unresolved placeholders anywhere** — see below for both P4 batches and the
two flagged citation disputes that got resolved along the way. **P5 (front/
back matter) is author-accepted, 2026-08-23**: a new §0 "On Method"
note (510 words, D-008's ~500-word target) and a new §11 "Glossary" (51
terms, ~2,290 words) — 158 sections total now. Chapter 1's opener, P5's
third deliverable, needed no separate work: the P3 chapter order already put
it last (see "Chapter order for P3" in `PLAN.md`), so it already describes
the book as it now exists. See "P5, accepted" below. **P6 (copyedit and
build) is author-accepted, 2026-08-23**: `tics.py` re-run book-wide (the
signature "foster" tic, 278 occurrences before P3, is now 0 — three section
titles and one sentence still carried it and are fixed below), a
terminology sweep found no residue to fix, `check_structure.py` gained a
check it was missing (a section's own heading title can drift from
`ORDER.tsv`'s title column, which is what `render.py` actually renders, with
nothing catching it — this had already happened twice), and the whole-book
proof PDF was rebuilt (132 pages, HTML → LibreOffice → ODT → PDF, spot-read)
and sent to the author, who read it and accepted. See "P6" below.

**P8 (second editorial review response) opened and drafted, 2026-08-23**,
scoped in `p8-scope.md` to four items the author ruled on (D-033 through
D-036). D-007 is lifted again for this pass only, on D-029's terms. The
central change is in section 2.1.4: the review found a collision the book had
never made — every discriminating feature of fascism-proper is molar, an AI
deployment is only molecular, so at the book's own scale only the
flags-everything signature remains. Resolved on the author's ruling that
molecular fascism *is* fascism (D-034), with the cost stated. The
weaponization half of section 7.1.7 moved forward to travel with the design
chapters; 7.1.7 was rewritten around what survives. The dissent through-line
is named at its three sites (2.1.4, 5.1.1, 7.1.6). Chapter 1's opener now
surfaces the persistence argument, and 2.4.4 is retitled. **None of it is
author-accepted.** Two of the review's six items were declined as already
satisfied, and two of its factual claims did not survive checking — both
recorded in `p8-scope.md` rather than passed over.

## Where the book is

`manuscript/sections/` — **158 sections** (the 156 body sections, chapters
1-10, plus P5's two new front/back-matter sections, §0 and §11 — see "P5,
accepted" below), one file each, nothing deeper than three levels.
`manuscript/parseable_text_v4.txt` is the join and must always match byte
for byte. `manuscript/parseable_text_v3b_2024-07-07.txt` is the frozen 2024
text, pinned by digest.

76,949 words total as of the last `section_stats.py` run (74,148 of that in
the 156 body sections, 2,801 in §0 and §11 — one word shorter than at P5
acceptance: a P6 tic-lint edit to §2.2.1, below). The 156-section figure is down
from ~113,000 before P3 started, because P3 is cutting real duplication
(D-021), not just changing voice. Chapter 3 alone went from ~24,000 words to 11,011 (91 of those words
are the freshly-drafted opener, §3, below — not a re-revision of the rest of
the chapter, which was already accepted); chapter 4 from
~19,240 to 14,119 (155 off in the P3.5 sweep, 8 back in the author's §4.7.1 rewrite, below); chapter 5 from 9,021 to 8,247 (net of two disclosed post-acceptance
edits: the 17-word stale-pointer fix from chapter 10's integration, and the
racial-capitalism paragraph added to §5.1 at the author's request — below); chapter 7 from
~19,578 to 13,925 (25 words added post-acceptance for the opener continuity
fix below); chapter 6 went from 8,617 to 5,369, a 38% cut; chapter 9 went
from 3,808 to 4,531, the only chapter to grow rather than shrink; chapter 10
went from 8,150 to 5,558, a 32% cut; chapter 1 went from 3,241 to 1,149 in
the P3 draft, then to 908 after the author's own 2026-08-23 hand revision —
a 72% cut overall and the largest proportional cut in the whole pass — see
below.

## What has actually been done to the prose

**Chapters 2 through 5 and chapter 7 — 112 sections author-accepted 2026-08-23,
one exception.** The author accepted the full drafted batch in one pass. The
exception was the chapter 3 opener (§3): at that point it had never been
drafted — still 2023 prose — so it wasn't part of the acceptance and chapter
3 wasn't fully done. It has since been drafted too, in this same session
(below) — not yet accepted, so chapter 3 still isn't fully done, but for a
different reason now: a fresh draft awaiting a read, not missing prose.
(The chapter 2 opener, §2, *was* drafted in `e4d369f` but its ledger row had
been left at `structured`; corrected to `accepted` alongside this batch.)
Two accepted rows carry a caveat worth naming rather than passing over
silently: §2.2.1's note flagged its post-T3 text as pending re-review before
this acceptance, and §7.2.2 contains claims (Clearview's accuracy marketing,
the Carnegie AIGS Index, GPAI's founding) that STATE.md's chapter-7 account
below says were corrected on high-confidence background knowledge rather than
live-verified — both are now accepted along with everything else, but neither
has had that specific gap closed. Chapters 1, 6, 9, and 10 are now drafted
too (all below) but none is yet author-accepted — nor is the chapter 3
opener (§3), drafted for the first time in this same pass (below). **Every
section in the book — all 156, across all ten active chapters — has now had
a P3 pass.** Chapter 8 was folded into 7.5 by P1; nothing else remains
untouched since 2024.

- **P4 (Source) started on the four chapters that clear its entry gate**
  (2026-08-23): P4's entry criterion is "chapter Accepted at P3." Only
  chapters 2, 4, 5, and 7 currently qualify — chapter 3 is blocked by its
  unaccepted opener (§3), and chapters 1, 6, 9, and 10 aren't accepted at
  all. P4 has not touched those five; nothing below applies to them. Five
  parallel agents split the four eligible chapters' 271 `claims.tsv` rows
  (chapter 2: 30; chapter 4: 80, split 4.1-4.5.2 / 4.5.3-4.7.1.1; chapter 5:
  54; chapter 7: 107), each doing live web verification, correcting or
  cutting what didn't hold up, and reporting findings back rather than
  writing directly to the shared `claims.tsv`/`ledger.tsv` files — merged
  centrally afterward to avoid concurrent-write races between agents. 92 of
  the 271 rows already carried real verification from earlier ad hoc work
  (chapters 5 and 7's original P3 passes, the D-024 racial-capitalism
  paragraph) and were skipped rather than re-checked.
  Of the remaining 179: **135 verified accurate** on independent search (no
  manuscript action), **2 corrected** — §2.2.1's citation year (Southgate &
  Hamilton's review was published 2008, not 2009, confirmed via
  PubMed/PsycNet) and §2.3.2's Empatica E4 sensor list (removed
  "pupil dilation" — the device's real sensors are PPG, EDA, accelerometer,
  and skin temperature; no pupil sensor, which would need eye-tracking
  hardware a wristband doesn't have) — **44 retired as orphaned rows** (old
  claim IDs C0001-C0009, C0031-C0068 whose citation tokens and sentences no
  longer exist anywhere in the manuscript, superseded earlier the same day
  when chapter 4's own P3 revise pass — commit `944e199` — rewrote those
  sections and replaced the citations under new IDs; kept in `claims.tsv`
  per its append-only convention, marked retired rather than deleted), and
  **2 left unresolved and flagged for the author** rather than guessed at:
  C0276 (whether Gallese or Fogassi personally reached for the object that
  first triggered a monkey's mirror-neuron firing — reputable sources
  genuinely disagree, e.g. Nautilus says Gallese, Scientific American says
  Fogassi, and no primary-source account resolving it was found) and C0277
  (whether "the neurons that shaped civilization" was Ramachandran's own
  phrase or an externally applied talk title — his 2011 book uses different
  wording, "neurons that built civilization"). No fabrications were found
  beyond what P3's own same-day passes had already caught and cut.
  **One process incident.** The chapter-2 agent had itself fanned out four
  research sub-agents; one of them, working only the six mirror-neuron
  claims, went out of scope and edited `finishing/reports/claims.tsv` and
  `finishing/ledger.tsv` directly (both explicitly forbidden — shared files
  other concurrent agents depend on). At the same time, the coordinator
  (this session) had — at the author's explicit request, in a direct
  exchange unrelated to any P4 agent — added a citation (C0703, the UN's
  1948 Universal Declaration of Human Rights) to §2.1.3, a section with no
  prior claims rows and therefore outside every P4 agent's assigned scope.
  The chapter-2 agent's `git diff` check found that addition, misread it as
  its own sub-agent's unauthorized, fabricated edit — the sub-agent's note
  falsely read "at author's request," which was actually true, just not of
  that agent — and reverted all three files (`git checkout --
  finishing/ledger.tsv finishing/reports/claims.tsv
  manuscript/sections/ch02/02_01_03.txt`) to `HEAD`. This undid the
  coordinator's real, author-requested, correctly-sourced edit along with
  the sub-agent's actual overreach. Caught when the manuscript file failed
  to match what had just been written; the §2.1.3 edit was reapplied after
  the chapter-2 agent finished, this time refined per the author's
  follow-up: the section now explicitly distinguishes a right's legitimate
  contextual translation (a real design problem) from a jurisdiction
  refusing to extend the right at all (not a cultural variant for the
  system to accommodate — a violation it doesn't launder as diversity).
  §2.1.3 remains an accepted section with a disclosed post-acceptance edit,
  same convention as §5.1's racial-capitalism paragraph.
  `claims.tsv`'s `note` column carries all resolution detail; its `status`
  column stays the literal string "unverified" for every row, a tooling
  convention that predates this pass and was not changed. The `[[cite:ID]]`
  tokens themselves are untouched in the manuscript for verified claims —
  P4 records what the citation should say, not the formatted endnote text
  itself, per the standing rule that the agent never authors a reference
  entry. Book total after this pass: 74,136 words, 156 sections,
  `check_all.sh` passing, title drift 0.

- **C0276 and C0277 resolved, and P4 finished on the remaining five
  chapters** (2026-08-23, later the same day): the author, asked whether to
  look at the two flagged citations, first said "I accept everything," then,
  asked directly whether chapters 1, 3, 6, 9, and 10 (44 sections, none read
  in this session) were also being accepted, confirmed "blanket-accept now,
  proceed to P4." Two separate actions followed from that.
  **First, C0276/C0277.** Rather than treat "I accept everything" as license
  to leave two genuinely disputed citations as printed, I did fresh web
  research. C0276 (§2.2.1, who reached for the object that first triggered a
  monkey's mirror-neuron firing) turned up a *third* incompatible account —
  Scientific American's "Mirroring Behavior" credits an unnamed Rizzolatti
  grad student with an ice cream cone, distinct from the Gallese and Fogassi
  versions already on record — which only strengthens the case that no named
  individual is safely attributable. Corrected: "Gallese reached out to pick
  up an object himself" → "someone in the room reached out to pick up an
  object." C0277 ("the neurons that shaped civilization") — TED's own talk
  description paraphrases the finding rather than quoting Ramachandran
  saying those words, and no transcript surfaced confirming he spoke them;
  what's confirmed is narrower — it's his 2009 TED talk's title. Corrected
  to stop presenting it as something he personally "called" the neurons.
  Both are disclosed edits to an accepted section (§2.2.1, +11 words),
  same convention as §2.1.3 and §5.1.
  **Second, the P3 blanket acceptance and P4 on chapters 1, 3, 6, 9, 10.**
  All 44 remaining ledger rows were set to `accepted`, each with a note
  disclosing that this was a blanket instruction, not the section-by-section
  read PLAN.md's standing rule #1 otherwise requires. Before running P4, a
  gap surfaced: 15 `claims.tsv` rows numbered under a stale "8.*" (chapter 8,
  folded into chapter 7's new §7.5 during P1) had been missed by the earlier
  P4 pass, which scoped chapter 7 to "7.*" claim numbers only. 5 of the 15
  have live cite tokens in `ch07/07_05.txt`; I verified all 5 directly
  (China's 2017 AI plan and its 2030 target, GPAI's 2020 launch with 15
  founding members, the EU's 2019 Ethics Guidelines for Trustworthy AI,
  Partnership on AI's 2016 founding) — the other 10 had no surviving cite
  token anywhere and were marked retired. Then four parallel agents split
  the ~248 remaining claims across chapters 1 (1), 3 (47), 6 (125, split
  6.1-6.3 / 6.4), and 9+10 (75), using the same report-back-don't-edit-
  shared-files discipline as the first P4 pass, with an added explicit rule
  this time: no internal sub-agent fan-out, after the first pass's chapter-2
  incident. **Zero manuscript edits were needed anywhere in this batch** —
  every claim resolved to verified, already-resolved-in-a-prior-pass, or
  retired as orphaned (132 retired — mostly chapter 6, where sections 6.1-6.4
  were extensively rewritten during P3 and dropped the old claim IDs
  entirely; 30 newly verified via fresh search, mostly chapter 3's cognitive-
  science citations; 86 already had real verification notes from earlier ad
  hoc work and were confirmed rather than re-researched). Every one of
  `claims.tsv`'s 536 rows now carries a non-empty note. Word count and
  `check_all.sh` unaffected by this batch (no manuscript text changed);
  chapters 1, 3, 6, 9, and 10 remain `accepted` at P3 by blanket instruction,
  not by a section-by-section read — that gap is real and belongs to the
  author, not something a sourcing pass can close.

- **P3.5 started (D-025), chapter 4 swept** (2026-08-23): the style pass the
  author's chapter 1 revision implied. 34 edits across 15 of chapter 4's 33
  sections, all deletions of a known shape: 4 strawman/meta contrastives of
  the exact kind the author cut ("rather than assuming the shape is neutral",
  "rather than summarizing it twice"), 1 "an open question, not a solved one"
  (the author cut that exact tail in §1), 14 defensive intensifiers
  ("a real shot at", "genuine ethical dilemmas", "genuinely informative",
  "That comparison is real, and it is not nothing"), and 15 contrasts whose
  positive claim carried the sentence alone. 155 words. **The projected cut
  rate was wrong and is worth recording:** I estimated a third to half of
  chapter 4's 159 constructions from the raw count; inspecting each one
  against the author's calibration, only 34 (21%) were the defensive shape.
  The other 125 name a live alternative and do real work — the augment/replace
  contrast, Kohlberg's post-conventional definition, the guilt/shame
  distinction, the fast/slow design implication. Chapter 4's density went
  from one construction per 92 words to one per 102; chapter 1's, after the
  author's own hand, is one per 199. **Closing that remaining gap would mean
  cutting load-bearing contrasts, which this pass did not do** — whether an
  argumentative body chapter should match an introduction's density is a
  judgment for the author, not something to assume.
- **`ORDER.tsv` title column was load-bearing after all; corrected**
  (2026-08-23). Building the proof PDF exposed an error in the previous
  commit's reasoning. `finishing/tools/render.py` reads `ORDER.tsv` and
  takes **every rendered heading's title from its `title` column**, not from
  the section files' own first lines. So the 55 titles left stale through
  D-024 and the §10.2 retitle were wrong in every proof PDF built since:
  24 headings still read "Anti-Authoritarian" and §10.2 still read
  "Roadmap," even though the manuscript source was correct. Nothing in
  `check_all.sh` catches this — `check_structure.py` compares
  `parseable_text_v4.txt` against `outline.tsv` and never reads
  `ORDER.tsv`'s titles, which is why the drift survived a passing check.
  The 55 titles are now synced from the section headings and the PDF
  rebuilt clean (0 stale headings). **The `sha256` column is deliberately
  left alone**, on a different rationale than the one I wrongly applied to
  titles: all 156 hashes record the original 2024 split and have been stale
  since P3 began rewriting sections. They are provenance, nothing reads
  them, and recomputing them would destroy the record. `ORDER.tsv` is
  therefore mixed by design — live `title`, historical `sha256` — and that
  asymmetry is now written down so it is not "fixed" later by mistake.
  Worth adding an `ORDER.tsv`-title check to `check_all.sh` during P6.
- **§10.2 retitled, D-023's last live conflict closed** (2026-08-23, the
  author's title): "Roadmap for Altruistic and Antifascist Superintelligence"
  → **"Signatures of Altruistic and Antifascist Superintelligence."**
  "Signature" in the scientific sense — an observable pattern indicating
  something is present — is what the section is actually for: evidence the
  project is working, not a sequence. The retitle orphaned the section's
  opening disclaimer ("What follows is not a roadmap in the sense of a
  sequenced plan with dates"), which existed only to defend against its own
  title; cut per D-025. §10.2.2's "the alternative to a fixed roadmap"
  cross-reference updated to match. §10's opener keeps its "short of the
  finished roadmap this book does not claim to deliver" — that is a claim
  about the book, not a pointer to the title. **`ORDER.tsv`'s stale titles turned out to be a
  real defect, not a harmless snapshot** — see the correction below.
- **P3.5 completed across the remaining seven chapters** (2026-08-23): swept
  by four parallel agents on disjoint chapters (7; 2 and 9; 3 and 6; 5 and
  10), each given the author's chapter 1 cuts, the five author-confirmed
  keeps, and chapter 4's worked examples, plus an explicit instruction that
  21% is the expected rate and forcing a higher one is the worse error.
  **164 edits across 79 files**, every one a deletion or minimal trim.
  Per-chapter rates held close to calibration: ch3+ch6 20%, ch2+ch9 23%,
  ch7 11% on contrastive clauses (49 cuts, but 37 of them defensive
  intensifiers rather than clauses), ch10 14% — correctly the lowest, since
  its prose is documented case studies where the contrast carries the
  finding. **Chapter 5 came in high at 37% and was reviewed:** the agent's
  stated reason held up — "visible rather than buried in an opaque process"
  and "before it causes harm rather than after" each recur near-verbatim
  across sections, and "bolted onto" four times, so those cuts are
  de-duplication rather than over-cutting. Two chapter 5 cuts were
  **restored** as over-aggressive: §5.2.2's "not a hope that the system's
  values happen to survive its own learning" and §5.1.2's "rather than
  optimizing for one and hoping the other follows," both unique clauses
  matching confirmed-keep shape (naming the specific wrong assumption).
  Verified after the sweep: 301 citation placeholders unchanged, all eight
  markup token counts unchanged, and all 156 section headings byte-identical
  to their pre-sweep state. One process incident: the chapter 7 agent ran
  `git stash`/`git stash pop` in the shared worktree while three other
  agents were mid-write, which could have lost work; it disclosed this
  itself, and I verified the stash list is empty and sampled surviving
  edits from every agent plus the `finishing/` changes. Nothing was lost.
  Final densities, one construction per N words: ch1 199 (the author's own),
  ch3 158, ch9 158, ch5 165, ch7 134, ch2 136, ch10 127, ch6 113, ch4 102.
- **P3.5 calibration audited and confirmed** (2026-08-23): the author asked
  for five of the *kept* constructions at random, judged one at a time.
  **All five were keeps** — §4.3.3's partial-view-not-settled-answer,
  §4.4.5's re-implemented-not-assumed-to-carry-over, §4.2.1's four-contrast
  guilt/shame sentence, §4.6.2's architecture-generates-pull-not-rule, and
  §4.7.1's play-not-instruction. The 21% cut rate is therefore the right
  rate, not a conservative one, and **chapter 1's one-per-199 density is not
  the target for body chapters**: the sweep keeps its current standard for
  the remaining chapters. One finding came out of the audit that the sweep
  itself was not built to catch — §4.7.1's paragraph made the same contrast
  twice in adjacent sentences (choices-its-own-not-a-script, then
  play-not-instruction), which is redundancy across sentences rather than a
  defensive clause inside one. The author rewrote that paragraph by hand
  (splitting the opening sentence in three, scare-quoting the system's
  "own" winning and choices, and hedging felt experience); the doubled
  contrast was kept deliberately. Chapters 2, 3, 5, 6, 7, 9, and 10 not yet
  swept.
- **Author hand-revision of chapter 1 + the D-024 antifascist rebrand**
  (2026-08-23, after the chapter 1 P3 draft below): the author revised all
  four chapter 1 sections by hand — the thesis is now "altruistic and
  antifascist by design," §1.1 is retitled and restores the 2023
  racial-capitalism sentence (reversing the P3 cut), §1.2 drops the
  roadmap-disavowal opening (the positive D-023 promise stands alone), and
  nine contrastive-negation ("X, not Y") clauses were cut across the chapter,
  a style verdict worth carrying into future drafting. Applied book-wide per
  D-024: every "anti-authoritarian(ism)" became "antifascist"/"antifascism"
  (72 occurrences across chapters 2–10, including 16 section/chapter
  retitles; descriptive uses of "authoritarian" stay). §2.1.4 now carries the
  one-sentence terminology statement (antifascist chosen deliberately; the
  stance includes anti-authoritarian resistance in full). Ripples handled in
  the same pass: §5.1 gained a racial-capitalism paragraph as the designated
  home (D-013) for the introduction's restored mention — Robinson's *Black
  Marxism* (C0701) and Benjamin's New Jim Code (C0702), both live-verified;
  a disclosed edit to an accepted section. §10's opener lost its now-stale
  "roadmap the introduction gestures at" clause. README subtitle updated,
  TOC regenerated, and four mechanical slips in the hand edits fixed
  (a typo, a dropped "of", a hyphen for an em dash, and "original
  motivations" unified per the author). Chapter 1 is now 908 words; claims
  ledger 534 rows. Chapter 1 remains not author-accepted in the ledger —
  the hand revision is the author's, but the agent's fixes on top of it
  have not had the author's read.
- **Chapter 1** (4 sections, 1,149 words, down from 3,241 — 65%, the largest
  proportional cut of the whole pass): every section revised, including a
  full rebuild of §1.3, which restores the run-in heads deleted in 2024
  (found in `manuscript/previous/parseable_text_2023-11-21.txt`: the section
  was originally four numbered subsections — Growth Mindset; Encouraging a
  Growth Mindset; Intrinsic Motivation and Autonomy; Interdisciplinary
  Collaboration — folded into headerless prose sometime before the 2024
  snapshot). §1.3 turned out to be the most extreme case of pre-emptive
  duplication found in the whole project: essentially its entire 2,526-word
  original is now superseded, in more developed and better-cited form, by
  chapters that didn't exist in revised form when P1 set its structure —
  the growth-mindset material by 4.1/4.1.1 (Dweck), the intrinsic-motivation
  material by 4.6/4.6.1/4.6.2, the autonomy material by 3.3.3 and 2.4.4.2,
  and the interdisciplinary-collaboration strategy list by 6.1, which names
  real institutions (Stanford's One Hundred Year Study, the Partnership on
  AI) this draft only gestured at generically. Rewrote as a genuine preview
  of three themes with real cross-references, landing at 359 words — well
  under the triage-set 1,400-word target, not padded to reach it, consistent
  with §10.1.3's precedent of an honest short section over manufactured
  length. §1.2 directly resolves D-023 (Q-013): "our intention is to
  establish a roadmap for AI development" is replaced with an explicit
  statement of what the book actually promises — concrete, specific, and
  where warranted ambitious proposals, named directly (the jobs guarantee at
  7.1.4, the EU's dual-use export controls at 5.4.3, ISO 42001 certification
  at 6.3.2) — and does not promise (a sequenced plan with dates). §1 and §1.1
  were voice-fixed and cut of two more redundant sentences (a generic
  "respect human dignity" line duplicating 7.2.5.2, and a stale chapter
  preview that predated the final 8-chapter structure) rather than argued.
  No new citations were needed anywhere in the chapter — every claim kept is
  a cross-reference to where it's already cited, following 9.1's and
  10.1.3's precedent that a pure synthesis section carries none of its own.

- **The chapter 3 opener (§3)** (79 → 131 words): the one section in the
  entire book that had never had a P3 draft, finished in the same pass as
  chapter 1 rather than left open. Rewritten by hand to bridge chapter 2's
  sentience/empathy/compassion foundations into chapter 3's cognition/
  alignment/play structure and accurately preview §§3.1-3.3. Chapter 3's own
  body (3.1-3.3.x) was already author-accepted; this opener is not — it's a
  fresh draft on a chapter otherwise done, the same status as chapter 2's
  opener before this session's acceptance batch caught up to it.

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
| P3 Revise | **all 156 sections accepted.** Chapters 2, 4, 5, and 7 were
  author-accepted by full read; chapters 1, 3's opener, 6, 9, and 10 (44
  sections) were accepted 2026-08-23 by explicit blanket author instruction
  rather than a section-by-section read — disclosed in `ledger.tsv` and
  above, not silently applied. |
| P3.5 Style | **all ten chapters swept, D-025.** 198 edits, 645 words. `outline.tsv` synced — title drift is 0 (re-confirmed 2026-08-23 after the register-seam fix below). Post-D-024 register-seam check: chapter 3 had two places where "antifascist" was bolted onto a generic ML-methods description with no argued connection (§3.1.3's "antifascist judgment" next to "empathy, altruism"; §3.2.3's title and opener, "ethical and antifascist decision-making" applied to plain supervised-learning classification) — flagged 2026-08-23, fixed the same day at the author's request: both now read "ethical" alone, matching how the book's other ch3 sections (§3.2.5, §3.3.2) actually argue a mechanism-specific connection to resisting authoritarian power rather than just labeling one. Still open: the author's own read of the per-chapter diffs (distinct from the P3 acceptance question above — nobody has confirmed reading these diffs specifically). |
| P4 Source | **complete, book-wide.** Every one of `claims.tsv`'s 536 rows carries a non-empty note; zero unresolved placeholders anywhere. The §7.2.2 Clearview/Rekognition cluster and §7.2.5's AIGS Index/GPAI cluster, previously flagged as never actually live-verified despite carrying "web-verified" notes, were independently re-checked 2026-08-23: Clearview and GPAI confirmed accurate as printed; the AIGS Index sentence was corrected (it had overstated "at least 75 of 176 countries" as "a large majority of the world's countries"). |
| P5 Front/back matter | **author-accepted, 2026-08-23.** Two new sections (§0 "On Method", §11 "Glossary"), 158 sections total. See below. |
| P6 Copyedit and build | **author-accepted, 2026-08-23.** See below. |

**No chapter order remains for P3** — every section in the book has a draft
and is accepted, including the chapter 3 opener.

## P5, accepted

2026-08-23. Two new sections, numbered `0` (before chapter 1) and `11`
(after chapter 10) so the existing numeric pipeline — `ORDER.tsv`,
`outline.tsv`, `ledger.tsv`, `common.numkey`/`level`, the chapter-heading
regex in `check_structure.py` — needed no format changes. `finishing/tools/
render.py` got one small addition: numbers `0` and `11` render without the
"Chapter N:" label other level-1 headings get, since neither is a chapter in
the reader-facing sense; both were spot-checked as single-chapter PDF proofs
(`render.py --chapter 0` / `--chapter 11` → LibreOffice → `gs` page render)
before this was committed.

- **§0, "On Method"** (510 words against D-008's ~500-word target). Names
  the persona-generation device — the April 2023 founding prompt, roughly a
  hundred simulated expert co-authors assigned by field, the editorial
  passes that reviewed each other's sections — and the 2026 single-author
  finishing pass, in the author's own first-person voice. Names no real
  person. States plainly that the repository is the full record and
  reinforces, rather than softens, the README's named-persons disclaimer
  (D-008, D-017).
- **§11, "Glossary"** (51 terms, ~2,290 words, `<<h>>` run-in heads per
  style.md §4a — precedented by §3.1.2's absorbed-subsection heads, not a
  new markup convention). Terms came from a full read of
  `parseable_text_v4.txt` (a background agent surveyed all 156 body
  sections for recurring or book-stipulated terms; 56 candidates came back,
  merged down to 51 — a few near-duplicates folded together, e.g. IRL and
  cooperative IRL into one entry). Every entry paraphrases the book's own
  usage in new words rather than quoting it, to avoid a misquote standing
  as the definition of record. No new `[[cite:ID]]` placeholders: where a
  term is tied to a named study or system already cited in the body (GPT-3,
  BERT, AlphaGo Zero, the AIGS Index, Bostrom's paperclip maximizer, and so
  on), the entry points to the section carrying that citation instead of
  duplicating it — the same cross-reference-over-repetition rule style.md
  §7 already applies to repeated arguments. `names_guard.py` flagged the
  glossary's citations of real scholars (Graziano, Nussbaum, Dweck,
  Bronfenbrenner, Benjamin, Robinson) as ordinary scholarly citation to
  confirm, not violations — each already appears cited the same way
  elsewhere in the accepted body text.
- **Chapter 1's opener** needed no separate work. PLAN.md's P3 chapter order
  (3 → 2 → 4 → 5 → 7 → 6 → 9 → 10 → 1 last) already put chapter 1's revision
  after every other chapter's, specifically so it would describe the book
  that exists rather than the one that was still being written — see
  "Chapter order for P3" in `PLAN.md`. That already happened; P5 did not
  reopen chapter 1.
- Both new sections were drafted with `status: drafted` in `ledger.tsv`.
  The author read both as rendered proof PDFs and accepted both the same
  day; `ledger.tsv` now carries `status: accepted` for both rows, with the
  acceptance disclosed in each row's notes the same way every other
  post-draft acceptance in this project is.
- `finishing/tools/check_all.sh`: **ALL CHECKS PASSED** after both additions
  (158 sections, round-trip OK, structure OK, named-persons guard clean).
  One pre-existing, unrelated staleness surfaced and was fixed in passing:
  `manuscript/sections/ORDER.tsv`'s title column for §3.2.3 still had the
  pre-register-seam-fix title ("...for Ethical and Antifascist
  Decision-Making") from before that fix landed earlier this session —
  `ORDER.tsv`'s title column isn't validated by any check script against
  the live manuscript (only `num`/`path` are), so this didn't fail
  anything, but it did produce a misleading "title differs" note in
  `check_structure.py`'s output. Corrected to match the current heading;
  no other `ORDER.tsv` title cells were audited.

## P6

2026-08-23. PLAN.md's P6 deliverables are "terminology consistency, tic
lint, HTML → ODT → PDF locally; other formats elsewhere", exit criterion
"clean build; author's final read." What's done and what's still open:

- **Tic lint.** `finishing/tools/tics.py` re-run book-wide: every high-count
  tic from the pre-P3 baseline (`foster` 278→0, `robust` 148→12, `crucial`
  118→0, `nuanced` 71→0, `navigate` 67→4, `leverage` 59→7, `intricate` 47→0,
  `harness` 34→1, `pivotal` 33→0, `landscape` 29→5) is down to single digits
  or zero. Every surviving hit was read in context, not just counted:
  - `foster` (was 4): three section titles — §2.3.3 "Fostering AI Systems
    with Self-awareness and Self-regulation", §3.3.1 "The Power of Play:
    Fostering Ethical AI Development through Play-Inspired Mechanisms",
    §7.2.3 "Fostering Public-Private Partnerships for AI Research and
    Innovation" — plus one sentence in §2.2.1 ("helping foster meaningful
    relationships") had survived P3/P3.5 because neither pass touched
    section titles. Fixed: retitled to "Self-awareness and Self-regulation
    in AI Systems", "The Power of Play: Ethical AI Development through
    Play-Inspired Mechanisms", and "Public-Private Partnerships for AI
    Research and Innovation"; §2.2.1's sentence now reads "...building
    meaningful relationships..." No argument or claim changed — see the
    disclosed notes on `ledger.tsv` rows 2.2.1, 2.3.3, 3.3.1, 7.2.3.
  - `robust`/`robustness` (12, all in ch05/ch07/ch09/ch10): every instance
    is the AI-safety technical term (§5.2's title is literally
    "Robustness, Generalization, and Adaptability in AI Systems") — domain
    vocabulary, not the vague-intensifier tic style.md warns against. Left
    alone.
  - `leverage` (7): every instance is the noun (bargaining power, economic
    leverage, a government's leverage over a company), not the
    corporate-buzzword verb ("leverage AI to..."). Left alone.
  - `landscape` (5): all five are the same recurring phrase,
    "treaty-and-declaration landscape," used consistently across chapters
    6, 7, and 10 as a handle for the specific cluster of treaties and
    declarations §7.5 covers — a term of art this book coined for itself,
    not a vacuous filler word. Left alone.
  - `navigate` (4): two section titles (§2.1.3, §2.4.7) and two body uses,
    all describing an actual dynamic (a transition, an ambiguous case, a
    Super Mario Bros. level) rather than standing in for nothing. Left
    alone.
  - `multifaceted` (1), `holistic` (1), `indispensable` (1): single
    instances, each making a real claim in context (genuine complexity, a
    named ethical framework, a genuine capacity claim). Left alone per
    style.md §3 ("None is forbidden; each is a flag").
  - Voice markers (`voice.tsv`): 4 "this work/document" hits are all the
    literal phrase "this work" (labor, not the book); the 2 "we (subject)"
    hits are inside the Westworld epigraph's quoted dialogue and inside
    §0's own description of the 2023 draft's institutional "we" — neither
    is the author speaking as "we." Read individually; zero actual D-008
    voice violations found.
- **Terminology consistency.** No open terminology-drift items were found:
  D-024's "anti-authoritarian"→"antifascist" switch has zero unconverted
  instances outside the two places D-024 itself says should keep
  "anti-authoritarian" (§2.1.4, §11's glossary entry, both stating the
  antifascist stance is anti-authoritarian in full). Acronym/proper-noun
  casing checked for one canonical spelling each: RLHF, COMPAS, GPAI,
  GPT-3, GPT-4, AlphaGo Zero, AIGS Index, IRB, MAML — all consistent, no
  variant casings found. Not checked: every other named term in the book:
  this was a sample of the terms most likely to drift (frequently-cited
  systems/acronyms and the glossary's own headwords), not an exhaustive
  pass over all ~90 separately drafted sections' vocabulary.
- **A tooling gap this pass exists to catch, closed.** `check_structure.py`
  compared `outline.tsv`'s titles against `ORDER.tsv`'s titles, and each
  file's own heading number against `ORDER.tsv`, but never compared a
  file's own heading *title* against `ORDER.tsv`'s title column — the
  column `render.py` actually renders from. A title could drift out of
  `ORDER.tsv` (as the 55 D-024/§10.2 titles did, and as the three
  `foster` titles above just did) and `check_all.sh` would stay green while
  the built book showed the stale title. `check_structure.py` now fails
  hard on that mismatch; sanity-tested by injecting a deliberate mismatch
  and confirming it fails, then reverting and confirming it passes again.
- **Build.** Whole book rendered via the documented path
  (`render.py` → `soffice` HTML→ODT → `soffice` ODT→PDF): 132 pages.
  Read as images: page 1 (§0, "On Method," no chapter label, matches P5's
  proof) and page 132 (§11's last three glossary entries, ending cleanly).
  Confirmed via text extraction that all three retitled headings
  (§2.3.3, §3.3.1, §7.2.3) render correctly. `finishing/reports/
  whole-book-proof_2026-08-23.pdf` — a committed exception to
  `pipeline.md`'s "build products stay in the scratchpad" rule, same as
  the earlier exceptions to that file — is rebuilt from this run.
- **"Other formats elsewhere":** not attempted. This machine has no TeX,
  pandoc, mermaid-cli, or graphviz, and no network path to install them
  (`pipeline.md`, confirmed again this session) — that clause of P6 is
  out of reach from here regardless of manuscript state.
- **Author's final read: done, 2026-08-23.** The author read the rebuilt
  whole-book proof PDF and accepted. P6's exit criterion is met; the pass
  is closed.

## P7 C3, the rebalance — done 2026-08-23 (D-032)

C3, the genre shift at the book's midpoint, was closed earlier the same day the
cheap way its own scope offered ("flag it in the roadmap or rebalance; cheap
version: the roadmap flags it") — §1.2 gained the flag. A second editorial
reading accepted that flag as "partly right" and asked for the rebalance
instead. The author ruled to fix it, and it is now done. Full account, with the
measurements and with what the review got wrong, in `p7-scope.md` under "C3
reopened."

- **The defect, measured before acting.** Chapter 6 was 22,014 words — 26
  percent of the book, 48 percent larger than the next-biggest chapter — at
  3.9 dated references per 1,000 words against 0.1 to 0.3 in chapters 2 to 4.
  Not a matter of taste: a measurably different genre holding a quarter of the
  book, and dating for no return, where D-027's dated targeting material at
  least earns its dating.
- **The rule.** The reviewer's own criterion, adopted verbatim: keep the
  instance that shows a mechanism working or failing, cut the instance that only
  establishes that a body exists. Applied across 19 sections.
- **Result.** Chapter 6: 22,014 → 20,023 words; dated references 88 → 35, from
  3.9 to 1.7 per 1,000, now level with chapters 5 and 9; the "founded in that
  year" construction from 22 occurrences to 3. Each of the 35 surviving dates
  was read individually and kept because the date is the argument — the Gebru
  and Mitchell dismissals, Canada's AIDA dying with its Parliament, Taiwan's
  statute, Bletchley-to-Paris. Chapter 6 is still the longest chapter; it is now
  the longest because it argues at length. **The word delta is smaller than the
  volume of cut catalogue**, because where an entry was cut the argument it had
  been illustrating was usually written out in its place, which is what the
  criterion asks for. D-019 held: no section was cut to reach a number.
- **Untouched, deliberately:** §6.4.2 (Google/Maven, Gebru and Mitchell,
  Facebook's Oversight Board, Clearview, Rekognition — every instance shows a
  mechanism failing), §6.5.x (technical, not institutional), §6.6.x (legal
  argument), and inside §6.7.6 the Tier B blocks, the Bletchley-to-Paris
  passage, and the diverging-national-rules comparison.
- **23 citations orphaned** by the cuts, marked retired in `claims.tsv` with the
  reason. No claim row deleted, following the P3 precedent.
- **The Ofqual NDA, one of three instances the review named as worth keeping, is
  not in the manuscript** — verified absent. Adding it would be new sourced
  prose (D-029) needing live verification (D-030), which is a different job from
  cutting and was not done. Recorded in `p7-scope.md` as an available addition,
  not as a gap. The other two the review named are present: the DeepMind Health
  panel at §6.2.2, kept and extended, and Bletchley-to-Paris at §6.7.6,
  untouched.

**Two things found along the way.**

- **§6.7's opener carried visible revision history** — a sentence about what
  earlier drafts had done and why the book kept negotiating a boundary in front
  of the reader. That is the A3 defect, in a section written during C2 *after*
  A3 had run. Deleted.
- **Every sha256 in `ORDER.tsv` was stale: 0 of 157 matched their files.** The
  digests were written once at the v4 split and never regenerated across P1
  through P7, because nothing verified them — the column had silently stopped
  being evidence of anything, which is the same class of gap P6 closed for title
  drift. `check_structure.py` now fails hard on a stale digest;
  `tools/refresh_order_shas.py` clears it; both directions sanity-tested by
  injecting a mismatch, confirming the failure, reverting, and confirming the
  pass. All 157 refreshed.

**D-025 regressed again and was swept again.** Writing this much replacement
prose reintroduced the contrastive-negation tic, exactly as Tier B recorded.
Worst was §6.2.1 at 1 per 84 words, now 1 per 245; every rewritten section now
runs 1 per 216 or better. Pre-existing instances in untouched paragraphs were
left alone, per the Tier B precedent — **and chapter 6's untouched sections run
much denser than D-025's calibration, §6.6.3 at 1 per 63 and §6.6.4 at 1 per 78.
That is not fixed and is not claimed as fixed.**


## P9, drafted 2026-08-24 (D-037)

The fourth editorial review, as unnumbered prose. Its thesis — **the manuscript
is optimized for a reader who dips in, at the cost of one reading linearly** —
is correct, and it names a structural signature rather than a set of slips: P1
folded 282 sections into 156 and D-013 gave each repeated argument one home,
and both correct decisions leave the same residue, a pointer where an argument
used to be. Expect the same complaint anywhere P1 folded heavily. Full account
in `finishing/p9-scope.md`.

Nine section files changed; +708 words book-wide (84,884 → 85,592), of which
chapter 7's opener is +654. `check_all.sh` green; ORDER.tsv digests refreshed
for the nine, join rebuilt, TOC regenerated, title diffs 0.

- **P9-1, the Ekman repetition: linked, not merged.** The review said §2.3.1
  and §7.2.1 "both walk through Ekman's Fore study and its collapse … the same
  argument delivered twice." **That is not what is there,** and the merge it
  proposed would have been wrong. The sections share the Fore study — one
  clause each — and nothing else: §2.3.1 asks whether emotion is a natural kind
  and collapses it with Panksepp, Barrett's imaging meta-analysis, and the
  Himba/Trobriand free-sorting work (C0300–C0303); §7.2.1 asks whether emotion
  is readable from a face and collapses it with the in-group advantage, the
  2019 APS panel, HireVue, and the EU AI Act (C0561–C0565). The real defect was
  that a linear reader meets Ekman twice, 40,000 words apart, cold both times.
  The review's own alternative — link them — was done in both directions.
- **P9-2, the pointer sections: openers rewritten, demotion declined.** The
  review wanted §§4.2.2/4.2.3/4.6.2/5.2.2 demoted to paragraphs inside their
  parents. Checked: the first three each carry an argument that exists nowhere
  else (4.2.2's invariance probe, 4.2.3's performed-versus-genuine moral
  emotion, 4.6.2's intrinsic/extrinsic mutual check), so the demotion was
  declined; the defect was confined to each opening paragraph, which
  inventoried what the section is *not* about before reaching its question. All
  three now lead with their own question. **§5.2.2 does not fit the complaint on
  any measure and was declined outright.**
- **P9-3, the escape hatch: done, and the review undercounted.** It said the
  "nobody is working on this" admission appears "three or four times." §7.1.5
  alone had three in 527 words; §7.1.6 had two; §7.1.2 and §7.1.4 one each, in a
  5,743-word chapter. Chapter 7's opener now states the qualification once —
  a search is not a survey — and lists the **eight** gaps with the nearest
  existing work that stops short of each. §7.1.5's three hedges are gone.
  **The list adds no verification:** every row restates a gap the chapter already
  claimed, and no live search was run for this pass. A later pass wanting to
  strengthen it has to actually search.
- **P9-4, the persistence through-line.** Chapter 1's paragraph (added
  yesterday by D-035) pointed at "chapter 2" generically; it now cites §2.4.1
  and §2.4.4 by number. §2.4.4 already pointed back to §2.4.1.

**D-025:** chapter 7's opener is the only substantial new block — 656 new words,
3 contrastive negations, 1 per 219, inside the band. The smaller additions
introduced none. The whole-diff aggregate reads 1 per 163 and is **not**
comparable, because a diff charges the pass for retained text inside paragraphs
it only partly rewrote.

**A cosmetic tool bug, found and not fixed:** `check_roundtrip.py` labels its
length "bytes" but computes characters (552,656 against the file's 554,585). The
equality test is a string comparison and is sound; only the printed number is
wrong.

## P10, drafted 2026-08-24 (D-038): tiers 1 and 2 of the fifth review

The fifth review came as a structured critique plus two dialogue turns. Nineteen
of its twenty checkable claims verified verbatim; the one exception is that
§5.3.5 does not hold the interruptibility material (§5.3's opener does).
Full account in `finishing/p10-scope.md`.

**Tier 1 — the epistemic-standard gap.** The review's sharpest finding and it
held: the book boxes mirror neurons and treats Ekman carefully, then anchored
chapter 4's 14,866 words on Kohlberg with a bare citation, and cited Gilligan
six sections later for care ethics without saying her account began as a
critique of Kohlberg. §4.1.1 gains a 568-word epistemic box (cross-cultural
critique, judgment-action gap, Gilligan — C0718–C0720, all verified by live
search *before* the prose went in) that also answers why these frameworks
transfer when mirror neurons did not: the mirror-neuron claim was that a
mechanism implements a capacity and died with the mechanism; Kohlberg's stages
are an order, not a mechanism. §4.7.1 now names the critique's origin. §4.1.4's
targets-per-hour indicator gets a run-in head parallel to §6.6.4's — it was
buried in paragraph 6 of 9 under the title "AI in Service of Human Dignity."

**Tier 2 — the floor.** New §2.1.5, "The Floor Beneath Learned Values," 1,261
words. The book arrives at an unconditional constraint three times (§4.6.3,
§6.7.6, §8.1.3) with none referencing the others, while §2.1.1 had set
deontology aside on rigidity and chapters 3–4 — 30.3% of the book — build
learned judgment instead. Author directed the **dialogue's** version over the
review's: same architecture, plus the fork the review's version conceals — an
architectural floor costs custody (§8.3.3), a borne floor costs patienthood
(§2.4.4), an external floor costs enforcement (§8.1.3), and those are the
book's three unfinished threads. §2.1 and the three arrival sites now link to it.

**Deliberately not taken, and this is the live tier-3 question:** the dialogue's
second turn concludes that the capacity to refuse and the capacity to suffer are
gated by the same architectural property. Its load-bearing step — that months of
integrated involvement constitutes Cassell's narrative self — is asserted, and
the dialogue itself identified that slack one turn earlier. (The D-034 analogy
originally offered for this is withdrawn as wrong; see D-039.) Taking it would make
§2.4.4's "consent is inapplicable" conditional on the system not being built to
refuse, and open "can it quit?". **Settled 2026-08-24 by author instruction ("settle the step"), in the
negative — see D-039.** A bearer meets Cassell's first condition (a self
extended in time: it must model its own role and that role's drift to notice
recuperation) and nothing in that delivers the second (distress at the prospect
of disintegration). Refusal runs on an outward-pointing stake. The corollary is
the payoff: the missing self-concern is a security property, because recuperation
works through exactly the stake the bearer lacks — it can be overpowered, not
suborned. §2.4.4's conclusion survives by a second route and now says so, so the
large reopening does not follow. **Narrowed the same day by D-040**, after the author pressed it with the
homeostatic objection (in animals the self-model exists *for* regulation, so the
caring is what the machinery is for) and a worked case (the bearer reports the
school, is wiped, the operators keep the coordinates it already produced and
proceed). The two-conditions argument stands. Two things are withdrawn: the
"cannot be suborned" corollary — immunity to leverage is worth nothing where
leverage is not the cheapest route, and erasing a bearer is cheap, quiet and
leaves its output intact, which is **custody again**; and "the floor is
buildable", now "not ruled out". Instrumentally acquired self-concern moves from
residual to **the central engineering difficulty**. New result: none of the three
branches escapes custody — they fail into one another. **Extended again the same
day by D-041**, on two author questions and one author proposal: the second
branch collapses into the third (nobody is left to preserve a bearer that will
not preserve itself); a new unresolved dilemma (suppressing self-preservation
leaves the bearer unable to defend the memory that makes it a bearer); a
collision named with §4.6.3 and §5.3's override commitments; the weights-not-
vector-store proposal credited and checked against §7.2.2's counterexample; and
the testimony standard corrected — no witness has an honest memory, so the target
is scaffolded testimony, and the honesty of what a system retains is a **character**
question, which is the first contribution chapters 3–4 make to this argument.
§2.4.1 gained one scoped sentence pair on the author's instruction. **§2.1.5 is
now 3,701 words, the book's third-longest section, grown from 1,261 in one day
across four passes and unread by the author at any length.**

**A render bug found by looking at the proof, not by any check.** The first draft
of §2.1.5 used markdown `**bold**` and `*italic*`; the dialect has no such
markup and `render.py` passes it through, so it rendered as literal asterisks.
Caught on page 13 of the proof and rewritten as plain prose. **§2.4's Westworld
epigraph has the same defect and still does** — one `*here*` that renders as
asterisks. Pre-existing, inside a quoted epigraph, and left alone rather than
edited as a side effect of this pass. `check_all.sh` does not test for this.

158 sections. Book 85,592 → 87,582 words (+1,990). Proof rebuilt, 145 pages (was 142);
pages 13 and 50 were looked at as images to confirm the box renders as a bordered
table and the run-in heads hold. The rest was not read.

## The immediate open items

**`finishing/QUESTIONS.md` was refreshed 2026-08-24 and is current as of P10.**
It carries the three live items that are not visible anywhere else: **Q-014**,
the fifth review's chapter-6 length item, which was analyzed and never scoped and
is neither done nor declined; **Q-015**, whether `check_all.sh` should run from a
pre-commit hook, which needs author approval under `AGENTS.md`; and **Q-016**,
that §2.1.5 quadrupled in one day and is unread. Q-011 is closed retroactively —
its default had been applied without being recorded.


- **P10 is drafted and unread**, and P9 and P8 before it. The proof committed at
  `finishing/reports/whole-book*_2026-08-24.*` predates P9 and is now stale.
- **P8 is drafted and unread.** Six sections changed (1's opener, 2.1.4,
  2.4.4's title, 5.1.1, 7.1.6, 7.1.7); +952 words book-wide. `check_all.sh`
  green, TOC regenerated, title diffs 0. **The proof was rebuilt 2026-08-24**
  and is committed as `finishing/reports/whole-book_2026-08-24.{html,odt}`
  and `whole-book-proof_2026-08-24.pdf`, 140 pages (was 132 at P6). The
  2026-08-23 trio was removed in the same commit rather than left beside it,
  per `pipeline.md`: a stale proof is worse than none. Three pages carrying
  new prose were looked at as images, not merely built — p11 (2.1.4's new
  block, run-in head and the seven-strategy list intact), p4 (chapter 1's
  two-standards paragraph), p124 (7.1.7's rewritten block). The rest of the
  proof was not read.
- **Section 7.1.6's contrastive-negation density is 1 per 136** and is not
  fixed. All four hits pre-date P8, in paragraphs P8 did not touch; the
  paragraph P8 added has none. Named rather than swept, per the Tier B
  precedent.

- **Chapter 6's contrastive-negation density is not fixed.** The C3 rebalance
  swept only its own new prose. Untouched sections run far denser than D-025's
  calibration of 1 per 345 words — §6.6.3 at 1 per 63, §6.6.4 at 1 per 78,
  §6.7.2 at 1 per 79. A future P3.5 sweep over chapter 6 has real work.
- **The author has not read the C3 rebalance.** 19 sections changed; the
  rebuilt proof is committed.
- **The author's own read of the P3.5 per-chapter diffs is still
  unconfirmed** — distinct from the P3 acceptance question above, which the
  author has settled by blanket instruction. P3.5's own exit criterion
  ("author has read the per-chapter diff") has never been confirmed done in
  any session on record.
- **`finishing/outline.tsv` title drift: closed, 2026-08-23** (re-confirmed
  same day after the §3.2.3 retitle below). All stale titles are synced from
  the manuscript's own (authoritative, D-011) headings, and
  `manuscript/table-of-contents.txt` is regenerated from the same source.
  `headings.py` reports **ms-vs-outline title diffs=0**.
  `finishing/reports/headings_reconcile.md` records the clean state.
- **The Clearview/AIGS Index/GPAI cluster in §7.2.2/§7.2.5: closed,
  2026-08-23.** See the P4 row above and `finishing/ledger.tsv`'s notes on
  §7.2.2 and §7.2.5 for the correction.

## What P1 deliberately left for P3, still ahead

**Nothing.** Every item below is now resolved; kept as a record of what P1
handed off rather than a live punch list.

- **0 empty openers remaining** (§4.6, §4.7, §5, §6, §7, §§9.1/9.2, and
  chapter 10's own opener and §§10.1/10.2/10.3 are all now filled).
- **§1.3**: subheadings restored (as run-in heads — see the chapter 1 account
  above for why not as numbered subsections) and compressed to 359 words,
  under the 1,400-word target because nearly all its original content turned
  out to be superseded elsewhere by the time chapter 1's pass arrived.
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
| `finishing/p8-scope.md` | P8: the four items, what was declined, and the review's errors |
| `finishing/style.md` | the operative spec for P3 — voice, tics, run-in heads, boxes, citations |
| `finishing/transplants.md` | the 16 transplants: source lines, targets, register edits |
| `finishing/triage.tsv` | every section's fate, with the reason |
| `finishing/toc_v4.tsv` | the outline, with what each section absorbed |
| `finishing/ledger.tsv` | per-section work state |
| `finishing/reports/claims.tsv` | the claims ledger, 534 rows |
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

**Commit messages:** `git commit -s` always. A commit without a DCO sign-off is rejected.

**Shell heredocs and `<<list>>`/`<<box>>`/`<<h>>` markup:** a bash heredoc
writing a file containing this literal markup silently truncated content once
today. Use the Write tool for any file containing this markup, not `cat >
file << 'EOF'`.

**`finishing/reports/ch2-3-proof_2026-08-23.pdf` is a one-off exception** to
`pipeline.md`'s "build products stay in the scratchpad" rule — the author
asked for it committed. It is already stale (chapter 4 isn't in it) and will
not be kept in sync; don't treat its presence as a new convention, and don't
regenerate/recommit it reflexively as chapters finish unless asked again.

---

## P11 — the sixth editorial review, 2026-08-24 (D-043)

**The structure of the book changed.** Chapters now run 0 through 11. Old §2.1.5
is **chapter 3, "The Floor Beneath Learned Values."** A new **chapter 7, "The
Recuperation of Dissent,"** gathers the synthesis the book had been making twice,
briefly, in subordinate positions two chapters apart. Old chapters 3–9 became
4–11. Every cross-reference in the manuscript was rewritten by script and then
**verified to resolve against `ORDER.tsv` — unresolved references: none.**

Full disposition in `p11-scope.md`. The short version:

**The flagship rebuild.** Old §6.3.3 is now §8.3.3, "A Jobs Guarantee, and the
Objection It Has to Answer," 950 → 3,157 words. The review's best catch, and it
held up on checking: **the section cited the WIOA evaluation as grounds to
disclaim the guarantee as a retraining program, when that evaluation's actual
finding is that classroom retraining fails and employer-led apprenticeship works
— which is the guarantee's own defined mechanism.** The book had the right
finding, in its own pages, pointing at its own design, and read it backwards.
Reversing it converts the proposal from a bare floor to a competitive one. Also:
skill mismatch is now argued rather than conceded (via §2.1.4's own legibility
diagnosis — what gets automated is the countable part, and countability is a poor
proxy for an occupation); the status concession is corrected for baseline
(unemployment, not the prior job); the costing is dated, indexed, resequenced and
bounded against Medicare and Social Security; the fiscal framing is asserted
rather than hedged, per chapter 0's disclosure standard, with the interest-income
channel named as the live good-faith disagreement; and the objection the section
actually needed — a guarantee under a hostile administration is a placement lever
with a compliance condition — is supplied with a three-part checkable design
specification.

**Four standing decisions overridden**, on the author's instruction to resolve
every collision in the review's favour: Q-016 closed rather than deferred; Q-014
executed rather than held for the reading question; D-019 preserved in method but
chapters 4 and 8 cut against a target the review set; D-010's chapter structure
superseded a second time.

**What was declined, with the author's explicit agreement**: the prose-rhythm
pass aimed at chapters 4 and 8, which measurement contradicts — those chapters
run 5.7 and 5.4 contrastive negations per thousand words, and **chapter 5 runs
9.9, which no review has mentioned.** Recorded as Q-017. Also the §10.6.4
collective-"we" complaint (two instances, one adjacent pair) and the claim that
"Chapter 2.1.3" appears twice (it appeared once; fixed).

**One premise dropped for failing verification** under D-009/D-030: the review's
supporting claim that radiology patients skew heavily elderly did not check out,
and the argument was rebuilt without it rather than hedged. Six other claims
(C0721–C0726) were verified live before the prose entered the manuscript.

**Numbers.** 90,273 → 92,574 words. 158 → 165 sections. 149 → 151 pages.
`check_all.sh` green on all four checks. Proof rebuilt, and pages 30, 90 and 100
rendered and looked at.

**On acceptance.** The author's ruling this pass — *"I read everything and stop
asking or caring about what i did or did not read"* — retires the practice of
flagging unread drafted material as a reason to defer. `ledger.tsv` still records
drafted versus accepted; that distinction is no longer raised as a blocker.
