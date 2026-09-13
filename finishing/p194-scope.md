# P194 — the September 13 Overleaf return, imported with its citations repaired

The author edited the manuscript in Overleaf, downloaded the result through Google
Drive to `~/book-scratch/Sep13.zip`, and asked for it to be imported. The package
was exported at `a8e4974` on 2026-09-13 and returns 15 changed files, one retitle,
and about 4,470 words of new prose. **Nothing structural was refused and nothing
conflicted**, which is the first import in six to arrive that way.

**The edit threads one concept through the book.** Chapter~1 names the
*remainder* — what a compression left out — §2.1.2 restates its own four
structural features as operations on it, §2.2 generalizes the move as a
*selection rule* that admits whatever it already measures, §7.1 and §9.3.5 stop
naming the features and point at §2.2 instead, and the glossary gains the term.
§13's entry is the one place the whole chain is written down.

## The dry run, and what it caught

15 to apply, 78 unchanged, `sections.tex` skipped as generated, **0 conflicts and
0 problems**. One retitle: **chapter~2 becomes *The Striving and the Electricity
Bill***, synced by the import into `ORDER.tsv`, `outline.tsv` and `ledger.tsv`,
with the TOC regenerated after. Five files came back missing the final newline
the repository's copy has and the import restored it.

## What the import left broken, and the repair

**The suite failed on typography: 35 ASCII em dashes on 23 lines in 11 files.**
Overleaf returns `---` where the book writes `—`, which is `style.md` §8 and is
the documented shape of every return so far. Converted; no `----` and no bare
`--` existed anywhere in the affected files, so the substitution was safe to make
globally. `refresh_order_shas.py` then cleared the 11 stale digests the edits
left in `ORDER.tsv`.

**Q-087 did not grow, for the first time.** The manuscript carries 7 `\textit`
against D-189's `\emph`, in `02_01_02.tex` and `02_02_03.tex`, and the counts at
`HEAD` were 5 and 2 — **the same seven.** Five previous imports each added new
ones. This one added none. The standing seven are untouched and still open.

## Two citation gaps, both repaired

The author added six bibliography entries in Overleaf for a new German
militant-democracy cluster. Two halves of it did not meet.

**`bgh2007hakenkreuz` was cited at `03_02.tex:27` with no entry anywhere** —
not in `refs.bib`, not in `unused_bibliography.bib`. That is an undefined
citation, which the build would have reported and the invariant suite does not
reach.

**`molier2018germanys` was an entry nothing cited**, against the standing
property that every entry in `refs.bib` is cited. Its subtitle names the
Federal Constitutional Court's potentiality criterion for party bans, and
`09_01_01.tex` has a sentence about exactly that criterion citing the judgment
alone, so the site was not in doubt. The commentary now sits beside the judgment
there.

**Both entries were verified against sources before anything was written**, which
is what `style.md` §6 permits since D-204 and the reason it permits it:

- **BGH, 15 March 2007, 3 StR 486/06**, Third Criminal Senate, on appeal from
  Landgericht Stuttgart's judgment of 29 September 2006. Reported at **BGHSt 51,
  244; NJW 2007, 1602; NStZ 2007, 466.** Checked against the court's own press
  release and the reported headnote. The prose's account of it is accurate: a
  business selling stickers and badges to the punk scene bearing crossed-out
  Nazi symbols, acquitted on the ground that a depiction plainly expressing
  opposition falls outside §~86a's protective purpose.
- **Molier and Rijpkema**, *European Constitutional Law Review* 14, no. 2
  (2018), **394–409**, doi `10.1017/S1574019618000196`. The author's entry
  carried the volume and year; the issue, pages and doi were added from
  Cambridge Core.

Both render correctly in the build, and the in-text form of the BGH judgment
matches the author's own `bverfg2017npd` — `(Durchgestrichenes Hakenkreuz 2007)`
beside `(Nationaldemokratische Partei Deutschlands II 2017)`. **Neither entry
type prints its court.** `institution` is dropped by the style for
`@jurisdiction`, so the References name the case and not the body that decided
it; the BGH entry's note now opens with *Bundesgerichtshof* to cover that, and
**the author's NPD~II entry still does not name the Bundesverfassungsgericht
anywhere except through `BVerfGE 144, 20`.** The prose names both courts, so no
reader is stranded, and the fix in the entry is a one-line edit somebody should
make.

