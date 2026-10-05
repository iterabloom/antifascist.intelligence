#!/usr/bin/env python3
"""Assemble tex4ht's output into one self-contained HTML file.

make4ht leaves book.html and book.css side by side in the build directory, and
the citation links it writes are absolute -- href='book.html#X0-key' -- so the
page only works under that filename, next to that stylesheet. This puts the
stylesheet inside the page, makes those links relative, and gives the file the
book's title, so the result can be renamed, moved, or mailed on its own.

Usage: html_single_file.py BUILD_DIR OUT_FILE
"""
import re
import sys
from pathlib import Path

# Layered on top of tex4ht's own stylesheet, which already sets a measure and a
# dark-mode palette. Pagella is what the PDF sets; Palatino is the same face by
# the name a browser is likely to have.
EXTRA_CSS = """
/* html_single_file.py: readability, on top of tex4ht's stylesheet. */
body { line-height: 1.5;
       font-family: Palatino, "Palatino Linotype", "TeX Gyre Pagella", Georgia, serif; }
h2, h3, h4 { margin-top: 1.6em; }
.tcolorbox { margin: 1.5em 0; }
/* tex4ht sets the verse block to nowrap, which pushes the longer epigraph lines
   off a narrow screen. The line breaks are <br/> and survive wrapping. */
.verse { white-space: normal; }
/* The Westworld epigraph carries a bare archive.org URL, which is text and not
   a link, so tex4ht's rule for breaking long links does not reach it. */
body { overflow-wrap: break-word; }
"""

# The HTML counterpart of the PDF's watermark and running foot (D-319). The page
# has no pages, so "on every page" becomes a tiled background that scrolls with
# nothing and a bar fixed to the bottom of the window.
#
# The mark is filled `gray` rather than branched on prefers-color-scheme: the
# stylesheet above sets `background-color: Canvas`, so the page follows the
# reader's system theme, and a mid grey at this opacity reads as a watermark
# against either end of that. The bar takes CanvasText for the same reason.
DRAFT_CSS = """
/* html_single_file.py: the draft apparatus. */
/* Citations of bibliography entries no human has checked yet (D-641): the
   preamble wraps each in this span, from the ledger, in draft mode only. */
.ref-unchecked { background-color: rgba(255, 140, 0, 0.35); }
body { background-image: url("data:image/svg+xml,\
%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20width='300'%20height='200'%3E\
%3Ctext%20x='150'%20y='115'%20font-family='Georgia,serif'%20font-size='46'\
%20fill='gray'%20text-anchor='middle'%20transform='rotate(-30%20150%20100)'\
%3EDRAFT%3C/text%3E%3C/svg%3E");
       background-repeat: repeat;
       background-attachment: fixed;
       padding-bottom: 3.2em; }
/* The tile is painted behind body's own content by the box model, so the prose
   needs no z-index of its own; only the fixed bar does. */
.draftbar { position: fixed; left: 0; right: 0; bottom: 0; z-index: 2;
            margin: 0; padding: 0.45em 0.8em;
            background-color: Canvas; color: CanvasText; opacity: 0.97;
            border-top: 1px solid rgba(128,128,128,0.45);
            font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
            font-size: 0.72rem; line-height: 1.3; text-align: center; }
@media print { body { background-image: none; padding-bottom: 0; }
               .draftbar { position: static; opacity: 1; } }
"""


def book_title(repo: Path) -> str:
    """Read the title out of book.tex, which is where it is written once."""
    src = (repo / "manuscript" / "book.tex").read_text(encoding="utf-8")
    parts = []
    for macro in ("booktitlemain", "booksubtitle"):
        m = re.search(r"\\newcommand\{\\%s\}\{([^}]*)\}" % macro, src)
        if not m:
            sys.exit(f"html_single_file.py: no \\{macro} in manuscript/book.tex")
        parts.append(m.group(1))
    return ": ".join(parts)


