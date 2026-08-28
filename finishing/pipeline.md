# Build pipeline

The book is LaTeX and builds two ways from the same `manuscript/book.tex`.
Verified end to end on this machine, 2026-08-28: **192-page PDF, lualatex +
biber, no undefined references; and a one-file HTML page, make4ht + biber, 1,323
internal links and none of them broken.**

## What is available here

TeX Live 2026 installed under `$HOME/texlive/2026` — user-space, because there
is no root on this machine and `apt` was therefore not an option. `lualatex`,
`biber` 2.22, `make4ht`/`tex4ht`, `scheme-medium` plus `collection-latexextra`.
Also `libreoffice` 24.2.7 headless, `gs`, `pdfinfo`/`pdftotext`, python 3.12,
node 20. **Not** here: `pandoc`, ImageMagick's `convert`, `tidy`.

`~/texlive/2026/bin/x86_64-linux` is **not** on the default PATH. `build_tex.sh`
adds it; set `TEXLIVE_BIN` to override.

## The commands

```sh
finishing/tools/build_tex.sh  [OUTDIR]     # the PDF        default $TMPDIR/es-build
finishing/tools/build_html.sh [OUTDIR]     # the HTML page  default $TMPDIR/es-build
finishing/tools/build_proof.sh [DATE]      # both, into finishing/reports/
```

`build_tex.sh` runs lualatex → biber → lualatex twice, from
`manuscript/book.tex`, with `-output-directory` so no aux files land in the
source tree. Two runs after biber: the first resolves citations, the second the
TOC and any page references that moved because of them. About 30 seconds.

`build_html.sh` runs the same sequence through `make4ht`, which drives lualatex
in tex4ht's dvi mode and converts the result. The sequence is in
`finishing/tools/html.mk4`, passed with `-e`, because make4ht's own default does
not run biber and biblatex would emit an empty bibliography. What make4ht leaves
behind is a page plus a stylesheet plus a dozen intermediates;
`finishing/tools/html_single_file.py` folds the stylesheet in, makes the citation
links relative so the file can be renamed, gives it the book's title, and refuses
to write anything it cannot verify. About 18 seconds.

**What each is for.** The PDF is the typeset book: it is the only one of the two
that can be page-proofed, because it is the only one with pages. The HTML is the
book to read in a browser and search with ctrl-F, and it is better than the PDF
at one thing — every `section~\ref` is a link you can follow and come back
from, and every `\autocite` jumps to its entry in the References. Nothing about
widows, breaks, or the shape of a page can be judged in it.

Build products go to the scratchpad, with one standing exception: the whole-book
proof is committed as `finishing/reports/whole-book-proof_<date>.pdf` **and
`.html`**, so the repository carries a readable copy of the book and not only its
sources. `build_proof.sh` writes both, so the two cannot drift apart — an HTML
proof a week older than the PDF beside it would be worse than none, because
nothing about it would say so. Rebuild and recommit whenever the manuscript
changes materially, and delete the older pair in the same commit; the script
prints the `git rm` lines for it.

`.gitattributes` marks both `-diff -merge`. They are generated whole on every
rebuild, and a megabyte of regenerated markup diffed line by line would bury the
source changes in the same commit — the cost D-068 named below, which the PDF
carries by being binary and which the HTML would otherwise carry worse.

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

## "Make the proofs"

An author's phrase — "make the proofs," "do the proofs," or any near variant —
that names a fixed sequence, not just a build. It means all of this, in order:

1. **Commit whatever is in the tree, to `main`, and push.** Directly to `main`;
   this gesture does not open a branch. Say what is being committed before
   committing it if it is more than the work just discussed — "everything" is
   the instruction, and a surprise in the diff is the author's to catch, not
   mine to swallow.
2. **Run `finishing/tools/build_proof.sh`.** Both formats, one date.
3. **Remove the previous dated pair** if the date has rolled over. The script
   prints the `git rm` lines; the proof is one pair replaced, not a series.
4. **Point the README's links at the new files.** Both of them, in the "Read the
   book" line under the subtitle. A link to a proof that is no longer there is
   worse than no link.
5. **Commit the proofs and the README, and push again.** Two commits, not one:
   the work is legible in the first, and the second is generated output.

Step 5 is why it is two commits. A megabyte of rebuilt proof in the same commit
as the prose that changed makes the prose unreadable in the diff, which is the
cost D-068 named and `.gitattributes` only partly pays down.

**A limit worth knowing before relying on the README's HTML link.** GitHub does
not render a committed `.html`; following that link gets the source or a
download, not a page. The PDF link renders in GitHub's own viewer and works.
Serving the HTML as a page needs a decision the repository has not taken —
GitHub Pages, or a third-party renderer — and it is recorded in D-083 rather
than chosen here.

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

**Do not escape a quotation mark in `refs.bib`.** A field is delimited by
braces, so a `"` inside it needs nothing; `\"` is LaTeX's diaeresis accent and
takes the next letter with it. Two entries had it, and the PDF had been printing
`Ëvaluating Large Language Models` and `in ẗheory of mind”̈` since the entries
were written. LaTeX raises nothing — both are valid accents — so this is invisible
until someone reads the References. It was found by the first HTML build, which
failed on it, because tex4ht cannot set `ẗ` as text and tried to make a picture
of it instead.

**Quotes inside a bibliography title have to be single, and literal.** biblatex
puts an article title in double quotes, so a nested double quote prints as `””`.
And a title *ending* in `'` meets biblatex's own closing `''`, which TeX's
ligature program reads as `”` followed by `’` — the outer quote inside the inner
one. Writing the characters themselves, `‘` and `’`, has no ligature to form.
Seven titles carried one of these; all seven now read correctly in both builds.

**`\euro` is the one non-base macro `refs.bib` uses**; `preamble.tex` provides a
fallback. Everything else it uses (`\url \S \i \emph \c \v \textsection \L`) is
standard.

**tex4ht rasterizes anything it cannot set as text**, and the single-file page
cannot carry an image, so `build_html.sh` fails on any such request rather than
writing a page with a hole in it. There are none in the book as it stands: no
mathematics, no diagrams, and the box, verse, and list environments all convert
to markup. A request appearing here means something new was written that tex4ht
does not understand — read the `--- needs ---` line it prints, which names the
page of the intermediate `.idv` file, not the page of the book.

**Look at the proof.** The build succeeding says nothing about whether the page
is right. Two defects in the first successful build were visible only in a
rasterized page and passed every automated check: epigraph stanza breaks were
being dropped, and paragraphs inside a box ran together because `tcolorbox`
zeroes `\parindent`.
