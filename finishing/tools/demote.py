#!/usr/bin/env python3
r"""Move the paragraphs of a section file that are not its spine into notes.

The book's main text is a spine of about a fifth of its words, with the rest
set as page-bottom notes under the \note{...} macro (D-906). This tool does
the mechanical half of that move for one section file, so that what the
editor decides is which blocks stay and the file's form stays regular.

    finishing/tools/demote.py manuscript/sections/ch08/08_01.tex --list
    finishing/tools/demote.py manuscript/sections/ch08/08_01.tex --keep 1,3
    finishing/tools/demote.py manuscript/sections/ch08/08_01.tex --keep 1,3 --write

--list numbers the file's blocks and prints each one's kind, its first words
and its word count. A block is a blank-line-separated paragraph; a heading
with its \label; a \runin{...} head; a list, quote, figure, table or box
environment, each whole, the table's \begingroup wrapper included; or a run
of comment lines, which stays with the block after it.

--keep names the blocks that stay, by number (1,3,7-9). Headings always stay.
Every run of blocks not kept becomes one note, hung at the end of the kept
block before it, or, when the run opens the section, at the end of the first
kept block after it. A figure, a table, a box, a heading or a block holding a
\label can't go into a note, and the tool refuses to move one. A kept run-in
head whose paragraph would move is refused too: a note can't hang from a
head. Inside a note a \runin{Head} becomes \emph{Head.} at the start of the
paragraph it headed, the lead-in form the notes use.

The source form a note takes: the host block's last line ends with \note{,
the moved blocks follow one per line with their blank lines kept, and the
closing brace stands alone on the next line. So diffs stay line-sized, and
check_structure.py and check_typography.py see nothing they did not before.

Without --write the result is printed, with the file's body word count
before and after (the words a reader reads in the main text, as
common.tex_sections_of counts them, notes left out). Splitting a paragraph
so that its first sentence stays is done by hand before this runs: put the
sentence on a paragraph of its own.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

HEAD = re.compile(r"^\\(chapter|section|subsection|subsubsection|part)\*?(?:\[[^\]]*\])?\{")
LABEL = re.compile(r"^\\(label|unnumberedlabel|backmattermark)\{")
RUNIN = re.compile(r"^\\runin\{")
BEGIN = re.compile(r"^\\begin\{(\w+\*?)\}")
END = re.compile(r"^\\end\{(\w+\*?)\}")
IMMOVABLE_ENVS = ("figure", "longtable", "tabular", "esbox", "center")

# Kinds a note may hold, and kinds it may not.
MOVABLE = ("para", "runin", "list", "quote", "comment")


def blocks_of(lines):
    """Split a section file into blocks: (kind, [lines]) in order."""
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.lstrip().startswith("%"):
            buf = []
            while i < n and lines[i].lstrip().startswith("%"):
                buf.append(lines[i]); i += 1
            out.append(["comment", buf])
            continue
        if HEAD.match(line):
            buf = [line]; i += 1
            while i < n and LABEL.match(lines[i]):
                buf.append(lines[i]); i += 1
            out.append(["heading", buf])
            continue
        if LABEL.match(line):
            out.append(["label", [line]]); i += 1
            continue
        if RUNIN.match(line):
            out.append(["runin", [line]]); i += 1
            continue
        if line.startswith("\\begingroup"):
            # The table wrapper (D-621): \begingroup ... \endgroup around a
            # longtable, one block with the table.
            buf = [line]; i += 1
            while i < n and not lines[i].startswith("\\endgroup"):
                buf.append(lines[i]); i += 1
            if i < n:
                buf.append(lines[i]); i += 1
            out.append(["table", buf])
            continue
        m = BEGIN.match(line)
        if m:
            env = m.group(1)
            buf, depth = [], 0
            while i < n:
                b, e = BEGIN.match(lines[i]), END.match(lines[i])
                if b and b.group(1) == env:
                    depth += 1
                buf.append(lines[i]); i += 1
                if e and e.group(1) == env:
                    depth -= 1
                    if depth == 0:
                        break
            kind = ("figure" if env == "figure" else
                    "table" if env in ("longtable", "tabular", "center") else
                    "box" if env == "esbox" else
                    "list" if env in ("itemize", "enumerate", "description") else
                    "quote" if env in ("quote", "quotation", "verse", "flushright") else
                    "env")
            out.append([kind, buf])
            continue
        buf = []
        while i < n and lines[i].strip() and not HEAD.match(lines[i]) \
                and not RUNIN.match(lines[i]) and not BEGIN.match(lines[i]) \
                and not lines[i].startswith("\\begingroup") \
                and not lines[i].lstrip().startswith("%"):
            buf.append(lines[i]); i += 1
        out.append(["para", buf])
    return out


def words_of(lines):
    paras, _ = common.tex_sections_of(lines)
    return sum(len(p.split()) for p in paras)


def first_words(lines, k=9):
    text = common.tex_prose_line(" ".join(l.strip() for l in lines)).strip()
    w = text.split()
    return " ".join(w[:k]) + (" …" if len(w) > k else "")


def parse_keep(spec, count):
    keep = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            keep.update(range(int(a), int(b) + 1))
        else:
            keep.add(int(part))
    bad = [k for k in keep if k < 1 or k > count]
    if bad:
        raise SystemExit("demote.py: no block %s; the file has %d" % (bad, count))
    return keep


def runin_to_leadin(line):
    """\\runin{Head} -> \\emph{Head.}: the lead-in form a note uses."""
    inner = line.strip()[len("\\runin{"):-1]
    if not inner.endswith((".", ":", "?", "!")):
        inner += "."
    return "\\emph{%s}" % inner


def note_lines(run):
    """The lines of one note from a run of moved blocks: blocks separated by
    a blank line, a run-in head folded into the paragraph after it."""
    out, pending_head = [], None
    for kind, lines in run:
        if kind == "runin":
            pending_head = runin_to_leadin(lines[0])
            continue
        lines = list(lines)
        if pending_head:
            lines[0] = pending_head + " " + lines[0].lstrip()
            pending_head = None
        if out:
            out.append("")
        out += lines
    if pending_head:
        # A head with nothing after it in the run: it stands as a line of its own.
        if out:
            out.append("")
        out.append(pending_head)
    return out


def host_index(lines):
    """Index of the line in a host block that takes the \\note{: the last
    line of a paragraph, the last item of a list, the last line inside a
    quote."""
    for j in range(len(lines) - 1, -1, -1):
        if END.match(lines[j]) or not lines[j].strip():
            continue
        return j
    return len(lines) - 1


def demote(blocks, keep):
    """Return the new file's lines, or raise on a block that can't move."""
    kinds = [b[0] for b in blocks]
    kept = [(i + 1 in keep) or kinds[i] in ("heading", "label") for i in range(len(blocks))]
    errors = []
    for i, (kind, lines) in enumerate(blocks):
        if kept[i]:
            continue
        if kind not in MOVABLE:
            errors.append("block %d is a %s and can't go into a note" % (i + 1, kind))
        if any("\\label{" in l for l in lines):
            errors.append("block %d holds a \\label and can't go into a note" % (i + 1))
    for i, (kind, lines) in enumerate(blocks):
        if kind == "runin" and kept[i] and i + 1 < len(blocks) and not kept[i + 1]:
            errors.append("block %d is a run-in head kept with its paragraph moved; "
                          "keep block %d or move the head too" % (i + 1, i + 2))
    if errors:
        raise SystemExit("demote.py: " + "; ".join(errors))

    # Runs of moved blocks, each assigned to a host: the kept prose block
    # before it, else the first kept prose block after it.
    hosts = {}  # host block index -> list of runs (each a list of blocks)
    i = 0
    while i < len(blocks):
        if kept[i]:
            i += 1
            continue
        run = []
        while i < len(blocks) and not kept[i]:
            run.append(blocks[i]); i += 1
        # A comment run at the head of a moved run stays with the note.
        prev = next((j for j in range(i - len(run) - 1, -1, -1)
                     if kept[j] and kinds[j] in ("para", "list", "quote")), None)
        nxt = next((j for j in range(i, len(blocks))
                    if kept[j] and kinds[j] in ("para", "list", "quote")), None)
        host = prev if prev is not None else nxt
        if host is None:
            raise SystemExit("demote.py: no kept paragraph to hang a note from; "
                             "keep at least one sentence after the heading")
        hosts.setdefault(host, []).append((run, prev is None))

    out, last_kind = [], None
    for i, (kind, lines) in enumerate(blocks):
        if not kept[i]:
            continue
        lines = list(lines)
        if i in hosts:
            j = host_index(lines)
            notes = []
            for run, _opens in hosts[i]:
                notes += ["\\note{"] + note_lines(run) + ["}"]
            # The first \note{ joins the host line; a second note on the same
            # host follows the first's closing brace.
            lines[j] = lines[j].rstrip() + notes[0]
            lines[j + 1:j + 1] = notes[1:]
        # Blocks are set apart by a blank line, except the first paragraph
        # after a heading, which the sources run straight on from the \label.
        if out and not (last_kind in ("heading", "label")):
            out.append("")
        out += lines
        last_kind = kind
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="a section file under manuscript/sections/")
    ap.add_argument("--list", action="store_true", help="number the blocks and stop")
    ap.add_argument("--keep", help="blocks that stay in the main text, e.g. 1,3,7-9")
    ap.add_argument("--write", action="store_true",
                    help="write the result back to the file (default: print it)")
    args = ap.parse_args()

    text = open(args.path, encoding="utf-8").read()
    lines = text.rstrip("\n").split("\n")
    blocks = blocks_of(lines)

    if args.list or not args.keep:
        total = words_of(lines)
        for i, (kind, bl) in enumerate(blocks, start=1):
            print("%3d  %-8s %5d  %s" % (i, kind, words_of(bl) if kind != "heading" else 0,
                                        first_words(bl)))
        print("     body words: %d" % total)
        return 0

    keep = parse_keep(args.keep, len(blocks))
    new = demote(blocks, keep)
    before, after = words_of(lines), words_of(new)
    if args.write:
        with open(args.path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(new) + "\n")
        print("%s: body words %d -> %d (%d%%)" % (args.path, before, after,
                                                  round(100.0 * after / before) if before else 0))
    else:
        print("\n".join(new))
        print("\n%% body words %d -> %d (%d%%); nothing written" % (
            before, after, round(100.0 * after / before) if before else 0), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
