#!/usr/bin/env python3
"""Hunt the recurring defect: one proposition conceded in one place and asserted
past the concession in another.

WHY THIS EXISTS. Four instances of one defect were found by outside notes in two
days -- D-328 (section 7.3's enumeration stating a verdict its own later paragraph
split), D-330 (section 3.8 closing on a necessity its penultimate paragraph
conceded), D-331 (section 7.3 again, the hard claim between two concessions inside
one paragraph), D-332 (section 2.1 dismissing six traditions on a ground it
withdraws seven lines later) -- and a fifth was caught in the Foreword's first
sentence at D-336. D-331's lead asked for the pattern to be hunted rather than
waited for. This is that hunt.

WHAT THE DEFECT IS. Not an overclaim: an overclaim is a sentence with nothing
behind it, and reading the rest of the book does not settle it. This is a *pair*.
The book says somewhere that it cannot show X, and says somewhere else that X
follows.

WHAT THE REPAIR COSTS, measured over all fifteen instances the record holds
(D-381, and an earlier draft of this file claimed the opposite): **the diagnosis is
cheap and the repair is usually not the one the diagnosis suggests.** Lowering the
assertion to the concession -- the obvious fix, and what this file first said the
class needs -- describes 5 of the 15. Four needed a paragraph re-analysed or a
claim narrowed with new support. **Five needed a new argument or a sweep across
many sites**: section 3.5's took ten sites read and nine edited, and section 3.7's
exit contradiction was closed only by inventing the compute floor, whose first
statement then *became the next instance of this class*. In four cases the book
already had the honest version in a different section and the repair was to stop
one passage contradicting it, which costs a pointer. And in four of the five
September cases the outside note's proposed repair was declined in favour of a
different one. So a hit here is worth reading and is not worth assuming is a
five-minute edit.

WHAT THE FOUR INSTANCES SHARE, which is what this looks for:
  1. The two members are in one section, or in a section and the section it
     depends on. Three of the four were inside a single section.
  2. The assertion sits in a *closing* position -- last sentence of its
     paragraph, or inside the section's last paragraph. Three of the four.
  3. The concession is explicit. All four. Two shapes: an inability ("I cannot
     say", "does not establish") and a withdrawal, where a later sentence takes
     back a ground the earlier one stood on ("None of the six is distinguished
     from an ethology by having a judge").
Content-word overlap is a *ranking* signal here and not a filter. It was tried as
a filter first and found one of the four: section 3.8's concession and its closer
share almost no vocabulary, because the concession is about the training signal
and the closer is about the fourth way, and a reader supplies the link.

WHAT IT FINDS, MEASURED. Run against the tree as it stood before the four fixes
(9505cd8, worktree), it surfaces three of the five known instances:
  D-331, section 7.3   ranked 1st and 2nd in the section -- the deleted sentence
                       paired with both of the concessions that bracket it
  D-332, section 2.1   ranked 1st -- "needs a judge, a judge needs somebody to
                       appoint him" against "None of the six is distinguished
                       from an ethology by having a judge"
  D-330, section 3.8   about 5th -- the closer is surfaced and paired with the
                       section's concessions, though not first with the one it
                       actually outruns, the two sharing no vocabulary
Two are out of reach and stay out of reach:
  D-328, section 7.3   the defect is a sweep against a *distinction* in section
                       7.1, not against a concession. Nothing in section 7.1 is
                       hedged; it separates two things that section 7.3 then
                       ran together. A concession lexicon cannot see a
                       distinction, and --cross does not help.
  D-336, the Foreword  an overclaim with no concession anywhere to pair against.

WHAT IT CANNOT SEE. Whether a concession and an assertion are about the same
proposition -- that is the hand read this exists to make cheap, and the reason the
default output lays a section's concessions beside its closers instead of
declaring pairs. It is blind to a pair split across two sections with no
cross-reference between them, to a flat declarative assertion carrying no modal
or connective, and to the two instances named above. Register alone is not the
defect: a section that concedes and then asserts something *else* is doing what a
section should, and most of what this prints is that.

Deliberately NOT wired into check_all.sh: the output needs judgment, not a
pass/fail gate.

Usage:
  finishing/tools/hedge_pairs.py                 sections carrying both, ranked
  finishing/tools/hedge_pairs.py --only 3.8      one section, everything in it
  finishing/tools/hedge_pairs.py --pairs         ranked concession/closer pairs
  finishing/tools/hedge_pairs.py --min 0.05      overlap floor for --pairs
  finishing/tools/hedge_pairs.py --census        lexicon hit counts
  finishing/tools/hedge_pairs.py --report        write reports/hedge_pairs.tsv

--report honours --min and --cross, so the flags decide what the committed
report contains. The committed one is written with BOTH:

  finishing/tools/hedge_pairs.py --report --min 0 --cross

--report alone gives a tenth of the rows, because --min defaults to 0.05 and
cross-referenced sections are left out. Regenerating it the short way would
look like the defect had mostly gone away.
"""
import argparse
import csv
import glob
import io
import math
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import tex_prose_line, REPORTS  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

