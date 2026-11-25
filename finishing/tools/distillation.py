#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
r"""The chapter-by-chapter distillation: what it covers, and what has gone stale.

finishing/distillation.md summarizes the manuscript, one entry per chapter and
appendix. It is written and checked by agents (finishing/pipeline.md, "The
distillation", says how), never by this tool. This tool does the bookkeeping:

  - A **unit** is one chapter-level heading of the book and the section files
    under it, in ORDER.tsv's reading order: the Preface, the Introduction, each
    chapter and each appendix. The glossary is
    not a unit. A file that carries a \part heading, a part's introduction, or
    \appendix belongs to no unit, so a change to a part's introduction makes
    nothing stale.
  - A unit's **key** is the `num` ORDER.tsv gives its chapter file. That is the
    file's identity, not the number the book prints, so a key survives a
    renumbering. In distillation.md each entry opens with an HTML comment
    naming the key, which a rendered page does not show:

        <!-- unit: 11 -->
        ### 12. A Pipeline Where the People Could Answer

        One or more paragraphs.

  - A unit's **fingerprint** is a sha256 over the path and sha256 of each of
    its files as they stand on disk. finishing/distillation.tsv records, per
    unit, the fingerprint its entry was last brought up to date against, the
    commit that state is in, the date, and who did it. A fingerprint that no
    longer matches is the whole staleness test, as in editions.py.

Stale, missing and orphaned entries are reported, not failed: a chapter changes
first and its entry follows, at the next "make the proofs". What fails --check
is a file or record that is malformed, or entries that are over their target.

  - **The target** (D-1295, D-1296): the entries together are held to
    TARGET_SHARE of the manuscript's word count, 7.4 percent. The manuscript is
    counted as render_markdown.py counts it (`--keys --check`, the text's
    words without its notes); the entries are counted as the words of their
    paragraphs, without marker lines, headings, or the file's opening. --check
    prints both counts every time. Entries over the target fail --check once
    every unit is up to date; while a unit is stale, missing or unrecorded the
    excess is reported and not failed, for the same reason a stale entry is
    not: the chapter changes first.

  distillation.py --check             validate; list stale, missing, orphaned
  distillation.py --stale             the keys that need work, one per line
  distillation.py --units             every unit: key, heading, files, words
  distillation.py --show KEY          one unit: heading, files, state, entry
  distillation.py --diff KEY          what changed in the unit's files since
                                      its entry was recorded (git diff)
  distillation.py --apply FILE        splice the entries in FILE (same format)
                                      into distillation.md, replacing or adding
  distillation.py --fix-headings      rewrite each entry's heading to the one
                                      the book prints now
  distillation.py --record KEY...     record that these entries are up to date
  distillation.py --record-all        the same for every unit with an entry
        --by NAME                     who brought them up to date (required)
"""
import argparse
import datetime
import hashlib
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

REPO = common.REPO
DIST = os.path.join(REPO, "finishing", "distillation.md")
RECORD = os.path.join(REPO, "finishing", "distillation.tsv")
RECORD_COLS = ["key", "heading", "source_sha256", "commit", "date", "by"]
MARK_RE = re.compile(r"^<!-- unit: (\S+) -->\s*$")
SKIP_TITLES = {"Glossary"}
TARGET_SHARE = 0.074


def manuscript_words():
    """The manuscript's word count as render_markdown.py prints it, or None
    with the reason if the render could not be run or read."""
    tool = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_markdown.py")
    try:
        r = subprocess.run([sys.executable, tool, "--keys", "--check"],
                           capture_output=True, text=True, cwd=REPO, timeout=120)
    except (OSError, subprocess.SubprocessError) as exc:
        return None, str(exc)
    m = re.search(r"(\d+) sections, (\d+) words", r.stderr + r.stdout)
    if not m:
        return None, "render_markdown.py --keys --check printed no word count"
    return int(m.group(2)), ""


def _divider(path):
    """A file that belongs to no unit: a part heading or \\appendix."""
    with open(os.path.join(REPO, path), encoding="utf-8") as fh:
        text = fh.read()
    return bool(re.search(r"^\\part(\*|intro)?\b", text, re.M)
                or re.search(r"^\\appendix\s*$", text, re.M))


