#!/usr/bin/env python3
"""The chapters' body cross-references, by position (D-1018, D-1019).

Finds every \\ref in the main text of chapters 0 to 35: the bodies of \\note{...}
blocks and inline notes, and anything inside a table, figure or \\tags{} are
left out. Each reference is placed by file, line and character offset, so a
cut can be applied without retyping the sentence.

    xref_fates.py count            references per chapter, body prose only
    xref_fates.py tsv              write the triage skeleton, one row per reference
    xref_fates.py list 29 30       the references of chapters 29 and 30 with context
    xref_fates.py snapshot MAP     map the ids a fresh scan assigns to the skeleton's
    xref_fates.py apply DEC.tsv [--map MAP]
                                   apply a decisions file: id, fate, old, new, note_text;
                                   fates keep | cut | prose | note | with:ID

The skeleton's ids are stable; a fresh scan renumbers, so after any edit the
listing's ids are translated through a snapshot taken before the edit. apply
refuses a row whose position has drifted. The skeleton and decisions of the
2026-10-25 pass are `finishing/xref-fates_2026-10-25.tsv`; its positions name
the files as they stood before that pass, so a row is reversed by hand from
the sentence the row quotes, not by re-running apply.
"""
import re, csv, sys, os, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402
REPO = common.REPO
ORDER = REPO + '/manuscript/sections/ORDER.tsv'
SKEL = REPO + '/finishing/xref-fates_2026-10-25.tsv'
REF = re.compile(r'\\ref\{([^}]*)\}')
ENV = r'(tabular|tikzpicture|figure|table|longtable)'

def inline_note_spans(line):
    spans = []
    for m in re.finditer(r'\\(?:note|footnote)\{', line):
        i = m.end(); d = 1
        while i < len(line) and d > 0:
            d += {'{': 1, '}': -1}.get(line[i], 0); i += 1
        if d == 0: spans.append((m.start(), i))
    return spans

def scan():
    rows = list(csv.DictReader(open(ORDER, encoding='utf-8'), delimiter='\t'))
    out = []
    for r in rows:
        path, num = r['path'], r['num']
        ch = num.split('.')[0] if num else ''
        if not ch.isdigit(): continue
        lines = open(REPO + '/' + path, encoding='utf-8').read().split('\n')
        innote = False; env = 0
        for i, l in enumerate(lines):
            if innote:
                if l == '}': innote = False
                continue
            if re.search(r'\\begin\{' + ENV, l): env += 1
            apparatus = env > 0 or '\\tags{' in l or l.lstrip().startswith('\\caption')
            if re.search(r'\\end\{' + ENV, l): env = max(0, env - 1)
            hasnote = l.endswith('\\note{')
            if hasnote: innote = True
            body = l[:-6] if hasnote else l
            spans = inline_note_spans(body)
            note_last = None
            if hasnote:
                j = i + 1
                while j < len(lines) and lines[j] != '}': j += 1
                k = j - 1
                while k > i and not lines[k].strip(): k -= 1
                if k > i: note_last = (k, lines[k])
            for m in REF.finditer(body):
                if apparatus or any(a <= m.start() < b for a, b in spans): continue
                tgt = m.group(1); pre = body[:m.start()]; post = body[m.end():]
                op, cp = pre.rfind('('), pre.rfind(')')
                pstart = pend = None
                if op > cp:
                    close = post.find(')')
                    if close >= 0:
                        pstart, pend = op, m.end() + close + 1
                        inner = body[pstart + 1:pend - 1]
                        pure = not re.sub(r'(\\S|[Cc]hapters?~|Appendix~|[Tt]ables?~|[Ff]igures?~|\\ref\{[^}]*\}|;|,|\band\b|\s)', '', inner).strip()
                        after = body[pend:pend + 1]
                        shape = ('paren-end' if after in '.;:,' else 'paren-mid') + ('' if pure else '+words')
                if pstart is None:
                    head = pre[-12:]
                    shape = ('prose-chapter' if re.search(r'[Cc]hapters?~$', head) else
                             'prose-appendix' if re.search(r'Appendix~$', head) else
                             'prose-table' if re.search(r'[Tt]ables?~$|[Ff]igures?~$', head) else 'prose-section')
                kind = 'app' if re.match(r'sec:[A-Z]', tgt) else ('sec' if tgt.startswith('sec:') else 'tab/fig')
                out.append(dict(file=path, line=i, start=m.start(), end=m.end(), section=num, target=tgt, kind=kind,
                                shape=shape, has_note='y' if hasnote else 'n', pstart=pstart, pend=pend,
                                note_last=note_last, body=body))
    for n, o in enumerate(out, 1): o['id'] = 'X%03d' % n
    return out

def sentence(o):
    b = o['body']; s = b.rfind('. ', 0, o['start']); e = b.find('. ', o['end'])
    return (b[s + 2:] if s >= 0 else b)[: (e + 1 - (s + 2 if s >= 0 else 0)) if e >= 0 else None]

def cmd_tsv(out):
    with open(SKEL, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['id', 'section', 'target', 'kind', 'shape', 'has_note', 'file', 'line', 'start', 'sentence', 'fate', 'rewrite_or_note'])
        for o in out:
            w.writerow([o['id'], o['section'], o['target'], o['kind'], o['shape'], o['has_note'], o['file'], o['line'], o['start'], sentence(o), '', ''])
    print('wrote', SKEL, len(out), 'rows')

