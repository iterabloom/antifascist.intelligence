#!/usr/bin/env python3
"""Pre-filter for resolving-but-wrong cross-references (P14, D-050).

check_xrefs.py answers "does this reference resolve?" It cannot answer "does
the target still say what the citing sentence claims it says?" -- the failure
D-046 recorded and P14 found eight more instances of. This narrows that
semantic question to a readable candidate list.

For each reference, pull the citing sentence, extract its salient tokens
(proper-noun phrases, acronyms, years), and report those absent from the
target section.

A HIT IS A CANDIDATE FOR A HAND READ, NOT A DEFECT. On the P14 run, 121
candidates over 610 reference-instances yielded 9 real defects; the rest were
the extractor mistaking a sentence-opening word for a proper noun, or a term
that legitimately belongs to the citing section rather than the target.

WHAT IT CANNOT SEE. A wrong pointer in a sentence naming no proper noun,
acronym or year is invisible to it -- and that is most sentences. It is a
net with a known mesh size, not a proof of correctness. It is deliberately
NOT wired into check_all.sh: its output needs judgment, not a pass/fail gate.

PORTED TO LATEX AT D-070. It read .txt sections and matched section numbers
typed into the prose. D-065 made the sections .tex and D-066 turned every
reference into \\ref{sec:N}, after which this tool matched nothing and said
so only in a line on stderr -- "0 references scanned" -- which is why the
D-067 split had to be checked by hand. Both the citing sentence and the
target are rendered to prose through common.tex_sections_of first, so a
proper noun that appears only inside a citation key cannot count as either a
salient token or a match.

Usage:  python3 finishing/tools/xref_content.py > finishing/reports/xref_content.tsv
"""
import re, sys, os, csv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

# After rendering, "section~\ref{sec:8.7.6}" reads "section 8.7.6", so the
# reference is matched in the prose exactly as a reader meets it.
REF = re.compile(r'(?:[Ss]ections?|[Cc]hapters?|§)\s*(\d{1,2}(?:\.\d{1,2}){0,2})')

STOP = set("""The A An In It Its This That These Those There Here What When Where Which Who Why How
And But For Nor Yet So Or If Then Than As At By Of On To From With Without Within
I We One Two Three Four Five Six Seven Eight Nine Ten Section Sections Chapter Chapters
AI Al Both Each Every Neither Either Some Most Much More Less Not No Nothing None
Section's Chapter's Whether Because Since While Although Though After Before Once
Stated Given Read Take Taken Call Called Consider Suppose Say Said Note Notice
His Her Their Our Your My Its' Do Does Did Done Be Been Being Is Are Was Were
Now Today Later Earlier Above Below Same Other Another Such Only Even Still Just
Chapters' First Second Third Fourth Fifth Sixth Last Next New Old Real
""".split())


def load_order():
    _, rows = common.read_tsv(os.path.join(common.SECTIONS, 'ORDER.tsv'))
    rows.sort(key=lambda r: common.numkey(r['num']))
    return [(r['num'], r['path'], r['title']) for r in rows]


def prose_of(path, unknown=None):
    """The section's paragraphs, rendered to the prose a reader sees."""
    with open(os.path.join(common.REPO, path), encoding='utf-8') as fh:
        paras, _ = common.tex_sections_of(fh.readlines(), unknown)
    return paras


def sentences(line):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z"—])', line)


def salient(sent):
    """Proper-noun phrases, acronyms, 4-digit years."""
    out = set()
    # multi-word capitalized phrases, allowing internal lowercase joiners
    for m in re.finditer(r"\b[A-Z][\w'’-]*(?:\s+(?:of|the|for|and|on|in|to|de)\s+[A-Z][\w'’-]*|\s+[A-Z][\w'’-]*)*", sent):
        phrase = m.group(0).strip()
        words = phrase.split()
        if len(words) == 1 and (phrase in STOP or len(phrase) < 4):
            continue
        # drop a leading stopword-ish sentence opener
        while words and words[0] in STOP:
            words = words[1:]
        if not words:
            continue
        phrase = ' '.join(words)
        if len(phrase) < 4 or phrase in STOP:
            continue
        out.add(phrase)
    for m in re.finditer(r'\b(1[89]\d\d|20\d\d)\b', sent):
        out.add(m.group(0))
    for m in re.finditer(r'\b([A-Z]{2,}(?:/[A-Z]{2,})?)\b', sent):
        if m.group(1) not in ('AI',):
            out.add(m.group(1))
    return out


def main():
    order = load_order()
    num2path = {n: p for n, p, _ in order}
    num2title = {n: t for n, _, t in order}
    unknown = set()

    prose = {n: prose_of(p, unknown) for n, p, _ in order}

    # a chapter reference covers all its descendants
    def target_text(num):
        return '\n'.join('\n'.join(prose[n]) for n in prose
                         if n == num or n.startswith(num + '.'))

    w = csv.writer(sys.stdout, delimiter='\t')
    w.writerow(['src', 'ref', 'target_title', 'missing', 'sentence'])
    n_refs = n_hits = 0
    for num, path, _ in order:
        for para in prose[num]:
            for sent in sentences(para):
                refs = REF.findall(sent)
                if not refs:
                    continue
                toks = salient(sent)
                for r in sorted(set(refs)):
                    n_refs += 1
                    if r not in num2path:
                        continue
                    tgt = target_text(r)
                    miss = sorted(t for t in toks
                                  if t not in tgt and t not in num2title.get(r, ''))
                    # ignore tokens that are themselves section-ref noise
                    miss = [m for m in miss if not re.fullmatch(r'\d{1,2}(\.\d{1,2}){0,2}', m)]
                    if miss:
                        n_hits += 1
                        w.writerow([path, r, num2title.get(r, ''),
                                    ' | '.join(miss), sent.strip()[:300]])
    print('# %d reference-instances scanned, %d candidates' % (n_refs, n_hits),
          file=sys.stderr)
    if not n_refs:
        # The failure this tool actually had: it scanned nothing and reported
        # it in a line easily read as a clean result.
        print('# xref_content: NO REFERENCES FOUND -- the tool is not reading '
              'the manuscript. Do not read this as a clean run.', file=sys.stderr)
        return 1
    if unknown:
        print('# WARNING: unknown LaTeX commands dropped from the prose: %s'
              % ', '.join(sorted(unknown)), file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())
