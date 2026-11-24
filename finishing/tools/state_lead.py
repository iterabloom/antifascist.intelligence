#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
r"""The lead of finishing/STATE.md: one status paragraph, one open list.

STATE.md opens with the paragraph a session is told to read first. The habit
that grew up around it was to put each new lead on top of the last and end it
"the open items of the lead below stand". Thirty leads stood that way on
2026-11-23, with thirty proof-status sentences and an open list that existed
only as a chain (D-1030 folded 145 of them a month earlier, and they came
back). This tool holds the form that stops it. finishing/pipeline.md,
"STATE.md's lead", is the procedure; this is the bookkeeping.

The **live lead** is everything above the first heading of STATE.md (the
first line that begins `# `). It has two parts and nothing else:

  1. The **status paragraph**: line 1 of the file, one paragraph, beginning
     `Read this first. **Updated YYYY-MM-DD, after the proofs of ...**`.
     It says what the last proof build was and what the decisions it carried
     did. It is the only line in the file that begins "Read this first.".

  2. The **open list**: a line beginning `**Open items.**`, which says when
     the list was last checked against the tree as a whole, and under it
     bullets (`- `) grouped under italic heads (a line that begins `*`).
     Every bullet names where it came from, a decision number (D-1234) or a
     date (2026-11-23). An item is stated here in full; no item is a pointer
     to an older lead.

Former leads do not stay in STATE.md. They are kept, newest first, in
finishing/STATE-superseded-leads.md (D-1254), each with its opening words
changed to "**Superseded lead, kept for the record.**".

  --check    Fails on a form error: no status paragraph on line 1; a second
             line beginning "Read this first."; a superseded lead left in
             STATE.md; no heading to end the lead; no open
             list; a line in the open list that is not a bullet or a group
             head; a bullet with no decision number and no date; a phrase that
             defers to another lead ("the lead below", "the leads above");
             a status paragraph over STATUS_MAX words; a live lead over
             LIVE_MAX words. Prints the counts. Prints a notice, and does not
             fail, when the open list was last checked as a whole more than
             RECHECK_DAYS days ago or holds more than ITEMS_NOTICE items.
             Runs in check_all.sh.

  --rotate FILE
             FILE holds the new status paragraph. The tool checks it, puts it
             on line 1, and moves the old status paragraph to the head of
             STATE-superseded-leads.md with its opening words changed to
             "**Superseded lead, kept for the record.**". The open list stays
             where it is; editing it is the agent's work, by hand.

  --show     Prints the live lead.

The tool never writes an open item and never decides whether one is closed.
"""
import argparse, datetime, os, re, subprocess, sys

STATUS_MAX = 700      # words in the status paragraph
LIVE_MAX = 8000       # words in the whole live lead (6,922 on 2026-11-23, with 146 items)
RECHECK_DAYS = 30     # after this, --check asks for a recheck of the whole list
ITEMS_NOTICE = 150    # above this, --check asks for a recheck of the whole list

LIVE = "Read this first."
DEAD = "**Superseded lead, kept for the record.**"
OPEN = "**Open items.**"
STATUS_RE = re.compile(r"^Read this first\. \*\*Updated \d{4}-\d{2}-\d{2}, after the proofs of [^*]+\*\*")
DEFER_RE = re.compile(r"\b(?:lead|leads)\s+(?:\w+\s+){0,2}?(?:below|above)\b|\bas in the lead\b", re.I)
SOURCE_RE = re.compile(r"\bD-\d{1,4}\b|\b\d{4}-\d{2}-\d{2}\b")
CHECKED_RE = re.compile(r"[Cc]hecked against the tree on (\d{4}-\d{2}-\d{2})")


def repo_root():
    return subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()


def state_path():
    return os.path.join(repo_root(), "finishing", "STATE.md")


def archive_path():
    return os.path.join(repo_root(), "finishing", "STATE-superseded-leads.md")


ARCHIVE_MARK = "<!-- leads begin -->"


def read_lines():
    with open(state_path(), encoding="utf-8") as f:
        return f.read().split("\n")


def first_heading(lines):
    for i, l in enumerate(lines):
        if l.startswith("# "):
            return i
    return None


def words(s):
    return len(s.split())


def check_status(par):
    errs = []
    if "\n" in par.strip("\n"):
        errs.append("the status paragraph is more than one line")
    if not STATUS_RE.match(par):
        errs.append('the status paragraph does not begin "Read this first. **Updated YYYY-MM-DD, after the proofs of ...**"')
    if words(par) > STATUS_MAX:
        errs.append("the status paragraph is %d words; the limit is %d (the detail belongs in DECISIONS.md)" % (words(par), STATUS_MAX))
    m = DEFER_RE.search(par)
    if m:
        errs.append('the status paragraph defers to another lead ("%s"); state the item in the open list' % m.group(0))
    return errs


