# Build pipeline

Verified end to end on this machine, 2026-08-22, on chapter 3 (55 sections):
**55-page PDF, justified serif text, numbered headings, lists and epigraphs
intact.**

## What is available here

`libreoffice` / `soffice` 24.2.7 headless, `gs`, python 3.12, node 20.
**No TeX, no pandoc, no mermaid-cli, no graphviz**, and no network to install
them. So the local path is HTML → LibreOffice → ODT → PDF.

## The commands

```sh
# whole book, or one chapter with --chapter N
python3 finishing/tools/render.py -o /path/to/scratch/book.html

soffice --headless --convert-to odt --infilter="HTML (StarWriter)" \
        --outdir /path/to/scratch /path/to/scratch/book.html

soffice --headless --convert-to pdf --outdir /path/to/scratch \
        /path/to/scratch/book.odt
```

`soffice` prints `Warning: failed to launch javaldx` and works anyway.
Build products go to the scratchpad, never into the repo.

To eyeball a page without a viewer:

```sh
gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r80 -dFirstPage=2 -dLastPage=2 \
   -sOutputFile=page.png book.pdf
```

## What the renderer does

`finishing/tools/render.py` maps the dialect to HTML: heading level from the
number's depth (`3.1.2.3.1.4` → `h6`, capped), `<<quote>>` → `<blockquote>`,
`<<list>>` → `<ol>` with the item marker stripped, `<<box>>` → a single-cell
table with its first line as a bold title, `#` notes dropped (they are notes to
self, not book text). Chapters start a new page; 34em measure,
Palatino with Georgia fallback.

## Two importer behaviours worth knowing

Found by looking at a rendered page, not by any automated check — both passed
every test in `check_all.sh`.

1. **A `<div>` border is applied to each child paragraph**, so a bordered block renders as a stack of separate boxes. Emit a single-cell table instead.
2. **Most stylesheet rules are dropped on import.** The table's CSS border and background vanished; `border`, `cellpadding`, `cellspacing`, `bgcolor` and `<b>` are honored. `render.py` now uses presentational attributes for boxes and CSS only for things that degrade gracefully.

The general rule: **look at the proof.** The build succeeding says nothing about
whether the page is right.

## Known limits of this path

- **No automatic table of contents.** LibreOffice's TOC is a field, and headless conversion does not reliably refresh it. Generate the TOC as literal content from `outline.tsv` when the structure settles.
- **No endnotes yet.** D-009 endnotes are not implemented; `[[cite:ID]]` placeholders currently pass through as literal text, which is the correct behaviour for now — they should be visible while they are unresolved.
- **Unmarked lists render as paragraphs.** The 585 items outside `<<list>>` markup look like prose here, because they are prose that wants to be a list. The style sheet handles this; the renderer should not guess.
- **Styling is a proof, not a design.** Real typesetting is a later decision and probably belongs on a machine with TeX. Nothing about the source format forecloses that.

## Fallbacks not needed yet

`render.py --md` (Markdown out, for a pandoc build elsewhere) and a flat-ODT
writer with real named styles are both straightforward if the LibreOffice path
proves inadequate. Neither is worth building until the text settles.
