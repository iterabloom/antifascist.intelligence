#!/usr/bin/env python3
"""What a section number written in the record means now.

The record cites sections by number 7,022 times and by label 228. A number is
only true as of a date: twenty-two renumbers stand between the earliest entries
and the book, and `QUESTIONS.md`'s own header calls reading through them the
largest gap in that file. This composes the maps so that reading is one command.

**It refuses to answer without `--as-of`, and that is the design.** Numbers are
reissued: `6.3` maps to nothing on 2026-08-23, to 6.2 on 2026-09-12 and to 6.4
on 2026-09-13, because a vacated number is handed to a new section later. Chained
from the wrong date the composition returns a confident wrong answer rather than
an error, which is worse than no tool in a repository whose rule is to derive a
figure before stating it.

What it cannot reach, and says so rather than guessing:

  * **A cut section did not become anything.** The 2026-09-12 map carries the
    September 12 return's 43 deletions as rows whose new number is a dash. The
    chain stops there and reports the cut, which is the true answer.
  * **A surviving number can name rewritten text.** D-288 measured 98 to 100
    percent of chapters 3, 4 and 5's returned sentences as appearing nowhere in
    the exported text. The number resolves; the section behind it is new prose.
    `QUESTIONS.md`'s own rule already says a question whose target was rewritten
    is not thereby answered, and a chain crossing that date is flagged.
  * **D-406 changed what a number is.** Before it, `ORDER.tsv`'s `num` was a
    file's position; after it, `num` is an identity and the printed number is
    computed. Every map predates D-406, so a composed result is an identity, and
    the printed number is resolved from it separately.

The two map dialects are both handled. `renumber-map_2026-08-23.tsv` enumerates
every descendant -- 7 to 6 and 7.1 to 6.3 and 7.1.1 to 6.3.1. The 08-24 map
instead writes `3  4  chapter and all descendants` and expects the suffix to be
carried over, with explicit child rows as exceptions to it. So a lookup takes an
exact row where there is one and otherwise propagates from the nearest mapped
ancestor, and says which of the two it did.

Usage:
  trace.py 3.6 --as-of 2026-08-25
  trace.py 6.3 --as-of D-302
  trace.py --list-maps
  trace.py --check-aux /tmp/es-build/book.aux    # printed numbers vs a real build
"""
import argparse
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

MAPS = os.path.join(common.REPO, "finishing")
DISSOLVED = ("", "-", "\u2014")
# The September 12 return, which cut 132 sections to 89 and rewrote what it kept.
REWRITE_DATE = "2026-09-12"


def map_files():
    """The renumber maps in the order they were applied.

    Sorted on the date in the filename and then on the suffix letter, which is
    how same-day maps are distinguished; the file mtimes agree with that order
    for every same-day pair on disk.
    """
    out = []
    for path in glob.glob(os.path.join(MAPS, "renumber-map_*.tsv")):
        m = re.search(r"renumber-map_(\d{4}-\d{2}-\d{2})([a-z]?)\.tsv$", path)
        if m:
            out.append((m.group(1), m.group(2), path))
    return sorted(out)


def read_map(path):
    """[(old, new, note)] for one map, leading comment lines and header dropped.

    One map opens with six comment lines instead of a header. Rows whose old is
    a dash record an insertion -- a section that did not previously exist -- and
    are dropped, because nothing can be traced *from* them.
    """
    rows = []
    with open(path, encoding="utf-8") as fh:
        lines = [l.rstrip("\n") for l in fh if l.strip()]
    lines = [l for l in lines if not l.startswith("#")]
    header = lines[0].split("\t")
    if header[0] != "old":
        raise SystemExit("%s: first non-comment line is not a header" % path)
    note_at = header.index("note") if "note" in header else None
    for line in lines[1:]:
        cells = line.split("\t")
        cells += [""] * (len(header) - len(cells))
        old, new = cells[0].strip(), cells[1].strip()
        note = cells[note_at].strip() if note_at is not None else ""
        if old in ("-", "\u2014", ""):
            continue
        rows.append((old, new, note))
    return rows


def ancestors(num):
    """3.4.1 -> ['3.4', '3'], nearest first."""
    parts = num.split(".")
    return [".".join(parts[:i]) for i in range(len(parts) - 1, 0, -1)]


