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
to the file that holds it. `--no-notes` strips the note field from every
bibliography entry: 161 of the 229 carry one, and they are a tenth of the file.

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


def draft_status(root):
    """The status line, or None when the book is not in draft mode.

    The switch is \\draftmode in manuscript/preamble.tex, so one edit there
    governs the PDF's footer, the HTML's bar and this line together instead of
    three files having to be remembered at once. The count is read from
    refs-ledger.tsv rather than from the generated draft-status.tex, so this
    renderer does not depend on that file having been regenerated.
    """
    pre = os.path.join(root, "manuscript", "preamble.tex")
    # Comments are stripped first and the LAST setting wins, which is what TeX
    # would do. Searching the raw file found \\draftmodefalse in the comment
    # that explains how to turn the apparatus off, and read the book as final.
    setting = None
    for line in open(pre, encoding="utf-8"):
        line = re.split(r"(?<!\\)%", line)[0]
        for m in re.finditer(r"\\draftmode(true|false)", line):
            setting = m.group(1)
    if setting != "true":
        return None
    ledger = os.path.join(root, "finishing", "refs-ledger.tsv")
    with open(ledger, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    n = sum(1 for r in rows if (r.get("checked") or "").strip().lower() == "yes")
    return ("PREPRINT \u00b7 WORKING MANUSCRIPT \u00b7 Rendered %s \u00b7 "
            "%d/%d bibliographic entries human-checked"
            % (datetime.datetime.now().strftime("%m/%d/%Y %H:%M"), n, len(rows)))


def read_order(root):
    path = os.path.join(root, "manuscript", "sections", "ORDER.tsv")
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def label_map(root, rows):
    """label -> section number, so \\ref{sec:3.2} can render as "3.2"."""
    out = {}
    for row in rows:
        text = open(os.path.join(root, row["path"]), encoding="utf-8").read()
        for m in re.finditer(r"\\(?:unnumbered)?label\{([^}]*)\}", text):
            out[m.group(1)] = row["num"]
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
                  lambda m: labels.get(m.group(1), m.group(1).replace("sec:", "")),
                  text)
    text = re.sub(r"\\url\{([^}]*)\}", r"<\1>", text)
    text = re.sub(r"\\(?:emph|textit)\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", text)
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


def render(path, num, root, labels):
    """One section file -> a list of Markdown lines."""
    text = open(os.path.join(root, path), encoding="utf-8").read()
    lines = text.split("\n")
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

        m = re.match(r"\\(?:runin|paragraph|boxtitle)\{(.*)\}\s*$", line)
        if m:
            head = "**" + inline(m.group(1), labels).strip() + "**"
            quoted = stack and stack[-1][0] == "quote"
            out += [">" if quoted else "",
                    ("> " + head) if quoted else head,
                    ">" if quoted else ""]
            continue

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


NOTE_FIELD = re.compile(r"note[ \t]*=", re.IGNORECASE)


def strip_notes(bib):
    """Remove every entry-level note field. Returns (text, fields removed).

    Depth is counted from the file, so `note` is recognized only where a field
    name can stand -- directly inside an entry -- and not inside a title or a
    url that contains the word. A note left as the entry's last field leaves a
    trailing comma behind; biber accepts one, and taking it out would mean
    deciding which of two commas was the survivor.
    """
    out, i, depth, removed = [], 0, 0, 0
    while i < len(bib):
        ch = bib[i]
        if (depth == 1 and ch in "nN" and NOTE_FIELD.match(bib, i)
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
            out.append(re.sub(r"\\addbibresource\{[^}]*\}",
                              lambda _: r"\addbibresource{%s.bib}" % bib_stem,
                              line))
            continue
        name = m.group(1)
        if name == "sections":
            out.append(sections_tex(root, rows))
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
            "%%%% Note fields stripped from %d of them (--no-notes): the References" % removed,
            "%% print shorter here than in the book, and nothing else differs.",
        ]
    head += [
        "%%",
        "%% Every file is between START and END markers naming its path in the",
        "%% repository, so a passage can be traced back to the file that holds it.",
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
    body = resolve_inputs(master, root, rows, stem)
    return "\n".join(head) + body.rstrip("\n") + "\n", entries, removed


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tex", action="store_true",
                    help="write the book as one compilable LaTeX file, "
                         "bibliography included, instead of Markdown")
    ap.add_argument("--no-notes", action="store_true",
                    help="--tex only: strip the note field from every "
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
                 ", %d note fields stripped" % removed if args.no_notes else "",
                 len(text.encode("utf-8")) // 1024), file=sys.stderr)
        if args.no_notes and not removed:
            print("WARNING: --no-notes removed nothing; refs.bib has no note "
                  "fields, or they are written in a shape strip_notes() does "
                  "not recognize.", file=sys.stderr)
    else:
        labels = label_map(root, rows)
        body = []
        for row in rows:
            body += render(row["path"], row["num"], root, labels)

        body = squeeze(body)
        status = draft_status(root)
        front = [
            "# Antifascist Intelligence: Building Machines That Can Refuse",
            "",
            "Joshua G. Stern",
            "",
        ] + (["**%s**" % status, ""] if status else []) + [
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
        foot = (["", "---", "", "**%s**" % status] if status else [])
        text = "\n".join(front + body + foot) + "\n"

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
