#!/usr/bin/env python3
"""Render the whole manuscript as one file, outside the repository.

Two forms, one reading order. The default is Markdown: the book as plain text,
to read without a PDF, to search or diff the prose across two states, or to
hand to something that takes Markdown. `--tex` writes LaTeX instead -- the
manuscript's own source, whole, bibliography included -- for pasting into
something that should see what the book actually says, macros and all, or for
a compile somewhere this repository is not.

The book is LaTeX (D-065) and neither output is a second source of truth: both
are disposable, written to /tmp by default, and nothing in the repository reads
either back.

Reading order and section numbers come from manuscript/sections/ORDER.tsv, the
same file gen_book.py builds sections.tex from, so both outputs are in the
book's order by construction rather than by a second list kept in step by hand.

What Markdown loses, and knowingly: page breaks, the table of contents, the
title page, the typeset bibliography. Citations survive as Pandoc-style keys
([@smith2020title]) pointing into finishing/refs.bib, which is not inlined.

--tex converts nothing. It is book.tex with every \\input resolved -- the
preamble, the generated draft-status macros, and every section in ORDER.tsv
order -- and finishing/refs.bib inside a filecontents block, with every file
between START and END markers naming its path, so a passage can be traced back
to the file that holds it. `--no-notes` strips both fields that print as a note
in the References -- `note` and `addendum` -- from every bibliography entry.
Of the 275 entries, 199 carry a `note` and 30 an `addendum`.

Neither form carries the draft apparatus (D-335). The Markdown drops the
PREPRINT status line it used to print at both ends, and the LaTeX writes the
preamble's \\draftmodetrue out as \\draftmodefalse, so there is no DRAFT
watermark and no footer on any page: both are proofing marks, and in text
handed to a reader they are noise to be discounted. The book keeps them --
the setting in manuscript/preamble.tex is untouched -- so a PDF built from
the rendered file is a draft with nothing saying so, and is not the proof.

The file compiles as it stands, to the same page count and the same text as
the book, but that is a side effect and not the point: five paragraphs break
their last line differently, because concatenating the sections drops a space
token that \\input contributes at each file boundary. The proof PDF is built
from manuscript/book.tex (finishing/tools/build_tex.sh) and never from here.

Usage:
    finishing/tools/render_markdown.py              # -> /tmp/<slug>_<date>.md
    finishing/tools/render_markdown.py --tex        # -> /tmp/<slug>_<date>.tex
    finishing/tools/render_markdown.py --tex --no-notes   # ... minus bib notes
    finishing/tools/render_markdown.py --out PATH
    finishing/tools/render_markdown.py --check      # report only, write nothing
"""

import argparse
import csv
import datetime
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

SLUG = "antifascist-intelligence"

# \chapter -> "##", because "#" is the book's own title. Depth is taken from
# the LaTeX command and not from the section number, so a starred subsection
# inside a section file lands where its author put it.
HEADING_DEPTH = {"chapter": 2, "section": 3, "subsection": 4, "subsubsection": 5}

# Dropped outright: typesetting with no Markdown counterpart.
DROP_COMMANDS = [
    r"\\label\{[^}]*\}",
    r"\\unnumberedlabel\{[^}]*\}\{[^}]*\}",
    r"\\backmattermark\{[^}]*\}",
    r"\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}",
    r"\\nopagebreak",
    r"\\hline",
    r"\\rule\{[^}]*\}\{[^}]*\}",
    r"\\(?:small|itshape|bfseries|noindent|par|medskip|smallskip|centering)\b",
]

# Escaped characters, restored to themselves.
UNESCAPE = {r"\$": "$", r"\%": "%", r"\&": "&", r"\#": "#", r"\_": "_"}


def repo_root():
    return subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True).stdout.strip()


def read_order(root):
    """ORDER.tsv in reading order.

    Via common.order_rows(), which sorts on `seq`. Reading the file and taking
    its rows as they stand gave the same answer only because ORDER.tsv happens
    to be stored in seq order, which nothing enforces (D-422).
    """
    return common.order_rows()


