#!/usr/bin/env python3
"""Derive the v4 outline from the triage rulings.

Mechanical: apply fold / cut / move to the current outline and see what
survives, renumbering the survivors. Writes finishing/toc_v4.tsv (the new
outline with its provenance) and reports/toc_v4.md (readable).
"""
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

GEO = ("7.5", "The Geopolitics of Ethical AI")  # chapter 8 lands here (D-010)


def main():
    _, tri = common.read_tsv(os.path.join(common.REPO, "finishing", "triage.tsv"))
    _, st = common.read_tsv(os.path.join(common.REPORTS, "section_stats.tsv"))
    words = {r["num"]: int(r["words"]) for r in st}
    fate = {r["num"]: r["fate"] for r in tri}
    title = {r["num"]: r["title"] for r in tri}
    target = {r["num"]: r["target"] for r in tri}

    def survivor(num):
        """Nearest ancestor that keeps its heading."""
        parts = num.split(".")
        while len(parts) > 1:
            parts = parts[:-1]
            anc = ".".join(parts)
            if fate.get(anc) in ("revise", "keep", "fill", "done", None):
                return anc
        return parts[0]

    absorbed = collections.defaultdict(list)
    rows, cut, moved = [], [], []
    for r in tri:
        num, f = r["num"], r["fate"]
        if f == "cut":
            cut.append(num)
            continue
        if f == "move":
            moved.append(num)
            continue
        # a row marked done can still owe a structural fold; the target column
        # carries it as pending_fold:<dest>
        if "pending_fold:" in target.get(num, ""):
            dest = target[num].split("pending_fold:")[1].split(";")[0].strip()
            absorbed[dest].append(num)
            continue
        if f in ("fold", "merge"):
            dest = target[num] if (f == "merge" and target[num] and
                                   not target[num].isdigit()) else survivor(num)
            absorbed[dest].append(num)
            continue
        rows.append(r)

    rows.sort(key=lambda r: common.numkey(r["num"]))
    out = []
    for r in rows:
        num = r["num"]
        w = words.get(num, 0) + sum(words.get(a, 0) for a in absorbed.get(num, []))
        tgt = target.get(num, "")
        if tgt.isdigit():
            w = int(tgt)
        out.append({"num": num, "title": title[num], "level": common.level(num),
                    "words_est": w,
                    "absorbs": ";".join(sorted(absorbed.get(num, []), key=common.numkey)),
                    "fate": r["fate"]})
    # the merged geopolitics section
    out.append({"num": GEO[0], "title": GEO[1], "level": 2, "words_est": 5000,
                "absorbs": ";".join(sorted(moved, key=common.numkey)), "fate": "new"})
    out.sort(key=lambda r: common.numkey(r["num"]))

    common.write_tsv(os.path.join(common.REPO, "finishing", "toc_v4.tsv"),
                     ["num", "title", "level", "words_est", "absorbs", "fate"], out)

    lines = ["# Outline v4", "",
             "Derived from the triage rulings by `finishing/tools/toc_v4.py`. "
             "Folds, cuts and the chapter-8 move applied; survivors keep their numbers "
             "for now, so the crosswalk stays legible.", "",
             "Word estimates are **pre-transplant**: the 10,400 words of D-014 "
             "material land inside these sections during the revise pass and are "
             "not counted below.", "",
             "**%d sections** (from 282), **~%d words** projected. "
             "%d sections absorbed into a parent, %d cut, %d moved into §7.5."
             % (len(out), sum(r["words_est"] for r in out),
                sum(len(v) for v in absorbed.values()), len(cut), len(moved)), ""]
    for r in out:
        ind = "  " * (r["level"] - 1)
        lab = ("Chapter %s: %s" % (r["num"], r["title"])) if r["level"] == 1 \
            else ("%s. %s" % (r["num"], r["title"]))
        lines.append("%s- **%s** — %d w%s" % (
            ind, lab, r["words_est"],
            ("  \n%s  *absorbs:* %s" % (ind, r["absorbs"].replace(";", ", "))) if r["absorbs"] else ""))
    lines += ["", "## Cut (%d)" % len(cut), "", ", ".join(cut) or "none", ""]
    with open(os.path.join(common.REPORTS, "toc_v4.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    depth = collections.Counter(r["level"] for r in out)
    print("v4 outline: %d sections (from 282), ~%d words"
          % (len(out), sum(r["words_est"] for r in out)))
    print("  depth:", "  ".join("L%d=%d" % (k, depth[k]) for k in sorted(depth)))
    print("  absorbed %d, cut %d, moved %d"
          % (sum(len(v) for v in absorbed.values()), len(cut), len(moved)))
    by_ch = collections.Counter()
    wch = collections.Counter()
    for r in out:
        c = r["num"].split(".")[0]
        by_ch[c] += 1
        wch[c] += r["words_est"]
    for c in sorted(by_ch, key=int):
        print("  ch%-2s %2d sections %7d words" % (c, by_ch[c], wch[c]))


if __name__ == "__main__":
    main()
