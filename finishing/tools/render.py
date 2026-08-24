#!/usr/bin/env python3
"""Render the manuscript dialect to standalone HTML (the build's front end).

There is no TeX or pandoc on this machine, so the local proof path is
HTML -> LibreOffice headless -> ODT -> PDF. See finishing/pipeline.md.

Usage: render.py [--chapter N] [-o OUT.html]
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

LIST_ITEM = re.compile(r"^\s*(\(\d+\)|\d+[.)]|[-•*]|[a-z][.)])\s+(.*)$")

CSS = """
body { font-family: 'Palatino Linotype', Palatino, Georgia, serif; font-size: 11pt;
       line-height: 1.45; margin: 2em auto; max-width: 34em; color: #1a1a1a; }
h1 { font-size: 20pt; margin: 2em 0 0.6em; page-break-before: always; }
h1.first { page-break-before: avoid; }
h2 { font-size: 14pt; margin: 1.6em 0 0.4em; }
h3 { font-size: 12pt; margin: 1.4em 0 0.35em; }
h4, h5, h6, h7 { font-size: 11pt; font-weight: bold; margin: 1.2em 0 0.3em; }
p { margin: 0 0 0.7em; text-align: justify; }
blockquote { margin: 1.2em 2em; font-style: italic; color: #444; }
blockquote p { text-align: left; }
ol, ul { margin: 0 0 0.8em 1.4em; }
li { margin-bottom: 0.3em; }
.num { color: #555; }
/* Boxes are emitted as a single-cell table, not a div: LibreOffice's HTML
   importer applies a div's border to every child paragraph, which renders as a
   stack of separate boxes rather than one. A table cell borders once. */
table.box { border: 0.5pt solid #999; border-collapse: collapse; margin: 1.2em 0; width: 100%; }
table.box td { padding: 0.8em 1em; background: #f7f7f5; }
table.box p { text-align: left; font-size: 10pt; margin: 0 0 0.5em; }
table.box p.boxtitle { font-weight: bold; margin-bottom: 0.5em; }
p.runin { font-weight: bold; margin: 1.1em 0 0.35em; page-break-after: avoid; }
"""


def esc(s):
    return html.escape(s, quote=False)


def render_section(num, title, lines, first):
    lvl = min(common.level(num), 6)
    tag = "h%d" % lvl
    cls = ' class="first"' if (first and lvl == 1) else ""
    # Front/back matter (num 0, 11) are numbered internally for the pipeline's
    # sort/identity scheme but are not "chapters" in the reader-facing book.
    if num in ("0", "11"):
        label = ""
    else:
        label = ("Chapter %s: " % num) if lvl == 1 else ("%s. " % num)
    out = ["<%s%s><span class=\"num\">%s</span>%s</%s>"
           % (tag, cls, esc(label), esc(title), tag)]
    quote = lst = box = False
    box_first = False
    buf = []

    def flush_list():
        if not buf:
            return
        out.append("<ol>")
        for item in buf:
            out.append("<li>%s</li>" % esc(item))
        out.append("</ol>")
        buf.clear()

    for line in lines[1:]:
        s = line.strip()
        if s == "<<quote>>":
            quote = True
            out.append("<blockquote>")
            continue
        if s == "<</quote>>":
            quote = False
            out.append("</blockquote>")
            continue
        if s.startswith("<<h>>") and s.endswith("<</h>>"):
            out.append('<p class="runin"><b>%s</b></p>' % esc(s[5:-6].strip()))
            continue
        if s == "<<box>>":
            box = True
            box_first = True
            # Presentational attributes, not CSS: LibreOffice's HTML importer
            # honors border/cellpadding/bgcolor and drops most stylesheet rules.
            out.append('<table class="box" border="1" cellpadding="10" '
                       'cellspacing="0" width="100%"><tr>'
                       '<td bgcolor="#F2F2EE">')
            continue
        if s == "<</box>>":
            box = False
            out.append("</td></tr></table>")
            continue
        if s == "<<list>>":
            lst = True
            continue
        if s == "<</list>>":
            lst = False
            flush_list()
            continue
        if s.startswith("#"):
            continue  # notes-to-self are not part of the book
        if not s:
            continue
        if quote:
            out.append("<p>%s</p>" % esc(s))
            continue
        m = LIST_ITEM.match(s)
        if lst:
            buf.append(m.group(2) if m else s)
            continue
        if box and box_first:
            # first line inside a box is its title
            out.append('<p class="boxtitle"><b>%s</b></p>' % esc(s))
            box_first = False
            continue
        out.append("<p>%s</p>" % esc(s))
    flush_list()
    return "\n".join(out)


def main():
    argv = sys.argv[1:]
    chapter = None
    if "--chapter" in argv:
        chapter = argv[argv.index("--chapter") + 1]
    out_path = None
    if "-o" in argv:
        out_path = argv[argv.index("-o") + 1]

    _, order = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    order.sort(key=lambda r: common.numkey(r["num"]))
    if chapter:
        order = [r for r in order if r["num"].split(".")[0] == str(chapter)]
    parts = []
    for i, r in enumerate(order):
        with open(os.path.join(common.REPO, r["path"]), encoding="utf-8", newline="") as f:
            lines = f.readlines()
        parts.append(render_section(r["num"], r["title"], lines, i == 0))
    doc = ("<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\">\n"
           "<title>Ethical Superintelligence</title>\n<style>%s</style></head>\n<body>\n%s\n</body></html>\n"
           % (CSS, "\n".join(parts)))
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(doc)
        print("wrote %s (%d sections, %d bytes)" % (out_path, len(order), len(doc)))
    else:
        sys.stdout.write(doc)


if __name__ == "__main__":
    main()
