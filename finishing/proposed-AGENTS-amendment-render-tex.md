# Amendment to AGENTS.md — the renderer's `--tex` form — APPLIED 2026-09-16

**Status: approved by the author and applied.** Kept as the record of what
changed and why; the live rule is in `AGENTS.md`. The approval was *yes please
modify AGENTS.md so that I can ask for either a markdown or a latex
single-file*, given after the proposal below was put to him in full.

**One sentence was added that the proposal below does not carry**, because the
approval asked for something the proposed text left implicit — which form fires
on which ask. It reads: *Which form is the author's ask: Markdown unless he says
LaTeX, `.tex`, or the source.* Everything else was applied as written.

## Why it needs one

The SOP in `AGENTS.md` is titled "Rendering the manuscript as Markdown" and says
the script "writes the whole book as one Markdown file." D-334 gave it a second
output: `--tex` writes the LaTeX instead, bibliography included, and
`--no-notes` strips the bibliography's note fields. A session that reads only
`AGENTS.md` — which is every session, since `CLAUDE.md` is one line pointing at
it — will not know the flag exists, and the paragraph as it stands is now
wrong about what the script does rather than merely incomplete.

`finishing/README.md`'s tool row already carries the change; that file needs no
approval, and it is read by a session that goes looking, not by every session.

## Current text

> - **Rendering the manuscript as Markdown.**
>   `finishing/tools/render_markdown.py` writes the whole book as one Markdown
>   file to `/tmp` and prints the absolute path on stdout. Run it when the text is
>   wanted in one plain file: to read without a PDF, to search or diff the prose
>   across two states, or to hand the book to something that takes Markdown.
>   Reading order and section numbers come from `manuscript/sections/ORDER.tsv`,
>   the same file `gen_book.py` builds `sections.tex` from, so the order is the
>   book's by construction and not by a second list kept in step by hand.
>   `--out PATH` writes elsewhere; `--check` reports and writes nothing.
>
>   **The output is disposable and the LaTeX is the source.** It lands outside the
>   repository on purpose. Do not commit it, do not point anybody at it as the
>   book, and do not edit it expecting the change to reach the manuscript —
>   nothing reads it back, and an edit made there is lost the next time anyone
>   runs the script. To change the book, change `manuscript/sections/`.
>
>   **What it does not carry:** page breaks, the table of contents, the title
>   page, and the typeset bibliography. Citations survive as Pandoc-style keys
>   (`[@key]`, with any locator following the key) pointing into
>   `finishing/refs.bib`, which is not inlined; `\ref` resolves to the section
>   number; `\S` becomes §. Everything else in the manuscript's macro set —
>   the run-in heads, boxes, epigraphs, the one table, the lists — has a
>   conversion. **The script prints a warning on stderr naming any LaTeX command
>   that reached the output unconverted.** That warning means the manuscript has
>   grown a construct the script has not been taught. Teach the script; do not
>   hand-fix the Markdown, which is thrown away.

## Proposed text

The heading changes, one sentence in the first paragraph changes, and one
paragraph is added at the end. Everything else stands as written.

> - **Rendering the manuscript as one file.**
>   `finishing/tools/render_markdown.py` writes the whole book to `/tmp` and
>   prints the absolute path on stdout — Markdown by default, or the LaTeX
>   itself under `--tex`. Run it when the text is wanted in one plain file: to
>   read without a PDF, to search or diff the prose across two states, or to
>   hand the book to something that takes Markdown. Reading order and section
>   numbers come from `manuscript/sections/ORDER.tsv`, the same file
>   `gen_book.py` builds `sections.tex` from, so the order is the book's by
>   construction and not by a second list kept in step by hand.
>   `--out PATH` writes elsewhere; `--check` reports and writes nothing.
>
>   **The output is disposable and the LaTeX is the source.** It lands outside the
>   repository on purpose. Do not commit it, do not point anybody at it as the
>   book, and do not edit it expecting the change to reach the manuscript —
>   nothing reads it back, and an edit made there is lost the next time anyone
>   runs the script. To change the book, change `manuscript/sections/`.
>
>   **What the Markdown does not carry:** page breaks, the table of contents, the
>   title page, and the typeset bibliography. Citations survive as Pandoc-style
>   keys (`[@key]`, with any locator following the key) pointing into
>   `finishing/refs.bib`, which is not inlined; `\ref` resolves to the section
>   number; `\S` becomes §. Everything else in the manuscript's macro set —
>   the run-in heads, boxes, epigraphs, the one table, the lists — has a
>   conversion. **The script prints a warning on stderr naming any LaTeX command
>   that reached the output unconverted.** That warning means the manuscript has
>   grown a construct the script has not been taught. Teach the script; do not
>   hand-fix the Markdown, which is thrown away.
>
>   **`--tex` converts nothing** (D-334). It writes `manuscript/book.tex` with
>   every `\input` resolved — the preamble, the generated `draft-status.tex`,
>   and every section — and `finishing/refs.bib` inside a `filecontents` block,
>   with each file between `%% ===== START <path> =====` and `%% ===== END
>   <path> =====` so a passage can be traced back to the file that holds it.
>   **`--no-notes` strips the `note` field from every bibliography entry**, 161
>   of the 229, taking 670 KB to 608 KB; it is refused without `--tex`. The file
>   compiles as it stands, to the same 164 pages and the same text, but that is
>   a side effect and not the point: five paragraphs break their last line
>   differently, because concatenating the sections drops a space token `\input`
>   contributes at each file boundary. **Page-proof the book from
>   `finishing/tools/build_tex.sh`, never from this file.**

## What is not proposed

Renaming the script. It is `render_markdown.py` and now has a LaTeX form, which
is a mismatch, but the name is cited by `AGENTS.md`, `finishing/README.md`,
D-318, D-319 and D-334, and a rename buys a tidier name at the price of
repointing an append-only record. Raise it as its own decision if it is worth
that.
