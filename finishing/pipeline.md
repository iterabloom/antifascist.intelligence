# Build pipeline

The book is LaTeX and builds two ways from the same `manuscript/book.tex`.
Verified end to end on this machine, most recently 2026-08-31 after P79 and P80,
against the committed proof pair rather than a build directory: **182-page PDF, lualatex +
biber, no undefined references and no undefined citations; and a one-file HTML page,
make4ht + biber, with 332 citation links made relative, one empty anchor dropped and
two duplicate ids dropped.** **The internal-link count is re-taken here and is 896
over 1,496 ids, with none broken and none duplicated.** The counts fall a little at every
rebuild because the compression passes keep cutting cross-references and citations along
with the prose carrying them; read a fall as the passes' work unless the broken or
duplicated columns move off zero, which is the number that would signal a defect.
**This rebuild is the cleanest instance of that reading yet**: links fell 932 to 896,
exactly the 36 cross-references P79 and P80 removed between them, and the id count did
not move at all, because neither pass cut a section or a heading. P77's 84-link fall was
the same arithmetic against the glossary. P78 moved the link count not at all and the id
count up three, which is what a pass that converts a construction rather than cutting a
claim looks like in these columns. The P53 figure, 1,091 over 1,589, was dropped as
uncarryable at P57 and is not comparable.

**Count the links with a parser that accepts single quotes.** tex4ht writes `id='x1-1000'`
and `href='#introduction'`, not double-quoted attributes, and a regular expression written
for `id="..."` returns zero over zero on a 944K page. That is a measurement failure and it
looks exactly like a clean result; it was reported as one for a moment during the P80
proofs before the raw `id=` count contradicted it.

## What is available here

TeX Live 2026 installed under `$HOME/texlive/2026` — user-space, because there
is no root on this machine and `apt` was therefore not an option. `lualatex`,
`biber` 2.22, `make4ht`/`tex4ht`, `scheme-medium` plus `collection-latexextra`.
Also `libreoffice` 24.2.7 headless, `gs`, `pdfinfo`/`pdftotext`, python 3.12,
node 20. **Not** here: `pandoc`, ImageMagick's `convert`, `tidy`. Nor, found at P62,
either Python package `redundancy.py` needs: `sentence_transformers` for its default
backend and `sklearn` for its `--tfidf` fallback. **That tool cannot run on this
machine**, and a redundancy check has to be done another way — P62 used shared n-grams
between the new section and the sections it drew from.

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
links relative so the file can be renamed, gives it the book's title, drops
tex4ht's one keyless anchor and any id it has already used, and refuses to write
anything it cannot verify. The de-duplication is D-095: tex4ht draws section and
citation anchors from one counter, so a chapter's title anchor and a citation
anchor can be the same id, and it can hang a heading's readable slug on a later
paragraph. It keeps the first, which is what the links point at, drops the rest,
and prints what it dropped. About 18 seconds.

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

## The Overleaf round trip

`finishing/tools/overleaf.py` takes the manuscript out to Overleaf for visual
editing and brings it back (D-169). Two subcommands, and **packages live outside
the repository** — `~/book-scratch/overleaf/` by default, beside
`choose-a-random-page.py`'s output. A path under the repository root is refused
in both directions, because a zip of the manuscript in the tree is a build
product and it would be committed.

```sh
finishing/tools/overleaf.py export                    # -> ~/book-scratch/overleaf/
finishing/tools/overleaf.py import ZIP --dry-run      # report, write nothing
finishing/tools/overleaf.py import ZIP                # apply, repair, check
```

**Always dry-run first.** It reports exactly what would be written, and it is
the only cheap way to see a conflict before it becomes a diff.

**The package** is `manuscript/` flattened to its own root — `book.tex`,
`preamble.tex`, `sections.tex`, the 137 section files — plus `refs.bib`, a
README and a manifest. **One line is rewritten**: `preamble.tex`'s
`\addbibresource{../finishing/refs.bib}` becomes `refs.bib`, because that is the
only path in the build escaping `manuscript/` and an Overleaf project has
nothing outside itself. Everything else travels byte for byte. The rewrite is
exact-match and counted in both directions; if the line is not there to reverse,
the file is reported and not applied rather than guessed at.

**Set the compiler to LuaLaTeX in Overleaf** — gear icon → Compiler. The book
loads `fontspec` and does not build under pdfLaTeX. Overleaf's documentation
gives that menu as the way to set it, so the package does not try from inside a
file. Verified: the exported package compiles on its own to **186 pages with no
undefined references**, the same as `build_tex.sh` on the same commit.

