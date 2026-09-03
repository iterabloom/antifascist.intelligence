#!/usr/bin/env python3
"""Candidate finder for cross-references that can go without losing an argument (P28, D-089).

The book cross-references at one reference per 120 words of prose. The count is
not itself the fault -- D-013 built the regime deliberately, to replace an
argument made nine times with one place it is made and pointers from the rest --
but at that density a reader meets a number every few sentences and the prose
reads as a repository being navigated.

This sorts every reference by the SHAPE of the sentence carrying it, because
shape is what separates a reference doing work from one decorating a claim the
sentence already makes. style.md section 7 states the test in prose: the
sentence carrying a reference has to make sense to a reader who does not follow
it. A reference that survives that test twice over -- the sentence makes sense
without it AND without the number the reader loses nothing -- is spendable.

Five removable shapes, and they are removable for different reasons:

  signpost      the whole sentence is a location announcement ("Section 8.2.3
                takes up what has to happen first."). Nothing is claimed. Cut
                the sentence.
  restated      the sentence gives the content AND says where else it lives
                ("Section 6.1.1 describes what COMPAS did: score Black
                defendants..."). Cut the pointer, keep the content.
  appended      a locator hung off the end of a finished clause ("...is the
                standard technical response and is covered at section 4.2.2").
  attributive   a relative clause that only re-attributes ("The Partnership on
                AI, which section 8.4.2 takes apart as a voluntary body...").
  structural    the book explaining its own filing ("...which is why sections
                6.4.2 and 6.4.3 treat these separately").

And one keep class, reported so the ratio is visible rather than assumed:

  imports       the sentence borrows a result and cannot stand without saying
                whose it is ("Section 7.2's argument for learning from
                disagreement applies here with unusual force"). These are the
                regime D-013 built and D-078 added to. They stay.

A HIT IS A CANDIDATE FOR A HAND READ, NOT A DEFECT -- the P14 precedent, and it
held here: on the P28 run the shape classifier's own accuracy was the limit, not
the reader's judgment. Verb lists cannot tell "section 3.1 argues that an
operator is a party that can be compelled" (imports a result) from "section
8.6.1 describes a review body" (names one), and the difference is what the
citing sentence needs, not what the verb is.

WHAT IT CANNOT SEE. Whether the target still says what the citing sentence
claims -- that is xref_content.py. Whether a reference the reader would want is
missing -- nothing checks that. Deliberately NOT wired into check_all.sh: the
output needs judgment, not a pass/fail gate.

Usage:  python3 finishing/tools/xref_shapes.py > finishing/reports/xref_shapes.tsv
        python3 finishing/tools/xref_shapes.py --summary
"""
import re, sys, os, csv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

# After rendering, "section~\ref{sec:8.7.6}" reads "section 8.7.6" -- the
# reference is matched in the prose exactly as a reader meets it.
REF = re.compile(r'(?:[Ss]ections?|[Cc]hapters?|§)\s*\d{1,2}(?:\.\d{1,2}){0,2}'
                 r'(?:\s*(?:,|and|through|to)\s*\d{1,2}(?:\.\d{1,2}){0,2})*')

# Verbs of coverage: the target holds material on a topic. A sentence whose
# only verb is one of these is telling the reader where to file something.
COVER = (r'covers?|takes? up|takes? apart|describes?|sets? out|works? through|'
         r'treats?|discusses?|addresses?|examines?|turns? to|goes? (?:in)?to|'
         r'spends?|gives?|lists?|names?|supplies?|walks? through|surveys?|'
         r'is where|are where|has|have|contains?|carries|carry|runs? through')

# Verbs of result: the target established something this sentence is using.
# A sentence built on one of these loses a load-bearing part if the reference
# goes, because the claim is being borrowed rather than located.
IMPORT = (r'argues?|shows?|establishes?|rules? out|finds?|concludes?|holds?|'
          r'defines?|identifies?|separates?|requires?|proves?|demonstrates?|'
          r'settles?|answers?|denies?|declines?|reverses?|corrects?|makes? the'
          r'|leaves? open|is right|was right|says? to|admits?|records?')

SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z“(])')


def sections():
    _, rows = common.read_tsv(os.path.join(common.SECTIONS, 'ORDER.tsv'))
    rows.sort(key=lambda r: common.numkey(r['num']))
    out = []
    for r in rows:
        path = os.path.join(common.REPO, r['path'])
        with open(path) as fh:
            paras, _ = common.tex_sections_of(fh.readlines())
        out.append((r['num'], r['path'], paras))
    return out


def openers(nums):
    """A section is an opener if some other section is numbered beneath it."""
    s = set(nums)
    return {n for n in s if any(o != n and o.startswith(n + '.') for o in s)}


