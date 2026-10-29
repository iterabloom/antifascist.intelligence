# Coined terms before the reorganization (2026-10-29)

The state of the book's coined terms before the planned rearrangement of
chapters, kept as the baseline to compare against afterward (D-1115). Taken
from `d872fadf`, manuscript unchanged since `21ce30df`, with the 22 exceptions
of `finishing/coinages_exceptions.tsv` applied and none stale.

| File | Command |
|---|---|
| `summary.txt` | `coinages.py` |
| `early.txt` | `coinages.py --early` |
| `multi.txt` | `coinages.py --multi` |
| `unmarked.txt` | `coinages.py --unmarked` |
| `snapshot.tsv` | `coinages.py --snapshot finishing/reports/coinages_before-reorg_2026-10-29/snapshot.tsv` |

After the rearrangement:

    python3 finishing/tools/coinages.py --compare finishing/reports/coinages_before-reorg_2026-10-29/snapshot.tsv

`--compare` with no path reads `finishing/reports/coinages_snapshot.tsv`, which
is overwritten whenever a snapshot is retaken; this copy is not. The snapshot's
398 early uses include those of `multi` terms, which the reports leave out. A
snapshot is only comparable with the tool, term list and exceptions it was
taken under; a change to any of them after this date shows up in `--compare`
as differences the rearrangement did not cause.

## Counts

7,414 sentences, 87 terms (59 glossary, 28 from `finishing/coinages.tsv`); 144
early uses across 35 terms, 12 terms with more than one definition, 4 with no
marked definition.

## Reading of the reports

Not a ruling: the author has not ruled on any of this.

**Economic vocabulary used long before its definitions.** levy (24 early, from
§15.2, defined §32.1.4), backstop (12, from §16.1, defined §32.1.4), offer of
work (11, from §10.1, defined §32.1.2), allowance (7, from §23.7, defined
§32.1.3), placement (4, from the §9.2 note, defined in chapter 17). Suggested:
a one-clause gloss at first use rather than moving chapter 32.

**Other long gaps.** registration standard (§7.2 to §26.6, 110 sections);
instructed search (§19.1, chapter 20 and chapter 29, defined only in Appendix
F); severity scale (§5.2 to §22.2, 96); formed disposition (§13.4 to §26.6,
81); the Association (chapter 1 to the §16.2 note, 72); register (12 early,
from §11.4.3, defined §27.1); commons (§3.2 note to chapter 12, 43); branch
deposit (§27.2 to §33.3, 38); boundary model (§13.2 to §20.1, 33); formed
attention (6 uses in chapter 19 before chapter 20).

**Glossary pointers past an earlier definition.** Caregiving is glossed in
§20.1, the glossary points to §20.3. Backstop is defined in the §16.2 note, the
glossary points to §32.1.4. Offer of work has a human sense (§10.2) and a
bearer sense (§32.1.2); the glossary gives the second. Attestation's glossary
pointer, §13.2, only uses the term; its first use is §4.3.

**More than one definition.** Commons: one gloss nearly verbatim in chapter 12,
§19.1 and §27.1. Bearer: chapter 4, re-glossed in §6.10, §7.1 and chapter 21,
which read as reminders over long gaps. Floor court §6.5 and §14.3; integrated
signal §21.2 and §30.3; removal bond §12.2 and §13.6; emergency and
corroborated license §6.1 and §6.2.

**No marked definition.** second guardian (11 uses from §26.4, meaning never
stated); content clause (§28.7); departures (introduced plainly in §5.2);
attestation.

**Local.** machine student, affective concern, spec-based refusal: one or two
sections early. Appendix G's "Dormancy clock:" run-in label and "This is the
dormancy clock" at the end of the same paragraph duplicate each other.

**Likely tool misses, unruled.** regrowth (chapter 20), tripwire (§7.2) and the
four conditions of creation (§11.8) are explained in the sentence that uses
them. "Commitment" in the Introduction and chapter 1, and "standing" in chapter
3, may be the plain words.