def check(lines):
    errs, notes = [], []
    if not lines or not lines[0].startswith(LIVE):
        errs.append('line 1 does not begin "%s"' % LIVE)
    extra = [i + 1 for i, l in enumerate(lines) if l.startswith(LIVE) and i != 0]
    if extra:
        errs.append('%d more line(s) begin "%s" (line %s%s): there is one live lead; --rotate retires the old one'
                    % (len(extra), LIVE, extra[0], ", ..." if len(extra) > 1 else ""))
    stray = [i + 1 for i, l in enumerate(lines) if l.startswith("**Superseded lead")]
    if stray:
        errs.append("%d superseded lead(s) stand in STATE.md (line %d%s): they belong in STATE-superseded-leads.md"
                    % (len(stray), stray[0], ", ..." if len(stray) > 1 else ""))
    cut = first_heading(lines)
    if cut is None:
        errs.append('no line begins "# ": the live lead has no heading to end it')
        cut = len(lines)
    if not os.path.exists(archive_path()):
        errs.append("finishing/STATE-superseded-leads.md is missing")
    live = lines[:cut]
    if lines and lines[0].startswith(LIVE):
        errs += check_status(lines[0])
    heads = [i for i, l in enumerate(live) if l.startswith(OPEN)]
    items = 0
    if not heads:
        errs.append('the live lead has no line beginning "%s"' % OPEN)
    else:
        if len(heads) > 1:
            errs.append('the live lead has %d lines beginning "%s"' % (len(heads), OPEN))
        h = heads[0]
        if any(l.strip() for l in live[1:h]):
            errs.append("something stands between the status paragraph and the open list (line %d)"
                        % (next(i for i in range(1, h) if live[i].strip()) + 1))
        m = CHECKED_RE.search(live[h])
        if not m:
            errs.append('the "%s" line does not say "checked against the tree on YYYY-MM-DD"' % OPEN)
        else:
            age = (datetime.date.today() - datetime.date.fromisoformat(m.group(1))).days
            if age > RECHECK_DAYS:
                notes.append("the open list was last checked as a whole on %s, %d days ago: recheck it (pipeline.md, \"STATE.md's lead\")"
                             % (m.group(1), age))
        for i in range(h + 1, len(live)):
            l = live[i]
            if not l.strip():
                continue
            if l.startswith("- "):
                items += 1
                if not SOURCE_RE.search(l):
                    errs.append("line %d: an open item names no decision number and no date" % (i + 1))
                m = DEFER_RE.search(l)
                if m:
                    errs.append('line %d: an open item defers to another lead ("%s")' % (i + 1, m.group(0)))
            elif l.startswith("*") and not l.startswith("**"):
                continue
            else:
                errs.append("line %d: in the open list, neither an item (- ) nor a group head (*...*)" % (i + 1))
    live_words = sum(words(l) for l in live)
    if live_words > LIVE_MAX:
        errs.append("the live lead is %d words; the limit is %d" % (live_words, LIVE_MAX))
    if items > ITEMS_NOTICE:
        notes.append("the open list holds %d items: recheck it against the tree and prune (pipeline.md, \"STATE.md's lead\")" % items)
    status_words = words(lines[0]) if lines else 0
    return errs, notes, status_words, items, live_words, cut


def cmd_check():
    lines = read_lines()
    errs, notes, status_words, items, live_words, cut = check(lines)
    for e in errs:
        print("  STATE.md: " + e)
    for n in notes:
        print("  NOTICE: " + n)
    print("STATE.md lead: status paragraph %d words, %d open items, live lead %d words, ending at line %d"
          % (status_words, items, live_words, cut))
    return 1 if errs else 0


def cmd_rotate(path):
    with open(path, encoding="utf-8") as f:
        new = f.read().strip("\n")
    errs = check_status(new)
    if errs:
        for e in errs:
            print("  new status paragraph: " + e)
        return 1
    lines = read_lines()
    if not lines or not lines[0].startswith(LIVE):
        print('  STATE.md: line 1 does not begin "%s"; nothing to rotate' % LIVE)
        return 1
    if lines[0] == new:
        print("  the new status paragraph is the one already on line 1; nothing done")
        return 1
    if not os.path.exists(archive_path()):
        print("  finishing/STATE-superseded-leads.md is missing; nothing to rotate into")
        return 1
    with open(archive_path(), encoding="utf-8") as f:
        arch = f.read().split("\n")
    if ARCHIVE_MARK not in arch:
        print('  STATE-superseded-leads.md has no "%s" line; nothing to rotate into' % ARCHIVE_MARK)
        return 1
    at = arch.index(ARCHIVE_MARK) + 1
    old = DEAD + lines[0][len(LIVE):]
    arch = arch[:at] + ["", old] + arch[at:]
    with open(archive_path(), "w", encoding="utf-8") as f:
        f.write("\n".join(arch))
    with open(state_path(), "w", encoding="utf-8") as f:
        f.write("\n".join([new] + lines[1:]))
    print("rotated: new status paragraph on line 1 (%d words); the old one now heads STATE-superseded-leads.md"
          % words(new))
    return cmd_check()


def cmd_show():
    lines = read_lines()
    cut = first_heading(lines) or len(lines)
    print("\n".join(lines[:cut]).rstrip("\n"))
    return 0


def main():
    ap = argparse.ArgumentParser(description="The lead of finishing/STATE.md: one status paragraph, one open list.")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--rotate", metavar="FILE")
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args()
    if a.rotate:
        sys.exit(cmd_rotate(a.rotate))
    if a.show:
        sys.exit(cmd_show())
    sys.exit(cmd_check())


if __name__ == "__main__":
    main()
