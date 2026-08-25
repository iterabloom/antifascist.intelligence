#!/usr/bin/env python3
"""P1: apply the v4 outline to manuscript/sections. Structure only.

Folds absorbed sections into their survivor, cuts what is ruled cut, and
gathers chapter 8 into a new section. Adds an unnumbered run-in head
(<<h>>...<</h>>) for each absorbed subsection where the survivor is long
enough to need signposts.

NO sentence is rewritten. Text moves; it is not edited. Two things the triage
asks for are therefore NOT done here and are left for the revise pass:
  * `fill` openers for empty headings -- that is writing
  * §1.3's subheading restoration and the compression targets -- also writing

Every word is accounted for: what goes in equals what comes out, plus the cuts.
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

RUNIN_THRESHOLD = 1500
GEO_NUM, GEO_TITLE = "7.5", "The Geopolitics of Ethical AI"


def fname(num):
    return "_".join("%02d" % int(p) for p in num.split(".")) + ".txt"


def body_of(path):
    """Everything after the heading line, verbatim."""
    with open(path, encoding="utf-8", newline="") as f:
        lines = f.readlines()
    return "".join(lines[1:])


def words_in(text):
    out, quote = [], 0
    for line in text.split("\n"):
        s = line.strip()
        if s == "<<quote>>":
            quote += 1
            continue
        if s == "<</quote>>":
            quote -= 1
            continue
        if quote > 0 or s.startswith("#"):
            continue
        if s.startswith("<<h>>") and s.endswith("<</h>>"):
            out.append(s[5:-6])
            continue
        if s.startswith(("<<", "<</")):
            continue
        out.append(s)
    return len(" ".join(out).split())


def main():
    apply = "--apply" in sys.argv
    _, tri = common.read_tsv(os.path.join(common.REPO, "finishing", "triage.tsv"))
    _, v4 = common.read_tsv(os.path.join(common.REPO, "finishing", "toc_v4.tsv"))
    _, order = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))

    path_of = {r["num"]: os.path.join(common.REPO, r["path"]) for r in order}
    title_of = {r["num"]: r["title"] for r in tri}
    fate = {r["num"]: r["fate"] for r in tri}
    est = {r["num"]: int(r["words_est"]) for r in v4}
    absorbs = {r["num"]: ([a for a in r["absorbs"].split(";") if a]) for r in v4}

    before = sum(words_in(body_of(p)) for p in path_of.values())
    cut_nums = [n for n in fate if fate[n] == "cut"]
    cut_words = sum(words_in(body_of(path_of[n])) for n in cut_nums)

    plan, produced, runin_words, runin_n = [], 0, 0, 0
    for r in v4:
        num = r["num"]
        parts = []
        if num == GEO_NUM:
            head = "%s. %s\n" % (GEO_NUM, GEO_TITLE)
        else:
            head = "%s. %s\n" % (num, title_of[num]) if "." in num \
                else "Chapter %s: %s\n" % (num, title_of[num])
            if num in path_of:
                own = body_of(path_of[num])
                if own.strip():
                    parts.append(own.rstrip("\n") + "\n")
        long_enough = est[num] >= RUNIN_THRESHOLD
        last_head = None
        for a in sorted(absorbs[num], key=common.numkey):
            if a not in path_of:
                continue
            b = body_of(path_of[a])
            if not b.strip():
                continue
            # A parent and its child sometimes carry the same title (3.1.2.3 and
            # 3.1.2.3.1 both read "Cognitive and Emotional Processes"). Folding
            # both would print the same run-in head twice with prose between; the
            # first head takes both blocks.
            if long_enough and title_of[a] != last_head:
                parts.append("\n<<h>>%s<</h>>\n" % title_of[a])
                runin_words += len(title_of[a].split())
                runin_n += 1
                last_head = title_of[a]
            parts.append(b.rstrip("\n") + "\n")
        text = head + "\n".join(p.rstrip("\n") for p in parts if p.strip()) + "\n"
        produced += words_in(text[len(head):])
        plan.append((num, text, absorbs[num]))

    print("P1 plan")
    print("  survivors            %4d" % len(plan))
    print("  absorbed             %4d" % sum(len(a) for _, _, a in plan))
    print("  cut                  %4d sections, %d words" % (len(cut_nums), cut_words))
    print("  words before         %7d   (body text only; heading lines excluded)" % before)
    print("  words after          %7d" % produced)
    print("  of which run-in head titles  %5d  (%d heads)" % (runin_words, runin_n))
    print("  cut                  -%6d" % cut_words)
    # A run-in head's words were a numbered heading before and are body text
    # now, so they are new to this accounting without being new to the book.
    balance = produced - runin_words + cut_words
    print("  balance              %7d   (after - run-in titles + cut)" % balance)
    if balance != before:
        print("  MISMATCH of %d words -- refusing to apply" % (before - balance))
        sys.exit(1)
    print("  accounting balances: no body text gained or lost")
    print("  run-in heads in %d sections at or above %d words"
          % (sum(1 for n, _, ab in plan if est[n] >= RUNIN_THRESHOLD and ab),
             RUNIN_THRESHOLD))
    if not apply:
        print("\ndry run; pass --apply to write")
        return

    shutil.rmtree(common.SECTIONS)
    new_order = []
    for num, text, _ in plan:
        d = os.path.join(common.SECTIONS, "ch%02d" % int(num.split(".")[0]))
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, fname(num))
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        import hashlib
        new_order.append({"path": os.path.relpath(p, common.REPO), "num": num,
                          "title": GEO_TITLE if num == GEO_NUM else title_of[num],
                          "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()})
    new_order.sort(key=lambda r: common.numkey(r["num"]))
    common.write_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"),
                     ["path", "num", "title", "sha256"], new_order)
    print("\nwrote %d section files" % len(new_order))


if __name__ == "__main__":
    main()
