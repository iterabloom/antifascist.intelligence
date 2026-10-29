"""Find the book's coined terms used before they are defined, and defined twice.

A term is the glossary's headwords plus the rows of finishing/coinages.tsv,
which also overrides how a glossary term is matched. A glossary entry with
several headwords ("Pool; backstop; levy.") gives one term each. A headword
that is "The" and a capitalized word (The Association) matches
case-sensitively without being told to.

WHAT IS READ. The book in ORDER.tsv order, sentence by sentence, with each
\\note's sentences placed right after the sentence that carries its marker.
Not read: the glossary, which defines everything at the end; epigraphs
(verse, flushright), which are not the author's words; figures and tikz. Read:
quote environments, boxes, list items and run-in heads, each item and head a
block of its own, and table rows, one sentence per row. The sentence splitter
knows common abbreviations (v., e.g., U.S., ch.) and is still approximate.

MATCHING. Case is ignored unless the term says otherwise; a hyphen in a term
matches a hyphen or a space; plurals are automatic (-s, -es, -y to -ies). A
match inside a longer term's match belongs to the longer term: "floor" in
"floor court" is an occurrence of the floor court only. A match capitalized in
mid-sentence, on a term that ignores case, is a name and not an occurrence:
the Maven Smart System, the Register of Copyrights.

An occurrence of a term is DEFINING when it is

  emph     inside an \\emph{} or \\textit{} that holds little else: the term,
           an article, at most two more words. An italic that is an inline
           label (capitalized, ending in a period or colon: "In a bearer.")
           or a title (every word capitalized: End Times Fascism) is not;
  quoted   in curly quotes: “the floor”, “walls.”;
  framed   in a defining frame: "which I call X", "what this book calls X",
           "call it X", "known as X", "by X I mean", "X means", "X here means";
  glossed  followed straight by its gloss: "a commons: a population of
           bearers...", "the floor court, the court whose..." (not where the
           comma closes an opening phrase: "Under the captured operator,
           the rows that..."); after a colon
           or dash only an "a/an" phrase counts, and not a list of them; or
           a phrase of two or more words introduced by "a/an" with a
           relative clause, at its first occurrence only: "an emergency
           license that acts at once";
  pinned   the first occurrence in the section coinages.tsv names in
           `defined_at`, which wins over all of the above.

Every other occurrence is a USE. A term's definition is its first defining
occurrence, or, where earlier, its first occurrence in a section the
glossary's entry points to (kind `glossary`): those pointers are the book's
own claim about where the term is defined. A use is fine if the definition
is in the same sentence or the next one; a use earlier than that is reported.

Each class is a FLAG, not a verdict, on the same footing as deixis.py and
reader_tax.py. Emphasis is also stress, and a quote is also a quotation, so a
"definition" here is a place the prose marks a term, and the author decides
whether it defines it. Not in check_all.sh.

THE REPORTS

  (default)     counts, and the terms in each report below
  --early       uses before the definition, by term, each with its distance
                in sections. A use whose sentence points at the definition's
                chapter or section is tagged `pointer`: by number (§6.2,
                chapter 6, Chapters 5 and 6), by a worded pointer checked
                against where it now leads ("the next chapter" only if the
                definition is in the chapter that now follows, "the next
                section" likewise), or by one that only says the
                definition is coming ("a later chapter", "defined below").
  --multi       terms marked as defined in more than one place, every site in
                book order, so a better definition that arrives late shows
                beside the first. Sites within one sentence of each other
                count once. Where the glossary's own pointers name sections
                and the first definition is in none of them, the term is
                tagged `glossary-elsewhere`.
  --unmarked    terms with no defining occurrence anywhere, and their first
                use: the place to read to see whether it defines the term,
                and to pin with `defined_at` if it does.
  --term T      every occurrence of one term, with its kind.
  --candidates  emphasized, quoted and framed phrases that are not terms yet
                and occur at least twice, phrases of two or more words first,
                by how often the book uses them: the raw material for
                coinages.tsv. Left out: phrases over four words, phrases
                of function words only (its, about, but), case names and
                titles, inline labels, and `phrase` exceptions.

  --chapter N   restrict --early, --multi and --unmarked to definitions or
                uses in one chapter (the number the book prints).

COINAGES.TSV, the hand-kept part, a row per term (a row whose term starts
with # is a comment), columns:

  term        the term as the reports print it. A glossary headword written
              the same way (case aside, leading "The" aside) is overridden.
  variants    other spellings, separated by " | ". Plurals are automatic.
  case        `exact` to match case-sensitively (the Association, not an
              association). Default: ignore case.
  status      `check` (default): both reports. `multi`: only --multi, for a
              word whose plain English sense makes every early use noise.
              `ignore`: neither.
  defined_at  a section label, as the reports print it: the definition is
              that section's first defining occurrence, or its first
              occurrence if none there is marked.
  regex       a Python pattern that replaces the automatic match, for a term
              whose other senses no variant list can exclude: `(?<=[Tt]he )
              registers?` keeps the register and drops "to register".
  note        free text, for the reason behind a ruling.

EXCEPTIONS, finishing/coinages_exceptions.tsv, which grows by use and is
created by the first `--except`. Every reported occurrence carries an id in
brackets, made from the term and the six words either side of it, numbers
left out, so it survives a move, a renumbering and edits elsewhere in the
paragraph, and goes stale when the words around the term change, which is
when the ruling deserves a fresh look. `--except ID [ID ...] --why TEXT`
appends a row for each, and the kind follows from what was reported, or
from `--as KIND`:

  not-term        the word is not the coined term here: a plain sense, a
                  verb, another institution with the same name ("bolt to
                  the floor", "standing on one foot"). Any occurrence can
                  take it, only with --as. It is left out of every report
                  as if the word weren't there, and like not-definition it
                  is a fact about the sentence, so no restructure lapses it.

  not-definition  a marked occurrence that defines nothing: stress, an
                  italic for how the sentence is read aloud, a quotation.
                  It counts as a use from then on, so the definition may
                  move later and early uses may appear. It is a fact about
                  the sentence, so no restructure lapses it. A definition
                  that is not marked, one the glossary's pointers or
                  `defined_at` supply, can't be excepted: `--except` says
                  so, and moving it is a `defined_at` in coinages.tsv.
  accept-early    an early use of the term the author lets stand, a
                  preview, where it sits now. The row keeps the
                  definition it was accepted against and the distance in
                  sections, and holds only while both hold: a restructure
                  that puts another definition first, or moves the use
                  farther away, lapses it, and the use is reported again,
                  tagged LAPSED.
  phrase          from `--except-phrase P [P ...]`: a phrase --candidates
                  stops listing.

  --stale       exceptions whose occurrence is no longer in the book. The
                summary's second line counts the rows, those applied and
                those stale.

The file's columns: id, term, kind, context and where (as reported when the
row was added, for a reader; nothing matches on them), why, date, and for
accept-early, def (the definition's id) and gap (sections). Two occurrences
of a term with the same six words either side share an id, and one ruling
covers both.

RESTRUCTURING. Reading order is ORDER.tsv's `seq`, so a rearranged book is
read in its new order with nothing to update here; `defined_at` and the
glossary's pointers are labels, which a move doesn't change. What a single
run can't say is what a change made worse, so:

  --snapshot [PATH]  write the state to compare against, before the change:
                each term's definition, every early use with its distance,
                every occurrence id, and the commit it was taken from
                ("+uncommitted" if the manuscript had changes not yet
                committed). Default finishing/reports/coinages_snapshot.tsv.
                Take it just before the change, so the comparison shows
                what the change did and not prose edited in between, and
                again after any change to this script, coinages.tsv or the
                exceptions, which a comparison would otherwise blame on the
                structure.
  --compare [PATH]   after the change, worst first:
                POINTER NO LONGER LEADS TO THE DEFINITION, an early use
                  whose worded pointer ("the next chapter") was right and
                  now isn't: the sentence needs rewording;
                NEWLY EARLY, a use that was fine and now precedes its
                  definition, tagged `moved` when its words are unchanged
                  (the structure did it) or `new text`;
                FARTHER, an early use at least 3 sections and half again
                  farther from its definition than it was (smaller drift is
                  counted, not listed);
                ACCEPTANCES LAPSED;
                DEFINITION CHANGED, a term whose first definition is now a
                  different occurrence, and whether the order or the words
                  changed it;
                and a count of what got better. Terms with status
                `multi` or `ignore` are left out, as in --early.

    finishing/tools/coinages.py                 summary
    finishing/tools/coinages.py --early         the read
    finishing/tools/coinages.py --multi
    finishing/tools/coinages.py --term "own-case rule"
    finishing/tools/coinages.py --except 5ab7bb03 4ade1db4 --why "stress"
    finishing/tools/coinages.py --except 48cca67a --as not-term --why "literal"
    finishing/tools/coinages.py --except-phrase "its own" --why "stress"
    finishing/tools/coinages.py --stale
    finishing/tools/coinages.py --snapshot      before a restructure
    finishing/tools/coinages.py --compare       after it
"""
import argparse, datetime, hashlib, os, re, signal, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (REPO, order_rows, read_tsv, section_labels, chapter_numbers,
                    ref_numbers, tex_prose_line, _take_arg, numkey)

