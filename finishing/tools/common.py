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
TEX_LABEL_RE = re.compile(r"^\\(?:label|unnumberedlabel)\{sec:([\d.]+)\}")


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
    return tuple(int(p) for p in num.split("."))


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


def section_headings():
    """[(num, title, path)] for every section, in ORDER.tsv order."""
    _, rows = read_tsv(os.path.join(SECTIONS, "ORDER.tsv"))
    rows.sort(key=lambda r: numkey(r["num"]))
    out = []
    for r in rows:
        p = os.path.join(REPO, r["path"])
        with open(p, encoding="utf-8") as f:
            head = [f.readline() for _ in range(4)]
        h = tex_heading(head)
        if h:
            out.append((h[0], h[1], r["path"]))
    return out


def heading_line(num, title):
    """The canonical one-line rendering of a heading, for the TOC."""
    return ("Chapter %s: %s" % (num, title)) if level(num) == 1 \
        else ("%s. %s" % (num, title))


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
                  "autocite", "cite", "nocite")
TEX_DROP_HEADING = ("chapter", "section", "subsection", "subsubsection")
TEX_KEEP_ARG = ("emph", "textbf", "textit", "runin", "boxtitle", "text")
TEX_BARE = ("small", "itshape", "bfseries", "par", "noindent", "medskip",
            "smallskip", "bigskip", "nopagebreak", "item", "centering")
TEX_QUOTE_ENVS = ("verse", "flushright")

_TEX_ENV = re.compile(r"\\(begin|end)\{([A-Za-z*]+)\}")
_TEX_REF = re.compile(r"\\ref\{sec:([^}]*)\}")
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
    line = _TEX_REF.sub(lambda m: m.group(1), line)   # a reference is its number
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
        else:
            if unknown is not None:
                unknown.add(name)
            out.append(" ")
    return "".join(out).replace("~", " ")


def tex_sections_of(lines, unknown=None):
    """Walk a .tex section file once; return (prose_paragraphs, structure).

    prose_paragraphs is a list of rendered non-empty paragraphs, epigraphs
    excluded. structure counts the things the dialect-era columns used to
    count, in their LaTeX form.
    """
    st = {"list_items": 0, "boxes": 0, "epigraphs": 0, "runins": 0,
          "refs": 0, "cites": 0}
    paras, envs = [], []
    for raw in lines:
        line = raw.rstrip("\n")
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
            continue                      # epigraph: not the author's words
        if re.match(r"^\\(chapter|section|subsection)\*?\{", line) or \
           re.match(r"^\\(label|unnumberedlabel|addcontentsline)", line):
            continue                      # the heading and its machinery
        if re.match(r"^\s*\\item\b", line):
            st["list_items"] += 1
        text = tex_prose_line(line, unknown).strip()
        if text:
            paras.append(text)
    return paras, st