_ABBR = re.compile(r"\b(?:e\.g|i\.e|cf|vs|Mr|Mrs|Dr|St|No|Art|ch|pp|ed)\.$", re.I)
_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[\u201c\"A-Z])")

# CONCESSION. What the book says when it is being careful. Two families:
# inability, and withdrawal of a ground the book itself laid down.
CONCESSIONS = [
    ("cannot-show", r"\b(?:I|we) (?:cannot|can(?:no|')t|do not|don't) "
                    r"(?:show|say|establish|demonstrate|prove|tell|know)\b"),
    ("not-established", r"\b(?:does|do|did|would) not (?:establish|show|prove|"
                        r"settle|demonstrate|entail|follow|make it|mean that)\b"),
    ("unsupported", r"\b(?:unsupported|unestablished|untested|unproven|"
                    r"undemonstrated|not established|no evidence|"
                    r"nothing (?:establishes|in this|here) |"
                    r"nobody has (?:built|shown|established|tested|described))\b"),
    ("hypothesis", r"\b(?:is|remains|as) an? (?:additional |further |open |"
                   r"standing )?(?:hypothesis|conjecture|possibility|"
                   r"open question)\b"),
    ("would-have-to", r"\b(?:would have to|would need to|remains to be|"
                      r"has yet to be|is yet to be|has not been shown)\b"),
    ("open", r"\b(?:leaves? (?:it |that |this )?open|is an open\b|stays open|"
             r"not settled here|is not settled|was not established|"
             r"is an open question)\b"),
    # withdrawal: a contrast the book drew, taken back
    ("withdraws", r"\b(?:narrower than|weaker than|less than it looks|"
                  r"only counts against|counts against this|"
                  r"does not generalize|stops short of|"
                  r"none of (?:the |them)|is not distinguished|"
                  r"nothing distinguishes|that advantage is|"
                  r"does not (?:actually )?turn on|"
                  r"is not what (?:separates|distinguishes))\b"),
    ("may", r"\b(?:it may be that|may turn out|might turn out|"
            r"it is possible that|could be that|on one reading)\b"),
]

# ASSERTION. Modal necessity, inferential connectives, universals, and the two
# constructions the found instances used: "is not an alternative to" and
# "cannot remain".
ASSERTIONS = [
    ("consequently", r"\b(?:consequently|therefore|it follows that|thus\b|"
                     r"hence\b|which is why)\b"),
    ("necessity", r"\b(?:necessarily|must (?:be|have|hold|therefore)|"
                  r"is required|is necessary for|cannot (?:be|remain|hold|"
                  r"exist|do|work) without|is impossible without|"
                  r"there is no way to|needs? (?:a|an|somebody|someone|"
                  r"to be)\b)"),
    ("universal", r"\b(?:every one of them|all of them are|in every case|"
                  r"always|never\b|no such|any such|without exception|"
                  r"invariably)\b"),
    ("not-optional", r"\b(?:is not an alternative|nor an optional|"
                     r"not optional|is not a matter of|is not merely)\b"),
    ("establishes", r"\b(?:establishes that|shows that|proves that|"
                    r"demonstrates that|entails)\b"),
    ("contradiction", r"\b(?:are in contradiction|is a contradiction|"
                      r"cannot both|is incompatible with)\b"),
    # D-397: the noun here was enumerated -- way|route|thing|mechanism -- and
    # the book has 41 "the only X" sentences of which that caught 9. The one it
    # missed that mattered is the author's own, at 3.2: "it is the only step by
    # which the specification bears on the route", labelled in the same breath
    # as this book's central inference. An enumeration over forms is defeated by
    # a new form -- which is section 3.6's own argument about floor terms,
    # arriving in the instrument built to hunt for overclaims. The noun is now
    # any word: 9 to 41 sentences, and the 32 added include "the only currency",
    # "the only party", "the only channel" and "the only position".
    ("only-way", r"\b(?:the only [a-z]+|the whole of|exactly what it takes)\b"),
]

