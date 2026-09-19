#!/usr/bin/env python3
"""Guard the named-persons rule.

The hazard this exists for is the **persona device**: this repository is full of
text a language model produced while pretending to be a named real person, and
none of that may reach the book, a planning file, or a commit message as though
the person had said or done it.

What the rule is NOT (author's ruling, 2026-08-23, recorded as D-017): a bar on
ordinary scholarly citation. Naming the researchers who published a finding,
quoting a published claim and citing it, or describing a documented event in a
laboratory is normal nonfiction and is allowed everywhere, including in the book.

So the test is not "does a name appear" but "is a name being credited with
something no source supports". Approximated here as: a persona name within
range of an attribution verb of the persona-device kind — reviewed, rated,
ranked, scored, feedback from, in their review, as a co-author, writing as, in
the voice of, simulated. Those are hard failures anywhere. Other name hits are
reported for a human to confirm are citations.

The persona name list is built in memory from the spreadsheets and is NEVER
written to disk. Since 2026-09-05 the spreadsheets live inside the
persona-device archive at the repository root (odsread reads them from there),
so that no rendered page carries a real person's name beside generated text.

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

# Verbs of the persona device: someone being credited with participating in
# THIS project, or with an opinion a model produced on their behalf.
ATTRIB = re.compile(
    r"\b(we thank|thanks to|acknowledg\w*|rated|ranked|scored|graded|reviewed by|"
    r"critiqu\w+ by|feedback from|as (?:a )?(?:co-)?author|co-author\w*|"
    r"our (?:reviewer|panel|team|triad)|persona|volunteered|assigned to|"
    r"in their review|suggested that we|told us|advised us|"
    r"writing as|in the voice of|simulated|as though you were|you are)\b", re.I)

PERSONA_SOURCES = [
    ("personas/section-assignments/superintelligence-ethics-outline_v3b_2024-07-07.ods", 1),
    ("personas/section-assignments/superintelligence-ethics-outline_v3_2024-07-07.ods", 1),
    ("personas/section-assignments/previous/superintelligence-ethics-outline_v3a_2024-07-07.ods", 1),
    ("personas/section-assignments/previous/superintelligence-ethics-outline_v2_2024-07-07.ods", 1),
    ("personas/nonredundant_authors_2023-05-08.ods", 0),
    ("personas/author-grouping-bootstrap_2023-08-21.ods", 0),
]

# A name may carry a lowercase particle between its first and last tokens (van,
# de, von, della). Until 2026-09-05 every token had to be capitalized, which
# silently dropped one persona from the roster; the 2026-09-05 audit found it.
NAME_TOKEN = re.compile(r"^[A-Z][\w.'-]*$")
PARTICLE = re.compile(r"^[a-z]{1,5}$")

STOP = {"the", "and", "of", "team", "comprising", "professor", "phd"}

# An entry with no personal-name token in it at all. Excluded as an exact phrase
# and not by token, because "service" as a token would drop a persona actually
# surnamed Service, and the roster is checked by surname as of D-382.
NONPERSON_PHRASES = {"Public Service"}

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
        if not odsread.exists(path):
            continue
        for _, rows in odsread.sheets(path):
            for row in rows:
                for cell in row[start_col:]:
                    for piece in re.split(r",(?![^()]*\))| and ", cell):
                        nm = _clean(piece)
                        toks = [t for t in nm.split() if t.lower() not in STOP]
                        if len(toks) < 2:
                            continue
                        if not (NAME_TOKEN.match(toks[0]) and NAME_TOKEN.match(toks[-1])):
                            continue
                        if not all(NAME_TOKEN.match(t) or PARTICLE.match(t) for t in toks[1:-1]):
                            continue
                        if len(toks) > 5:
                            continue
                        if any(t.lower() in NONPERSON for t in toks):
                            continue
                        full = " ".join(toks)
                        if full in NONPERSON_PHRASES:
                            continue
                        names.add(full)
    return names


def build_regex(names):
    """Full-name forms: "Given Family" and the "Family, Given" a BibTeX author
    field is written in. Before D-382 only the first was built, so every
    `author = {Family, Given}` in refs.bib was invisible to this guard -- and
    refs.bib was not in the scan set either."""
    pats = []
    for n in sorted(names, key=len, reverse=True):
        toks = n.split()
        # first ... last, tolerating middle names/initials in between
        pats.append(re.escape(toks[0]) + r"(?:\s+[\w.'-]+){0,3}\s+"
                    + re.escape(toks[-1]))
        # last, first -- the bibliography's order
        pats.append(re.escape(toks[-1]) + r",\s+" + re.escape(toks[0]))
    return re.compile(r"\b(?:%s)\b" % "|".join(pats)) if pats else None


def build_surname_regex(names):
    """Surnames alone, for the HARD zone only.

    A bare surname is not evidence of anything -- the roster's surnames include
    Hall, Ross, Bell and Miller, and refs.bib alone holds 66 occurrences of 30 of
    them, every one an ordinary citation. So a surname hit is never reported as a
    name to confirm. It is reported only when a persona-device verb sits within
    range, which is the case this guard exists for and the case the full-name
    regex could not see: "as Hall put it in their review of this chapter" names
    nobody the old pattern matched.

    Two-token surnames and particles are kept whole so that "van Dijk" does not
    match on "Dijk" alone. Surnames of four characters or fewer are dropped, which
    loses any persona surnamed Ng or Sen and is the price of not matching every
    occurrence of "Bell" and "Ross" in the bibliography.

    Measured at the window sizes 40/60/80/120/200 the advisory list runs
    0/2/2/3/4 across 392 files, so the collision this pass looks for is rare. The
    window is 60 to match the full-name pass rather than to hit a target."""
    surs = set()
    for n in names:
        toks = n.split()
        i = 1
        while i < len(toks) - 1 and PARTICLE.match(toks[i]):
            i += 1
        surs.add(" ".join(toks[i:]) if i < len(toks) - 1 else toks[-1])
    surs = {s for s in surs if len(s) > 3}
    if not surs:
        return None
    return re.compile(r"\b(?:%s)\b"
                      % "|".join(re.escape(s) for s in
                                 sorted(surs, key=len, reverse=True)))


def scan(paths, rx, hard_zone, surname_rx=None):
    hard, warn, read = [], [], []
    seen_hard = set()
    for p in paths:
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
        except (IsADirectoryError, FileNotFoundError):
            continue
        rel = os.path.relpath(p, common.REPO)
        for i, line in enumerate(lines, 1):
            for m in rx.finditer(line):
                rec = (rel, i, m.group(0), line.strip()[:120])
                if hard_zone(p):
                    hard.append(rec)
                    seen_hard.add((rel, i))
                else:
                    ctx = " ".join(lines[max(0, i - 2):i + 1])
                    lo = max(0, m.start() - 60)
                    near = line[lo:m.end() + 60]
                    if ATTRIB.search(near) or ATTRIB.search(ctx):
                        hard.append(rec)
                        seen_hard.add((rel, i))
                    else:
                        warn.append(rec)
            # Surname alone: advisory, and deliberately not a hard failure. See
            # build_surname_regex and the READ note in main for why.
            if surname_rx is None:
                continue
            for m in surname_rx.finditer(line):
                if (rel, i) in seen_hard:
                    continue
                near = line[max(0, m.start() - 60):m.end() + 60]
                if ATTRIB.search(near):
                    read.append((rel, i, m.group(0), near.strip()[:120]))
                    break
    return hard, warn, read


def main():
    argv = sys.argv[1:]
    msg_mode = "--msg" in argv
    # D-017: the same test applies everywhere. A name near a persona-device verb
    # fails; a name on its own is a citation to confirm, not a violation.
    hard_zone = lambda p: False  # noqa: E731
    if msg_mode:
        paths = [argv[argv.index("--msg") + 1]]
    elif "--paths" in argv:
        paths = argv[argv.index("--paths") + 1:]
    else:
        # manuscript/sections is the source of truth; the joined build and the
        # frozen v3b are derived/historical copies of the same text, so scanning
        # them too would triple-count every hit.
        paths = []
        for root in ("finishing", os.path.join("manuscript", "sections")):
            for dp, dn, fn in os.walk(os.path.join(common.REPO, root)):
                dn[:] = [d for d in dn if d not in ("reports", "previous", "__pycache__")]
                paths += [os.path.join(dp, f) for f in fn
                          if f.endswith((".txt", ".tex", ".md", ".tsv", ".py",
                                         ".sh", ".bib"))]

    names = persona_names()
    rx = build_regex(names)
    surname_rx = build_surname_regex(names)
    if rx is None:
        sys.exit("no persona names loaded; refusing to pass vacuously")
    hard, warn, read = scan(paths, rx, hard_zone, surname_rx)

    print("names_guard: %d persona names loaded, %d files scanned" % (len(names), len(paths)))
    print("  full names in both orders, gating; surnames alone, advisory")
    if warn:
        print("\nNAMES TO CONFIRM AS CITATIONS (not violations): %d" % len(warn))
        for r in warn[:40]:
            print("  %s:%d  %s | %s" % r)
        if len(warn) > 40:
            print("  ... %d more" % (len(warn) - 40))
    if read:
        # WHY THIS IS NOT A FAILURE. A surname is far likelier than a full name
        # to sit beside an ATTRIB verb innocently, because ATTRIB's vocabulary
        # overlaps ordinary research prose: "scored", "rated", "ranked",
        # "assigned to". Wiring these into the hard zone produced 21 failures on
        # first run, every one a citation -- among them a sentence about an audit
        # in which "gender was scored as female or male". This guard runs in the
        # pre-commit hook, so a false failure here blocks every commit. The
        # surname pass therefore reports and does not gate.
        print("\nSURNAME BESIDE A PERSONA-DEVICE VERB -- READ THESE: %d" % len(read))
        print("  Advisory, not failures. A surname alone is not evidence; what")
        print("  makes one worth reading is the verb next to it.")
        for r in read[:40]:
            print("  %s:%d  %s | %s" % r)
        if len(read) > 40:
            print("  ... %d more" % (len(read) - 40))
    if hard:
        print("\nFAIL: %d name(s) credited with participating in this project" % len(hard))
        for r in hard[:40]:
            print("  %s:%d  %s | %s" % r)
        sys.exit(1)
    print("\nOK: no disallowed name references")


if __name__ == "__main__":
    main()
