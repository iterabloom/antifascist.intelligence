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
| D-006 | 2026-08-22 | Title conflict at 3.1.2.3.1.11 | The manuscript's own heading wins over the spreadsheet: "Applications and Examples". `outline.tsv` keeps the spreadsheet's string until the author rules; `check_structure.py` reports the difference as a note, not an error. | provisional — see Q-006 |

Open items live in `QUESTIONS.md` and move here when answered.
