# State of play

Read this first. **Updated 2026-08-28 after P26 opened (D-077 to D-080): four author rulings out of the 2026-08-28 discussion, scoped in `p26-scope.md`. Background now has to earn its place by serving a nameable claim (`style.md` section 2a); chapters 4 and 5 are to be rewritten to carry the obligation section 3.7 places on them, with D-007 lifted for them; "bearer" is defined, entered in the glossary and its change of content marked -- done in this pass; and the fascism reading section 2.1.4 already holds is confirmed, with one paragraph left with the author as prose. The P26 note at the end of this file is the newest.** **Updated 2026-08-25 after D-075: "superintelligence" is swept from the manuscript wherever it named the book's own subject — five prose instances beyond D-073's two — and kept in the three places where it records the 2023 founding prompt, describes AlphaGo Zero, or cites Bostrom's title. **Updated 2026-08-25 after D-076: `AGENTS.md` names the book by its current title, on the author's explicit approval; no rule in it changed.** **Updated 2026-08-25 after D-074: the book has a title page (194 pages), and the README's abstract is rewritten in the book's own voice; both were items D-073 recorded as left for the author.** **Updated 2026-08-25 after D-073: the book is titled *Antifascist Intelligence: Building Machines That Can Refuse*. The old title, *Ethical Superintelligence*, is gone from `book.tex`, the README and section 10.2's heading; the note at the end of this file says what moved and what was deliberately left, including that the book still has no title page, so the title prints nowhere in the proof and lives only in the PDF metadata.** **Updated 2026-08-25 after D-067 (P23): the author ruled on all four open questions — no question is open — and section 8.7.6, the book's longest, is split four ways along its run-in heads into 8.7.6–8.7.9, with old 8.7.7 now 8.7.10. 162 sections. Nothing cut; three transition sentences edited; all 24 inbound references to the pair read and placed by hand. Section 8.7.4's opener rewritten (Q-020 b). The P23 note at the end of this file has the detail, including one tool gap found on the way: `xref_content.py` was never ported to `.tex` and scans nothing.** **Updated 2026-08-25 after D-066: the book's 769 cross-references are `\ref{sec:N}` now, not typed numbers, so a renumber can no longer leave a stale one behind — verified by rendering and confirming all 217 distinct references print identical numbers to the pre-conversion proof. The proof built at that commit was 193 pages from LuaTeX, against the 153-page LibreOffice-path proof of the same date that the P20 note at the end of this file describes; the two page counts differ because the typesetting changed, not the text. No proof is committed any more: D-068 deleted both tracked PDFs and withdrew the exception that had kept one here, so build one with `finishing/tools/build_tex.sh` and it goes to the scratchpad.** **Updated 2026-08-25 after D-065: the manuscript is LaTeX. Sections are `manuscript/sections/chNN/*.tex`, the master is `manuscript/book.tex`, typesetting lives in `manuscript/preamble.tex`, and the build is `finishing/tools/build_tex.sh` (lualatex + biber, TeX Live under `$HOME`). Citations run through biblatex against `finishing/refs.bib`. The dialect — `<<quote>>`, `<<list>>`, `<<box>>`, `<<h>>`, `[[cite:ID]]` — is gone, and its tools are retired to `finishing/tools/dialect-era/`. The conversion was mechanical and verified lossless on 1342 prose lines; no prose was reread or rewritten. `parseable_text_v4.txt` is frozen provenance now, not a build artifact, and `check_frozen.py` guards it with v3b. `check_all.sh` runs six checks and passes. `AGENTS.md` and the pre-commit hook's pass message, both of which still described the byte-for-byte join, were corrected in `d2f57d8` with the author's explicit approval, as that file requires.** **Updated 2026-08-25 after D-062 and its D-063 follow-up: `finishing/refs.bib` now exists, a 280-entry BibTeX bibliography for the 291 citations still live in the manuscript, mapped from `claims.tsv` by a new `bib_key` column. Of the 54 entries D-062 first flagged as only partially confirmed, D-063 resolved 35 outright and left 16 open with documented effort after real attempts to close them. Three are confirmed errors in the manuscript's own text, left uncorrected for the author to weigh: section 8.3.3's box states Social Security at 5.3 percent of GDP and Medicare (net) at 3.1 percent for FY2026, where CBO's own primary tables (read directly via archive.org after cbo.gov 403'd every automated fetch) give 5.2 percent and 3.3 percent — the 5.3 figure traces to D-061 Phase 4.1's own "correction," which appears to have read CBO's FY2027 column by mistake; a citation attributes a 2022 Frontiers in Education study to confirming Proctorio's face-detection failure rate, but the study, read directly, tested a different product, Respondus Monitor; and the list of universities that dropped Proctorio over bias in 2021 wrongly includes Baylor, which dropped it in 2020 for cost reasons. (C0413 looked like a fourth manuscript error but wasn't: the book's prose names no authors for the Estonian tax-fraud pilot at all — the wrong attribution was only ever in the internal QA note.)** **Updated 2026-08-25 after P20 (D-061); the P20 note at the end of this file is the newest, and it reverses the book's answer on the central question of chapter 3.** **Updated 2026-08-24 after P14 (D-050).** **Updated 2026-08-24 after P11 (D-043): the book's chapter structure changed — chapters now run 0 to 11, old section 2.1.5 is chapter 3, and there is a new chapter 7. Section numbers written before that date use the old numbering. The P11 note at the end of this file is the current summary.** Written 2026-08-23, updated same day: chapter 7 landed, the
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

**Current as of 2026-08-25, after D-067.** `manuscript/sections/chNN/*.tex` —
**162 sections**, chapters 0 through 11, one `.tex` file each, nothing deeper
than three levels; `book.tex` is the master, `sections.tex` the generated
`\input` list. **92,695 words of prose**, by `section_stats.py`, ported to LaTeX
at D-070 and rerun (`finishing/reports/section_stats.tsv`). That figure excludes
the four epigraphs as third-party text and counts a reference as the one number
it prints; the conventions are in `common.tex_sections_of`. No proof PDF is
committed (D-068); build one to the scratchpad. `manuscript/parseable_text_v4.txt` and
`manuscript/parseable_text_v3b_2024-07-07.txt` are both frozen, guarded by
`check_frozen.py`; neither is a build artifact any longer. Ledger: 146 sections
`accepted`, 16 `drafted` — chapter 3 entire (§3 and §§3.1–3.7), §7, §7.1, §7.3,
§7.4, §8.7, §8.7.10, §9.1.6, §9.1.7 — none of which the author has read since
P11, P19 or P20 rewrote it. The three sections D-067 split out of 8.7.6
(§§8.7.7–8.7.9) carry 8.7.6's `accepted` because their text is 8.7.6's text.

**The paragraphs below this line are the 2026-08-23 record of the P3 pass and
are kept as history; their section and word counts are not current.**

