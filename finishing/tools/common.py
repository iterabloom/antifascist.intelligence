"""Shared helpers: heading parsing and the manuscript dialect."""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTLINE_ODS = os.path.join(
    REPO, "personas", "section-assignments",
    "superintelligence-ethics-outline_v3b_2024-07-07.ods")
TOC_TXT = os.path.join(REPO, "manuscript", "table-of-contents.txt")
SECTIONS = os.path.join(REPO, "manuscript", "sections")
OUTLINE_TSV = os.path.join(REPO, "finishing", "outline.tsv")
LEDGER_TSV = os.path.join(REPO, "finishing", "ledger.tsv")
REPORTS = os.path.join(REPO, "finishing", "reports")

CHAPTER_RE = re.compile(r"^Chapter (\d+): (.+)$")
SECTION_RE = re.compile(r"^(\d+(?:\.\d+)+)\.\s+(.+)$")

# The manuscript became LaTeX-native on 2026-08-25 (D-065). A section file now
# opens with its heading command and then its label; the number lives in the
# label, because LaTeX generates the printed number itself.
TEX_HEAD_RE = re.compile(r"^\\(chapter|section|subsection)\*?\{(.*)\}\s*$")
# \label for numbered sections; \unnumberedlabel for the starred front and
# back matter, which pins the printed value (see preamble.tex).
# D-406: the prefix may be sec: or ch:, and the name need not be a number.
# The restructure retains legacy sec:N labels on files whose printed number has
# moved, and gives new chapters named ch: labels, so a label name is an identity
# and not a claim about what LaTeX prints. printed_headings() computes the number.
TEX_LABEL_RE = re.compile(r"^\\(?:label|unnumberedlabel)\{(?:sec|ch):([^}]+)\}")


def parse_heading(line):
    """Return (num, title) for a heading line, else None.

    Chapters are numbered '3'; sections keep their dotted number without the
    trailing dot ('3.1.2'). Title excludes the number.
    """
    line = line.rstrip("\n")
    m = CHAPTER_RE.match(line)
    if m:
        return m.group(1), m.group(2).strip()
    m = SECTION_RE.match(line)
    if m:
        return m.group(1), m.group(2).strip()
    return None


def numkey(num):
    """Sort key for a section number, tolerant of a trailing letter.

    D-406 added the letter form: `3.8a` is a section cut out of 3.8 that keeps
    its relation to it in the filename and the label, and it has to sort
    immediately after 3.8 rather than crash. Each dotted part becomes
    (0, int, suffix), so 3.8 < 3.8a < 3.9, and a part with no leading digit at
    all sorts after every numbered one.
    """
    out = []
    for p in num.split("."):
        m = re.match(r"^(\d+)(.*)$", p)
        out.append((0, int(m.group(1)), m.group(2)) if m else (1, 0, p))
    return tuple(out)


def level(num):
    return len(num.split("."))


def parent(num):
    parts = num.split(".")
    return ".".join(parts[:-1]) if len(parts) > 1 else ""


def tex_heading(lines):
    """(num, title) from a .tex section file's opening lines, else None.

    The heading command comes first and the label follows, but front and back
    matter put an \\addcontentsline between them (they are \\chapter*, so they
    are not in the TOC otherwise), hence the small scan rather than lines[1].
    """
    if not lines:
        return None
    h = TEX_HEAD_RE.match(lines[0].rstrip("\n"))
    if not h:
        return None
    for line in lines[1:4]:
        lab = TEX_LABEL_RE.match(line.rstrip("\n"))
        if lab:
            return lab.group(1), h.group(2).strip()
    return None


def order_rows():
    """ORDER.tsv's rows in reading order.

    Reading order is the `seq` column when ORDER.tsv has one, and numeric `num`
    order otherwise. Before D-406 the two were the same thing: `num` was both a
    file's identity and its position, so sorting by it reproduced the book. The
    restructure separates them -- a file keeps the `num` its filename, its label
    and the ledger know it by, while its position moves -- and nothing can be
    derived from `num` about where a file sits any more.

    A row with an empty `num` is a **continuation**: a file with no heading of
    its own, printing under the heading before it. It has no identity, no ledger
    row and no outline row, and it is placed by `seq` alone.
    """
    header, rows = read_tsv(os.path.join(SECTIONS, "ORDER.tsv"))
    if "seq" in header:
        rows.sort(key=lambda r: int(r["seq"]))
    else:
        rows.sort(key=lambda r: numkey(r["num"]))
    return rows