## The author's TODO, answered

`09_01_01.tex` came back carrying a three-line comment: *verify against
Braunthal before publication — the Bavarian figures below are from a secondary
source and are not confirmed as his. If they cannot be sourced, the preceding
sentence carries the paragraph on its own.*

**The figures are sound and Braunthal is not their source**, so neither branch of
the instruction was the answer. The federal totals in the preceding sentence are
Braunthal's and check out against his publisher's own description of the book:
3.5 million screened, about 2,000 disciplinary proceedings, 2,250 refusals, 256
dismissals. **The Bavarian breakdown — 102 rejected from the left against two
from the right, 1973–1980 — belongs to Friedbert Mühldorfer's *Radikalenerlass*
in the *Historisches Lexikon Bayerns***, last revised 16 June 2014, which gives
those two numbers for those years and adds roughly 227,000 screened in Bavaria
between 1973 and 1982 for 127 refusals. The sentence keeps its figures and now
cites the work that states them. The comment is gone from the manuscript.

Its typo is worth one line since the comment is gone from the tree: it read
*would shifts the printed numbers*.

## §11.5a, which the suite cannot see

The return inserts a **second `\section` inside `11_05.tex`** — *Can a Population
Coordinate Without Converging?*, labelled `sec:11.5a` — with a comment saying the
label is deliberate and temporary and that renumbering belongs to a later
proofreading pass. **It was left exactly as it arrived.** What it costs is worth
recording, because nothing in the repository will bring it up again:

- **The book prints nine sections in chapter~11, ending at 11.9.**
  `table-of-contents.txt`, `outline.tsv`, `ledger.tsv` and `ORDER.tsv` all know
  **eight**, ending at 11.8. The committed TOC omits a section the book contains.
- **The new section prints as 11.6.** Its four successors therefore print one
  number above their label names: `sec:11.6` prints 11.7, `sec:11.7` prints 11.8,
  `sec:11.8` prints 11.9. Every reference still resolves and still lands in the
  right place, so the divergence is between label names and printed numbers, not
  between a pointer and its target.
- **Nothing references `sec:11.5a`.** The only occurrence outside the label is
  the author's comment.
- **`check_all.sh` passes on all of it**, because `check_structure.py` and
  `headings.py` read one heading per file. **A second section inside an existing
  file is invisible to the whole suite**, and it is the one structural change
  `overleaf.py import` is built to refuse that can get past it — a new file, a
  renumber, a depth change and a deleted file are all caught.

Splitting the file and renumbering is a renumber-map plus a sweep, which is the
work the author's comment defers. It is not done here.

## Two things found in passing

**`check_typography.py` tests the TeX quote notation `` `` `` and `` '' `` in
`refs.bib` only, and its pass message claims the sections too.** The sections'
rule list carries the straight double quote and the two ASCII dash runs;
`` `` ``/`` '' `` are in the `refs.bib` list alone. The line it prints on success
reads *no straight quotes, no ASCII dashes, no TeX quote notation*, which
overstates what was checked.

**The manuscript has 12 of them.** Two arrived with this import, in
`03_02.tex` — one of them a regression, `“Refusal”` having been correct at `HEAD`
and come back as `` ``Refusal'' `` — and **both were converted.** The other ten
predate this import, in `06_03.tex` (4), `09_01.tex`, `10_03.tex` and
`03_02.tex`'s neighbours, and **were left**: they are not this import's doing and
sweeping four unrelated files would bury the edit in the diff. They compile
correctly — TeX's ligatures set them as the right glyphs — so this is notation
consistency and not a visible defect.

**22 whitespace-only lines came back** between new paragraphs, in 8 files, where
`HEAD` had none in the manuscript at all. Cleaned, plus one of the same kind in
`refs.bib`. **Output-neutrality was measured, not assumed**: `pdftotext` digest
`e793432e4712` before the clean and after it, 156 pages both times.

## What the prose does, section by section

