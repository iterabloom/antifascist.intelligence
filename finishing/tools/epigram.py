#!/usr/bin/env python3
"""Find the landing line followed by the sentence that qualifies it.

THE SHAPE. A sentence that reads as a conclusion -- short, balanced, quotable --
immediately followed by a sentence carrying the limit, the cost, or the other
half of a two-sided finding. The complaint is not about either sentence. It is
that a reader who stops at the quotable one stops before the argument's honesty,
and the prose has a habit of landing the line and then continuing.

WHERE IT COMES FROM. Four passes made the same repair before anyone named it as
one class: D-234 (P134) on section 2.1.2's detector paragraph, whose own note
recorded "the epigram between the two failure directions, so the second arrived
after the line that reads as a verdict and a reader who stopped at the quotable
sentence stopped one failure short"; D-247 (P147) on section 9.1.5's
update-channel disanalogy; and D-248 (P148) on section 11.1's near-term work.
D-239 (P139) is the family's sibling and not an instance -- it ordered three
qualifications by weight, with no landing line among them.

WHAT IT CANNOT DO, and this is most of what there is to say about it. Whether a
sentence reads as a conclusion is a fact about a reader, and whether the sentence
after it is being discarded is a fact about the same reader. No regular
expression reaches either. What the patterns below select is a SHORT SENTENCE
NEXT TO A LIMITING ONE, which is the shape's silhouette and not the shape. So
every hit is a CANDIDATE FOR A HAND READ, NOT A DEFECT, and this tool is
deliberately not in check_all.sh.

Two things it is blind to by construction. A landing line that is long -- the
manuscript has several at 30 words and more -- falls outside the length test,
because length is the only cheap proxy for quotability. And a qualification that
arrives a paragraph later rather than a sentence later is the same defect with
more distance, which --gap finds only in its one-paragraph form.

THE ORDER THE REPAIR WANTS. State the trade-off before the line, not after it.
That is the author's rule and it is not universal: a limit in final position in a
paragraph is emphatic rather than discarded, so a pair at the end of a paragraph
is weaker evidence than one in the middle. --pairs marks which is which.

  --census      per-section counts, highest first (default)
  --list SEC    every pair in a section, both sentences in full
  --pairs       every pair in the book, ordered by tier
  --tier T      restrict to balanced | copula | short
  --maxwords N  length ceiling for the landing line (default 24)
  --chapter N   restrict any mode to one chapter
  --report      write reports/epigram.tsv
"""
import argparse, glob, io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import tex_prose_line, REPORTS

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

# Sentence-final punctuation followed by a capital. The guards are the
# abbreviations the manuscript actually contains; "e.g." is permitted in body
# prose by D-198 and appears twice.
_ABBR = re.compile(r"\b(?:e\.g|i\.e|cf|vs|Mr|Mrs|Dr|St|No|Art|ch|pp|ed)\.$", re.I)
_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[“\"A-Z])")

# A sentence qualifies the one before it if it opens on a limiting move ...
_OPENER = re.compile(
    r"^(?:But|Yet|Still|Nor|Neither|None|Nothing|No\b|Not\b|Except|Only|Although|"
    r"Though|Whether|What it does|What that does|What the|That is not|It is not|"
    r"Both|Each|Against|Short of|Unless|Where it|Its limit|The limit|The cost|"
    r"The price|The exception|The objection|The qualification|The trouble)\b")
# ... or carries limiting content.
_LIMIT = re.compile(
    r"\b(?:does not|do not|did not|cannot|can not|is not|are not|was not|were not|"
    r"no version|leaves open|leaves it|untouched|does nothing|buys nothing|"
    r"stops short|falls short|fails|the cost|the price|only|neither|nothing|"
    r"unanswered|unsolved|not enough|no route|no mechanism|short of)\b", re.I)

_CONTENT = re.compile(r"\b[a-z]{4,}\b")
_COPULA = re.compile(r"\b(?:is|are|was|were|means|amounts to|comes to)\b")


def sentences(para):
    out, buf = [], ""
    for piece in _SPLIT.split(para):
        buf = (buf + " " + piece).strip() if buf else piece
        if _ABBR.search(buf):
            continue
        out.append(buf)
        buf = ""
    if buf:
        out.append(buf)
    return [s for s in out if s.strip()]


def paragraphs(src):
    """Prose paragraphs, blank-line separated, headings and markup dropped.

    A \\runin head is its own unit and not the first words of the sentence after
    it; leaving it in gave section 11.3 a 14-word landing line that was really a
    head plus a 5-word sentence.
    """
    paras, cur = [], []
    for line in src.split("\n"):
        if line.lstrip().startswith("\\runin{"):
            if cur:
                paras.append(" ".join(cur))
                cur = []
            continue
        if not line.strip():
            if cur:
                paras.append(" ".join(cur))
                cur = []
            continue
        p = tex_prose_line(line)
        if p and p.strip():
            cur.append(re.sub(r"\s+", " ", p.strip()))
    if cur:
        paras.append(" ".join(cur))
    return paras


def sections(chapter=None):
    for f in sorted(glob.glob(os.path.join(ROOT, "manuscript/sections/ch*/*.tex"))):
        src = io.open(f, encoding="utf-8").read()
        m = re.search(r"\\label\{sec:([^}]*)\}", src)
        num = m.group(1) if m else os.path.basename(f)
        if chapter and num.split(".")[0] != str(chapter):
            continue
        yield num, f, paragraphs(src)


def words(s):
    return re.findall(r"[A-Za-z0-9'’-]+", s)