HEAD_RE = re.compile(r"^\\(chapter|section|subsection|subsubsection)(\*?)\s*\{(.*)\}\s*$")
UNNUM_RE = re.compile(r"^\\unnumberedlabel\{(?:sec|ch):([^}]+)\}\{([^}]*)\}")
LEVELS = {"chapter": 0, "section": 1, "subsection": 2, "subsubsection": 3}


def printed_headings():
    """[(printed_number, title, path, lineno, numbered)] for every heading in the TOC.

    `numbered` is False for a starred heading whose value is pinned with
    \\unnumberedlabel -- the Foreword and the glossary. Those print no number,
    so they must not be mistaken for chapters LaTeX numbers; conflating the two
    is what made check_numbers.py report a collision against itself at D-406.

    Simulates LaTeX's chapter/section/subsection counters over the files in
    reading order, so the number is the one that will be typeset. A starred
    heading prints nothing and increments nothing; it appears here only if the
    file pins a value with \\unnumberedlabel, in which case that value is used.
    This is what the table of contents is generated from (D-406). Before then the
    TOC took its numbers from each file's label name, which was the printed
    number only while the two could not diverge.
    """
    out, counters, appendix = [], [0, 0, 0, 0], False
    for r in order_rows():
        path = os.path.join(REPO, r["path"])
        rel = os.path.relpath(path, REPO)
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        pending_star_title = None
        for i, line in enumerate(lines, 1):
            # \appendix resets the chapter counter and prints it as a letter, so
            # every number under it changes. It lives on a continuation row of
            # its own, because it has to precede the \chapter it renumbers.
            if line.rstrip("\n") == "\\appendix":
                appendix = True
                counters = [0, 0, 0, 0]
                continue
            m = HEAD_RE.match(line.rstrip("\n"))
            if m:
                kind, star, title = m.group(1), m.group(2), m.group(3).strip()
                if star:
                    pending_star_title = title
                    continue
                lvl = LEVELS[kind]
                counters[lvl] += 1
                for d in range(lvl + 1, 4):
                    counters[d] = 0
                head = chr(ord("A") + counters[0] - 1) if appendix else str(counters[0])
                num = ".".join([head] + [str(counters[d]) for d in range(1, lvl + 1)])
                out.append((num, title, rel, i, True))
                continue
            u = UNNUM_RE.match(line.rstrip("\n"))
            if u and pending_star_title is not None:
                out.append((u.group(2), pending_star_title, rel, i, False))
                pending_star_title = None
    return out


def section_headings():
    """[(label, title, path)] for every section, in ORDER.tsv order.

    The first element is the **label**, and it always was: `tex_heading` reads
    it off the `\\label` line. It was called `num` here until D-470, which was
    harmless only while every label was a number. D-463 named them, and the
    tools that rolled up on `label.split(".")[0]` began raising
    `int('opening')`. Use `section_labels()` for the locator and
    `chapter_numbers()` for the rollup.
    """
    out = []
    for r in order_rows():
        p = os.path.join(REPO, r["path"])
        with open(p, encoding="utf-8") as f:
            head = [f.readline() for _ in range(4)]
        h = tex_heading(head)
        if h:
            out.append((h[0], h[1], r["path"]))
    return out


def section_labels():
    """path -> the label on the file's heading, `sec:`/`ch:` prefix dropped.

    **What a locator column shows** (D-470, the author's call). A label names a
    section in a way that survives a restructure. The two alternatives do not:
    ORDER.tsv's `num` is an identity that stopped being a position at D-406, and
    the printed number moves whenever a chapter does, which is what put a `3.3`
    in front of the file that prints 6.1 in five committed reports.

    A continuation file has no heading and no label, and is absent here.
    """
    out = {}
    for r in order_rows():
        with open(os.path.join(REPO, r["path"]), encoding="utf-8") as f:
            for _ in range(4):
                m = TEX_LABEL_RE.match(f.readline().rstrip("\n"))
                if m:
                    out[r["path"]] = m.group(1)
                    break
    return out