def label_map(root, rows):
    """label -> the number the book prints for it.

    NOT ORDER.tsv's `num` (D-422). D-406 made `num` a stable identity that
    matches the filename, the legacy label and the ledger key, while a file's
    printed position moves; mapping a label to `num` made this renderer print
    6.1 as 3.3 and ch:route as 16, wrong for 139 of the 201 references the
    manuscript then held. The printed number comes from the same counter
    simulation the generated table of contents is built from, checked against
    the proof build's own book.aux at D-422: 96 labels, zero disagreements.

    Three cases the heading number alone does not cover:
      * \\unnumberedlabel{X}{V} pins V, which is what LaTeX writes and what the
        aux records (sec:0 -> 0, sec:13 -> 17).
      * a \\label anywhere in a file's body takes the number in force at its
        line, not the file's own heading (sec:hold -> 3.1).
      * a file with no heading is a continuation and carries the number of the
        heading before it.
    """
    out = {}
    current = ""
    by_path = {}
    for num, title, path, lineno, numbered in common.printed_headings():
        by_path.setdefault(path, []).append((lineno, str(num)))
    for row in rows:
        path = os.path.join(root, row["path"])
        heads = by_path.get(path) or by_path.get(row["path"]) or []
        with open(path, encoding="utf-8") as fh:
            for i, line in enumerate(fh, start=1):
                for ln, num in heads:
                    if ln == i:
                        current = num
                pin = re.match(r"\s*\\unnumberedlabel\{([^}]*)\}\{([^}]*)\}", line)
                if pin:
                    out[pin.group(1)] = pin.group(2)
                    continue
                for m in re.finditer(r"\\label\{([^}]*)\}", line):
                    out[m.group(1)] = current
    return out


def cite(m):
    """\\autocite[III P2 Schol.]{spinoza1985collected} -> [@spinoza1985collected, III P2 Schol.]"""
    locator, keys = m.group(1), m.group(2)
    keys = ", ".join("@" + k.strip() for k in keys.split(","))
    return "[%s%s]" % (keys, ", " + locator if locator else "")


def inline(text, labels):
    """Commands that live inside a paragraph."""
    text = re.sub(
        r"\\(?:auto|paren|text|foot|super)?cite[a-z]*\s*(?:\[([^\]]*)\])?\{([^}]*)\}",
        cite, text)
    text = re.sub(r"\\ref\{([^}]*)\}",
                  lambda m: labels.get(m.group(1))
                  or re.sub(r"^(?:sec|ch):", "", m.group(1)),
                  text)
    text = re.sub(r"\\url\{([^}]*)\}", r"<\1>", text)
    text = re.sub(r"\\(?:emph|textit)\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", text)
    # \standing{...} is a note under a heading saying which of the foreword's
    # claims the text beneath it rests on. A blockquote, not italics: the book
    # sets it italic, but one of the eight notes contains an \emph and Markdown
    # does not nest emphasis, so italics here would swallow it.
    # Last, because its argument holds \emph and \ref whose braces have to go
    # first: running it earlier took the first nested } and ate it (D-422).
    text = re.sub(r"\\standing\{(.*)\}", r"> \1", text)
    for pattern in DROP_COMMANDS:
        text = re.sub(pattern, "", text)
    text = text.replace(r"\S", "§").replace("~", " ")
    for old, new in UNESCAPE.items():
        text = text.replace(old, new)
    return text


def table(lines, labels):
    """A tabular body -> a Markdown table. Column count comes from row one."""
    rows = []
    for line in lines:
        line = re.sub(r"\\\\(\[[^\]]*\])?\s*$", "", line.strip())
        line = inline(line, labels).strip()
        if not line:
            continue
        rows.append([c.strip() for c in line.split("&")])
    if not rows:
        return []
    width = len(rows[0])
    out = ["| " + " | ".join(rows[0]) + " |",
           "|" + "|".join([" --- "] * width) + "|"]
    for row in rows[1:]:
        row = (row + [""] * width)[:width]
        out.append("| " + " | ".join(row) + " |")
    return out


