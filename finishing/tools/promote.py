#!/usr/bin/env python3
r"""Move a note back into the main text, one note at a time, as the text stood
before the notes pass.

The reverse of demote.py. The notes pass (D-906 to D-914) moved paragraphs
and sentences into \note{...} notes and left the sources' earlier state in
the history, so a note named here is put back by taking its text from the
commit before the pass merged, with the paragraph breaks, run-in heads and
wording it had there, and nothing else in the file moves.

    finishing/tools/promote.py --map [--notes RENDER_notes.md]
    finishing/tools/promote.py 654 656 660 [--write]

A note is named by the number a Markdown render in its default mode
(citations as footnotes) gives it, counted through the whole book: the
number `split_notes.py`'s notes file labels it with. --map prints that
number for every \note in the sources, with its file and line, whether it
is a block note (opened at a line's end, the form the pass wrote) or an
inline one (a footnote the book had before the pass), and its first words;
with --notes it checks every number against that file and stops on a
mismatch, so a stale render can't name the wrong note.

For a block note the tool finds the note's text in the baseline file, by
its words rather than its markup, and uses the baseline to decide where the
text goes and how it joins: after the host sentence, or before the host
paragraph when the moved run opened its section, with the paragraph or line
break the baseline had. The words are the note's as they stand, not the
baseline's (D-1116): the baseline's could differ by a tenth, or by any
citation, and taking them undid every edit made since the pass. A lead-in
written as \emph{Head.} comes back as the \runin{Head} the baseline had.
The baseline file is the note's path at the baseline; failing that, the path
git follows the file back to; failing that, the baseline section file that
holds the note's opening words, since files were renamed, split and merged
after the pass. For an inline note the baseline holds no body text to
restore, so the note's text is unwrapped into the sentence at its mark and
the joins are left to a hand edit, which the report says.

A number that names a citation is refused: name the note that holds it. A
block note the baseline can't place (its words not found, or found at a
similarity under 0.9) is unwrapped at its mark like an inline one, and the
report says so. Without --write the result is a unified diff per file; with
it the files are written, and refresh_order_shas.py is the next step as
after any edit.
"""

import argparse
import difflib
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

NOTE_OPEN = re.compile(r"\\(?:foot)?note\{")
CITE_CMD = re.compile(
    r"\\(?:auto|paren|text|foot|super)?cite(?:s(?=\s*[\[{]))?\*?"
    r"((?:\s*(?:\[[^\]]*\]){0,2}\{[^}]*\})+)")
NUMBERED = re.compile(NOTE_OPEN.pattern + "|" + CITE_CMD.pattern)
CMD = re.compile(r"\\[A-Za-z]+\*?")
COMMENT = re.compile(r"(?<!\\)%[^\n]*")
LIST_ENVS = ("itemize", "enumerate", "description", "quote", "quotation")
DEFAULT_BASELINE = "f10bc393^"     # main before the notes pass merged (D-914)
DEFAULT_NOTES = os.path.expanduser(
    "~/book-scratch/p222/render-truncate5_787557cf_notes.md")


def masked(text):
    """Comments blanked to spaces, so positions stay those of the text."""
    return COMMENT.sub(lambda m: " " * len(m.group(0)), text)


def norm(raw):
    """(the alphanumerics of the prose, lowercased; their positions in raw).
    Comments, notes, citations and environment names are left out, command
    names without their arguments, and a \\ref becomes its label's name, so
    the same words match whether set as body or note, in the sources or in
    a render."""
    raw = masked(raw)
    out, idx, i, n = [], [], 0, len(raw)
    while i < n:
        if raw[i] == "\\":
            if NOTE_OPEN.match(raw, i):
                _, end = common._take_arg(raw, raw.index("{", i))
                i = end
                continue
            m = CITE_CMD.match(raw, i)
            if m:
                i = m.end()
                continue
            m = re.match(r"\\(?:begin|end)\{[^}]*\}", raw[i:])
            if m:
                i += m.end()
                continue
            m = re.match(r"\\ref\{(?:sec|ch):([^}]*)\}", raw[i:])
            if m:
                for c in m.group(1):
                    if c.isalnum():
                        out.append(c.lower())
                        idx.append(i)
                i += m.end()
                continue
            m = CMD.match(raw, i)
            i = m.end() if m else i + 1
            continue
        c = raw[i]
        if c.isalnum():
            out.append(c.lower())
            idx.append(i)
        i += 1
    return "".join(out), idx