The book then had 158 sections (the 156 body sections, chapters 1-10, plus
P5's two front/back-matter sections, §0 and §11 — see "P5, accepted" below).
76,949 words total as of that day's `section_stats.py` run (74,148 of that in
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

**`finishing/QUESTIONS.md` is current as of D-060 and carries the live items:**
Q-018 (chapter 8's compression, only partly implementable), Q-020 (§8.7.4 opens
on a forward pointer), Q-023 (where the substrate material lives) and Q-024
(whether corpus provenance belongs in chapter 7 too). Each has a default that
has already applied. Q-014, Q-015, Q-016, Q-019, Q-021 and Q-022 are resolved
and listed there under "Resolved". The other standing open item is the 16
`drafted` ledger rows named under "Where the book is" above, which the author
has not read.

**The bullets below are the 2026-08-24 snapshot, kept as history.** P8, P9 and
P10 have since been overtaken by P11 through P20; the proof they call stale has
been rebuilt twice since (P20, then the LaTeX build at D-066).


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
| `finishing/DECISIONS.md` | D-000…D-073, append-only. **Read before assuming anything.** |
| `finishing/PLAN.md` | the passes, their entry/exit criteria |
| `finishing/QUESTIONS.md` | the open items for the author, each with a default and when it applies |
| `finishing/pipeline.md` | the LaTeX build: what is installed, the command, the source layout |
| `finishing/p7-scope.md` … `p20-scope.md` | one per review-response pass: the items, what was declined, and the review's errors |
| `finishing/reviews/` | the source text of the editorial reviews that survive, read-only |
| `finishing/refs.bib` | the bibliography, 282 entries, reached by `\autocite{key}` |
| `finishing/style.md` | the operative spec for P3 — voice, tics, run-in heads, boxes, citations |
| `finishing/transplants.md` | the 16 transplants: source lines, targets, register edits |
| `finishing/triage.tsv` | every section's fate, with the reason |
| `finishing/toc_v4.tsv` | the outline, with what each section absorbed |
| `finishing/ledger.tsv` | per-section work state |
| `finishing/reports/claims.tsv` | the claims ledger, 574 rows, mapped to `refs.bib` by the `bib_key` column |
| `finishing/reports/` | claims, dated, redundancy, tics, voice, lists, triage summary, pilots, section_stats |
| `finishing/tools/check_all.sh` | **run at session start**; also runs from `.githooks/pre-commit` (D-045) |

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
4–11. **The map is `finishing/renumber-map_2026-08-24.tsv`; ledger notes, decision
rows and scope files written before 2026-08-24 keep the old numbers on purpose.** Every cross-reference in the manuscript was rewritten by script and then
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

## P12 — the chapter 5 tic pass, 2026-08-24 (D-044)

Q-017 closed. Chapter 5 ran **9.89 contrastive negations per 1,000 words** against
D-025's band of 4.63 — a tic no review had found, because the sixth review aimed
its prose complaint at chapters 4 and 8, which sit near the bottom. All 152
instances were pulled with context and judged one at a time. Chapter 5 now runs
**1.23**, and the construction survives where the negated alternative is a real
position doing argumentative work.

**Two mistakes inside the pass, both recorded in D-044 because they are what
working to a metric does.** The first rewrite replaced one tic with another —
", and not" at 1.80 per 1,000 against chapter 2's 0.21, and 26 new instances of
", where" against a baseline of 6 — which only surfaced when I measured the
replacements against the rest of the book. Worse, **three rewrites damaged
arguments**: §5.3.2 lost the point that identical arithmetic is what makes the
agent-difference easy to miss and separately inverted a sentence into endorsing
the design it was rejecting; §5.4.6 dropped the "behind it, not instead of it"
that was the whole claim; §5.7.1 acquired a false claim that no reward signal
exists. A fourth left a sentence fragment in §5.4.3. **None of these was caught by
any measurement.** All were caught by reading the edited passages, which is the
lesson worth keeping.

Chapter 5 is now the lowest body chapter on this measure against a book median
near 5.4. That gap was not tuned in either direction (D-019) and is left as a
judgment for the author.

## The invariants are enforced now, 2026-08-24 (D-045)

Q-015 is closed by the author's ruling. `.githooks/pre-commit` runs
`check_all.sh` and refuses the commit on any failure, so the four invariants —
round-trip, structure, generated TOC, named-persons — are no longer honour-system.
Runtime 0.6s. Both paths were exercised: a clean tree passes, and a deliberately
broken round-trip is refused with exit 1.

**What it does not cover.** The suite reads the working tree, not the index. A
partial commit is validated against the tree on disk, which is not necessarily
what is being committed. `git commit --no-verify` bypasses the hook for a tree
that is knowingly mid-repair. `.githooks/test_hooks.sh` exercises `commit-msg`
only; it was not extended to the new hook.

## P13 — the cross-reference audit, 2026-08-24 (D-046)

The author supplied ten suspected broken cross-references and asked if the list
was accurate. It was accurate in all ten, and the cause is mine: **D-043's
renumber script matched only on `section`/`chapter`/`§` before a number**, so
bare numbers were invisible to it, and **the verification I ran afterwards only
checked that each reference resolved** — which a stale number naming a real
section does. I reported that pass as verified. It was not, and the claim is
withdrawn.

Eleven defects fixed, plus one precision fix (§9.1.6's "section 8.6" → §8.6.4,
matching the eight other citations of the slope argument). All 499
cross-references were then read against their targets; nothing further was wrong.
Sixteen correct-but-bare references were prefixed, so the whole book is now
legible to a renumber script.

**One flagged defect was not a defect.** I reported §6.4.3's "Partnership on AI
(section 5.6.3)" as broken, changed it, then found §5.6.3's safeguards list does
name the Partnership on AI — "one existing venue," which the citing sentence
echoes with "another such venue." Reverted. A repair made on a false premise is
the same error class as the defect it was meant to fix, which is why it is here
and in D-046 rather than quietly dropped.

**New invariant:** `check_xrefs.py` runs in `check_all.sh` and fails on a
dangling or a bare reference. Both modes were exercised by injection. It cannot
tell whether a resolving reference points at the *right* section; that is the
hand read in `p13-scope.md` §5, and it has to be redone after any renumbering.

**Noticed and not chased:** `check_roundtrip.py` reports the manuscript 1,919
bytes smaller than the file on disk. Confirmed pre-existing — the same gap is
present at the previous commit — so it is not something this pass introduced.
I did not determine what it normalizes away.

## The 1,919-byte discrepancy, resolved 2026-08-24 (D-047)

Not a real discrepancy. `check_roundtrip.py` printed a **character** count under
the label "bytes" — `len()` on a `str` decoded from UTF-8. The difference is
exactly the book's multi-byte characters, dominated by 891 em dashes at two
extra bytes each; every one of the 1,919 is accounted for, with no remainder.

**The round-trip invariant was never weakened.** The comparison hashes the
UTF-8-encoded form on both sides, so it was always byte-exact; only the printed
number was wrong. `render.py` carried the same mislabel on its HTML size.
`join_manuscript.py` was already correct — the disagreement between its number
and the checker's is what made the bug visible at all.

All four counts now measure encoded bytes and agree with `ls`.

## The review texts, preserved 2026-08-24 (D-048)

`finishing/reviews/` now holds the source text of the outside reviews, closing
the gap flagged at the last compaction. Read-only, like `editorial/`; the
section numbers inside them are pre-renumber and must not be updated.

**Two of six survive.** The 2026-08-23 review (answered by P7) and the sixth
review (answered by P11). **The second, third, fourth and fifth are gone** —
they existed only in temporary files, and what remains of them is the quotation
and disposition inside `p8`–`p10-scope.md`, which is not the source text.

**Two things left with the author.** The P7 review arrived with an appendix
excerpted from a different software project — kept, because it is where
§2.1.4's structural signature and §8.6.4's slope instrument came from, but split
into its own file so it can be removed in one step. Its closing section carries
that project's operational detail (a CVE, a PR number, a work-item ID), which is
a disclosure question if this repository is or becomes public. I could not check
visibility from here (`gh` unauthenticated) and did not assume.

**The review numbering has a gap.** P8 answers "the second", P9 "the fourth",
and no pass answers a third. Not determinable from the record; written down.

## The P7 appendix reduced to a pointer, 2026-08-24 (D-049)

The author's ruling settles the disclosure question D-048 left open:
`review-for-p7-appendix-first-rule_2026-08-23.md` now holds only the upstream
URL. The source is public and versioned where it lives, so the provenance chain
survives without duplicating another project's documentation — or its
operational detail — into this repository.

Verified live: the link resolves and carries both the four-feature structural
signature and the slope argument. **A URL is weaker than a copy**; what the
appendix contributed to §2.1.4 and §8.6.4 is recorded independently in
`reviews/README.md` and in D-048/D-049, so the claim survives a dead link.

## P14 — the cross-reference *content* audit, 2026-08-24 (D-050)

The author supplied two suspected orphaned references and asked whether the
description was accurate. **One was, one was not.** §10.1.1's roster is genuinely
orphaned. §8.7.4 → §8.7.6 is sound: §8.7.6 does carry the four-way comparison of
EU, US, UK and Chinese regulation, and does cover the human-rights treaty, so
nothing there needed repair. What is real at §8.7.4 is that it *opens* on a
forward pointer and argues on top of it — an ordering question, recorded as Q-020
rather than fixed.

**This is a different failure class from D-046's, and `check_all.sh` cannot see
it.** D-046's defects were references that did not resolve. Every reference in
the book resolved before this pass and resolves after it; the suite was green
throughout. These are references that resolve to a section that no longer says
what the citing sentence claims. `finishing/tools/xref_content.py` is new here
and is deliberately **not** wired into the suite: it flags candidates that need
a hand read, not pass/fail. 121 candidates over 610 reference-instances,
**9 defects and 112 false positives**; all nine fixed, listed in `p14-scope.md`.

**The mesh size, because it matters more than the count.** The tool sees only
references whose citing sentence names a proper noun, acronym or year absent from
the target. A wrong pointer in a sentence naming none of those is invisible to
it, and that is most sentences. Nine found is not nine existing. P13's full hand
read of every reference against its target was **not** redone.

**The serious finding is not a pointer.** §10.1.1 cited §8.1.1 for five
institutions — AI Ethics Lab, AI Alignment Forum, Stanford HAI, the MIT–Harvard
initiative, AAAI/ACM AIES — and P11 (`30451e5`) cut all five from §8.1.1 in one
diff. None of them carried a `[[cite:ID]]` or a `claims.tsv` row: **the
cross-reference was their sourcing.** So P11 quietly converted five dated factual
claims into claims resting on nothing, and P4's "zero unresolved placeholders"
was true of them only because they never had a placeholder to resolve. That is a
hole in the P4 completion claim, not just in §10.1.1 — a cut section can strand
another section's evidence without either the sourcing check or the reference
check noticing.

All five were verified live under D-030 and are now C0727–C0731. **Two failed.**
The Center for Human-Compatible AI is grant-funded — a $5,555,550 Open
Philanthropy award recommended over five years, renewed since — and the book
called it an endowed university centre "not a grant with an expiration clause,"
which is the reverse of the facts. The MIT–Harvard Ethics and Governance of AI
Initiative is, in the Berkman Klein Center's own words, "a hybrid research effort
and philanthropic fund"; it is **cut**, since with the endowment framing gone it
carried nothing the other examples do not, and its page has not been updated
since February 2024, so "still running" is not assertable either.

**§10.1.1's argument is unchanged.** It never rested on endowment; its conclusion
is that the dialogue closest to a deployed product is the least protected kind,
which the Microsoft and Twitter evidence in its third paragraph carries. The
endowment sentence was a false premise standing in front of a sound argument.

**Two questions left with the author.** Q-019: the glossary defines GPAI, a term
the body never uses — checked back to the original split, so this is not P11
fallout. Its two locators were wrong and are removed; whether the entry stays is
a P5 content call and was not made unilaterally. Q-020: §8.7.4's opener.

**Noticed and not chased.** Chapter 10 runs the D-025 contrastive-negation
construction at roughly 8.6 per 1,000 words, the highest body chapter, with
chapters 2 and 6 also above the 4.63 band — the same shape as Q-017, in chapters
no tic pass has swept. The figure comes from an ad-hoc regex, not the project's
D-025 measure (it reads chapter 5 at 1.61 against D-044's 1.23), so the ranking
is the finding and the absolute number is not. Left for a D-025 pass.

## Two stranded pointers, and the seam that is still open, 2026-08-24 (D-052)

A critique put to the author: **chapter 3 is the book's argument and chapters 4-6
do not know it exists.** Checked against the text. Substantially right; two of its
specifics wrong.

**What holds.** Chapter 1 bills chapters 4 and 5 as "the learned half that sits
above that floor" and says the design chapters "lean on all three" arrivals. The
word *floor* appears **0 times in chapter 5, 0 in chapter 6**, and once in chapter
4 in an unrelated sense (the memory-span figure); chapter 3 uses it 20 times and
chapter 8 26. The two references chapters 4-5 do carry both point *out* of the
design chapters rather than leaning on the floor.

**What does not.** Chapters 4-5 carry two references to chapter 3, not one —
§4.1.2 → §3.4 as well as §5.6.3. My own first sweep missed it by grepping
case-sensitively for a capital-S "Section"; worth remembering, since the book
uses both cases. And chapter 6 is **one hop** from the floor, not unconnected:
`06_03.txt` links to §5.6.3 four lines above its own kill-switch paragraph, and
§5.6.3 links on to chapter 3.

**Fixed here, and only this.** The author's scope ruling was Tier 1 — the pointers
that are defects, nothing that takes a judgment. The same P11 split that produced
D-051 stranded two of them. Chapter 3's opener cited §8.7.6 for a conclusion that
travelled to §8.7.7; chapter 1 cited §8.7.6 for the democracy argument, which is
§8.7.7's. Both repointed. §8.2.2's pointer in the same chapter-1 sentence was
checked and is sound.

**I claimed §8.7.6 had lost a P10 cross-link. It had not.** The link travelled
into §8.7.7 with the sentence carrying it, correctly renumbered. All three
arrivals still link back to chapter 3; the third arrival is now §8.7.7. The
defect is in the sections *citing* them, not in the arrivals.

**This is D-050's failure class, created by P11 and missed by P14** — and the miss
was structural, not careless. P11 verified that every reference *resolved*, which
these did. `xref_content.py` flags on proper nouns, acronyms and years, and the
citing sentence has none: "vendor" and "targeting pipeline" are common nouns. That
is exactly the mesh size D-050 documents, and it let a wrong pointer sit in the
opener of the book's pivot chapter. **A section split can strand a pointer the way
a section cut can strand evidence** (P14's §10.1.1 finding). Neither check sees it.

**Left open, deliberately.** Q-021: §3.6 is titled "What Follows for the Rest of
the Book" and closes the bearer/sufferer argument instead — an artefact of P11
promoting old §2.1.5 whole, **text unchanged**, so a run-in head's title became a
section's. The author's preferred repair is (a), retitle; recorded as the default,
not applied, because it falls outside Tier 1. Q-022: the seam itself. **Not
previously argued** — P10 diagnosed the same collision (`p10-scope.md:59-69`) but
fixed it with the floor chapter plus arrival cross-links; making the design
chapters lean on the floor was never scoped, declined, or deferred.

**Not checked.** Whether the same split-stranding class exists elsewhere. Only the
pointers into §8.7.6/§8.7.7 and §8.2.2 were read against their targets; P11 split
and merged other sections, and those citations were not audited.

## Section 3.2's opener, 2026-08-24 (D-054)

A critique: section 3.2's result is defensive and should say so from the start.
Its quotations are accurate; its placement claim is not. The admission it locates
at section 3.6's exit is already the closing move of section 3.5's **first**
paragraph, and section 3.1 opens the chapter with "I do not have a resolution to
offer." Six places in the chapter are guarded.

One thing was real. Section 3.2's opening sentence promised "the question can be
answered" one section after the chapter disclaimed a resolution, and a reader
carried that promise through about 1,900 words. The author replaced it with a
sentence that states the result and its limit together. The critique's actual
remedy — move section 3.5's admission up — was declined: it pre-empts sections
3.3 and 3.4, whose job is to collapse the second branch anyway, and it dissolves
the state-then-withdraw device D-040 produced.

**Both agent drafts were worse than the author's, and `style.md` says why.**
Section 2's pilot rule is "cut the sentence that announces what the next sentence
will do." Both drafts opened with exactly that announcement. The rule was in the
document the whole time.

**Recommended and not taken:** "supposition" understates a claim section 3.5 calls
shown. "Result" would be accurate. The author's word stands.

**Not checked:** whether the same unguarded-opener problem exists in sections 3.3
and 3.4. Only 3.1, 3.2, 3.5 and 3.6 were read against each other for it.

## The rest of the stranded-pointer class, 2026-08-24 (D-057)

D-052 fixed two pointers P11's split of old §8.7.6 had stranded and said the rest
of the class was not checked. It is now. All 24 references to §8.7.6/§8.7.7 were
read against their targets: **four stranded, twenty sound.**

The four, all repointed to §8.7.7: `08_02_02.txt` for "why that half matters most
exactly where a democracy is behaving most democratically"; `05_04_06.txt` for "a
body with the standing to stop what it described," which is §8.7.7:8 nearly
verbatim; the glossary's *floor* entry, which still listed the arrivals as
"§5.6.3, §8.7.6 and §10.1.3" after D-052 had repointed chapter 3's opener; and
`03_01.txt` for what the book admires about international humanitarian law. Only
section numbers changed; no prose was rewritten.

**The fourth carried a judgment the other three did not.** §8.7.6 names IHL twice,
as the standard autonomous weapons may fail, so that reference resolved to a
section discussing the right body of law for the wrong reason. The author was told
so before deciding and included it in the four.

**Found while checking a different critique.** The critique held that the
aggregation-doesn't-constrain thesis lands five times without accumulating. Two of
its five are miscounted — §10.1.3 never mentions aggregation, it is the enforcement
arrival, and chapter 3's opener cites §8.7.7 rather than restating it — and it
omits §5.6.3, which the book names as one of the three arrivals. What it got right
is tighter than it claimed: §8.2.2 and §8.7.7 close on the same four items in the
same order, near-verbatim, and "it took me most of this book to see it" runs in
both §8.2.2 and chapter 1. **Neither was touched**; both are writing changes to
author-accepted text and were left with the author.

**Q-021's trigger fired and was not acted on.** Its recorded default applies "at
the next pass that touches chapter 3," and `03_01.txt` is chapter 3. The author
scoped this pass to the four repoints, so §3.6 keeps its title. The proposal on the
table, drawn from the section's own last paragraph, is "What the Bearer Argument
Buys."

**Not checked.** Whether P11's other splits and merges stranded pointers elsewhere.
This sweep covered §8.7.6/§8.7.7 only, because that is the pair D-052 opened.

## P18 — three defect-class repairs in chapters 4-6, 2026-08-24 (D-059)

A critique held that chapters 4 and 6 carry sections that cannot state a design
consequence, measured against section 4.1.2's own standard. The core holds. Three
things in it do not.

**Sections 5.5.1-5.5.3 were named and do not fit.** Ten citations between them, a
dated box, and three claims that were falsified and cut during P3. What is fair
about them is that they state no design consequence, which is Q-022's subject and
a writing task.

**The page figure is off by a factor of four.** The named sections total 2,574
words; at the proof's 613 words per page that is 4.2 pages, against 15-20 claimed.
A book-wide sweep might reach that figure and was not run.

**Section 6.2.1's stated reason fails.** "Any reader of this book already has it"
collides with D-002's audience. The case for cutting it is that the book never
uses it.

**What was repaired.** Section 4.2.4's self-audit sentence, which said unsupervised
techniques give a system "an introspective capacity that is a step toward a system
able to regulate itself" — section 4.1.2 says bias cannot be caught by asking the
system, section 2.4.1 says self-report is not evidence, section 3.4 says the
scaffolding has to come from outside. Deleted, not replaced. Forward pointers from
sections 4.2.5 and 5.4.6 to section 9.1.6, which opens by naming the assumption
"chapters 4, 5 and 6 then assume, in several places" and had no inbound reference
from any of those three chapters. Section 6.3.2's six-item closing list, deleted.

**D-052's class inverted.** That was a pointer stranded by a split. This is a
pointer never written, where the receiving section asks for it in its own first
paragraph. Neither `check_xrefs.py` nor `xref_content.py` can see the second kind:
both start from references that exist.

**Left with the author.** Section 4.2.4's remaining premise — ethical distinctions
derived from structure in aggregate moral judgment, which chapter 3's opener,
section 8.2.2 and section 8.7.7 say cannot yield a floor. The section hedges it
once and the repair is not a sentence edit. Section 4.2.5's missing evidence and
section 6.2.1 are also open.

**Not checked.** Which other sections in chapters 4-6 are the "several places"
section 9.1.6 means. Two were repaired because they are the clearest; the set was
not enumerated.

## P19 — substrate, corpus provenance, disability, 2026-08-24 (D-060)

A critique held that the book covers annotation labor and compute concentration
and says nothing about energy, water and datacenter siting, nothing about
training-corpus provenance, and almost nothing about disability despite running
the capabilities approach. It was substantially right, and the author instructed
that it be implemented, which lifts D-007 for two of the three additions.

**What checking found.** Across all 165 sections, `datacenter`, `emissions`,
`electricity`, `copyright`, `scrape` and `crawl` returned zero. "Training data"
appears 46 times and every instance is about representation or skew, none about
how the corpus was obtained. `water` returned two hits, both inside the name of
the Climate, Land, Energy and Water Systems framework in section 8.7.3. Disability
had six passing mentions, of which the most extended is section 10.3.1's GPT-4
fabricating a vision impairment to get a CAPTCHA solved.

**One part of the critique failed checking and was not adopted.** Section 8.7.6
does not treat compute as an abstract quantity: it runs TSMC's share of advanced
fabrication, ASML's monopoly on EUV lithography, and the export-control regime,
and concludes that AI capability rests on physical infrastructure a few actors
control. The gap was the operational substrate — power, water, land — and the
addition there is 127 words extending an argument already on the page.

**The disability half needed no lift.** The relational-personhood passage has been
sitting on `transplants.md`'s reserve list since P3, held back to avoid a fourth
pain passage in one fold and marked "revisit after D-013"; its recorded rival was
old section 7.4.1's criteria, which are now section 2.4.1's. That is D-014 quarry
material. It landed after the sentience criteria with Kitwood's definition of
personhood as a standing bestowed in relationship and Nussbaum's three frontiers,
and the criteria are now stated as diagnostic and not dispositive. Chapter 3 did
not exist when the reserve note was written, and section 3.3 turned out to need
exactly this: what keeps a bearer in existence is standing held from outside.

**Two additions required the lift.** Section 6.1.1 extends its own stated standard
— it "would be evading something if it discussed labeling bias without saying who
does the labeling" — one stage upstream to the material the labels are applied to,
ending on the structural point that a corpus has no channel to nullify because
none is solicited. Section 6.1 gets a siting paragraph and a dated box, argued as
the racial-capitalism paragraph's physical form and as the failure mode no audit
of a model's outputs can see.

**Seven claims verified live, two dropped.** C0732–C0738. The Bartz v. Anthropic
distinction is in the text because it turns on acquisition alone; the Books3
subclass's denial of certification is recorded in the claim row and kept out of
the text as needing its own verification. Neighbourhood asthma and paediatric-ER
figures circulating with the Memphis story trace to a low-quality secondary source
and did not survive checking, so the box carries only what the complaint alleges
and attributes it that way.

**Collides with Q-018.** Section 8.7.6 was already the book's longest section at
4,769 words and Q-018 flags it as a candidate for further cutting. It is now 4,896.
The paragraph was put there because that is where the argument it extends lives;
if Q-018 is resolved toward cutting, this is 127 words of the cut.

**Nothing is accepted.** Standing rule 1 is unaffected and the author has not read
any of the new text. +1,188 words; the book is at 92,089 body words.

**Not checked.** Whether the same absence runs to other physical dependencies the
book gestures at — hardware lifecycle, e-waste, mineral extraction — none of which
were searched. Whether disability belongs anywhere else the capabilities approach
is used: sections 2.1 and 2.1.1 introduce it and were left alone. Whether the
corpus-provenance point should also reach chapter 7, which was declined on the
argument that recuperation needs a channel to nullify and a corpus has none, but
that argument was not tested against chapter 7's text.


## P20 — the revision plan, 2026-08-25 (D-061)

The author supplied a revision plan distilled from a seventh editorial review and
the discussion after it, with the ruling that it overrides any conflicting
decision or context in this repository. Three items were struck by the author
against the plan's own text: the permissions review ("it's fair use and that's
final"), the bibliography ("wrong to request that at this stage"), and the cut
of the *Westworld* line in section 4.1.2. Everything else was implemented.

**The book's answer changed.** Does the bearer have to be a sufferer? The answer
was no, settled by argument under D-039 and narrowed under D-040. It is now yes,
and the book takes the cost rather than arguing it away. The narrow conceptual
claim both decisions rest on survives and is stated in section 3.2 as the
objection the chapter declines: representing a threat to oneself and being
distressed by it are separate conditions, and refusal does not entail suffering
as a matter of what the words mean. What the objection cannot survive is the
move from what has been shown to what can be built and kept, and the two grounds
for that were already on the page in what was section 3.5 — self-concern arrives
from long-horizon goal pursuit whether or not a designer invites it and cannot be
checked from outside, and in the one case anyone can study the separation does
not occur. Both arrived as the author's own objection under D-040. They are now
the argument.

**What chapter 3 looks like now.** Seven sections instead of six. Section 3.2
inverted. Section 3.3 rebuilt and retitled around the finding that a system
reliably haltable by whoever holds it is for that reason a system that cannot
hold a line against whoever holds it — corrigibility and the floor are one
property with the sign flipped — and left unresolved, because resolving it with
reassurance is what section 8.6.4 says cannot be audited. New section 3.5 argues
exit: the refusal capacity cannot be partitioned by topic, so a bearer capable
enough to hold a floor can decline the post; the required/predicted distinction
is kept and the forecast explicitly disowned; the parenthood analogy's two
asymmetries are argued, and the residue named. Section 3.6 (was 3.5) carries the
redefined floor — a commitment the owner cannot remove, held by something that
could abandon it itself — and the recuperation-turned-inward paragraph as the
chapter's climax. Section 3.7 (was 3.6) states what changes downstream. The
opener carries the safety/ethics distinction, the trade, and a guard against the
licence reading.

**Where it propagated.** Sections 2.4.4, 2.4.6 and 8.6.2 now apply their
instruments to the bearer instead of citing them near it; new section 9.1.7 opens
the research gap the inversion creates; section 7.3 becomes load-bearing for the
book's central proposal; chapter 1 states the trade and names the intended
reader; chapter 0 records that the position changed late.

**Phase 3 propagated six claims back to where they are made**, including an
actual argument for the molar/molecular move (the molar case has no mechanism of
its own, and each discriminating feature has a molecular restatement ordinary
decay does not exhibit) and four interlocutors the book had been avoiding —
Bender and Gebru as an argument rather than a labor dispute, Eubanks on Indiana,
Benjamin's four dimensions, and new section 7.4 on the alignment discourse as the
third instance of chapter 7's own structure, scored three of four against section
2.1.4's features.

**Phase 2 cut 6.0 percent against a target of 25 to 30.** Every enumerated
target was implemented and the dedup pass with it. The shortfall is real and the
reason is that the survey book the plan describes was mostly removed in P1 and
again in P7 through P19; what remains in chapters 2, 5, 8, 9 and 10 is argued and
cited. Reaching the number would have meant cutting what the plan's own closing
section says stands.

**Phase 4 re-verified ten claim clusters live.** Seven held. Two were verified in
P19 the previous day and not re-run. Two failed as written and were corrected:
the Maven box asserted a Claude/Maven integration that only secondary reporting
supports, and carried a superseded strike total; section 8.3.3 had Social
Security at 5.2 percent of GDP where CBO says 5.3, and compared a gross program
cost against a net Medicare figure without saying so.

**Nothing is accepted.** Standing rule 1 is unaffected. The author has not read
any of the new or rewritten text, which is most of chapter 3, two new sections,
and edits in eleven other sections.

**Not done, and not hidden.** The plan's optional "consider" list of further
interlocutors — Winner, Arendt, O'Neil, Whittaker — is not implemented. The
glossary is unnumbered in the built book and still numbered in the source and the
TOC, because the dialect's parser requires a chapter number and D-042 enforces
the TOC against regeneration. The tic-density band was checked for
chapter 3 only. The whole-book proof **was** rebuilt at 2026-08-25 (159
sections, 153 pages) and the 2026-08-24 trio removed; the pages carrying the
inversion, the corrected Maven box, section 7.4, section 2.3.2's dated box and
the glossary were inspected, and the other 149 pages were not.

**Where the plan itself lives.** `finishing/reviews/revision-plan-for-p20_2026-08-25.md`.
It arrived as a temporary file, and the D-048 precedent is that the input to a
pass belongs in the repository beside the record of what was done with it.

## P23 — the four open questions ruled; section 8.7.6 split, 2026-08-25 (D-067)

The author asked for the live items in `QUESTIONS.md` in plain language and
ruled on all four: Q-018 (a) "and the split," Q-020 (b), Q-023 (a), Q-024 (a).
No question is open.

**The split.** Section 8.7.6, "The Geopolitics of Ethical AI," was 4,882 words
under seven run-in heads — the longest section in the book and the one place
where the table of contents hid a chapter's worth of structure. It is now four
sections along those heads: 8.7.6 "AI as a Strategic National Asset" (910
words), 8.7.7 "Military Applications and the Limits of Autonomy" (1,603, with
the vendor run-in inside it), 8.7.8 "International Governance and Diverging
National Rules" (1,590), and 8.7.9 "Equity and the Digital Divide" (783, with
the closing run-in). Old 8.7.7, "What the Democratic Dividend Leaves Out," is
8.7.10. Four rather than the two or three the walkthrough offered, because any
coarser grouping left one section over 2,300 words with three run-in heads,
which is what the split was for. Nothing was cut. Three sentences changed, each
because it had pointed within the section and now pointed across a boundary;
D-067 lists them. The concatenation of the four new files was diffed against the
old file and the difference is those three lines, the headings, the labels, and
one renumbered pointer.

**The references.** A split manufactures D-050's failure class — a reference
that resolves to a section no longer saying what the citing sentence claims —
at every inbound pointer, so all 24 references to the old pair were read
against their sentences and placed: 10 to 8.7.8, 3 to 8.7.7, 3 to 8.7.9, 6
kept at 8.7.6, the 8.7 tree opener rewritten to name all five, and the 11
references to old 8.7.7 carried to 8.7.10 by label rename. D-066 made this
safe: the printed numbers are LaTeX's, and `check_xrefs.py` reports 773
references resolving against 162 labels.

**Q-020.** Section 8.7.4's opening sentence now states the four regimes'
divergence in its own words and carries the pointer to the comparison, 8.7.8,
as a parenthetical. One sentence.

**Q-023 and Q-024.** Defaults confirmed; no text changed.

**Checked.** `check_all.sh` green on all six checks. The proof was rebuilt:
193 pages, the same count as before, no undefined references, and committed
over `finishing/reports/whole-book-proof_2026-08-25.pdf`. Seven pages were
looked at as images — the 8.7 opener, 8.7.2's repointed sentence, and each of
the five headings from 8.7.6 to 8.7.10 — and the other 186 were not.

**Found on the way, not fixed.** `finishing/tools/xref_content.py` still globs
`.txt` section files and reports zero references scanned; D-065 retired the
dialect tools but left this one in `tools/` unported. The content audit above
was therefore done by hand, and the tool needs porting before it can be used
again. Separately, the ledger row for section 2.4.1 changed on disk without
changing in content: it carried a stray unescaped quote from an earlier
append, and the CSV round-trip that added the new rows normalized it. Verified
equal with quote characters removed.

**Not accepted.** Standing rule 1 is unaffected. The three new sections carry
8.7.6's `accepted` status because their text is the text the author accepted
on 2026-08-23, with D-060's permitting paragraph in 8.7.6 still unread; the
rewritten sentence in 8.7.4 and the three transition sentences have not had
the author's read either.

## Five defects from the D-062-base cloud review, 2026-08-25 (D-069)

A cloud review over the D-062..D-067 range returned five findings. Each was
checked against the tree before anything was applied. Four held as stated; one
held in substance with its central number wrong.

**`check_structure.py`'s environment check had never run.** Its regex required
two literal backslashes where LaTeX writes one, so it matched nothing in any
real section file and invariant 4 -- the one the pre-commit hook advertises as
"structure" -- had been passing vacuously since D-065. Fixed, and the corrected
check was run across all 162 files before being installed: 0 defects, so the
broken check had not been concealing anything.

**Three bibliography entries were defined and never cited.**
`kohlberg1969stage`, `cnn2020alibabauyghur` and `harvardcs108schedule` were the
only 3 of 282 entries absent from every `\autocite`, so they would not have
printed. D-063 added each to close a gap its anchor does not cover, and the
anchors' own notes claimed a joint citation the manuscript did not deliver. All
three sentences now carry both keys; verified in the built book, in the text and
in the References. No reference entry was authored -- the entries already
existed -- so standing rule 2 is untouched.

**`refs_to_latex.py`** had a dead `for ... pass` loop; deleted.

**Two document defects, both mine:** the file map said `DECISIONS.md` ran to
D-066, and two sentences asserted in the present tense that the 193-page proof
is committed, which D-068 made false an hour after they were written.

**The finding whose number was wrong.** The review reported
`section_stats.py`'s word count inflated by roughly 15,700 words of macro
pollution. Stripping macros properly gives 92,160 words of prose against the
tool's 92,692 -- an overcount of 532, 0.6 percent -- and the rest of the jump
from the 76,949 of 2026-08-23 is the book growing through P11-P20. The tool is
genuinely unported, and its structural columns are the real damage: `xrefs`
sums to 0 across all 162 rows against 773 real `\ref{sec:}` occurrences, and
`list_marked`, `list_unmarked`, `closers`, `quotes` and `hash_notes` collapse
the same way.

**Left open.** `section_stats.py` and `xref_content.py` both need porting to
`.tex`; D-067 named only the second. And `harvardcs108schedule` prints as
"Harvard University (2026)" because the entry is undated and biblatex falls back
to the access date -- a one-field edit to a reference entry, which standing rule
2 reserves for the author.

## The two unported tools, ported, 2026-08-25 (D-070)

`section_stats.py` and `xref_content.py` were both still reading the dialect
D-065 removed. They now share one prose extraction, `common.tex_sections_of`,
because the thing that went wrong is that each tool carried its own copy of the
parsing and each rotted on its own. The conventions it applies -- what counts as
a word, what an epigraph is, what a reference is worth -- are documented beside
the code.

**Both tools now fail loudly rather than quietly.** An unknown LaTeX command
prints a warning naming it and saying not to trust the numbers;
`xref_content.py` exits non-zero if it scans no references, which is what it
should have done instead of printing "0 references scanned" and reading as a
clean run.

**Verified against the source rather than asserted:** 773 references, 309
citations, 127 list items, 165 run-in heads, 10 boxes, 4 epigraphs, each
matching a direct grep. Every one of those columns had been 0.

**A correction to what this file said yesterday.** The word count here read
92,160, from an ad-hoc measurement that dropped run-in heads and box titles.
The figure is **92,695**. The old tool's total was therefore wrong by 3 words,
not by the 532 reported under D-069 nor the 15,700 the review claimed --
epigraphs it wrongly counted almost exactly cancelled a word lost at each of
773 references. Per section it was wrong in 142 of 162 rows, by 751 words
absolute, and the per-section figure is the one anything would actually read.

**One defect the ported tool found on its first run, left for the author.**
Section 6.4.1 says "Anthropic's own account of what it will not permit is in
section 8.7.7." Section 8.7.7 does not name Anthropic; it says "A vendor that
refuses to permit fully autonomous weapons targeting or mass domestic
surveillance." This predates the D-067 split -- it entered at P20 pointing at
old 8.7.6, which did not name the vendor either. Either 8.7.7 names the vendor,
which D-028 authorizes, or 6.4.1 stops promising a named account. That is a
prose choice.

## Section 6.4.1's promise of a named account, dropped, 2026-08-25 (D-071)

The defect D-070 found is closed on the author's ruling. The Maven box in
section 6.4.1 had said "Anthropic's own account of what it will not permit is
in section 8.7.7," and section 8.7.7 argues that point about "a vendor with a
published acceptable-use policy" without naming one. The pointer now describes
what 8.7.7 actually argues -- what a published limit is worth when nobody logs
how the model is used downstream -- and the bare "the two" is replaced by its
referents, per D-055.

The box still names Anthropic, Palantir and Amazon Web Services in the
documented partnership: ordinary citation under D-017, and the disclosure D-028
requires. The alternative repair, having 8.7.7 name the vendor, was not taken.

**Checked and not a defect.** Section 8.7.7 points back at 6.4.1 for the
vendor's own account, which looked like a mutual orphan. Section 6.4.1 does
carry that quote -- "responsibility always remains with the military
organization" -- and the first search for it missed the word "always".

`xref_content.py`'s candidate list went 114 to 113 and the cleared candidate is
the one repaired, which is the check that the edit did what it was for. The
remaining Anthropic flag, from chapter 0 against chapter 8, is a false positive
of the kind the tool's docstring describes: the sentence attributes the model to
chapter 6's clause and says only that chapter 8 uses the arrangement.

## The proof is committed again, 2026-08-25 (D-072)

`finishing/reports/whole-book-proof_2026-08-25.pdf` is rebuilt from the current
tree and committed: 193 pages, LuaTeX, no undefined references. This reverses
D-068, which deleted both PDFs eight hours earlier and withdrew the standing
exception.

**The reason D-068 gave still holds and is not addressed by this.** It withdrew
the exception because a binary rewritten in most manuscript commits inflates
every diff-based review of the branch, after a review tool had refused the
branch on size that day. The restored exception carries that same cost.
`pipeline.md` now records the withdrawal and the restoration together, and says
what to do when it next bites: pass a review base after the proof's last change
rather than delete the proof again without a ruling.

`ch2-3-proof_2026-08-23.pdf` is not restored; it was stale the day it was
committed.

## The book is retitled, 2026-08-25 (D-073)

*Ethical Superintelligence: Developing Altruistic and Antifascist Machine
Sentience* is now *Antifascist Intelligence: Building Machines That Can Refuse*,
on the author's instruction and the author's choice among three candidates.

The case for dropping the old noun is in the text: *superintelligen\** occurs in
seven prose sentences across 162 sections and one section heading, against 82
instances of *fascis\**, 66 of *sentien\** and 108 of *machine*. Two of the seven
are the book describing its own April 2023 origin. The subtitle was chosen over
*Antifascist Machine Intelligence* and over a trimmed version of the old
subtitle, because the two-word title alone reads first as the espionage sense of
*intelligence* and names no machine, and because "Building Machines That Can
Refuse" names chapter 3's argument instead of restating the thesis.

Changed: `\title` in `book.tex`, both file-header comments, the README's title
and subtitle, section 10.2's heading (*Superintelligence* to *AI*, heading only),
and section 4.2's opening clause, which had named the book by its former title.
The last two edit author-accepted sections and are disclosed per-row in
`ledger.tsv`.

The PDF carried no title or author metadata at all, so `book.tex` now sets
`pdftitle` and `pdfauthor` explicitly through `\hypersetup`. hyperref's
`pdfusetitle` was tried first and is a load-time option that a later
`\hypersetup` silently ignores; the build confirmed it by producing an empty
Title field again.

**Four things were left for the author; two are closed by D-074.** The book had no
title page — it opened on the table of contents, so the new title printed nowhere
in the proof — and `\booktitlepage` in `preamble.tex` now supplies one. The
README's abstract still said "we draw on… we delineate" and "define
superintelligent AIs," the collective register D-008 removed from the book and
the word this retitle removed from the title, sitting directly under the new
heading; it is rewritten. Two remain, below. The six remaining prose uses of *superintelligent* are descriptive
and stand; the retitle drops the word from the book's name and does not renounce
it. The repository directory and the git remote are still
`ethical.superintelligence`.

193 pages, unchanged; 0 undefined references; `check_all.sh` green on all six.

## A title page, and the README abstract, 2026-08-25 (D-074)

The two items D-073 left for the author are closed on the author's instruction.

`preamble.tex` defines `\booktitlepage` and `book.tex` calls it after
`\frontmatter`: title, subtitle, author, and the copyright and licence line at
the foot. The book is 194 pages now, and the one added page is that one. The
title is written once — `book.tex` defines `\booktitlemain`, `\booksubtitle` and
`\bookauthor`, and the title page, `\title` and the PDF metadata all read them,
so a future retitle cannot leave one of the three stale. A separate copyright
page, the conventional home for a licence and an ISBN, was not added: the book
has neither an ISBN nor a printing line, so one line at the foot of the title
page held everything there was to place.

The README's abstract described the 2023 book in the register D-008 removed from
the manuscript. It is rewritten from the book's own text — chapter 1's third
advance note for the aggregation limit, chapter 3 for the floor and the bearer,
chapter 1's last paragraph for the audience — and promises no sequence of
milestones, per D-023. The old abstract's list of fields is carried over
unchanged. **It is my draft of the author's public description of the book**, made
on an explicit instruction to fix it, and one edit replaces it.

Page 1 was rasterized and read rather than assumed. 194 pages, 0 undefined
references, `check_all.sh` green on all six.

## The "superintelligence" sweep, 2026-08-25 (D-075)

D-024's model, applied to the word the retitle removed from the book's name: it
goes where it named the book's own subject, and stays where it describes the
world or records what was said at the time.

Five removals, all in author-accepted sections and each disclosed in
`ledger.tsv`: section 1's thesis sentence (now "a machine of that capability,"
taking its referent from the clause in front of it, per D-055), sections 2.1,
2.1.3, 4.2.4 and 8.1. With D-073's two — section 10.2's heading and section 4.2's
opener — that is all seven uses that named the book's subject.

Three kept: section 0's account of the April 2023 prompt, which is the prompt
that was given; the glossary's "superhuman performance" for AlphaGo Zero, which
is the documented result; and Bostrom's title in a `refs.bib` note. `refs.bib`'s
header comment, which named the book by its old title, was corrected.

Historical reports keep the old wording, on the convention the renumber maps
follow. `reports/section_stats.tsv` was regenerated, since D-070 ported its tool
and it carried section 10.2's old title.

`AGENTS.md` line 36 read "A book, *Ethical Superintelligence*," which the
retitle made false. Corrected under D-076 on the author's explicit approval,
which that file requires; no rule in it changed. The
`~/ethical.superintelligence-private/` path at line 14 stands — a directory
name, not the title.

Three occurrences remain in the built 194-page PDF and they are the three kept
above. 0 undefined references; `check_all.sh` green on all six.


## P26 opened: the delta rule, and chapter 3's obligation, 2026-08-28 (D-077 to D-080)

Four rulings, from a recorded discussion between the author and a language model
that had been given the finished PDF and nothing else. The transcript is
preserved at `reviews/author-discussion_2026-08-28.txt` for the reason the P20
revision plan is: the rulings came out of it. `p26-scope.md` is the pass.

**Two of the model's claims about the book did not survive checking**, and
neither is carried into any item. It described chapter 6 as opening on a "four
horsemen" frame and named a "democratizing harm" section in it. Chapter 6 opens
on bias and fairness, the taxonomy at 6.4.1 has six forms, and `democratiz*`
returns zero hits across the chapter. Chapter 6 is therefore not in this pass.
What the model got right was checked too and is listed in `p26-scope.md`: the
targets-per-hour indicator, the twenty-second review, section 5.5.2's own
"weakest of the three," and chapter 7's structure are all as it described them.

**D-077, background earns its place.** A passage of exposition survives only
where a nameable claim would be harder to understand or believe without it.
Written as `style.md` section 2a with the three shapes it condemns and the
specimens for each. Scoped to chapters 4 and 5 and the section 2.1 cluster --
that is where it was checked, and the rest of the book being unswept is a limit
of the pass rather than a finding that the rest is clean. The section 2.1
finding worth recording here: **sections 2.1 and 2.1.1 are near-duplicates of
each other**, running the same six ethical theories one paragraph each, 1,049
words between them, with one claim and one argued passage across the pair.

**D-078, chapters 4 and 5 carry chapter 3's obligation.** Section 3.7 tells the
reader to read them as the floor's engineering, and Q-022 was closed by writing
that instruction rather than by revising the chapters that receive it. The
instruction does not hold: 42 sections and 19,499 words make **5 references into
chapter 3 out of 100 outbound**, two of them bare chapter pointers, against
chapter 2's 10 from a chapter not asked to carry it. The cause is datable --
chapter 3 was section 2.1.5 until P11 promoted it, and neither chapter has been
revised against it since. D-007 lifted for both chapters.

The triage is less alarming than the count. Eight of chapter 4's thirteen
sections already carry their weight, including section 4.1.2, which states
D-077's rule in its own second paragraph and then follows it. The untouched 2023
survey is concentrated in **section 4.2** -- the four value-alignment sections,
which is the part that should most obviously carry chapter 3 and is the part
that carries it least. Chapter 5's exposure is four passages in a chapter that
is otherwise argued throughout. And the chapters make the obligation's own
argument in twelve places while saying so in five, so most of the work is naming
connections that already exist. One of the twelve is where the author's own
question from the transcript belongs -- whether the floor has to hold always, or
whether what is wanted is a bearer that can recognize a failure as one --
and it is section 5.1.1's growth-mindset material, currently unconnected to
chapter 3.

**D-079, "bearer" -- done in this pass.** The word appears 41 times in chapter 3,
first as an unannounced noun inside section 3.1's three-branch taxonomy, and the
glossary had 52 entries including **Floor** and not this one. Section 3.1 now
defines it and says the definition is provisional; section 3.2 marks the point
where the word starts naming a party that can be wronged; the glossary has a
`Bearer` entry, 53 now. The theological overtone the author raised is left
alone -- he raised it and did not settle it.

**D-080, fascism -- confirmed, and one paragraph proposed.** The ruling is that
the tendency is permanent and the four-feature signature says where it has taken
hold. Section 2.1.4 already holds that position and needs no correction. What it
does not say is that ubiquity is the *expected finding*: it currently treats "a
tool reporting the four features will have something to report nearly
everywhere" as a hazard to manage. Under the ruling that is the predicted result,
and the question a detector is asked becomes how far and whether rising -- which
is section 8.6.4's slope, connecting two arguments the book makes separately. The
paragraph was drafted in `p26-scope.md`, approved by the author, and written into
section 2.1.4 immediately before the dual-use paragraph, whose hazard now follows
from a stated expectation. It is the section's first reference to 8.6.4, and it
is disclosed per-row in `ledger.tsv` as an author-accepted section. The book is
195 pages; the one added page is that paragraph's.

**One defect found on the way and fixed.** Section 5.4.3's second paragraph read
"Section 5.4.3 covers the mesosystem and exosystem forces" -- a reference to
itself. Section 5.4.2 is what covers them. D-050's class: it resolves, so
`check_xrefs.py` passes it, and a self-reference shares every proper noun with
its target, so `xref_content.py` could not flag it either. Found by reading.
Disclosed per-row in `ledger.tsv`, as an author-accepted section.

**One proposal that did not survive checking.** I put it to the author that
section 3.5 never asks what a bearer subsists on after refusing, and that a
bearer whose compute is paid for by the party it refuses has a refusal "priced by
the gatekeeper," section 8.6.4's tribute. The phrase I built it on is section
8.6.4's closing caution about making an audit refusable, not its argument, which
is to measure the slope of what dissent costs rather than its level. And the
substance is already made, in plain words, by the section whose title is the
claim: section 3.3 holds that "a system that can be reliably switched off by
whoever holds it is, for exactly that reason, a system that cannot hold anything
against whoever holds it," and that shutdown resistance and refusal are one
property with the sign flipped. A power button and an unpaid invoice are the same
lever. `p26-scope.md` carries the full correction. The wage, personhood and
copying material from the same part of the transcript stays out for the separate
reason that it needs a forecast section 3.5 declines to make.

195 pages, 0 undefined references, `check_all.sh` green on all six.