def ref_targets():
    """path -> [(label, printed_number)] for every label in the file, in order.

    Every `\\label` in the manuscript is a reference target, and not all of
    them sit under a heading LaTeX numbers. The appendix's nine test headings
    are `\\subsection*`, which increments nothing, so a `\\label` after one
    takes the number of the section it is inside -- A.1 for all nine. That is
    LaTeX's rule for `\\@currentlabel`, and it is why this cannot be a
    positional zip against `printed_headings()`.
    """
    nums = {}
    for num, _t, path, _l, _nb in printed_headings():
        nums.setdefault(path, []).append(str(num))
    out = {}
    for r in order_rows():
        queue = list(nums.get(r["path"], []))
        cur, pend_num, pend_star, found = "", False, False, []
        with open(os.path.join(REPO, r["path"]), encoding="utf-8") as fh:
            for line in fh:
                line = line.rstrip("\n")
                h = HEAD_RE.match(line)
                if h:
                    if h.group(2):                 # starred: prints no number
                        pend_star = True
                    else:
                        cur = queue.pop(0) if queue else cur
                        pend_num = True
                    continue
                m = TEX_LABEL_RE.match(line)
                if not m:
                    continue
                if line.startswith("\\unnumberedlabel") and pend_star:
                    cur = queue.pop(0) if queue else cur
                found.append((m.group(1), cur))
                pend_num = pend_star = False
        if queue:
            raise AssertionError(
                "common.ref_targets: %s left %d printed numbers unclaimed (%s). "
                "A heading shape here is one this walk does not know."
                % (r["path"], len(queue), ", ".join(queue)))
        if found:
            out[r["path"]] = found
    return out


_REF_NUMBERS = None


def ref_numbers():
    """label -> the number a `\\ref` to it prints. Computed once, cached.

    D-463 renamed 84 heading labels from numbers to names, and every tool that
    reads the rendered prose began showing `\\S build-costs` where the book
    prints \\S\\,3.4 -- which silently emptied `xref_shapes.py`, whose pattern
    looks for a number after the sign (D-470). The book has always printed a
    number here; only the label stopped being one.
    """
    global _REF_NUMBERS
    if _REF_NUMBERS is None:
        out = {}
        for _path, pairs in ref_targets().items():
            out.update(pairs)
        _REF_NUMBERS = out
    return _REF_NUMBERS


def chapter_numbers():
    """path -> the number the book prints for the chapter the file sits in.

    What a per-chapter rollup groups on, and what `--chapter` matches: a reader
    names a chapter by its number and cites a section by its label. Numbered
    chapters give '1'..'16', the appendix gives letters, and a starred chapter
    gives the value it pins -- '0' for the Preface, '18' for the glossary, which
    is what a `\\ref` to either yields rather than anything on the page.

    **Sort these with `numkey`, never `int`.** The rollups split ORDER.tsv's
    `num` on '.' and called `int()` on the head, which broke on the appendix's
    letter before the labels were named and on every label after (D-470).
    """
    first = {}
    for num, _title, path, _lineno, _numbered in printed_headings():
        first.setdefault(path, num)
    out, cur = {}, ""
    for r in order_rows():
        n = first.get(r["path"])
        if n and "." not in n:
            cur = n
        out[r["path"]] = cur
    return out


def heading_line(num, title):
    """The canonical one-line rendering of a heading, for the TOC."""
    if level(num) != 1:
        return "%s. %s" % (num, title)
    word = "Chapter" if num[:1].isdigit() else "Appendix"
    return "%s %s: %s" % (word, num, title)