def apply_map(num, rows):
    """(new_number, how, note) after one map, or (num, None, '') if untouched.

    `how` is 'exact', 'propagated', or 'dissolved'. A map is applied as one
    simultaneous substitution and never row by row, so a map that vacates a
    number and reissues it in the same pass cannot be read twice.
    """
    exact = {o: (n, note) for o, n, note in rows}
    if num in exact:
        new, note = exact[num]
        return (None, "dissolved", note) if new in DISSOLVED else (new, "exact", note)
    for anc in ancestors(num):
        if anc in exact:
            new, note = exact[anc]
            if new in DISSOLVED:
                return None, "dissolved", note
            suffix = num[len(anc):]
            enumerated = [o for o in exact if o.startswith(anc + ".")]
            carries = "descendant" in note.lower()
            flag = "propagated" if (carries or not enumerated) else "propagated?"
            return new + suffix, flag, note
    return num, None, ""


def resolve_as_of(text):
    """A date, a D-NNN, or a PNN -> (date, how it was read)."""
    text = text.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return text, "a date"
    m = re.fullmatch(r"[Dd]-?(\d{3})", text)
    if m:
        want = "| D-%s |" % m.group(1)
        with open(os.path.join(common.REPO, "finishing", "DECISIONS.md"),
                  encoding="utf-8") as fh:
            for line in fh:
                if line.startswith(want):
                    date = line.split("|")[2].strip()
                    return date, "D-%s, dated %s in DECISIONS.md" % (m.group(1), date)
        raise SystemExit("no row D-%s in DECISIONS.md" % m.group(1))
    m = re.fullmatch(r"[Pp]-?(\d{1,3})", text)
    if m:
        # A pass number is not a column anywhere. The first decision row whose
        # topic names the pass is the best available anchor, and the row is
        # named in the output so the reading can be checked rather than trusted.
        pat = re.compile(r"\bP%s\b" % m.group(1))
        with open(os.path.join(common.REPO, "finishing", "DECISIONS.md"),
                  encoding="utf-8") as fh:
            for line in fh:
                if not line.startswith("| D-"):
                    continue
                cells = line.split("|")
                # The pass number lives in the Topic cell ("P131: ..."), not the
                # decision body, where a later row discussing that pass would
                # match first and date the anchor wrongly.
                if len(cells) > 3 and pat.search(cells[3]):
                    return cells[2].strip(), ("P%s, read off %s dated %s -- check it"
                                              % (m.group(1), cells[1].strip(), cells[2].strip()))
        raise SystemExit("no decision row names P%s" % m.group(1))
    raise SystemExit("--as-of takes a date (2026-09-12), a decision (D-302) or a pass (P131)")


def printed_for(identity):
    """Today's printed number and label for an ORDER.tsv identity, or None."""
    for row in common.order_rows():
        if row["num"] != identity:
            continue
        for num, _title, path, _line, numbered in common.printed_headings():
            if path == row["path"] and numbered:
                label = None
                with open(os.path.join(common.REPO, row["path"]), encoding="utf-8") as fh:
                    m = re.search(r"\\label\{([^}]*)\}", fh.read())
                    if m:
                        label = m.group(1)
                return str(num), label, row["path"], row["title"]
        return None, None, row["path"], row["title"]
    return None


