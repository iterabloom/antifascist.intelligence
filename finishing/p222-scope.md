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
| I | 1–3 | 2,966 | | | |
| II | 4–11 | 22,859 | | | |
| III | 12–16 | 18,414 | | | |
| IV | 17–25 | 33,937 | | | |
| V | 26–29 | 10,014 | | | |
| VI | 30 | 1,814 | | | |
| VII | 31–34 | 11,525 | | | |

## What this pass has not done

At D-906 no chapter has moved. The trial on chapter 8, run on main to prove
the chain (the tool, the suite, the render, the count, the coverage check and
a whole-book build), was reverted before the commit; chapter 8 moves with
Part II on the branch.