# Macros whose argument inline() converts, and which a hard wrap may have split
# across two lines. inline() runs per line, so a split argument reached the
# output verbatim: the unconverted-command warning named \emph for two sites a
# re-wrap had broken (D-422).
JOIN_ARGS = ("emph", "textit", "textbf", "ref", "autocite", "cite",
             "standing", "runin", "boxtitle", "url", "text")


def join_split_args(text):
    r"""Collapse newlines that fall inside a macro argument, at any brace depth.

    A first attempt used [^{}]* and stopped at the first nested brace, so
    \standing{... \emph{x} ...} joined only its first line (D-422).
    """
    head = re.compile(r"\\(?:" + "|".join(JOIN_ARGS) + r")\*?(?:\[[^\]]*\])?\{")
    out, i = [], 0
    while True:
        m = head.search(text, i)
        if not m:
            out.append(text[i:])
            return "".join(out)
        try:
            end = _matching_brace(text, m.start())
        except SystemExit:
            out.append(text[i:m.end()])
            i = m.end()
            continue
        out.append(text[i:m.start()])
        out.append(re.sub(r"\n[ \t]*", " ", text[m.start():end]))
        i = end


def render(path, num, root, labels):
    """One section file -> a list of Markdown lines."""
    text = open(os.path.join(root, path), encoding="utf-8").read()
    lines = join_split_args(text).split("\n")
    out, i, first_heading, stack = [], 0, True, []

    while i < len(lines):
        line = lines[i]
        i += 1

        m = re.match(r"\\(chapter|section|subsection|subsubsection)\*?\{(.*)\}\s*$", line)
        if m:
            kind, title = m.group(1), inline(m.group(2), labels).strip()
            starred = "*{" in line.split("{", 1)[0] + "{"
            prefix = ""
            if first_heading and num and num != "0" and not line.startswith("\\" + kind + "*"):
                prefix = num + ("." if kind == "chapter" else "") + " "
            out += ["", "#" * HEADING_DEPTH[kind] + " " + prefix + title, ""]
            first_heading = False
            continue

        m = re.match(r"\\(?:runin|paragraph|boxtitle)\{", line)
        if m:
            # The head may hold braces of its own (\runin{What \emph{hold} means}),
            # so it is read by matching the brace rather than to the line's last
            # one, and a run-in head may be followed by prose on the same source
            # line -- \runin ends with \par, so that prose is the next paragraph.
            # Eight of them are, in the assembled-offices section, and a regex
            # anchored at end-of-line left all eight unconverted (D-449).
            depth, j = 1, m.end()
            while j < len(line) and depth:
                depth += {"{": 1, "}": -1}.get(line[j], 0)
                j += 1
            head = "**" + inline(line[m.end():j - 1], labels).strip() + "**"
            rest = inline(line[j:], labels).strip()
            quoted = stack and stack[-1][0] == "quote"
            out += [">" if quoted else "",
                    ("> " + head) if quoted else head,
                    ">" if quoted else ""]
            if rest:
                out += [("> " + rest) if quoted else rest,
                        ">" if quoted else ""]
            continue

        if line.rstrip() == "\\appendix":
            continue                      # structure only; nothing to render

        m = re.match(r"\\begin\{(\w+)\}", line)
        if m:
            env = m.group(1)
            if env == "tabular":
                body = []
                while i < len(lines) and not lines[i].startswith(r"\end{tabular}"):
                    body.append(lines[i]); i += 1
                i += 1
                out += [""] + table(body, labels) + [""]
            elif env in ("center", "figure"):
                pass
            elif env in ("verse", "flushright", "esbox", "quote", "quotation"):
                stack.append(["quote", env, 0])
                out.append("")
            elif env == "enumerate":
                stack.append(["ol", env, 0]); out.append("")
            elif env in ("itemize", "description"):
                stack.append(["ul", env, 0]); out.append("")
            continue

        m = re.match(r"\\end\{(\w+)\}", line)
        if m:
            if stack and stack[-1][1] == m.group(1):
                stack.pop()
            out.append("")
            continue

        m = re.match(r"\s*\\item\s*(?:\[([^\]]*)\])?\s*(.*)$", line)
        if m:
            term, body = m.group(1), inline(m.group(2), labels).strip()
            if stack and stack[-1][0] == "ol":
                stack[-1][2] += 1
                bullet = "%d. " % stack[-1][2]
            else:
                bullet = "- "
            if term:
                body = "**" + inline(term, labels).strip().rstrip(":") + ":** " + body
            out.append(bullet + body)
            continue

        line = inline(line, labels)
        line = re.sub(r"\\\\(\[[^\]]*\])?\s*$", "  ", line)  # hard break
        if stack and stack[-1][0] == "quote":
            if line.strip():
                brk = "  " if line.endswith("  ") else ""
                out.append("> " + line.strip() + brk)
            else:
                out.append(">")
        else:
            out.append(line)

    return out


