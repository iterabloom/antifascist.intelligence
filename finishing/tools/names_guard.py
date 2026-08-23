#!/usr/bin/env python3
"""Guard the AGENTS.md named-persons rule.

The repo names many real people because language models were prompted to write
*as if* they were those people. Nothing we produce may characterize, rate, rank,
score, or attribute views or conduct to a real named person.

Policy enforced here:
  * finishing/** and commit-message drafts: ANY persona full-name hit is a hard
    failure. Planning artifacts cite reviews by file + index/line, never by name.
  * manuscript/**: a full-name hit near an attribution verb is a hard failure
    (that is the forbidden "X reviewed/rated/argued for us" shape). Other hits
    are listed as warnings for a human to adjudicate as ordinary citation.

The persona name list is built in memory from the spreadsheets and is NEVER
written to disk.

Usage:
  names_guard.py                       # scan finishing/ and manuscript/
  names_guard.py --paths a.txt b.txt   # scan specific files
  names_guard.py --msg FILE            # scan a commit-message draft (hard-fail zone)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
import odsread  # noqa: E402

ATTRIB = re.compile(
    r"\b(we thank|thanks to|acknowledg\w*|rated|ranked|scored|graded|reviewed by|"
    r"critiqu\w+ by|feedback from|as (?:a )?(?:co-)?author|co-author\w*|"
    r"our (?:reviewer|panel|team|triad)|persona|volunteered|assigned to|"
    r"in their review|suggested that we|told us|advised us)\b", re.I)

PERSONA_SOURCES = [
    ("personas/section-assignments/superintelligence-ethics-outline_v3b_2024-07-07.ods", 1),
    ("personas/section-assignments/superintelligence-ethics-outline_v3_2024-07-07.ods", 1),
    ("personas/nonredundant_authors_2023-05-08.ods", 0),
    ("personas/author-grouping-bootstrap_2023-08-21.ods", 0),
]

STOP = {"the", "and", "of", "team", "comprising", "professor", "phd"}

# Field and category labels live in the grouping spreadsheet's columns beside
# the names ("AI Research", "Cognitive Science"). A cell containing any of these
# is a heading, not a person.
NONPERSON = {
    "research", "science", "sciences", "ethics", "intelligence", "systems",
    "learning", "studies", "policy", "law", "economics", "psychology",
    "neuroscience", "philosophy", "technology", "computing", "engineering",
    "development", "governance", "safety", "alignment", "ai", "machine",
    "cognitive", "social", "political", "moral", "chapter", "section",
}


def _clean(cell):
    """Strip a parenthetical descriptor: 'Given Family (the linguist)' -> 'Given Family'."""
    s = re.sub(r"\(.*?\)", " ", cell)
    s = re.sub(r"\s+", " ", s).strip(" ,;")
    return s


def persona_names():
    """Set of full names, built in memory only. Never persisted."""
    names = set()
    for rel, start_col in PERSONA_SOURCES:
        path = os.path.join(common.REPO, rel)
        if not os.path.exists(path):
            continue
        for _, rows in odsread.sheets(path):
            for row in rows:
                for cell in row[start_col:]:
                    for piece in re.split(r",(?![^()]*\))| and ", cell):
                        nm = _clean(piece)
                        toks = [t for t in nm.split() if t.lower() not in STOP]
                        if len(toks) < 2:
                            continue
                        if not all(re.match(r"^[A-Z][\w.'-]*$", t) for t in toks):
                            continue
                        if len(toks) > 5:
                            continue
                        if any(t.lower() in NONPERSON for t in toks):
                            continue
                        names.add(" ".join(toks))
    return names


def build_regex(names):
    pats = []
    for n in sorted(names, key=len, reverse=True):
        toks = n.split()
        # first ... last, tolerating middle names/initials in between
        pat = re.escape(toks[0]) + r"(?:\s+[A-Z][\w.'-]*){0,3}\s+" + re.escape(toks[-1])
        pats.append(pat)
    return re.compile(r"\b(?:%s)\b" % "|".join(pats)) if pats else None


def scan(paths, rx, hard_zone):
    hard, warn = [], []
    for p in paths:
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
        except (IsADirectoryError, FileNotFoundError):
            continue
        for i, line in enumerate(lines, 1):
            for m in rx.finditer(line):
                rec = (os.path.relpath(p, common.REPO), i, m.group(0), line.strip()[:120])
                if hard_zone(p):
                    hard.append(rec)
                else:
                    ctx = " ".join(lines[max(0, i - 2):i + 1])
                    lo = max(0, m.start() - 60)
                    near = line[lo:m.end() + 60]
                    (hard if (ATTRIB.search(near) or ATTRIB.search(ctx)) else warn).append(rec)
    return hard, warn


def main():
    argv = sys.argv[1:]
    msg_mode = "--msg" in argv
    if msg_mode:
        paths = [argv[argv.index("--msg") + 1]]
        hard_zone = lambda p: True  # noqa: E731
    elif "--paths" in argv:
        paths = argv[argv.index("--paths") + 1:]
        hard_zone = lambda p: "/finishing/" in p.replace(os.sep, "/")  # noqa: E731
    else:
        # manuscript/sections is the source of truth; the joined build and the
        # frozen v3b are derived/historical copies of the same text, so scanning
        # them too would triple-count every hit.
        paths = []
        for root in ("finishing", os.path.join("manuscript", "sections")):
            for dp, dn, fn in os.walk(os.path.join(common.REPO, root)):
                dn[:] = [d for d in dn if d not in ("reports", "previous", "__pycache__")]
                paths += [os.path.join(dp, f) for f in fn
                          if f.endswith((".txt", ".md", ".tsv", ".py", ".sh"))]
        hard_zone = lambda p: "/finishing/" in p.replace(os.sep, "/")  # noqa: E731

    names = persona_names()
    rx = build_regex(names)
    if rx is None:
        sys.exit("no persona names loaded; refusing to pass vacuously")
    hard, warn = scan(paths, rx, hard_zone)

    print("names_guard: %d persona names loaded, %d files scanned" % (len(names), len(paths)))
    if warn:
        print("\nWARN (manuscript, adjudicate citation vs attribution): %d" % len(warn))
        for r in warn[:40]:
            print("  %s:%d  %s | %s" % r)
        if len(warn) > 40:
            print("  ... %d more" % (len(warn) - 40))
    if hard:
        print("\nFAIL: %d disallowed name reference(s)" % len(hard))
        for r in hard[:40]:
            print("  %s:%d  %s | %s" % r)
        sys.exit(1)
    print("\nOK: no disallowed name references")


if __name__ == "__main__":
    main()
