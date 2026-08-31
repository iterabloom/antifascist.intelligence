# finishing/

Working area for the campaign to finish the book. Everything here is new work;
nothing in `genesis/`, `personas/`, `generation/`, `editorial/`, `summaries/`,
or `manuscript/previous/` is touched by it — those stay read-only provenance.

New files here omit the date suffix, as the file convention allows.

## What is where

| Path | What it is |
|---|---|
| `PLAN.md` | The finishing plan: ordered passes, each with entry/exit criteria, unit of work, and decider |
| `DECISIONS.md` | Append-only decision log, `D-NNN`. A reversal is a new dated line, never an edit |
| `QUESTIONS.md` | The open batch for the author. Each item has a recommended default and the event at which the default applies |
| `reviews/` | The source text of the outside editorial reviews, read-only. Only two survive; the second through fifth were never preserved and exist only as quotation inside `p8`–`p10-scope.md`. See `reviews/README.md` |
| `renumber-map_<date>.tsv` | Old-to-new section numbers for each renumbering (D-031, D-043). Notes written before a renumber keep the old numbers; these files are the translation |
| `outline.tsv` | The live outline: number, title, level, parent. Seeded once from column A of the v3b assignment spreadsheet, hand-maintained after that |
| `ledger.tsv` | One row per section: status, action, evidence, decisions. The work tracker |
| `tools/` | Read-only analysis and invariant checks (see below) |
| `reports/` | Generated, committed, small. Regenerate rather than hand-edit |

The tool table below covers what a session finishing the book would reach for. **Eight further scripts in `tools/` are deliberately not listed**: `common.py` and `odsread.py` are libraries, `html_single_file.py` is documented in `pipeline.md` where it runs, and `triage.py`, `apply_triage.py`, `toc_v4.py`, `list_candidates.py` and `refs_to_latex.py` are one-shot instruments from P0–P1 and the D-066 conversion, kept because they record how the structure was decided and not because anything should run them again.

## The manuscript's working form

The book is LaTeX (D-065). The editable form is one file per section:

```
manuscript/sections/chNN/NN_NN_NN.tex   heading command, label, body
manuscript/sections/ORDER.tsv           path, num, title, sha256
manuscript/book.tex                     the master; \input's the sections
manuscript/sections.tex                 that \input list, generated
```

Filenames are zero-padded and `_`-separated so byte-order sorting reproduces
book order (with `.` as the separator a child sorts before its parent).

The dialect era — `<<quote>>`, `<<list>>`, `[[cite:ID]]`, and the joined
`parseable_text_v4.txt` — ended at D-065. Its two reference texts, v3b and v4,
were removed from the repository at D-088; git holds them at every commit
before that one, and the tools that read them are in `tools/dialect-era/`.

## Tools

Run from the repo root. Stdlib-only except `redundancy.py`, which needs the venv
on PATH and runs offline (`HF_HUB_OFFLINE=1`). (`quarry_map.py`, named here
until D-118, is not in the repository and appears in no commit; the reference was
wrong rather than stale.)