def squeeze(lines):
    """No more than one blank line in a row; no leading or trailing blanks."""
    out = []
    for line in lines:
        if not line.strip() and (not out or not out[-1].strip()):
            continue
        # A trailing double space is a Markdown hard break, not stray
        # whitespace: the verse epigraphs are the only place it matters.
        hard = line.endswith("  ") and line.strip()
        out.append(line.rstrip() + ("  " if hard else ""))
    while out and not out[-1].strip():
        out.pop()
    return out


# ---------------------------------------------------------------------------
# --tex: the book's own source, whole, in one file.
#
# The Markdown above converts; this does not. It assembles: book.tex with its
# three \input lines resolved -- preamble.tex, the generated draft-status.tex,
# and the sections -- and refs.bib carried inside a filecontents block, every
# file between markers naming its path. Nothing is rewritten except the
# \addbibresource path, which has to name the embedded copy instead of
# ../finishing/refs.bib.

INPUT_LINE = re.compile(r"^[ \t]*\\input\{([^}]*)\}[ \t]*$")


def skip_space(s, i):
    while i < len(s) and s[i] in " \t\r\n":
        i += 1
    return i


def skip_value(s, i):
    """Index just past a field value: a braced group, a quoted string, or a
    bare token. Braces nest, which is why this is not a regular expression --
    note fields carry them, as in 37{,}000."""
    if i >= len(s):
        return i
    if s[i] == "{":
        depth = 0
        while i < len(s):
            if s[i] == "{":
                depth += 1
            elif s[i] == "}":
                depth -= 1
                if depth == 0:
                    return i + 1
            i += 1
        return i
    if s[i] == '"':
        i += 1
        while i < len(s) and s[i] != '"':
            i += 1
        return i + 1
    while i < len(s) and s[i] not in ",}\n":
        i += 1
    return i


NOTE_FIELD = re.compile(r"(?:note|addendum)[ \t]*=", re.IGNORECASE)
# First letters NOTE_FIELD can start on, so the scan below can skip cheaply.
NOTE_FIRST = "nNaA"


def strip_notes(bib):
    """Remove every entry-level note-like field. Returns (text, fields removed).

    Two field names, not one: biblatex prints `note` AND `addendum` in the
    References, verified against the built HTML. Stripping only `note` left 30
    entries printing a note under a flag that said there would be none, 7 of
    them carrying the agent-verification sentences D-385 relabelled.

    Depth is counted from the file, so `note` is recognized only where a field
    name can stand -- directly inside an entry -- and not inside a title or a
    url that contains the word. A note left as the entry's last field leaves a
    trailing comma behind; biber accepts one, and taking it out would mean
    deciding which of two commas was the survivor.
    """
    out, i, depth, removed = [], 0, 0, 0
    while i < len(bib):
        ch = bib[i]
        if (depth == 1 and ch in NOTE_FIRST and NOTE_FIELD.match(bib, i)
                and not (i and (bib[i - 1].isalnum() or bib[i - 1] in "_-"))):
            j = skip_space(bib, bib.index("=", i) + 1)
            j = skip_value(bib, j)
            while j < len(bib) and bib[j] in " \t":
                j += 1
            if j < len(bib) and bib[j] == ",":
                j += 1
            while j < len(bib) and bib[j] in " \t":
                j += 1
            if j < len(bib) and bib[j] == "\n":
                j += 1
            while out and out[-1] in " \t":   # the indent already emitted
                out.pop()
            i, removed = j, removed + 1
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        out.append(ch)
        i += 1
    return "".join(out), removed