GLOSSARY = "manuscript/sections/chZ/glossary.tex"
TERMS_TSV = os.path.join(REPO, "finishing", "coinages.tsv")
EXC_TSV = os.path.join(REPO, "finishing", "coinages_exceptions.tsv")
EXC_HEADER = ["id", "term", "kind", "context", "where", "why", "date", "def", "gap"]
SNAPSHOT = os.path.join(REPO, "finishing", "reports", "coinages_snapshot.tsv")
FARTHER_MIN, FARTHER_RATIO = 3, 1.5     # what --compare calls farther
SNAP_HEADER = ["row", "term", "id", "def", "gap", "sents", "where", "context", "ptr"]

EMPH_ON, EMPH_OFF, NOTE = "\x01", "\x02", "\x03"
QUOTE_ENVS = ("verse", "flushright")             # epigraphs: not the author's words
SKIP_ENVS = ("tikzpicture", "figure")
EMPH_SLACK = 2                                   # extra words an \emph may hold

STOP = set("a an the of and or to in on for by with as at is are be it its this "
           "that not no do does did was were has have had can may must will would "
           "should could from what who how why when which than then own one two "
           "about into if but after before already inside above below keep asks "
           "neither either both only also even still".split())


# --- reading the book ----------------------------------------------------

def _mark_emph(s):
    r"""\emph{X} and \textit{X} -> EMPH_ON X EMPH_OFF, at any depth."""
    out, i = [], 0
    pat = re.compile(r"\\(?:emph|textit)\{")
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            return "".join(out)
        arg, end = _take_arg(s, m.end() - 1)
        out.append(s[i:m.start()] + EMPH_ON + _mark_emph(arg) + EMPH_OFF)
        i = end


def _pull_notes(text):
    r"""(text with each \note/\footnote replaced by NOTE k NOTE, [note bodies]).

    The note's own newlines are dropped, so a note written over several lines,
    or several paragraphs, stays inside the sentence that carries it. A line
    map is returned alongside so a paragraph still knows its source line."""
    notes, out, lines = [], [], []
    line, i = 1, 0
    pat = re.compile(r"\\(?:foot)?note\{")
    while True:
        m = pat.search(text, i)
        chunk = text[i:m.start()] if m else text[i:]
        for c in chunk:
            out.append(c)
            lines.append(line)
            if c == "\n":
                line += 1
        if not m:
            return "".join(out), lines, notes
        body, end = _take_arg(text, m.end() - 1)
        notes.append((body.replace("\n", " "), line))
        for c in "%s%d%s" % (NOTE, len(notes) - 1, NOTE):
            out.append(c)
            lines.append(line)
        line += text.count("\n", m.start(), end)
        i = end


def _prose(tex):
    s = tex_prose_line(_mark_emph(tex))
    s = s.replace("\\\\", " ").replace("&", " | ")
    return re.sub(r"\s+", " ", s).strip()


_ABBREV = re.compile(r"\b(?:v|vs|e\.g|i\.e|cf|etc|Dr|Mr|Ms|Mrs|St|No|al|Inc|Co|"
                     r"U\.S|U\.K|U\.N|ch|chs|pp|p|art|arts|para|paras|sec|Ch)\.$")


def split_sentences(p):
    parts, out = re.split(r"(?<=[.!?])([”’)\x02]*)\s+(?=[A-Z“‘(\x01\d§])", p), []
    # re.split with one group returns text, closer, text, closer, ...
    buf = ""
    for k in range(0, len(parts), 2):
        piece = parts[k] + (parts[k + 1] if k + 1 < len(parts) else "")
        buf = (buf + " " + piece).strip() if buf else piece
        if _ABBREV.search(buf.rstrip("”’)\x02")):
            continue
        out.append(buf)
        buf = ""
    if buf:
        out.append(buf)
    return [s for s in out if s.strip()]


