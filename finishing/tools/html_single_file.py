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

    # The stylesheet goes in the page; the link to it goes away.
    link = re.compile(r"[ \t]*<link href='book\.css'[^>]*/>\n?")
    if not link.search(html):
        sys.exit("html_single_file.py: no <link> to book.css -- tex4ht's output changed shape")
    html = link.sub("<style>\n" + css + EXTRA_CSS + "</style>\n", html, count=1)

    # tex4ht writes citation links as href='book.html#X0-key'. Relative to what
    # the file is called, they break the moment it is renamed.
    html, n_links = re.subn(r"href='book\.html#", "href='#", html)

    # The document has no \maketitle, so tex4ht has no title to find.
    if "<title></title>" not in html:
        sys.exit("html_single_file.py: expected an empty <title> to fill in")
    html = html.replace("<title></title>", f"<title>{title}</title>", 1)

    # tex4ht pads its output with runs of whitespace-only lines. There is no
    # <pre> in this book, so dropping them changes nothing that renders.
    lines = [ln.rstrip() for ln in html.split("\n")]
    html = "\n".join(ln for ln in lines if ln) + "\n"

    # Say what is wrong rather than write a file that looks finished.
    problems = []
    if "<img" in html:
        problems.append("the page references an image; a single file cannot carry one")
    if "book.html#" in html:
        problems.append("a link to book.html survived the rewrite")
    if "References" not in html:
        problems.append("no References heading -- biber did not run")
    if len(html) < 500_000:
        problems.append(f"only {len(html)} bytes; the book is larger than that")
    if problems:
        sys.exit("html_single_file.py: " + "; ".join(problems))

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out} ({len(html):,} bytes, {n_links} citation links made relative)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
