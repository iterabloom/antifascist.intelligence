#!/usr/bin/env python3
"""Find run-on enumerations that are NOT wrapped in <<list>>.

The dialect's <<list>> markup was used in some chapters and abandoned in others;
a typeset pass needs the unmarked ones found and converted (or prosed).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

OUT = os.path.join(common.REPORTS, "list_candidates.tsv")
ITEM = re.compile(r"^\s*(\(\d+\)|\d+[.)]|[-•*]|[a-z][.)])\s+\S")


def marker_style(line):
    m = ITEM.match(line)
    tok = m.group(1)
    if tok.startswith("("):
        return "(n)"
    if tok[0].isdigit():
        return "n." if tok.endswith(".") else "n)"
    if tok[0] in "-•*":
        return "bullet"
    return "alpha"


def main():
    _, order = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    order.sort(key=lambda r: common.numkey(r["num"]))
    rows = []
    for r in order:
        with open(os.path.join(common.REPO, r["path"]), encoding="utf-8", newline="") as f:
            lines = f.readlines()
        inlist = 0
        run = []
        for ln, line in enumerate(lines, 1):
            s = line.strip()
            if s == "<<list>>":
                inlist += 1
                continue
            if s == "<</list>>":
                inlist -= 1
                continue
            if inlist > 0 or not s:
                if run and not s:
                    pass  # blank lines separate items in this dialect; keep the run open
                continue
            if ITEM.match(line):
                run.append((ln, marker_style(line)))
            else:
                if len(run) >= 2:
                    rows.append({"num": r["num"], "start": run[0][0], "end": run[-1][0],
                                 "items": len(run), "style": run[0][1]})
                run = []
        if len(run) >= 2:
            rows.append({"num": r["num"], "start": run[0][0], "end": run[-1][0],
                         "items": len(run), "style": run[0][1]})
    common.write_tsv(OUT, ["num", "start", "end", "items", "style"], rows)
    total = sum(r["items"] for r in rows)
    print("wrote %s: %d unmarked runs, %d items, in %d sections"
          % (OUT, len(rows), total, len({r["num"] for r in rows})))
    by_ch, by_style = {}, {}
    for r in rows:
        ch = r["num"].split(".")[0]
        by_ch[ch] = by_ch.get(ch, 0) + r["items"]
        by_style[r["style"]] = by_style.get(r["style"], 0) + r["items"]
    print("  by chapter: " + "  ".join("ch%s=%d" % (c, by_ch[c]) for c in sorted(by_ch, key=int)))
    print("  by style:   " + "  ".join("%s=%d" % kv for kv in sorted(by_style.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