class Unit:
    """One sentence of the book, in reading order."""
    __slots__ = ("idx", "sec", "path", "line", "label", "chapter", "text", "emph", "note")

    def __init__(self, path, line, label, chapter, raw, note):
        self.path, self.line, self.label, self.chapter, self.note = \
            path, line, label, chapter, note
        self.text, self.emph, stack, buf = "", [], [], []
        for c in raw:
            if c == EMPH_ON:
                stack.append(len(buf))
            elif c == EMPH_OFF:
                if stack:
                    self.emph.append((stack.pop(), len(buf)))
            else:
                buf.append(c)
        self.text = "".join(buf)


def read_book():
    labels, chapters = section_labels(), chapter_numbers()
    units, label = [], ""
    for r in order_rows():
        path = r["path"]
        if path == GLOSSARY:
            continue
        label = labels.get(path, label)          # a continuation keeps the last
        chapter = chapters.get(path, "")
        src = open(os.path.join(REPO, path), encoding="utf-8").read()
        text, linemap, notes = _pull_notes(src)
        paras, buf, envs, off = [], [], [], 0

        def flush():
            if buf:
                paras.append((buf[0][0], " ".join(t for _, t in buf)))
                del buf[:]

        for raw in text.split("\n"):
            ln = linemap[off] if off < len(linemap) else linemap[-1]
            off += len(raw) + 1
            s = raw.strip()
            for m in re.finditer(r"\\(begin|end)\{([A-Za-z*]+)\}", s):
                if m.group(1) == "begin":
                    envs.append(m.group(2))
                elif envs:
                    envs.pop()
            if not s or s.startswith("%"):
                flush()
                continue
            if any(e in QUOTE_ENVS + SKIP_ENVS for e in envs) or \
               re.match(r"\\end\{(%s)\}" % "|".join(QUOTE_ENVS + SKIP_ENVS), s):
                flush()
                continue
            if re.match(r"\\(chapter|section|subsection|subsubsection|label|"
                        r"unnumberedlabel|addcontentsline|backmattermark|"
                        r"begingroup|endgroup|hline|endhead|endfirsthead|appendix)\b", s) \
               or re.match(r"\\begin\{(longtable|tabular)\}", s):
                flush()
                continue
            if s.startswith("\\item") or s.startswith("\\runin{") or "&" in s:
                flush()
                buf.append((ln, s))
                flush()                          # an item, a head, a table row: one block
                continue
            buf.append((ln, s))
        flush()

        for ln, p in paras:
            for sent in split_sentences(_prose(p)):
                marks = [int(k) for k in re.findall(NOTE + r"(\d+)" + NOTE, sent)]
                sent = re.sub(NOTE + r"\d+" + NOTE, "", sent)
                units.append(Unit(path, ln, label, chapter, sent, False))
                for k in marks:
                    body, nln = notes[k]
                    for ns in split_sentences(_prose(body)):
                        units.append(Unit(path, nln, label, chapter, ns, True))
    # sec counts headed sections in reading order, so the distance between a
    # use and its definition can be stated in sections as well as sentences.
    sec, last = -1, None
    del SEC_LABELS[:], CHAPTERS[:]
    for i, u in enumerate(units):
        u.idx = i
        if u.label != last:
            sec, last = sec + 1, u.label
            SEC_LABELS.append(u.label)
        u.sec = sec
        if u.chapter and (not CHAPTERS or CHAPTERS[-1] != u.chapter):
            CHAPTERS.append(u.chapter)
    return units


SEC_LABELS = []     # section ordinal -> label, in reading order
CHAPTERS = []       # chapter numbers in reading order, for "the next chapter"


# --- the terms -------------------------------------------------------------

def _key(t):
    return re.sub(r"^the\s+", "", t.strip().lower())


def glossary_terms():
    """[(headword, [labels the glossary points to])] from the glossary."""
    src = open(os.path.join(REPO, GLOSSARY), encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^\\emph\{([^}]*)\.\}(.*)$", src, re.M):
        refs = re.findall(r"\\ref\{(?:sec|ch):([^}]*)\}",
                          (re.findall(r"\(([^()]*\\ref[^()]*)\)\s*$", m.group(2)) or [""])[-1])
        for t in re.split(r";\s*", m.group(1)):
            out.append((t.strip(), refs))
    return out


class Term:
    def __init__(self, name, variants=(), case="", status="check", defined_at="",
                 gloss_refs=(), source="glossary", regex=""):
        self.name, self.status, self.defined_at = name, status or "check", defined_at
        self.gloss_refs, self.source = list(gloss_refs), source
        forms = [name] + [v for v in variants if v]
        exact = case == "exact"
        if not case and name.startswith("The ") and name[4:5].isupper():
            exact = True                        # "The Association": the proper noun
        alts = []
        for f in forms:
            f = re.sub(r"^[Tt]he\s+", "", f.strip())
            words = [re.escape(w).replace(r"\-", r"[-\s]") for w in f.split()]
            last = f.split()[-1]
            if last.endswith("y") and not last.endswith(("ay", "ey", "oy", "uy")):
                words[-1] = re.escape(last[:-1]) + "(?:y|ies)"
            elif not last.endswith("s"):
                words[-1] += "(?:s|es)?"
            alts.append(r"\s+".join(words))
        flags = 0 if exact else re.I
        self.rx = re.compile(regex if regex else
                             r"(?<![\w-])(?:%s)(?![\w-])" % "|".join(alts), flags)


def load_terms():
    rows = {}
    if os.path.exists(TERMS_TSV):
        _, body = read_tsv(TERMS_TSV)
        for r in body:
            if r.get("term", "").strip() and not r["term"].startswith("#"):
                rows[_key(r["term"])] = r
    terms, seen = [], set()
    for head, refs in glossary_terms():
        r = rows.get(_key(head), {})
        terms.append(Term(r.get("term") or head,
                          [v.strip() for v in r.get("variants", "").split("|")],
                          r.get("case", ""), r.get("status", ""), r.get("defined_at", ""),
                          refs, "glossary", r.get("regex", "")))
        seen.add(_key(head))
    for k, r in rows.items():
        if k not in seen:
            terms.append(Term(r["term"], [v.strip() for v in r.get("variants", "").split("|")],
                              r.get("case", ""), r.get("status", ""),
                              r.get("defined_at", ""), (), "tsv", r.get("regex", "")))
    return [t for t in terms if t.status != "ignore"]


# --- classifying occurrences ----------------------------------------------

FRAME_BEFORE = re.compile(
    r"(?:\b(?:I|we|this book|the book|chapter \d+|Part [IVX]+)\s+(?:will\s+|shall\s+|'ll\s+)?"
    r"(?:call|calls|called|term|terms|termed)(?:\s+(?:it|this|that|them|these|those))?"
    r"|\bcall(?:ing)?\s+(?:it|this|that|them|these|those)"
    r"|\b(?:known|referred to) as|\bwhat (?:I|we|this book|the book) (?:call|calls)"
    r"|\b(?:is|are|was|were) called)\s*(?:the\s+|a\s+|an\s+)?[“‘]?$", re.I)
