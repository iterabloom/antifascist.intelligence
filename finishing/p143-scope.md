# P143 — §11.3 states the limit it was built on top of

Q-101, closed on option (b) by the author's ruling rather than on its default.

## What was wrong

§11.3 makes longitudinal access the first thing a detector would need, on the
ground that every one of the four features is *defined by a change over time*,
and concludes *the slope rather than the level is the instrument*. **A party that
declares the decoupling outright has no slope.** §11.3 never said so — zero
occurrences of *declare*, *announce*, *myth*, *outright*, *overt* or *avow* in
1,714 words — so the section that exists to say what a detector would have to
detect did not say what this one cannot.

**P142 is why the default stopped being right.** P133 had patched this with a
forward pointer from §2.1.2, and P142 removed it on the reader test, correctly:
it sent a reader nine chapters ahead from inside a definition. That left nothing
in the book connecting the limit to the section inheriting it.

## The edit

One sentence, at the end of the paragraph that makes the slope argument:

> An institution that announces its decoupling has no slope to measure, and a
> detector built this way would not see it.

**No cross-reference and no apparatus**, as ruled. The count stays at 231.

**The contrast is carried by the paragraph, not by the sentence.** Three clauses
earlier the same paragraph names *a model drifting from what it tracks*, so
*announces* does the work without an *instead of drifting* construction —
`antithesis.py`'s shape, and one this section does not need.

**The wording does not echo §2.1.2's.** That site says *an instrument tuned to
drift will not register a party that announces it*; this one says an institution
announcing has no slope and a detector built this way would not see it. **0
shared runs at six words or more**, which matters because these are now the
book's two statements of one limit and Q-104 is the record of what happens when
two such statements are written the same way.

## Where the limit now sits

`02_01_02.tex:14` states it inside the definition of the fourth feature, for a
reader learning what the feature is. `11_03.tex:11` states it inside the detector
specification, for a reader working out what could be built. **Neither points at
the other and neither needs to.**

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
the sentence read back out of `pdftotext` in position.

## Figures

133 sections, **1 changed**. 99,318 → **99,339** words (+21); §11.3 1,714 →
1,735. **196 pages unchanged.** 231 cross-references unchanged. 324 bibliography
entries unchanged. 0 `\textit`. **The proof pair was not rebuilt and is now
eleven passes stale.**