def landing_tier(s, maxwords):
    """Why this sentence reads as a landing line, or None."""
    w = words(s)
    if not (3 <= len(w) <= maxwords):
        return None
    if re.search(r"\d", s):          # a figure is evidence, not an epigram
        return None
    halves = [h for h in re.split(r";|\s+--\s+|\s+—\s+", s) if words(h)]
    if len(halves) >= 2 and all(len(words(h)) >= 3 for h in halves):
        a, b = set(_CONTENT.findall(halves[0].lower())), set(_CONTENT.findall(halves[1].lower()))
        if a & b or ";" in s:
            return "balanced"
    if len(w) <= 16 and _COPULA.search(s):
        return "copula"
    if len(w) <= 12:
        return "short"
    return None


def qualifies(s):
    if _OPENER.match(s):
        return True
    return len(_LIMIT.findall(s)) >= 2


def pairs(chapter=None, maxwords=24):
    for num, path, paras in sections(chapter):
        for pi, para in enumerate(paras):
            sents = sentences(para)
            for i in range(len(sents) - 1):
                a, b = sents[i], sents[i + 1]
                tier = landing_tier(a, maxwords)
                if not tier or not qualifies(b):
                    continue
                final = (i + 2 == len(sents))
                yield dict(num=num, para=pi, tier=tier, a=a, b=b,
                           final=final, alen=len(words(a)), blen=len(words(b)))


TIERS = ("balanced", "copula", "short")

# The second side of a two-sided finding, arriving in a position weaker than the
# first side's. This is what the four named repairs actually had in common --
# D-234's epigram interrupting a pair, D-247's concessive tail inside one
# sentence, D-248's requirement in the last of three prepositional phrases,
# D-239's third-of-three ordering -- and it is NOT "a quotable sentence followed
# by a qualifying one", which the hand read found to be mostly good prose.
_TAIL = re.compile(
    r",\s+(?:and|but|though|although|since|while|which|where)\s+[^,]{0,40}?"
    r"\b(?:not|no|nothing|never|cannot|fails?|only|short of)\b", re.I)


def tails(chapter=None, minwords=18):
    """Sentences whose limit arrives in a trailing subordinate clause."""
    for num, path, paras in sections(chapter):
        for pi, para in enumerate(paras):
            for s in sentences(para):
                w = words(s)
                if len(w) < minwords:
                    continue
                m = _TAIL.search(s)
                if not m:
                    continue
                head = s[:m.start()]
                # The head has to stand on its own as a claim, which is what
                # makes the tail discardable.
                if len(words(head)) < 8:
                    continue
                yield dict(num=num, para=pi, sent=s, head=head,
                           tail=s[m.start():].strip(", "), slen=len(w))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--census", action="store_true")
    ap.add_argument("--list")
    ap.add_argument("--pairs", action="store_true")
    ap.add_argument("--tier", choices=TIERS)
    ap.add_argument("--maxwords", type=int, default=24)
    ap.add_argument("--chapter")
    ap.add_argument("--tails", action="store_true")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    if args.tails:
        rows = list(tails(args.chapter))
        per = {}
        for r in rows:
            per.setdefault(r["num"], []).append(r)
        for num in sorted(per, key=lambda n: -len(per[n])):
            for r in per[num]:
                print("%-8s %s" % (num, r["head"].strip()))
                print("%-8s   TAIL: %s" % ("", r["tail"]))
        print("\n%d sentences in %d sections. Candidates for a hand read, not defects."
              % (len(rows), len(per)))
        return

    rows = [r for r in pairs(args.chapter, args.maxwords)
            if not args.tier or r["tier"] == args.tier]

    if args.list:
        for r in rows:
            if r["num"] != args.list:
                continue
            print("[%s%s] para %d" % (r["tier"], " FINAL" if r["final"] else "", r["para"]))
            print("  LANDS (%dw): %s" % (r["alen"], r["a"]))
            print("  QUALIFIES (%dw): %s" % (r["blen"], r["b"]))
            print()
        return

    if args.pairs:
        for t in TIERS:
            for r in rows:
                if r["tier"] != t:
                    continue
                print("%-8s %-9s %s" % (r["num"], t + ("*" if r["final"] else ""), r["a"]))
                print("%-8s %-9s   -> %s" % ("", "", r["b"][:150]))
        print("\n%d pairs. * = qualification is the paragraph's last sentence, "
              "which is emphatic rather than discarded." % len(rows))
        print("Candidates for a hand read, not defects.")
        return

    if args.report:
        os.makedirs(REPORTS, exist_ok=True)
        out = os.path.join(REPORTS, "epigram.tsv")
        with io.open(out, "w", encoding="utf-8") as fh:
            fh.write("section\ttier\tfinal\tlanding_words\tlanding\tqualifier\n")
            for r in rows:
                fh.write("%s\t%s\t%s\t%d\t%s\t%s\n" % (
                    r["num"], r["tier"], "yes" if r["final"] else "no",
                    r["alen"], r["a"], r["b"]))
        print("wrote %s: %d pairs" % (out, len(rows)))
        return

    per = {}
    for r in rows:
        per.setdefault(r["num"], []).append(r)
    for num in sorted(per, key=lambda n: -len(per[n])):
        rs = per[num]
        print("%-8s %2d  %s" % (num, len(rs),
              " ".join(sorted({r["tier"] + ("*" if r["final"] else "") for r in rs}))))
    mid = sum(1 for r in rows if not r["final"])
    print("\n%d pairs in %d sections; %d mid-paragraph, %d paragraph-final."
          % (len(rows), len(per), mid, len(rows) - mid))
    print("Candidates for a hand read, not defects.")


if __name__ == "__main__":
    main()