BY_I_MEAN = (re.compile(r"\bby\s+(?:the\s+|a\s+|an\s+)?[“‘]?$", re.I),
             re.compile(r"^[”’]?\s+(?:I|we)\s+mean\b"))
# "X means" defines only where X is the sentence's subject or is quoted:
# "postponing majority means idling the asset" is not a definition of majority.
FRAME_AFTER = re.compile(
    r"^[”’]?(?:s|es)?\s*(?:,\s*)?(?:here\s+|in this book\s+|as used here\s+)?"
    r"(?:means|denotes|refers to|is defined as|,?\s*by which I mean)\b", re.I)
# The term followed straight by its gloss: "a commons: a population of bearers
# that...", "the floor court, the court whose jurisdiction is fixed...".
#
# After a colon or dash only an indefinite noun phrase counts, and not a list
# of them: "a commons: a population of bearers" glosses the term, while "the
# scarce thing was the wall: the clerk, the officer and the soldier..." and "a
# halt, a restore or a retraining" go on with the sentence.
GLOSS_AFTER = re.compile(
    r"^(?:s|es)?[”’]?(?:\s+of\s+[\w-]+)?(?::|\s+—)\s+(?:a|an)\s+(?![\w-]+(?:\s+[\w-]+)?,\s+(?:a|an)\s)")
# The appositive: "the floor court, the court whose jurisdiction...". Not
# when the comma closes an opening phrase the term ends: "Under the captured
# operator, the rows that prevent..." and "In a user-held system, the
# freedoms that..." go on with the sentence.
APPOS_AFTER = re.compile(
    r"^(?:s|es)?[”’]?,\s+(?:a|an|the)\s+(?:[\w-]+\s+){0,2}?(?:that|which|whose|who|where)\b")
OPENING_PHRASE = re.compile(
    r"^(?:In|Under|For|On|At|With|Without|By|From|Against|Within|Across|After|Before|"
    r"Between|Among|Inside|Outside|Over|Through|Beside|Behind|Beyond)\b[^,;:]*$")
# A phrase introduced with an indefinite article and a relative clause that
# says what it is: "an emergency license that acts at once". Phrases only: "a
# system that" and "an operator that" are ordinary relative clauses, and
# counting them put System's defining sites at 79.
INTRO_BEFORE = re.compile(r"(?:^|\W)(?:a|an)\s+$", re.I)
INTRO_AFTER = re.compile(r"^(?:s|es)?\s+(?:that|which|whose|where)\s")
SUBJECT = re.compile(r"(?:^|[.:;]\s)\s*(?:[“‘]?(?:The|A|An|the|a|an)\s+)?[“‘]?$")
BY_I_MEAN = (re.compile(r"\bby\s+(?:the\s+|a\s+|an\s+)?[“‘]?$", re.I),
             re.compile(r"^[”’]?\s+(?:I|we)\s+mean\b"))
FRAME_AFTER = re.compile(
    r"^[”’]?(?:s|es)?\s*(?:,\s*)?(?:here\s+|in this book\s+|as used here\s+)?"
    r"(?:means|meant|names|denotes|refers to|is defined as|,?\s*by which I mean)\b"
    r"|^[”’]?\s+I\s+mean\b", re.I)


def classify(u, m):
    """'emph', 'quoted', 'framed', 'glossed' or 'use' for match m in unit u."""
    a, b = m.span()
    for s, e in u.emph:
        if s <= a and b <= e:
            inner = u.text[s:e].strip()
            words = inner.split()
            if re.search(r"[.:]$", inner) and inner[:1].isupper():
                break                           # an inline label: "In a bearer."
            if len(words) > len(m.group(0).split()) and \
               all(w[:1].isupper() for w in words if w.lower() not in STOP):
                break                           # a title: End Times Fascism
            extra = (u.text[s:a] + " " + u.text[b:e]).split()
            extra = [w for w in extra if w.lower().strip(".,;:") not in ("the", "a", "an")]
            if len(extra) <= EMPH_SLACK:
                return "emph"
    before, after = u.text[max(0, a - 70):a], u.text[b:b + 40]
    if re.search(r"[“‘](?:the\s+|a\s+|an\s+)?$", before, re.I) and \
       re.match(r"(?:s|es)?[.,;:!?]?[”’]", after):
        return "quoted"
    if FRAME_BEFORE.search(before):
        return "framed"
    if FRAME_AFTER.match(after) and (SUBJECT.search(before) or re.search(r"[“‘]$", before)):
        return "framed"
    if BY_I_MEAN[0].search(before) and BY_I_MEAN[1].match(after):
        return "framed"
    if GLOSS_AFTER.match(after):
        return "glossed"
    if APPOS_AFTER.match(after) and not OPENING_PHRASE.match(u.text[:a]):
        return "glossed"
    if len(m.group(0).split()) > 1 and INTRO_BEFORE.search(before) and INTRO_AFTER.match(after):
        return "introduced"                 # analyse() keeps it only at a first meeting
    return "use"


def proper_noun(term, u, m):
    """A capital in mid-sentence on a term that doesn't ask for one is a name
    the term happens to be part of: the Maven Smart System, the Register of
    Copyrights. A capital after an opening quote, a bracket, a list marker
    ("[1.] Standing") or a colon is not."""
    if not (term.rx.flags & re.I) or not m.group(0)[:1].isupper():
        return False
    before = u.text[:m.start()].rstrip("  ")
    return bool(before) and not before.endswith(("“", "‘", "(", "[", "]", ":", "—", "|", "."))


def occurrences(units, term, longer=()):
    """[(unit, match, kind)], leaving out a match that sits inside a longer
    term's: "floor" in "floor court" is the floor court's occurrence."""
    out = []
    for u in units:
        ms = list(term.rx.finditer(u.text))
        if not ms:
            continue
        cover = [x.span() for t in longer for x in t.rx.finditer(u.text)]
        for m in ms:
            a, b = m.span()
            if any(s <= a and b <= e and (e - s) > (b - a) for s, e in cover):
                continue
            if proper_noun(term, u, m):
                continue
            out.append((u, m, classify(u, m)))
    return out


REF_NAME = re.compile(r"\b(Appendix|Appendices|Parts?|[Cc]hapters?|[Cc]hs?\.)\s+[A-Z]+"
                      r"(?:(?:,\s*|,?\s+and\s+|\s+to\s+|–)[A-Z]+)*\b|(§)\s*[A-Z]+\b")


