#!/usr/bin/env python3
"""Check that nothing was lost between two Markdown renders of the book.

The move of the main text into notes (D-906) deletes nothing: every sentence
of the book before it should stand in the book after it, in the body or in a
note, changed at most by the grammatical repair a move requires. This tool
reads two renders from finishing/tools/render_markdown.py and says so, or
names what is missing.

    finishing/tools/sentence_coverage.py OLD.md NEW.md
    finishing/tools/sentence_coverage.py OLD.md NEW.md --chapters 1-3
    finishing/tools/sentence_coverage.py OLD.md NEW.md --old-has-citation-notes

Both files are normalized the same way: note markers, note-definition
prefixes and citation keys dropped, Markdown furniture and indentation
stripped, case folded, curly quotes and dashes unified, whitespace collapsed.
Each line is then split into sentences at . ! ? followed by a space, and
fragments under four words are left out. For every sentence of the old side
the report says whether it stands in the new side exactly, nearly (the best
match by difflib ratio at or above --ratio, printed with both forms, to be
read as a repair), or not at all. The exit status is 1 when anything is
missing.

--chapters A-B restricts the old side to those chapters (the text between
the "## A." heading and the next chapter heading after B; 0 is the preface).
--old-has-citation-notes drops the note definitions from the old side, for
a render whose notes are biblatex's citations and not the author's text.
"""

import argparse
import collections
import difflib
import re
import sys

MARK = re.compile(r"\[\^\d+\]")
DEF = re.compile(r"^\[\^\d+\]:\s*")
KEY = re.compile(r"\[@[^\]]*\]")
HEADING = re.compile(r"^## (Preface|\d+)\b")


def normalize(line):
    line = DEF.sub("", line)
    line = MARK.sub("", line)
    line = KEY.sub("", line)
    line = re.sub(r"^\s*>+\s?", "", line)          # quotes
    line = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line)  # list bullets
    line = line.replace("|", " ")                  # table cells
    line = re.sub(r"\*\*|\*|~~|`", "", line)
    line = re.sub(r"\s+([.,;:!?)])", r"\1", line)  # "court ." after a dropped key
    for a, b in (("“", '"'), ("”", '"'), ("‘", "'"), ("’", "'"),
                 ("—", "-"), ("–", "-"), ("…", "...")):
        line = line.replace(a, b)
    return re.sub(r"\s+", " ", line).strip().lower()


def sentences(line):
    parts = re.split(r"(?<=[.!?])\s+", line)
    return [p.strip() for p in parts if len(p.split()) >= 4]


def subsequence(small, big):
    """True when every item of `small` occurs in `big`, in order."""
    it = iter(big)
    return all(any(w == x for x in it) for w in small)


def chapter_of(line, cur):
    m = HEADING.match(line)
    if m:
        return "0" if m.group(1) == "Preface" else m.group(1)
    return cur


def load(path, chapters=None, drop_defs=False):
    """(sentence, chapter) pairs, in order."""
    out, cur = [], None
    lo, hi = chapters if chapters else (None, None)
    for raw in open(path, encoding="utf-8").read().split("\n"):
        cur = chapter_of(raw, cur)
        if raw.startswith("#") or cur is None:
            continue              # headings, and the front matter before the preface
        if drop_defs and DEF.match(raw):
            continue
        if chapters:
            if cur is None or not cur.isdigit():
                continue
            if not (lo <= int(cur) <= hi):
                continue
        norm = normalize(raw)
        if not norm:
            continue
        for s in sentences(norm):
            out.append((s, cur))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("old")
    ap.add_argument("new")
    ap.add_argument("--chapters", metavar="A-B",
                    help="restrict the old side to chapters A through B (0 is the preface)")
    ap.add_argument("--old-has-citation-notes", action="store_true",
                    help="drop the note definitions from the old side")
    ap.add_argument("--ratio", type=float, default=0.85,
                    help="difflib ratio at or above which a sentence counts as "
                         "nearly present (default 0.85)")
    ap.add_argument("--quiet", action="store_true", help="print the counts only")
    args = ap.parse_args()

    chapters = None
    if args.chapters:
        a, b = args.chapters.split("-", 1)
        chapters = (int(a), int(b))

    old = load(args.old, chapters, args.old_has_citation_notes)
    new = load(args.new)
    new_set = set(s for s, _ in new)

    # Candidates for a near match: sentences sharing the old sentence's longer
    # words, found through an inverted index, so the comparison is not all
    # against all.
    index = collections.defaultdict(set)
    new_list = [s for s, _ in new]
    def long_words(s):      # bare words, so "head." and "head" meet
        return set(w for w in re.findall(r"[\w']+", s) if len(w) >= 5)
    for k, s in enumerate(new_list):
        for w in long_words(s):
            index[w].add(k)

    exact = near = 0
    nears, missing = [], []
    seen_old = set()
    for s, ch in old:
        if s in seen_old:
            continue
        seen_old.add(s)
        if s in new_set:
            exact += 1
            continue
        score = collections.Counter()
        for w in long_words(s):
            for k in index.get(w, ()):
                score[k] += 1
        best, best_r = None, 0.0
        # The eight best candidates by shared words, the nearer in length
        # first among equals: a four-word head shares its one long word with
        # every sentence that mentions the subject.
        ranked = sorted(score.items(), key=lambda kv: (-kv[1], abs(len(new_list[kv[0]]) - len(s))))
        for k, _ in ranked[:8]:
            cand = new_list[k]
            # autojunk=False: with it, difflib treats the space as junk in a
            # sentence over 200 characters and rates a one-word change at 0.5.
            r = difflib.SequenceMatcher(None, s, cand, autojunk=False).ratio()
            # A repair that inserts a clause (an antecedent restored) keeps
            # every old word in order; that counts as near whatever the
            # ratio says about the lengths.
            if subsequence(re.findall(r"[\w']+", s), re.findall(r"[\w']+", cand)):
                r = max(r, args.ratio)
            if r > best_r:
                best, best_r = cand, r
        if best is not None and best_r >= args.ratio:
            near += 1
            nears.append((ch, best_r, s, best))
        else:
            missing.append((ch, s))

    if not args.quiet:
        for ch, r, s, b in nears:
            print("NEAR %.2f [ch %s]\n  old: %s\n  new: %s" % (r, ch, s, b))
        for ch, s in missing:
            print("MISSING [ch %s]: %s" % (ch, s))
    print("%d old sentences: %d exact, %d near, %d missing"
          % (exact + near + len(missing), exact, near, len(missing)))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