def scan(text):
    """Every numbered item of one file in render order: (kind, start, end)
    with the note's inner text, a note's citations following it."""
    mt = masked(text)
    items, i = [], 0
    while True:
        m = NUMBERED.search(mt, i)
        if not m:
            return items
        if m.group(0).endswith("note{"):
            _, end = common._take_arg(mt, m.end() - 1)
            items.append(("note", m.start(), end, text[m.end():end - 1]))
            i = m.end()               # on into the note: its citations are next
        else:
            items.append(("cite", m.start(), m.end(), None))
            i = m.end()


def book_map():
    """[{n, path, line, form, key, start, end, inner}] for every note."""
    out, n = [], 0
    for row in common.order_rows():
        path = row["path"]
        with open(os.path.join(common.REPO, path), encoding="utf-8") as fh:
            text = fh.read()
        for kind, start, end, inner in scan(text):
            n += 1
            if kind != "note":
                continue
            out.append({"n": n, "path": path, "line": text.count("\n", 0, start) + 1,
                        "form": "block" if inner.startswith("\n") else "inline",
                        "key": norm(inner)[0][:40], "start": start, "end": end,
                        "inner": inner})
    return out, n


def load_notes_file(path):
    notes = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"\[(\d+)\] (.*)", line)
            if m:
                notes[int(m.group(1))] = m.group(2)
    return notes


def check_map(entries, total, notes):
    """Every note's opening words against the render's notes file."""
    bad = []
    for e in entries:
        got = notes.get(e["n"])
        if got is None:
            bad.append("%d: not in the notes file" % e["n"])
            continue
        want = e["key"][:30]
        have = re.sub(r"\W+", "", re.sub(r"\[\d+\]", "", got).lower())[:30]
        if len(want) >= 8 and want != have[:len(want)] and \
                difflib.SequenceMatcher(None, want, have, autojunk=False).ratio() < 0.8:
            bad.append("%d (%s:%d): sources %r, notes file %r"
                       % (e["n"], e["path"], e["line"], want, have))
    if max(notes) != total:
        bad.append("the sources number %d items, the notes file %d" % (total, max(notes)))
    return bad


def _git(*args):
    return subprocess.run(["git", "-C", common.REPO] + list(args),
                          capture_output=True, text=True)


def baseline_text(rev, path, key=None):
    """The baseline's text of the file a note now sits in. The path first; then
    the path git follows the file back to, since files were renamed after the
    notes pass (D-1116); then, for a file assembled since from others, the
    baseline section file holding the note's opening words."""
    r = _git("show", "%s:%s" % (rev, path))
    if not r.returncode:
        return r.stdout
    names = _git("log", "--follow", "--name-only", "--format=", "%s..HEAD" % rev,
                 "--", path).stdout.split()
    if names:
        r = _git("show", "%s:%s" % (rev, names[-1]))
        if not r.returncode and (key is None or key in norm(r.stdout)[0]):
            return r.stdout
    if key:
        for p in _git("ls-tree", "-r", "--name-only", rev,
                      "manuscript/sections").stdout.split():
            if p.endswith(".tex"):
                t = _git("show", "%s:%s" % (rev, p)).stdout
                if key in norm(t)[0]:
                    return t
    return None


def locate(nb, ni, window=40, slack=120):
    """Where the note's first (or, with ni reversed, last) words sit in the
    baseline: (position in nb, how many of ni's characters came before the
    window that matched). A repaired head is skipped by sliding the window."""
    best = None
    for off in range(0, min(max(len(ni) - window, 0), slack) + 1, 10):
        for w in (window, 80):
            key = ni[off:off + w]
            if len(key) < 20:
                break
            hits = [m.start() for m in re.finditer(re.escape(key), nb)]
            if len(hits) == 1:
                return hits[0], off
            if not hits:
                break
    return best


