"""Shared helpers: heading parsing and the manuscript dialect."""
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V3B = os.path.join(REPO, "manuscript", "parseable_text_v3b_2024-07-07.txt")
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
TEX_LABEL_RE = re.compile(r"^\\label\{sec:([\d.]+)\}\s*$")


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

    Retained for the frozen dialect references (v3b, parseable_text_v4.txt),
    which are provenance and still in the dialect. Section files are .tex now;
    use section_headings() for those.
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