def bib_text(root, drop_notes):
    """finishing/refs.bib, with its note fields gone if asked. Returns
    (text, entries, notes removed)."""
    text = open(os.path.join(root, "finishing", "refs.bib"),
                encoding="utf-8").read()
    entries = len(re.findall(r"^@", text, flags=re.M))
    removed = 0
    if drop_notes:
        text, removed = strip_notes(text)
    return text, entries, removed


# The draft apparatus (D-319) -- the DRAFT watermark, the PREPRINT footer, the
# generated counts behind it and the comments explaining all three -- does not
# reach this output at all (D-335). It marks a page being proofed; this file is
# text handed to a reader, where a mark on every page is noise to discount, and
# a switch left in the preamble is a thing to read and wonder about. So it is
# removed rather than turned off, and the file says nothing about it.
#
# The rules below are about shape, not about a list of command names, and the
# gate after them is what makes that safe: nothing is written if a single word
# of the vocabulary survives. Add to the apparatus and the gate fails loudly
# naming what it found, which means teach these rules -- the same bargain the
# Markdown's unconverted-command warning strikes.

SECTIONS = "@@SECTIONS@@"

DRAFT_WORDS = re.compile(
    r"draftmode|draftstatus|draftwatermark|SetWatermark|watermark|"
    r"refschecked|refstotal|buildstamp|ds@|draft-status|PREPRINT|"
    r"WORKING MANUSCRIPT|human-checked|footer", re.IGNORECASE)


def _matching_fi(text, i):
    r"""Index just past the \fi closing the conditional that opens at i."""
    depth = 0
    for m in re.finditer(r"\\(if[a-zA-Z@]*|fi)\b", text[i:]):
        if m.group(1) == "fi":
            depth -= 1
            if depth == 0:
                return i + m.end()
        else:
            depth += 1
    raise SystemExit("render_markdown.py: unclosed conditional in the preamble")


def _matching_brace(text, i):
    """Index just past the } closing the group whose { is at or after i."""
    i = text.index("{", i)
    depth = 0
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise SystemExit("render_markdown.py: unclosed group in the preamble")


def strip_draft(text):
    r"""The preamble without the draft apparatus.

    Four shapes, in order. A \ifdraftmode conditional goes whole, wherever it
    sits and however it is spelled -- the watermark block, the two \fancyfoot
    lines, the title page's status line. A definition or hook whose body names
    the apparatus goes whole, by brace balance, because \draftstatusline and
    the \AtBeginDocument that computes the timestamp run to several lines. Then
    any remaining line whose code names it. Then any run of comment lines in
    which it is named, as a run, because the apparatus is explained in
    paragraphs and taking the sentences that name it out of one leaves prose
    about nothing.
    """
    while True:
        m = re.search(r"(?<!\\newif)\\ifdraftmode", text)
        if not m:
            break
        text = text[:m.start()] + text[_matching_fi(text, m.start()):]

    for opener in (r"\\newcommand\{\\draftstatusline\}", r"\\AtBeginDocument"):
        while True:
            m = re.search(opener, text)
            if not m:
                break
            end = _matching_brace(text, m.end())
            if not DRAFT_WORDS.search(text[m.start():end]):
                break
            text = text[:m.start()] + text[end:]

    kept, run = [], []
    for line in text.split("\n"):
        code = re.split(r"(?<!\\)%", line)[0]
        if line.lstrip().startswith("%"):
            run.append(line)
            continue
        if run:
            kept += [] if any(DRAFT_WORDS.search(c) for c in run) else run
            run = []
        if DRAFT_WORDS.search(code):
            continue
        kept.append(line)
    if run and not any(DRAFT_WORDS.search(c) for c in run):
        kept += run

    text = "\n".join(kept)
    text = re.sub(r"\\makeatletter\s*\\makeatother\s*", "", text)
    return re.sub(r"\n{3,}", "\n\n", text)


def rewrite_bibresource(line, bib_stem):
    r"""\addbibresource has to name the embedded copy, not ../finishing/refs.bib."""
    return re.sub(r"\\addbibresource\{[^}]*\}",
                  lambda _: r"\addbibresource{%s.bib}" % bib_stem, line)