def sentence_start_before(btext, pos, want):
    """The sentence boundary before raw position pos whose distance to pos,
    in prose characters, is nearest `want`."""
    cands = [m.end() for m in re.finditer(
        r"(?<=[.!?;:])\s+(?=[\"“‘(A-Z\\])|\n[ \t]*\n|\\runin\{[^}]*\}\n|\\label\{[^}]*\}\n",
        btext[:pos])]
    if not cands:
        return 0
    return min(cands, key=lambda c: (abs(len(norm(btext[c:pos])[0]) - want), -c))


def sentence_end_after(btext, pos, want):
    cands = [pos + m.end() for m in re.finditer(r"[.!?](?=\s|$|\\note\{|\})", btext[pos:])]
    if not cands:
        return len(btext)
    return min(cands, key=lambda c: (abs(len(norm(btext[pos:c])[0]) - want), c))


def extend_start(btext, rs, inner):
    r"""Back over an opening quote or \emph{, the \item and \begin of a list the
    span opens, and the \runin head a lead-in stood for."""
    while True:
        moved = False
        for pre in ("\\emph{", "\\textit{", "\\runin{", "“", "‘", "(", "\"", "\\item ", "\\item\n"):
            if btext[:rs].endswith(pre):
                rs -= len(pre)
                moved = True
        m = re.search(r"\\begin\{(%s)\}[ \t]*\n$" % "|".join(LIST_ENVS), btext[:rs])
        if m:
            rs = m.start()
            moved = True
        if not moved:
            break
    if inner.lstrip().startswith("\\emph{"):
        m = re.search(r"\\runin\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[ \t]*\n[ \t]*$", btext[:rs])
        if m:
            rs = m.start()
    return rs


def extend_end(btext, re_):
    r"""On over closing punctuation, a citation or inline note the sentence
    ends with, and the \end of a list the span closes."""
    n = len(btext)
    while re_ < n:
        c = btext[re_]
        if c in ".,;:!?”’)\"}":
            re_ += 1
            continue
        m = re.match(r"[ \t]*\\(?:auto|paren|text|foot|super)?cite", btext[re_:])
        if m:
            m2 = CITE_CMD.match(btext, re_ + len(m.group(0)) - len(m.group(0).lstrip()))
            if m2:
                re_ = m2.end()
                continue
        if NOTE_OPEN.match(btext, re_):
            _, re_ = common._take_arg(btext, btext.index("{", re_))
            continue
        m = re.match(r"\s*\\end\{(%s)\}" % "|".join(LIST_ENVS), btext[re_:])
        if m:
            re_ += m.end()
            continue
        break
    return re_


STRUCTURAL = re.compile(
    r"\\(?:item\b|begin\{|end\{|runin\{|paragraph\{|boxtitle\{|label\{|unnumberedlabel\{"
    r"|chapter\b|section\b|subsection\b|subsubsection\b|begingroup\b|endgroup\b)")


def join_of(gap, preceding, following=""):
    """What stood between two pieces of baseline text: a paragraph break; the
    line break after a label or head, or before an \\item, an environment
    line or a head, which a space would break; a space; or nothing."""
    if re.search(r"\n[ \t]*\n", gap):
        return "\n\n"
    if "\n" in gap and (STRUCTURAL.match(following) or re.search(
            r"\\(label|unnumberedlabel|chapter|section|subsection|subsubsection|runin)\{[^\n]*\}[ \t]*$",
            preceding.rstrip("\n"))):
        return "\n"
    if gap == "":
        return ""
    return " "


def host_block_start(ctext, start):
    r"""Where the host paragraph begins: after the last blank line, label line
    or heading line before the note, or after \item."""
    head = ctext[:start]
    cands = [m.end() for m in re.finditer(
        r"\n[ \t]*\n|\\(?:label|unnumberedlabel|chapter|section|subsection|subsubsection)\{[^\n]*\}[ \t]*\n|\\item[ \t]+",
        head)]
    return cands[-1] if cands else 0


