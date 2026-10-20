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
title page, the typeset bibliography. Citations are footnotes, as the book sets
them (D-774): full at a work's first citation in a chapter, short after, with
the entry's note after its first full citation. Their text is biblatex's, not
this script's, taken from an HTML build of the tree as it stands (build_html.sh,
about a minute), so it cannot disagree with the proof (D-776). Each footnote is
matched to its citation by the keys the build leaves in it as HTML comments,
and a build of other sources stops the run. `--notes-from HTML` takes an
existing build instead; the keys guard the citations, not refs.bib, so an
entry edited since that build prints as it was. `--truncate N` cuts each
citation's footnote after N words and ends it with an ellipsis; the author's
own footnotes stay whole. `--keys` builds nothing and leaves each citation as a
Pandoc-style key ([@smith2020title]) into finishing/refs.bib.

Page-bottom notes (D-906): `\\note{...}` is the manuscript's footnote macro for
the prose that is not the spine. A note may hold paragraphs, lists and quotes,
and a citation or a \\footnote inside it is the next footnote in the chapter's
series. Here a note is a Pandoc note, its later paragraphs indented four
spaces, and a footnote inside it is a note of its own, numbered after it;
under --keys a citation inside it stays a key. The HTML-based footnotes assume
the build's notes come in the sources' order, which the nesting may not give;
when they disagree the run stops and names --keys. `--chapters` prints one
line per chapter of body words and note words, headings left out, and the
totals before and after the appendices: the spine's measure, in the tree.

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
    finishing/tools/render_markdown.py --truncate 30   # ... notes cut at 30 words
    finishing/tools/render_markdown.py --keys       # ... citations as [@key]
    finishing/tools/render_markdown.py --tex        # -> /tmp/<slug>_<date>.tex
    finishing/tools/render_markdown.py --tex --no-notes   # ... minus bib notes
    finishing/tools/render_markdown.py --out PATH
    finishing/tools/render_markdown.py --check      # report only, write nothing