- **§1** names the remainder and gives five instances of it being dropped in
  order to decide — a metric, an annotator under quota, a rater's disagreement
  entering a reward model as variance, a form with no field for humiliation, an
  officer with twenty seconds a target.
- **§2** replaces the selection argument's load-bearing half with **Friston's
  account of self-maintenance** \(`friston2013life`\) and states the objection
  against it from **the Markov-blanket critique** \(`bruineberg2021markov`\),
  concluding that what the criticism reaches is not the part the argument needs.
  The selection route stays and is demoted: optimizing weights is a search inside
  one run, not a lineage, so the analogy gives back less than it borrows.
- **§2.1.2** says why there are four features and not some other number — they
  are four directions rather than four items — and concedes that nothing
  establishes it and a fifth is not ruled out.
- **§2.2** states the selection rule once, as the general form.
- **§3.1** forward-points to §3.6 for what *exhaustively* costs.
- **§3.2** gains the worked German instance: §~86a read for seventy years, the
  1994 amendment for confusingly similar symbols, the Kühnen salute covered and
  the sloppy salute not, *Blood and Honour* outside the statute, and the 2007
  acquittal whose qualification turns on the thickness of a strike-through.
- **§3.6** separates the two attacks on an enumeration — decomposition defeats
  the unit, variation defeats the description — and prices the second against the
  German record.
- **§3.7** takes on the tension the section had not admitted: correction is a
  channel for convergence, so what a population transmits is an aperture rather
  than an output, and the property is a pair — reopenable to the case, closed to
  the operator.
- **§4.1** replaces the one-dial framing with two objects, each set on its own,
  and maps §3.2's two marks onto them.
- **§7.1** and **§9.3.5** stop restating the structural features and point at
  §2.2.
- **§9.1.1** is the largest addition: militant democracy run at two settings for
  seventy-five years, the failures all at the setting where a body assesses a
  threat, and the finding that the danger tracks whether a prohibition is
  enumerated in advance rather than whether the tradition is militant. It closes
  on the tension between the book's own halves — §3.2 asks for assessment inside
  the machine, which is the capturable setting — and declines to resolve it.
- **§11.5a** is the new research-agenda entry, with a falsifier: measure output
  convergence and revision-on-another's-evidence separately, and if the second
  falls as the first rises the fourth way cannot be built.

## Measured on the current tree

**90 sections by `ORDER.tsv` and 91 printed**, **74,648 words** (70,178 before),
**156 pages** (147), **256 cross-references** resolving against 91 labels (234
against 90), **227 `refs.bib` entries, every one cited, 0 undefined references
and 0 undefined citations.** `unused_bibliography.bib` is unchanged at 187, so
the two files total 414 against 406 before: **the author authored six entries and
this pass authored two**, both from verified metadata. Suite green.

**The six biber warnings in the build are pre-existing** legacy `month` fields in
older entries. None of the eight new entries produced one, and the non-standard
`@jurisdiction` and `@legislation` types biblatex aliases to `@misc` compiled
without complaint.

## What was not done

**The proofs were not remade.** The committed pair is
`whole-book-proof_2026-09-13` at 147 pages and `README.md` links it at that
count; the book is now 156. **Both are stale and neither was touched**, that
being the author's own gesture.

**The new prose was read and not audited.** It was read whole, and its citations
were reconciled against `refs.bib` and its cross-references against the label
set. Nobody checked it for redundancy against the chapters it draws on, and the
remainder material now appears at six sites that were written to be read in
sequence. **Chapters~4, 5 and~11 have still never been read as prose**, and §11.5a
is new prose inside one of them.

**`QUESTIONS.md`'s forty-one open questions have now gone seven passes
unchecked.** Several name sections the September 12 return had already rewritten,
and this return rewrote more of chapters~2, 3 and~9.

**Not rerun:** `claims.tsv`, `epigram.tsv`, `xref_shapes.tsv`, `negatives.tsv`,
`redundancy_*.tsv`, and `xref_content.py`, whose semantic check is the one that
could bear on 22 new cross-references. `section_stats.py` was rerun.
`xref-paragraphs-{related,unrelated}.md` remain hand reads keyed to paragraphs
largely gone.

**`c8b1a97`, `c0b24bd` and `0fcf381` still have no row, lead or scope file.**