**The main document is `book.tex`, and until D-170 the package did not make that
findable.** Overleaf chooses a project's main file by scanning for
`\documentclass`, which lived in `preamble.tex` — so Overleaf compiled the
preamble, hit end of file with no `\begin{document}`, and aborted on
`(job aborted, no legal \end found)` under the banner `<*> preamble.tex`. **The
package was fine and the entry point was wrong**, which is what that error means
wherever it appears. D-170 moved `\documentclass` into `book.tex`, leaving it
the only file in the package that carries one. The move is output-neutral: the
PDF before and after is 186 pages with an identical `pdftotext` digest, and the
HTML build is unaffected.

**What that fixes and what it does not.** What is verified here is that
`book.tex` is now the sole bearer of `\documentclass` and that the local builds
do not move. **Whether Overleaf's detection then picks it is a fact about
Overleaf and is not verifiable from this machine** — and an existing project
remembers the main file it was given, so re-uploading into one that already
chose `preamble.tex` will keep that choice. The fallback is the file tree:
right-click `book.tex` → Set as Main File, or Menu → Main document.

**The claim above was published before it was fully true.** It read that the
package "compiles there as it stands," and the page and reference counts in it
are right and reproduce. The upload it describes must have had its main file set
by hand, and the step went unrecorded — the first real Overleaf compile after
D-169 failed on exactly this. **A round trip verified by its output is not
verified end to end**; the steps taken to reach that output are part of what
gets recorded, and one of them was missing.

**What the import is up against**, and the answer to each:

- **`sections.tex` is generated.** It has to be in the package or Overleaf
  cannot compile, so it goes out and is then ignored on the way back and
  regenerated from `ORDER.tsv`. The TOC is not in the package at all.
- **Four files carry each heading.** The `.tex` heading is authoritative
  (D-011); `ORDER.tsv`, `outline.tsv` and `ledger.tsv` each keep a copy of the
  title, and a mismatch with `ORDER.tsv` fails `check_structure.py` **fatally**.
  A retitle in Overleaf is fine: the import syncs all three and prints every
  line it changed. `--no-sync-titles` leaves them stale, which fails the suite.
- **The repository moves while the author edits.** The manifest records both
  what was exported and what the repository held at the time, so the import
  tells "Overleaf changed this" from "the repository changed this" and
  **refuses the file where both moved**. All three cases were tested and
  separate correctly. Delete the manifest and that distinction is gone; the
  import then refuses to run without `--no-manifest-ok`.

**Structural change stops the import with nothing written.** A renumber, a
heading-depth change, a heading that no longer opens the file, and a deleted or
renamed section were caught together in one run and none of them was applied.
Each needs rows in `ORDER.tsv`, `outline.tsv` and `ledger.tsv`, or a
renumber-map and a sweep of every `\ref` — none of which are in the package.
Those are made in the repository, not in Overleaf. A file Overleaf added is
reported and never applied, for the same reason.

After applying, the import runs `refresh_order_shas.py`, `gen_book.py`,
`headings.py --write-toc` and `check_all.sh`, and prints the result. **A green
suite means the structure survived the trip, not that the prose did** — what
came back is writing, and writing is read. `git diff` is the read, which is why
the import refuses a dirty tree without `--allow-dirty`.

One oddity the round trip surfaced and did not change:
`manuscript/sections/ch12/12_02_03.tex` is the only file in the manuscript with
no final newline. Normalizing it on the way back invented an edit to a file
nobody had opened, so the import now restores a final newline only where the
repository's own copy has one.

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
   **Rolled over in local time**, which is what `build_proof.sh` names files by
   (`date +%F`) and what this repository's `name_YYYY-MM-DD` convention has
   always meant. The machine runs on US Eastern, so between roughly 20:00 and
   midnight local the UTC date is already tomorrow and the proof's is not.
   Checking `date -u` and concluding the pair needs renaming is a mistake this
   file now records because it was made. Read `date`, not `date -u`.
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
| `manuscript/sections/chNN/*.tex` | one file per section, 136 of them. The prose. |
| `finishing/refs.bib` | 308 entries, every one of them cited, reached from the manuscript by `\autocite{key}`. The 37 nothing cites live in `unused_bibliography.bib` (D-111, five more at D-137 to D-139, one at D-145, two at D-147, two at D-148, two at D-153, and two at D-156). |

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
