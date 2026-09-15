#!/usr/bin/env python3
"""Render the whole manuscript as one Markdown file, outside the repository.

The book is LaTeX (D-065) and this is not a second source of truth: the output
is disposable, written to /tmp by default, and nothing in the repository reads
it. It exists so the manuscript can be read, searched, diffed or handed to a
tool that wants one plain-text file.

Reading order and section numbers come from manuscript/sections/ORDER.tsv, the
same file gen_book.py builds sections.tex from, so the Markdown is in the
book's order by construction rather than by a second list kept in step by hand.

What is lost, and knowingly: page breaks, the table of contents, the title
page, the typeset bibliography. Citations survive as Pandoc-style keys
([@smith2020title]) pointing into finishing/refs.bib, which is not inlined.

Usage:
    finishing/tools/render_markdown.py            # -> /tmp/<slug>_<date>.md
    finishing/tools/render_markdown.py --out PATH
    finishing/tools/render_markdown.py --check    # report only, write nothing
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


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", help="output path (default: /tmp/<slug>_<date>.md)")
    ap.add_argument("--check", action="store_true",
                    help="report what would be rendered and write nothing")
    args = ap.parse_args()

    root = repo_root()
    rows = read_order(root)
    labels = label_map(root, rows)

    head = subprocess.run(["git", "-C", root, "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "-C", root, "status", "--porcelain"],
                           capture_output=True, text=True).stdout.strip()
    stamp = datetime.date.today().isoformat()

    body = []
    for row in rows:
        body += render(row["path"], row["num"], root, labels)

    body = squeeze(body)
    front = [
        "# Antifascist Intelligence: Building Machines That Can Refuse",
        "",
        "Joshua G. Stern",
        "",
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

    out = args.out or os.path.join("/tmp", "%s_%s.md" % (SLUG, stamp))
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(os.path.abspath(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
