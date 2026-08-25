#!/usr/bin/env python3
"""Render the manuscript dialect to LaTeX (lualatex + biblatex/biber).

The companion to render.py, which targets HTML -> LibreOffice -> PDF. This
target exists because LaTeX's referencing machinery is mature and the book now
has a real bibliography: finishing/refs.bib, reached from a [[cite:ID]] marker
through claims.tsv's bib_key column.

Three things this renderer does that render.py does not, each a fidelity gap
in the HTML path rather than a new feature:

  *emphasis*  becomes \\emph{}. render.py escapes it, so the current HTML/ODT
              proof prints literal asterisks (13 of them).
  <<list>>    honors its item markers: "- " is a bullet list, "1. " a numbered
              one. render.py emits <ol> for both, so 80 bullet items render as
              numbered ones.
  <<quote>>   honors indent depth. Three tabs is quoted matter, two tabs is its
              attribution; render.py flattens both to <p>.

Usage: render_tex.py [--chapter N] [-o OUT.tex] [--standalone]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

CLAIMS = os.path.join(common.REPORTS, "claims.tsv")
BIB = os.path.join(common.REPO, "finishing", "refs.bib")

LIST_ITEM = re.compile(r"^\s*(\(\d+\)|\d+[.)]|[-•*]|[a-z][.)])\s+(.*)$")
NUMBERED = re.compile(r"^\s*(\(?\d+[.)]|[a-z][.)])\s")
CITE = re.compile(r"\[\[cite:([^\]]+)\]\]")
BLANK = -1   # marks a blank line inside <<quote>>: a stanza break
EMPH = re.compile(r"\*([^*\n]+)\*")

# The manuscript contains none of \ { } # ^ _ ~ -- verified across all 159
# sections -- so only these three ever need escaping. Kept complete anyway:
# a future edit could introduce one, and a silent mis-escape is worse than a
# redundant table entry.
ESCAPES = {
    "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$",
    "&": r"\&", "#": r"\#", "^": r"\textasciicircum{}", "_": r"\_",
    "~": r"\textasciitilde{}", "%": r"\%",
}


def load_bib_keys():
    """claim_id -> bib_key, for rows that have one."""
    _, rows = common.read_tsv(CLAIMS)
    return {r["claim_id"]: r["bib_key"] for r in rows if r.get("bib_key")}


def esc(s):
    out = []
    for ch in s:
        out.append(ESCAPES.get(ch, ch))
    return "".join(out)


def inline(s, keys, missing):
    """Escape, then restore the markup that survives into LaTeX.

    Order matters: escaping first means a marker's own punctuation cannot be
    mangled, and the markers themselves use no characters the escape table
    touches, so they come through the escape pass intact.
    """
    s = esc(s)
    s = EMPH.sub(lambda m: r"\emph{%s}" % m.group(1), s)

    def cite(m):
        cid = m.group(1)
        key = keys.get(cid)
        if not key:
            missing.add(cid)
            return r"\textbf{[?%s]}" % cid
        return r"\autocite{%s}" % key

    return CITE.sub(cite, s)


def render_section(num, title, lines, keys, missing):
    lvl = common.level(num)
    out = []
    # Front and back matter carry numbers 0 and 11 for the pipeline's sort and
    # identity scheme, but are not reader-facing chapters. render.py drops
    # their labels; an unnumbered \chapter* does the same here, and the counter
    # is fixed up by the caller so the numbered chapters still run 1..10.
    if lvl == 1:
        if num in ("0", "11"):
            out.append(r"\chapter*{%s}" % esc(title))
            out.append(r"\addcontentsline{toc}{chapter}{%s}" % esc(title))
        else:
            out.append(r"\chapter{%s}" % esc(title))
    else:
        cmd = {2: "section", 3: "subsection"}[lvl]
        out.append(r"\%s{%s}" % (cmd, esc(title)))
    out.append(r"\label{sec:%s}" % num)

    quote = lst = box = False
    box_first = False
    items = []
    quote_buf = []

    def flush_list():
        if not items:
            return
        env = "enumerate" if NUMBERED.match(items[0][0]) else "itemize"
        out.append(r"\begin{%s}" % env)
        for _, text in items:
            out.append(r"  \item %s" % text)
        out.append(r"\end{%s}" % env)
        items.clear()

    def flush_quote():
        """Three tabs is quoted matter, two is its attribution."""
        if not quote_buf:
            return
        body = [(d, x) for d, x in quote_buf if d >= 3 or d == BLANK]
        while body and body[0][0] == BLANK:
            body.pop(0)
        while body and body[-1][0] == BLANK:
            body.pop()
        attrib = [x for d, x in quote_buf if 0 < d < 3]
        if body:
            stanzas = [[]]
            for depth, text in body:
                if depth == BLANK:
                    if stanzas[-1]:
                        stanzas.append([])
                    continue
                stanzas[-1].append(text)
            out.append(r"\begin{verse}")
            out.append("\n\n".join(" \\\\\n".join(s) for s in stanzas if s))
            out.append(r"\end{verse}")
        if attrib:
            out.append(r"\begin{flushright}\small\itshape")
            out.append(" \\\\\n".join(attrib))
            out.append(r"\end{flushright}")
        quote_buf.clear()

    for line in lines[1:]:
        raw = line.rstrip("\n")
        s = raw.strip()
        if s == "<<quote>>":
            quote = True
            continue
        if s == "<</quote>>":
            quote = False
            flush_quote()
            continue
        if s.startswith("<<h>>") and s.endswith("<</h>>"):
            out.append(r"\runin{%s}" % inline(s[5:-6].strip(), keys, missing))
            continue
        if s == "<<box>>":
            box, box_first = True, True
            out.append(r"\begin{esbox}")
            continue
        if s == "<</box>>":
            box = False
            out.append(r"\end{esbox}")
            continue
        if s == "<<list>>":
            lst = True
            continue
        if s == "<</list>>":
            lst = False
            flush_list()
            continue
        if s.startswith("#"):
            continue  # notes-to-self are not book text
        if quote:
            if not s:
                quote_buf.append((BLANK, ""))   # stanza break
            else:
                # Depth is meaningful here, so measure it before stripping.
                depth = len(raw) - len(raw.lstrip("\t"))
                quote_buf.append((depth, inline(s, keys, missing)))
            continue
        if not s:
            continue
        m = LIST_ITEM.match(s)
        if lst:
            items.append((s, inline(m.group(2) if m else s, keys, missing)))
            continue
        if box and box_first:
            out.append(r"\boxtitle{%s}" % inline(s, keys, missing))
            box_first = False
            continue
        out.append(inline(s, keys, missing))
        out.append("")
    flush_list()
    flush_quote()
    return "\n".join(out)


PREAMBLE = r"""% Generated by finishing/tools/render_tex.py -- do not edit by hand.
\documentclass[11pt,oneside]{book}

