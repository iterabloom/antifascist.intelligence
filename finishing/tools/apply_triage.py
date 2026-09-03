#!/usr/bin/env python3
"""Merge ruled fates from staged TSV files into finishing/triage.tsv.

Input files are tab-separated: num, fate, target, why. Rows already carrying a
fate in triage.tsv are NOT overwritten unless --force, so the author's own
rulings always win over a delegated one.

Checks as it goes:
  * every num exists in triage.tsv
  * no num ruled twice across input files
  * forced fates are respected: level > 3 must be fold (or move for chapter 8),
    6.4.1.1-.9 must be cut
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

VALID = {"keep", "revise", "fold", "move", "merge", "cut", "fill", "done"}

# `done` means the prose work is finished. It says nothing about the heading:
# a done section deeper than three levels still folds when P1 runs. The two
# questions -- what happens to this text, what happens to this heading -- are
# separate, and `pending_fold` in the notes carries the second.


def forced(num, level):
    parts = num.split(".")
    if num.startswith("6.4.1.") and len(parts) == 4 and parts[3].isdigit() \
            and 1 <= int(parts[3]) <= 9:
        return "cut"
    if parts[0] == "8":
        return "move"
    if level > 3:
        return "fold"
    return None


def main():
    force = "--force" in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith("-")]
    hdr, rows = common.read_tsv(os.path.join(common.REPO, "finishing", "triage.tsv"))
    by_num = {r["num"]: r for r in rows}

    seen, applied, skipped, problems = {}, 0, 0, []
    for path in files:
        with open(path, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                line = line.rstrip("\n")
                if not line.strip():
                    continue
                parts = line.split("\t")
                while len(parts) < 4:
                    parts.append("")
                num, fate, target, why = parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip()
                if num not in by_num:
                    problems.append("%s:%d unknown section %r" % (os.path.basename(path), lineno, num))
                    continue
                if fate not in VALID:
                    problems.append("%s:%d invalid fate %r for %s" % (os.path.basename(path), lineno, fate, num))
                    continue
                if num in seen:
                    problems.append("%s ruled twice (%s and %s)" % (num, seen[num], os.path.basename(path)))
                    continue
                seen[num] = os.path.basename(path)
                r = by_num[num]
                if r["fate"] and not force:
                    # already ruled (by the author, or by an earlier pass);
                    # do not validate an incoming ruling we are going to ignore
                    skipped += 1
                    continue
                want = forced(num, int(r["level"]))
                if want and fate != want:
                    problems.append("%s ruled %r but is forced %r" % (num, fate, want))
                    continue
                r["fate"], r["target"], r["why"] = fate, target, why
                applied += 1

    if problems:
        print("PROBLEMS (%d) — nothing written:" % len(problems))
        for p in problems:
            print("  " + p)
        sys.exit(1)

    common.write_tsv(os.path.join(common.REPO, "finishing", "triage.tsv"), hdr, rows)
    ruled = sum(1 for r in rows if r["fate"])
    print("applied %d, skipped %d already-ruled; %d of %d rows now have a fate"
          % (applied, skipped, ruled, len(rows)))
    unruled = [r["num"] for r in rows if not r["fate"]]
    if unruled:
        print("still unruled (%d): %s" % (len(unruled), ", ".join(unruled[:20])))


if __name__ == "__main__":
    main()