def marked(path, body, label=None):
    """A file's contents between START and END markers naming its path."""
    head = "%%%% ===== START %s" % path
    if label:
        head += "  (%s)" % label
    return [head + " =====", body.rstrip("\n"),
            "%%%% ===== END %s =====" % path]


def sections_tex(root, rows):
    """Every section file, in ORDER.tsv order, between markers naming the file
    it came from. The markers are what the single file gives back of the split
    it flattens: the path a reader -- or whatever the file is pasted into --
    has to open to change the prose. They are LaTeX comments, so they cost the
    compiler nothing."""
    out = []
    for row in rows:
        out += [""] + marked(row["path"],
                             open(os.path.join(root, row["path"]),
                                  encoding="utf-8").read(),
                             "%s  %s" % (row["num"] or "--", row["title"]))
    return "\n".join(out)


def resolve_inputs(text, root, rows, bib_stem, seen=()):
    r"""Inline every line that is nothing but \input{...}.

    Line-wise on purpose: preamble.tex's own comments mention \input, and a
    pattern loose enough to match those would inline a comment. `sections` is
    special -- it resolves from ORDER.tsv rather than from the generated
    sections.tex, so the single file cannot be in an order the book is not.
    """
    out = []
    for line in text.split("\n"):
        m = INPUT_LINE.match(line)
        if not m:
            out.append(rewrite_bibresource(line, bib_stem))
            continue
        name = m.group(1)
        if name == "sections":
            out.append(SECTIONS)
            continue
        if name in seen:
            raise SystemExit("render_markdown.py: \\input loop at %s" % name)
        path = os.path.join(root, "manuscript", name)
        if not path.endswith(".tex"):
            path += ".tex"
        body = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, root)
        out += marked(rel, resolve_inputs(body, root, rows, bib_stem,
                                          tuple(seen) + (name,)))
    return "\n".join(out)


