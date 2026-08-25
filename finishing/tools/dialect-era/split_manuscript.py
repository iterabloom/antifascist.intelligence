#!/usr/bin/env python3
"""Split the manuscript into one file per section, byte-exactly.

Each section file is the raw slice from its heading line through the line
before the next heading, heading included, whitespace preserved. The dialect
(<<quote>>, <<list>>, '#' notes) is kept unchanged so the joined file stays
parseable by the 2023/2024 generation notebooks.

Filenames are zero-padded per number component so a sorted glob reproduces
book order. Aborts if the regex heading scan and the outline disagree.
"""
import hashlib
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def fname(num):
    """Zero-padded, '_'-separated: a plain sorted glob then reproduces book order.

    '_' matters: with '.' as the separator, '03.03.03.txt' sorts BEFORE
    '03.03.txt' (because '.' < 't'), putting children ahead of their parent.
    With '_', the parent's '.txt' ('.' = 0x2E) beats the child's '_' (0x5F).
    """
    return "_".join("%02d" % int(p) for p in num.split(".")) + ".txt"


def main():
    force = "--force" in sys.argv
    src = common.V3B
    if os.path.exists(common.SECTIONS):
        if not force:
            sys.exit("%s exists; refusing (use --force)" % common.SECTIONS)
        shutil.rmtree(common.SECTIONS)

    with open(src, encoding="utf-8", newline="") as f:
        lines = f.readlines()
    heads = common.headings_in(src)
    if not heads:
        sys.exit("no headings found")
    if heads[0][0] != 1:
        sys.exit("text before the first heading (line %d); handle a preamble file" % heads[0][0])

    _, outline_rows = common.read_tsv(common.OUTLINE_TSV)
    ol = {r["num"]: r["title"] for r in outline_rows}
    ms = {n: t for _, n, t, _ in heads}
    if set(ms) != set(ol):
        sys.exit("heading NUMBER sets differ from outline.tsv: only-ms=%s only-outline=%s"
                 % (sorted(set(ms) - set(ol)), sorted(set(ol) - set(ms))))
    title_diffs = [(n, ms[n], ol[n]) for n in ms if ms[n] != ol[n]]

    starts = [h[0] for h in heads]
    order = []
    for i, (ln, num, title, _) in enumerate(heads):
        end = starts[i + 1] - 1 if i + 1 < len(starts) else len(lines)
        chunk = "".join(lines[ln - 1:end])
        ch = num.split(".")[0]
        d = os.path.join(common.SECTIONS, "ch%02d" % int(ch))
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, fname(num))
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(chunk)
        order.append({"path": os.path.relpath(path, common.REPO),
                      "num": num, "title": title,
                      "sha256": hashlib.sha256(chunk.encode("utf-8")).hexdigest()})

    common.write_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"),
                     ["path", "num", "title", "sha256"], order)
    print("wrote %d section files under %s" % (len(order), common.SECTIONS))
    if title_diffs:
        print("NOTE title differs from outline.tsv (manuscript text wins in the file):")
        for n, a, b in title_diffs:
            print("  %s\n    manuscript: %s\n    outline:    %s" % (n, a, b))


if __name__ == "__main__":
    main()
