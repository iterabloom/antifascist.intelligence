#!/usr/bin/env python3
"""Census the bare demonstrative opening, and locate every instance for a hand read.

The shape is a sentence that opens on *This*, *That*, *These*, *Those*, *It* or
*They* with a verb straight after it and no noun naming what the pronoun stands
for -- "That is refusal tracking its own rationale", "They were written as the
learned half". The repair the author proposes costs two words: name the referent
in the subject, "That requirement is", "Chapters 4 and 5 were written".

WHAT THIS IS FOR, AND WHAT IT CANNOT DO. Whether a bare opening is a defect is
not a fact about the sentence carrying it. It is a fact about the sentence
BEFORE it: a reader coming off six plain words resolves "That is" without
noticing, and a reader coming off a fifty-word sentence with three clauses has
to go back and pick which clause. So the count below is not a defect count, and
the hits are CANDIDATES FOR A HAND READ. The tool is deliberately not in
check_all.sh.

reader_tax.py already carries a narrower version of this class as `deixis`,
232 hits from one anchored pattern over three pronouns and six verbs; D-117
recorded that most of that pool is fine. This tool widens the pattern to the
class the author described and adds the half that discriminates.

THE TIERS, which are the point. Every hit is graded by what the reader has to do
to resolve it:

  para-initial  the sentence opens its paragraph, so the referent is in the
                paragraph before it or is that paragraph's whole subject. The
                reader crosses a boundary to find it. Hardest.
  after-long    the preceding sentence runs >= 40 words, which is the author's
                own stated condition. The referent is present but has to be
                picked out of a sentence with several candidates.
  after-short   the preceding sentence is under 40 words. The referent is close,
                usually the sentence's whole content, and the pronoun is doing
                ordinary work.

`--clauses N` narrows after-long further by counting clause boundaries -- commas,
semicolons, colons and dashes -- in the preceding sentence, the second half of
the author's condition.

  --census      per-chapter counts by tier, and the rate per 1,000 words (default)
  --list SEC    every instance in a section, with the sentence before it
  --tier NAME   restrict --census or --hard to one tier
  --hard        every para-initial and after-long instance, book order: the read
  --clauses N   for --hard, require N+ clause boundaries in the preceding sentence
  --chapter N   restrict any mode to one chapter
"""
import argparse, glob, io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import tex_prose_line, section_labels, chapter_numbers, numkey

PRONOUNS = r"(?:This|That|These|Those|It|They)"

# Verb forms that can stand immediately after the pronoun. An optional adverb
# slot lets "That is not", "This also is" and "It simply does" through.
VERBS = (
    r"(?:is|was|are|were|has|have|had|does|do|did|will|would|can|could|may|might|"
    r"shall|should|must|makes|made|leaves|left|gives|gave|means|meant|seems|seemed|"
    r"becomes|became|remains|remained|requires|required|needs|needed|comes|came|"
    r"goes|went|works|worked|holds|held|turns|turned|puts|put|takes|took|sits|sat|"
    r"runs|ran|follows|followed|matters|mattered|applies|applied|happens|happened|"
    r"depends|depended|carries|carried|counts|counted|says|said|shows|showed|"
    r"stands|stood|rests|rested|reaches|reached|produces|produced|costs|cost|"
    r"buys|bought|breaks|broke|falls|fell|raises|raised|names|named|lets|let)"
)
ADVERBS = r"(?:not |also |already |still |only |simply |never |always |now |then |therefore |however )?"

OPENING = re.compile(r"^%s\s+%s\b%s\b" % (PRONOUNS, ADVERBS, VERBS))

LONG = 40


def sections(chapter=None):
    """Yield (path, label, prose). The locator is the label (D-470).

    It was derived from the filename here, which D-464's rename made agree with
    the printed number for chapters 1 to 16 by accident -- and which called the
    Preface `1`, colliding with chapter 1, and the appendix `17` where the book
    prints A. `--chapter` matches the printed number, from the path.
    """
    labels, chapters = section_labels(), chapter_numbers()
    for path in sorted(glob.glob("manuscript/sections/ch*/*.tex")):
        src = io.open(path, encoding="utf-8").read()
        if chapter and chapters.get(path) != str(chapter):
            continue
        yield (path, labels.get(path, os.path.basename(path)),
               "\n".join(tex_prose_line(l) or "" for l in src.split("\n")))