"""

import argparse
import csv
import datetime
import html.parser
import os
import re
import shutil
import subprocess
import sys
import tempfile

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
    # The epigraph page (D-621): a page of its own in the book, nothing here.
    r"\\clearpage",
    r"\\thispagestyle\{[^}]*\}",
    r"\\vspace\*?\{[^}]*\}",
]

# Footnotes, numbered through the whole book and set as Pandoc notes. inline()
# swaps each for its marker and queues its text; render() writes the queue after
# the file's last line, which Pandoc accepts anywhere in the document (D-623).
FOOTNOTES = {"n": 0, "pending": []}

# The footnotes of an HTML build, in document order, when the citations are
# set as the book sets them (D-776): `queue` holds one (keys, segments) pair per
# footnote, `next` the index of the next one to take, `truncate` the word limit
# for a citation's footnote, or None. `queue` is None under --keys.
NOTES = {"queue": None, "next": 0, "truncate": None}

# \part numbers, counted in reading order as LaTeX counts them.
PARTS = {"n": 0}
FIGURES = {}  # chapter number -> figures so far, for "Figure 24.1"
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

# Escaped characters, restored to themselves.
UNESCAPE = {r"\$": "$", r"\%": "%", r"\&": "&", r"\#": "#", r"\_": "_"}


def book_title(root):
    """"Title: Subtitle", read from book.tex's two macros. It was a literal here,
    and kept a subtitle book.tex had dropped (D-623)."""
    tex = open(os.path.join(root, "manuscript", "book.tex"), encoding="utf-8").read()
    get = lambda name: re.search(r"\\newcommand\{\\%s\}\{(.*)\}\s*$" % name, tex, re.M).group(1)
    return "%s: %s" % (get("booktitlemain"), get("booksubtitle"))


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
        aux records (ch:preface -> 0, ch:glossary -> 18).
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


CITE_GROUP = re.compile(r"((?:\[[^\]]*\]){0,2})\{([^}]*)\}")


def cite(m):
    """\\autocite[III P2 Schol.]{spinoza1985collected} -> [@spinoza1985collected, III P2 Schol.]

    The multicite forms (\\autocites and kin) take one optional-argument set
    and one key group per cited work: \\autocites[ch.~9]{a}{b} is two cites, the
    locator belonging to the first. Until this read every group, the pattern
    stopped at the first and left the rest in the prose as `{b}`. Groups are
    joined with `;`, Pandoc's separator between cites. The keys within a group
    are joined with `;` too: Pandoc reads a comma after a key as the start of a
    locator, so `[@a, @b]` was one cite of a with "@b" as its locator. A
    group's postnote follows its last key, where biblatex prints it. Two
    brackets are biblatex's [prenote][postnote]; one is the postnote.
    """
    parts = []
    for g in CITE_GROUP.finditer(m.group(1)):
        notes = re.findall(r"\[([^\]]*)\]", g.group(1))
        pre, post = notes if len(notes) == 2 else ("", notes[0] if notes else "")
        keys = "; ".join("@" + k.strip() for k in g.group(2).split(","))
        parts.append((pre + " " if pre else "") + keys + (", " + post if post else ""))
    return "[%s]" % "; ".join(parts)


CITE_CMD = re.compile(
    r"\\(?:auto|paren|text|foot|super)?cite(?:s(?=\s*[\[{]))?\*?"
    r"((?:\s*(?:\[[^\]]*\]){0,2}\{[^}]*\})+)")


def cite_keys(args):
    """The keys of one citation command, in order, from its argument groups."""
    return [k.strip() for g in CITE_GROUP.finditer(args)
            for k in g.group(2).split(",")]


def take_note(keys, what, text):
    """The next footnote of the HTML build, which must cite `keys`.

    The build and the sources are walked in the same order, and each footnote
    is checked against the citation it is taken for by the keys the build left
    in it (the preamble writes them as HTML comments under tex4ht). A build of
    other sources fails here instead of setting a note against the wrong
    citation."""
    q, i = NOTES["queue"], NOTES["next"]
    if i >= len(q):
        raise SystemExit("render_markdown.py: the sources have more footnotes "
                         "than the HTML build's %d; the build is not of these "
                         "sources. At: %s" % (len(q), text[:120]))
    got, segs = q[i]
    if got != keys:
        raise SystemExit("render_markdown.py: footnote %d is a %s citing %s in "
                         "the sources and cites %s in the HTML build; the build "
                         "is not of these sources. At: %s"
                         % (i + 1, what, keys or "nothing", got or "nothing",
                            text[:120]))
    NOTES["next"] += 1
    return segs


def take_own_note(inner):
    """Under an HTML build, a note's own footnote, which comes before the
    footnotes of its citations (D-906).

    The preamble sets a citation or a footnote inside a note as the next
    footnote in the series, so the build's footnote for the note cites
    nothing, and what it holds comes after it, in the order the sources hold
    it. The note's text is rendered from the sources, as in --keys, and its
    citations take the build's footnotes that follow. A note is matched by
    position, so its opening words, up to the first command, are checked
    against the build's."""
    segs = take_note([], "note", inner)
    want = re.sub(r"\W+", "", re.split(r"\\", inner)[0].lower())[:30]
    got = re.sub(r"\W+", "", render_segments(segs, None).lower())
    if len(want) >= 8 and want not in got:
        raise SystemExit("render_markdown.py: footnote %d in the HTML build "
                         "does not read as the sources' note there: %s"
                         % (NOTES["next"], inner[:120]))


def footnotes(text, labels):
    """\\footnote{...} -> [^n], its text converted and queued. Braces matched,
    because a note can hold a \\autocite of its own.

    With an HTML build's footnotes loaded (NOTES), a citation outside a
    footnote is a footnote too, as the book sets it (D-774), and both kinds
    take their text from the build, in the order they occur. The marker
    follows the punctuation after the citation and drops the space before it,
    as biblatex places it. A note's own citations are footnotes of their own
    in the build, after the note's (D-906); take_own_note() takes the note's,
    its text is rendered from the sources, and its citations take theirs."""
    notes = NOTES["queue"] is not None
    pat = re.compile(NOTE_OPEN.pattern + ("|" + CITE_CMD.pattern if notes else ""))
    out, i = "", 0
    while True:
        m = pat.search(text, i)
        if not m:
            return out + text[i:]
        FOOTNOTES["n"] += 1
        n = FOOTNOTES["n"]
        if m.group(0).endswith("note{"):
            end = _matching_brace(text, m.start())
            inner = text[m.end():end - 1]
            # A footnote inside this note is queued while the body is
            # converted; the carrier goes in ahead of it (D-906).
            slot = len(FOOTNOTES["pending"])
            if notes:
                take_own_note(inner)
            body = inline(inner, labels).strip()
            out += text[i:m.start()] + "[^%d]" % n
            i = end
            FOOTNOTES["pending"].insert(slot, "[^%d]: %s" % (n, body))
        else:
            segs = take_note(cite_keys(m.group(1)), "citation", m.group(0))
            body = render_segments(segs, NOTES["truncate"])
            out = (out + text[i:m.start()]).rstrip()
            i = m.end()
            if i < len(text) and text[i] in ".,;:!?":
                out += text[i]
                i += 1
            out += "[^%d]" % n
            FOOTNOTES["pending"].append("[^%d]: %s" % (n, body))