\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}          % a Palatino, matching the HTML path
\usepackage{microtype}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{tcolorbox}
\tcbuselibrary{breakable}   % the only library the box style needs
\usepackage[english]{babel}
\usepackage{textcomp}
% refs.bib uses \euro, which is not a base LaTeX macro. Everything else it
% uses (\url \S \i \emph \c \v \textsection \L) is standard.
\providecommand{\euro}{\texteuro}
\usepackage[hidelinks]{hyperref}   % before biblatex, per its own guidance
\usepackage[backend=biber,style=authoryear,sorting=nyt,maxcitenames=2]{biblatex}
\addbibresource{@@BIB@@}

\setcounter{secnumdepth}{2}             % deepest heading in the book is x.y.z
\setcounter{tocdepth}{2}

% Run-in head: the dialect's <<h>>...<</h>>.
\newcommand{\runin}[1]{\par\medskip\noindent\textbf{#1}\par\nopagebreak\smallskip}

\newtcolorbox{esbox}{
  colback=black!3, colframe=black!35, boxrule=0.4pt, arc=1pt,
  left=8pt, right=8pt, top=8pt, bottom=8pt, breakable,
  fontupper=\small,
  before upper={\setlength{\parskip}{0.5\baselineskip}%
               \setlength{\parindent}{0pt}},
}
\newcommand{\boxtitle}[1]{{\bfseries #1}\par\smallskip}

\title{Ethical Superintelligence}
\date{}
\begin{document}
\frontmatter
\tableofcontents
\mainmatter
"""

POSTAMBLE = r"""
\backmatter
\printbibliography[heading=bibintoc,title={References}]
\end{document}
"""


def main():
    argv = sys.argv[1:]
    chapter = argv[argv.index("--chapter") + 1] if "--chapter" in argv else None
    out_path = argv[argv.index("-o") + 1] if "-o" in argv else None

    keys = load_bib_keys()
    missing = set()

    _, order = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    order.sort(key=lambda r: common.numkey(r["num"]))
    if chapter:
        order = [r for r in order if r["num"].split(".")[0] == str(chapter)]

    parts = []
    for r in order:
        with open(os.path.join(common.REPO, r["path"]), encoding="utf-8", newline="") as f:
            lines = f.readlines()
        # Chapter 0 is unnumbered and precedes chapter 1, so the counter has to
        # be put back to 0 after it or the first numbered chapter would be 2.
        if r["num"] == "1":
            parts.append(r"\setcounter{chapter}{0}")
        parts.append(render_section(r["num"], r["title"], lines, keys, missing))

    doc = (PREAMBLE.replace("@@BIB@@", BIB) + "\n\n".join(parts) + POSTAMBLE)

    if missing:
        sys.stderr.write("WARNING: %d cite ids with no bib_key: %s\n"
                         % (len(missing), ", ".join(sorted(missing))))
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(doc)
        print("wrote %s (%d sections, %d bytes)"
              % (out_path, len(order), len(doc.encode("utf-8"))))
    else:
        sys.stdout.write(doc)


if __name__ == "__main__":
    main()
