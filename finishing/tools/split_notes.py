#!/usr/bin/env python3
"""Split a Markdown render of the book into two files: the main text, and the notes.

Reads a file written by `render_markdown.py` (either mode: citations as
footnotes, `--truncate N` or not, or `--keys`) and writes, beside it unless
`--out-dir` says otherwise:

  <stem>_main.md   every line that is not a note, the note markers kept as [n]
  <stem>_notes.md  every note, in order, as "[n] text", each under the chapter
                   and section heading of the place it is called from

The markers are rewritten from Pandoc's [^n] to a plain [n] in both files,
because a Pandoc note definition with no reference in its own file is dropped
when rendered, and a file of notes would come out empty. A note's later
paragraphs, indented four spaces in the render, are set flush left. A marker
inside a note (a citation, or a note nested in a note under D-906) points at
another note in the same file.

Like the render, the output is disposable and the LaTeX is the source: nothing
reads these files back.

usage: split_notes.py RENDER.md [--out-dir DIR]
"""
import argparse
import os
import re
import sys

DEF = re.compile(r"^\[\^(\d+)\]: ?(.*)$")
MARK = re.compile(r"\[\^(\d+)\]")
HEAD = re.compile(r"^(#{2,6}) ")


def words(lines):
    return sum(len(MARK.sub(" ", l).split()) for l in lines)


def split(lines):
    """-> (main lines, [(number, heading chain, note lines)])."""
    main, notes = [], []
    heads = {}                      # level -> heading line, for the place a note belongs to
    i = 0
    while i < len(lines):
        line = lines[i]
        m = DEF.match(line)
        if not m:
            h = HEAD.match(line)
            if h:
                level = len(h.group(1))
                heads = {k: v for k, v in heads.items() if k < level}
                heads[level] = line
            main.append(line)
            i += 1
            continue
        body = [m.group(2)]
        i += 1
        # Continuation: indented lines, and blank lines that an indented line follows.
        while i < len(lines):
            if lines[i].startswith("    "):
                body.append(lines[i][4:])
                i += 1
            elif lines[i].strip() == "" and i + 1 < len(lines) and lines[i + 1].startswith("    "):
                body.append("")
                i += 1
            else:
                break
        notes.append((int(m.group(1)), [heads[k] for k in sorted(heads)], body))
    return main, notes


def squeeze(lines):
    out = []
    for l in lines:
        if l.strip() == "" and out and out[-1].strip() == "":
            continue
        out.append(l)
    while out and out[-1].strip() == "":
        out.pop()
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("render", help="a Markdown file written by render_markdown.py")
    ap.add_argument("--out-dir", help="where to write (default: beside the render)")
    args = ap.parse_args()

    src = open(args.render, encoding="utf-8").read().split("\n")
    main_lines, notes = split(src)

    # Every marker in either part has its note, and every note is called once.
    numbers = [n for n, _, _ in notes]
    defined = set(numbers)
    called = [int(x) for l in main_lines for x in MARK.findall(l)]
    called += [int(x) for _, _, b in notes for l in b for x in MARK.findall(l)]
    problems = []
    if len(defined) != len(numbers):
        problems.append("a note number defined twice")
    if set(called) - defined:
        problems.append("markers with no note: %s" % sorted(set(called) - defined)[:10])
    if defined - set(called):
        problems.append("notes nothing calls: %s" % sorted(defined - set(called))[:10])
    if problems:
        sys.exit("split_notes.py: %s: %s" % (args.render, "; ".join(problems)))

    title = next((l for l in src if l.startswith("# ")), "# The book")
    stem = os.path.splitext(os.path.basename(args.render))[0]
    out_dir = args.out_dir or os.path.dirname(os.path.abspath(args.render))
    os.makedirs(out_dir, exist_ok=True)
    main_path = os.path.join(out_dir, stem + "_main.md")
    notes_path = os.path.join(out_dir, stem + "_notes.md")

    plain = lambda l: MARK.sub(r"[\1]", l)
    main_out = squeeze([plain(l) for l in main_lines])

    notes_out = [title + ": the notes", "",
                 "The notes of %s, %d in all, numbered as the main text calls them, "
                 "each under the heading of the place that calls it. Disposable output; "
                 "the manuscript is the LaTeX under manuscript/sections/."
                 % (os.path.basename(args.render), len(notes)), ""]
    shown = []
    for n, chain, body in notes:
        # Print the headings that changed since the last note shown.
        common = 0
        while common < min(len(chain), len(shown)) and chain[common] == shown[common]:
            common += 1
        for h in chain[common:]:
            notes_out += [h, ""]
        shown = chain
        notes_out.append("[%d] %s" % (n, plain(body[0])))
        notes_out += [plain(l) for l in body[1:]]
        notes_out.append("")
    notes_out = squeeze(notes_out)

    with open(main_path, "w", encoding="utf-8") as f:
        f.write("\n".join(main_out) + "\n")
    with open(notes_path, "w", encoding="utf-8") as f:
        f.write("\n".join(notes_out) + "\n")

    note_words = sum(words(b) for _, _, b in notes)
    print("main text: %s  (%d words)" % (main_path, words(main_lines)))
    print("notes:     %s  (%d notes, %d words)" % (notes_path, len(notes), note_words))


if __name__ == "__main__":
    main()