def restore_block(ctext, btext, e, report):
    start, end, inner = e["start"], e["end"], e["inner"]
    nb, ib = norm(btext)
    ni, _ = norm(inner)
    if len(ni) < 20:
        report.append("note %d: too short to locate" % e["n"])
        return None
    hit = locate(nb, ni)
    if not hit:
        report.append("note %d: its opening words are not in the baseline" % e["n"])
        return None
    s_pos, s_off = hit
    # The last words: slide a window back from the end.
    hit = None
    for off in range(0, min(max(len(ni) - 40, 0), 120) + 1, 10):
        for w in (40, 80):
            key = ni[max(len(ni) - w - off, 0):len(ni) - off]
            if len(key) < 20:
                break
            hits = [m.start() for m in re.finditer(re.escape(key), nb)]
            if len(hits) == 1:
                hit = (hits[0] + len(key) - 1, off)
                break
            if not hits:
                break
        if hit:
            break
    if not hit:
        report.append("note %d: its closing words are not in the baseline" % e["n"])
        return None
    e_pos, e_off = hit
    rs = ib[s_pos] if s_off == 0 else sentence_start_before(btext, ib[s_pos], s_off)
    re_ = ib[e_pos] + 1 if e_off == 0 else sentence_end_after(btext, ib[e_pos], e_off)
    rs = extend_start(btext, rs, inner)
    re_ = extend_end(btext, re_)
    span = btext[rs:re_]
    ratio = difflib.SequenceMatcher(None, norm(span)[0], ni, autojunk=False).ratio()
    if ratio < 0.9:
        report.append("note %d: baseline span matches at %.2f only; skipped. Span opens %r, note opens %r"
                      % (e["n"], ratio, span[:80], inner.strip()[:80]))
        return None
    # The words are the note's as it stands, not the baseline's: the baseline
    # says only where the span stood and how it joined (D-1116). Its words
    # differ by as much as a tenth, and a citation, which norm() leaves out,
    # by any amount, so taking them would undo every edit made since the pass.
    # A lead-in the baseline set as a run-in head comes back as that head.
    cur = inner.strip()
    lead = re.match(r"\\emph\{[^{}]*\}\s*", cur)
    head = re.match(r"\\runin\{[^\n]*\}[ \t]*\n(?:[ \t]*\n)?", span)
    span = head.group(0) + cur[lead.end():] if lead and head else cur

    # Which side of the host the span stood on.
    hs = host_block_start(ctext, start)
    host_text = ctext[hs:start]
    hn, _ = norm(host_text)
    direction = "after"
    hkey = hn[-40:]
    if len(hkey) >= 20:
        hits = [m.start() for m in re.finditer(re.escape(hkey), nb)]
        if len(hits) == 1 and hits[0] >= e_pos:
            direction = "before"
        elif not hits:
            report.append("note %d: the host sentence is not in the baseline as it stands "
                          "(a repair?); the span goes after it" % e["n"])
    prev_end = len(btext[:rs].rstrip())
    jb = join_of(btext[prev_end:rs], btext[:prev_end], span)
    nxt = re_ + (len(btext[re_:]) - len(btext[re_:].lstrip()))
    ja = join_of(btext[re_:nxt], span, btext[nxt:])

    rest = ctext[end:]
    if direction == "before":
        # The wrapper goes; the span stands before the host paragraph.
        jh = ja if ja in (" ", "\n", "\n\n") else "\n\n"
        new = ctext[:hs] + span + jh + ctext[hs:start] + rest
    else:
        before = ctext[:start].rstrip(" ")
        if rest.startswith("\\note{"):
            report.append("note %d: a second note follows on the same host; left attached" % e["n"])
            new = before + jb + span + rest
        else:
            k = len(rest) - len(rest.lstrip("\n"))
            cont = rest[k:]
            if not cont.strip():
                new = before + jb + span + "\n"
            else:
                if STRUCTURAL.match(cont) and ja == " ":
                    ja = "\n"          # what follows in the file is a line of its own
                new = before + jb + span + (ja if ja in (" ", "\n", "\n\n") else "\n\n") + cont
    words = len(common.tex_prose_line(common.strip_tex_notes(span.replace("\n", " "))).split())
    report.append("note %d (%s:%d): restored %s the host, %d words, match %.2f, join %r/%r%s"
                  % (e["n"], e["path"], e["line"], direction, words, ratio,
                     jb.replace("\n", "¶"), ja.replace("\n", "¶"),
                     "; a lead-in became its run-in head" if "\\runin{" in span and inner.lstrip().startswith("\\emph{") else ""))
    return new