def units():
    """[{key, heading, files}] in reading order."""
    chapter_at = {}
    for num, title, path, _lineno, numbered in common.printed_headings():
        if "." not in num and path not in chapter_at:
            chapter_at[path] = (num, title, numbered)
    out, cur = [], None
    for r in common.order_rows():
        path = r["path"]
        if path in chapter_at:
            num, title, numbered = chapter_at[path]
            if title in SKIP_TITLES:
                cur = None
                continue
            cur = {"key": r["num"],
                   "heading": "%s. %s" % (num, title) if numbered else title,
                   "files": [path]}
            out.append(cur)
        elif cur is not None and not (r["num"] == "" and _divider(path)):
            cur["files"].append(path)
    keys = [u["key"] for u in out]
    if len(set(keys)) != len(keys) or "" in keys:
        sys.exit("distillation.py: chapter files in ORDER.tsv do not have distinct, non-empty num values")
    return out


def fingerprint(unit):
    h = hashlib.sha256()
    for path in unit["files"]:
        with open(os.path.join(REPO, path), "rb") as fh:
            h.update(("%s\t%s\n" % (path, hashlib.sha256(fh.read()).hexdigest())).encode())
    return h.hexdigest()


def words(unit):
    n = 0
    for path in unit["files"]:
        with open(os.path.join(REPO, path), encoding="utf-8") as fh:
            n += len(fh.read().split())
    return n


def parse(path):
    """(preamble_lines, [entry]) where entry = {key, heading, body, extra}.

    `body` is the entry's text after its heading. `extra` is whatever follows
    the entry that is not part of it: a `## ` part heading before the next
    entry, kept in place when entries are replaced.
    """
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    pre, entries, errors = [], [], []
    i, n = 0, len(lines)
    while i < n and not MARK_RE.match(lines[i]):
        pre.append(lines[i])
        i += 1
    while i < n:
        key = MARK_RE.match(lines[i]).group(1)
        i += 1
        if i >= n or not lines[i].startswith("### "):
            errors.append("unit %s: the marker is not followed by a '### ' heading" % key)
            heading = ""
        else:
            heading = lines[i][4:].strip()
            i += 1
        body, extra = [], []
        while i < n and not MARK_RE.match(lines[i]):
            if extra or re.match(r"^#{1,2} ", lines[i]):
                extra.append(lines[i])
            elif lines[i].startswith("### "):
                errors.append("unit %s: a second '### ' heading with no marker before it" % key)
                body.append(lines[i])
            else:
                body.append(lines[i])
            i += 1
        entries.append({"key": key, "heading": heading,
                        "body": "\n".join(body).strip(),
                        "extra": "\n".join(extra).strip()})
    seen = set()
    for e in entries:
        if e["key"] in seen:
            errors.append("unit %s: more than one entry" % e["key"])
        seen.add(e["key"])
    return pre, entries, errors


def write(pre, entries):
    out = ["\n".join(pre).rstrip("\n"), ""]
    for e in entries:
        out += ["<!-- unit: %s -->" % e["key"], "### %s" % e["heading"], "", e["body"], ""]
        if e["extra"]:
            out += [e["extra"], ""]
    with open(DIST, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out).rstrip("\n") + "\n")


def read_record():
    if not os.path.exists(RECORD):
        return []
    header, rows = common.read_tsv(RECORD)
    if header != RECORD_COLS:
        sys.exit("distillation.py: %s has columns %s, expected %s" % (RECORD, header, RECORD_COLS))
    return rows


def write_record(rows, us):
    pos = {u["key"]: i for i, u in enumerate(us)}
    rows.sort(key=lambda r: pos.get(r["key"], len(pos)))
    common.write_tsv(RECORD, RECORD_COLS, rows)


def state(us, entries, record):
    """key -> 'ok' | 'stale' | 'missing' | 'unrecorded'; plus orphan keys."""
    have = {e["key"]: e for e in entries}
    rec = {r["key"]: r for r in record}
    out = {}
    for u in us:
        k = u["key"]
        if k not in have or not have[k]["body"]:
            out[k] = "missing"
        elif k not in rec:
            out[k] = "unrecorded"
        elif rec[k]["source_sha256"] != fingerprint(u):
            out[k] = "stale"
        else:
            out[k] = "ok"
    known = {u["key"] for u in us}
    orphans = [e["key"] for e in entries if e["key"] not in known]
    return out, orphans


def git(*args):
    return subprocess.run(["git", "-C", REPO] + list(args), capture_output=True, text=True)