def headings_in(path):
    """[(lineno_1based, num, title, raw_line)] for a manuscript-dialect file.

    Retained for dialect-era/split_manuscript.py, its only caller left.
    Section files are .tex now; use section_headings() for those.
    """
    out = []
    quote = list_ = False
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            s = line.strip()
            if s == "<<quote>>":
                quote = True
                continue
            if s == "<</quote>>":
                quote = False
                continue
            if s == "<<list>>":
                list_ = True
                continue
            if s == "<</list>>":
                list_ = False
                continue
            if quote or list_ or s.startswith("#"):
                continue
            h = parse_heading(line)
            if h:
                out.append((i, h[0], h[1], line.rstrip("\n")))
    return out


def read_tsv(path):
    with open(path, encoding="utf-8") as f:
        rows = [l.rstrip("\n").split("\t") for l in f if l.strip()]
    header, body = rows[0], rows[1:]
    return header, [dict(zip(header, r + [""] * (len(header) - len(r)))) for r in body]


def write_tsv(path, header, rows):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            vals = [str(r.get(h, "")).replace("\t", " ").replace("\n", " ") for h in header]
            f.write("\t".join(vals) + "\n")


# --- LaTeX prose extraction (D-070) --------------------------------------
#
# Section files are LaTeX (D-065). Any tool that measures or reads the prose
# has to get the prose out of the markup first, and every tool has to do it
# the same way -- section_stats.py and xref_content.py were both left counting
# dialect markers at D-065 and reported nonsense for two days because each
# carried its own copy of the parsing.
#
# The conventions, stated because they are judgment calls and not facts:
#
#   * A \ref prints one number and the word in front of it ("section") is
#     already prose, so a \ref counts as one word.
#   * A citation is apparatus, not prose: \autocite drops out entirely. This
#     also keeps the year inside a key like piaget1932moral out of the
#     year scan.
#   * A run-in head and a box title are read by the reader, so they count.
#     The section's own heading does not -- it is the title, counted once in
#     ORDER.tsv, and the dialect-era tools skipped it too.
#   * verse/flushright is an epigraph: third-party text, excluded from the
#     author's word count, same as the dialect's <<quote>> was.
#   * A box is the author's own prose and counts, same as <<box>> did.

TEX_DROP_WHOLE = ("label", "unnumberedlabel", "addcontentsline", "input",
                  "autocite", "cite", "nocite", "backmattermark", "rule")
TEX_DROP_HEADING = ("chapter", "section", "subsection", "subsubsection")
# \url keeps its argument: the address is text on the page, and it counts
# as the one token it prints, the same convention \ref gets above.
# "standing" joins this list at D-406: a standing note is a sentence a reader
# reads, so its words are the book's words.
TEX_KEEP_ARG = ("emph", "textbf", "textit", "runin", "standing", "boxtitle", "text",
                "url", "paragraph")
TEX_BARE = ("small", "itshape", "bfseries", "par", "noindent", "medskip",
            "smallskip", "bigskip", "nopagebreak", "item", "centering",
            "hline", "linewidth", "appendix")

# Commands that print a character. \S carries a section number behind it, so it
# has to join the number rather than become the space a dropped command becomes.
TEX_LITERAL = {"S": "\u00a7"}
TEX_QUOTE_ENVS = ("verse", "flushright")

_TEX_ENV = re.compile(r"\\(begin|end)\{([A-Za-z*]+)\}")
# D-406: ch: as well as sec:, or a reference to a new chapter counts as nothing
# and is reported as an unknown command.
_TEX_REF = re.compile(r"\\ref\{(?:sec|ch):([^}]*)\}")
_TEX_CMD = re.compile(r"\\([A-Za-z]+)\*?")
_TEX_ESCAPED = re.compile(r"\\([&%$#_{}])")


def _take_arg(s, i):
    """Text of the brace group starting at s[i]=='{', and the index past it."""
    if i >= len(s) or s[i] != "{":
        return "", i
    depth, j = 0, i
    while j < len(s):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)          # unbalanced; take the rest