def restore_inline(ctext, e, report):
    start, end, inner = e["start"], e["end"], e["inner"]
    before = ctext[:start].rstrip(" ")
    rest = ctext[end:]
    new = before + " " + inner.strip() + ("" if rest[:1] in (" ", "\n", "") else " ") + rest
    report.append("note %d (%s:%d): an inline note, unwrapped at its mark; the joins need a hand edit"
                  % (e["n"], e["path"], e["line"]))
    return new


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("numbers", nargs="*", type=int, help="render numbers of the notes to restore")
    ap.add_argument("--map", action="store_true", help="print every note's number, place and first words")
    ap.add_argument("--notes", default=DEFAULT_NOTES,
                    help="the notes file of the render the numbers come from (default: %(default)s)")
    ap.add_argument("--baseline", default=DEFAULT_BASELINE,
                    help="the commit the text comes back from (default: %(default)s)")
    ap.add_argument("--write", action="store_true", help="write the files (default: print diffs)")
    args = ap.parse_args()

    entries, total = book_map()
    if os.path.exists(args.notes):
        bad = check_map(entries, total, load_notes_file(args.notes))
        if bad:
            raise SystemExit("promote.py: the numbers don't match %s:\n  %s"
                             % (args.notes, "\n  ".join(bad[:20])))
    elif args.numbers:
        raise SystemExit("promote.py: no notes file at %s to check the numbers against" % args.notes)

    if args.map or not args.numbers:
        for e in entries:
            print("%4d  %-40s %5d  %-6s  %s" % (e["n"], e["path"], e["line"], e["form"],
                                               e["inner"].strip().replace("\n", " ")[:70]))
        print("%d notes, %d numbered items in all" % (len(entries), total))
        return 0

    by_n = {e["n"]: e for e in entries}
    cites = [n for n in args.numbers if n not in by_n and 1 <= n <= total]
    unknown = [n for n in args.numbers if n < 1 or n > total]
    if cites or unknown:
        raise SystemExit("promote.py: %s%s" % (
            ("%s name citations, not notes; name the note that holds each" % cites) if cites else "",
            (" %s are out of range (1 to %d)" % (unknown, total)) if unknown else ""))

    # Resolve now, by file and opening words, since the numbers shift as notes go.
    wanted = [(by_n[n]["path"], by_n[n]["key"], n) for n in sorted(set(args.numbers))]
    for path, key, n in wanted:
        if sum(1 for e in entries if e["path"] == path and e["key"] == key) > 1:
            raise SystemExit("promote.py: note %d's opening words recur in %s; can't name it safely" % (n, path))

    report, originals, texts = [], {}, {}
    for path, key, n in wanted:
        if path not in texts:
            with open(os.path.join(common.REPO, path), encoding="utf-8") as fh:
                texts[path] = fh.read()
        text = texts[path]
        originals.setdefault(path, text)
        e = next(({"n": n, "path": path, "line": text.count("\n", 0, start) + 1,
                   "form": "block" if inner.startswith("\n") else "inline",
                   "start": start, "end": end, "inner": inner}
                  for kind, start, end, inner in scan(text)
                  if kind == "note" and norm(inner)[0][:40] == key), None)
        if e is None:
            report.append("note %d: no longer found in %s (restored with another?)" % (n, path))
            continue
        if e["form"] == "inline":
            new = restore_inline(text, e, report)
        else:
            btext = baseline_text(args.baseline, path, key)
            if btext is None:
                report.append("note %d: no file at %s holds it" % (n, args.baseline))
            new = restore_block(text, btext, e, report) if btext else None
            if new is None:
                # Not placeable from the baseline (written since, or rewritten
                # past recognition): unwrapped at its mark, like an inline one.
                new = restore_inline(text, e, report)
        if new is not None:
            texts[path] = new

    for line in report:
        print(line)
    for path, new in texts.items():
        if args.write:
            with open(os.path.join(common.REPO, path), "w", encoding="utf-8") as fh:
                fh.write(new)
        else:
            sys.stdout.writelines(difflib.unified_diff(
                originals[path].splitlines(True), new.splitlines(True),
                "a/" + path, "b/" + path))
    if args.write:
        print("%d file(s) written; run refresh_order_shas.py" % len(texts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
