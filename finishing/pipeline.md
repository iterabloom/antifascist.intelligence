# Build pipeline

The book is LaTeX. Verified end to end on this machine, 2026-08-25: **193-page
PDF from `manuscript/book.tex`, lualatex + biber, no undefined references.**

## What is available here

TeX Live 2026 installed under `$HOME/texlive/2026` — user-space, because there
is no root on this machine and `apt` was therefore not an option. `lualatex`,
`biber` 2.22, `scheme-medium` plus `collection-latexextra`. Also `libreoffice`
24.2.7 headless, `gs`, `pdfinfo`/`pdftotext`, python 3.12, node 20.

`~/texlive/2026/bin/x86_64-linux` is **not** on the default PATH. `build_tex.sh`
adds it; set `TEXLIVE_BIN` to override.

## The command

```sh
finishing/tools/build_tex.sh [OUTDIR]      # default $TMPDIR/es-build
```

It runs lualatex → biber → lualatex twice, from `manuscript/book.tex`, with
`-output-directory` so no aux files land in the source tree. Two runs after
biber: the first resolves citations, the second the TOC and any page references
that moved because of them.

Build products go to the scratchpad, with one standing exception: the
whole-book proof is committed as
`finishing/reports/whole-book-proof_<date>.pdf`, so the repository carries a
readable copy of the book and not only its sources. Rebuild and recommit it
whenever the manuscript changes materially; a stale proof is worse than none.

That exception has been withdrawn and restored once each. It was withdrawn on
2026-08-25 (D-068), and both PDFs deleted, because a binary rewritten in most
manuscript commits inflates every diff-based review of the branch; it was
restored the same day (D-072) on the author's instruction. **The cost D-068
named has not gone away** — if a review tool refuses the branch on size again,
that is this file, and the fix is to pass a base after the proof's last change
rather than to delete it a second time without a ruling.

The one-off `ch2-3-proof_2026-08-23.pdf` was deleted by D-068 and is not
restored: it was stale from the day it was committed.

To eyeball a page without a viewer:

```sh
gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r95 -dFirstPage=6 -dLastPage=6 \
   -sOutputFile=page.png book.pdf
```

## The source layout

| file | what it is |
| --- | --- |
| `manuscript/book.tex` | master. Hand-edited. |
| `manuscript/preamble.tex` | all typesetting. Hand-edited; this is the design surface. |
| `manuscript/sections.tex` | the `\input` list. **Generated** by `finishing/tools/gen_book.py` from `sections/ORDER.tsv`. |
| `manuscript/sections/chNN/*.tex` | one file per section, 162 of them. The prose. |
| `finishing/refs.bib` | 282 entries, reached from the manuscript by `\autocite{key}`. |

Add, remove, or renumber a section and you must re-run `gen_book.py` and
`refresh_order_shas.py`; `check_all.sh` fails if either is stale. You do **not**
have to chase the cross-references: since D-066 they are `\ref{sec:N}`, so LaTeX
regenerates every printed number. Write new ones the same way —
`section~\ref{sec:8.7.7}`, with the tie, so the reference cannot break across a
line — and `check_xrefs.py` will tell you if a number gets typed into the prose
by hand.

## Things worth knowing

**`refs.bib` is compiled, so LaTeX validates it.** The first full build failed
on four URLs containing bare `%` inside `note` fields — a comment character in
the `.bbl`, which swallowed the rest of the line — and on `$15/hour`, which
opened math mode. Nothing in `check_all.sh` would ever have caught either. When
editing `refs.bib`, escape `% _ # & $ ^` in prose fields. Do **not** escape them
in `url`, `doi`, or `eprint`: biber emits those inside `\verb` blocks, where an
escape ends up literally in the link.

**`\euro` is the one non-base macro `refs.bib` uses**; `preamble.tex` provides a
fallback. Everything else it uses (`\url \S \i \emph \c \v \textsection \L`) is
standard.

**Look at the proof.** The build succeeding says nothing about whether the page
is right. Two defects in the first successful build were visible only in a
rasterized page and passed every automated check: epigraph stanza breaks were
being dropped, and paragraphs inside a box ran together because `tcolorbox`
zeroes `\parindent`.