def classify(sent, ref, start, end):
    """Return (shape, why). Order matters: the first shape that fits wins."""
    before = sent[:start].strip()
    after = sent[end:].strip()
    words = len(sent.split())

    # possessive name-drop: "section 10.3.3's whole argument" with no claim made
    if re.match(r"[’']s\s+(whole\s+)?(argument|point|case|claim|thesis|finding)\b", after):
        if not re.search(r'\b(is|are|was|were)\b.{0,40}(that|:)', after):
            return 'possessive', 'names an argument instead of making it'

    # appended locator: reference closes the sentence after a finished clause
    if re.match(r'^[).,;]*$', after) or re.match(r'^\)?[.,;]?$', after):
        if re.search(r'\b(?:covered|discussed|described|set out|treated|taken up|'
                     r'see|per|cf\.?)\s*(?:at|in|by)?\s*$', before, re.I):
            return 'appended', 'locator hung off a finished clause'
        if before.endswith('(') or re.search(r'\(\s*$', before):
            return 'appended', 'parenthetical locator'

    # parenthetical anywhere
    if re.search(r'\(\s*$', before) and re.search(COVER, after):
        return 'appended', 'parenthetical locator'

    # signpost: sentence opens on the reference and only locates
    if not before or before in ('(', '“'):
        if re.match(r'^(?:%s)\b' % COVER, after.lstrip(), re.I) and words <= 30:
            if not re.search(r'[:—]', sent):
                return 'signpost', 'sentence is a location announcement'
            return 'restated', 'gives the content and says where else it lives'
        if re.match(r'^(?:%s)\b' % IMPORT, after.lstrip(), re.I):
            return 'imports', 'borrows a result'

    # attributive relative clause: ", which section X covers as ..."
    if re.search(r',\s*(?:which|whom|that)\s*$', before, re.I) and re.search(
            r'^(?:%s)\b' % COVER, after.lstrip(), re.I):
        return 'attributive', 're-attributes a noun the sentence already names'

    # structural self-justification
    if re.search(r'which is why\s*$', before, re.I):
        return 'structural', 'the book explaining its own filing'

    if re.search(r'^(?:%s)\b' % IMPORT, after.lstrip(), re.I) or re.search(
            r"[’']s\s+(argument|finding|result|criteria|test|definition)", after):
        return 'imports', 'borrows a result'

    return 'inline', 'reference is a term in the sentence'


REMOVABLE = ('signpost', 'restated', 'appended', 'attributive', 'structural',
             'possessive')


def main():
    summary = '--summary' in sys.argv
    secs = sections()
    op = openers([n for n, _, _ in secs])
    rows, counts, words = [], {}, {}
    for num, path, paras in secs:
        # The glossary's references are locators in a reference apparatus, not
        # prose a reader is reading through; counted, reported apart.
        kind = 'glossary' if num == '11' else ('opener' if num in op else 'leaf')
        for para in paras:
            for sent in SENT.split(para):
                for m in REF.finditer(sent):
                    shape, why = classify(sent, m.group(0), m.start(), m.end())
                    counts[shape] = counts.get(shape, 0) + 1
                    words[shape] = words.get(shape, 0)
                    rows.append({
                        'num': num, 'kind': kind, 'shape': shape,
                        'removable': 'y' if shape in REMOVABLE else '',
                        'ref': m.group(0), 'why': why,
                        'sentence': ' '.join(sent.split())[:400],
                        'path': path,
                    })

    if summary:
        gl = [r for r in rows if r['kind'] == 'glossary']
        rows_p = [r for r in rows if r['kind'] != 'glossary']
        counts = {}
        for r in rows_p:
            counts[r['shape']] = counts.get(r['shape'], 0) + 1
        tot = len(rows_p)
        print(f'{tot} references in the prose, by shape\n')
        for s in sorted(counts, key=lambda k: -counts[k]):
            flag = 'REMOVABLE' if s in REMOVABLE else 'keep'
            print(f'{counts[s]:>5}  {100*counts[s]/tot:>5.1f}%  {s:<12} {flag}')
        rem = sum(counts.get(s, 0) for s in REMOVABLE)
        print(f'\n{rem} candidates ({100*rem/tot:.1f}%), {tot-rem} kept')
        print(f'{len(gl)} more in the glossary, counted apart')
        for k in ('opener', 'leaf'):
            sub = [r for r in rows_p if r['kind'] == k]
            n = sum(1 for r in sub if r['removable'])
            print(f'  {k:<8} {len(sub):>4} refs, {n:>3} candidates')
        return

    w = csv.DictWriter(sys.stdout, fieldnames=list(rows[0]), delimiter='\t',
                       lineterminator='\n')
    w.writeheader()
    w.writerows(rows)


if __name__ == '__main__':
    main()