def paragraphs(body):
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]


def sentences(p):
    return [s.strip() for s in re.split(r"(?<=[.!?]) +", p) if s.strip()]


def words(s):
    return len(s.split())


def clause_marks(s):
    return len(re.findall(r"[,;:]|\s—\s|\s--\s", s))


def hits(chapter=None):
    """Yield (label, tier, sentence, previous_sentence, prev_words, prev_clauses)."""
    for path, num, body in sections(chapter):
        for p in paragraphs(body):
            ss = sentences(p)
            for i, s in enumerate(ss):
                if not OPENING.match(s):
                    continue
                if i == 0:
                    yield num, "para-initial", s, "", 0, 0
                else:
                    prev = ss[i - 1]
                    w, c = words(prev), clause_marks(prev)
                    tier = "after-long" if w >= LONG else "after-short"
                    yield num, tier, s, prev, w, c


TIERS = ("para-initial", "after-long", "after-short")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--census", action="store_true")
    ap.add_argument("--list", metavar="LABEL",
                    help="a heading label, as the locator column prints it")
    ap.add_argument("--hard", action="store_true")
    ap.add_argument("--tier", choices=TIERS)
    ap.add_argument("--clauses", type=int, default=0)
    ap.add_argument("--chapter", help="the number the book prints: 1..16, or A")
    a = ap.parse_args()

    rows = list(hits(a.chapter))

    if a.list:
        for num, tier, s, prev, w, c in rows:
            if num != a.list:
                continue
            print("[%s]" % tier)
            if prev:
                print("  prev (%dw, %d clauses): %s" % (w, c, prev))
            print("  HIT: %s\n" % s)
        return

    if a.hard:
        n = 0
        for num, tier, s, prev, w, c in rows:
            if tier == "after-short":
                continue
            if a.tier and tier != a.tier:
                continue
            if tier == "after-long" and c < a.clauses:
                continue
            n += 1
            print("%-26s %-13s %s" % (num, tier, s[:100]))
            if prev:
                print("%-26s %-13s   <- %dw %dc: %s" % ("", "", w, c, prev[-90:]))
        print("\n%d instances" % n)
        return

    # census
    tot = {t: 0 for t in TIERS}
    bych = {}
    # A label carries no chapter, so the rollup takes the chapter from the path.
    _labels = section_labels()
    lab2ch = {_labels.get(p, os.path.basename(p)): ch
              for p, ch in chapter_numbers().items()}
    for num, tier, s, prev, w, c in rows:
        tot[tier] += 1
        ch = lab2ch.get(num, "?")
        bych.setdefault(ch, {t: 0 for t in TIERS})[tier] += 1
    wordcount = {}
    sentcount = {}
    for path, num, body in sections(a.chapter):
        ch = lab2ch.get(num, "?")
        wordcount[ch] = wordcount.get(ch, 0) + len(body.split())
        sentcount[ch] = sentcount.get(ch, 0) + sum(len(sentences(p)) for p in paragraphs(body))

    print("%-4s %13s %11s %12s %8s %8s %7s" %
          ("ch", "para-initial", "after-long", "after-short", "total", "sents", "pct"))
    for ch in sorted(bych, key=numkey):
        d = bych[ch]
        t = sum(d.values())
        print("%-4s %13d %11d %12d %8d %8d %6.1f%%" %
              (ch, d["para-initial"], d["after-long"], d["after-short"], t,
               sentcount.get(ch, 0), 100.0 * t / max(1, sentcount.get(ch, 1))))
    grand = sum(tot.values())
    allsent = sum(sentcount.values())
    print("%-4s %13d %11d %12d %8d %8d %6.1f%%" %
          ("all", tot["para-initial"], tot["after-long"], tot["after-short"],
           grand, allsent, 100.0 * grand / max(1, allsent)))
    print("\nmechanical pool: %d of %d sentences (%.1f%%)" % (grand, allsent, 100.0 * grand / allsent))
    print("the author's condition (para-initial + after-long): %d (%.1f%% of sentences, %.0f%% of the pool)"
          % (tot["para-initial"] + tot["after-long"],
             100.0 * (tot["para-initial"] + tot["after-long"]) / allsent,
             100.0 * (tot["para-initial"] + tot["after-long"]) / grand))


if __name__ == "__main__":
    main()