def old_files(commit, key):
    """The unit's file list as ORDER.tsv had it at `commit`, or []."""
    r = git("show", "%s:manuscript/sections/ORDER.tsv" % commit)
    if r.returncode != 0:
        return []
    lines = r.stdout.split("\n")
    cols = lines[0].split("\t")
    rows = [dict(zip(cols, ln.split("\t"))) for ln in lines[1:] if ln]
    if "seq" in cols:
        rows.sort(key=lambda x: int(x["seq"]))
    start = next((i for i, x in enumerate(rows) if x["num"] == key), None)
    if start is None:
        return []
    out = [rows[start]["path"]]
    for x in rows[start + 1:]:
        if x["num"] and "." not in x["num"]:
            break
        if x["num"]:
            out.append(x["path"])
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--stale", action="store_true")
    ap.add_argument("--units", action="store_true")
    ap.add_argument("--show", metavar="KEY")
    ap.add_argument("--diff", metavar="KEY")
    ap.add_argument("--apply", metavar="FILE")
    ap.add_argument("--fix-headings", action="store_true")
    ap.add_argument("--record", metavar="KEY", nargs="+")
    ap.add_argument("--record-all", action="store_true")
    ap.add_argument("--by")
    a = ap.parse_args()

    us = units()
    by_key = {u["key"]: u for u in us}

    if a.units:
        for u in us:
            print("%s\t%s\t%d files\t%d words" % (u["key"], u["heading"], len(u["files"]), words(u)))
        return

    if not os.path.exists(DIST):
        sys.exit("distillation.py: %s does not exist" % os.path.relpath(DIST, REPO))
    pre, entries, errors = parse(DIST)
    record = read_record()
    st, orphans = state(us, entries, record)
    have = {e["key"]: e for e in entries}
    rec = {r["key"]: r for r in record}

    def unit_or_exit(key):
        if key not in by_key:
            sys.exit("distillation.py: no unit with key %r (see --units)" % key)
        return by_key[key]

    if a.stale:
        for u in us:
            if st[u["key"]] != "ok":
                print("%s\t%s\t%s" % (u["key"], st[u["key"]], u["heading"]))
        for k in orphans:
            print("%s\torphan\t%s" % (k, have[k]["heading"]))
        return

    if a.show:
        u = unit_or_exit(a.show)
        print("key:      %s" % u["key"])
        print("heading:  %s" % u["heading"])
        print("state:    %s" % st[u["key"]])
        if u["key"] in rec:
            r = rec[u["key"]]
            print("recorded: %s at commit %s by %s" % (r["date"], r["commit"][:12], r["by"]))
        print("files (%d, %d words):" % (len(u["files"]), words(u)))
        for p in u["files"]:
            print("  %s" % p)
        print()
        print(have[u["key"]]["body"] if u["key"] in have else "(no entry)")
        return

    if a.diff:
        u = unit_or_exit(a.diff)
        if u["key"] not in rec:
            sys.exit("distillation.py: unit %s has no recorded state to diff against; read the chapter whole" % u["key"])
        commit = rec[u["key"]]["commit"]
        if git("cat-file", "-e", commit + "^{commit}").returncode != 0:
            sys.exit("distillation.py: commit %s is not in this repository's history; read the chapter whole" % commit[:12])
        paths = sorted(set(u["files"]) | set(old_files(commit, u["key"])))
        sys.stdout.write(git("diff", "--word-diff=plain", commit, "--", *paths).stdout)
        return

    if a.apply:
        _pre, new, errs = parse(a.apply)
        if errs:
            sys.exit("distillation.py: %s is malformed:\n  %s" % (a.apply, "\n  ".join(errs)))
        if not new:
            sys.exit("distillation.py: %s has no '<!-- unit: KEY -->' entries" % a.apply)
        pos = {u["key"]: i for i, u in enumerate(us)}
        for e in new:
            u = unit_or_exit(e["key"])
            if not e["body"]:
                sys.exit("distillation.py: unit %s in %s has an empty entry" % (e["key"], a.apply))
            if e["key"] in have:
                have[e["key"]]["body"] = e["body"]
                have[e["key"]]["heading"] = u["heading"]
                print("replaced  %s  %s" % (e["key"], u["heading"]))
            else:
                item = {"key": e["key"], "heading": u["heading"], "body": e["body"], "extra": ""}
                # After the last existing entry that precedes it in reading order.
                at = 0
                for i, x in enumerate(entries):
                    if pos.get(x["key"], -1) < pos[e["key"]]:
                        at = i + 1
                if at > 0 and entries[at - 1]["extra"]:
                    # Stay inside the part the preceding entry closes only if
                    # the next unit is in it too; otherwise go after the part
                    # heading. A new last chapter of a part is the rarer case,
                    # so the heading stays with the entry before it.
                    item["extra"], entries[at - 1]["extra"] = entries[at - 1]["extra"], ""
                entries.insert(at, item)
                have[e["key"]] = item
                print("added     %s  %s" % (e["key"], u["heading"]))
        write(pre, entries)
        return

    if a.fix_headings:
        n = 0
        for e in entries:
            if e["key"] in by_key and e["heading"] != by_key[e["key"]]["heading"]:
                print("%s: %r -> %r" % (e["key"], e["heading"], by_key[e["key"]]["heading"]))
                e["heading"] = by_key[e["key"]]["heading"]
                n += 1
        if n:
            write(pre, entries)
        print("%d heading(s) rewritten" % n)
        return

    if a.record or a.record_all:
        if not a.by:
            sys.exit("distillation.py: --record needs --by")
        keys = [u["key"] for u in us if u["key"] in have and have[u["key"]]["body"]] if a.record_all else a.record
        head = git("rev-parse", "HEAD").stdout.strip()
        today = datetime.date.today().isoformat()
        for k in keys:
            u = unit_or_exit(k)
            if k not in have or not have[k]["body"]:
                sys.exit("distillation.py: unit %s has no entry to record" % k)
            dirty = git("status", "--porcelain", "--", *u["files"]).stdout.strip()
            if dirty:
                sys.exit("distillation.py: unit %s has uncommitted changes in its files; commit the "
                         "manuscript first, so the recorded commit holds the text the entry was "
                         "checked against:\n%s" % (k, dirty))
        for k in keys:
            u = by_key[k]
            row = {"key": k, "heading": u["heading"], "source_sha256": fingerprint(u),
                   "commit": head, "date": today, "by": a.by}
            if k in rec:
                rec[k].update(row)
            else:
                record.append(row)
                rec[k] = row
        write_record(record, us)
        print("recorded %d unit(s) at commit %s" % (len(keys), head[:12]))
        return

    # --check, and the default.
    for r in record:
        if not re.fullmatch(r"[0-9a-f]{64}", r["source_sha256"]):
            errors.append("record: unit %s: source_sha256 is not a sha256" % r["key"])
        if not re.fullmatch(r"[0-9a-f]{40}", r["commit"]):
            errors.append("record: unit %s: commit is not a full commit id" % r["key"])
        if r["key"] not in have and r["key"] in by_key:
            errors.append("record: unit %s is recorded but has no entry in distillation.md" % r["key"])
    if len({r["key"] for r in record}) != len(record):
        errors.append("record: a unit is recorded more than once")
    for e in errors:
        print("ERROR: %s" % e)
    order = [e["key"] for e in entries if e["key"] in by_key]
    if order != [u["key"] for u in us if u["key"] in set(order)]:
        print("ORDER: the entries are not in the book's reading order")
    for u in us:
        k = u["key"]
        if st[k] == "stale":
            print("STALE: %s (%s): the chapter has changed since %s" % (u["heading"], k, rec[k]["date"]))
        elif st[k] == "missing":
            print("MISSING: %s (%s): no entry" % (u["heading"], k))
        elif st[k] == "unrecorded":
            print("UNRECORDED: %s (%s): an entry nobody has recorded as checked" % (u["heading"], k))
        if k in have and have[k]["heading"] != u["heading"]:
            print("HEADING: %s: entry says %r, the book prints %r (--fix-headings)"
                  % (k, have[k]["heading"], u["heading"]))
    for k in orphans:
        print("ORPHAN: entry %s (%r) matches no chapter in ORDER.tsv" % (k, have[k]["heading"]))
    counts = {s: sum(1 for v in st.values() if v == s) for s in ("ok", "stale", "missing", "unrecorded")}
    print("distillation: %d units, %d up to date, %d stale, %d missing, %d unrecorded, %d orphaned"
          % (len(us), counts["ok"], counts["stale"], counts["missing"], counts["unrecorded"], len(orphans)))
    over = False
    entry_words = sum(len(e["body"].split()) for e in entries if e["key"] in by_key)
    book_words, why = manuscript_words()
    if book_words is None:
        print("TARGET: the manuscript could not be counted (%s); entries %d words, not tested" % (why, entry_words))
    else:
        target = int(round(TARGET_SHARE * book_words))
        print("distillation: entries %d words, %.2f percent of the manuscript's %d; target %.1f percent, %d words"
              % (entry_words, 100.0 * entry_words / book_words, book_words, 100 * TARGET_SHARE, target))
        if entry_words > target:
            behind = counts["stale"] + counts["missing"] + counts["unrecorded"]
            if behind:
                print("OVER TARGET by %d words: not failed while %d unit(s) are behind" % (entry_words - target, behind))
            else:
                over = True
                print("ERROR: the entries are %d words over the target; shorten them (finishing/pipeline.md, "
                      "\"What an entry is\", rule 8)" % (entry_words - target))
    sys.exit(1 if errors or over else 0)


if __name__ == "__main__":
    main()