def occ_id(term, u, m):
    """The occurrence's id: the term and the six words either side of it.

    Words only, no numbers: a cross-reference prints the number of the section
    it points to, and a restructure renumbers it, so "§15.5" becoming "§14.5"
    would otherwise make every occurrence near it look rewritten. Letters and
    numerals after Appendix, Part, chapter and § are left out for the same
    reason: "Appendix C" and "§C.2" are \refs, re-lettering the appendices
    changes them, and a chapter moved among them prints as "chapter H"."""
    a, b = m.span()
    w = lambda x: re.findall(r"[a-z]+", REF_NAME.sub(lambda r: r.group(1) or r.group(2), x).lower())
    key = " ".join([_key(term.name), "|"] + w(u.text[:a])[-6:] + ["|"] +
                   w(u.text[a:b]) + ["|"] + w(u.text[b:])[:6])
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:8]


def load_exceptions():
    if not os.path.exists(EXC_TSV):
        return {}
    _, rows = read_tsv(EXC_TSV)
    return {r["id"]: r for r in rows if r.get("id")}


EXC = None          # id -> row, loaded once by analyse()
SEEN = set()        # ids met in this run, for --stale


def analyse(units, terms):
    global EXC
    if EXC is None:
        EXC = load_exceptions()
    printed = ref_numbers()
    res = []
    for t in terms:
        longer = [o for o in terms if o is not t and t.rx.search(o.name)
                  and len(o.name) > len(t.name)]
        occ = []
        for u, m, kind in occurrences(units, t, longer):
            i = occ_id(t, u, m)
            if i in EXC:
                SEEN.add(i)
                if EXC[i]["kind"] == "not-term":
                    continue                    # not this term at all, anywhere
                if kind != "use" and EXC[i]["kind"] == "not-definition":
                    kind = "use"
            occ.append((u, m, kind))
        # "a corroborated license that can't arrive" introduces nothing to a
        # reader who has met the phrase: an introduction defines only the
        # first time the term occurs.
        occ = [(u, m, ("glossed" if k == "introduced" and n == 0 else
                       "use" if k == "introduced" else k))
               for n, (u, m, k) in enumerate(occ)]
        if not occ:
            res.append(dict(term=t, occ=[], defs=[], definition=None, early=[], accepted=[]))
            continue
        defs = [o for o in occ if o[2] != "use"]
        definition = None
        if t.defined_at:
            here = [o for o in occ if o[0].label == t.defined_at]
            marked = [o for o in here if o[2] != "use"]
            definition = (marked or here or [None])[0]
            if definition is not None:
                definition = (definition[0], definition[1], "pinned")
        if definition is None:
            # The glossary's pointers are the book's own claim about where a
            # term is defined, so the first occurrence in a section it points to
            # competes with the first marked one, and the earlier wins.
            pointed = [o for o in occ if any(
                printed.get(o[0].label, o[0].label) == printed.get(l, l)
                or printed.get(o[0].label, o[0].label).startswith(printed.get(l, l) + ".")
                for l in t.gloss_refs)]
            cands = [o for o in (defs[:1] + [(p[0], p[1], "glossary") for p in pointed[:1]])]
            if cands:
                definition = min(cands, key=lambda o: o[0].idx)
        # early: (unit, match, pointer?, sections before the definition, lapse)
        early, accepted = [], []
        if definition is not None:
            d = definition[0].idx
            did = occ_id(t, definition[0], definition[1])
            dnum = printed.get(definition[0].label, definition[0].label)
            for u, m, kind in occ:
                if u.idx < d - 1:
                    i = occ_id(t, u, m)
                    gap = definition[0].sec - u.sec
                    e = [u, m, pointer(u, definition[0], dnum), gap, None]
                    x = EXC.get(i, {})
                    if x.get("kind") == "accept-early":
                        # An acceptance holds for the definition and the
                        # distance it was given for. A restructure that moves
                        # the use farther away, or puts another definition
                        # first, lapses it and the use is reported again.
                        ok_def = x.get("def", "") in ("", did)
                        ok_gap = not x.get("gap", "").isdigit() or gap <= int(x["gap"])
                        if ok_def and ok_gap:
                            accepted.append(tuple(e))
                            continue
                        e[4] = ("accepted %s %s sections before %s; now %d before %s" % (
                            x.get("date", ""), x.get("gap", "?"), x.get("def", "?"), gap, did))
                    early.append(tuple(e))
        # distinct defining sites: one per run of sentences within one of each other
        sites, last = [], -10
        for o in defs:
            if o[0].idx - last > 1:
                sites.append(o)
            last = o[0].idx
        res.append(dict(term=t, occ=occ, defs=sites, definition=definition, early=early,
                        accepted=accepted))
    return res


def pointer(u, d, dnum):
    """True if use u's sentence points at definition d's chapter or section.

    A numbered pointer is a \ref and renumbers itself when the book moves. A
    worded one doesn't, so it is checked against where it now leads: "the
    next chapter" points at the definition only while the definition is in
    the chapter that follows, which a rearrangement can quietly undo."""
    text, dchap = u.text, d.chapter
    for n in re.findall(r"§\s*([0-9A-Z]+(?:\.\d+)*)", text):
        if n == dnum or dnum.startswith(n + ".") or n.startswith(dnum + "."):
            return True
    for lst in re.findall(r"\b(?:[Cc]hapters?|Ch\.|Appendix|Appendices)\s+"
                          r"([0-9A-Z]+(?:(?:,\s*|,?\s+and\s+|\s+to\s+|–)[0-9A-Z]+)*)\b", text):
        if dchap in re.split(r",\s*|,?\s+and\s+|\s+to\s+|–", lst):
            return True
    t = text.lower()
    if re.search(r"\b(?:the next|the following) chapter\b", t):
        if u.chapter in CHAPTERS and CHAPTERS.index(u.chapter) + 1 < len(CHAPTERS) \
           and CHAPTERS[CHAPTERS.index(u.chapter) + 1] == dchap:
            return True
    if re.search(r"\b(?:the next|the following) section\b|\bdefined in the next\b", t):
        nxt = SEC_LABELS[u.sec + 1] if u.sec + 1 < len(SEC_LABELS) else None
        if nxt and (d.label == nxt or d.label.startswith(nxt + ".")):
            return True
    # Pointers that only say the definition is coming: every early use's
    # definition is later, so these hold wherever the chapters go.
    if re.search(r"\b(?:a later|a coming|a following) (?:chapter|section|part)\b|"
                 r"\bdefined (?:below|later)\b|\bthe next part\b", t):
        return True
    return False


