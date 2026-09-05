# P99 — the author's second Overleaf pass over chapter 3, imported

**The instruction.** *I'd like to do some manual editing in overleaf.* Then, on the
returned package: *my updates are here.* Then, on the findings below: *let's defer all
those rulings and make the proofs.*

This is P94's shape one week on — an author edit made by hand in Overleaf and brought
back through `finishing/tools/overleaf.py` — and it is numbered as a pass for the same
reason P94 was: the manuscript changed, and what changed needs a record.

## The round trip

Exported at `22a57b2`, 144 files, 0.4 MB. The package went to the author over
`~/upload-tool/upload.sh` and came back the same way, encrypted, on the author's ask
each time. Both legs were verified by SHA-256 against `.upload-secrets`, and the
author decrypted the return leg themselves so the passphrase stayed out of the session.

**The returned zip was doubly wrapped and the first dry run refused it.** The outer
zip held exactly one file, an inner `___1_.zip`, and carried no
`overleaf-manifest.json`; `overleaf.py` stopped rather than guess, which is the
manifest check doing its job. The inner zip is the package as exported, 144 files,
manifest intact. **Unwrap before importing, and dry-run the inner zip.**

**What the import reported.** 6 to apply, 135 unchanged, 1 skipped (`sections.tex`,
regenerated), **0 conflicts, 0 problems**. The manifest recorded the export at
2026-09-03T22:51:26Z from `22a57b29d5a6`, and the tree was still on that commit with
nothing staged, so the manifest's Overleaf-versus-repository test had nothing to
separate — the same condition as P94, and it means the test was not exercised.

## What came back

Six files, all chapter 3: `03.tex`, `03_01.tex`, `03_02.tex`, `03_03.tex`, `03_04.tex`,
`03_05.tex`.

**§3.5 is retitled**, *What Can Be Switched Off Cannot Hold a Line* → *If You Can Be
Switched Off, Can You Hold the Line?*, and the import synced it into `ORDER.tsv`,
`outline.tsv`, `ledger.tsv` and the TOC. Label and number unmoved. `03_05.tex` has no
other change: the title is the whole of the edit to that file.

**The substantive edits, by file.** §3 rehedges its own claims (*I am taking that trade*
→ *I am inclined to take*) and drops the chapter's falsifiability offer. §3.1 rewrites
the *Slaughter* and *Cook* paragraphs D-190 built, ending the third way's failure on an
ironic refrain, and **cuts its entire closing bridge into §3.2**. §3.2 moves the
operational-refusal paragraph up under its run-in, where it now follows the head that
introduces it, and compresses four passages. §3.3 compresses six passages and gains two
working notes. §3.4 restates the ordering of its two questions and loosens the
self-model sentence.

## What was repaired, neither of it the author's text

**Two straight double quotes in §3.2**, around Chalmers' hard problem and around
*simply*. Overleaf's editor does not set smart quotes, so they came back straight and
`check_typography.py` failed on both. **Straight apostrophes were left alone**: every
file in the chapter already uses them, the checker tests doubles only, and `Chalmers'`
is what the convention asks for.

**Twelve `\textit` converted to `\emph`**, in §3, §3.1, §3.2 and §3.3. This is
**D-189's class one pass later, and it recurred for the reason D-189 gave**: `style.md`
has no rule on emphasis, so the book's practice is uniform and unwritten and nothing
flags a departure. The manuscript carried zero `\textit` and 55 `\emph` before this
import; all twelve arrived with the edits. `\textit` is now zero and `\emph` 67.
**Applied on P94's ruling rather than a fresh one**, the situation being identical.

**Four `ORDER.tsv` digests refreshed.** Both repairs staled digests the import had just
refreshed — D-189's finding exactly, that any edit after an import re-stales them —
and `check_all.sh` caught it.

## Numbers

**91,501 → 91,199 words, −302**; chapter 3 at 18,777. **184 pages, unchanged; 0
undefined references; 138 sections.** 20 overfull boxes, **with no count taken before
the pass**, so nothing is claimed about whether that number moved. `check_all.sh` green
at both commits, run by the pre-commit hook. Two commits, `949dffa` and `1a67809`, and
the proof pair rebuilt at 2026-09-04 with the 2026-09-03 pair removed, the date having
rolled over in local time.

## What ships unruled

**The author deferred every ruling below and asked for the proofs.** All of it is in
the 2026-09-04 pair. Four are entered as Q-077 through Q-080; the rest are here.

**Two working notes are now in §3.3 and both print.** §3.3:19 appends a parenthetical
about pytorch, CUDA and cublas determinism settings, ending *iirc*; **its claim was not
verified here**. §3.3:55 carries an all-capital objection to the sentence it sits
inside. **Neither was removed, and the reason is Q-069 and Q-070**: working notes of
this kind are in the manuscript by the author's choice and print in the proofs. What is
new is the markup — the `\textbf` at §3.3:55 opens 24 words before the note, so a clause
of the book's own argument prints in bold beside it. Q-077.

**A verb that no longer takes its prepositions**, §3:15: *it specifies the antifascist
question from the matter of what a system values into…*. The cut verb was *converts*,
which takes from/into. Q-078.

**Three register departures, all first instances.** The first authorial *we* in the
book, twice in §3.2; the only *e.g.* in body prose, in §3.4; and the book's first
second-person section title, §3.5. Q-079 groups them. On the substance §3.5's new title
is arguably a repair — the old one asserted what the section's own opening qualifies,
*The halt is always available* — and the entry says so.

**Four cut sentences.** §3.1's closing bridge is Q-080, being structural: the section
now ends on its hybrids sentence with no transition into §3.2 and no statement that the
chapter inclines toward the bearer. The other three are recorded here and not entered —
§3's *What would falsify the inference is on the page, and I would rather someone found
it*; §3.2's *That disagreement gets settled by building something, and not by argument
about what mattering is*; §3.3's *A field that has not attempted something and does not
have it has produced no evidence that the thing is unavailable*. Each is a sentence the
author cut in their own prose, and none leaves a dangling reference.

## Left undone, named

- **The six sections were not read end to end.** What was read is the diff, closely, plus
  §3.5's opening and §3.1's new ending in context. A seam outside the changed lines would
  not have been seen.
- **No sweep for knock-on effects of the §3.5 retitle or the cut bridge.** Chapters 4 to
  14 were not checked for text that leans on either. Four sections cite §3.5 by
  cross-reference; whether any paraphrases the old title was not checked.
- **The determinism claim at §3.3:19 was not verified**, and no source was consulted for
  it.
- **`\textbf` is otherwise unused in the prose.** The only other instance in the
  manuscript is `ch02/02_02.tex`'s table header. Nothing was done about that asymmetry.
- **The overfull-box count has no baseline**, for the second pass running.
- **This write-up records what the author deferred; it does not pre-judge any of it.**
