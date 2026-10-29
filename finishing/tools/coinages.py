"""Find the book's coined terms used before they are defined, and defined twice.

A term is the glossary's headwords plus the rows of finishing/coinages.tsv,
which also overrides how a glossary term is matched. The book is read in
ORDER.tsv order, sentence by sentence, with each \\note's sentences placed
right after the sentence that carries its marker. The glossary itself is not
read: it defines everything, at the end.

An occurrence of a term is DEFINING when it is

  emph     inside an \\emph{} or \\textit{} that holds little else: the term,
           an article, at most two more words;
  quoted   in curly quotes: “the floor”, “walls.”;
  framed   in a defining frame: "which I call X", "what this book calls X",
           "call it X", "known as X", "by X I mean", "X means", "X here means";
  glossed  followed straight by its gloss: "a commons: a population of
           bearers that...", "the floor court, the court whose...";
  pinned   the first occurrence in the section coinages.tsv names in
           `defined_at`, which wins over all of the above.

Every other occurrence is a USE. A term's definition is its first defining
occurrence, or, where earlier, its first occurrence in a section the
glossary's entry points to (kind `glossary`): those pointers are the book's
own claim about where the term is defined. A use is fine if the definition is in the same sentence or the
next one; a use earlier than that is reported.

Each class is a FLAG, not a verdict, on the same footing as deixis.py and
reader_tax.py. Emphasis is also stress, and a quote is also a quotation, so a
"definition" here is a place the prose marks a term, and the author decides
whether it defines it. Not in check_all.sh.

THE REPORTS

  (default)     counts, and the terms in each report below
  --early       uses before the definition, by term. A use whose sentence
                points at the definition's chapter or section (§6.2,
                chapter 6) is tagged `pointer`.
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
                coinages.tsv.

  --chapter N   restrict --early, --multi and --unmarked to definitions or
                uses in one chapter (the number the book prints).

COINAGES.TSV, the hand-kept part, columns:

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

    finishing/tools/coinages.py                 summary
    finishing/tools/coinages.py --early         the read
    finishing/tools/coinages.py --multi
    finishing/tools/coinages.py --term "own-case rule"
"""
import argparse, os, re, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (REPO, order_rows, read_tsv, section_labels, chapter_numbers,
                    ref_numbers, tex_prose_line, _take_arg, numkey)

GLOSSARY = "manuscript/sections/chZ/glossary.tex"
TERMS_TSV = os.path.join(REPO, "finishing", "coinages.tsv")

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
    __slots__ = ("idx", "path", "line", "label", "chapter", "text", "emph", "note")

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
    for i, u in enumerate(units):
        u.idx = i
    return units


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
GLOSS_AFTER = re.compile(
    r"^(?:s|es)?[”’]?(?:\s+of\s+[\w-]+)?(?::|\s+—)\s+(?:a|an|the)\s"
    r"|^(?:s|es)?[”’]?,\s+(?:a|an|the)\s+(?:[\w-]+\s+){0,2}?(?:that|which|whose|who|where)\b")
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
    return "use"


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
            out.append((u, m, classify(u, m)))
    return out


def analyse(units, terms):
    printed = ref_numbers()
    res = []
    for t in terms:
        longer = [o for o in terms if o is not t and t.rx.search(o.name)
                  and len(o.name) > len(t.name)]
        occ = occurrences(units, t, longer)
        if not occ:
            res.append(dict(term=t, occ=[], defs=[], definition=None, early=[]))
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
        early = []
        if definition is not None:
            d = definition[0].idx
            dnum = printed.get(definition[0].label, definition[0].label)
            for u, m, kind in occ:
                if u.idx < d - 1:
                    early.append((u, m, pointer(u.text, dnum, definition[0].chapter)))
        # distinct defining sites: one per run of sentences within one of each other
        sites, last = [], -10
        for o in defs:
            if o[0].idx - last > 1:
                sites.append(o)
            last = o[0].idx
        res.append(dict(term=t, occ=occ, defs=sites, definition=definition, early=early))
    return res


def pointer(text, dnum, dchap):
    """True if the sentence points at the definition's chapter or section."""
    for n in re.findall(r"§\s*([0-9A-Z]+(?:\.\d+)*)", text):
        if n == dnum or dnum.startswith(n + ".") or n.startswith(dnum + "."):
            return True
    for n in re.findall(r"\b(?:[Cc]hapters?|Ch\.|Appendix)\s+([0-9A-Z]+)\b", text):
        if n == dchap:
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
        print("   def:   %s" % snippet(u, m))
        for eu, em, ptr in early:
            print("   %-7s %s\n          %s" % ("pointer" if ptr else "use", where(eu), snippet(eu, em)))
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
            print("   %-7s %s\n          %s" % (kind, where(u), snippet(u, m)))
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
            print("   %-12s %s\n               %s" % (tag, where(u), snippet(u, m)))
        return
    print("no term matches %r (terms come from the glossary and %s)" %
          (name, os.path.relpath(TERMS_TSV, REPO)))


def report_candidates(units, terms):
    seen = Counter()
    first = {}
    known = lambda p: any(t.rx.fullmatch(p) for t in terms)
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


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--early", action="store_true")
    g.add_argument("--multi", action="store_true")
    g.add_argument("--unmarked", action="store_true")
    g.add_argument("--term", metavar="T")
    g.add_argument("--candidates", action="store_true")
    ap.add_argument("--chapter", help="the number the book prints: 1..36, or A")
    a = ap.parse_args()

    units, terms = read_book(), load_terms()
    if a.candidates:
        return report_candidates(units, terms)
    res = analyse(units, terms)
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