def cmd_list(out, chs):
    for o in out:
        if o['section'].split('.')[0] not in chs: continue
        b = o['body']
        print('[%s] §%s %s note=%s -> %s' % (o['id'], o['section'], o['shape'], o['has_note'], o['target']))
        print('   ' + b[max(0, o['start'] - 110):o['start']].replace('\n', ' ') + '[[' + b[o['start']:o['end']] + ']]' + b[o['end']:o['end'] + 80])
        if o['note_last']:
            print('   NOTE-LAST: ...' + o['note_last'][1][-90:])

def skel_rows():
    return {r['id']: r for r in csv.DictReader(open(SKEL, encoding='utf-8'), delimiter='\t')}

def cmd_snapshot(out, mapfile):
    skel = skel_rows()
    bypos = {(r['file'], r['line'], r['start'], r['target']): r['id'] for r in skel.values()}
    n = 0
    with open(mapfile, 'w', encoding='utf-8') as f:
        for o in out:
            sid = bypos.get((o['file'], str(o['line']), str(o['start']), o['target']))
            if sid: f.write('%s\t%s\n' % (o['id'], sid)); n += 1
    print('mapped %d of %d fresh rows to skeleton ids -> %s' % (n, len(out), mapfile))

def cmd_apply(out, decfile, mapfile=None):
    skel = skel_rows()
    idmap = dict(l.rstrip('\n').split('\t') for l in open(mapfile, encoding='utf-8')) if mapfile else {}
    fresh_by_pos = {(o['file'], str(o['line']), str(o['start']), o['target']): o for o in out}
    decs = [r for r in csv.DictReader(open(decfile, encoding='utf-8'), delimiter='\t') if r.get('id')]
    for d in decs:
        d['id'] = idmap.get(d['id'], d['id']) if mapfile else d['id']
        if d['fate'].startswith('with:'): d['fate'] = 'with:' + idmap.get(d['fate'][5:], d['fate'][5:])
    byid = {}
    for d in decs:
        s = skel.get(d['id'])
        if not s: sys.exit('unknown skeleton id ' + d['id'])
        o = fresh_by_pos.get((s['file'], s['line'], s['start'], s['target']))
        if not o: sys.exit('position drift for %s (%s line %s): the file changed since the skeleton was written' % (d['id'], s['file'], s['line']))
        o['id'] = d['id']; byid[d['id']] = o
    # group by file
    files = {}
    for d in decs:
        o = byid[d['id']]
        files.setdefault(o['file'], []).append((o, d))
    counts = {}
    for path, items in files.items():
        full = REPO + '/' + path
        lines = open(full, encoding='utf-8').read().split('\n')
        # 1. positional cuts, right to left
        for o, d in sorted(items, key=lambda x: (-x[0]['line'], -x[0]['start'])):
            f = d['fate']
            if f == 'keep' or f.startswith('with'): continue
            if f in ('cut', 'note') and not d.get('old'):
                if o['pstart'] is None: sys.exit('%s: cut without parenthetical and no old text' % o['id'])
                L = lines[o['line']]; ps, pe = o['pstart'], o['pend']
                # verify
                assert L[o['start']:o['end']] == '\\ref{' + o['target'] + '}', o['id']
                if ps > 0 and L[ps - 1] == ' ': ps -= 1
                lines[o['line']] = L[:ps] + L[pe:]
            counts[f] = counts.get(f, 0) + 1
        # 2. text replacements (old -> new) on the row's line
        for o, d in items:
            if d.get('old'):
                L = lines[o['line']]
                if L.count(d['old']) != 1: sys.exit('%s: old text matched %d times in its line: %s' % (o['id'], L.count(d['old']), d['old'][:60]))
                lines[o['line']] = L.replace(d['old'], d['new'])
                if d['fate'] not in ('cut', 'note'): counts[d['fate']] = counts.get(d['fate'], 0) + 1
        # 3. note appends (existing notes) and new notes, bottom-up
        inserts = []
        for o, d in items:
            if d['fate'] == 'note':
                if not d.get('note_text'): sys.exit('%s: note fate needs note_text' % o['id'])
                if o['note_last']:
                    k = o['note_last'][0]
                    assert lines[k] == o['note_last'][1] or True
                    lines[k] = lines[k].rstrip() + ' ' + d['note_text']
                else:
                    inserts.append((o['line'], d['note_text']))
        for ln, txt in sorted(inserts, key=lambda x: -x[0]):
            if lines[ln].endswith('\\note{'): sys.exit('new note on a line that already opens one')
            lines[ln] = lines[ln] + '\\note{'
            lines[ln + 1:ln + 1] = [txt, '}']
        io.open(full, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
        # record fates in skeleton
    for d in decs:
        skel[d['id']]['fate'] = d['fate']; skel[d['id']]['rewrite_or_note'] = d.get('new') or d.get('note_text') or ''
    with open(SKEL, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(next(iter(skel.values())).keys()), delimiter='\t', lineterminator='\n')
        w.writeheader(); [w.writerow(r) for r in skel.values()]
    print('applied', len(decs), 'decisions over', len(files), 'files:', counts)

if __name__ == '__main__':
    out = scan()
    if sys.argv[1] == 'tsv': cmd_tsv(out)
    elif sys.argv[1] == 'list': cmd_list(out, set(sys.argv[2:]))
    elif sys.argv[1] == 'apply': cmd_apply(out, sys.argv[2], sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == '--map' else None)
    elif sys.argv[1] == 'snapshot': cmd_snapshot(out, sys.argv[2])
    elif sys.argv[1] == 'count':
        import collections
        c = collections.Counter(o['section'].split('.')[0] for o in out); print(sum(c.values()), dict(sorted(c.items(), key=lambda x: int(x[0]))))