class _NoteParser(html.parser.HTMLParser):
    """One footnote of tex4ht's HTML -> the cited keys and a list of
    (text, style) segments, style one of "", "i", "b", "sup", "url" (text the
    address). The footnote's own number is dropped; small capitals (url, doi,
    isbn) are set as capitals; tex4ht sets a superscript in mathematics (the
    10^25 of the compute thresholds) in a 6-point font and not in <sup>."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.keys, self.segs, self.stack = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class") or ""
        style = ""
        if "footnote-mark" in cls:
            style = "skip"
        elif tag == "a" and "url" in cls.split():
            style = "url"
            self.segs.append((a.get("href", ""), "url"))
        elif tag == "sup" or re.search(r"\bcmr-[5-7]\b", cls):
            style = "sup"
        elif re.search(r"lmri|lmsi|-it\b", cls):
            style = "i"
        elif "lmbx" in cls:
            style = "b"
        elif "small-caps" in cls:
            style = "caps"
        self.stack.append((tag, style))

    def handle_startendtag(self, tag, attrs):
        if tag == "br":
            self.handle_data(" ")

    def handle_endtag(self, tag):
        while self.stack:
            if self.stack.pop()[0] == tag:
                break

    def handle_comment(self, data):
        data = data.strip()
        if data.startswith("cite:"):
            self.keys.append(data[len("cite:"):].strip())

    def handle_data(self, data):
        styles = [st for _, st in self.stack if st]
        if "skip" in styles or "url" in styles:
            return
        style = styles[-1] if styles else ""
        if style == "caps":
            data, style = data.upper(), ""
        self.segs.append((re.sub(r"\s+", " ", data), style))


def load_notes(path):
    """Every footnote of an HTML build, in document order, as (keys, segments)."""
    page = open(path, encoding="utf-8").read()
    asides = re.findall(r"<aside class='footnotetext'[^>]*>(.*?)</aside>",
                        page, re.S)
    if not asides:
        raise SystemExit("render_markdown.py: no footnotes in %s" % path)
    if not re.search(r"<!--\s*cite:", page):
        raise SystemExit("render_markdown.py: %s carries no citation keys; it "
                         "was built before the preamble wrote them (D-776). "
                         "Rebuild it, or leave out --notes-from." % path)
    notes = []
    for a in asides:
        p = _NoteParser()
        p.feed(a)
        p.close()
        segs = []
        for text, style in p.segs:          # adjacent runs of one style merge
            if segs and segs[-1][1] == style and style != "url":
                segs[-1] = (segs[-1][0] + text, style)
            else:
                segs.append((text, style))
        if segs:
            segs[0] = (segs[0][0].lstrip(), segs[0][1])
        notes.append((p.keys, segs))
    return notes


def render_segments(segs, limit):
    """Segments -> one line of Markdown. Under `limit`, only the first `limit`
    words, an address counting as one, and an ellipsis where the cut fell;
    a note no longer than that is left whole."""
    words = sum(1 if st == "url" else len(t.split()) for t, st in segs)
    cut = limit is not None and words > limit
    out, left = [], limit if cut else None
    for text, style in segs:
        if left is not None:
            if left <= 0:
                break
            if style == "url":
                left -= 1
            else:
                toks = re.findall(r"\s*\S+", text)
                if len(toks) > left:
                    text = "".join(toks[:left])
                left -= len(toks)
        if style == "url":
            out.append("<%s>" % text)
            continue
        # A literal asterisk (the "FAT* 2018" of a proceedings title) would
        # open or close emphasis; escaped, it prints as itself.
        text = text.replace("*", "\\*")
        core = text.strip()
        if not core or not style:
            out.append(text)
            continue
        mark = {"i": "*", "b": "**", "sup": "^"}[style]
        lead = text[:len(text) - len(text.lstrip())]
        trail = text[len(text.rstrip()):]
        out.append(lead + mark + core + mark + trail)
    body = re.sub(r" {2,}", " ", "".join(out)).strip()
    if cut:
        body = body.rstrip(",;:").rstrip() + " …"
    return body


def inline(text, labels):
    """Commands that live inside a paragraph."""
    text = footnotes(text, labels)
    text = CITE_CMD.sub(cite, text)
    text = re.sub(r"\\ref\{([^}]*)\}",
                  lambda m: labels.get(m.group(1))
                  or re.sub(r"^(?:sec|ch):", "", m.group(1)),
                  text)
    text = re.sub(r"\\url\{([^}]*)\}", r"<\1>", text)
    text = re.sub(r"\\(?:emph|textit)\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", text)
    text = re.sub(r"\\textsuperscript\{([^}]*)\}", r"^\1^", text)
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
        # longtable's furniture (D-621): a rule after every row, and the
        # header-repeat marker. Gone before the row break is looked for, which
        # it would otherwise hide.
        line = re.sub(r"\\hline|\\endhead|\\endfirsthead", "", line).strip()
        line = re.sub(r"\\\\(\[[^\]]*\])?\s*$", "", line).strip()
        if not line:
            continue
        # Split on the column separator BEFORE inline() restores an escaped \&
        # to a bare one, or a cell holding "R\&D" became two cells.
        cells = re.split(r"(?<!\\)&", line)
        rows.append([inline(c, labels).strip().replace("|", "\\|") for c in cells])
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
# re-wrap had broken (D-422). A note's argument is not joined: its lines are
# paragraphs, and render_lines() reads it as a block (D-906).
JOIN_ARGS = ("emph", "textit", "textbf", "ref", "autocite", "cite",
             "standing", "runin", "boxtitle", "url", "text",
             "textsuperscript", "part")


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


def printed_numbers():
    """path -> the printed number of each numbered heading in it, in order.

    From the same counter simulation the generated table of contents is built
    from (D-406). Starred headings are left out: they print no number, and the
    value \\unnumberedlabel pins for the Foreword and the glossary is what a
    \\ref to one yields, not something the page shows.
    """
    out = {}
    for num, _title, path, _lineno, numbered in common.printed_headings():
        if numbered:
            out.setdefault(path, []).append(str(num))
    return out


def render(path, nums, root, labels):
    """One section file -> a list of Markdown lines.

    `nums` is the printed number of each numbered heading in the file, in the
    order they appear -- NOT ORDER.tsv's `num`. D-406 made that an identity
    that stops describing a file's position the moment the file moves, and
    D-422 rebuilt the cross-references on the printed number and left the
    headings on the identity, so the export printed "## 14. Custody" over the
    chapter the book numbers 4 and resolved a reference inside it to 6: one
    file disagreeing with itself. A list and not a single value because a file
    can carry more than one heading -- survives.tex holds a chapter and three
    sections, and prefixing only the first left those three unnumbered.
    """
    text = open(os.path.join(root, path), encoding="utf-8").read()
    # A part epigraph (\partepigraph{...}, which the preamble sets on the part's
    # title page) is a quote under the part heading, which in Markdown is
    # what a quote environment already renders as.
    while "\\partepigraph{" in text:
        start = text.index("\\partepigraph{")
        end = _matching_brace(text, start)
        body = text[text.index("{", start) + 1:end - 1].strip("\n")
        text = (text[:start] + "\\begin{quote}\n" + body + "\n\\end{quote}"
                + text[end:])
    # A part intro (\partintro{...}, D-921) is a paragraph of the book's own
    # prose on the same page, so it renders as one, after the part heading.
    while "\\partintro{" in text:
        start = text.index("\\partintro{")
        end = _matching_brace(text, start)
        body = text[text.index("{", start) + 1:end - 1].strip("\n")
        text = text[:start] + "\n" + body + "\n" + text[end:]
    # A comment that starts mid-line takes the rest of the line and the
    # newline after it, and TeX skips the next line's leading spaces, so the
    # two lines are one. §19.3 carries one, a note that a citation is owed,
    # and it reached the Markdown as prose. A whole-line comment is left to
    # the loop below.
    text = re.sub(r"^(?!\s*%)(.*?)(?<!\\)%[^\n]*\n[ \t]*", r"\1", text,
                  flags=re.M)
    lines = join_split_args(text).split("\n")
    out = render_lines(lines, list(nums), labels, path, nums)
    if FOOTNOTES["pending"]:
        for note in FOOTNOTES["pending"]:
            out += ["", note]
        out.append("")
        FOOTNOTES["pending"] = []
    return out


NOTE_OPEN = re.compile(r"\\(?:foot)?note\{")


def note_def(n, md_lines):
    """A Pandoc note from rendered lines: the first on the marker's line, the
    rest indented four spaces, blank lines kept, so the note holds its
    paragraphs, lists and quotes (D-906)."""
    md_lines = squeeze(md_lines)
    if not md_lines:
        return "[^%d]:" % n
    out = ["[^%d]: %s" % (n, md_lines[0])]
    out += [("    " + l) if l.strip() else "" for l in md_lines[1:]]
    return "\n".join(out)


def render_lines(lines, heads, labels, path, nums):
    """Lines of a section file, or of a note inside one, to Markdown lines.

    `heads` is the printed number of each numbered heading still to come, in
    order; a note's lines carry none. The queue of notes is flushed by
    render(), once per file, so a note rendered here keeps its place.
    """
    out, i, stack = [], 0, []

    while i < len(lines):
        line = lines[i]
        i += 1

        # A whole-line LaTeX comment is not prose and reached the Markdown as
        # prose: the four lines explaining the \appendix continuation file and
        # the six explaining the preface's sloppypar. Only a line whose first
        # non-space character is an unescaped % is dropped; one that starts
        # mid-line went above. --tex keeps them, being the source rather than
        # a rendering of it.
        if re.match(r"\s*%", line):
            continue

        # A note whose argument runs past its line (D-906): \note{ or
        # \footnote{ opened here and closed on a later line. Its lines are
        # rendered by this same loop, so a list, a quote or a lead-in inside
        # it comes out as it does in the body, and the result is queued as a
        # Pandoc note, numbered before anything nested in it. The host line
        # keeps the marker and whatever follows the closing brace, and goes
        # on through the rules below.
        while True:
            hit = None
            for m in NOTE_OPEN.finditer(line):
                rest = line + "\n" + "\n".join(lines[i:])
                end = _matching_brace(rest, m.start())
                if end > len(line):
                    hit = (m, rest, end)
                    break
            if not hit:
                break
            m, rest, end = hit
            inner = rest[m.end():end - 1]
            tail = rest[end:].split("\n", 1)[0]
            i += rest[:end].count("\n")
            # A note or citation earlier on the line is numbered first, as the
            # page numbers them; a single-line note after the closing brace
            # is left to inline(), and a second block note there comes round
            # again.
            prefix = footnotes(line[:m.start()], labels)
            FOOTNOTES["n"] += 1
            n = FOOTNOTES["n"]
            slot = len(FOOTNOTES["pending"])
            if NOTES["queue"] is not None:
                take_own_note(inner.strip())
            body = render_lines(inner.strip("\n").split("\n"), [], labels,
                                path, nums)
            FOOTNOTES["pending"].insert(slot, note_def(n, body))
            line = prefix + "[^%d]" % n + tail

        m = re.match(r"\\(chapter|section|subsection|subsubsection)\*?(?:\[[^\]]*\])?\{(.*)\}\s*$", line)
        if m:
            kind, title = m.group(1), inline(m.group(2), labels).strip()
            prefix = ""
            if not line.startswith("\\" + kind + "*"):
                if heads:
                    prefix = heads.pop(0) + ("." if kind == "chapter" else "") + " "
                else:
                    # Degrade to an unnumbered heading rather than to a wrong
                    # number, and say so: the two heading patterns, this one and
                    # common.HEAD_RE, have to agree for the numbers to line up.
                    print("WARNING: %s: no printed number left for heading %r, "
                          "rendered without one; this pattern and "
                          "common.HEAD_RE disagree about what a heading is."
                          % (path, title), file=sys.stderr)
            out += ["", "#" * HEADING_DEPTH[kind] + " " + prefix + title, ""]
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

        # The table wrapper (D-621): font size and row spacing, nothing to render.
        if line.startswith(("\\begingroup", "\\endgroup")):
            continue

        m = re.match(r"\\part\{(.*)\}\s*$", line)
        if m:
            # Above a chapter's "##", so "#", the depth of the book's title. A
            # Part is the one division larger than a chapter, and Markdown has
            # no level between the two.
            PARTS["n"] += 1
            out += ["", "# Part %s — %s" % (ROMAN[PARTS["n"] - 1],
                                           inline(m.group(1), labels).strip()), ""]
            continue

        # An unnumbered Part (D-984): the closing heading over the last
        # chapter, set at the same depth as a Part, with no numeral.
        m = re.match(r"(?:\\cleardoublepage\\phantomsection\\addcontentsline\{toc\}\{part\}\{.*\})?\\part\*\{(.*)\}\s*$", line)
        if m:
            out += ["", "# %s" % inline(m.group(1), labels).strip(), ""]
            continue
        if re.match(r"\\cleardoublepage\\phantomsection\\addcontentsline\{toc\}\{part\}\{.*\}\s*$", line):
            continue

        # A figure (D-894) is TikZ, which Markdown can't draw. Its picture is
        # skipped, with the scaffolding around it, and its caption is printed
        # with the figure's number, as the book prints it: the chapter's
        # number and the figure's place in the chapter.
        # The \def and \makebox before it end in %, so the comment handling
        # above has already joined them to the \begin line.
        if "\\begin{tikzpicture}" in line:
            while i < len(lines) and not lines[i].startswith("\\end{tikzpicture}"):
                i += 1
            i += 1
            continue
        if line.startswith("\\caption{"):
            body = line[len("\\caption{"):_matching_brace(line, 0) - 1]
            chap = (list(nums) or ["?"])[0].split(".")[0]
            FIGURES[chap] = FIGURES.get(chap, 0) + 1
            out += ["", "**Figure %s.%d.** %s *(A diagram, drawn in the PDF and the HTML.)*"
                    % (chap, FIGURES[chap], inline(body, labels).strip()), ""]
            continue

        m = re.match(r"\\begin\{(\w+)\}", line)
        if m:
            env = m.group(1)
            if env in ("tabular", "longtable"):
                body = []
                while i < len(lines) and not lines[i].startswith(r"\end{%s}" % env):
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
            # An explicit number on an enumerate item is the item's number
            # (D-621 writes every one as \item[N.]); printing it as a bold label
            # after the list's own counter set "1. **1.**" 84 times. A lettered
            # one, 6a, is no Markdown list number, so it becomes a paragraph
            # inside the item before it, keeping its label (D-623).
            if stack and stack[-1][0] == "ol" and term and re.fullmatch(r"\d+[a-z]*\.", term.strip()):
                t = term.strip()
                if t[:-1].isdigit():
                    stack[-1][2] = int(t[:-1])
                    out.append("%s %s" % (t, body))
                else:
                    out += ["", "   **%s** %s" % (t, body)]
                continue
            if stack and stack[-1][0] == "ol":
                stack[-1][2] += 1
                bullet = "%d. " % stack[-1][2]
            else:
                bullet = "- "
            if term:
                # A label that already ends in a sentence mark punctuates
                # itself. Appending the colon unconditionally set the preface's
                # chapter map as "**1, Twenty Seconds.:**". The description
                # labels in the formation chapter end in a colon and are
                # unaffected.
                t = inline(term, labels).strip()
                tail = "" if t.endswith((".", "?", "!")) else ":"
                body = "**" + t.rstrip(":") + tail + "** " + body
            out.append(bullet + body)
            continue

        # A \par ending a source line ends the paragraph there. The fields of
        # the birth record in chapter 31 are written one to a line that way,
        # and inline() dropping the \par ran all eight into one paragraph.
        par = bool(re.search(r"\\par\s*$", line))
        line = inline(line, labels)
        line = re.sub(r"\\\\(\[[^\]]*\])?\s*$", "  ", line)  # hard break
        if stack and stack[-1][0] == "quote":
            if line.strip():
                brk = "  " if line.endswith("  ") else ""
                out.append("> " + line.strip() + brk)
            else:
                out.append(">")
            if par:
                out.append(">")
        else:
            out.append(line)
            if par:
                out.append("")

    return out


def is_note_line(line):
    """A Pandoc note's lines: the marker line, and the continuation lines
    indented four spaces under it (D-906). Nothing else this script writes
    starts with four spaces."""
    return bool(re.match(r"\[\^\d+\]:", line)) or line.startswith("    ")


def chapter_table(flat):
    """One TSV line per chapter, body words and note words with the headings
    left out, then the totals before and after the appendices: the measure
    of the spine (D-906). `flat` is the rendered body, one string per line."""
    counts, order, cur = {}, [], None
    for line in flat:
        m = re.match(r"## (Preface|Glossary|\d+|[A-H])\b", line)
        if m:
            cur = m.group(1)
            if cur not in counts:
                counts[cur] = [0, 0]
                order.append(cur)
            continue
        if line.startswith("#") or cur is None:
            continue
        # Words a reader reads: a note's marker and a citation's key under
        # --keys are apparatus, not words, and are left out here.
        prose = re.sub(r"\[\^\d+\]|\[@[^\]]*\]", "", line)
        prose = re.sub(r"\s+([.,;:!?)])", r"\1", prose)   # "court ." after a key
        counts[cur][1 if is_note_line(line) else 0] += len(prose.split())
    out = ["chapter\tbody\tnotes"]
    out += ["%s\t%d\t%d" % (c, counts[c][0], counts[c][1]) for c in order]
    for name, pick in (("main text before appendices", lambda c: not re.fullmatch(r"[A-H]|Glossary", c)),
                       ("appendices", lambda c: re.fullmatch(r"[A-H]", c))):
        out.append("%s\t%d\t%d" % (name,
                                   sum(counts[c][0] for c in order if pick(c)),
                                   sum(counts[c][1] for c in order if pick(c))))
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
    r"WORKING MANUSCRIPT|human-checked|footer|"
    r"refcheckedkey|refok@|refunchecked|ref-unchecked|draft:cite", re.IGNORECASE)


def _matching_fi(text, i):
    r"""Index just past the \fi closing the conditional that opens at i.

    A test that takes its branches as braced arguments -- etoolbox's \ifcsdef,
    biblatex's \iffieldundef -- closes with its last brace and has no \fi, so
    it is not counted: an \if-name followed by an opening brace is skipped
    (D-641, when the citation highlight put an \ifcsdef inside \ifdraftmode).
    """
    depth = 0
    for m in re.finditer(r"\\(fi)\b|\\(if[a-zA-Z@]*)(?![a-zA-Z@])(?!\s*\{)", text[i:]):
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
    raise SystemExit("render_markdown.py: unclosed brace group at: %s"
                     % text[text.index("{", i) - 60 if text.index("{", i) > 60 else 0:
                            text.index("{", i) + 80].replace("\n", " "))


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
    # The title page's verification sentence (D-922) is the book's and not the
    # apparatus's: it stays, with the two generated counts it prints written
    # in as the numbers they were at this render, so the gate below has no
    # word of the vocabulary to find in it.
    counts = dict(re.findall(r"\\newcommand\{\\(refschecked|refstotal)\}\{(\d+)\}", text))
    m = re.search(r"\\providecommand\{\\bookverification\}", text)
    if m and counts:
        end = _matching_brace(text, m.end())
        body = re.sub(r"\\(refschecked|refstotal)(\\ |\{\}|(?=[^a-zA-Z]))",
                      lambda mm: counts[mm.group(1)] + (" " if mm.group(2) == "\\ " else ""),
                      text[m.start():end])
        text = text[:m.start()] + body + text[end:]

    while True:
        m = re.search(r"(?<!\\newif)\\ifdraftmode", text)
        if not m:
            break
        text = text[:m.start()] + text[_matching_fi(text, m.start()):]

    for opener in (r"\\newcommand\{\\draftstatusline\}", r"\\newcommand\{\\draftstampline\}",
                   r"\\AtBeginDocument"):
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
    compiler nothing.

    The number beside the title is the one the page prints, simulated from the
    counters, and not ORDER.tsv's `num` -- which is a file's identity and has
    not tracked its position since D-406, so 77 of the 97 markers named a
    number the book does not print there and 38 of those named a real number
    belonging to a different file (D-468). A file whose heading is starred and
    a continuation file with no heading both print no number and are marked
    `--`; a file with more than one heading is marked with the first, the one
    the marker opens on."""
    heads = printed_numbers()
    out = []
    for row in rows:
        nums = heads.get(row["path"])
        label = "%s  %s" % (nums[0] if nums else "--", row["title"])
        out += [""] + marked(row["path"],
                             open(os.path.join(root, row["path"]),
                                  encoding="utf-8").read(),
                             label if label.strip("- ") else None)
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
        "%% Antifascist Intelligence: Building Machines That Have Feelings, why no one will know if it works, why not to attempt it, and why if you insist on doing it anyway you should be democratic socialist about it I wrote this with LLMs",
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
        "%% The number beside the title in a marker is the one the page prints; a",
        "%% heading that prints no number is marked --.",
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
    ap.add_argument("--keys", action="store_true",
                    help="Markdown only: leave each citation as a Pandoc key "
                         "into finishing/refs.bib instead of building the HTML "
                         "for its footnote")
    ap.add_argument("--notes-from", metavar="HTML",
                    help="Markdown only: take the footnotes from this HTML "
                         "build (build_html.sh's book.html, or a proof's) "
                         "instead of building one")
    ap.add_argument("--truncate", type=int, metavar="N",
                    help="Markdown only: cut each citation's footnote after N "
                         "words and end it with an ellipsis; the author's own "
                         "footnotes are left whole")
    ap.add_argument("--chapters", action="store_true",
                    help="Markdown only: print, on stdout, one line per chapter "
                         "of body words and note words, headings left out, and "
                         "the totals before and after the appendices")
    args = ap.parse_args()

    if args.tex and (args.keys or args.notes_from or args.truncate is not None
                     or args.chapters):
        ap.error("--keys, --notes-from, --truncate and --chapters apply to the Markdown, not --tex")
    if args.keys and (args.notes_from or args.truncate is not None):
        ap.error("--keys sets no footnotes, so --notes-from and --truncate do nothing with it")
    if args.truncate is not None and args.truncate < 1:
        ap.error("--truncate takes a positive number of words")

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
        numbers = printed_numbers()
        if not args.keys:
            if args.notes_from:
                NOTES["queue"] = load_notes(args.notes_from)
            else:
                # The footnotes are biblatex's, as the HTML proof sets them,
                # so they come from a build of the tree as it stands (D-776).
                build = tempfile.mkdtemp(prefix="render-md-")
                print("building the HTML for the footnotes (about a minute)",
                      file=sys.stderr)
                try:
                    r = subprocess.run(
                        [os.path.join(root, "finishing", "tools", "build_html.sh"),
                         build], capture_output=True, text=True, cwd=root)
                    if r.returncode:
                        raise SystemExit("render_markdown.py: build_html.sh "
                                         "failed:\n" + r.stdout + r.stderr)
                    if "WARNING" in r.stdout:
                        print(r.stdout.strip(), file=sys.stderr)
                    NOTES["queue"] = load_notes(os.path.join(build, "book.html"))
                finally:
                    shutil.rmtree(build, ignore_errors=True)
            NOTES["truncate"] = args.truncate
        body = []
        for row in rows:
            body += render(row["path"], numbers.get(row["path"], []), root, labels)
        if NOTES["queue"] is not None and NOTES["next"] != len(NOTES["queue"]):
            raise SystemExit("render_markdown.py: the HTML build has %d footnotes "
                             "and the sources account for %d; the build is not "
                             "of these sources, or its notes are not in the "
                             "sources' order (a footnote inside a note). "
                             "--keys renders from the sources alone."
                             % (len(NOTES["queue"]), NOTES["next"]))
        if args.keys:
            cites = ("Citations are keys into finishing/refs.bib; the "
                     "bibliography, ")
        else:
            cites = ("Citations are footnotes, as the book's HTML build sets "
                     "them%s; the bibliography, "
                     % ("" if args.truncate is None else
                        ", each cut after %d words where it ran longer, an "
                        "ellipsis marking the cut" % args.truncate))

        body = squeeze(body)
        front = [
            "# " + book_title(root),
            "",
            "Joshua G. Stern",
            "",
        ] + [
            ("Rendered %s from %s%s, %d sections. "
             % (stamp, head or "an unknown commit",
                " with uncommitted changes in the tree" if dirty else "", len(rows)))
            + cites + "table of contents and page breaks are not reproduced. "
            "This file is disposable output, not a source: the manuscript is "
            "the LaTeX under manuscript/sections/.",
            "",
            "---",
            "",
        ]
        text = "\n".join(front + body) + "\n"

        leftover = sorted(set(re.findall(r"\\[a-zA-Z]+", text)))
        # The text's words, not its notes', so the count stays comparable
        # with and without the footnotes. A queued note is one string, with
        # its later paragraphs on lines of its own, so the body is split to
        # lines first.
        flat = "\n".join(body).split("\n")
        words = len(re.findall(r"\S+", "\n".join(
            l for l in flat if not is_note_line(l))))
        print("%d sections, %d words" % (len(rows), words), file=sys.stderr)
        if args.chapters:
            print("\n".join(chapter_table(flat)))
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