def main() -> int:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build, out = Path(sys.argv[1]), Path(sys.argv[2])
    repo = Path(__file__).resolve().parents[2]

    html_src, css_src = build / "book.html", build / "book.css"
    for f in (html_src, css_src):
        if not f.exists():
            sys.exit(f"html_single_file.py: {f} missing -- the make4ht run did not finish")

    html = html_src.read_text(encoding="utf-8")
    css = css_src.read_text(encoding="utf-8")
    title = book_title(repo)

    # The status line the preamble sets into the title page. Its absence is not
    # a failure: it means \draftmodefalse, and then the page gets no apparatus
    # either. Taking the text from the page rather than rebuilding it from the
    # ledger is what keeps the bar and the PDF's footer saying the same thing --
    # they are the same string, set once by TeX.
    m = re.search(r">(PREPRINT[^<]*)<", html)
    status = " ".join(m.group(1).split()) if m else None

    # The stylesheet goes in the page; the link to it goes away.
    link = re.compile(r"[ \t]*<link href='book\.css'[^>]*/>\n?")
    if not link.search(html):
        sys.exit("html_single_file.py: no <link> to book.css -- tex4ht's output changed shape")
    extra = EXTRA_CSS + (DRAFT_CSS if status else "")
    html = link.sub("<style>\n" + css + extra + "</style>\n", html, count=1)

    # tex4ht writes citation links as href='book.html#X0-key'. Relative to what
    # the file is called, they break the moment it is renamed.
    html, n_links = re.subn(r"href='book\.html#", "href='#", html)

    # It also emits one anchor with no key at all -- <a href='book.html' id='X0-'>
    # </a>, ahead of the first bibliography entry. The href has no fragment, so
    # the rewrite above does not touch it, and it points at a file that is not
    # there; the id is the empty X0- prefix. It links nothing and labels nothing,
    # so it goes.
    html, n_empty = re.subn(r"<a href='book\.html' id='X0-'>\s*</a>", "", html)

    # A DOI containing an underscore is set as a dot-above accent in the link
    # text -- 10.1007/978-3-662-47854-7_14 prints as ...-7˙14 -- while the
    # href beside it keeps the underscore and works. The PDF sets the same entry
    # correctly, so this is tex4ht's, not the bibliography's; one entry in
    # refs.bib has such a DOI and escaping it in the .bib breaks the href
    # instead. The href is what biblatex built from the field, so it is the
    # authority: where the link text disagrees with it, take the href.
    def doi_text(m):
        href, text = m.group(1), m.group(2)
        if text == href:
            return m.group(0)
        doi_fixed.append(href)
        return m.group(0).replace(">" + text + "<", ">" + href + "<")

    doi_fixed = []
    html = re.sub(
        r"<a href='https://doi\.org/([^']*)'>([^<]*)</a>", doi_text, html
    )

    # tex4ht draws section anchors and citation anchors from one counter, so a
    # chapter anchor and a citation anchor can collide (x1-70002 is both chapter
    # 2's title and the second citation in a later paragraph), and it can hang a
    # heading's readable slug on a later paragraph as well. Either way the second
    # id is the accident: the first is what the table of contents and the prose
    # links point at. Drop the duplicates and say which, rather than shipping a
    # page whose ids are not unique.
    seen, dropped = set(), []

    def dedupe(m):
        value = m.group(1)
        if value in seen:
            dropped.append(value)
            return ""
        seen.add(value)
        return m.group(0)

    html = re.sub(r" id='([^']*)'", dedupe, html)

    # The document has no \maketitle, so tex4ht has no title to find.
    if "<title></title>" not in html:
        sys.exit("html_single_file.py: expected an empty <title> to fill in")
    html = html.replace("<title></title>", f"<title>{title}</title>", 1)

    if status:
        if "<body>" not in html:
            sys.exit("html_single_file.py: no <body> to attach the draft bar to")
        html = html.replace("<body>", f"<body>\n<div class='draftbar'>{status}</div>", 1)

    # tex4ht pads its output with runs of whitespace-only lines. There is no
    # <pre> in this book, so dropping them changes nothing that renders.
    lines = [ln.rstrip() for ln in html.split("\n")]
    html = "\n".join(ln for ln in lines if ln) + "\n"

    # Say what is wrong rather than write a file that looks finished.
    problems = []
    if "<img" in html:
        problems.append("the page references an image; a single file cannot carry one")
    if "book.html" in html:
        problems.append("a link to book.html survived the rewrite")
    ids = re.findall(r" id='([^']*)'", html)
    if len(ids) != len(set(ids)):
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        problems.append(f"duplicate ids survived de-duplication: {', '.join(dupes)}")
    if "id=''" in html:
        problems.append("an element carries an empty id")
    if "References" not in html:
        problems.append("no References heading -- biber did not run")
    if len(html) < 500_000:
        problems.append(f"only {len(html)} bytes; the book is larger than that")
    if problems:
        sys.exit("html_single_file.py: " + "; ".join(problems))

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    note = f"{len(html):,} bytes, {n_links} citation links made relative"
    if n_empty:
        note += f", {n_empty} empty anchor dropped"
    if dropped:
        note += f", duplicate ids dropped: {', '.join(sorted(set(dropped)))}"
    if doi_fixed:
        note += f", DOI link text repaired: {', '.join(doi_fixed)}"
    note += ", draft watermark and status bar" if status else ", no draft apparatus (draftmode off)"
    print(f"wrote {out} ({note})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
