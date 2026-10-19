# P222: the spine and the notes

## What was asked

The author asked, on 2026-10-18, for a much faster read without loss of
substance: about 80 percent of the main text (the chapters, not the
appendices) moved into footnotes, leaving a main text of about 20,000 words,
with no substance deleted and only the grammatical tweaks a move requires.

## The author's rulings

1. **Page-bottom footnotes**, the apparatus the citations already use, through
   one macro (`\note{…}`) so the form could be switched later.
2. **Stays whole**, outside the 80 percent rule: the preface and chapter 34;
   each chapter's opening paragraph and each rule as the book states it; the
   opening scenes (the officer and Minab, Fishback, Hernández Romero, Thompson,
   the Challenger night), one paragraph each; tables, figures and boxed
   records.
3. **Rhythm:** Part by Part. The agent applies a whole Part, re-renders, and
   the author reads the render and names what comes back up.
4. **A branch**, merged to main when the whole book is done.
5. **A citation or a footnote inside a note is a footnote of its own**, in the
   chapter's single series, numbered in sequence after the note that carries
   it, typeset like every other footnote; this holds for every footnote.
6. **The HTML build is not a priority.** It may be broken by the nesting; the
   PDF is the proof and the Markdown render in `--keys` mode is the reading
   copy.

## The measure

From the render of 2026-10-18 built from `ad9effa1`, by
`render_markdown.py --check --keys --chapters` (headings, note markers and
citation keys left out): 103,320 main-text words before the appendices, 1,503
in the author's notes, 28,439 in the appendices. The target spine is about
20,700 words. The baselines are kept in `~/book-scratch/p222/`
(`baseline-keys_ad9effa1.md`, `baseline-chapters_ad9effa1.tsv`,
`render-truncate5_ad9effa1.md`).

Per chapter, main-text words at the baseline:

| ch | words | ch | words | ch | words | ch | words |
|---|---|---|---|---|---|---|---|
| Pref | 1,431 | 9 | 785 | 18 | 6,257 | 27 | 1,093 |
| 1 | 1,818 | 10 | 771 | 19 | 5,415 | 28 | 3,744 |
| 2 | 622 | 11 | 7,334 | 20 | 1,845 | 29 | 3,055 |
| 3 | 526 | 12 | 1,972 | 21 | 5,154 | 30 | 1,814 |
| 4 | 1,762 | 13 | 3,925 | 22 | 5,913 | 31 | 4,443 |
| 5 | 3,030 | 14 | 2,749 | 23 | 2,889 | 32 | 4,448 |
| 6 | 5,408 | 15 | 4,572 | 24 | 3,139 | 33 | 1,843 |
| 7 | 2,775 | 16 | 5,196 | 25 | 2,188 | 34 | 791 |
| 8 | 994 | 17 | 1,497 | 26 | 2,122 | | |

## The order of work

- **Setup, on main (D-906):** the `\note` macro, the render script, the two
  tools, the 31 existing footnotes as notes, the records; one commit; then the
  branch `p222-notes` in the worktree `~/antifascist.intelligence-p222`.
- **Seven rounds**, one per Part, in reading order: I (ch. 1–3), II (4–11),
  III (12–16), IV (17–25), V (26–29), VI (30), VII (31–34). Each round: the
  spine listing to `~/book-scratch/p222/partN-spine.md`; `demote.py` chapter
  by chapter with the hand splits before it; `refresh_order_shas.py`;
  `check_all.sh`; `--chapters` against the baseline; the `--keys` render for
  the author; a scratch PDF; `sentence_coverage.py` with zero missing; the
  spine read straight through; two commits on the branch; the Part's
  DECISIONS row and the STATE lead on main.
- **Close:** merge with `--no-ff`, the final records, "proofs please", the
  branch and worktree removed.

## The rule applied in the rounds

`finishing/style.md` §4d states it: what stays, what moves, the unit, the
hanging rule, the repairs allowed and the form in the source.

## Per Part

| Part | chapters | before | after | round closed | row |
|---|---|---|---|---|---|
| I | 1–3 | 2,966 | 1,527 | 2026-10-18 | D-907 |
| II | 4–11 | 22,859 | 9,874 | 2026-10-18 | D-908 |
| III | 12–16 | 18,414 | 7,911 | applied 2026-10-18; merged unread 2026-10-19 (D-914) | D-909 |
| IV | 17–25 | 33,937 | 17,080 | applied 2026-10-19; merged unread 2026-10-19 (D-914) | D-910 |
| V | 26–29 | 10,014 | 5,947 | applied 2026-10-19; merged unread 2026-10-19 (D-914) | D-911 |
| VI | 30 | 1,814 | 1,580 | applied 2026-10-19; merged unread 2026-10-19 (D-914) | D-912 |
| VII | 31–34 | 11,525 | 7,418 | applied 2026-10-19; merged unread 2026-10-19 (D-914) | D-913 |
| preface | | 1,431 | 1,431 | untouched by ruling | |
| whole | | 103,320 | 52,768 | | |

The whole-book line is the render's "main text before appendices" at the
branch's `6e3a5a99`, and at the merge `f10bc393` on main: 51 percent of the
baseline, against the 20 percent asked. The rulings set the floor: the preface and chapter 34 whole (2,222
words), every chapter's opening paragraph, every rule and definition as the
book states it, the five scenes, the fifteen tables, the three figures and
the two boxed records. The Parts that are mostly rules (V, VI, VII) sit
near three fifths; the Parts that are mostly argument and evidence (I to
IV) sit near half, held there by the openings and the rules.

## What this pass has not done

As of D-914 the pass is merged to main and the proofs are rebuilt, on the
author's instruction, with Parts III to VII unread by him; Parts I and II
were closed on his reading. A reversal from here is a note moved back into
the body on main, with the coverage check run again. Not done: the author's
reading of Parts III to VII, with whatever comes back up; a reading of the
notes as prose on the page, beyond the coverage diff and the spine reads.
The HTML build under nested notes was tried at the close and built without
error (D-914); nobody has read it as a page. The trial on chapter 8 at D-906 was reverted before the commit;
chapter 8 moved with Part II.