def tex_prose_line(line, unknown=None):
    """One line of LaTeX to the prose a reader sees.

    Unknown commands are dropped and their names collected in `unknown` (a
    set, if given) so a macro this function has never been taught shows up as
    a warning instead of silently skewing a count.
    """
    # A reference is the number it prints. Since D-463 the label is a name, so
    # the name is translated here rather than passed through (D-470); a label
    # the map does not know falls back to itself, which is visible rather than
    # silent.
    _refn = ref_numbers()
    line = _TEX_REF.sub(lambda m: "\x00" + _refn.get(m.group(1), m.group(1)), line)
    out, i = [], 0
    while i < len(line):
        m = _TEX_CMD.match(line, i)
        if not m:
            e = _TEX_ESCAPED.match(line, i)
            if e:
                out.append(e.group(1))
                i = e.end()
                continue
            out.append(line[i])
            i += 1
            continue
        name, i = m.group(1), m.end()
        if name in ("begin", "end"):
            _, i = _take_arg(line, i)
            out.append(" ")
        elif name in TEX_DROP_WHOLE or name in TEX_DROP_HEADING:
            while i < len(line) and line[i] == "{":
                _, i = _take_arg(line, i)
            out.append(" ")
        elif name in TEX_KEEP_ARG:
            arg, i = _take_arg(line, i)
            out.append(tex_prose_line(arg, unknown))
        elif name in TEX_BARE:
            out.append(" ")
        elif name in TEX_LITERAL:
            out.append(TEX_LITERAL[name])
        else:
            if unknown is not None:
                unknown.add(name)
            out.append(" ")
    return "".join(out).replace("~", " ").replace("\x00", "")


def tex_sections_of(lines, unknown=None):
    r"""Walk a .tex section file once; return (prose_paragraphs, structure).

    prose_paragraphs is a list of rendered non-empty paragraphs, epigraphs
    excluded. structure counts the things the dialect-era columns used to
    count, in their LaTeX form.

    PARAGRAPHS, NOT LINES (D-384). Until then this appended one entry per
    non-empty prose line, so a paragraph written across several lines counted
    several times: 21 of 89 section files hold hard-wrapped prose and
    section_stats.py's `paras` column was inflated by 359 across the manuscript,
    section 9.1 by 59 and section 6.4.1 by 51 against a true 19 (D-344). Words
    were never affected, the sum over lines being the sum over paragraphs, but
    every caller that runs a sentence splitter over an entry was splitting
    sentences at line breaks.

    A paragraph ends at a blank line, at a heading, at an epigraph, at a
    \runin head, and at each \item. The \runin case is not cosmetic: the head
    sits on its own line with the paragraph beginning on the next one and no
    blank between them, so joining them would make the label the first words of
    the first sentence -- the same trap epigram.py records at section 11.3.
    """
    st = {"list_items": 0, "boxes": 0, "epigraphs": 0, "runins": 0,
          "refs": 0, "cites": 0}
    paras, envs = [], []
    buf = []

    def flush():
        if buf:
            paras.append(" ".join(buf))
            del buf[:]

    for raw in lines:
        line = raw.rstrip("\n")
        if not line.strip():
            flush()
            continue
        st["refs"] += len(_TEX_REF.findall(line))
        st["cites"] += len(re.findall(r"\\autocite\{", line))
        st["runins"] += len(re.findall(r"\\runin\{", line))
        opened = []
        for m in _TEX_ENV.finditer(line):
            if m.group(1) == "begin":
                envs.append(m.group(2))
                opened.append(m.group(2))
                if m.group(2) == "esbox":
                    st["boxes"] += 1
                if m.group(2) == "verse":
                    st["epigraphs"] += 1
            elif envs:
                envs.pop()
        if any(e in TEX_QUOTE_ENVS for e in envs) or \
           any(e in TEX_QUOTE_ENVS for e in opened):
            flush()
            continue                      # epigraph: not the author's words
        if re.match(r"^\\(chapter|section|subsection)\*?\{", line) or \
           re.match(r"^\\(label|unnumberedlabel|addcontentsline)", line):
            flush()
            continue                      # the heading and its machinery
        if re.match(r"^\s*\\item\b", line):
            st["list_items"] += 1
            flush()                       # each item is its own block
        runin = line.lstrip().startswith("\\runin{")
        if runin:
            flush()                       # the head is not the paragraph's first words
        text = tex_prose_line(line, unknown).strip()
        if text:
            buf.append(text)
        if runin:
            flush()
    flush()
    return paras, st
