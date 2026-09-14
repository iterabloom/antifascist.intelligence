# P205 — §8.2.2 and §8.3.5 cut, the specificity lesson kept as one sentence

The author's finding, given whole: *§8.2.2 and §8.3.5 overlap heavily and are
both policy inventory. The specificity lesson — ask the public about facial
recognition, not about AI — is the one thing worth keeping and it's a sentence.*
**Executed as given.** The book is **89 sections, 74,121 words and 155 pages**,
suite green, 0 undefined references and 0 undefined citations.

## What was checked before cutting

The finding was verified rather than assumed, because two sections and 720 words
were going.

**The overlap is real and it is the public tier.** §8.2.2 opened on literacy
work taking the form of *a course to enroll in*, which reaches *the people who
came looking*; §8.3.5's first run-in head was *The public tier is the one nobody
owns*, and its argument was that the familiar mechanisms *reach people already
inside the pipeline*. Those are the same claim. Around it both sections ran an
inventory — courses, degree programs, pre-university curricula, certification,
deliberation formats — which is the description the author gave them.

**Both were misfiled as well as redundant.** §8.2.2, *AI Literacy Outside the
Classroom*, sat under §8.2 *Ask the People It Happens To*, which is about who is
in the room when a system is designed. §8.3.5, *Literacy, Training, and Where
Each One Sits*, sat under §8.3 *The Political Economy of AI and Power*, whose
other four children are concentration, the jobs guarantee, the right to produce,
and wages for a bearer. Neither section was where its subject belonged.

**Nothing in the book depended on either.** Zero `\ref` resolve to `sec:8.2.2` or
`sec:8.3.5`. No glossary entry defines a term they were the last home of — the
check is P48's defect class run in the other direction, a term surviving in the
glossary after its section goes. The one consequence worth recording is that
***literacy* now appears nowhere in the book**: it occurred three times, all of
them in these two sections.

**Neither cut renumbers anything.** §8.2.2 was the last of §8.2's two children
and §8.3.5 the last of §8.3's five, so §8.2.1 and §8.3.1–§8.3.4 keep their
numbers. **No renumber map was written, because no number changed meaning.**

## The sentence that was kept

It closes §8.2.1's citizen-assembly item, after the four assemblies already
listed there — Ireland, the 2023 US panel, Taiwan, French-speaking Switzerland:

> The Ada Lovelace Institute's Citizens' Biometrics Council shows what the format
> needs from its question: fifty members of the UK public were asked not what they
> thought about AI, a question almost nobody can answer usefully, but about facial
> recognition — a thing with a location, an operator, and a consequence.

**The wording is the book's own.** The second clause is §8.2.2's own sentence,
carried over intact; only the frame in front of it is new. P7 (D-032) drew the
specificity argument out of this council in the first place, cutting the MIT
Museum example and keeping this one, so the sentence preserves that pass's work
rather than restating it.

**The placement is §8.2.1's citizen-assembly item and not §8.2's opener**, because
the council is itself a citizens' assembly — fifty members of the public
deliberating over an extended period — and the lesson is a condition on the
format the item describes. It sits after the item's closing *And forty randomly
selected residents…*, so the enumeration of instances stays intact and the lesson
lands on top of it.

**One antithesis was accepted deliberately.** *Not what they thought about AI…
but about facial recognition* is the shape `antithesis.py` censuses and D-025
sweeps. It is kept because the contrast is the content — the lesson is a
difference between two questions — and because the tool's own finding is that an
isolated instance is defensible and density is what is not. This one is isolated:
§8.2.1 carries no other.

## The bibliography, checked by hand

The two sections carried six sources between them and **all six were cited
nowhere else**. Five moved to `unused_bibliography.bib` with a dated comment
block, per D-111's convention: `helsinki2020elements`, `grosz2019embedded`,
`harvardgazette2019ethics`, `harvardcs108schedule`, `ieeesa2020certifaied`.
`adalovelaceinstitute2021biometrics` stayed in `refs.bib`, cited by the kept
sentence.

**Nothing in `check_all.sh` tests that `refs.bib` corresponds to the book**, which
is the gap D-302 named when a moved section nearly dropped a key. It was
therefore checked directly after the move: **222 entries, all 222 cited, none
cited-but-missing.** `refs.bib` went 227 → 222 and `unused_bibliography.bib` 187
→ 192.

**The first run of that check was wrong and the correction is worth keeping.** A
pattern matching `\autocite{` reported two uncited entries, `eu2024aiact` and
`spinoza1985collected`. Both are cited in the optional-argument form
`\autocite[Art.~101]{…}`, which the pattern did not reach. **A citation check
written for the bare form silently misses every page-locator citation**, and the
failure looks like a finding rather than like a bug.

## One defect found on the way out

§8.3.5's opening paragraph read: *Cross-training among developers, ethicists and
legal scholars has already been named as a lever on a system's immediate
environment.* **Nothing in the book names it.** `cross-train` appears in no other
section; *lever on a system's immediate environment* appears nowhere at all. The
nearest thing is §8.1, which argues for funding structures that make
collaboration expensive to walk away from — a claim about grants and venues, not
about training people.

This is D-050's class: a pointer that reads as a back-reference and resolves to
nothing. It is recorded rather than repaired, the section carrying it being gone.
**It also corroborates the author's reading of the section**: an inventory opening
on a reference to material the book does not contain.

## Two things left for the author

**§8.2 now has a single child.** With §8.2.2 gone, §8.2 *Ask the People It
Happens To* (210 words) has exactly one subsection, §8.2.1 (785 words). **Every
other parent in the book has two or more**; this is the first. Folding §8.2.1's
text up into §8.2 would close it and would take the book to 88 sections, and the
merged section would run about 995 words, under the 1,500 at which §4a wants
run-in heads — and it already carries one. **Not done here**: it is a ruling about
§8.2's structure, not about the overlap this pass was given.

**The book is down to one `accepted` row.** §8.2.2 was one of two; chapter~6 is
the other. That status came from the 2026-08-23 blanket instruction — *I accept
them. Do them. Do P4 on them.* — which the row's own ledger note disclosed as not
the section-by-section read the standing rule requires, so the acceptance was
weaker than the column suggests. Recorded because the column now reads 1.

## Files touched

| File | Change |
|---|---|
| `manuscript/sections/ch08/08_02_01.tex` | one sentence added to the citizen-assembly item |
| `manuscript/sections/ch08/08_02_02.tex` | deleted |
| `manuscript/sections/ch08/08_03_05.tex` | deleted |
| `manuscript/sections/ORDER.tsv` | two rows removed; one sha256 refreshed |
| `manuscript/sections.tex` | regenerated, 89 inputs |
| `manuscript/table-of-contents.txt` | regenerated, 89 entries |
| `finishing/outline.tsv`, `finishing/ledger.tsv` | two rows each removed |
| `finishing/refs.bib`, `finishing/unused_bibliography.bib` | five entries moved |
| `finishing/DECISIONS.md`, `finishing/STATE.md`, `finishing/PLAN.md` | D-307, new lead, header figures |

## Measured after

89 sections, 74,121 words, 155 pages, 258 cross-references against 89 labels, 222
bibliography entries all cited, 0 undefined references and 0 undefined citations.
Suite green.

**The committed proof pair is now stale.** It is `whole-book-proof_2026-09-13` at
157 pages and the book is 155; `README.md` still says 157. Rebuilding it is the
"make the proofs" sequence and was not run this pass.