CONC_RE = [(n, re.compile(p, re.I)) for n, p in CONCESSIONS]
ASRT_RE = [(n, re.compile(p, re.I)) for n, p in ASSERTIONS]

_WORD = re.compile(r"\b[a-z][a-z'-]{3,}\b")
STOP = set("""about above after again against also although among another any
back because been before being below between both came come could does doing
done down during each either else enough even ever every first from further
give given gives goes going gone half have having here hold holds however
into itself just kept know known last least less like made make makes many
more most much must never next none nothing offer offers once only other
others over own part parts place puts rather same says seem seems several
shall since some someone something still such take takes tell than that
their them then there these they thing things this those three through time
took toward under until upon used uses very want wants well were what when
where whether which while will with within without word words work works
would your""".split())


def paragraphs(src):
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


def load():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, "manuscript/sections/ch*/*.tex"))):
        src = io.open(f, encoding="utf-8").read()
        m = re.search(r"\\(?:unnumbered)?label\{sec:([^}]*)\}", src)
        num = m.group(1) if m else os.path.basename(f)
        out.append((num, f, [sentences(p) for p in paragraphs(src)]))
    return out


def content(s):
    return {w for w in _WORD.findall(s.lower()) if w not in STOP}


def idf(secs):
    """Inverse document frequency over sections: a word in one section is
    distinctive even when that section repeats it."""
    df = Counter()
    for num, path, paras in secs:
        seen = set()
        for para in paras:
            for s in para:
                seen |= content(s)
        for w in seen:
            df[w] += 1
    n = len(secs)
    return {w: math.log(n / c) for w, c in df.items()}


def overlap(a, b, weights):
    if not a or not b:
        return 0.0
    inter = sum(weights.get(w, 0.0) for w in (a & b))
    union = sum(weights.get(w, 0.0) for w in (a | b))
    return inter / union if union else 0.0


class Sent(object):
    __slots__ = ("num", "pi", "si", "text", "conc", "asrt", "closer", "words")

    def __init__(self, num, pi, si, text, npara, nsent, lastpara):
        self.num, self.pi, self.si, self.text = num, pi, si, text
        self.conc = [n for n, rx in CONC_RE if rx.search(text)]
        asrt = [n for n, rx in ASRT_RE if rx.search(text)]
        # A sentence that concedes and asserts in the same breath is conceding:
        # "What I cannot say is that it is always legible" is the careful
        # register, and counting it as an assertion was this tool's first and
        # loudest false positive.
        self.asrt = [] if self.conc else asrt
        self.closer = (si == nsent - 1) or (pi == lastpara)
        self.words = content(text)

    def where(self):
        return "p%d.%d" % (self.pi, self.si)