def trace(number, as_of_date):
    """Walk every map applied after the as-of date. Returns (hops, final, notes)."""
    hops, warnings = [], []
    current, crossed_rewrite = number, False
    later_reissue = False
    for date, suffix, path in map_files():
        if date <= as_of_date:
            # A map at or before the as-of is already reflected in the number.
            # Whether the same string is remapped later is the reissue hazard,
            # and it is reported rather than silently resolved.
            continue
        rows = read_map(path)
        if any(o == number for o, _n, _t in rows) and current != number:
            later_reissue = True
        new, how, note = apply_map(current, rows)
        if how:
            hops.append((os.path.basename(path), current, new, how, note))
            if how == "dissolved":
                current = None
                break
            current = new
        if date >= REWRITE_DATE > as_of_date:
            crossed_rewrite = True
    if crossed_rewrite:
        warnings.append(
            "this chain crosses the %s return (D-288), which cut 43 sections and\n"
            "    rewrote most of what it kept -- a number that resolves may name new prose"
            % REWRITE_DATE)
    if later_reissue:
        warnings.append(
            "'%s' is also the old number of a later map row, so the as-of is load-bearing:\n"
            "    a mention written after that map means a different section" % number)
    same_day = [os.path.basename(p) for d, _s, p in map_files() if d == as_of_date]
    if same_day:
        warnings.append(
            "the as-of resolves to a day that carries its own renumber (%s).\n"
            "    Maps on the as-of date are treated as already applied; if the mention was\n"
            "    written earlier that day, trace it from the day before."
            % ", ".join(same_day))
    if any(h[3] == "propagated?" for h in hops):
        warnings.append(
            "one hop was propagated from a parent in a map that enumerates other\n"
            "    children explicitly, so the parent's row may not have been meant to carry it")
    return hops, current, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("number", nargs="?", help="a section number as the record writes it")
    ap.add_argument("--as-of", help="a date, a decision (D-302) or a pass (P131)")
    ap.add_argument("--list-maps", action="store_true", help="the renumber timeline")
    ap.add_argument("--check-aux", metavar="AUX",
                    help="validate today's printed numbers against a real book.aux")
    args = ap.parse_args()

    if args.list_maps:
        for date, suffix, path in map_files():
            rows = read_map(path)
            cut = sum(1 for _o, n, _t in rows if n in DISSOLVED)
            print("%s%s  %3d rows, %2d of them cuts   %s"
                  % (date, suffix or " ", len(rows), cut, os.path.basename(path)))
        return 0

    if args.check_aux:
        aux = {}
        with open(args.check_aux, encoding="utf-8") as fh:
            for m in re.finditer(r"\\newlabel\{([^}]*)\}\{\{([^}]*)\}", fh.read()):
                aux[m.group(1)] = m.group(2)
        mine = {}
        for num, _t, path, line, numbered in common.printed_headings():
            with open(os.path.join(common.REPO, path), encoding="utf-8") as fh:
                body = fh.read().split("\n")
            for i, src in enumerate(body[line - 1:line + 2], start=line):
                m = re.search(r"\\label\{([^}]*)\}", src)
                if m:
                    mine[m.group(1)] = str(num)
                    break
        shared = sorted(set(mine) & set(aux))
        bad = [(k, mine[k], aux[k]) for k in shared if mine[k] != aux[k]]
        print("labels in the aux: %d; resolved here: %d; comparable: %d"
              % (len(aux), len(mine), len(shared)))
        print("  the rest are labels in a file's body rather than a heading's own,")
        print("  which this tool does not resolve and does not claim to")
        print("disagreements: %d" % len(bad))
        for k, a, b in bad[:10]:
            print("   %-14s here %-8s aux %s" % (k, a, b))
        return 1 if bad else 0

    if not args.number:
        ap.error("give a section number, or --list-maps")
    if not args.as_of:
        ap.error("--as-of is required. A number is only true as of a date, and "
                 "numbers are reissued: chained from the wrong date this returns a "
                 "confident wrong answer. Give a date, a decision (D-302) or a pass (P131).")

    date, how_read = resolve_as_of(args.as_of)
    print("%s as of %s (%s)" % (args.number, date, how_read))
    hops, final, warnings = trace(args.number, date)

    if not hops:
        print("  no renumber touched it after that date")
    for name, was, now, how, note in hops:
        arrow = "cut" if how == "dissolved" else now
        print("  %-32s %-8s -> %-8s %s%s"
              % (name, was, arrow, how, "   (%s)" % note if note else ""))

    if final is None:
        print("\n  GONE: the chain ends in a cut. The section was removed, not renumbered,")
        print("  and no map can say what it became because it did not become anything.")
    else:
        got = printed_for(final)
        if got is None:
            print("\n  %s is not an identity in ORDER.tsv today." % final)
            print("  The likeliest reading is that it was cut at or before the as-of,")
            print("  so no later map mentions it; trace it from an earlier date to see")
            print("  the cut. Otherwise a map is missing a hop, or the as-of is wrong.")
        else:
            printed, label, path, title = got
            print("\n  identity today : %s   %s" % (final, title))
            print("  file           : %s" % path)
            print("  label          : %s" % (label or "(none)"))
            print("  the book prints: %s" % (printed or "(unnumbered)"))
    for w in warnings:
        print("\n  NOTE: %s" % w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