# --- printing ----------------------------------------------------------------

def where(u):
    return "%s:%d [%s]%s" % (u.path.replace("manuscript/sections/", ""), u.line,
                             u.label, " note" if u.note else "")


def snippet(u, m, width=70):
    a, b = m.span()
    s = u.text[max(0, a - width):a] + "«" + u.text[a:b] + "»" + u.text[b:b + width]
    return ("…" if a > width else "") + s + ("…" if b + width < len(u.text) else "")


def in_chapter(u, chap):
    return chap is None or u.chapter == chap


def report_early(res, chap):
    n = 0
    for r in sorted((r for r in res if r["early"] and r["term"].status == "check"),
                    key=lambda r: r["early"][0][0].idx):
        early = [e for e in r["early"] if in_chapter(e[0], chap)]
        if not early:
            continue
        u, m, kind = r["definition"]
        print("== %s   (%d early; defined %s, %s)" % (r["term"].name, len(early), where(u), kind))
        print("   def:    [%s] %s" % (occ_id(r["term"], u, m), snippet(u, m)))
        for eu, em, ptr, gap, lapse in early:
            print("   %-7s %s  [%s]  %s\n          %s" % (
                "pointer" if ptr else "use", where(eu), occ_id(r["term"], eu, em),
                "same section" if gap == 0 else "%d section%s before" % (gap, "s"[:gap != 1]),
                snippet(eu, em)))
            if lapse:
                print("          LAPSED: %s" % lapse)
        n += len(early)
        print()
    print("%d early uses" % n)


def report_multi(res, chap):
    printed = ref_numbers()
    n = 0
    for r in res:
        if len(r["defs"]) < 2 or not any(in_chapter(o[0], chap) for o in r["defs"]):
            continue
        n += 1
        tags = []
        if r["term"].gloss_refs:
            first = r["defs"][0][0]
            pointed = [printed.get(l, l) for l in r["term"].gloss_refs]
            num = printed.get(first.label, first.label)
            if not any(num == p or num.startswith(p + ".") or (p == first.chapter)
                       for p in pointed):
                tags.append("glossary-elsewhere: glossary points to %s" % ", ".join(pointed))
        print("== %s   (%d sites)%s" % (r["term"].name, len(r["defs"]),
                                         "   " + "; ".join(tags) if tags else ""))
        for u, m, kind in r["defs"]:
            print("   %-7s %s  [%s]\n          %s" % (kind, where(u), occ_id(r["term"], u, m),
                                                 snippet(u, m)))
        print()
    print("%d terms defined in more than one place" % n)


def report_unmarked(res, chap):
    n = 0
    for r in res:
        if r["definition"] is not None or r["term"].status == "multi":
            continue
        if not r["occ"]:
            print("== %s   (never occurs outside the glossary)\n" % r["term"].name)
            n += 1
            continue
        u, m, _ = r["occ"][0]
        if not in_chapter(u, chap):
            continue
        n += 1
        print("== %s   (%d occurrences, none marked)" % (r["term"].name, len(r["occ"])))
        print("   first   %s\n          %s\n" % (where(u), snippet(u, m)))
    print("%d terms with no marked definition" % n)


def report_term(res, name):
    for r in res:
        if _key(r["term"].name) != _key(name) and not r["term"].rx.fullmatch(name):
            continue
        d = r["definition"]
        print("== %s  [%s, %s]  definition: %s" % (
            r["term"].name, r["term"].source, r["term"].status,
            where(d[0]) if d else "none"))
        for u, m, kind in r["occ"]:
            tag = kind
            if d and u.idx < d[0].idx - 1:
                tag += " EARLY"
            print("   %-12s %s  [%s]\n               %s" % (tag, where(u), occ_id(r["term"], u, m),
                                                      snippet(u, m)))
        return
    print("no term matches %r (terms come from the glossary and %s)" %
          (name, os.path.relpath(TERMS_TSV, REPO)))


def report_candidates(units, terms):
    seen = Counter()
    first = {}
    dropped = {r["term"].lower() for r in load_exceptions().values() if r["kind"] == "phrase"}
    known = lambda p: p.lower() in dropped or any(t.rx.fullmatch(p) for t in terms)
    for u in units:
        found = []
        for s, e in u.emph:
            found.append(("emph", u.text[s:e]))
        for m in re.finditer(r"“([^”]{2,40})”", u.text):
            found.append(("quoted", m.group(1)))
        for m in re.finditer(r"\b(?:I|we|this book) (?:call|calls)\s+(?:it\s+|this\s+|that\s+)?"
                             r"((?:the |a |an )?[“‘]?[\w-]+(?: [\w-]+){0,3})", u.text):
            found.append(("framed", m.group(1)))
        for kind, p in found:
            p = re.sub(r"^(?:the|a|an)\s+", "", p.strip(" .,;:“”‘’"), flags=re.I)
            w = p.split()
            if not w or len(w) > 4 or all(x.lower() in STOP for x in w):
                continue
            if re.search(r"\bv\.|\d{3}", p) or (len(w) > 1 and all(x[:1].isupper() for x in w)):
                continue                        # a case or a title
            if p[:1].isupper() and len(w) > 1 and not p[1:2].isupper():
                continue                        # a run-in label: "Why it comes first"
            if known(p):
                continue
            k = (kind, p.lower())
            seen[k] += 1
            first.setdefault(k, u)
    # A phrase met once needs no ordering check, so each candidate is counted
    # across the whole book, marked or not, and one met only once is dropped.
    text = "\n".join(u.text for u in units)
    merged = defaultdict(lambda: [0, set(), None])
    for (kind, p), c in seen.items():
        r = merged[p]
        r[0] += c
        r[1].add(kind)
        if r[2] is None or first[(kind, p)].idx < r[2].idx:
            r[2] = first[(kind, p)]
    rows = []
    for p, (c, kinds, u) in merged.items():
        n = len(re.findall(r"(?<![\w-])%s(?![\w-])" % re.escape(p), text, re.I))
        if n >= 2:
            rows.append((len(p.split()) > 1, n, c, p, ",".join(sorted(kinds)), u))
    rows.sort(key=lambda r: (not r[0], -r[1], r[3]))
    print("uses\tmarked\tkind\tphrase\tfirst marked")
    for _multi, n, c, p, kinds, u in rows:
        print("%d\t%d\t%s\t%s\t%s" % (n, c, kinds, p, where(u)))


def write_exceptions(new):
    """Append rows to coinages_exceptions.tsv, writing the header on first use."""
    fresh = not os.path.exists(EXC_TSV)
    with open(EXC_TSV, "a", encoding="utf-8") as f:
        if fresh:
            f.write("\t".join(EXC_HEADER) + "\n")
        for r in new:
            f.write("\t".join(str(r.get(h, "")).replace("\t", " ").replace("\n", " ")
                              for h in EXC_HEADER) + "\n")