def scan(secs, only=None):
    by = {}
    for num, path, paras in secs:
        if only and num != only:
            continue
        lastpara = len(paras) - 1
        rows = []
        for pi, para in enumerate(paras):
            for si, text in enumerate(para):
                rows.append(Sent(num, pi, si, text, len(paras), len(para),
                                 lastpara))
        by[num] = rows
    return by


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--cross", action="store_true",
                    help="also pair a section's assertions against concessions "
                         "in the sections it cross-references, which is the "
                         "shape of D-328")
    ap.add_argument("--pairs", action="store_true")
    ap.add_argument("--min", type=float, default=0.05)
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--census", action="store_true")
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args()

    secs = load()
    weights = idf(secs)
    by = scan(secs, args.only)

    if args.census:
        cc, ac = Counter(), Counter()
        cs, as_ = {}, {}
        for num, rows in by.items():
            for r in rows:
                for n in r.conc:
                    cc[n] += 1
                    cs.setdefault(n, set()).add(num)
                for n in r.asrt:
                    ac[n] += 1
                    as_.setdefault(n, set()).add(num)
        print("%-12s %-16s %6s %9s" % ("kind", "class", "hits", "sections"))
        for n, c in cc.most_common():
            print("%-12s %-16s %6d %9d" % ("concession", n, c, len(cs[n])))
        for n, c in ac.most_common():
            print("%-12s %-16s %6d %9d" % ("assertion", n, c, len(as_[n])))
        nc = sum(1 for rs in by.values() for r in rs if r.conc)
        na = sum(1 for rs in by.values() for r in rs if r.asrt)
        ncl = sum(1 for rs in by.values() for r in rs if r.asrt and r.closer)
        print("\n%d concessions, %d assertions, %d of the assertions in a "
              "closing position" % (nc, na, ncl))
        print("%d sections scanned" % len(by))
        return

    # candidate pairs: a concession and an assertion in one section, and with
    # --cross in a section it points at
    refs = {}
    if args.cross:
        for num, path, paras in secs:
            src = io.open(path, encoding="utf-8").read()
            refs[num] = set(re.findall(r"\\(?:auto)?ref\{sec:([0-9.]+)\}", src))
    pairs = []
    for num, rows in by.items():
        conc = [r for r in rows if r.conc]
        asrt = [r for r in rows if r.asrt]
        for t in refs.get(num, ()):
            conc = conc + [r for r in by.get(t, ()) if r.conc]
        for a in asrt:
            for c in conc:
                o = overlap(a.words, c.words, weights)
                samesec = a.num == c.num
                samepara = samesec and a.pi == c.pi
                # score: overlap, plus the positional facts the four found
                # instances shared. Proximity breaks the many ties at overlap
                # zero -- a concession three paragraphs from the assertion is a
                # likelier pair than one twenty paragraphs away, and D-330's is
                # eight.
                near = (1.0 / (1 + abs(a.pi - c.pi))) if samesec else 0.0
                score = o + (0.06 if a.closer else 0.0) + \
                    (0.06 if samepara else 0.0) + 0.04 * near
                pairs.append((score, o, num, a, c, samepara))
    pairs.sort(key=lambda t: -t[0])

    if args.report:
        out = os.path.join(REPORTS, "hedge_pairs.tsv")
        with io.open(out, "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(["score", "overlap", "num", "same_para", "closer",
                        "shared", "assertion_class", "assertion",
                        "concession_class", "concession"])
            for score, o, num, a, c, sp in pairs:
                if score < args.min:
                    continue
                shared = sorted(a.words & c.words,
                                key=lambda w_: -weights.get(w_, 0))[:6]
                w.writerow(["%.3f" % score, "%.3f" % o, num,
                            "yes" if sp else "", "yes" if a.closer else "",
                            " ".join(shared), "|".join(a.asrt), a.text,
                            "|".join(c.conc), c.text])
        print("wrote %s: %d rows" % (out, sum(1 for p in pairs
                                              if p[0] >= args.min)))
        return

    if args.pairs or args.only:
        shown = 0
        for score, o, num, a, c, sp in pairs:
            if score < args.min:
                continue
            if shown >= args.top:
                break
            shown += 1
            shared = sorted(a.words & c.words,
                            key=lambda w_: -weights.get(w_, 0))[:6]
            print("== %.3f (overlap %.3f) section %s%s%s  [%s]" %
                  (score, o, num, "  same paragraph" if sp else "",
                   "  closer" if a.closer else "", " ".join(shared)))
            print("   ASSERTS  (%s) %s  %s" %
                  (",".join(a.asrt), a.where(), a.text))
            print("   CONCEDES (%s) %s%s  %s" %
                  (",".join(c.conc),
                   "" if c.num == a.num else "section %s " % c.num,
                   c.where(), c.text))
            print()
        print("%d pairs at score >= %.2f; %d shown" %
              (sum(1 for p in pairs if p[0] >= args.min), args.min, shown))
        return

    # default: sections carrying both, ranked by how much material a hand read
    # would have to weigh
    print("%-7s %5s %5s %6s   %s" %
          ("section", "conc", "asrt", "closer", "top pair"))
    rows = []
    for num, srows in by.items():
        nc = sum(1 for r in srows if r.conc)
        na = sum(1 for r in srows if r.asrt)
        ncl = sum(1 for r in srows if r.asrt and r.closer)
        if not (nc and na):
            continue
        best = max((p for p in pairs if p[2] == num), key=lambda t: t[0],
                   default=None)
        rows.append((ncl, nc * na, num, nc, na, ncl, best))
    rows.sort(key=lambda t: (-t[0], -t[1]))
    for _, _, num, nc, na, ncl, best in rows:
        tp = "%.3f %s" % (best[0], best[3].text[:70]) if best else ""
        print("%-7s %5d %5d %6d   %s" % (num, nc, na, ncl, tp))
    print("\n%d sections carry both a concession and an assertion, of %d"
          % (len(rows), len(by)))


if __name__ == "__main__":
    main()
