# P173 — the record written, ten passes late

Author instruction, in answer to whether the session was ready for a
compaction: write the record first.

**The gap this closes.** P163 through P172 ran in one session and left
`STATE.md` reading as of P162, `DECISIONS.md` stopping at D-262, no scope files,
and `QUESTIONS.md` unread. Ten passes of argument existed only in commit
messages — written unusually full for that reason — and in a context about to be
summarized.

## What was written

Ten scope files, `p163` through `p172`. Eleven decision rows, D-263 through
D-273, the last being **not a pass**: it records that standing rule 1 was
suspended for the session, what was authored under it, and that `PLAN.md` was
deliberately left stating the rule, so the default survives the session.

**`STATE.md`'s new lead opens on the red suite**, because that is the thing a
fresh session would get wrong. `check_all.sh` fails, 28 of the 30 violations are
the author's own inline notes, and the obvious repair — stripping them — would
destroy editorial work that exists nowhere else.

## What checking the record found

**The chapter~3 trigger had fired and nobody had noticed.** Q-075, Q-076 and
Q-088 were set to fire at the close of the next pass touching chapter~3, and
seven chapter~3 files were touched this session. **All three were checked against
the manuscript before anything was applied, and all three have premises that no
longer hold.**

**Q-075's default would now damage the book.** It asks for a sentence naming the
fork and its four branches on the finding that `branch` survived 22 times.
**It survives twice, both unrelated**, and `fork` six times, all ordinary
computational sense. **The counts were already 2 and 6 at `4065f15`** — this
session did not cause it, and an earlier pass removed the vocabulary without
closing the question. Applying the default would reintroduce a figure the book
does not use.

**Q-076's two items are both gone**, §3.2 having been restructured at `373d894`.

**Q-088's default is a safe no-op, and its reasoning lost a leg.** It cites
§11.3:13 for the who-prices-the-dissent test, and D-264 cut §11.3 whole. **A grep
across all 132 sections finds the test nowhere.** That is **Q-115**, new: the
sharpest one-sentence form of a distinction the book uses in three chapters left
with the section, and the default proposed is to restore it to §2.1.2 attached to
feature~1, where D-266 has already made tempo definitional.

**A second lapse, older than this session.** `ledger.tsv`'s decisions column
stops at D-258, so P159 onward have added nothing to it. Recorded rather than
repaired: attributing eleven decisions to sections accurately is its own pass,
and half-doing it is worse than saying it is undone.

## What this pass did not do

No manuscript file was touched. No question was closed — Q-076 is recommended
for closure as overtaken and left open, because closing it is the author's. No
default was applied. `PLAN.md`'s header figures are refreshed and its standing
rules are unedited.

## Figures

132 sections, **0 changed**. 100,363 words, 198 pages, 245 cross-references, 329
bibliography entries — all unchanged, this pass being record only. Suite red on
typography, at the same 30 violations, 28 of them the author's notes.