def add_exceptions(res, ids, why, kind_as=None):
    """An id names what was reported: a marked occurrence becomes
    not-definition, an early use accept-early. The kind is read off the
    analysis as it stands, before the new rows apply. `kind_as` overrides it:
    not-term for any occurrence; the other two only where they apply."""
    have, today = load_exceptions(), datetime.date.today().isoformat()
    found, new = {}, []
    for r in res:
        d = r["definition"]
        early = {id(e[1]) for e in r["early"]}
        for u, m, kind in r["occ"]:
            i = occ_id(r["term"], u, m)
            if i not in ids or i in found:
                continue
            extra = {}
            if d and d[1] is m and kind == "use":
                k = "unmarked-definition:" + d[2]
            elif kind != "use":
                k = "not-definition"
            elif id(m) in early:
                k = "accept-early"
                extra = dict(def_=occ_id(r["term"], d[0], d[1]), gap=d[0].sec - u.sec)
            else:
                k = None
            found[i] = (r["term"], u, m, k, extra)
    for i in ids:
        if i in have:
            print("%s  already excepted (%s, %s)" % (i, have[i]["term"], have[i]["kind"]))
        elif i not in found:
            print("%s  matches no occurrence in the book as it stands" % i)
        elif found[i][3] and found[i][3].startswith("unmarked-definition:"):
            print("%s  is %s's definition because %s, not because the prose marks it; "
                  "an exception can't move it: set defined_at in %s" % (
                      i, found[i][0].name,
                      "the glossary points to its section" if found[i][3].endswith("glossary")
                      else "defined_at pins it", os.path.relpath(TERMS_TSV, REPO)))
        elif kind_as == "not-term":
            t, u, m, _k, _extra = found[i]
            new.append(dict(id=i, term=t.name, kind="not-term", context=snippet(u, m, 50),
                            where=where(u), why=why, date=today))
            print("%s  not-term  %s  %s" % (i, t.name, where(u)))
        elif kind_as and kind_as != found[i][3]:
            print("%s  is reported as %s, so it can't be excepted as %s" % (
                i, found[i][3] or "an ordinary use", kind_as))
        elif found[i][3] is None:
            print("%s  is an ordinary use, reported as neither a definition nor early: "
                  "nothing to except (unless it isn't the term at all: --as not-term)" % i)
        else:
            t, u, m, k, extra = found[i]
            new.append(dict(id=i, term=t.name, kind=k, context=snippet(u, m, 50),
                            where=where(u), why=why, date=today,
                            gap=extra.get("gap", ""), **{"def": extra.get("def_", "")}))
            print("%s  %s  %s  %s" % (i, k, t.name, where(u)))
    if new:
        write_exceptions(new)
        print("%d row(s) appended to %s" % (len(new), os.path.relpath(EXC_TSV, REPO)))


def add_phrases(phrases, why):
    have = {r["term"].lower() for r in load_exceptions().values() if r["kind"] == "phrase"}
    today = datetime.date.today().isoformat()
    new = []
    for p in phrases:
        if p.lower() in have:
            print("%r already excepted" % p)
            continue
        i = hashlib.sha1(("phrase|" + p.lower()).encode("utf-8")).hexdigest()[:8]
        new.append(dict(id=i, term=p, kind="phrase", why=why, date=today))
        print("%s  phrase  %s" % (i, p))
    if new:
        write_exceptions(new)
        print("%d row(s) appended to %s" % (len(new), os.path.relpath(EXC_TSV, REPO)))


def report_stale():
    n = 0
    for i, r in load_exceptions().items():
        if r["kind"] != "phrase" and i not in SEEN:
            n += 1
            print("%s  %s  %s  was %s\n          %s" % (i, r["kind"], r["term"], r["where"],
                                                    r["context"]))
    print("%d stale exceptions: the words around the term changed, or it is gone. "
          "Delete the row, or re-except the occurrence under its new id." % n)


def write_snapshot(res, path):
    """The state a later run compares against: each term's definition, every
    early use with its distance, and every occurrence id (to tell an
    occurrence that moved from one whose words changed)."""
    import subprocess
    head = subprocess.run(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    dirty = subprocess.run(["git", "-C", REPO, "status", "--porcelain", "manuscript"],
                           capture_output=True, text=True).stdout.strip()
    rows = [dict(row="meta", term=datetime.date.today().isoformat(),
                 id=head + ("+uncommitted" if dirty else ""))]
    for r in res:
        t, d = r["term"], r["definition"]
        did = occ_id(t, d[0], d[1]) if d else ""
        rows.append(dict(row="occ", term=t.name,
                         id=" ".join(sorted({occ_id(t, u, m) for u, m, _ in r["occ"]}))))
        if d:
            rows.append(dict(row="def", term=t.name, id=did, where=where(d[0]),
                             context=snippet(d[0], d[1], 40)))
        for kind, es in (("early", r["early"]), ("accepted", r["accepted"])):
            for u, m, ptr, gap, _l in es:
                rows.append(dict(row=kind, term=t.name, id=occ_id(t, u, m), gap=gap,
                                 sents=d[0].idx - u.idx, where=where(u),
                                 ptr="1" if ptr else "", **{"def": did}))
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(SNAP_HEADER) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(h, "")).replace("\t", " ") for h in SNAP_HEADER) + "\n")
    print("wrote %s: %d terms, %d early uses, %d accepted, from %s" % (
        os.path.relpath(path, REPO), len(res), sum(len(r["early"]) for r in res),
        sum(len(r["accepted"]) for r in res), rows[0]["id"]))


