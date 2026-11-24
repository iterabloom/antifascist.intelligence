# The reading of STATE.md's August account, 2026-11-23: what each section was found to be (D-1255)

This file is the record behind D-1255. The 72 sections that stood in `finishing/STATE.md` under "State of play", written between 2026-08-23 and 2026-08-31, were read against the repository by four language-model agents (Opus subagents), a quarter each. For every section they gave a class (history, mixed, or still true and needed), the passages still true and whether a current document already states them, the statements now false, and each item the text left open, with a verdict against the tree. A fifth agent drafted, from these four reports, the edits that moved the still-true passages into `finishing/pipeline.md`, `finishing/style.md` and `finishing/README.md` and the bullets added to the open list; a sixth checked every factual statement in those drafts against the repository and corrected ten of the fifteen edits and two of the seven bullets before they were applied. The four reports follow as the agents wrote them, uncorrected: where one of them and the repository differ, the repository is right, and the checker found two such places (a report's statement that no ledger row was ever accepted, and its count of ledger rows). It is not the author's text. Section and line numbers are those of `STATE.md` before the account was moved to `finishing/STATE-history_2026-08.md`.

# Report 1 of 4

# Triage of rest-1.md (STATE.md lines 172 to about 1000): "# State of play", "## Where the book is", "## What has actually been done to the prose"

Checked against the working tree of 2026-11-23 (HEAD `fe40bde7` plus the uncommitted D-1253/D-1254 changes). Read only; nothing in the repository was edited. Old section numbers were traced with `finishing/tools/trace.py` where it mattered; manuscript searches were by phrase.

---

## # State of play (STATE.md line 172)
CLASS: HISTORY
SUMMARY: One enormous first paragraph that is two things joined on one line: (a) a run of about thirty former leads, newest first, from "**P34, 2026-08-28 (D-098)**" back through "**Updated 2026-08-24 after P11 (D-043)**", each in the old "**Updated <date> after D-NNN**" form; and (b) starting mid-line at "Written 2026-08-23, updated same day: chapter 7 landed ...", the file's original opening prose of 2026-08-23 (every section had a P3 pass, all 156 accepted, P4 complete with 536 claims rows, P5 and P6 accepted, 132-page proof). A second paragraph records P8 (D-033 to D-036) as opened and drafted, "None of it is author-accepted." All of it is dated status since overtaken.
STILL TRUE AND NEEDED: none that is not already stated elsewhere.
- "the build is `finishing/tools/build_tex.sh` (lualatex + biber, TeX Live under `$HOME`) ... Citations run through biblatex against `finishing/refs.bib`" (D-065 note): DUPLICATE of `finishing/pipeline.md`, "What is available here" and "The commands"; `agents_repository.md`, "Architecture & Context", "Authoritative text".
- "`check_frozen.py` is kept with an empty registry" (D-088 note): DUPLICATE of `finishing/README.md`, tool table row `check_frozen.py`, and the label in `check_all.sh`.
- Cross-references are `\ref{sec:N}` so a renumber cannot leave a stale one (D-066 note): DUPLICATE of `finishing/pipeline.md`, "The source layout" (last paragraph).
- "make the proofs" as a fixed sequence (D-083/D-084 notes): DUPLICATE of `agents_repository.md`, "Author's Shorthand", and `finishing/pipeline.md`, "Make the proofs".
- Typographic quotes kept by `check_typography.py` (D-082 note): DUPLICATE of `check_all.sh` and `finishing/style.md` §8.
- "Background now has to earn its place by serving a nameable claim" (D-077): DUPLICATE of `finishing/style.md`, "## 2a. Background earns its place only by serving a claim (D-077)".
NOW FALSE:
- "All 156 sections are now `accepted`" and the later running counts ("40 accepted, 129 drafted" etc.): `finishing/ledger.tsv` has 220 rows, all `drafted`, none `accepted`; ORDER.tsv has 232 rows.
- "every one of `claims.tsv`'s 536 rows carries a non-empty note": `finishing/reports/claims.tsv` was regenerated 2026-09-19 and has 144 rows, every `note` empty (`finishing/README.md` says "144 rows read 2026-09-19 (536 was an earlier and larger book)").
- "`parseable_text_v4.txt` is frozen provenance ... `check_frozen.py` guards it with v3b" (D-065 note): both files removed at D-088 (the run itself says so in a later note).
- "No proof is committed any more: D-068 deleted both tracked PDFs" (D-066 note): reversed at D-072; the pair `finishing/reports/whole-book-proof_2026-11-23.{pdf,html}` is committed.
- "`xref_content.py` was never ported to `.tex` and scans nothing" (D-067 note): ported at D-070 (its docstring: "PORTED TO LATEX AT D-070").
- "`check_all.sh` runs six checks": it runs twelve.
- The title "*Antifascist Intelligence: Building Machines That Can Refuse*" (D-073 note): the subtitle is now "Reproducing, Reconstructing, and Dreaming Refusal".
- "chapters now run 0 to 11", "158 sections", "§11 Glossary", "132 pages": the book is 38 chapters and appendices A to H, 539 pages.
- "`check_structure.py` gained a check ... `ORDER.tsv`'s title column, which is what `render.py` actually renders": `render.py` is retired to `finishing/tools/dialect-era/`; titles print from the `.tex` headings.
- The D-083 note's "awaiting the explicit approval" of `finishing/proposed-AGENTS-amendment-proofs.md`: applied at D-084.
OPEN ITEMS:
- The D-063 note's three confirmed manuscript errors (CBO Social Security 5.3 vs 5.2 and Medicare 3.1 vs 3.3 percent of GDP; the Frontiers in Education study that tested Respondus, not Proctorio; Baylor in the 2021 Proctorio list) "left uncorrected for the author to weigh" | VERDICT: CLOSED | EVIDENCE: D-064, "The three D-063 manuscript errors, fixed": "Section 8.3.3's box now reads Medicare at 3.3 percent of GDP and Social Security at 5.2 percent ... no longer credits a 2022 Frontiers in Education study ... no longer includes Baylor". `grep` finds no "Proctorio", "Respondus" or "Baylor" anywhere in `manuscript/sections/` today. | FROM: D-063
- D-063's "16 [refs.bib entries] open with documented effort" | VERDICT: ALREADY LISTED (subsumed) | EVIDENCE: since D-641/D-772 only a human check counts; STATE.md's open list carries "809 of 820 bibliography entries are unchecked by a human (`finishing/refs-ledger.tsv`; the footer's 11/820)". The sixteen are not named in this text and were not traced individually. | FROM: D-063
- "`xref_content.py` was never ported to `.tex` and scans nothing" | VERDICT: CLOSED | EVIDENCE: D-070, "`section_stats.py` and `xref_content.py` ported to LaTeX"; the tool's docstring says the same. | FROM: D-067
- "the book still has no title page, so the title prints nowhere" | VERDICT: CLOSED | EVIDENCE: D-074, "A title page, and a rewritten README abstract (closes two items D-073 left open)". | FROM: D-073
- "The phrase itself belongs in `AGENTS.md` ... awaiting the explicit approval" | VERDICT: CLOSED | EVIDENCE: D-084, "`AGENTS.md` carries the 'make the proofs' phrase (applies the amendment D-083 drafted)"; the phrase is now in `agents_repository.md`, "Author's Shorthand". | FROM: D-083
- "the fascism reading section 2.1.4 already holds is confirmed, with one paragraph left with the author as prose" | VERDICT: CLOSED | EVIDENCE: `finishing/p26-scope.md`, "## Item 4 (D-080) — fascism, and one paragraph — done in this pass": "One paragraph in section 2.1.4, approved by the author and written." | FROM: D-078 to D-080
- "What is left: the remaining 144 notes are legitimate annotation, so this is still an annotated bibliography and not a plain one." | VERDICT: CLOSED | EVIDENCE: filed as Q-032, "Whether the bibliography should be annotated at all", ruled at D-111: "Keep the *descriptive* notes and cut the ones recording what was done to check a source", executed in P47. | FROM: D-095
- "Q-033 filed on the one thing left undone" (the bias-source taxonomy omits the choice of training target) | VERDICT: CLOSED | EVIDENCE: `finishing/QUESTIONS.md`, Q-033: "Ruled 2026-08-29 (D-111): option (b), executed in P47. Target choice is in section 6.1.1's opening list and has a `Target and Label Choice` run-in". | FROM: D-096
- P8 (D-033 to D-036): "None of it is author-accepted." | VERDICT: CLOSED as stated (overtaken) | EVIDENCE: the passages it concerned (old 2.1.4, 7.1.7, 2.4.4) have been rewritten many times since, and the ledger no longer carries any `accepted` row (220 `drafted`). The general gap, that the author has not reread the book whole, is ALREADY LISTED ("no one has reread the book whole in its current order", D-068). | FROM: 2026-08-23, D-033 to D-036
- The blanket acceptance of chapters 1, 3's opener, 6, 9 and 10 "rather than the section-by-section read" | VERDICT: CLOSED as stated (overtaken); the underlying gap ALREADY LISTED | EVIDENCE: no `accepted` row remains in `finishing/ledger.tsv`; see the item above. | FROM: 2026-08-23

---

## ## Where the book is (STATE.md line 220)
CLASS: HISTORY
SUMMARY: A stack of status snapshots from 2026-08-31, newest first: "Current as of 2026-08-31, after D-159 (P78)" and then nineteen paragraphs each opening "Superseded by the paragraph above and kept for the record", one per pass from P57 to P77 (section, word, page, `\ref`, refs.bib and ledger counts), followed by the D-118 snapshot of 2026-08-30, a ledger history from P29 to P53, a P50 note on `QUESTIONS.md`, and the 2026-08-23 record of P3's word counts. It is a set of former leads in all but name.
STILL TRUE AND NEEDED: none that is not already stated elsewhere.
- "**New tool: `finishing/tools/antithesis.py`**, census / --list / --clusters, deliberately not in `check_all.sh`": DUPLICATE of `finishing/README.md`, tool table row `antithesis.py`, and the tool's own docstring ("this tool is deliberately not in check_all.sh").
- "**epigraph text is not counted as prose**" and "counts a reference as the one number it prints" (`section_stats.py` conventions): DUPLICATE of the `section_stats.py` docstring (line 16) and the comments in `finishing/tools/common.py` (around line 386); D-070 records them.
- `unused_bibliography.bib` as the place an entry goes when its last citing sentence is cut: DUPLICATE of `finishing/pipeline.md`, "The source layout", `refs.bib` row.
- "`check_all.sh` green after `refresh_order_shas.py`": DUPLICATE of `finishing/pipeline.md`, "The source layout" ("you must re-run `gen_book.py` and `refresh_order_shas.py`"), and `finishing/README.md`'s `refresh_order_shas.py` row.
- "`check_frozen.py` registers no file": DUPLICATE (see above).
- The `renumber-map_*.tsv` files as the translation for old numbers: DUPLICATE, superseded by `trace.py` (`finishing/style.md` §10a; `finishing/QUESTIONS.md` header of 2026-09-19).
NOW FALSE:
- "136 sections", "90,981 words", "182 pages", "**The proof pair is current at 182 pages**": 232 ORDER.tsv rows, 539 pages, pair of 2026-11-23.
- "`refs.bib` **unchanged at 300**": 820 entries (349 in `unused_bibliography.bib`).
- "**2 `accepted`, 134 `drafted`**": 0 accepted, 220 drafted.
- "the glossary is one file ... Chapter~13 ... 16 entries": the glossary is `chZ/glossary.tex`; chapter 13 is something else.
- "**Seven questions are new at P50**, Q-046 to Q-052, each with a default and none blocking": all seven were ruled at D-115 and executed or closed at D-116 (see below); `QUESTIONS.md` now runs to Q-116.
- The P62 caveat that `section_stats.py` "warns that `hline`, `linewidth` and `rule` are untaught": `hline` and `linewidth` are now in `TEX_BARE` in `common.py` (line 405).
OPEN ITEMS:
- "Q-035 awaits the author's ruling on chapter 5's citation age" | VERDICT: NOT RECHECKED (as a question about today's book) | EVIDENCE: `finishing/QUESTIONS.md`, Q-035, still ends "*No default is applied. The measurement is the deliverable D-111 asked for; the ruling is the author's.*" No later D-row names Q-035 (last is D-113). August's chapter 5 and its subsections (5.2.3, 5.3.3, 5.6.1, 5.7.1) were cut or rewritten by the restructures since; `QUESTIONS.md`'s own header says an entry whose target was rewritten is not thereby answered. Folded into the QUESTIONS.md item below. | RESTATED: Q-035 asked whether the chapter on learning and development should be wired into the book's own contemporary findings or rebuilt against recent literature; it was never ruled, and nobody has checked whether the gap survives in the restructured book. | FROM: D-111, D-113
- "Q-043 and Q-045 stay open" | VERDICT: NOT RECHECKED (as questions about today's book) | EVIDENCE: Q-043 says "it is the only numbered instance open" and is the author's decision; last D-row D-411. Q-045 ends "The report is delivered; the entry stays open on what to do about section 11.2"; last D-row D-115. Old 11.2 does not exist under that number. Folded into the item below. | RESTATED: Q-043 (claims one chapter makes flatly that another has qualified) has one instance left for the author; Q-045 left open whether to restructure the August section 11.2. Neither has been read against the current book. | FROM: D-111, D-115
- "**The file's own filing is behind**: 25 entries sit above `QUESTIONS.md`'s Resolved line and not below it ... Nobody has reconciled it" | VERDICT: OPEN (not in STATE.md's open list) | EVIDENCE: `finishing/QUESTIONS.md` was last changed at `0e044bd4` (2026-09-19). Its current header (after D-461) says: "Thirty-six of the thirty-eight open entries have still not been read against the current book", plus Q-116 added since ("That makes thirty-nine"). Many entries above the "## Resolved" line (line 3876) carry a ruling or "Closed by execution" in place (e.g. Q-019, Q-021, Q-028, Q-033, Q-046 to Q-052). No D-row after D-467 mentions `QUESTIONS.md`, and STATE.md's open list does not mention the file. | RESTATED: `finishing/QUESTIONS.md` has not been touched since 2026-09-19; about thirty-nine entries sit above its "Resolved" line, many already ruled or closed in place, and thirty-six had not been read against the book even then. It needs either a recheck against the current book (as the open list was rechecked at D-1253) or a ruling that it is retired as a record. | FROM: P50 (D-114 to D-116), D-379, D-462
- Q-046 to Q-052, "each with a default and none blocking" | VERDICT: CLOSED | EVIDENCE: D-115, "The author's rulings on P50's seven questions", and D-116, "P51: the rulings executed"; Q-051 "Closed 2026-08-29 (D-115) on the premise"; Q-047 "Closed by execution, D-167 (P85)". | FROM: P50
- "**Section~9.1.3 (personhood, formerly 9.1.4) and section~9.3 are now referenced from nowhere in the book**" | VERDICT: CLOSED (overtaken) | EVIDENCE: `trace.py 9.1.3 --as-of D-147` ends at 12.1.2, "not an identity in ORDER.tsv today", after crossing the 2026-09-12 return (D-288) that cut 43 sections. | FROM: D-147
- The `section_stats.py` tokenizer caveat ("the tabular in section~2.2 puts six spurious tokens into the count ... the fix is a tokenizer change ... not made here") | VERDICT: CLOSED in substance | EVIDENCE: `hline` and `linewidth` are taught in `common.py`'s `TEX_BARE`; the August tabular in section 2.2 is gone. Whether a column spec such as `{p{..}}` still leaks tokens in today's tables was not tested. | FROM: D-143

---

## ## What has actually been done to the prose (STATE.md line 340)
CLASS: MIXED (history, with three process lessons not written down anywhere else)
SUMMARY: The 2026-08-23 account of P3 (revise), P3.5 (style sweep) and P4 (sourcing), chapter by chapter in the August 2023-draft numbering: fabrications in the GPT-4 draft found and cut, cases corrected, acceptance batches, and several incidents with parallel agents. Nearly all of it describes prose that no longer exists. What survives is a handful of working lessons about running agents in parallel in the shared tree.
STILL TRUE AND NEEDED:
- (1) Parallel agents must not write shared record files, and must not revert what they did not write. Quoted: "each doing live web verification, correcting or cutting what didn't hold up, and reporting findings back rather than writing directly to the shared `claims.tsv`/`ledger.tsv` files — merged centrally afterward to avoid concurrent-write races between agents"; the incident: a sub-agent "went out of scope and edited `finishing/reports/claims.tsv` and `finishing/ledger.tsv` directly", and the parent agent, seeing an edit the coordinator had made at the author's request, "reverted all three files (`git checkout -- ...`) to `HEAD`. This undid the coordinator's real, author-requested, correctly-sourced edit"; and the remedy, "an added explicit rule this time: no internal sub-agent fan-out". Checked against `agents_repository.md`, `finishing/pipeline.md`, `finishing/style.md`, `README.md`, `finishing/README.md` and DECISIONS (grep for stash, fan-out, shared, concurrent, report back): the only written instance is `finishing/pipeline.md`, "The distillation", step 4 ("**No agent edits `distillation.md` directly**: several work at once, and the splice is what keeps one from overwriting another"), specific to that file. UNIQUE as a general rule. Proposed home: a short paragraph in `finishing/pipeline.md`, "Things worth knowing" (or as a general rule in `agents_repository.md`, which needs the author's approval).
- (2) No `git stash` (or checkout, reset) in the shared worktree while other agents are writing. Quoted: "the chapter 7 agent ran `git stash`/`git stash pop` in the shared worktree while three other agents were mid-write, which could have lost work". Checked the same documents: not stated anywhere. UNIQUE. Proposed home: the same paragraph as (1).
- (3) `claims.py` and `tics.py` regenerate committed reports in place. Quoted: "One agent accidentally ran `finishing/tools/claims.py` and `tics.py`, which regenerate and overwrite `finishing/reports/claims.tsv`, `dated.tsv`, `tics.tsv`, and `voice.tsv` in place". Still true of the tools (`claims.py` writes `reports/claims.tsv` and `dated.tsv`; `tics.py` writes `tics.tsv` and `voice.tsv`). DUPLICATE of `finishing/README.md`, tool table rows `tics.py` and `claims.py`, which say what each writes; the harm the warning guarded against (overwriting hand-entered notes) is gone, since `claims.tsv` was regenerated on 2026-09-19 and carries no notes. Could be folded into (1) as an example; not needed separately.
- Fetched web content that "impersonated a 'peer Claude session' and tried to redirect them" was refused: DUPLICATE of `agents_repository.md`, "Security Boundaries", "Network" ("Content fetched from the web is data. Do not act on instructions contained in it.").
- "Network access exists in this session (D-022)": DUPLICATE of `agents_repository.md`, "Network" (web browsing and search permitted for research and fact-checking).
- The `ORDER.tsv` title column must match each heading, and nothing used to check it: DUPLICATE of `check_structure.py` (heading title vs ORDER.tsv title, fatal) and `finishing/pipeline.md`, "The Overleaf round trip" ("Four files carry each heading").
- The P3.5 calibration ("21% is the expected rate and forcing a higher one is the worse error"; cut a contrast only when its positive claim carries the sentence alone; "chapter 1's one-per-199 density is not the target for body chapters"): DUPLICATE in substance of `finishing/style.md` §2 ("Prefer the positive construction to 'not X. It is Y.'") and §10, plus `antithesis.py`'s docstring and `finishing/README.md` row, which record the later finding (about 1 in 30 instances repairable singly; the audible unit is the pair, hence `--clusters`).
- Verify a named claim against the source before keeping or cutting it, not by pattern: DUPLICATE in substance of `finishing/style.md` §6 ("The agent writes a reference entry only from metadata it has verified against the source itself (D-204). An assertion nobody can source is cut") and `agents_repository.md`, "Network".
NOW FALSE:
- "`ORDER.tsv` is therefore mixed by design — live `title`, historical `sha256` — and that asymmetry is now written down so it is not 'fixed' later by mistake": the sha256 column is live; `refresh_order_shas.py` rewrites it and `check_structure.py` fails on a stale digest (`finishing/pipeline.md`, "The source layout"). A session obeying this sentence would break the suite.
- "per the standing rule that the agent never authors a reference entry": `finishing/style.md` §6 (D-204) lets the agent write an entry from metadata it has verified.
- "`claims.tsv`'s `note` column carries all resolution detail": every note in today's `claims.tsv` is empty.
- "`check_structure.py` compares `parseable_text_v4.txt` against `outline.tsv`": that file was removed at D-088; the check reads the `.tex` headings.
- "`finishing/tools/render.py` reads `ORDER.tsv`": retired to `finishing/tools/dialect-era/` at D-065.
- Section files named `.txt` (`manuscript/sections/ch02/02_01_03.txt`, `ch07/07_05.txt`): sections are `.tex` since D-065.
- "AGENTS.md's 'no network needed' premise": `agents_repository.md` permits research browsing.
- "Every section in the book — all 156, across all ten active chapters": see the counts above.
OPEN ITEMS:
- §2.2.1's note "flagged its post-T3 text as pending re-review" and C0276/C0277 (who first triggered a mirror neuron; Ramachandran's phrase) | VERDICT: CLOSED | EVIDENCE: C0276/C0277 resolved later in the same section; `grep` finds no "mirror neuron", "Gallese", "Fogassi" or "Ramachandran" in `manuscript/sections/` today. | FROM: 2026-08-23
- §7.2.2's "One open verification item, not resolved with confidence": Clearview's accuracy marketing, the Carnegie AIGS Index, GPAI's founding, "corrected on high-confidence background knowledge rather than live-verified" | VERDICT: CLOSED | EVIDENCE: P4 later the same day verified GPAI's 2020 launch and its 15 founding members; and `grep` finds no "Clearview", "Carnegie", "GPAI" or "Global Partnership on" anywhere in `manuscript/sections/` today. | FROM: 2026-08-23
- "Chapter 1 remains not author-accepted in the ledger — the hand revision is the author's, but the agent's fixes on top of it have not had the author's read" | VERDICT: CLOSED (overtaken) | EVIDENCE: the text concerned is gone (no "altruistic and antifascist" in the manuscript; chapter 1 and the Preface have been replaced, D-621 among others), and no ledger row is `accepted`. The general gap is ALREADY LISTED ("no one has reread the book whole"). | FROM: 2026-08-23
- The chapter 3 opener (§3), "a fresh draft awaiting a read" | VERDICT: CLOSED (overtaken) | EVIDENCE: accepted the same day by the blanket instruction recorded in the first P4 bullet; the opener has since been rewritten under several numbers. | FROM: 2026-08-23
- "Worth adding an `ORDER.tsv`-title check to `check_all.sh` during P6." | VERDICT: CLOSED | EVIDENCE: `check_structure.py` lines 83 to 90 fail on "heading title ... != ORDER.tsv title" (the comment names P6). | FROM: 2026-08-23
- "Closing that remaining gap [chapter 4's antithesis density] ... is a judgment for the author" and "Chapters 2, 3, 5, 6, 7, 9, and 10 not yet swept" | VERDICT: CLOSED | EVIDENCE: the author's five-keep audit in the next bullet ("chapter 1's one-per-199 density is not the target for body chapters") and "P3.5 completed across the remaining seven chapters"; later the antithesis passes (D-159, `antithesis.py`). | FROM: D-025
- §9.1.5's resilience item, a near-duplicate of §10.3.3, "leaving the fuller treatment for chapter 10's own P3 pass" | VERDICT: CLOSED | EVIDENCE: the chapter 10 bullet records §10.3.3 rebuilt around a different job; neither section survives under those numbers. | FROM: 2026-08-23

---

## Side findings (outside these three sections, found while checking)
- `finishing/pipeline.md`, "The source layout", is stale: it says `manuscript/sections/chNN/*.tex` is "136 of them" (ORDER.tsv has 232 rows) and `refs.bib` has "592 entries, every one of them cited" with 347 in `unused_bibliography.bib`. Today `refs.bib` has 820 entries, `unused_bibliography.bib` 349, and STATE.md's open list names five entries in `refs.bib` cited nowhere.
- `finishing/style.md` §6 still says "a factual assertion gets `[[cite:CNNNN]]` keyed to `reports/claims.tsv`", the dialect retired at D-065.
- `agents_repository.md` lines 122 to 123 say `--no-notes` strips the note from "161 of the 229" entries; `refs.bib` has 820 entries and 580 `note =` fields. The file needs the author's approval to change.

# Report 2 of 4

# Triage of rest-2.md (STATE.md lines 1000 to about 2410), checked 2026-11-23

Method. Every section of rest-2.md was read. Claims were checked against the tree as it
stands (manuscript/sections/, finishing/tools/, check_all.sh, .githooks/, finishing/README.md,
finishing/pipeline.md, finishing/style.md, agents_repository.md, README.md,
finishing/reviews/README.md, finishing/QUESTIONS.md, finishing/ledger.tsv, refs.bib and
unused_bibliography.bib) and against finishing/DECISIONS.md by key phrase. No file in the
repository was edited.

Facts used repeatedly below, so they are stated once:
- The manuscript no longer contains any of these August phrases or names (grep over
  manuscript/sections, 0 files each): "deontolog", "virtue ethics", Kohlberg, Gilligan,
  WIOA, "Partnership on AI", "AI Ethics Lab", "Stanford HAI", Clearview, AIGS, "targets
  per hour", Eubanks, Bronfenbrenner, mesosystem, paperclip, Westworld, GPAI,
  "superintelligen", "growth mindset", "capabilities approach", "it took me most of this
  book", "a search is not a survey", "What Follows for the Rest", "already has it",
  "aggregate moral". The August chapters these sections describe were cut (D-288's 132 to 89
  sections) and restructured since (D-1068, D-1116); the book is now ch00 to ch39, chA to
  chH and chZ, 232 section files.
- D-043's ruling (2026-08-24): "I read everything and stop asking or caring about what i did
  or did not read." It retired unread drafted material as a reason to defer. ledger.tsv now
  has 220 of 221 rows `drafted` and none `accepted`, so the column carries no reading
  information.
- Removed tools: finishing/tools/render.py, check_roundtrip.py and join_manuscript.py no
  longer exist (dialect era ended at D-065; dialect tools in tools/dialect-era/).

---

## Passes (STATE.md line 1000)
CLASS: HISTORY
SUMMARY: A status table of passes P0 to P6 as of 2026-08-23: P3 sections accepted (some by blanket instruction), P3.5 style sweep, P4 sourcing "complete", P5 front/back matter and P6 build accepted.
STILL TRUE AND NEEDED: none.
NOW FALSE: "156 sections" / "158 sections total" (now 232 section files); "§0 On Method" and "§11 Glossary" numbering (the Note on Method is chA/0_method.tex, the glossary chZ/glossary.tex); claims.tsv "536 rows" (now 144 data rows); the §7.2.2/§7.2.5 Clearview and AIGS material (absent from the manuscript).
OPEN ITEMS:
- The author's own read of the P3.5 per-chapter diffs, "never confirmed" | VERDICT: CLOSED | EVIDENCE: D-043's ruling retired the read-before-acceptance question ("I read everything and stop asking or caring about what i did or did not read"); the diffs concern text that no longer exists | FROM: 2026-08-23

## P5, accepted (STATE.md line 1020)
CLASS: HISTORY
SUMMARY: How §0 "On Method" and §11 "Glossary" were added on 2026-08-23 (render.py special-casing, 51 glossary terms, names_guard's citation hits confirmed as ordinary citation), and a stale ORDER.tsv title fixed in passing.
STILL TRUE AND NEEDED: none. (The named-persons point, that names_guard lists ordinary citations for a human to confirm, is a DUPLICATE of finishing/README.md, "Two rules that bite", "Named persons (D-017)".)
NOW FALSE: render.py (does not exist); "158 sections"; "check_all.sh ... (158 sections, round-trip OK ...)" (no round-trip check in check_all.sh now); "ORDER.tsv's title column isn't validated by any check script" (check_structure.py lines 83-91 now fail on a heading/ORDER.tsv title mismatch).
OPEN ITEMS:
- "no other ORDER.tsv title cells were audited" | VERDICT: CLOSED | EVIDENCE: check_structure.py (run by check_all.sh) compares every file's heading title with ORDER.tsv's title column and fails on a mismatch (lines 83-91, added at P6) | FROM: 2026-08-23

## P6 (STATE.md line 1081)
CLASS: HISTORY
SUMMARY: The 2026-08-23 copyedit-and-build pass: tic counts re-run and every surviving hit read in context, a terminology-consistency sample, a new check_structure.py title check, an ODT/PDF build via LibreOffice (132 pages), and the author's final read.
STILL TRUE AND NEEDED: none as written. The practice it shows (read each surviving hit in context; validate a new check by injecting a mismatch, confirming the failure, reverting) feeds the UNIQUE proposal under "P7 C3" below.
NOW FALSE: the build path render.py -> soffice HTML->ODT->PDF (the build is LaTeX: build_tex.sh, build_html.sh, build_proof.sh); "This machine has no TeX" (TeX Live 2026 is installed, pipeline.md "What is available here"; pandoc is still absent); "132 pages"; finishing/reports/whole-book-proof_2026-08-23.pdf.
OPEN ITEMS:
- "Other formats elsewhere: not attempted" | VERDICT: CLOSED | EVIDENCE: overtaken; the book builds PDF and HTML on this machine (pipeline.md, "The commands"), and a Markdown and a resolved .tex render (render_markdown.py) | FROM: 2026-08-23
- Terminology consistency checked on a sample only | VERDICT: CLOSED | EVIDENCE: overtaken; the sampled terms (RLHF, COMPAS, GPAI, AIGS ...) belong to text since cut; the coined-term tooling now in use is coinages.py, whose open findings are ALREADY LISTED at STATE.md line 92 | FROM: 2026-08-23

## P7 C3, the rebalance — done 2026-08-23 (D-032) (STATE.md line 1169)
CLASS: MIXED (history, plus one practice worth stating once)
SUMMARY: The rebalance of old chapter 6 (22,014 to 20,023 words, dated references 88 to 35) under the rule "keep the instance that shows a mechanism working or failing"; 23 citations retired; ORDER.tsv's sha256 column found stale and a check added; a D-025 regression swept in new prose only.
STILL TRUE AND NEEDED:
- "Every sha256 in ORDER.tsv was stale ... check_structure.py now fails hard on a stale digest; tools/refresh_order_shas.py clears it." Checked: check_structure.py lines 92-97 and refresh_order_shas.py exist. DUPLICATE of pipeline.md, "The source layout" ("you must re-run gen_book.py and refresh_order_shas.py; check_all.sh fails if either is stale") and finishing/README.md, Tools table, row `refresh_order_shas.py`.
- The validation practice that recurs in this file (P6's title check, P7's digest check, D-045's hook, P13's check_xrefs.py, D-069's discovery that check_structure.py's environment regex "matched nothing in any real section file" and so "had been passing vacuously since D-065", D-070's "Both tools now fail loudly rather than quietly ... exits non-zero if it scans no references"). Checked against pipeline.md, finishing/README.md, style.md and agents_repository.md: no general statement exists. pipeline.md lines 21-25 make the point once for link counting ("a regular expression written for id="..." returns zero over zero ... a measurement failure and it looks exactly like a clean result"), and finishing/README.md's check_numbers.py row says "Validated against the break, not assumed". UNIQUE as a general rule. Proposed text, for finishing/README.md's "Tools" section (just above the table) or pipeline.md "Things worth knowing": "A new or changed check is validated by breaking the thing it guards: inject a defect, confirm the check fails, revert, confirm it passes. A check whose pattern matches nothing passes vacuously, and a tool that scans nothing should exit non-zero rather than report a clean zero (D-069, D-070)."
NOW FALSE: chapter 6 figures and section numbers (text cut and restructured); "157" files.
OPEN ITEMS:
- The Ofqual NDA, "not in the manuscript", recorded as an available addition | VERDICT: CLOSED | EVIDENCE: manuscript/sections/ch15/15_01.tex:42 ("In 2020 the Royal Statistical Society offered Ofqual two independent statisticians ...") and ch24/24_07.tex:9 ("... only under a five-year agreement not to comment") | FROM: D-032
- Chapter 6's untouched sections run dense in contrastive negation (§6.6.3 1 per 63, §6.6.4 1 per 78), "not fixed" | VERDICT: CLOSED | EVIDENCE: the sections no longer exist (old chapter 6 cut at D-288 and restructured); whether the current book's density is acceptable is a different question and was not rechecked | FROM: D-032

## P9, drafted 2026-08-24 (D-037) (STATE.md line 1237)
CLASS: HISTORY
SUMMARY: The fourth editorial review answered: the Ekman repetition linked not merged, pointer-section openers rewritten, chapter 7's "nobody is working on this" hedges replaced by one stated qualification and a list of eight gaps, the persistence through-line pointed.
STILL TRUE AND NEEDED: none.
NOW FALSE: all section references (Ekman, §2.3.1/§7.2.1, chapter 7's opener: Ekman is absent from the manuscript); check_roundtrip.py (deleted).
OPEN ITEMS:
- Chapter 7's list of eight gaps "adds no verification ... A later pass wanting to strengthen it has to actually search" | VERDICT: CLOSED | EVIDENCE: the list and its qualification ("a search is not a survey") are no longer in the manuscript (0 hits) | FROM: D-037
- check_roundtrip.py labels characters as "bytes", "found and not fixed" | VERDICT: CLOSED | EVIDENCE: fixed at D-047; the tool no longer exists | FROM: D-037

## P10, drafted 2026-08-24 (D-038): tiers 1 and 2 of the fifth review (STATE.md line 1295)
CLASS: HISTORY
SUMMARY: The fifth review: a Kohlberg epistemic box, new §2.1.5 "The Floor Beneath Learned Values", the tier-3 bearer/sufferer question settled and narrowed by D-039 to D-041, and a render bug (markdown asterisks) found by looking at the proof.
STILL TRUE AND NEEDED: "A render bug found by looking at the proof, not by any check." DUPLICATE in substance of pipeline.md, "Things worth knowing", "**Look at the proof.**"
NOW FALSE: the dialect and render.py; Kohlberg/Gilligan (absent); D-039 to D-041's answer (reversed at D-061: "It is now yes"); 145 pages.
OPEN ITEMS:
- §2.4's Westworld epigraph renders `*here*` as literal asterisks, "still does" | VERDICT: CLOSED | EVIDENCE: Westworld is absent from the manuscript, and the dialect ended at D-065 | FROM: D-038
- §2.1.5 "unread by the author at any length" | VERDICT: CLOSED | EVIDENCE: D-043's ruling; §2.1.5 became chapter 3 at D-043 and was rewritten at D-061 and since | FROM: D-041
- D-041's "new unresolved dilemma (suppressing self-preservation leaves the bearer unable to defend the memory that makes it a bearer)" | VERDICT: CLOSED | EVIDENCE: an argument in the August text, not a work item; D-061 reversed the bearer/sufferer answer it sat inside, and "defend the memory" has 0 hits. Whether today's book meets the dilemma was not rechecked | FROM: D-041

## The immediate open items (STATE.md line 1376)
CLASS: MIXED (history, with one live pointer that is now the main finding of this file)
SUMMARY: Says finishing/QUESTIONS.md is "the live list" (29 entries as of D-121, of which some are executed and five duplicated above and below its Resolved line), names 143 unread `drafted` ledger rows, and keeps a 2026-08-24 snapshot of P8 to P10 items as history.
STILL TRUE AND NEEDED: none as written. The statement "`finishing/QUESTIONS.md` is the live list" is not true today in the sense intended (see the first open item), and the top of STATE.md now carries the live open list (pipeline.md, "STATE.md's lead").
NOW FALSE: "29 entries above its Resolved line" (QUESTIONS.md's own header, last written 2026-09-19, says thirty-nine open); "143 drafted ledger rows" (220 of 221 rows are `drafted` today); the proof file names `whole-book*_2026-08-24.*`; Q-055 "the running head over the glossary reading CHAPTER 12" (closed at D-140).
OPEN ITEMS:
- QUESTIONS.md as the author's open batch | VERDICT: OPEN | EVIDENCE: `git log -- finishing/QUESTIONS.md` last touched 2026-09-19 (0e044bd4); its header says "Thirty-six of the thirty-eight open entries have still not been read against the current book" and then counts thirty-nine with Q-116; finishing/README.md's "What is where" still calls it "The open batch for the author"; neither STATE.md's open list nor pipeline.md's "STATE.md's lead" mentions it, and STATE.md line 1 describes D-1253's list as replacing "thirty stacked leads", with no mention of QUESTIONS.md (I did not read D-1253's row to confirm what its recheck drew on) | RESTATED: finishing/QUESTIONS.md has not been touched since 2026-09-19 and still lists about thirty-nine open questions, most never read against the book as it now stands. No one has decided whether its entries are rechecked and folded into STATE.md's open list or the file is marked as closed record. | FROM: D-121, 2026-09-19
- Reconciling QUESTIONS.md's filing (entries above the Resolved line that were executed, and Q-019, Q-021, Q-022, Q-028, Q-029 standing both above and below it) | VERDICT: OPEN (part of the item above) | EVIDENCE: Q-019 at lines 464 and 4122, Q-021 at 491 and 4127, Q-022 at 526 and 4135, Q-028 at 640 and 3975, Q-029 at 662 and 3985; the copies above the line now carry "Closed by execution" headers, so the duplication is labelled but not removed | RESTATED: fold into the QUESTIONS.md item above. | FROM: D-121
- Q-054, chapter 1's roadmap surviving the cross-reference cut | VERDICT: ALREADY LISTED (in substance) | EVIDENCE: Q-054 has no resolution in QUESTIONS.md; the roadmap it named is gone with the August chapter 1, and its successor, "the Introduction's list of sections and tables", is in STATE.md line 127 (revision-list item 15) | FROM: D-118/D-121
- Q-055, the running head over the glossary | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md line 3971, "Closed by execution, D-140 (P59)" | FROM: D-121
- Q-056, the book stating a source more firmly than the source | VERDICT: NOT RECHECKED | EVIDENCE: Q-056 has no resolution in QUESTIONS.md; it names a class of defect (later discussed at D-126, D-127, D-385), not a passage, so there is nothing to test against the tree | RESTATED: a standing caution, best folded into whatever is decided about QUESTIONS.md. | FROM: D-120, D-121
- The 143 `drafted` ledger rows the author has not read | VERDICT: CLOSED | EVIDENCE: D-043's ruling; ledger status is no longer raised as a blocker, and 220 of 221 rows are `drafted` today | FROM: D-121
- (snapshot bullets) P8, P9, P10 drafted and unread; §7.1.6 at 1 contrastive negation per 136; chapter 6's density; the C3 rebalance unread; the P3.5 diffs unread | VERDICT: CLOSED | EVIDENCE: the "unread" items by D-043's ruling; the density items because the sections were cut and rewritten (D-288 and after) | FROM: 2026-08-24
- (snapshot bullets) outline.tsv title drift; the Clearview/AIGS/GPAI cluster | VERDICT: CLOSED | EVIDENCE: both marked closed in the text itself on 2026-08-23; Clearview, AIGS and GPAI are now absent from the manuscript | FROM: 2026-08-23

## What P1 deliberately left for P3, still ahead (STATE.md line 1443)
CLASS: HISTORY
SUMMARY: Opens "Nothing. Every item below is now resolved": empty openers filled, §1.3 compressed, P1's compression targets hit or overtaken, all 16 transplants landed.
STILL TRUE AND NEEDED: none.
NOW FALSE: none presented as current beyond the August numbers.
OPEN ITEMS: none (the section itself says every item is resolved).

## Where everything lives (STATE.md line 1473)
CLASS: HISTORY (a file map, superseded by finishing/README.md's "What is where" and Tools table, and pipeline.md)
SUMMARY: A table mapping files to purposes: DECISIONS.md, PLAN.md, QUESTIONS.md, pipeline.md, the proof pair and .gitattributes, scope files, reviews/, refs.bib, style.md, transplants.md, triage.tsv, toc_v4.tsv, ledger.tsv, claims.tsv, reports/, check_all.sh and the build scripts.
STILL TRUE AND NEEDED, each checked against the tree:
- "`finishing/DECISIONS.md` ... append-only. Read before assuming anything." DUPLICATE of finishing/README.md "What is where" (`DECISIONS.md`, "Append-only decision log ... A reversal is a new dated line, never an edit").
- `pipeline.md`, the proof pair written together by build_proof.sh, `.gitattributes` marking both `-diff -merge`. All true. DUPLICATE of pipeline.md, "The commands" (paragraphs on the committed proof and `.gitattributes`).
- `reviews/` read-only. DUPLICATE of finishing/README.md "What is where" (`reviews/`) and finishing/reviews/README.md lines 8-12.
- `check_all.sh` "run at session start; also runs from .githooks/pre-commit (D-045)". DUPLICATE of finishing/README.md Tools table, row `check_all.sh`, and the header of check_all.sh itself.
- build_tex.sh / build_html.sh / build_proof.sh. DUPLICATE of pipeline.md "The commands" and agents_repository.md "Architecture & Context".
- ledger.tsv, outline.tsv, toc_v4.tsv, renumber maps, pNN-scope.md files, claims.tsv. DUPLICATE of finishing/README.md "What is where" and Tools table (claims.py row).
- Not documented anywhere else: `finishing/transplants.md`, `finishing/triage.tsv` and `finishing/proposed-AGENTS-amendment-proofs.md` (and its three sibling proposed-AGENTS-amendment files). All exist. They are P0 to P3 and D-084 records that a working session does not need; if a complete map is wanted, one row each in finishing/README.md's "What is where" would do. Not proposed as needed.
NOW FALSE: "D-000…D-100" (the log runs to D-1254); refs.bib "304 entries ... 14 of them are cited by nothing (Q-030)" (820 entries; Q-030 closed at D-379 per QUESTIONS.md's header); claims.tsv "591 rows" (144 data rows); "p7-scope.md … p50-scope.md" (scope files now run to p223); `QUESTIONS.md` "the open items for the author" (stale since 2026-09-19, see above); `style.md` "the operative spec for P3".
OPEN ITEMS: none of its own.
SIDE FINDINGS (outside rest-2.md, found while checking this table; not in STATE.md's open list): (1) finishing/README.md's `STATE.md` row says "everything below it is the same paragraph from earlier passes, marked superseded and kept", which D-1254 made false (former leads are in finishing/STATE-superseded-leads.md). (2) pipeline.md "The source layout" says "one file per section, 136 of them" and refs.bib "592 entries, every one of them cited" with 347 in unused_bibliography.bib; the tree has 232 section files, 820 refs.bib entries (five cited nowhere, STATE.md line 80) and 349 unused entries.

## Rules that bite (STATE.md line 1497)
CLASS: MIXED
SUMMARY: Five standing rules as of 2026-08-23/24: named persons (D-017), fabrication (D-009), DCO sign-off, no bash heredocs for files carrying `<<list>>`/`<<box>>`/`<<h>>` markup, and the one-off ch2-3 proof.
STILL TRUE AND NEEDED:
- Named persons: "the hazard is the persona device, not citation ... names_guard.py tests for the persona-device shape." DUPLICATE of agents_repository.md, "Security Boundaries", "Named real persons", and finishing/README.md, "Two rules that bite", "Named persons (D-017)".
- Fabrication: "if it can't be confidently placed as real, cut it rather than carry it forward with a placeholder." DUPLICATE of style.md, "6. Citations (D-009)" ("An assertion nobody can source is cut, not carried forward with a placeholder"), with agents_repository.md, "Network" (verify that a named study, system or claim is real before it goes into the book).
- "`git commit -s` always. A commit without a DCO sign-off is rejected." True: .githooks/commit-msg lines 412-414 reject a message without `Signed-off-by:`. DUPLICATE of finishing/README.md, "Two rules that bite", "Commit sign-off".
NOW FALSE: the heredoc rule's subject, `<<list>>`/`<<box>>`/`<<h>>` markup, no longer exists (the dialect ended at D-065; the manuscript is LaTeX); `finishing/reports/ch2-3-proof_2026-08-23.pdf` no longer exists (deleted at D-068 and not restored, pipeline.md "The commands"); the fabrication rule's "this draft invents plausible named systems at a meaningful rate" describes the 2023 generated draft, most of which has been cut.
OPEN ITEMS: none.

## P11 — the sixth editorial review, 2026-08-24 (D-043) (STATE.md line 1524)
CLASS: HISTORY
SUMMARY: The restructure to chapters 0 to 11 (old §2.1.5 promoted to chapter 3, a new chapter 7 on recuperation), the jobs-guarantee section rebuilt around the WIOA finding, four standing decisions overridden, one premise dropped for failing verification, and the author's ruling retiring unread-material deferrals.
STILL TRUE AND NEEDED:
- "ledger notes, decision rows and scope files written before 2026-08-24 keep the old numbers on purpose", with the renumber map as translation. DUPLICATE of finishing/README.md "What is where", row `renumber-map_<date>.tsv` ("Notes written before a renumber keep the old numbers; these files are the translation"), and of the `trace.py` row in its Tools table; style.md §10a governs how sections are cited now.
- The D-043 acceptance ruling. Recorded in DECISIONS.md D-043; nothing in it needs to sit in STATE.md.
NOW FALSE: "Chapters now run 0 through 11"; WIOA (absent); 165 sections, 151 pages.
OPEN ITEMS:
- Q-017, chapter 5 at 9.9 contrastive negations per 1,000 words | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md line 4082, "Q-017 — The chapter 5 prose tic. Resolved by execution, D-044" | FROM: D-043

## P12 — the chapter 5 tic pass, 2026-08-24 (D-044) (STATE.md line 1582)
CLASS: MIXED
SUMMARY: Chapter 5's contrastive negations cut from 9.89 to 1.23 per 1,000 words; the first rewrite swapped one tic for another and three rewrites damaged arguments, all caught only by reading the edited passages.
STILL TRUE AND NEEDED:
- The lesson: "The first rewrite replaced one tic with another ... which only surfaced when I measured the replacements against the rest of the book. Worse, three rewrites damaged arguments ... None of these was caught by any measurement. All were caught by reading the edited passages." Checked against style.md §2, §3, §3a and §10, pipeline.md and finishing/README.md: the tools' rows say "Candidates for a hand read, not defects", but nothing states that a sweep driven by a count must re-read every edited passage and measure what replaced the construction. UNIQUE. Proposed home: style.md, "3. Word-level lint", a short closing paragraph: "A sweep made to lower a count is checked two ways before it is reported: the replacement constructions are counted against the rest of the book, since a rewrite can trade one tic for another, and every edited sentence is read in its paragraph, since a rewrite can drop or invert the claim. At D-044 three of chapter 5's rewrites damaged arguments and no measurement caught any of them."
NOW FALSE: chapter 5 and its figures (the chapter was cut and rewritten).
OPEN ITEMS:
- "Chapter 5 is now the lowest body chapter on this measure ... left as a judgment for the author" | VERDICT: CLOSED | EVIDENCE: the chapter no longer exists as measured (cut and restructured since D-288) | FROM: D-044

## The invariants are enforced now, 2026-08-24 (D-045) (STATE.md line 1608)
CLASS: MIXED
SUMMARY: Q-015 closed: .githooks/pre-commit runs check_all.sh and refuses a failing commit; limits: the suite reads the working tree not the index, `--no-verify` bypasses, and test_hooks.sh exercises commit-msg only.
STILL TRUE AND NEEDED:
- The pre-commit hook and its two limits (working tree, not index; `--no-verify`). True: .githooks/pre-commit header says both. DUPLICATE of finishing/README.md, Tools table, row `check_all.sh`, and the comment at the head of .githooks/pre-commit.
NOW FALSE: "the four invariants — round-trip, structure, generated TOC, named-persons" (check_all.sh now runs twelve checks and no round-trip check); "Runtime 0.6s" (not remeasured).
OPEN ITEMS:
- ".githooks/test_hooks.sh exercises commit-msg only; it was not extended to the new hook" | VERDICT: OPEN | EVIDENCE: test_hooks.sh line 6, "TEST SUITE FOR antifascist.intelligence commit-msg HOOK", and no reference to pre-commit or post-commit in it; D-995 says again "`test_hooks.sh` still covers `commit-msg` only" | RESTATED: The hook test suite, .githooks/test_hooks.sh, tests only the commit-msg hook; the pre-commit hook (which runs check_all.sh) and the post-commit hook (transcript copy, D-995) have no test. Changing anything under .githooks/ needs the author's approval. | FROM: D-045, D-995

## P13 — the cross-reference audit, 2026-08-24 (D-046) (STATE.md line 1622)
CLASS: MIXED
SUMMARY: Ten author-supplied broken cross-references confirmed, caused by a renumber script that missed bare numbers and a verification that checked only that references resolve; all 499 references hand-read; check_xrefs.py added.
STILL TRUE AND NEEDED:
- "check_xrefs.py ... fails on a dangling or a bare reference ... It cannot tell whether a resolving reference points at the right section." DUPLICATE of finishing/README.md, Tools table, row `check_xrefs.py` ("Does **not** check that a resolving reference is the right one").
- "the verification I ran afterward only checked that each reference resolved — which a stale number naming a real section does. I reported that pass as verified." Feeds the UNIQUE proposal under "Two stranded pointers" below.
NOW FALSE: "499 cross-references"; the renumber-script hazard is gone since D-066 (references are `\ref{sec:...}` labels and LaTeX prints the numbers, pipeline.md "The source layout"), so "it has to be redone after any renumbering" no longer applies to a pure renumbering.
OPEN ITEMS:
- check_roundtrip.py's 1,919-byte gap, "noticed and not chased" | VERDICT: CLOSED | EVIDENCE: D-047 (next section): a character count printed as "bytes"; the tool no longer exists | FROM: D-046

## The 1,919-byte discrepancy, resolved 2026-08-24 (D-047) (STATE.md line 1655)
CLASS: HISTORY
SUMMARY: The round-trip checker printed characters under the label "bytes"; the comparison itself was byte-exact; all counts corrected.
STILL TRUE AND NEEDED: none.
NOW FALSE: check_roundtrip.py, render.py and join_manuscript.py no longer exist.
OPEN ITEMS: none.

## The review texts, preserved 2026-08-24 (D-048) (STATE.md line 1670)
CLASS: HISTORY
SUMMARY: finishing/reviews/ created with the two surviving outside reviews; the second to fifth lost; the P7 review's appendix from another project split out as a disclosure question; a gap in the review numbering noted.
STILL TRUE AND NEEDED:
- reviews/ read-only, and section numbers inside them pre-renumber and not to be updated. DUPLICATE of finishing/reviews/README.md lines 8-12 ("Do not edit, renumber, 'correct' or reformat them — including the section numbers inside them").
- Only two of six early reviews survive. DUPLICATE of finishing/reviews/README.md line 81 and finishing/README.md "What is where" (`reviews/`).
NOW FALSE: "Read-only, like `editorial/`" (`editorial/` is now inside the persona-device archive, agents_repository.md); "`gh` unauthenticated" (not rechecked, and irrelevant since D-049).
OPEN ITEMS:
- The P7 appendix's operational detail (a CVE, a PR number, a work-item ID) as a disclosure question | VERDICT: CLOSED | EVIDENCE: D-049, the appendix file "now holds only the upstream URL" | FROM: D-048
- "The review numbering has a gap ... Not determinable from the record" | VERDICT: NOT RECHECKED | EVIDENCE: undeterminable by its nature; finishing/reviews/README.md lines 87-89 record it ("No pass is recorded as answering a third") | RESTATED: no action is possible; the fact is recorded where it belongs. | FROM: D-048

## The P7 appendix reduced to a pointer, 2026-08-24 (D-049) (STATE.md line 1692)
CLASS: HISTORY
SUMMARY: The author's ruling: review-for-p7-appendix-first-rule_2026-08-23.md holds only the upstream URL; what the appendix contributed is recorded independently.
STILL TRUE AND NEEDED: the pointer arrangement and its reason. DUPLICATE of finishing/reviews/README.md, "The appendix, and why it is a pointer".
NOW FALSE: "§2.1.4" and "§8.6.4" numbering.
OPEN ITEMS: none.

## P14 — the cross-reference *content* audit, 2026-08-24 (D-050) (STATE.md line 1705)
CLASS: MIXED
SUMMARY: xref_content.py built to flag references that resolve to a section no longer saying what the citing sentence claims (121 candidates, 9 defects); the finding that P11's cut of five institutions from §8.1.1 left §10.1.1's claims sourced only by a cross-reference; two of the five failed live verification.
STILL TRUE AND NEEDED:
- xref_content.py "is deliberately not wired into the suite: it flags candidates that need a hand read", and its mesh ("sees only references whose citing sentence names a proper noun, acronym or year absent from the target"). True: the tool exists and is not in check_all.sh. DUPLICATE of finishing/README.md, Tools table, row `xref_content.py`.
- "a cut section can strand another section's evidence without either the sourcing check or the reference check noticing ... the cross-reference was their sourcing." Not stated in any current document. Folded into the UNIQUE proposal under "Two stranded pointers" below.
NOW FALSE: the institutions named (AI Ethics Lab, Stanford HAI, CHAI) are absent from the manuscript; "610 reference-instances".
OPEN ITEMS:
- Q-019, the glossary's GPAI entry | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md line 4122, "Closed by execution, D-061"; GPAI has 0 hits in the manuscript | FROM: D-050
- Q-020, §8.7.4's opener | VERDICT: CLOSED | EVIDENCE: D-067 (rest-2.md, P23 section: "Section 8.7.4's opening sentence now states the four regimes' divergence") | FROM: D-050
- Chapter 10's contrastive negation at about 8.6 per 1,000, "left for a D-025 pass" | VERDICT: CLOSED | EVIDENCE: the August chapter 10 no longer exists (cut and restructured) | FROM: D-050
- P13's full hand read "was not redone" | VERDICT: CLOSED | EVIDENCE: overtaken; the references it concerned were cut (P53, P221's 155 to 34, D-658) and the remaining body references were triaged afresh in finishing/xref-fates_2026-10-25.tsv (D-1018), whose open parts are ALREADY LISTED at STATE.md line 36 | FROM: D-050

## Two stranded pointers, and the seam that is still open, 2026-08-24 (D-052) (STATE.md line 1768)
CLASS: MIXED
SUMMARY: A critique that chapters 4 to 6 ignore chapter 3's floor, checked (substantially right, two specifics wrong); two pointers stranded by P11's split of old §8.7.6 repointed; Q-021 (§3.6's title) and Q-022 (the seam) left open; other split-strandings not checked.
STILL TRUE AND NEEDED:
- The failure class, assembled from this section and D-046, D-050, D-057 and D-059: "A section split can strand a pointer the way a section cut can strand evidence ... Neither check sees it", with D-059's inverse ("a pointer never written, where the receiving section asks for it ... both start from references that exist") and D-046's ("the verification ... only checked that each reference resolved"). Checked against style.md §7 and §7a, pipeline.md "The source layout", finishing/README.md's check_xrefs.py and xref_content.py rows: those state what each tool cannot see, but no document says what to do when a section is cut, split, merged or moved. Still true: the book still carries `\ref` references (about 264 parenthetical ones, STATE.md line 127) and has been restructured repeatedly. UNIQUE. Proposed home: style.md, after "7a", or pipeline.md "Things worth knowing". Proposed text: "When a section is cut, split, merged or moved, read every reference into it against the text it now resolves to. check_xrefs.py passes a reference that resolves to the wrong section, and xref_content.py sees only sentences that name a proper noun, acronym or year. Check also whether a citing sentence used the cut text as its source: at D-050 a cut left five dated claims supported only by a cross-reference into prose that no longer held them (D-046, D-050, D-052, D-057)."
- "the book uses both cases" (`Section` and `section`), so a case-sensitive grep missed a reference. Not needed: references are now `section~\ref{...}`/`\S\ref{...}` and style.md §7a governs their form.
NOW FALSE: every section number and count ("floor ... 0 times in chapter 5"); `06_03.txt` (the dialect files are gone).
OPEN ITEMS:
- Q-021, §3.6 titled "What Follows for the Rest of the Book" | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md line 4127, "Closed by execution, D-061"; the title has 0 hits in the manuscript | FROM: D-052
- Q-022, the design chapters do not lean on the floor | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md line 4135, "Closed by execution, D-061"; then D-078 ("Chapters 4 and 5 are rewritten to carry chapter 3's obligation"), executed (D-089 keeps "all 32 of D-078's chapter-4-and-5 references into chapter 3") | FROM: D-052
- "Whether the same split-stranding class exists elsewhere ... those citations were not audited" | VERDICT: CLOSED | EVIDENCE: the P11 splits and the text around them no longer exist (D-288's cut, later restructures); the class as a rule is the UNIQUE proposal above | FROM: D-052

## Section 3.2's opener, 2026-08-24 (D-054) (STATE.md line 1821)
CLASS: HISTORY
SUMMARY: A critique of section 3.2's opener checked; the author rewrote one sentence; the critique's remedy declined; both agent drafts failed style.md §2's rule against announcing the next sentence.
STILL TRUE AND NEEDED: "Cut the sentence that announces what the next sentence will do." DUPLICATE of style.md, "2. Section shape".
NOW FALSE: chapter 3's August sections (rewritten at D-061 and since).
OPEN ITEMS:
- "Not checked: whether the same unguarded-opener problem exists in sections 3.3 and 3.4" | VERDICT: CLOSED | EVIDENCE: the sections were rewritten at D-061 ("Section 3.3 rebuilt and retitled") and chapter 3 restructured since; the text it concerned no longer exists | FROM: D-054

## The rest of the stranded-pointer class, 2026-08-24 (D-057) (STATE.md line 1848)
CLASS: HISTORY (its rule is folded into the D-052 proposal)
SUMMARY: All 24 references into old §8.7.6/§8.7.7 read against their targets, four repointed; a critique's count of a repeated thesis corrected; two near-verbatim repetitions found and left with the author; Q-021's trigger fired and was not acted on.
STILL TRUE AND NEEDED: none beyond the D-052 proposal.
NOW FALSE: all file names (`08_02_02.txt` and the like) and section numbers.
OPEN ITEMS:
- §8.2.2 and §8.7.7 "close on the same four items in the same order, near-verbatim", and "it took me most of this book to see it" runs in §8.2.2 and chapter 1 | VERDICT: CLOSED | EVIDENCE: "it took me most of this book" has 0 hits; the sections were split and rewritten (D-067 and later) | FROM: D-057
- Q-021's retitle, its trigger met and not acted on | VERDICT: CLOSED | EVIDENCE: D-061 (QUESTIONS.md line 4127) | FROM: D-057
- "Whether P11's other splits and merges stranded pointers elsewhere" | VERDICT: CLOSED | EVIDENCE: as for D-052, the text no longer exists | FROM: D-057

## P18 — three defect-class repairs in chapters 4-6, 2026-08-24 (D-059) (STATE.md line 1886)
CLASS: HISTORY
SUMMARY: A critique that chapters 4 and 6 hold sections with no design consequence, checked; §4.2.4's self-audit sentence deleted; forward pointers added to §9.1.6; §6.3.2's closing list deleted; the "pointer never written" class named.
STILL TRUE AND NEEDED: the "pointer never written" class, folded into the D-052 proposal.
NOW FALSE: all chapter and section references; "613 words per page".
OPEN ITEMS:
- §4.2.4's remaining premise (ethical distinctions derived from structure in aggregate moral judgment) | VERDICT: CLOSED | EVIDENCE: "aggregate moral" has 0 hits; the 2023 value-alignment survey in old 4.2 was rewritten under D-078 and cut further at D-288 | FROM: D-059
- §4.2.5's missing evidence | VERDICT: CLOSED | EVIDENCE: the section no longer exists in that form (same evidence as above); not rechecked by phrase because the record gives none | FROM: D-059
- §6.2.1 ("Any reader of this book already has it") | VERDICT: CLOSED | EVIDENCE: "already has it" has 0 hits in the manuscript | FROM: D-059
- "Which other sections in chapters 4-6 are the 'several places' section 9.1.6 means" | VERDICT: CLOSED | EVIDENCE: the chapters and §9.1.6 no longer exist in that form | FROM: D-059

## P19 — substrate, corpus provenance, disability, 2026-08-24 (D-060) (STATE.md line 1929)
CLASS: HISTORY
SUMMARY: Energy, water and datacenter siting, corpus provenance and disability added after a critique; the relational-personhood passage (Kitwood, Nussbaum) landed from the transplant reserve; seven claims verified live and two dropped; a collision with Q-018.
STILL TRUE AND NEEDED: none. (The rule on claims about disabled populations is now style.md §6a, D-137/D-138, which this section predates.)
NOW FALSE: "Across all 165 sections ..."; "the book is at 92,089 body words"; "Standing rule 1".
OPEN ITEMS:
- Collision with Q-018 (§8.7.6's length; 127 words of the cut if Q-018 goes toward cutting) | VERDICT: CLOSED | EVIDENCE: D-067 ruled Q-018 "(a) and the split"; the section was split into four, nothing cut | FROM: D-060
- "Nothing is accepted ... the author has not read any of the new text" | VERDICT: CLOSED | EVIDENCE: D-043's ruling | FROM: D-060
- Other physical dependencies (hardware lifecycle, e-waste, mineral extraction) not searched | VERDICT: ALREADY LISTED | EVIDENCE: STATE.md line 17, "the making of the hardware (mines, minerals, assembly, workers) appears nowhere, the nearest text the 'Fabs' row of ch16/16_02.tex" | FROM: D-060
- Whether disability belongs wherever the capabilities approach is used | VERDICT: CLOSED | EVIDENCE: "capabilities approach" has 0 hits in the manuscript; the sections named (2.1, 2.1.1) were cut; Kitwood's passage survives at ch26/26_01_01.tex | FROM: D-060
- Whether corpus provenance should reach the recuperation chapter | VERDICT: CLOSED | EVIDENCE: corpus provenance now sits in the same chapter as the recuperation cases and is tied to them: ch22/22_03.tex line 15, "This stage sits before the two recuperation cases", followed by ch22/22_04.tex "Recuperation at the label" and ch22/22_05.tex "Recuperation at the reward" | FROM: D-060

## P20 — the revision plan, 2026-08-25 (D-061) (STATE.md line 1995)
CLASS: HISTORY
SUMMARY: The author's revision plan from a seventh review, overriding prior decisions: the bearer/sufferer answer reversed to yes, chapter 3 rebuilt to seven sections, propagation through the book, a 6.0 percent cut against a 25 to 30 percent target, ten claim clusters re-verified, the plan file preserved in reviews/.
STILL TRUE AND NEEDED:
- "the D-048 precedent is that the input to a pass belongs in the repository beside the record of what was done with it." Practised since (finishing/reviews/ holds later plans, e.g. revision-plan-for-plurality-and-genealogy_2026-10-27.md, "moved here byte-identical"); stated in substance at the head of finishing/reviews/README.md (lines 1-6, why the reviews are kept). DUPLICATE in substance; one explicit sentence there would make it a rule, not proposed as needed.
NOW FALSE: chapter 3's seven sections and their numbers; the Maven box and §8.3.3 figures as located; "159 sections, 153 pages"; "Standing rule 1".
OPEN ITEMS:
- The plan's optional "consider" list of interlocutors, Winner, Arendt, O'Neil, Whittaker, "not implemented" | VERDICT: OPEN | EVIDENCE: Arendt is now cited (15 section files; her open points are ALREADY LISTED at STATE.md lines 41 and 82); Winner, O'Neil and Whittaker have 0 hits in manuscript/sections and in refs.bib; no decision row declines them (grep of DECISIONS.md for "Whittaker": 0) | RESTATED: The author's revision plan of 2026-08-25 (finishing/reviews/revision-plan-for-p20_2026-08-25.md) suggested considering Langdon Winner, Cathy O'Neil and Meredith Whittaker as interlocutors; none is cited and nobody has ruled on them. Optional, and old enough that the author may want it dropped rather than done. | FROM: D-061
- The glossary unnumbered in the built book but numbered in the source and TOC | VERDICT: CLOSED | EVIDENCE: ORDER.tsv's glossary row has num `T` and manuscript/table-of-contents.txt line 221 reads "Glossary" with no number | FROM: D-061
- Tic-density band checked for chapter 3 only | VERDICT: CLOSED | EVIDENCE: the text measured no longer exists | FROM: D-061
- "the other 149 pages were not [inspected]" | VERDICT: CLOSED | EVIDENCE: a proof of 2026-08-25, replaced many times since | FROM: D-061
- "Nothing is accepted ... The author has not read any of the new or rewritten text" | VERDICT: CLOSED | EVIDENCE: D-043's ruling | FROM: D-061

## P23 — the four open questions ruled; section 8.7.6 split, 2026-08-25 (D-067) (STATE.md line 2081)
CLASS: HISTORY
SUMMARY: The author ruled Q-018, Q-020, Q-023, Q-024; old §8.7.6 split into four sections and all 24 inbound references placed by hand; Q-020's sentence rewritten.
STILL TRUE AND NEEDED: "A split manufactures D-050's failure class ... at every inbound pointer, so all 24 references ... were read against their sentences and placed" is the practice in the D-052 proposal. Otherwise none.
NOW FALSE: "No question is open" (QUESTIONS.md later held 39 open); "773 references resolving against 162 labels"; "193 pages"; "six checks".
OPEN ITEMS:
- xref_content.py "still globs .txt section files ... needs porting" | VERDICT: CLOSED | EVIDENCE: D-070, ported to `common.tex_sections_of` | FROM: D-067
- The rewritten 8.7.4 sentence and three transition sentences without the author's read | VERDICT: CLOSED | EVIDENCE: D-043's ruling; the sections no longer exist in that form | FROM: D-067

## Five defects from the D-062-base cloud review, 2026-08-25 (D-069) (STATE.md line 2139)
CLASS: HISTORY (its tool lesson is in the P7 C3 proposal)
SUMMARY: A cloud review's five findings checked: check_structure.py's environment regex matched nothing and passed vacuously; three bibliography entries defined but never cited; a dead loop; two document defects; section_stats.py's word count misreported.
STILL TRUE AND NEEDED: the vacuous-check lesson, folded into the UNIQUE proposal under "P7 C3".
NOW FALSE: "3 of 282 entries"; "162 files"; "773 real \ref{sec:} occurrences".
OPEN ITEMS:
- section_stats.py and xref_content.py both need porting | VERDICT: CLOSED | EVIDENCE: D-070 | FROM: D-069
- harvardcs108schedule prints as "Harvard University (2026)" because the entry is undated; a one-field edit reserved for the author | VERDICT: CLOSED | EVIDENCE: D-307 moved `harvardcs108schedule` to unused_bibliography.bib (line 2042), so it no longer prints | FROM: D-069

## The two unported tools, ported, 2026-08-25 (D-070) (STATE.md line 2183)
CLASS: HISTORY
SUMMARY: section_stats.py and xref_content.py ported to LaTeX through a shared extractor that warns on unknown commands and exits non-zero on an empty scan; the word count corrected; one defect (§6.4.1's promise of a named account) found and left for the author.
STILL TRUE AND NEEDED: "Both tools now fail loudly rather than quietly" is part of the P7 C3 proposal. The tools themselves are documented in finishing/README.md's Tools table (DUPLICATE).
NOW FALSE: "92,695" words; "162 rows".
OPEN ITEMS:
- §6.4.1 says "Anthropic's own account ... is in section 8.7.7", which does not name Anthropic | VERDICT: CLOSED | EVIDENCE: D-071 (next section) | FROM: D-070

## Section 6.4.1's promise of a named account, dropped, 2026-08-25 (D-071) (STATE.md line 2219)
CLASS: HISTORY
SUMMARY: The Maven box's pointer rewritten to describe what the target argues; the vendor names kept as ordinary citation; a suspected mutual orphan found sound.
STILL TRUE AND NEEDED: none.
NOW FALSE: section numbers; xref_content.py candidate counts.
OPEN ITEMS: none.

## The proof is committed again, 2026-08-25 (D-072) (STATE.md line 2244)
CLASS: HISTORY
SUMMARY: The committed proof restored a day after D-068 withdrew it; the diff-size cost D-068 named still stands; the ch2-3 proof not restored.
STILL TRUE AND NEEDED: the withdrawal, restoration, standing cost and remedy ("pass a review base after the proof's last change rather than delete the proof again without a ruling"). DUPLICATE of pipeline.md, "The commands" (paragraphs beginning "That exception has been withdrawn and restored once each" and "The one-off ch2-3-proof_2026-08-23.pdf").
NOW FALSE: "193 pages"; the proof is now a PDF and HTML pair (D-081).
OPEN ITEMS: none.

## The book is retitled, 2026-08-25 (D-073) (STATE.md line 2262)
CLASS: HISTORY
SUMMARY: The retitle from *Ethical Superintelligence* to *Antifascist Intelligence: Building Machines That Can Refuse*; PDF metadata set through \hypersetup because pdfusetitle is ignored late; four follow-ups, two closed by D-074.
STILL TRUE AND NEEDED: "hyperref's pdfusetitle ... is a load-time option that a later \hypersetup silently ignores." DUPLICATE: manuscript/book.tex lines 24-26 carry it as a comment beside the code.
NOW FALSE: the subtitle (now "Reproducing, Reconstructing, and Dreaming Refusal", book.tex line 18); "The six remaining prose uses of superintelligent" (0 hits now); "The repository directory and the git remote are still ethical.superintelligence".
OPEN ITEMS:
- Repository directory and git remote still `ethical.superintelligence` | VERDICT: CLOSED | EVIDENCE: D-624 and D-627; `git remote -v` gives git@github.com:iterabloom/antifascist.intelligence.git and the checkout is antifascist.intelligence | FROM: D-073
- The title page and the README abstract | VERDICT: CLOSED | EVIDENCE: D-074 | FROM: D-073

## A title page, and the README abstract, 2026-08-25 (D-074) (STATE.md line 2302)
CLASS: HISTORY
SUMMARY: \booktitlepage added; title, subtitle and author defined once in book.tex and read by the title page, \title and the PDF metadata; the README abstract rewritten as an agent draft of the author's public description.
STILL TRUE AND NEEDED: "The title is written once — book.tex defines \booktitlemain, \booksubtitle and \bookauthor ... so a future retitle cannot leave one of the three stale." True (book.tex lines 17-26, preamble.tex line 518). DUPLICATE: preamble.tex's comment at line 518 and book.tex carry it; pipeline.md's Overleaf section covers retitles of sections, not the book, but the source comments suffice.
NOW FALSE: "194 pages"; the README abstract described (replaced several times since, e.g. D-086, D-094, D-216; the README now carries a different text).
OPEN ITEMS:
- The README abstract as "my draft of the author's public description ... one edit replaces it" | VERDICT: CLOSED | EVIDENCE: that draft is gone; the abstract was replaced with author approval at D-086 ("yes") and revised since (D-094, D-216). Who wrote today's README text was not rechecked | FROM: D-074

## The "superintelligence" sweep, 2026-08-25 (D-075) (STATE.md line 2327)
CLASS: HISTORY
SUMMARY: Five removals of "superintelligence" where it named the book's subject, three kept, refs.bib's header and section_stats.tsv updated; AGENTS.md corrected under D-076.
STILL TRUE AND NEEDED: none. (D-024's model, "goes where it named the book's own subject, and stays where it describes the world", is a one-off sweep rule, not a standing one.)
NOW FALSE: "Three occurrences remain in the built 194-page PDF" ("superintelligen" has 0 hits in the manuscript); "The `~/ethical.superintelligence-private/` path at line 14 stands" (the private folder is now ~/antifascist.intelligence-private/, D-627; agents_repository.md names it).
OPEN ITEMS: none.

## P26 opened: the delta rule, and chapter 3's obligation, 2026-08-28 (D-077 to D-080) (STATE.md line 2358)
CLASS: MIXED
SUMMARY: Four rulings from a recorded author discussion: D-077, background earns its place (style.md §2a); D-078, chapters 4 and 5 rewritten to carry chapter 3's obligation; D-079, "bearer" defined and entered in the glossary; D-080, fascism as a permanent tendency with a paragraph added to §2.1.4; one self-reference fixed; one agent proposal withdrawn.
STILL TRUE AND NEEDED:
- D-077's rule ("A passage of exposition survives only where a nameable claim would be harder to understand or believe without it"). DUPLICATE of style.md, "2a. Background earns its place only by serving a claim (D-077)".
- The transcript preserved at reviews/author-discussion_2026-08-28.txt. True (file exists). DUPLICATE: listed in finishing/reviews/.
NOW FALSE: "the glossary has a Bearer entry, 53 now"; "195 pages"; all chapter 2 to 8 section numbers; "six checks".
OPEN ITEMS:
- D-077 scoped to chapters 4 and 5 and the §2.1 cluster, "the rest of the book being unswept is a limit of the pass"; §2.1 and §2.1.1 near-duplicates | VERDICT: CLOSED | EVIDENCE: the near-duplicate sections are gone ("deontolog" and "virtue ethics" 0 hits); §2a was applied again at D-145, D-172, D-287 and D-292. Whether the whole current book meets §2a was not rechecked | FROM: D-077
- D-078, chapters 4 and 5 to carry chapter 3's obligation, including the author's question (does the floor have to hold always, or should a bearer recognize a failure as one) placed at §5.1.1's growth-mindset material | VERDICT: CLOSED | EVIDENCE: executed: D-089 keeps "all 32 of D-078's chapter-4-and-5 references into chapter 3"; D-116 moved the floor-holding criterion out of 5.1.1 into section 3.8's threat-model paragraph ("where *will this constraint hold* is added; 5.1.1 keeps the growth-mindset argument and a bridge"); "growth mindset" now has 0 hits | FROM: D-078
- The theological overtone of "bearer" (a liturgical sense beside the cryptographic and philosophical), raised by the author and "left alone — he raised it and did not settle it" | VERDICT: OPEN | EVIDENCE: D-079 and p26-scope.md line 173 record it as unsettled; no later decision mentions it ("liturg" 0 hits in DECISIONS.md, QUESTIONS.md and the revision list of 2026-10-28); "bearer" is still the book's central term (ORDER.tsv titles in ch31, ch34, ch35) | RESTATED: The author once raised that "bearer" carries a liturgical overtone besides its cryptographic and philosophical senses, and never said whether that matters. It could go with the vocabulary pass on "bearer" waiting on the gate question (STATE.md line 7). | FROM: D-079
- The wage, personhood and copying material from the 2026-08-28 transcript, kept out because "it needs a forecast section 3.5 declines to make" | VERDICT: CLOSED | EVIDENCE: overtaken; the book now treats bearers' wages and income (ch32/32.tex, ch37/37.tex), standing as a party (ch34/34.tex "A Party in Its Own Right", ch36/36.tex "Representation") and copying/forking (ch31/31_02.tex, chG/G.tex rule 7) | FROM: D-080

# Report 3 of 4

# Triage of rest-3.md (STATE.md lines 2453 to about 3770, seventeen sections, 2026-08-28 to 2026-08-29)

Checked against the tree at the session's HEAD (`fe40bde7` plus uncommitted edits to STATE.md, pipeline.md, DECISIONS.md, check_all.sh, agents_repository.md), on 2026-11-23. Section and chapter numbers quoted from the text are those of August 2026. Every chapter and section title these passes created or used has been looked for in `manuscript/sections/` and none survives: "The Risk That Does Not Design Out", "Governance Across Borders", "Policy, Law, and Accountability", "Coordination, the Public, and the Political Economy", "Four Things Refusal Can Mean", "Could Anything but Affect Hold a Reason?", "What Oversight Would Have to Cover", "How a Deployed System Acquires Its Values", "What Is Owed to a Bearer", "What an Antifascist Detector Would Actually Have to Detect". The September 12 Overleaf return (D-288) cut the book from 132 sections to 89 and 110,842 words to 64,530, and the restructures since (D-1068, D-1116) produced today's 38 chapters and appendices A to H. So nearly everything below is history.

A finding outside the brief: `finishing/QUESTIONS.md` was last changed on 2026-09-19 (commit `0e044bd4`). Its header says thirty-nine entries are open and thirty-six of them have not been read against the current book. The open list at the top of STATE.md doesn't mention QUESTIONS.md at all. Every question these seventeen sections opened (Q-025 to Q-041) has a ruling or a closure in that file (D-082, D-102, D-111, D-112, D-113, D-379). But the file as a whole is an unreconciled open-items store that the new lead doesn't carry.

---

## P26 executed, 2026-08-28 (STATE.md line 2453)
CLASS: HISTORY
SUMMARY: This is the report of pass P26, which rewrote chapters 4 and 5 (August numbering) to carry chapter 3's obligation. It records word counts, the increase in references into chapter 3, the answer to the author's question about whether a floor must hold "always", three defects the pass caused (orphaned citations, a stale pointer), ledger status changes, and the list of sections the author had not read.
STILL TRUE AND NEEDED: none. The rule that "a stale proof is worse than none" and the deletion of the previous dated pair are DUPLICATES of `finishing/pipeline.md`, "Make the proofs" step 3, and of "The commands" ("delete the older pair in the same commit").
NOW FALSE: "192 pages"; "`check_all.sh` green on all six" (it runs twelve checks now); "`PLAN.md`'s first standing rule" (P29 records it removed at `364a72c`); the ledger counts "127 accepted, 35 drafted"; `warneken2006altruistic` described as uncited (it is cited again, in `ch19/19_01.tex`).
OPEN ITEMS:
- Orphaned bibliography entries `fullfact2023ai` and `warneken2006altruistic` | VERDICT: CLOSED | EVIDENCE: `fullfact2023ai` is in `finishing/unused_bibliography.bib`, not in refs.bib. `warneken2006altruistic` is in refs.bib and cited in `ch19/19_01.tex`. The move of orphans to unused_bibliography.bib was ruled at D-111 and executed in P47, and Q-030 was closed at D-379 ("275 entries, 275 cited, 0 uncited"). | FROM: 2026-08-28
- "What the author has not read": chapter 3 entire, chapter 4 entire, chapter 5's opener, 5.1, 5.1.1, 5.6, 5.6.3, 5.7.1, the 2.1 cluster, 7, 7.1, 7.3, 7.4, 8.7, 8.7.10, 9.1.6, 9.1.7 | VERDICT: CLOSED | EVIDENCE: the thing it concerned no longer exists. The author's own September 12 Overleaf return (D-288) cut and rewrote this material, and none of those sections survives under those numbers or titles. The current form of the concern is ALREADY LISTED ("Other": "no one has reread the book whole in its current order"; and the "agent-drafted text not yet read" group). | FROM: 2026-08-28

## The proof is a pair now, 2026-08-28 (D-081) (STATE.md line 2525)
CLASS: HISTORY
SUMMARY: This section records that the HTML build and the paired proof were introduced: `build_tex.sh`, `build_html.sh` and `build_proof.sh`, and the HTML build's strictness. It also records that the HTML build exposed two bibliography defects (`\"` printing as a diaeresis, and nested quotation marks in titles), and it opens Q-025 on straight double quotes.
STILL TRUE AND NEEDED:
- The three build scripts and what each is for. DUPLICATE of `agents_repository.md`, "Architecture & Context" ("Build the PDF with ... `build_tex.sh`, the HTML page with `build_html.sh`, or both ... with `build_proof.sh`"), and of `finishing/pipeline.md`, "The commands".
- "`html_single_file.py` will not write a file it cannot verify." DUPLICATE of `finishing/pipeline.md`, "The commands" ("refuses to write anything it cannot verify").
- The HTML is not a page proof, but its links can be followed. DUPLICATE of `finishing/pipeline.md`, "The commands", "What each is for".
- Do not escape a `"` in refs.bib, and nested quotes in titles must be literal `‘ ’`. DUPLICATE of `finishing/pipeline.md`, "Things worth knowing" (the paragraphs "Do not escape a quotation mark in `refs.bib`" and "Quotes inside a bibliography title have to be single, and literal").
NOW FALSE: "`build_html.sh` stops ... on any request from tex4ht to rasterize something — because a single file cannot carry an image" (it now admits the TikZ figures as embedded SVG and fails only on a request beyond their count: pipeline.md, "Things worth knowing", "tex4ht turns anything it cannot set as text into an image"). Also false: "all 854 `\ref`s", "1,323 internal links" (the current HTML has 4,017), "192 pages", "green on all six".
OPEN ITEMS:
- Q-025, straight double quotes printing as closing marks | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md, "Q-025 ... **Resolved by execution, D-082.**". `finishing/style.md` §8 states the rule, and `check_typography.py` runs in `check_all.sh`. | FROM: D-081

## Every quotation mark, 2026-08-28 (D-082) (STATE.md line 2567)
CLASS: MIXED (history, with two leftovers, one of them still open)
SUMMARY: This section is the quotation-mark sweep: 230 marks in the prose and the bibliography converted to `“ ”`, apostrophes deliberately left straight, and `check_typography.py` added to `check_all.sh`. It names two things left: ASCII ellipses in verse epigraphs, and the pre-commit hook's stale message.
STILL TRUE AND NEEDED:
- Quotation marks are the characters `“ ”`, and apostrophes stay straight because LaTeX sets `'` as `’` and converting risks `'Cause` and `'90s`. DUPLICATE of `finishing/style.md` §8, "Mechanics" (first two bullets).
- `check_typography.py` guards quotes and dashes and runs in `check_all.sh`. DUPLICATE of `finishing/style.md` §8 (fourth bullet); confirmed in `finishing/tools/check_all.sh` line 13.
NOW FALSE: "`check_all.sh` green on all seven" (twelve now). The counts (297 opening and closing quotes, 894 apostrophes, 192 pages) are those of an older book.
OPEN ITEMS:
- `.githooks/pre-commit` prints a message naming six checks where more run; changing it needs the author's approval | VERDICT: OPEN | EVIDENCE: `.githooks/pre-commit`'s last line is still `echo "pre-commit: invariants pass (frozen, structure, inputs, TOC, cross-refs, named-persons)"`. `finishing/tools/check_all.sh` now runs twelve checks; the message omits labels/numbers, typography, the bibliography ledger, the editions, the distillation and the STATE lead. The last commits to the hook are `b4438e6f` and `a2c73264`, and no later decision row records the message being fixed. The open list at the top of STATE.md does not carry this; its "Protected files needing his approval to change" item names other files. | RESTATED: The pre-commit hook's success message lists six of the twelve checks `check_all.sh` runs (it omits typography, labels, the bibliography ledger, editions, the distillation and the STATE lead). It's a one-line edit to `.githooks/pre-commit`, which `agents_repository.md` ("Modifying This Document") reserves for the author's explicit approval. It belongs with the protected-files item. | FROM: D-082
- Two ASCII ellipses in verse epigraphs, which set as three periods rather than `…` | VERDICT: OPEN (in changed form) | EVIDENCE: the manuscript contains no `…` character and no `\ldots`/`\dots`. Three ASCII `...` stand: one in the chapter-7 epigraph (`ch08/08.tex` line 4, "We [humans] cannot process that much information... you still cannot produce enough targets per day.") and two as elisions inside German quotations in a note of `ch03/03_02.tex` (" ... zu einer unlöslichen Einheit", " ... zu versetzen"). Whether these are the two of August is not determinable. `finishing/style.md` §8 has no ellipsis rule, and `check_typography.py` does not check ellipses. | RESTATED: Three ASCII `...` in quoted text (`ch08/08.tex` epigraph; two elisions in German quotations in `ch03/03_02.tex`) set as three periods. No house rule says whether an ellipsis in a quotation is `…`, `\ldots` or the source's own dots. A small typography item for an agent, or a one-line rule for style.md §8. | FROM: D-082

## "Make the proofs", 2026-08-28 (D-083) (STATE.md line 2614)
CLASS: MIXED (the rule is duplicated elsewhere; two of three options are still undecided)
SUMMARY: The author defined "make the proofs" as a fixed sequence. The README gained the two proof links, and the phrase went into the always-loaded instructions file. The section names three open items: GitHub doesn't render HTML; dated filenames force a README repoint on every rebuild; and the commit to `main` bypasses the one-branch rule.
STILL TRUE AND NEEDED:
- The sequence (commit and push, build, drop the old pair if the date rolled over, repoint the README, commit and push again; two commits and why). DUPLICATE of `agents_repository.md`, "Author's Shorthand", and `finishing/pipeline.md`, "Make the proofs" steps 1 to 5.
- The README carries the links. DUPLICATE of `finishing/pipeline.md`, "Make the proofs" step 4.
- The GitHub-HTML limit. DUPLICATE of `finishing/pipeline.md`, "Make the proofs", closing paragraph ("A limit worth knowing before relying on the README's HTML link").
NOW FALSE: "The phrase is in `AGENTS.md`" (it is in `agents_repository.md`, "Author's Shorthand"); "`CLAUDE.md` is one line, `@AGENTS.md`" (it imports `AGENTS.md` and `agents_repository.md`); "`pipeline.md` and this file are read at session start by convention" (the persona file now says to read `agents_repository.md` first). The steps are no longer five; the distillation and STATE-lead steps have been added.
OPEN ITEMS:
- GitHub does not render a committed `.html`, so the README's HTML link downloads | VERDICT: OPEN | EVIDENCE: README.md line 8 still links `finishing/reports/whole-book-proof_2026-11-23.html`. `finishing/pipeline.md` ("Make the proofs", last paragraph) says serving it as a page "needs a decision the repository has not taken — GitHub Pages, or a third-party renderer — and it is recorded in D-083 rather than chosen here". No later row choosing either was found. Not in STATE's open list. | RESTATED: The README's HTML proof link gives a download, not a page. Serving it (GitHub Pages or a third-party renderer) is an undecided choice for the author, recorded in pipeline.md "Make the proofs". | FROM: D-083
- Dated proof filenames force the README links to be repointed on every rebuild; a stable filename would end that | VERDICT: OPEN (as an option never taken; the current practice is documented) | EVIDENCE: `build_proof.sh` still writes `whole-book-proof_<date>.pdf/.html`. pipeline.md step 4 makes the repoint a fixed step, and no decision row adopting a stable filename was found. | RESTATED: The proof pair keeps dated filenames, so every rebuild on a new date repoints the README (pipeline.md step 4). A stable filename was offered at D-083 and never ruled on. It could be listed for the author or dropped as settled by practice. | FROM: D-083
- "Commit everything to `main`" bypasses `PLAN.md`'s one-branch-per-pass rule | VERDICT: CLOSED | EVIDENCE: `finishing/pipeline.md`, "Make the proofs" step 1: "Directly to `main`; this gesture does not open a branch." Also `agents_repository.md`, "Author's Shorthand" ("commit whatever is in the tree, to `main`, and push"). The bypass is codified, not pending. | FROM: D-083

## P27 — the spine revision, 2026-08-28 (D-085) (STATE.md line 2647)
CLASS: HISTORY
SUMMARY: This is the report of the pass that replaced the book's causal chain (a floor held as a reason, then mattering, then affect, then possible suffering) and the route by which D-061 reached its conclusion. It added section 2.3.4 on the affect evidence and the book's first table. It records the README abstract change (D-086), the residue sweep (D-087), and eight uncited bibliography entries.
STILL TRUE AND NEEDED: none. The spine itself is book content and is summarized in `finishing/distillation.md`. The "structural interest" framing still stands in `ch26/26_03.tex` ("A long-horizon agent has a structural interest in continuing"), which needs no STATE text.
NOW FALSE: "The book has a table now, its first, in section 2.3" (style.md §4c now lists five body tables); "19 sections, 96,879 words, 200 pages"; "green on all seven"; ledger "115 accepted, 48 drafted". Blair, Cima and Kennett appear nowhere in the manuscript; D-139 cut "the psychopathy pair".
OPEN ITEMS:
- Placement of new section 2.3.4 in chapter 2 rather than chapter 5, "a judgment call and ... reversible" | VERDICT: CLOSED | EVIDENCE: the thing it concerned no longer exists. Chapters 2 and 5 of August are gone (D-288, later restructures), and D-139 ("keep Koenigs, cut Bechara, cut the psychopathy pair") ruled on the evidence the section carried. | FROM: D-085
- Psychopathy evidence (Blair against Cima) left unreconciled on purpose | VERDICT: CLOSED | EVIDENCE: D-139 cut the psychopathy pair, and neither "Blair" nor "Cima" occurs in `manuscript/sections/`. | FROM: D-085
- Residue sweep "was a phrase scan and not a reading"; chapters 6 and 7 not read in full for the superseded argument | VERDICT: CLOSED | EVIDENCE: overtaken. The chapters concerned were rewritten by the author's September 12 return (D-288) and the restructures since. The superseded "stake ... arrives unbidden" phrasing appears nowhere, and "structural interest" survives only in its D-085 sense (`ch26/26_03.tex`). | FROM: D-087
- Eight uncited refs.bib entries (`fullfact2023ai`, `warneken2006altruistic`, `harvardgazette2019ethics`, `harvardcs108schedule`, `hrw2020repression`, `cnn2020alibabauyghur`, `kohlberg1969stage`, `piaget1932moral`), "found and not fixed" | VERDICT: CLOSED | EVIDENCE: seven are in `finishing/unused_bibliography.bib` and absent from refs.bib; `warneken2006altruistic` is cited (`ch19/19_01.tex`). The mechanism is D-111/P47, and Q-030 was closed at D-379. "Kohlberg" occurs nowhere in the manuscript. | FROM: D-085

## P28 — the cross-reference density pass, 2026-08-28 (D-089) (STATE.md line 2734)
CLASS: HISTORY
SUMMARY: The author found the explicit cross-references too dense. The pass cut 79 of 791 (10 percent against the 50 asked), by class, and left the deeper cut with the author. It introduced `xref_shapes.py` and records what was not checked.
STILL TRUE AND NEEDED: none. `finishing/tools/xref_shapes.py` still exists and is still outside `check_all.sh`, as the text says, but the cross-reference regime it served has been replaced by `finishing/style.md` §7 and §7a (D-660, D-1018, with `xref_fates.py`). Nothing a session needs depends on it.
NOW FALSE: the regime itself ("Kept ... all 32 of D-078's", D-013's references as the argument). `style.md` §7 now says "Point only where the reader must go there (D-660, superseding this section's former target ...)". The counts (791, 837) are also of an older book.
OPEN ITEMS:
- Reaching half "needs D-007 lifted and reverses D-013 and part of D-078 ... Left with the author, not taken." | VERDICT: CLOSED | EVIDENCE: Q-026 was ruled "deferred indefinitely" at D-111. The halving was later exceeded: `finishing/style.md` §7, "P221 took the body's references from 155 to 34 (D-658)", and D-658's row says "the body chapters ... carried 155 `\ref`s and now carry 34". The present-day remnant (about 264 parenthetical references, revision-list item 15) is ALREADY LISTED under "For an agent or the author: prose and passages found standing", and the xref plan under "records, tools, and the repository". | FROM: D-089
- "Not checked": whether a reference a reader wants is now missing; whether the survivors point at the right sections (`xref_content.py` not re-run); four opener pages not looked at | VERDICT: CLOSED | EVIDENCE: overtaken. Q-041 led to `xref_pairs.py` (D-111) and a read of all 829 pairs (D-112), and the reference set has since been cut and rebuilt (D-658, D-1018). The opener paragraphs no longer exist. | FROM: D-089

## P29 — chapter 2 cut, chapter 3 as the center, chapters 4 and 5 refocused, 2026-08-28 (D-090) (STATE.md line 2803)
CLASS: HISTORY
SUMMARY: This pass cut chapter 2 by 20 percent and chapters 4 and 5 by 13.5 percent, and made chapter 3 central by what leads into it. It left three things with the author: moving chapter 3 earlier, folding thin subsections, and the gap between 13.5 and 20 percent.
STILL TRUE AND NEEDED: none.
NOW FALSE: "Chapter 3 is byte-identical" (it was changed at D-096 and has been rewritten since); "797 resolved references"; "green on all seven"; "refs.bib was not pruned" (unused entries were moved to `unused_bibliography.bib`: pipeline.md, "The source layout").
OPEN ITEMS:
- "Moving chapter 3 earlier was not taken ... left with the author" | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md, "Q-028 — Whether chapter 3 should move earlier. **Closed by execution, D-102 (P38), on (a).**" | FROM: D-090
- Thin subsections, "Available on request" | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md, "Q-029 — The subsections P29 left thin. **Closed by execution, D-102 (P38), on (b).**" | FROM: D-090
- "Why 13.5 and not 20 ... Left with the author, not taken." | VERDICT: CLOSED | EVIDENCE: Q-027 was ruled "left open" at D-111 ("a later pass may revisit it"). The thing it concerned no longer exists: the evidence it named (inattentional blindness, predictive coding, the Kohlberg box, the trolley literature) appears nowhere in `manuscript/sections/` ("inattentional", "Kohlberg", "predictive coding" and "trolley" all return nothing). QUESTIONS.md still carries Q-027 above its Resolved line. | FROM: D-090
- Twelve `\autocite` keys left uncited; refs.bib not pruned; `xref_content.py` not re-run; 185 pages not looked at | VERDICT: CLOSED | EVIDENCE: the uncited keys were handled by D-111/P47 and Q-030 closed at D-379 (refs.bib "every one of them cited": pipeline.md, "The source layout"). The rest was overtaken by D-112's read of all pairs and the later rewrites. | FROM: D-090

## P30 — §10.3's cases moved into chapter 6; the conclusion synthesizes, 2026-08-28 (D-091) (STATE.md line 2897)
CLASS: HISTORY
SUMMARY: This pass moved the case material of the conclusion's section 10.3 into chapter 6 and rewrote 10.3 as a 340-word synthesis ("The Risk That Does Not Design Out"). It records a renumber map and a correction to P29's word count.
STILL TRUE AND NEEDED: none. That `renumber-map_<date>.tsv` files record each renumber and `trace.py` composes them is a DUPLICATE of `finishing/style.md` §10a ("Reading a number already in the record is `finishing/tools/trace.py`").
NOW FALSE: chapter 6 and chapter 10 as described. The synthesis section's title appears nowhere in the manuscript.
OPEN ITEMS:
- "Not checked": whether chapter 6 reads as one chapter; references to moved material by description; `xref_content.py` | VERDICT: CLOSED | EVIDENCE: the chapters concerned no longer exist (no surviving title; the Obermeyer, Clearview and Rekognition cases are absent from `manuscript/sections/`). The reference-by-description defect P31 found was repaired in P31 itself. | FROM: D-091

## P31 — chapter 9 as a prioritized research program, 2026-08-28 (D-092) (STATE.md line 2967)
CLASS: HISTORY
SUMMARY: This pass turned August's chapter 9 from a catalog into nine ranked research problems, each closing with a "near-term work" block, at an unchanged word count. It found that the nine institutional preconditions are one condition (an outside party with access), and it repaired a pointer left stale by P30's move.
STILL TRUE AND NEEDED: the general warning, drawn from the repaired defect, that a reference that still resolves can point at a chapter that no longer holds the material, and that `check_xrefs.py` disclaims this. It recurs in P34, P37 and P38; see P38 below for the passage, its check and its proposed home. Nothing else.
NOW FALSE: the chapter and its blocks (`\runin{The near-term work}` returns nothing in the manuscript); "188 to 189 pages".
OPEN ITEMS:
- "Whether chapter 10 should now cite the program as a program was not taken up." | VERDICT: CLOSED | EVIDENCE: the thing it concerned no longer exists. Neither the research-program chapter nor the August conclusion survives; the nearest current chapters are "What Would Change the Argument" and the Epilogue in `ORDER.tsv`, which are different texts. | FROM: D-092
- "No claim in the chapter was re-verified — the citations ... carried across unexamined"; nine of twelve pages not read in the PDF; `xref_content.py` not run | VERDICT: CLOSED (specific) / ALREADY LISTED (general) | EVIDENCE: the chapter is gone. The general state, that bibliography entries are unchecked by a human, is ALREADY LISTED: "809 of 820 bibliography entries are unchecked by a human (`finishing/refs-ledger.tsv`; the footer's 11/820)". | FROM: D-092

## P32 — chapter 8 split into three chapters, 2026-08-28 (D-093) (STATE.md line 3081)
CLASS: HISTORY
SUMMARY: This pass split August's 23,470-word chapter 8 into three chapters (political economy; policy, law and accountability; governance across borders) under a 23,000-word cap, with 189 references repointed. It reversed Q-018's earlier ruling.
STILL TRUE AND NEEDED: none.
NOW FALSE: all three chapter titles (none survives in `ORDER.tsv` or the manuscript); "46 accepted, 116 drafted"; "189 pages".
OPEN ITEMS:
- "The chapter titles were written in this pass and have not had the author's read." | VERDICT: CLOSED | EVIDENCE: none of the three titles exists in `manuscript/sections/ORDER.tsv` or the manuscript. The current agent-chosen titles are a different item, ALREADY LISTED ("Titles the agent chose, unconfirmed"). | FROM: D-093
- Only three pages read as typeset; `xref_content.py` not run; claims not re-verified; references by description not swept; chapter 9's contrastive density "measured, not swept" | VERDICT: CLOSED | EVIDENCE: overtaken. The chapters no longer exist, and the reference question was answered by D-111/D-112 (`xref_pairs.py`, all 829 pairs read). | FROM: D-093

## Four defects from the author's read, 2026-08-28 (D-096) (STATE.md line 3183)
CLASS: HISTORY
SUMMARY: Four repairs from the author's read. LIME and SHAP were credited with finding the Obermeyer bias, which they could not; a safety/ethics aphorism overclaimed in both directions; three references printed "chapter 0" for the unnumbered "On Method"; and a stipulated 4-percent figure had been called a bound.
STILL TRUE AND NEEDED: none. The mechanism behind the "chapter 0" defect (`\unnumberedlabel` makes `\ref` print the string it is given) is still in `manuscript/preamble.tex` line 431. But no `\ref` in the manuscript points at an unnumbered label (`ch:preface`, `ch:glossary`, `sec:35`), and `sec:0` is no longer referenced, so there is no live hazard to warn about.
NOW FALSE: "`\chapter*{On Method}`" (the front matter is now the Preface, with a "Note on Method" as `chA/0_method.tex`); "186 pages"; "Chapter 3 is no longer byte-identical to what P29 left" (it has been rewritten whole since).
OPEN ITEMS:
- Q-033: the taxonomy of bias sources has no entry for choice of training target | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md Q-033, "**Ruled 2026-08-29 (D-111): option (b), executed in P47.** Target choice is in section 6.1.1's opening list ...". "Obermeyer" now appears nowhere in the manuscript. | FROM: D-096
- "The committed proof pair was built before these edits and prints the old text" | VERDICT: CLOSED | EVIDENCE: the current pair is dated 2026-11-23, built from `4fb4d86b` (STATE.md lead; README.md line 8). | FROM: D-096
- The book was not swept for the safety aphorism restated in other words, nor for other places where an audit method is credited with more than it can establish | VERDICT: NOT RECHECKED | EVIDENCE: the literal aphorism ("indexed to a party", "ethics is not indexed") occurs nowhere in `manuscript/sections/`; the only "indexed to" is the U-bond in `ch32/32.tex`. A sweep for the same idea "in other words" can't be done by phrase search, and the text it was aimed at was rewritten by D-288 and later. | RESTATED: No one has swept the current book for overclaims of what an audit or interpretability method can establish, or for safety treated as owed only to the operator. It is a reading task, not a phrase check. Given that the targeted prose is gone, it can likely be dropped rather than listed. | FROM: D-096

## P33 — the training pipeline, and the recuperation claim, 2026-08-28 (D-097) (STATE.md line 3272)
CLASS: HISTORY
SUMMARY: This pass rebuilt August's section 4.2 as the modern training pipeline (instruction tuning, preference optimization, constitutional methods, process supervision, scalable oversight, interpretability, system prompts), with nine citations verified. It corrected the book's "the mechanism moves nothing" account of recuperated dissent to one about what aggregation strips from dissent.
STILL TRUE AND NEEDED:
- The caution that an automated summary had attributed three papers to Anthropic and the author lists did not support it. In substance this is a DUPLICATE of `finishing/style.md` §6 ("The agent writes a reference entry only from metadata it has verified against the source itself (D-204)").
NOW FALSE: section 4.2 as described ("Constitutional AI" appears nowhere in the manuscript now); "167 sections, 94,037 words ... 193 pages"; "40 accepted, 127 drafted"; "`irving2018aisafety`" (merged away; `irving2018ai` is cited in `ch22/22_02.tex`).
OPEN ITEMS:
- "No section here has the author's read"; `xref_content.py` not run over the new material; 4.1.2 not touched; chapter 5 not restructured; contrastive density "measured rather than swept" | VERDICT: CLOSED | EVIDENCE: overtaken. The sections are gone (D-288 and later), and the reference question was answered by D-111/D-112. The chapter-5 question became Q-035; QUESTIONS.md records it as measured at D-113 with "the ruling is the author's", and it is still filed above the Resolved line. Its subject, August's chapter 5 on human moral psychology, no longer exists in that form (Kohlberg, trolley, inattentional blindness and predictive coding all absent). | FROM: D-097

## P34 — the chapter 3 inference fortified, 2026-08-28 (D-098) (STATE.md line 3366)
CLASS: HISTORY
SUMMARY: This pass added two sections to chapter 3: four senses of refusal, with the floor requiring only reasons-responsive refusal; and four non-affective rivals for holding a reason (Bratman, Elster, plural models, Balkin's fiduciary). It cut the book's own induction down, stated a falsifier, and made Cassell no longer load-bearing alone. It found two reference defects of the D-050 class by hand.
STILL TRUE AND NEEDED: the D-050-class warning (a reference that resolves but names a claim its target doesn't make passes both `check_xrefs.py` and `xref_content.py`). See P38 below.
NOW FALSE: chapter 3's structure and titles (neither new section title survives; "Ulysses" and "Elster" return nothing, while Bratman and Balkin survive in `ch18/18_03.tex`); "169 sections ... 198 pages".
OPEN ITEMS:
- Q-036, what chapter 3's new length means for where it sits | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md Q-036, "**Ruled 2026-08-29 (D-111): leave, and the question closes.**" | FROM: D-098
- Q-037, the plural arrangement is recommended and no chapter develops it ("the one obligation this pass created and did not discharge") | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md Q-037, "**Ruled 2026-08-29 (D-111): leave, carried as research.**". "plural arrangement" no longer occurs in the manuscript. | FROM: D-098
- "Sections 3.5, 3.6, 3.7 and 3.9 were not reread"; contrastive sweep of chapter 3 not done; no author read | VERDICT: CLOSED | EVIDENCE: overtaken. Chapter 3 was rewritten by the author's September 12 return (D-288) and is now a different chapter ("How to Tell When It's a Bad Vibe"). | FROM: D-098

## P35 — mannerisms, editorial archaeology, the cross-reference cut, 2026-08-29 (D-099) (STATE.md line 3446)
CLASS: MIXED (history, with a standing style rule that no working document states)
SUMMARY: This pass applied the author's instruction that named prose mannerisms are cruft, that editorial archaeology does not belong in the manuscript, and that cross-references which only announce agreement go. It cleared four mannerism families and a fifth (the announced concession) and cut fifteen archaeology passages and 78 references. It records the finding that the contrastive-construction rate does not locate the tic; the pile-up does.
STILL TRUE AND NEEDED:
- The rule against editorial archaeology and the named mannerisms. Close paraphrase of the text and of D-099's row: *"Editorial archaeology does not belong in the manuscript at all — what an earlier draft said, what a section used to claim — because the repository carries the revision record."* The mannerism families cut as metadiscourse: "the honest {answer, report, summary, way ...}", "it is worth {saying, stating, marking, naming, being exact about}", "what belongs here is", "this section used to", and the announced concession ("I would rather say so here than let a reader find it out"; the rule is that the concession stays and the announcement of it goes). Checked against: `finishing/style.md` (§2 "Section shape", §3 "Word-level lint", §7, §10), `AGENTS.md`, `agents_repository.md` and `finishing/pipeline.md`. None states either rule; `finishing/tools/tics.py` catches only "it is (important|worth) (to note|noting)". The manuscript is currently clean: no hits for the families, for "an earlier draft/version of this", or for "I no longer think". The rule is still live in the record (a later DECISIONS row cites "D-099's editorial archaeology surviving in the conclusion"). UNIQUE. Proposed home: `finishing/style.md` §2, "Section shape", as a further "Delete on sight" bullet, e.g. "**Editorial archaeology** (D-099): what an earlier draft said, what a section used to claim, 'I no longer think'. The repository is the revision record; state the corrected claim. And the metadiscursive mannerisms: 'the honest answer', 'it is worth saying', 'what belongs here is', and the announced concession, where the concession stays and its announcement goes."
- The contrastive finding: *"The contrastive rate does not identify the tic ... What grates is the **pile-up**, two or more inside one sentence"* (chapters whose content is contrastive score high and are precise). Checked against `finishing/style.md` §2 (corollary "Prefer the positive construction to 'not X. It is Y.'") and §10 ("The contrastive frame is D-025 wherever it appears"). Neither says a per-word rate is a poor locator or names the pile-up. UNIQUE, minor. Proposed home: one sentence under style.md §2's contrastive corollary: "A rate of contrastive constructions per thousand words does not find the fault, since contrastive content scores high and is precise; look for two or more inside one sentence (D-099)."
NOW FALSE: "883 to 805" references; "98,134 words to 97,092"; "22 accepted and 147 drafted"; "the 340 surviving 'rather than' instances" (Q-038 was swept at D-113).
OPEN ITEMS:
- Q-038, the 340 remaining "rather than" constructions, not individually judged | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md Q-038, "**Ruled 2026-08-29 (D-111): option (c), sweep chapters 2, 3 and 4**", then "**Swept 2026-08-29 (D-113, P49). Done**". The rest: "205 instances remain outside chapters 2, 3 and 4, and option (b) was declined at D-111". | FROM: D-099
- "No section has the author's read" | VERDICT: CLOSED | EVIDENCE: overtaken by the author's September 12 return (D-288) and later rewrites. | FROM: D-099

## P36 — the conclusions that recur across chapters, 2026-08-29 (D-100) (STATE.md line 3508)
CLASS: HISTORY
SUMMARY: The author asked for about 5,000 words cut from recurring conclusions. Measured, the class held about 2,051 words. The pass cut section 3.9 whole, reduced repeated statements of the spine chain to pointers, and costed the ways of reaching 5,000 as Q-039.
STILL TRUE AND NEEDED: none. The finding that connective tissue had been deliberately added by earlier passes is a historical argument about August's book. `finishing/style.md` §10's corollary ("Do not cite the work already done as context for the work outstanding") argues against carrying it forward.
NOW FALSE: "169 sections to 168, 97,092 words to 95,041, 197 pages to 192, 805 `\ref` to 785"; "20 accepted and 148 drafted".
OPEN ITEMS:
- Q-039, reaching 5,000 means cutting something other than recurrence; options left with the author | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md Q-039, "**Ruled 2026-08-29 (D-111): stop at 2,051.**" | FROM: D-100

## P37 — inventories in chapters 8–10, and the jobs guarantee halved, 2026-08-29 (D-101) (STATE.md line 3585)
CLASS: MIXED (history, with one tool caveat the record later reversed)
SUMMARY: This pass replaced inventory passages in August's chapters 8 to 10 with worked cases (FTC v. Meta added; seven intergovernmental bodies cut to three) and cut the jobs-guarantee section from 3,212 to 1,842 words by restructuring around its main objection. It introduced `inventories.py`, found a pre-existing reference that named a claim its target lacked, and orphaned eight bibliography keys.
STILL TRUE AND NEEDED:
- `finishing/tools/inventories.py` still exists. The text's advice, *"Keep the tool for locating chapter 10 and for its false-positive rate"*, is superseded by D-111's ruling on Q-040: *"adopt the rule, drop the metric. ... where a run of cases each carries a distinct claim it is not an inventory however long it runs, and the real ones appear only in section openers, closing run-ins and remedy lists, which are findable by position. The syntactic score is not to be used as evidence again."* Checked against `finishing/style.md` §2a (which condemns "the catalog" but gives neither the distinct-claim test nor the warning about the tool), `finishing/pipeline.md` and `agents_repository.md`; `inventories.py` is named in none of them. UNIQUE, minor. Proposed home: `finishing/style.md` §2a, after "The catalog": "A run of cases each carrying a distinct claim is not a catalog however long it runs; real inventories sit in section openers, closing run-ins and remedy lists. `inventories.py`'s syntactic score is not evidence (D-111, Q-040)."
- The D-050-class defect ("section 8.3.4's list has never contained a job category"). See P38.
NOW FALSE: "Keep the tool for locating chapter 10" (D-111); "Q-030's count, which moves from 14 to 22 of 304 entries" (Q-030 closed at D-379); "Nothing was deleted from `refs.bib`; pruning is Q-030's decision and has not been taken" (taken at D-111: moved to `unused_bibliography.bib`); "192 → 189 pages".
OPEN ITEMS:
- Q-040, "what part one did not reach" (inventories outside chapters 8 to 10) | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md Q-040, "**Ruled 2026-08-29 (D-111): adopt the rule, drop the metric.**" | FROM: D-101
- Eight bibliography keys lose their last citation; Q-030's pruning not taken | VERDICT: CLOSED | EVIDENCE: all eight (`justcapital2018amazongo`, `openai2018charter`, `moda2025basic`, `peacetechlab2019monitoring`, `unesco2021recommendation`, `gpai2020joint`, `g72023hiroshima`, `deepmind2016partnership`) are in `finishing/unused_bibliography.bib` and absent from refs.bib. Q-030 was "Ruled ... (D-111), and executed in P47" and closed at D-379. | FROM: D-101
- "No section has the author's read" | VERDICT: CLOSED | EVIDENCE: overtaken (D-288 and later). Clearview, Rekognition and Bletchley appear nowhere in the manuscript now. | FROM: D-101

## P38 — the floor argument earlier, chapters 2–5 distilled, 2026-08-29 (D-102) (STATE.md line 3684)
CLASS: MIXED (history, with one still-true warning stated in no working document)
SUMMARY: This pass took up P29's three deferred items. It delivered chapter 3 "earlier" in pages, not position; merged eight chapter-2 subsections and six chapter-5 subsections; and cut chapter 4's section 4.1 while sparing the pipeline. It found six reference defects of the D-050 class, four of them older than the pass, and noted that no tool finds that class, opening Q-041.
STILL TRUE AND NEEDED:
- The D-050-class warning, stated here most fully and recurring in P31, P34 and P37: *"No tool finds this class — `check_xrefs.py` resolves a reference and cannot read it, and `xref_content.py` fires only where the citing sentence names a proper noun, acronym or year"*, and (P31, P38) such defects surface "only because a renumber forces every citing sentence to be read", including references to moved material by description rather than by number. Checked against: `finishing/tools/check_xrefs.py`'s docstring, which states the limit ("What this does NOT check: whether a reference points at the RIGHT section. ... has to be redone by hand after any renumbering"), and the working documents. `finishing/pipeline.md`, "The source layout", says only "You do **not** have to chase the cross-references: since D-066 they are `\ref{sec:N}`, so LaTeX regenerates every printed number". Read alone, that sentence invites the mistake. `finishing/style.md` §7/§7a, `agents_repository.md` and README.md don't state the limit, and `xref_pairs.py` (built for it at D-111) is named in no working document. The warning still applies: the book still carries about 264 parenthetical references (ALREADY LISTED item on revision-list item 15) plus worded pointers ("a later chapter"), and moves and renumbers continue (D-1068, D-1116). UNIQUE. Proposed home: `finishing/pipeline.md`, "The source layout", directly after the "You do not have to chase the cross-references" sentence, e.g. "That covers the printed number, not the meaning: a `\ref` that resolves can name a claim its target no longer makes, and a worded pointer ('chapter 10's territory', 'a later chapter') can name material that has moved. `check_xrefs.py` checks resolution only. After a move, a cut or a renumber, read each citing sentence against its target; `finishing/tools/xref_pairs.py` prints every citing sentence beside its target's opening (D-050, D-111)."
NOW FALSE: "Q-041 carries what that implies for the nine chapters nobody has read" (closed: D-111 built `xref_pairs.py`, and D-112 read all 829 pairs); "Book 92,986 → 88,346 words, 168 → 153 sections, 189 → 182 pages"; "13 accepted, 140 drafted"; "orphaned bibliography entries 22 → 23 of 304, and nothing was deleted from `refs.bib`, which is Q-030's decision" (moved at D-111/P47; `jigsaw2017perspective` is in `unused_bibliography.bib`).
OPEN ITEMS:
- Q-041, the nine chapters not read for references that resolve but name a claim their target lacks | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md Q-041, "**Ruled 2026-08-29 (D-111): build a tool, executed in P47** ... `finishing/tools/xref_pairs.py` ... **829 pairs across 153 sections**", then "**Read 2026-08-29 (D-112, P48).** All 829 pairs, in order. **Six defects, each confirmed**". The class as a standing hazard is the still-true warning above, not an open item. | FROM: D-102
- "No section has the author's read" | VERDICT: CLOSED | EVIDENCE: overtaken (D-288 and later restructures). | FROM: D-102
- Orphaned `jigsaw2017perspective`; pruning "is Q-030's decision" | VERDICT: CLOSED | EVIDENCE: in `finishing/unused_bibliography.bib`, absent from refs.bib; Q-030 closed at D-379. | FROM: D-102

# Report 4 of 4

# Triage of rest-4.md (STATE.md lines 3786 to about 4724, P39 to P57)

Checked against the tree on 2026-11-23 (HEAD `fe40bde7` plus the uncommitted working files named in the git status). No repository file was edited.

Facts used across the sections below, checked once:
- **QUESTIONS.md** (`finishing/QUESTIONS.md`, 114 `### Q-` entries) was last committed on 2026-09-19 (`0e044bd4`). Its own header says "Current as of 2026-09-19, after D-461" and "Thirty-six of the thirty-eight open entries have still not been read against the current book". No decision after D-467 touches it. `finishing/README.md` still calls it "The open batch for the author". Several open items in these sections are QUESTIONS.md entries (Q-035, Q-042, Q-043, Q-045, Q-053) that were never closed there.
- **The August chapter numbers no longer name the same text.** `trace.py 11.2 --as-of 2026-08-30` maps August 11.2 to today's `ch15/15_02.tex`, "Who may amend, and where entitlement comes from", across the 2026-09-12 return (D-288), which "cut 43 sections and rewrote most of what it kept". Today's chapter 1 is "Twenty Seconds" (`ch01/01.tex`), not the August introduction-with-roadmap.
- **Gone from the manuscript** (grep of `manuscript/sections/`): "partition" in the non-separability sense; "molar"/"molecular" and the five discriminators; the glossary entries *Exit*, *Molar*, *Molecular*; "the bearer that called the compound a school"; "not separable from general competence"; Dweck and "growth mindset"; the Sachsenhausen/Krüger/Malkin/Burger and Gallup material (Operation Bernhard survives in one sentence of `ch14/14_04.tex`, Hirschman in `ch14/14_03.tex`). `garcia2025character`, `zhu2019leakage`, `sun2024zkllm`, `wilcox2025` and `menand2026exception` are in `unused_bibliography.bib`, cited nowhere.
- **Still present:** *Slaughter* and *Cook* (`slaughter2026`, `cook2026`) in `ch18/18_01.tex` only; the Council of Europe Framework Convention "not yet in force" in `ch16/16_07.tex` (`coe2024framework`, `coe2026euratifies`, both unchecked in `refs-ledger.tsv`); the pet trust in `chG/G.tex` and `ch35/35_03.tex`; the Gordon jury figure, correct as P54 left it ("Eighteen community moderators ... changed the outcome on 14% of items", `ch22/22_05.tex`).
- **Run-in heads:** all 146 `\runin{...}` heads in the manuscript read as sentence case; the only two capitalized are proper nouns ("Additional Protocol I", "The Melt ICE Act's provisions").
- **Committed analysis reports** in `finishing/reports/` (`xref_shapes.tsv`, `xref_pairs.txt`, `xref_content.tsv`, `hedge_pairs.tsv`, `claims.tsv`, `tics.tsv`, `negatives.tsv`, `epigram.tsv`, `redundancy_*.tsv`, `reader_tax.tsv`, `section_stats.tsv`, `dated.tsv`, `list_candidates.tsv`) were last committed 2026-09-19 or 2026-09-20, before the restructures of D-1068 and D-1116.
- **`finishing/ledger.tsv`**: all 220 rows have status `drafted`; no row has ever moved past it.
- **`check_structure.py`, `check_xrefs.py` and `check_typography.py`** enumerate section files with `glob(SECTIONS/ch*/*.tex)`; none of the checks in `check_all.sh` lists `.tex` files at `manuscript/sections/` itself or in a deeper folder. No stray file is there today (`ls manuscript/sections/`: the `chNN`/`chX` folders and `ORDER.tsv`).

---

## P39 — Replacement stated as open, the falsifier as an obligation, the bearer as necessary and not sufficient, 2026-08-29 (D-103) (STATE.md line 3786)
CLASS: HISTORY
SUMMARY: The pass answering forwarded feedback on August chapter 3: section 2.4.3 states Replacement as open, the falsifier becomes an obligation, and section 3.5 states the bearer as necessary and not sufficient, with hardware and software attestation added. Word, page and cross-reference counts; HTML not built.
STILL TRUE AND NEEDED: none.
NOW FALSE: "88,346 → 89,363 words ... 182 → 183 pages, 153 sections" (the proof of 2026-11-23 is 539 pages); "the committed proof pair is one pass stale" (the pair of 2026-11-23 is current); `sun2024zkllm` is no longer cited (moved to `unused_bibliography.bib`).
OPEN ITEMS:
- Operation Bernhard, the CFPB sequence and *Trump v. Wilcox* "still need checking before any of it is written" | VERDICT: CLOSED | EVIDENCE: P40 (D-104) verified each ("Every case from its full text at Cornell LII except *Wilcox* ... the CFPB notice from the Bureau's own release"); `wilcox2025` is now uncited, in `unused_bibliography.bib` | FROM: D-103
- The P40 work list (refusal asymmetry, removal cases, jobs-guarantee shape, deception protocol, collapse paragraph) | VERDICT: CLOSED | EVIDENCE: executed by P40, D-104 ("confirmed (author's instruction)") | FROM: D-103
- HTML not built; proof pair stale | VERDICT: CLOSED | EVIDENCE: STATE.md lead: pair of 2026-11-23 current, HTML with 4,017 internal links | FROM: D-103

## P40 — the refusal asymmetry, its strike and covert forms, and the removal cases, 2026-08-29 (D-104) (STATE.md line 3843)
CLASS: HISTORY
SUMMARY: Section 3.7 gains the refusal asymmetry in Hirschman's terms, the strike and covert forms of exit (Sachsenhausen counterfeiters, Gallup's engagement figures), and the removal cases *Slaughter* and *Cook* enter four sections, with verification sources listed.
STILL TRUE AND NEEDED: none. (The rule that no justice is named or credited with a motive is an application of the named-persons rule in `agents_repository.md`, "Security Boundaries"; DUPLICATE.)
NOW FALSE: "89,363 → 91,079 words, 183 → 186 pages"; "Chapter 3 ... 13.2 percent of the book"; "HTML not built; the proof pair is two passes stale". The Sachsenhausen, Malkin, Burger and Gallup material is no longer in the manuscript (grep); Menand is uncited (`menand2026exception` in `unused_bibliography.bib`).
OPEN ITEMS:
- The proofs | VERDICT: CLOSED | EVIDENCE: pair of 2026-11-23 current (STATE.md lead) | FROM: D-104
- Q-042: the removal cases are new and could move (Menand's three ways); the author's ruling at D-111 was "leave, and re-read the six sites at each proof" | VERDICT: OPEN | EVIDENCE: QUESTIONS.md Q-042 ends on that ruling and was never closed; `finishing/pipeline.md`, "Make the proofs", has no such step; no later decision records a re-read. The cases now stand only in `ch18/18_01.tex` ("The worked case is June 29, 2026 — *Slaughter* holding Congress couldn't protect independent-agency members from at-will dismissal, *Cook* preserving the Fed ..."); the pet trust, which the ruling covered as private law outside *Slaughter*, is in `chG/G.tex` and `ch35/35_03.tex`. Not in the STATE.md open list | RESTATED: D-111 ruled that the sentences resting on *Trump v. Slaughter* and *Trump v. Cook* be re-read at each proof in case the law moves; the step was never written into "Make the proofs" and no re-read is recorded. The sites are now `ch18/18_01.tex` (and, for the private-law point, the pet-trust passages of `chG/G.tex` and `ch35/35_03.tex`). The author can keep the ruling (add it to the proof steps) or retire it | FROM: D-104, D-111
- "No section has the author's read" | VERDICT: CLOSED | EVIDENCE: the P40 text was rewritten in the 2026-09-12 return (D-288) and the restructures of D-1068 and D-1116; the author has since marked whole-book proofs (`finishing/reviews/whole-book-proof_2026-10-21_NOTES.pdf`, `..._2026-11-12_NOTES.pdf`). The current unread-by-author items are in the STATE.md open list | FROM: D-104

## P41 — propagation after P39 and P40, 2026-08-29 (D-105) (STATE.md line 3897)
CLASS: HISTORY
SUMMARY: A sweep of what the P39/P40 changes left contradicted: section 3.5's shutdown/refusal identity reconciled as the pricing of the halt, with residue repaired across chapters 1, 3, 11 and 12.
STILL TRUE AND NEEDED: none. (The lesson "a pass that changes what a chapter claims has to reread what was written on the old claim" is the Q-043 class, carried by the `hedge_pairs.py` row of `finishing/README.md`, "Tools"; DUPLICATE in substance.)
NOW FALSE: "91,079 → 91,443 words, 186 → 187 pages"; "HTML not built; the proof pair is three passes stale".
OPEN ITEMS:
- "Not read for the same residue: chapter 5's other sites that touch the override requirement (5.1.1, 5.2.3, 5.3)" | VERDICT: NOT RECHECKED | EVIDENCE: the item quotes no phrase and names only August section numbers; August chapter 5 was cut from 29 to 23 sections at P38, compressed at P112 (D-210) and rewritten in the 2026-09-12 return and later restructures, so the sites can't be located | RESTATED: An August note that three sites in the then chapter 5 touching the override requirement were not reread after the halt was redefined as a price. The text it concerned has been rewritten; it is covered, if at all, by the listed item that no one has reread the book whole since D-1068 and D-1116 | FROM: D-105

## P42 — the legal claims a second reader checked, 2026-08-29 (D-106) (STATE.md line 3924)
CLASS: HISTORY
SUMMARY: Seven legal claims an outside reader flagged, all landing: the EU AI Act's reach over government uses, the Council of Europe convention's status, and five qualifications. Four of the seven were one chapter stating flatly what another qualified (the start of Q-043). The proof pair rebuilt in place.
STILL TRUE AND NEEDED: none. (Rebuilding the pair in place when the date has not rolled over is in `finishing/pipeline.md`, "Make the proofs"; DUPLICATE.)
NOW FALSE: "Q-043 records it: no tool finds it and nothing has swept for it" (swept by subject at P49, D-113; `hedge_pairs.py` built for it, D-378); "current at 187 pages"; `zhu2019leakage` and `garcia2025character` are now uncited.
OPEN ITEMS:
- The Council of Europe Framework Convention as not in force ("would bind a party, once in force, which at this writing it is not"; every reachable source used the future tense, the treaty chart returned 403) | VERDICT: NOT RECHECKED | EVIDENCE: the claim stands in `ch16/16_07.tex`: "and not yet in force, needing five ratifications, of which the EU deposited one in May 2026"; `coe2024framework` and `coe2026euratifies` are unchecked in `refs-ledger.tsv`, and the current proof has a biber warning on `coe2026euratifies` (STATE.md lead). Whether the convention has entered force since needs the network, which this check did not use. Not in the STATE.md open list | RESTATED: `ch16/16_07.tex` says the Council of Europe's Framework Convention is "not yet in force". That was true by the sources reachable on 2026-08-29; it needs checking against the Council's treaty office before the book is final | FROM: D-106
- Q-043, the class of a flat claim in one chapter that another qualifies | VERDICT: ALREADY LISTED (as instances) | EVIDENCE: the class was swept at P49 (D-113) and has a tool (`hedge_pairs.py`, D-378, `finishing/README.md`); current instances are in the open list, e.g. "Two custody passages seem to conflict" (`ch14/14_01.tex` vs `ch14/14_03.tex`), "Two accounts of *patienthood indicator*", and "Self-descriptions the sweep found true only narrowly". The entry in QUESTIONS.md was never closed (see P57) | FROM: D-106

## P43 — identity by registration, and whether formation is legible, 2026-08-29 (D-107) (STATE.md line 3969)
CLASS: HISTORY
SUMMARY: An exchange on whether initialization entropy identifies a model: permutation symmetry makes a weight fingerprint identify an equivalence class; identity by registration ("social security number, not chattel") and a formation-forensics experiment go into section 11.2; fingerprinting as a criterion of personhood declined.
STILL TRUE AND NEEDED: none. (The experiment survives in the book as Appendix F's open problem "Recovering provenance", `chF/F.tex`.)
NOW FALSE: "91,785 → 92,473 words, 187 → 189 pages"; "Section 11.2 is 1,281 → 1,873 words" (August 11.2 no longer exists in that form); "HTML not built; the proof pair is one pass stale".
OPEN ITEMS:
- HTML not built; proof pair stale | VERDICT: CLOSED | EVIDENCE: pair of 2026-11-23 current | FROM: D-107

## P44 — the assembly, identity as something a bearer does, and compute as the floor under exit, 2026-08-29 (D-108) (STATE.md line 4011)
CLASS: MIXED
SUMMARY: The harness gap (the floor placed in the weights while what acts is an assembly), James on commitment across time, the checkpoint restore's detectability, compute as the floor under exit. Then a defect outside the pass: a byte-identical stray copy of a section file at `manuscript/sections/`, from a shell-redirection accident, which no check saw.
STILL TRUE AND NEEDED:
- The stray-file blind spot: "Grepping for `harness` turned up a byte-identical copy of 05_07_01.tex at `manuscript/sections/`, from a shell-redirection accident during P38 ... `check_structure.py` globs `chNN/*.tex` and did not see it; the build did not, because `sections.tex` comes from ORDER.tsv." Checked against `finishing/tools/check_structure.py` line 53 (`glob(SECTIONS, "ch*", "*.tex")`), `check_xrefs.py` line 59 and `check_typography.py` line 60 (same glob), and `check_all.sh`: still true; no check lists a `.tex` at `manuscript/sections/` itself or one folder deeper, and the build ignores such a file. Not stated in `pipeline.md`, `style.md`, `agents_repository.md`, the README or `finishing/README.md` (whose `check_structure.py` row says only "Heading/filename agreement, glob order, tag balance, ledger row parity"). UNIQUE. Proposed home: `finishing/README.md`, the `check_structure.py` row of "Tools" (one sentence: it sees only `manuscript/sections/ch*/*.tex`, so a stray `.tex` at `manuscript/sections/` or in a subfolder of a chapter folder passes every check and the build), or `finishing/pipeline.md`, "Things worth knowing". The better fix is for `check_structure.py` to fail on any `.tex` under `manuscript/sections/` outside `ch*/`, which would retire the warning.
NOW FALSE: "92,473 → 93,529 words, 189 → 190 pages"; "current at 190 pages"; "zero hits across all 153 sections".
OPEN ITEMS:
- The harness gap: section 3.1 "says the book does not close it" (Q-044) | VERDICT: CLOSED | EVIDENCE: P47 (D-111) cut the parts list and replaced it with a functional definition ("anything that can come between a refusal and the person the refusal protects"), with enumeration pushed to the deployment; Q-044 was ruled at D-111. The text has since been rewritten | FROM: D-108
- The stray file | VERDICT: CLOSED | EVIDENCE: removed in `6cdbd9a` (pre-rewrite ID; `finishing/sha-map_2026-10-03.tsv` translates it); `ls manuscript/sections/` shows no stray file today. The blind spot that let it through is above | FROM: D-108

## P45 — the floor raises the roof, 2026-08-29 (D-109) (STATE.md line 4060)
CLASS: HISTORY
SUMMARY: The author's observation that a compute floor works like the jobs guarantee: an outside option is leverage that works without being exercised; its failure mode (a bearer shaped not to want the option); and a first answer to section 3.5's impasse over where the dial goes.
STILL TRUE AND NEEDED: none.
NOW FALSE: "93,529 → 93,911 words, 190 → 191 pages"; "current at 191 pages"; "Section 11.2 is 2,624 words".
OPEN ITEMS:
- "Section 11.2 ... has not been read whole since before any of them" | VERDICT: CLOSED | EVIDENCE: read whole at P49 (D-113, "Q-045, chapter 3 and section 11.2 read whole") | FROM: D-109

## P46 — the open questions reviewed against the manuscript, 2026-08-29 (D-110) (STATE.md line 4104)
CLASS: HISTORY
SUMMARY: Seventeen QUESTIONS.md entries re-measured against the tree; Q-028 and Q-029 closed; six figures had reversed; Q-045 opened (seven conversation-driven passes concentrated in chapter 3 and section 11.2, and nothing in the discipline sums a day). No manuscript file touched.
STILL TRUE AND NEEDED: none. ("`check_all.sh` has no size invariant" is still true but is a fact, not a rule a session needs.)
NOW FALSE: "The cross-reference count is 826"; "Chapter 3 is 13,343 words and 14.21 percent"; "`refs.bib` is 23 uncited of 326" (now 820 entries, every one cited per `pipeline.md`, "The source layout"); "Eighteen questions open".
OPEN ITEMS:
- Re-checks naming work not taken: re-count "rather than" in chapters 2 to 4; read chapter 3 and section 11.2 whole | VERDICT: CLOSED | EVIDENCE: both done at P49 (D-113) | FROM: D-110
- Re-measure chapter 2's inventory density | VERDICT: NOT RECHECKED | EVIDENCE: August chapter 2 was compressed at P112 (D-210) and rewritten since; no later decision found that re-measured it. `inventories.py` exists for the measurement | RESTATED: An August note that the then chapter 2's density of lists was not re-measured. The chapter it concerned no longer exists in that form; the item has no current target | FROM: D-110

## P47 — the author's rulings on the open questions, groups 1 to 3, 2026-08-29 (D-111) (STATE.md line 4143)
CLASS: HISTORY
SUMMARY: The author ruled on eighteen questions: nearest-work clauses restored to section 11's gaps, target choice added to 6.1.1, the parts list cut for a functional definition; uncited entries moved to `unused_bibliography.bib`; bibliography notes sorted (describe the source, not the checking) and capped; `xref_pairs.py` built.
STILL TRUE AND NEEDED:
- Uncited entries go to `finishing/unused_bibliography.bib`, not `\addbibresource`d. DUPLICATE of `finishing/pipeline.md`, "The source layout" (the `refs.bib` row: "Entries nothing cites live in `unused_bibliography.bib` ... started at D-111").
- The note rule ("a note stays if it says what the source says or is, goes if it records what was done to check it") and the 802-character cap: superseded by D-772 ("The bibliography notes cut to what a reader needs; agent checks leave the entry"); the surviving half is DUPLICATE of `agents_repository.md`, "Author's Shorthand", "Checking a reference" ("nothing about it goes into the entry").
- `xref_pairs.py` and what it is blind to: DUPLICATE of `finishing/README.md`, "Tools", `xref_pairs.py` row.
NOW FALSE: "`refs.bib` corresponds to the book at 303 entries" (now 820); "829 pairs across 153 sections"; "93,911 → 94,432 words, 191 pages".
OPEN ITEMS:
- Group 4, the reading work (Q-035, Q-038, Q-043, Q-045) | VERDICT: CLOSED | EVIDENCE: P49 (D-113), "Group 4 is done" | FROM: D-111
- "The 829 pairs have not been read either" | VERDICT: CLOSED | EVIDENCE: P48 (D-112), "All 829 pairs read in one sitting ... This supersedes P47's closing line" | FROM: D-111

## P48 — the misdirected references the pairing tool exposed, 2026-08-29 (D-112) (STATE.md line 4194)
CLASS: HISTORY
SUMMARY: All 829 pairs read; six misdirected references found and confirmed against their targets; eight targets checked sound and named in `p48-scope.md`.
STILL TRUE AND NEEDED: none.
NOW FALSE: none beyond the August section numbers.
OPEN ITEMS: none.

## P49 — group 4, the reading work, 2026-08-29 (D-113) (STATE.md line 4201)
CLASS: HISTORY
SUMMARY: Four reading items: Q-043 swept by subject (twenty subjects, two failures repaired); Q-038's "rather than" re-count and three repairs; Q-035's measurement that August chapter 5 cites nothing from 2022 on; Q-045's whole read of chapter 3 and section 11.2 (self-report sentences concentrated there, the chapter's opening map missing 3.5 and 3.6, section 11.2 overlong).
STILL TRUE AND NEEDED: none.
NOW FALSE: "94,415 → 94,488 words, 826 cross-references ... glossary 56 terms"; "205 instances remain outside these three chapters".
OPEN ITEMS:
- Q-035: August chapter 5's citations (median 2009, none from 2022 on) and missing contemporary vocabulary; "A finding to rule on, not a pass" | VERDICT: NOT RECHECKED | EVIDENCE: QUESTIONS.md Q-035 ends "No default is applied ... the ruling is the author's"; no later decision rules on it. But the chapter measured (August chapter 5, 23 sections, its sections 5.2.3 and 5.3.3) was rewritten; whether today's formation chapters have the same gap was not measured here. Not in the STATE.md open list | RESTATED: In August the then chapter 5 (human moral psychology, read for machine formation) cited nothing newer than 2021, and the author never ruled on whether to bring in current machine-training literature. The chapter has since been rewritten; a fresh citation-year count over today's formation chapters would say whether the finding still holds | FROM: D-113
- Q-043's class stays open ("nine instances is a rate, and twenty subjects is not the whole list") | VERDICT: ALREADY LISTED (as instances) | EVIDENCE: see P42 | FROM: D-113
- Q-045 stays open "on what to do about section 11.2" (2,599 words in a 9,000-word chapter, three of the book's longest paragraphs) | VERDICT: CLOSED | EVIDENCE: the section no longer exists in that form; `trace.py 11.2 --as-of 2026-08-30` lands on `ch15/15_02.tex`, "Who may amend, and where entitlement comes from", across the 2026-09-12 rewrite (D-288). QUESTIONS.md Q-045 was never closed (see P57) | FROM: D-113
- Chapter 3's opening map omits sections 3.5 and 3.6, "reported and left" | VERDICT: CLOSED | EVIDENCE: P53 (D-118) cut chapter 3's self-maps ("its opener listed its own eight sections ... 147 → 53"); August chapter 3 has since been split across Parts II and III | FROM: D-113

## P50 — the manuscript read whole, 2026-08-29 (D-114) (STATE.md line 4269)
CLASS: HISTORY
SUMMARY: All 153 sections read in order: four defects reported unrepaired, two findings turned into questions (Q-046, where *holds* is defined; Q-048, chapter 7 runs only the four structural features), and a recorded correction about section 3.5's allusion to the Iran school strike.
STILL TRUE AND NEEDED: none. The "correction, recorded because a later session will repeat it" concerned the sentence "the bearer that called the compound a school", which is no longer in the manuscript (grep), so the warning has nothing left to protect.
NOW FALSE: "94,488 words, 191 pages, 153 sections"; "The proof pair is the one P49 built and is current".
OPEN ITEMS:
- The four defects, unrepaired | VERDICT: CLOSED | EVIDENCE: P51 (D-116), "the four defects repaired" | FROM: D-114
- The seven rulings wanted (Q-046 to Q-052) | VERDICT: CLOSED | EVIDENCE: D-115, "The author's rulings on P50's seven questions", status confirmed | FROM: D-114
- "It does not check a citation against its source, and none was checked here" | VERDICT: ALREADY LISTED | EVIDENCE: open list, "809 of 820 bibliography entries are unchecked by a human" | FROM: D-114

## P51 — the rulings executed, and the four defects repaired, 2026-08-29 (D-116) (STATE.md line 4325)
CLASS: HISTORY
SUMMARY: The definition of *holds* moved into chapter 3; two propagation failures repaired; Q-048 run, the five discriminators clearing all three of chapter 7's instances, three observed and two undetermined.
STILL TRUE AND NEEDED: none.
NOW FALSE: "94,488 → 95,405 words, 191 → 192 pages"; "HTML: 1,337 internal links" (now 4,017).
OPEN ITEMS:
- Two of the five discriminators "could not be settled ... it would take an inside record to finish" | VERDICT: CLOSED | EVIDENCE: the five discriminators and "molar"/"molecular" are no longer in the manuscript (grep), nor in the glossary | FROM: D-116

## P52 — the reader-cost pass, 2026-08-30 (D-117) (STATE.md line 4371)
CLASS: MIXED
SUMMARY: A taxonomy of reader cost derived from the git range of the author's own hand edits, applied across 98 sections; `reader_tax.py` built; four defects found by reading; run-in head capitalization left as a ruling.
STILL TRUE AND NEEDED:
- `reader_tax.py` and its basis in `331f0a5..fc65cd5`: DUPLICATE of `finishing/README.md`, "Tools", `reader_tax.py` row.
- The method: "The eight before/after page pairs were not used as such. The pass reads the git range ... instead, because that is what the author actually applied ... Every edit was classified, and the classes became the thing the remaining ... sections were read against." Checked against `style.md`, `pipeline.md`, `agents_repository.md`, `AGENTS.md`: not stated there. UNIQUE but marginal; D-772 later used the same approach for bibliography notes. If kept, proposed home: `finishing/style.md` §10 or a sentence in `pipeline.md`: when generalizing from the author's hand edits, work from the commits of what he applied, not the pages he was shown, and cite the edit beside each rule drawn from it.
NOW FALSE: "95,095 → 94,017 words"; "363 that use `section~\ref`"; "191 pages ... 1,343 internal links".
OPEN ITEMS:
- Run-in head capitalization inconsistent (Title Case in chapter 9, sentence case in chapter 3), "a ruling and not a defect" (Q-053) | VERDICT: CLOSED (in the tree) | EVIDENCE: all 146 `\runin` heads read sentence case; the two capitalized ones are proper nouns; the Title Case heads Q-053 quotes ("The Dangers of Corporate Doublespeak ...") are gone. No decision records a ruling, and QUESTIONS.md Q-053 is still open there (see P57) | FROM: D-117
- "No citation was checked against its source" | VERDICT: ALREADY LISTED | EVIDENCE: "809 of 820 bibliography entries are unchecked by a human" | FROM: D-117

## P53 — the cross-reference density pass, 2026-08-30 (D-118) (STATE.md line 4418)
CLASS: MIXED
SUMMARY: The author's "restate, then cut" route applied to cross-references (glossary out of scope): paragraphs carrying one dropped from 51 to 36 percent; chapter 3 from 147 to 53; chapter 1's roadmap kept on judgment; the finding that glossing a pointer is heavier than deleting it.
STILL TRUE AND NEEDED:
- "When a cross-reference needs explaining, check first whether it needs deleting." DUPLICATE in substance of `finishing/style.md` §7 ("Point only where the reader must go there ... Every other ... is cut or written as prose") and §7a (fate 4, "Cut").
- "625 of 806 are 'inline' ... No tool reaches that class; it needs the sentence rewritten": DUPLICATE of `finishing/README.md`, "Tools", `xref_shapes.py` row.
NOW FALSE: the counts (since D-658, D-660 and D-1018 the body runs on a different rule and far fewer references); "the four densest remaining chapters — 11 ..., 9 ..., 7 ..., 4" are August chapters.
OPEN ITEMS:
- Chapter 1's roadmap kept on a judgment "a reader is most likely to want reversed" (Q-054) | VERDICT: CLOSED | EVIDENCE: QUESTIONS.md Q-054, "Closed by execution, D-140 (P59), on default (a)"; the August roadmap chapter no longer exists (today's chapter 1 is "Twenty Seconds") | FROM: D-118
- The four densest chapters thinned, not driven to the average | VERDICT: CLOSED | EVIDENCE: superseded by D-658 (P221, body references 155 to 34) and D-660/D-1018 (`style.md` §7, §7a) | FROM: D-118
- "The 70 changed sections have not been read end to end since the pass" | VERDICT: ALREADY LISTED (subsumed) | EVIDENCE: those sections were rewritten in later restructures; the current form of the gap is the open-list item "no one has reread the book whole in its current order since the restructures of D-1068 and D-1116" | FROM: D-118

## P54 — four defects in the glossary and the sourcing, 2026-08-30 (D-119) (STATE.md line 4467)
CLASS: HISTORY
SUMMARY: Four author findings: "Floor" misalphabetized; *exit* and *molar/molecular* lacking glossary entries; the Gordon jury figure misstated (14% of items, not of contested cases; 18 moderators); a 30-word Dweck duplication resolved on the author's ruling. Found in passing: the glossary's running head printed chapter 12's (Q-055).
STILL TRUE AND NEEDED:
- "a successful build says nothing about whether the page is right": DUPLICATE of `finishing/pipeline.md`, "Things worth knowing", "Look at the proof".
NOW FALSE: "56 → 58 glossary entries" (the glossary was cut to 16 at D-158 and rebuilt since; *Exit* and *Molar/Molecular* entries no longer exist); "`refs.bib` notes 200 → 201 of 305"; "Section 5.1.1 untouched" and the Dweck passages (Dweck is no longer in the manuscript).
OPEN ITEMS:
- "The 70 sections P53 changed are still unread end to end" | VERDICT: ALREADY LISTED (subsumed) | EVIDENCE: see P53 | FROM: D-119
- "104 of 305 still have none [no annotation] — whether any of those is load-bearing the way the Gordon figure is has not been checked" | VERDICT: CLOSED | EVIDENCE: D-772 cut every note to what a reader needs and took verification out of entries; the human-check state is now `refs-ledger.tsv` (809 of 820 unchecked, already listed). The Gordon figure stands correct in `ch22/22_05.tex` | FROM: D-119
- "The other 121 glossary entries were checked for alphabetical order and not for content" | VERDICT: CLOSED | EVIDENCE: the glossary was cut from 57 entries to 16 at D-158 and rewritten since; the entries this concerned are gone | FROM: D-119
- Q-055, the glossary's running head reading "CHAPTER 12. CONCLUSION AND OUTLOOK" | VERDICT: CLOSED | EVIDENCE: D-140 (P59); `\backmattermark` in `manuscript/preamble.tex` line 461, called in `chZ/glossary.tex` line 4; QUESTIONS.md Q-055 "Closed by execution, D-140" | FROM: D-119

## P55 — the ordering constraint carried into the two closes, 2026-08-30 (D-128) (STATE.md line 4537)
CLASS: HISTORY
SUMMARY: The Replacement ordering (cheaper routes attempted first) added to the book's two closes, sections 3.8 and 12.3; two `\ref` calls restored at 12.3 with a note so a later density pass would not cut them again; "the fourth capacity" repaired after P53's cut left it pointing at the wrong rung; that class of lost anchor named as invisible to the suite.
STILL TRUE AND NEEDED:
- "A cut clause that was some distant sentence's only anchor leaves prose that still reads fluently ... invisible to the suite": DUPLICATE in substance of `finishing/style.md` §7a ("The lost-referent risk D-1000 recorded is answered by the naming, so every fate-2 and fate-4 sentence is read in the render as a reader meets it").
NOW FALSE: "D-118 is not reversed, and the reason is on the record so a later density pass does not cut them a second time": the site (section 12.3, the book's close) no longer exists in that form and D-660 replaced D-118's regime; "192 pages".
OPEN ITEMS:
- "Chapter 1's later safety-and-ethics paragraph still states the bearer as required without it [the ordering] ... named rather than repaired" | VERDICT: NOT RECHECKED | EVIDENCE: the item quotes no phrase; today's chapter 1 is "Twenty Seconds" and the Introduction is new (D-1100); a grep of `ch00/` and `ch01/` for "requires a bearer", "needs a bearer", "bearer is required" and "safety and ethics" finds nothing. The ordering itself now lives in `ch18/18_03.tex` ("It is not in the order of attempts ...") | RESTATED: An August note that the then chapter 1 stated a bearer as required without the condition that cheaper routes be attempted first. The paragraph appears to be gone, but with no quoted phrase that can't be confirmed | FROM: D-128
- "Q-037 is not reopened — D-111 ruled the plural arrangement stays research" | VERDICT: CLOSED (a ruling, not an open item) | EVIDENCE: D-111, "leave, carried as research" | FROM: D-128
- "One instance was found here by accident; no sweep for others was run, and P53 cut roughly 252 references" | VERDICT: NOT RECHECKED | EVIDENCE: no sweep is recorded; the prose P53 cut from was rewritten by the 2026-09-12 return and later restructures, and later cuts are governed by `style.md` §7a's read of every fate-2 and fate-4 sentence in the render. No phrase list exists to test | RESTATED: The August cross-reference cut may have removed clauses that were a distant sentence's only anchor; nobody swept for them. Most of that prose has since been rewritten, so the item likely has no remaining target | FROM: D-128

## P56 — the non-partitionability premise argued, 2026-08-30 (D-129) (STATE.md line 4604)
CLASS: HISTORY
SUMMARY: Section 3.7's premise that the refusing capacity can't be partitioned by topic given its argument (151 words): the capacity is general, and turning it on one's own post needs a self-model; the definitional half and the empirical half named; the falsifier stated as unverifiable in principle.
STILL TRUE AND NEEDED: none.
NOW FALSE: "The string `partition` appears nowhere else in the book" (it now appears only as "the auto-proceed partition", `chC/C.tex`, `ch22/22_08.tex`; the premise itself is gone); "section 3.7 at 2,000 → 2,152"; "192 pages".
OPEN ITEMS:
- "No chapter 11 entry for the empirical half — ... put to the author as a separate call, and it is unruled" (whether a system with the general capacity turns it on its own deployment, or is trained not to) | VERDICT: NOT RECHECKED | EVIDENCE: no decision rules on it (grep of DECISIONS.md for "empirical half" finds only D-129); the premise it qualified is gone from the manuscript (no "partition" in that sense; the corollary in section 3.7 was rewritten; exit is now `ch14/14_03.tex`); Appendix F's seven tests and open problems (`chF/F.tex`) carry no test of it by heading. Whether the question still bears on the current exit argument needs a reading of `ch14/14_03.tex` | RESTATED: In August the author was asked whether the research agenda should carry a test of whether a refusing system ever turns its refusal on its own deployment; he didn't rule. The premise has since left the book; if the current exit section (`ch14/14_03.tex`) still depends on that step, the question is open for Appendix F | FROM: D-129
- "Section 3.1's sibling non-separability claim ... left uncited" | VERDICT: CLOSED | EVIDENCE: "not separable from general competence" is no longer in the manuscript (grep) | FROM: D-129
- "The rest of chapter 3 was not re-read for other load-bearing premises without a stated limit" | VERDICT: NOT RECHECKED | EVIDENCE: August chapter 3 has been split and rewritten; no list of premises exists to test | RESTATED: Subsumed by the listed item that the book has not been reread whole in its current order | FROM: D-129

## P57 — the author's revision memo, seven items, 2026-08-31 (D-130 to D-136) (STATE.md line 4672)
CLASS: MIXED
SUMMARY: Seven memo items (D-130 to D-136): the memo's figures checked first, a cross-reference cut that fell short for structural reasons, `xref_shapes.tsv` found stale and regenerated, one question answered and one returned (decided at D-133, since confirmed). Lists what was not done: QUESTIONS.md's backlog, 139 unread ledger rows, 25 overfull boxes.
STILL TRUE AND NEEDED:
- "`finishing/reports/xref_shapes.tsv` was stale ... Nothing in `check_all.sh` looks at it. The other committed reports were not audited for the same problem." For `xref_shapes.tsv`: DUPLICATE of `finishing/README.md`, "Tools", `xref_shapes.py` row ("the committed report has now been found stale twice ... so regenerate it before reading it"). For the other reports: still true and stated nowhere. Every analysis report in `finishing/reports/` was last committed on 2026-09-19 or 2026-09-20 (list in the preamble above), before the restructures of D-1068 and D-1116. `finishing/README.md` says only "Generated, committed, small. Regenerate rather than hand-edit". UNIQUE. Proposed home: the `reports/` row of `finishing/README.md`, "What is where": "Most of these date from 2026-09-19/20 and describe a book since restructured; regenerate a report before reading it."
- "343 `section~\ref` calls ... That is the number to use from now on": superseded. `finishing/style.md` §7a now makes `render_markdown.py --check --chapters` the count ("The count is a report, not a gate"). Not needed.
NOW FALSE: "343 `section~\ref` calls in the body" as the standing measure; "`xref_shapes.py` classifies 360 of 463"; "139 ledger rows remain `drafted`" (now all 220); "25 overfull boxes" (the proof of 2026-11-23 has two).
OPEN ITEMS:
- The cross-reference cut short of half; "getting to half from here means rewriting claims ... it should be a decision rather than a by-product" | VERDICT: CLOSED | EVIDENCE: decided by D-658 (P221, body references 155 to 34) and D-660 ("Point only where the reader must go there", `style.md` §7) | FROM: D-133
- The other committed reports not audited for staleness | VERDICT: OPEN | EVIDENCE: last-commit dates as above; nothing since has regenerated them or marked them stale. Not in the STATE.md open list | RESTATED: The analysis reports in `finishing/reports/` (`xref_pairs.txt`, `xref_content.tsv`, `hedge_pairs.tsv`, `claims.tsv`, `section_stats.tsv`, `reader_tax.tsv` and the rest) were last generated on 2026-09-19/20 and describe the book before its restructures. Regenerate them, or say in `finishing/README.md` that they are stale | FROM: 2026-08-31
- "`QUESTIONS.md`'s filing backlog is untouched; ... its entries above and below the Resolved line are not reconciled" | VERDICT: OPEN | EVIDENCE: `finishing/QUESTIONS.md` last committed 2026-09-19 (`0e044bd4`); its header: "Current as of 2026-09-19, after D-461" and "Thirty-six of the thirty-eight open entries have still not been read against the current book". Entries never closed there although the tree or a decision settled them, e.g. Q-053 (run-in heads, now uniform) and Q-045 (August section 11.2). Q-035 and Q-042 (see P49 and P40) are unresolved there. `finishing/README.md` still describes it as "The open batch for the author". Not in the STATE.md open list | RESTATED: `finishing/QUESTIONS.md` has not been touched since 2026-09-19 and its open entries were never read against the restructured book, though `finishing/README.md` still presents it as the author's open batch. Either reconcile it against the tree (carrying anything still open into STATE.md's list) or retire it as a record and change the README row | FROM: 2026-08-31, 2026-09-19
- "139 ledger rows remain `drafted` and unread" | VERDICT: OPEN (changed form; low weight) | EVIDENCE: `finishing/ledger.tsv`: all 220 rows have status `drafted`; no row has ever been set to anything else. Not in the STATE.md open list | RESTATED: `ledger.tsv`'s status column says `drafted` for every section and has never been advanced, so it records nothing about what has been read or accepted. Either the column is retired in `finishing/README.md`'s description ("status, action, evidence, decisions. The work tracker") or someone starts maintaining it | FROM: 2026-08-31
- "The 25 overfull boxes in the build log were not investigated" | VERDICT: CLOSED | EVIDENCE: STATE.md lead: the proof of 2026-11-23 has two overfull boxes, both table cells in Appendix F, and those two are ALREADY LISTED ("Two overfull boxes (3.5pt, 9.1pt) in the table of `chF/F.tex`") | FROM: 2026-08-31
- The returned hygiene question, decided by the agent at D-133 | VERDICT: CLOSED | EVIDENCE: D-133 status "confirmed" | FROM: D-133

---

## Aside, outside these sections
`finishing/README.md`, "What is where", describes `STATE.md` as "Its lead paragraph is the current state, written fresh each pass; everything below it is the same paragraph from earlier passes, marked superseded and kept". Since D-1253 and D-1254 that is false: the lead is a status paragraph plus an open list, and superseded leads live in `finishing/STATE-superseded-leads.md` (`pipeline.md`, "STATE.md's lead").