| Tool | Does |
|---|---|
| `check_all.sh` | Every invariant below. Run at session start; **run automatically by `.githooks/pre-commit`**, which refuses the commit on failure (D-045). It reads the working tree, not the index, so a partial commit is checked against the tree on disk; `git commit --no-verify` bypasses |
| `check_structure.py` | Heading/filename agreement, glob order, tag balance, ledger row parity |
| `check_xrefs.py` | Cross-references resolve, and every one is prefixed with `section`/`chapter`/`§` so a renumber script can see it (D-046). Does **not** check that a resolving reference is the right one |
| `xref_content.py` | The semantic half `check_xrefs.py` disclaims (D-050): flags references whose citing sentence names a proper noun, acronym or year the target section does not contain. Writes `reports/xref_content.tsv`. **Candidates for a hand read, not defects** — the P14 run was 9 real out of 121 — and deliberately not in `check_all.sh`. Blind to any wrong pointer in a sentence naming none of those, which is most sentences |
| `names_guard.py` | Enforces the named-persons rule (see below) |
| `check_typography.py` | Quotes and dashes are the characters they should be, in the sections and in `refs.bib` (D-082). In `check_all.sh` |
| `check_frozen.py` | Kept with an empty registry since D-088; it passes without reading anything. The docstring says how to freeze a file again |
| `gen_book.py` | Generates `manuscript/sections.tex` from `ORDER.tsv`. `--check` is the invariant; re-run it after any add, remove or renumber |
| `build_tex.sh` · `build_html.sh` · `build_proof.sh` | The PDF, the one-file HTML page, and both into `reports/` as the committed proof pair. See `pipeline.md` |
| `outline_extract.py` | Seeds `outline.tsv` from the spreadsheet's column A only |
| `headings.py` | Three-way reconcile: manuscript / outline / TOC. `--write-toc` regenerates the TOC; `--check` fails if the TOC on disk is not what regeneration would produce (D-042), and is run by `check_all.sh` |
| `refresh_order_shas.py` | Rewrites `ORDER.tsv`'s sha256 column from the files. `check_structure.py` fails on a stale digest; this clears it |
| `section_stats.py` | Per-section counts and the generation's tells; `--seed-ledger` |
| `reader_tax.py` | What the prose charges the reader that the argument does not need (D-117). The taxonomy is read off the author's own hand edits at `331f0a5..fc65cd5`, and every class cites the edit it comes from. **Candidates for a hand read, not defects** — `deixis` is a pool of 232 and most of it is fine — and deliberately not in `check_all.sh`. It finds only the four classes a regular expression can find; the other six need reading |
| `xref_shapes.py` | Sorts every cross-reference by the **shape** of its sentence — signpost, restated, appended, attributive, structural, and the `imports` keep class — so a density cut can be argued rather than guessed. Built for P28 (D-089) and the instrument P53 (D-118) used to explain P28's shortfall: **the five removable shapes total about 100 references and 625 of 806 are `inline`**, where the reference is a term in the sentence and no tool reaches it. **Candidates for a hand read, not defects.** Not in `check_all.sh` |
| `xref_pairs.py` | Writes every cross-reference's citing sentence next to its target's opening sentence, to `reports/xref_pairs.txt` (D-111). For Q-041's class — a reference that resolves and names a claim its target does not make. **Blind to anything the target's first sentence does not show**, which is what P50 found by reading instead |
| `negatives.py` | Negative claims made next to a citation — what a source *does not* say (D-126). Built for Q-056's fourth mechanism: a claim that a source says something can be checked by opening it, and a claim that it does **not** cannot, because confirming an absence means reading the whole document. Two tiers: `cited`, a negation inside a sentence carrying a citation, and `adjacent`, a negation plus a source-word whose neighbour in the same paragraph carries one. **Candidates for a hand read, not defects** — most hits are negations about the world, not about a source — and not in `check_all.sh`. The first run was 36 rows, all read: three were claims about a document's contents and all three held on checking; the one real defect it found was a fourth shape, an unbounded negative about a body of testing (D-126, corrected at D-127). Writes `reports/negatives.tsv` |
| `inventories.py` | Counts sentences carrying a series of three or more items, per chapter (D-101). Its limit is on the record: the syntactic test missed the shape that produces the reading experience, an inventory spread over consecutive sentences, so P37's diagnosis was made by reading |
| `tics.py` | Censuses the generation's verbal tics and voice markers; writes `reports/tics.tsv` and `reports/voice.tsv` |
| `claims.py` | Extracts every assertion needing a source and every dated claim, to `reports/claims.tsv` — the P4 sourcing record, 536 rows |
| `choose-a-random-page.py` | One random page of the book as markdown, for a before/after revision pass, written to `~/book-scratch/random-pages/`. The page always opens on a heading; the page number is a cross-product estimate that runs high by a median of 18 pages, and the docstring carries the measurement and the `--pages` value that fixes it |

## Two rules that bite

**Named persons (D-017).** The hazard is the **persona device**: this repository
is full of text a language model produced while pretending to be a named real
person. None of it may reach the book, a planning file, or a commit message as
though that person had said or done it. Reviews from the editorial record are
cited by file and index or line range, never by name.

What the rule does **not** forbid is ordinary scholarly citation. Naming the
researchers who published a finding, quoting a published claim and citing it,
and describing a documented event in a laboratory are normal nonfiction and are
allowed everywhere, including in the book.

`names_guard.py` therefore tests for the persona-device *shape* — a name within
range of "reviewed by", "rated", "in their review", "writing as", "in the voice
of", "simulated", and similar — and hard-fails on that anywhere. Other name hits
are listed as citations for a human to confirm. The name list is built in memory
from the spreadsheets and is never written to disk. Material that must exist and
cannot live here goes to `~/ethical.superintelligence-private/`.

**Commit sign-off.** `git commit -s` is mandatory. A commit without a DCO
sign-off is rejected. Don't put anything you need to keep into a trailer.
