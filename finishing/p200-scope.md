# P200 — §2.2.1 moved into chapter 6, revised, and the two chapters renumbered around it

The author supplied the revision as a marked-up block: the section to move, where
to put it, what the new numbering is, and a stub paragraph to leave behind.
**Executed as specified.** The book is **91 sections, 74,789 words and 157 pages**,
suite green, 0 undefined references and 0 undefined citations.

## What moved

*What Emotion Is, and What a System Reads*, §2.2.1, becomes **§6.1, *The Standard
Face Is a File***, the first numbered section of chapter~6. It sits immediately
after the data-centre energy esbox and the *arrangement is visible in the
accounting* paragraph that follows it, and immediately before what was *Who
Supplies the System's Values* — the placement the instruction named, verified on
the rasterized page.

**The revision reorders it.** The deployed case comes first and the scientific
dispute second, which reverses the order it carried in chapter~2. The
Ekman/Barrett material goes from four paragraphs to three. **All eight citations
are retained** — `taigman2014deepface`, `buolamwini2018gender`,
`deleuze1987plateaus`, `ekman1969pancultural`, `panksepp1998affective`,
`lindquist2012brain`, `gendron2014perceptions`, `crivelli2016fear` — checked as a
set against the old file before the move, because a dropped key would have left an
uncited entry in `refs.bib` and nothing in the suite tests for that.

## Three corrections to the supplied text

**The label.** The block carried `\label{sec:2.2.1}` on a section becoming §6.1.
Left alone it would have failed `check_structure.py`, which requires the label's
number to match the filename's, and it would have reproduced exactly the
divergence D-296 was opened to close. It is `\label{sec:6.1}`.

**One cross-reference was a number behind.** The block read `section~\ref{sec:11.7}`
for *the open question about the instrument*. **D-296 moved that section to
§11.8** earlier today, and the file in the tree already said `sec:11.8`. Kept at
`sec:11.8`, which is *What Does a Face-Reading System Measure?* — verified against
the label, not just the number.

**Typography.** Seven ASCII em dashes and one TeX quote pair, converted to the
characters per `style.md` §8. The quotation now prints `“Racism operates by the
determination…never abides alterity”` with the right marks and
`(Deleuze and Guattari 1987, p. 178)` after it.

## The renumbering

Eight numbers moved and `renumber-map_2026-09-13b.tsv` records them. **This is the
second renumber map of the day**; `renumber-map_2026-09-13.tsv` is D-296's, in
chapter~11.

| old | new | |
|---|---|---|
| 2.2.1 | **6.1** | the moved section, retitled |
| 2.2.2 | 2.2.1 | Self-awareness and Self-regulation in AI Systems |
| 2.2.3 | 2.2.2 | Is Affect Necessary for Moral Concern? |
| 6.1 | 6.2 | Who Supplies the System's Values |
| 6.2 | 6.3 | Who Is Allowed to Look |
| 6.3 | 6.4 | Same Robot, Worse Boss |
| 6.3.1 | 6.4.1 | Twenty Seconds |
| 6.3.2 | 6.4.2 | Custody and State Compulsion |

**Nine cross-references were remapped, in one simultaneous pass** so that `6.3`
could become `6.4` while `6.2` became `6.3` without either overtaking the other,
and matched on the full brace so `sec:6.3` never matched inside `sec:6.3.1`. They
sit in `02_01_02.tex`, `03_06.tex`, `06.tex`, `07_04.tex`, `13.tex` (five of the
nine) — and **nothing at all pointed at the moved section**, which is why the move
cost no repointing beyond the stub.

Files were renamed with `git mv` in reverse order so no name collided. **The
ledger row travelled with the section** rather than being deleted and recreated,
so §6.1 keeps the decision history the section accumulated as §2.2.1.

## The stub

Inserted in §2.2 after *Only the fourth is relevant to genuine caring…stays open*
and before `\runin{Performance, competence, and agency}`, as specified. It keeps
the first capacity a live category for the table above it and points at §6.1.
**Its reference was changed from the supplied `sec:2.2.1` to `sec:6.1`** for the
same reason as the label.

## Verified

**All 91 labels print the number their name says**, read out of `book.aux` where
LaTeX records each resolved value: **0 divergences.** That is the check D-296
introduced and the one this kind of edit exists to break.

`check_all.sh` green at 91 sections, contents regenerated and matching the printed
contents for both chapters, `sections.tex` regenerated at 91 inputs, ORDER digests
refreshed, **157 pages** with 0 undefined references and 0 undefined citations, 258
cross-references resolving against 91 labels. The new section's opening page was
rasterized and read.

**Chapter~2 is 10 sections and 13,490 words; chapter~6 is 7 sections and 5,412.**
The book gains 123 words net — the stub, plus the new opening paragraph, less the
Ekman/Barrett compression — and one page.

## One thing to look at, not changed

**A 23-word clause is now stated twice, on facing pages.** Chapter~6's opener
defines Benjamin's four categories and says of coded exposure: *the
face-recognition case, where the fix for a system that fails on dark skin is a
system that identifies dark-skinned faces reliably for whoever is looking.* §6.1's
first paragraph says: *The worked case is the one named above: face recognition,
where the fix for a system that fails on dark skin is a system that identifies
dark-skinned faces reliably for whoever is looking.* **The second half is
identical word for word**, and the two land on printed pages 59 and 60.

*The one named above* already does the pointing, so the restatement is the part
that could go. It is `style.md` §2's shape and D-013's one-home rule, at a
distance short enough that a reader will feel it. **Nothing was changed**: this is
the author's own prose, and the pickup may be deliberate.