def render_tex(root, rows, stem, drop_notes, provenance):
    """The whole book as one .tex file."""
    bib, entries, removed = bib_text(root, drop_notes)
    master = open(os.path.join(root, "manuscript", "book.tex"),
                  encoding="utf-8").read()
    head = [
        "%% Antifascist Intelligence: Building Machines That Can Refuse",
        "%% Joshua G. Stern",
        "%%",
        "%%%% THE WHOLE BOOK AS ONE FILE. %s" % provenance,
        "%%%% %d sections, %d bibliography entries." % (len(rows), entries),
    ]
    if drop_notes:
        head += [
            "%%%% Note and addendum fields stripped, %d in all (--no-notes): the" % removed,
            "%% References print shorter here than in the book, and nothing else",
            "%% differs.",
        ]
    head += [
        "%%",
        "%% Every file is between START and END markers naming its path in the",
        "%% repository, so a passage can be traced back to the file that holds it.",
        "%%",
        "%% Disposable output, not a source. The manuscript is the LaTeX under",
        "%% manuscript/sections/, one file per section; nothing reads this file back,",
        "%% and an edit made here is lost the next time anyone runs the script.",
        "%%",
        "%% It also compiles as it stands -- lualatex -> biber -> lualatex twice, the",
        "%% sequence finishing/tools/build_tex.sh runs -- to the same page count and",
        "%% the same text as the book. The first lualatex writes",
        "%%%% %s.bib into the directory the compile runs in, from the" % stem,
        "%% filecontents block below; the name carries this file's own stem so that a",
        "%% compile started inside the repository cannot overwrite finishing/refs.bib.",
        "%% Five paragraphs break their last line differently, because concatenating",
        "%% the sections drops a space token that the book's own \\input contributes at",
        "%% each file boundary. Nothing else moves, and the proof PDF is built from",
        "%% manuscript/book.tex and not from here.",
        "",
        "%% ===== START finishing/refs.bib =====",
        r"\begin{filecontents}[overwrite,noheader]{%s.bib}" % stem,
        bib.rstrip("\n"),
        r"\end{filecontents}",
        "%% ===== END finishing/refs.bib =====",
        "",
    ]
    # The sections stand aside as a sentinel while the apparatus is stripped,
    # so neither the rules nor the gate ever read the book's own prose -- where
    # a word like "watermark" would be an ordinary word and not a mark on a page.
    body = strip_draft(resolve_inputs(master, root, rows, stem))
    left = [ln for ln in body.split("\n") if DRAFT_WORDS.search(ln)]
    if left:
        raise SystemExit(
            "render_markdown.py: the draft apparatus survived the strip, and "
            "nothing was written.\n  " + "\n  ".join(left[:10])
            + "\nTeach strip_draft() the shape it missed.")
    body = body.replace(SECTIONS, sections_tex(root, rows))
    return "\n".join(head) + body.rstrip("\n") + "\n", entries, removed


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tex", action="store_true",
                    help="write the book as one compilable LaTeX file, "
                         "bibliography included, instead of Markdown")
    ap.add_argument("--no-notes", action="store_true",
                    help="--tex only: strip every field that prints as a note "
                         "in the References -- note and addendum -- from every "
                         "bibliography entry")
    ap.add_argument("--out", help="output path "
                                  "(default: /tmp/<slug>_<date>.md, or .tex under --tex)")
    ap.add_argument("--check", action="store_true",
                    help="report what would be rendered and write nothing")
    args = ap.parse_args()

    if args.no_notes and not args.tex:
        # The Markdown carries no bibliography to strip, so the flag would do
        # nothing and say nothing. Refuse rather than accept it silently.
        ap.error("--no-notes applies to the bibliography, which only --tex carries")

    root = repo_root()
    rows = read_order(root)

    head = subprocess.run(["git", "-C", root, "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "-C", root, "status", "--porcelain"],
                           capture_output=True, text=True).stdout.strip()
    stamp = datetime.date.today().isoformat()
    provenance = ("Generated %s from %s%s by finishing/tools/render_markdown.py."
                  % (stamp, head or "an unknown commit",
                     " with uncommitted changes in the tree" if dirty else ""))

    out = args.out or os.path.join(
        "/tmp", "%s_%s.%s" % (SLUG, stamp, "tex" if args.tex else "md"))

    if args.tex:
        stem = os.path.splitext(os.path.basename(out))[0]
        text, entries, removed = render_tex(root, rows, stem, args.no_notes,
                                            provenance)
        print("%d sections, %d bibliography entries%s, %d KB"
              % (len(rows), entries,
                 ", %d note/addendum fields stripped" % removed if args.no_notes else "",
                 len(text.encode("utf-8")) // 1024), file=sys.stderr)
        if args.no_notes and not removed:
            print("WARNING: --no-notes removed nothing; refs.bib has no note or "
                  "addendum fields, or they are written in a shape "
                  "strip_notes() does not recognize.", file=sys.stderr)
    else:
        labels = label_map(root, rows)
        body = []
        for row in rows:
            body += render(row["path"], row["num"], root, labels)

        body = squeeze(body)
        front = [
            "# Antifascist Intelligence: Building Machines That Can Refuse",
            "",
            "Joshua G. Stern",
            "",
        ] + [
            "Rendered %s from %s%s, %d sections. Citations are keys into "
            "finishing/refs.bib; the bibliography, table of contents and page "
            "breaks are not reproduced. This file is disposable output, not a "
            "source: the manuscript is the LaTeX under manuscript/sections/."
            % (stamp, head or "an unknown commit",
               " with uncommitted changes in the tree" if dirty else "", len(rows)),
            "",
            "---",
            "",
        ]
        text = "\n".join(front + body) + "\n"

        leftover = sorted(set(re.findall(r"\\[a-zA-Z]+", text)))
        words = len(re.findall(r"\S+", "\n".join(body)))
        print("%d sections, %d words" % (len(rows), words), file=sys.stderr)
        if leftover:
            print("WARNING: unconverted LaTeX commands: " + " ".join(leftover),
                  file=sys.stderr)
            print("Teach them to render_markdown.py before trusting this file.",
                  file=sys.stderr)

    if args.check:
        return 0

    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(os.path.abspath(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
