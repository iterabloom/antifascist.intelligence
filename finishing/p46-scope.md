# P46 — the open questions reviewed against the manuscript

**Author's instruction, 2026-08-29:** *"take a step back and analyze all of the
open questions up through Q-044, and in light of the latest manuscript, update or
resolve the questions as applicable."*

**Decision row:** D-110. **Branch:** `pass/46-questions-review`. **No manuscript
file is touched.**

## Method

Every figure the seventeen open entries turn on was re-measured against the tree
at D-109 rather than carried forward: word counts by chapter from
`section_stats.py`, `\ref{sec:` calls across the section files, `refs.bib`
entries against the manuscript's `\autocite` calls, entries carrying notes and
their word count, instances of "rather than" through `common.tex_prose_line`,
glossary locators, and leaf subsections under 230 words. Each entry then got a
dated re-check paragraph saying what moved and whether its default still holds.

## The figures, 2026-08-29 after D-109

93,911 words, 153 sections, 191 pages. 826 `\ref{sec:` calls, one per 114 words.
`refs.bib` at 326 entries, 23 uncited, 210 carrying notes totalling 8,695 words.
317 instances of "rather than". 124 glossary locators. Five leaf subsections
under 230 words.

## Closed

- **Q-028**, chapter 3's position — by execution at P38 on option (a). The
  instruction was answered in pages rather than in position, on two stated
  grounds, and Q-036 had independently reached (a) on the dependency.
- **Q-029**, the thin subsections — by execution at P38 on option (b). All eight
  of P29's were folded; the five that remain are pre-existing. The cost the entry
  warned of returned something: the renumber is what forced the reading that
  found Q-041's four pre-existing defects.

Both had been claimed as closed in the file's header since P38 and neither entry
said so. That is fixed, with records under "Resolved".

## Where a figure had reversed direction

- **Q-026.** The cross-reference count is **826, up from 758** — P39 through P45
  added 68 while adding 5,565 words. Density is unchanged at one per 114, which is
  why nothing flagged it: every pass added references at exactly the rate it added
  prose. "Stop here" held as a rate and failed as a count, and D-089's complaint
  was about the count.
- **Q-036.** Chapter 3 is **13,343 words, 14.21 percent, and the longest chapter in
  the book by 2,486 words.** Both of the entry's premises are gone: it is not third,
  and the two chapters it stood behind were cut at P38 while it grew. Option (a)
  still holds on its own reasoning; option (c)'s seam no longer divides the chapter
  evenly.
- **Q-032.** **210 entries carry notes, 8,695 words**, against 144 and roughly
  6,600. The growth is this session's verification notes, which are exactly the
  qualifying kind option (c) preserves — so (c) is strengthened and (b) weakened.
- **Q-043.** **Seven instances, not four**, across four passes. P41, P44 and P45
  each found one, and two of the three were contradictions the book carried in its
  central argument. That is a rate rather than a set of incidents, and it is the
  strongest case in the file for reading by subject.
- **Q-030.** 23 uncited of 326, from 14 of 297. None of the 29 entries added since
  is an orphan; the nine new ones came from prose cut around them at P36, P37 and
  P38. The mechanism the entry describes is confirmed.
- **Q-038.** 317, **down 23 while the book grew**, because cutting prose removes
  the constructions and reading does not. Confirms the entry's diagnosis.

## Where the entry stands and something moved under it

Q-027 (P38 executed option (c) and hit the same wall, which two passes have now
hit independently), Q-031 (the chapter 11 opener has grown 166 words for other
reasons), Q-034 (section 4.2's nine subsections are now more than half of chapter
4, and chapter 3 has nine sections of its own), Q-035 (chapter 5 was distilled
again at P38 without the measurement ever being run), Q-037 (P40's removal cases
are the plural arrangement's independence assumption failing in public law),
Q-039 (option (e) was executed at P38; option (d) sits in a chapter 2,000 words
larger), Q-040 (chapter 2's density figure is stale after P38; the reasoning does
not depend on it), Q-042 (six sites lean on the removal cases now, not four),
Q-044 (P45's compute floor is the one custody measure not defeated by the
assembly gap, because it is not in the artifact).

Q-033 was re-verified unchanged.

## New

**Q-045 — seven passes in one day added to two places nobody has read.** Chapter 3
went 11,341 → 13,343 and section 11.2 went 1,061 → 2,624, and no instruction was
about the length of either. Each pass was small and justified; the aggregate was
invisible from inside any of them. Nothing in the project's discipline sums a day:
`ledger.tsv` is per-section, `check_all.sh` has no size invariant, and Q-036 was
three passes stale when this review reached it. Four options, default (a).

## What was not done

- **No manuscript change.** Several re-checks name work — re-counting "rather
  than" in chapters 2, 3 and 4, re-measuring chapter 2's inventory density, reading
  chapter 3 and section 11.2 whole — and none was taken, because the instruction
  was to review the questions.
- **Q-019, Q-021 and Q-022 were not re-checked.** They carry closed banners from
  D-061 and are kept above the line by the file's own convention.
- **No default was changed.** Every one still applies; two entries now say why the
  default is weaker than it was (Q-026, Q-043).
