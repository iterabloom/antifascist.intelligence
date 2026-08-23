# Open questions for the author

**Session digest — 2026-08-22**

- Created `finishing/` and split the manuscript into 282 per-section files under `manuscript/sections/`. The join is **byte-identical** to the frozen v3b (`cmp` clean). Tags `v3b-import`, `v4-split`.
- Guardrails live and green: round-trip, structure, named-persons, commit-message dry-run — all under `finishing/tools/check_all.sh`.
- Measured: 115,377 body words; 11 headings with no body text; manuscript and the v3b spreadsheet agree on all 282 numbers with one title conflict (Q-006).
- **Citation debt: 268 items in 91 sections.** Mostly named bodies, laws and systems. The book contains 3 percent-signs and 9 hedged-evidence phrases in 115k words — it asserts very little that is checkable, which is its own problem.
- **585 unmarked list items in 102 sections**, chapters 2–10 (not 4–8 as I previously assumed); chapter 3 has the most.
- **Redundancy: nothing is copy-pasted, but two arguments are each written 6–9 times.** See `reports/redundancy.md` and Q-008 below. §2.4 and §7.4 are one treatment written twice; their informed-consent pair is the single highest-scoring section pair in the book.
- `ledger.tsv` now carries evidence links for 190 of 282 sections.
- **Nothing needs an answer to keep going.** The batch below shapes the next assessments; every item has a default that applies on its own if you say nothing.

---

How to answer: reply in chat with just the IDs, e.g. **"Q-001 a, Q-003 b, rest defaults"**. Or edit this file on the phone. Answers move to `DECISIONS.md` with a date.

**Deadline convention:** unanswered items take their default when Phase 3 (Adjudicate) opens — that is, after the assessment reports are built. A default-applied decision is still reversible; it just stops the work from stalling.

---

### Q-001 — Revise or rewrite? (D1)
The body prose has not been rewritten since 2023: fewer than 90 lines changed across three versions, all heading moves. 54% of sections sit in the 400–599 word band — one prompt per section, then nothing.
- **(a) Default — decide from evidence.** Triage all 282 sections into Keep / Revise / Rewrite / Merge / Cut; if more than 40% of words land in Rewrite/Merge/Cut, the plan calls itself a rewrite and is budgeted as one.
- (b) Declare it a rewrite now and skip the triage argument.
- (c) Declare it a revise-only pass: fix voice, cut duplication, add sources, leave the substance.

### Q-002 — Voice, and whether the book admits how it was made (D2/D3)
The text says "this report" six times and never "book"; institutional "we" appears 258 times, but no named person had any connection to the project.
- **(a) Default.** Single author: "I" where you speak, "we" only reader-inclusive; "report" → "book"; plus a ~500-word "On method" note that names the device (models prompted to write as simulated expert co-authors) and names no persons, pointing to this repository as the record.
- (b) Same voice change, no method note — just the colophon line the README already has.
- (c) Keep the committee "we".

### Q-003 — Citations (D4)
There are none: no bibliography, no footnotes, ~40 named laws and bodies unsourced, and a handful of claims that are wrong as written. Your own `(FAKE)` audit in `generation/prompt-fragments/` shows model-produced references cannot be trusted.
- **(a) Default.** Endnotes for named studies, statutes, systems, and quotations only. The agent writes `[[cite:ID]]` placeholders and never authors a reference entry; anything unverifiable is cut during rewrite, not carried forward. Verification runs in a separate networked session, and you spot-check a sample.
- (b) Same, but you verify everything yourself.
- (c) Trade style: no notes, a "further reading" list per chapter.

### Q-004 — What to cut (D5/D7)
The outline reaches six levels deep (`3.1.2.3.1.11.1`); eight of fourteen 2023 reviews asked for a cap at four and it was never applied. §6.4.1's nine country subsections and all of Chapter 8 are a 2021–22 snapshot; Chapter 8 is also the second-thinnest chapter.
- **(a) Default.** Cap the reader-facing outline at three levels (~90 sections); cut §6.4.1.1–.9, keep the principles sections; fold Chapter 8 into Chapter 7 as one geopolitics section. Removes roughly 8–10k words.
- (b) Cap the depth but keep the country surveys, updated.
- (c) Keep the structure; cut only duplication.

### Q-005 — `manuscript/table-of-contents.txt` (D11)
It has 293 entries and records the *pre-restructure* state; the manuscript and the v3b spreadsheet agree on 282. `AGENTS.md` currently names this file as authoritative, so changing its role needs your approval.
- **(a) Default.** The manuscript's own headings are authoritative. `table-of-contents.txt` becomes regenerated output (`headings.py --write-toc`), and the `AGENTS.md` "Authoritative text" line is amended to point at `manuscript/sections/` plus the join. **Needs your explicit approval before the amendment is committed.**
- (b) Freeze `table-of-contents.txt` as a historical artifact and point `AGENTS.md` at `finishing/outline.tsv` instead.
- (c) Leave it alone for now.

### Q-006 — One conflicting title (D-006)
Section `3.1.2.3.1.11`: the manuscript says **"Applications and Examples"**, the spreadsheet says **"Integrating Cognitive and Emotional Processes in AI Systems"**. The section's own body is a run of worked examples, and its three children are "Frameworks for Integration", "Challenges in Integration", "Examples of Integrated AI Systems".
- **(a) Default.** Manuscript wins; `outline.tsv` is corrected to match. (This subtree is a strong candidate for restructuring later anyway — its parent `3.1.2.3` and child `3.1.2.3.1` currently carry the *same* title.)
- (b) Spreadsheet wins; the manuscript heading is changed.

### Q-007 — Epigraphs (D9)
Three: Run the Jewels lyrics (Chapter 1), Lady Gaga / Bradley Cooper lyrics (§2.2), Westworld dialogue (§2.4). All third-party copyright; lyrics are licensed aggressively and a CC BY-NC-ND license on your side does not cover them. Eight of fourteen 2023 reviews independently asked for the first one to go.
- **(a) Default.** Drop all three. The opening paragraph already carries the same idea in your own words.
- (b) Keep them and open a licensing task, with a date after which they are dropped.
- (c) Keep the Westworld dialogue only (the most defensible), drop the lyrics.

### Q-008 — Where do the two repeated arguments live? (new; from the redundancy analysis)
Nothing in the book is copy-pasted, but two arguments are each made six to nine times in different words, in different chapters:

**Cluster A — "promote democratic values through international cooperation":** §5.4.3, §7.2.5.3, §4.6.3.1.2, §10.1.3, §8.2.1, §8.2.3, §8.3.1, §6.4.1.12, §10.3.2.1. The pair §5.4.3 ↔ §7.2.5.3 scores 0.950, second-highest in the book. Every one of §5.4.3's thirteen high-similarity partners is in another chapter — it has no relatives at home.

**Cluster B — "emotional intelligence and affective computing":** §2.3.1, §2.3.2, §4.2.2, §4.2.2.1, §3.1.2.3.1.10, §9.2.3. Note §2.3.1 is a **47-word stub** that nevertheless has ten cross-chapter twins: the material that belongs there was written three times elsewhere.

- **(a) Default — decide in triage.** Each cluster gets one home during Phase 3, and the other instances are cut or reduced to a cross-reference. I propose the argument, you rule.
- (b) Tell me the homes now, if you already know where each belongs.
- (c) Treat the repetition as deliberate reinforcement and leave it.