def report_compare(res, path):
    """What changed since the snapshot, worst first. An occurrence whose id
    the snapshot has was moved, not rewritten, so what happened to it is the
    structure's doing; one the snapshot lacks is new or rewritten text."""
    if not os.path.exists(path):
        sys.exit("no snapshot at %s: run --snapshot before the change" % os.path.relpath(path, REPO))
    _, rows = read_tsv(path)
    meta = next((r for r in rows if r["row"] == "meta"), {})
    occ = {r["term"]: set(r["id"].split()) for r in rows if r["row"] == "occ"}
    defs = {r["term"]: r for r in rows if r["row"] == "def"}
    old = {(r["term"], r["id"]): r for r in rows if r["row"] in ("early", "accepted")}
    print("against %s, snapshot of %s from %s\n" % (
        os.path.relpath(path, REPO), meta.get("term", "?"), meta.get("id", "?")))
    newly, farther, closer, gone, moved, lapsed, drift, broken = [], [], [], [], [], [], [], []
    now = set()
    for r in res:
        t, d = r["term"], r["definition"]
        if t.status != "check":
            continue
        cause = lambda i: "moved" if i in occ.get(t.name, ()) else "new text"
        for u, m, ptr, gap, lapse in r["early"]:
            i = occ_id(t, u, m)
            now.add((t.name, i))
            o = old.get((t.name, i))
            line = (t.name, u, m, gap, ptr)
            if o is not None and o.get("ptr") == "1" and not ptr:
                broken.append(line + ("pointed at the definition before",))
            if lapse:
                lapsed.append(line + (lapse,))
            elif o is None:
                newly.append(line + (cause(i),))
            elif o["gap"].isdigit() and gap > int(o["gap"]):
                # Local damage, not drift: a use 103 sections early that is now
                # 106 was already far; one 4 sections early that is now 11 is news.
                g0 = int(o["gap"])
                if gap - g0 >= FARTHER_MIN and gap >= FARTHER_RATIO * g0:
                    farther.append(line + ("was %d section%s before" % (g0, "s"[:g0 != 1]),))
                else:
                    drift.append(t.name)
            elif o["gap"].isdigit() and gap < int(o["gap"]):
                closer.append(t.name)
        did = occ_id(t, d[0], d[1]) if d else ""
        o = defs.get(t.name)
        if o and o["id"] != did:
            why = ("the old one is still in the book, so the order changed"
                   if o["id"] in {occ_id(t, u, m) for u, m, _ in r["occ"]}
                   else "the old one's words changed or it is gone")
            moved.append((t.name, o, d, why))
    checked = {r["term"].name for r in res if r["term"].status == "check"}
    gone = [k for k in old if k not in now and old[k]["row"] == "early" and k[0] in checked]

    def show(title, items, extra=True):
        print("== %s: %d" % (title, len(items)))
        for name, u, m, gap, ptr, note in items:
            print("   %-24s %s  [%s]  %d section%s before%s  (%s)\n          %s" % (
                name[:24], where(u), occ_id(next(x["term"] for x in res if x["term"].name == name), u, m),
                gap, "s"[:gap != 1], ", pointer" if ptr else "", note, snippet(u, m)))
        print()

    show("POINTER NO LONGER LEADS TO THE DEFINITION", sorted(broken, key=lambda x: x[1].idx))
    show("NEWLY EARLY", sorted(newly, key=lambda x: x[1].idx))
    show("FARTHER FROM THE DEFINITION", sorted(farther, key=lambda x: x[1].idx))
    show("ACCEPTANCES LAPSED", sorted(lapsed, key=lambda x: x[1].idx))
    print("== DEFINITION CHANGED: %d" % len(moved))
    for name, o, d, why in moved:
        print("   %s: was %s [%s], now %s [%s]; %s" % (
            name, o["where"], o["id"], where(d[0]) if d else "none",
            occ_id(next(x["term"] for x in res if x["term"].name == name), d[0], d[1]) if d else "-",
            why))
    print()
    print("not listed: %d early uses slightly farther (under %d more sections, or "
          "under %.1f times the distance)" % (len(drift), FARTHER_MIN, FARTHER_RATIO))
    print("better: %d no longer early, %d closer to the definition" % (len(gone), len(closer)))


def main():
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)      # quiet under | head
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--early", action="store_true")
    g.add_argument("--multi", action="store_true")
    g.add_argument("--unmarked", action="store_true")
    g.add_argument("--term", metavar="T")
    g.add_argument("--candidates", action="store_true")
    g.add_argument("--except", dest="exc", nargs="+", metavar="ID",
                   help="ids from a report; needs --why")
    g.add_argument("--except-phrase", nargs="+", metavar="P",
                   help="phrases --candidates stops listing; needs --why")
    g.add_argument("--stale", action="store_true")
    g.add_argument("--snapshot", nargs="?", const=SNAPSHOT, metavar="PATH",
                   help="write the state --compare reads (default %(const)s)")
    g.add_argument("--compare", nargs="?", const=SNAPSHOT, metavar="PATH",
                   help="what got worse since the snapshot")
    ap.add_argument("--why", help="the reason, kept in the exceptions file")
    ap.add_argument("--as", dest="kind_as",
                    choices=("not-term", "not-definition", "accept-early"),
                    help="with --except: the kind, instead of the one the report implies")
    ap.add_argument("--chapter", help="the number the book prints: 1..36, or A")
    a = ap.parse_args()
    if (a.exc or a.except_phrase) and not a.why:
        ap.error("--except and --except-phrase need --why")
    if a.except_phrase:
        return add_phrases(a.except_phrase, a.why)

    units, terms = read_book(), load_terms()
    if a.candidates:
        return report_candidates(units, terms)
    res = analyse(units, terms)
    if a.exc:
        return add_exceptions(res, a.exc, a.why, a.kind_as)
    if a.stale:
        return report_stale()
    if a.snapshot:
        return write_snapshot(res, a.snapshot)
    if a.compare:
        return report_compare(res, a.compare)
    if a.early:
        return report_early(res, a.chapter)
    if a.multi:
        return report_multi(res, a.chapter)
    if a.unmarked:
        return report_unmarked(res, a.chapter)
    if a.term:
        return report_term(res, a.term)

    print("%d sentences read (notes included); %d terms (%d glossary, %d from %s)" % (
        len(units), len(terms), sum(t.source == "glossary" for t in terms),
        sum(t.source == "tsv" for t in terms), os.path.relpath(TERMS_TSV, REPO)))
    exc = [r for r in EXC.values() if r["kind"] != "phrase"]
    stale = sum(1 for r in exc if r["id"] not in SEEN)
    print("%d exceptions in %s, %d applied, %d stale%s" % (
        len(EXC), os.path.relpath(EXC_TSV, REPO), len(exc) - stale, stale,
        " (--stale lists them)" if stale else ""))
    print()
    print("%-34s %5s %5s %6s %6s  %s" % ("term", "occ", "defs", "early", "ptr", "first definition"))
    for r in sorted(res, key=lambda r: r["definition"][0].idx if r["definition"] else 10**9):
        d = r["definition"]
        ptr = sum(1 for e in r["early"] if e[2])
        early = "-" if r["term"].status == "multi" else str(len(r["early"]))
        print("%-34s %5d %5d %6s %6d  %s" % (
            r["term"].name[:34], len(r["occ"]), len(r["defs"]), early, ptr,
            "%s (%s)" % (where(d[0]), d[2]) if d else "NONE"))


if __name__ == "__main__":
    main()
