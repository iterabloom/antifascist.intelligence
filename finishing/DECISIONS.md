# Decisions

Append-only. A reversal is a new dated line referencing the superseded ID, never
an edit to the old row. Cite IDs from `ledger.tsv`, commit bodies, and `PLAN.md`.

Status: `confirmed` (author said so) · `provisional` (author's first answer, may
change) · `default-applied` (unanswered by its deadline; reversible) ·
`superseded-by:D-NNN`.

| ID | Date | Topic | Decision | Status |
|---|---|---|---|---|
| D-000 | 2026-08-22 | Planning scope | Planning produces documents, read-only tools and reports, a byte-identical split of the manuscript, and one pilot section. No other content edits during planning. | confirmed |
| D-001 | 2026-08-22 | Who writes the prose | Agent drafts each section from a brief; author reads and Accepts or returns with notes; at most two rounds, then the author hand-edits. | confirmed |
| D-002 | 2026-08-22 | Target form (D0) | A book for serious general readers, ~75–90k words, single-author voice, endnotes for named studies/statutes/systems, PDF/EPUB/POD under the existing CC BY-NC-ND. Chapters may be released as they are accepted. | provisional |
| D-003 | 2026-08-22 | Author availability | Under 2 hours per week. This is the binding constraint: author time goes to decisions and acceptance reads only; everything else is agent work or default-applies. | confirmed |
| D-004 | 2026-08-22 | Working representation | The manuscript is edited as one file per section under `manuscript/sections/`, keeping the existing dialect; `parseable_text_v4.txt` is the join. v3b stays frozen in place. | confirmed (implied by D-000; recorded for reference) |
| D-005 | 2026-08-22 | Section-file naming | Zero-padded, `_`-separated numbers so byte-order sorting reproduces book order. | confirmed |
| D-006 | 2026-08-22 | Title conflict at 3.1.2.3.1.11 | The manuscript's own heading wins: "Applications and Examples". `outline.tsv` corrected to match. | confirmed (Q-006 a) |
| D-007 | 2026-08-22 | Revise or rewrite (Q-001) | **Revise only.** Fix the voice, cut duplication, add sources; leave the substance. The triage still runs, but its fates are drawn from Keep / Revise / Merge / Cut — "Rewrite from nothing" is off the table except where a section has no body text at all. | confirmed (Q-001 c) |
| D-008 | 2026-08-22 | Voice and method note (Q-002) | Single author: "I" where the author speaks, "we" only reader-inclusive; "report" → "book" throughout. A ~500-word "On method" note names the device (models prompted to write as simulated expert co-authors), names no persons, and points to this repository as the record. | confirmed (Q-002 a) |
| D-009 | 2026-08-22 | Citations (Q-003) | Endnotes for named studies, statutes, systems, and quotations only. The agent writes `[[cite:ID]]` placeholders and never authors a reference entry. Anything unverifiable is cut during the revise pass, not carried forward with a TODO. | confirmed (Q-003 a) |
| D-010 | 2026-08-22 | Structure and cuts (Q-004) | Reader-facing outline capped at three levels (~90 sections). Cut §6.4.1.1–.9, keep the principles sections. Fold Chapter 8 into Chapter 7 as a single geopolitics section. | confirmed (Q-004 a) |
| D-011 | 2026-08-22 | Authoritative text (Q-005) | The manuscript's own headings are authoritative. `manuscript/table-of-contents.txt` becomes regenerated output (`headings.py --write-toc`). The `AGENTS.md` "Authoritative text" line is amended to point at `manuscript/sections/` plus the join. **Author gave explicit approval for the AGENTS.md edit.** | confirmed (Q-005 a) |
| D-012 | 2026-08-22 | Epigraphs (Q-007) | **Keep all three** (Run the Jewels, Lady Gaga / Bradley Cooper, Westworld). A permissions task is opened and tracked in `PLAN.md`; the rights exposure is the author's accepted risk, recorded here rather than re-argued. | confirmed (Q-007 b) |
| D-013 | 2026-08-22 | The two repeated arguments (Q-008) | Each cluster gets one home, decided during triage; the other instances are cut or reduced to a cross-reference. Under D-007 the surviving instance is the best existing text, edited — not new prose. | confirmed (Q-008 a) |
| D-014 | 2026-08-22 | The quarry (Q-009) | The original transplant plan stands: roughly 12,000 words from `cognition/` may enter the book. **This is the single exception to D-007** — the one place new material is allowed. Everything else remains a revise. | confirmed (Q-009 c) |
| D-017 | 2026-08-23 | How strictly to read the named-persons rule | **Not strictly.** The rule exists to keep the persona device out of the book: text a model produced while pretending to be a named person must never appear as though that person said or did it. It is **not** a bar on ordinary scholarly citation. Naming the researchers behind a published finding, quoting a published claim with a citation, and describing a documented laboratory event are all allowed, in the book and in `finishing/`. `names_guard.py` now tests for the persona-device shape rather than for the presence of a name. | confirmed |
| D-016 | 2026-08-22 | T7, the case against empathy (Q-010) | **Taken unframed.** The empathic-concern/personal-distress dissociation and the spotlight bias go in at full strength; chapter 2's thesis absorbs the hit rather than being cushioned by the compassion half. 700 words into §2.2.3. Carries a coherence obligation — see `transplants.md` §T7. | confirmed (Q-010 b) |
| D-015 | 2026-08-22 | Chapter 9 triage | 9.1 and 9.2 get openers (fill, not cut); 9.2.3 merges and is not the home of the emotional-intelligence argument; the other nine sections revise. | confirmed |

Open items live in `QUESTIONS.md` and move here when answered.
