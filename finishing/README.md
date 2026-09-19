# finishing/

Working area for the campaign to finish the book. Everything here is new work;
nothing in the provenance record — `summaries/`, `manuscript/previous/`, what
remains of `generation/`, and the persona-device archive at the repository root —
is touched by it. That record is read-only.

New files here omit the date suffix, as the file convention allows.

## What is where

| Path | What it is |
|---|---|
| `STATE.md` | **The handoff. Read this first.** Its lead paragraph is the current state, written fresh each pass; everything below it is the same paragraph from earlier passes, marked superseded and kept |
| `PLAN.md` | The finishing plan: ordered passes, each with entry/exit criteria, unit of work, and decider |
| `DECISIONS.md` | Append-only decision log, `D-NNN`. A reversal is a new dated line, never an edit |
| `QUESTIONS.md` | The open batch for the author. Each item has a recommended default and the event at which the default applies |
| `reviews/` | The source text of the outside editorial reviews, read-only. Only two survive; the second through fifth were never preserved and exist only as quotation inside `p8`–`p10-scope.md`. See `reviews/README.md` |
| `renumber-map_<date>.tsv` | Old-to-new section numbers for each renumbering (D-031, D-043). Notes written before a renumber keep the old numbers; these files are the translation |
| `outline.tsv` | The live outline: number, title, level, parent. Seeded once from column A of the v3b assignment spreadsheet, hand-maintained after that |
| `ledger.tsv` | One row per section: status, action, evidence, decisions. The work tracker |
| `refs-ledger.tsv` | One row per bibliography key: whether a human has checked that entry against the source it names, when, and by whom. Hand-edited, or marked with `tools/refs_ledger.py --mark`. The count of `yes` rows is what the draft footer prints on every page (D-319). **What counts as a check is not defined here** and is the author's to set: the file records a flag, and nothing tests what earned it |
| `pNN-scope.md` | One per pass: what was asked, what checking found, what was done, and what was left. Named from `PLAN.md`, `STATE.md` and `DECISIONS.md` |
| `xref-paragraphs-{related,unrelated}.md` | Every body paragraph carrying a cross-reference, sorted by whether the reference bears on the paragraph's point (D-161, P80). **A hand read, not regenerable by a tool**; the test it applies is stated in each file's header |
| `tools/` | Read-only analysis and invariant checks (see below) |
| `reports/` | Generated, committed, small. Regenerate rather than hand-edit |

The tool table below covers what a session finishing the book would reach for. **Nine further scripts in `tools/` are deliberately not listed**: `common.py` and `odsread.py` are libraries, `html_single_file.py` is documented in `pipeline.md` where it runs, and `triage.py`, `apply_triage.py`, `toc_v4.py`, `list_candidates.py` and `refs_to_latex.py` are one-shot instruments from P0–P1 and the D-066 conversion, kept because they record how the structure was decided and not because anything should run them again. The ninth is `redundancy.py`, which is not omitted on purpose but **cannot run on this machine**: P62 found that neither package it needs is installed, and `pipeline.md` carries that finding. The line above about running it offline with the venv on PATH describes a machine this is not.

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
| `overleaf.py` | Round-trips the manuscript through Overleaf: `export` writes a package that compiles there as it stands (verified — 186 pages, zero undefined references, the same as `build_tex.sh`; **and the main document is `book.tex`, which is why `\documentclass` sits there and not in `preamble.tex` — D-170, after an Overleaf compile picked the preamble and died on "no legal `\end` found"**), `import` applies the zip back and repairs what the edit invalidated. **The import is the half with the design in it.** It discards `sections.tex` and regenerates it; it syncs a retitle into the three files that copy the title, ORDER.tsv fatally; and it reads a manifest carried in the package to tell an Overleaf edit from a repository edit made since the export, refusing the file where both moved. **A renumber, a depth change, a broken heading or a deleted file stops the whole import with nothing written**, because each needs rows in files the package does not carry. Runs `check_all.sh` at the end — which says the structure survived, not that the prose did. Packages live in `~/book-scratch/overleaf/`, outside the repository, and a path inside it is refused. D-169. See `pipeline.md` |
| `outline_extract.py` | Seeds `outline.tsv` from the spreadsheet's column A only |
| `render_markdown.py` | The whole manuscript as one file in `/tmp`, absolute path on stdout. Markdown by default (D-318); **`--tex` writes the LaTeX instead** (D-334) — `book.tex` with every `\input` resolved and `refs.bib` inside a `filecontents` block, every file between `START`/`END` markers naming its path, for pasting somewhere that should see the source. **`--no-notes`** strips the `note` field from all 161 entries that carry one, 670 KB to 608 KB; it is refused without `--tex`, the Markdown carrying no bibliography. **Neither form carries a trace of the draft apparatus** (D-335): the Markdown prints no status line, and `--tex` removes the apparatus from the preamble it inlines — conditionals, definitions, generated counts and the comments explaining them — so the file reads as though it had never been written. A gate refuses to write anything if a word of the vocabulary survives in the master or preamble, the book's prose held aside while it runs. A PDF built from the rendered `.tex` is therefore a draft with no watermark and no footer saying so. Order and numbers come from `ORDER.tsv`, so the reading order is the book's by construction. **Both outputs are disposable and the LaTeX under `manuscript/sections/` is the source**: nothing reads either back, and an edit made there is lost on the next run. The Markdown warns on stderr naming any LaTeX command that reached the output unconverted — teach the script, do not hand-fix the file. **The `.tex` compiles**, to 164 pages and the same text, but that is a side effect: five paragraphs break their last line differently, because concatenating the sections drops a space token `\input` contributes at each file boundary, and the proof is built from `manuscript/book.tex`. `AGENTS.md` carries the SOP, and describes the Markdown form only |
| `headings.py` | Three-way reconcile: manuscript / outline / TOC. `--write-toc` regenerates the TOC; `--check` fails if the TOC on disk is not what regeneration would produce (D-042), and is run by `check_all.sh` |
| `refresh_order_shas.py` | Rewrites `ORDER.tsv`'s sha256 column from the files. `check_structure.py` fails on a stale digest; this clears it |
| `refs_ledger.py` | The bibliography's human-check tracker, and the two macros the draft footer prints from it (D-319). A plain run syncs `refs-ledger.tsv` to `refs.bib` and regenerates `manuscript/draft-status.tex`; `--mark KEY --by jgs` and `--unmark KEY` set a row from the shell, though the TSV is meant to be edited by hand as well. **`--check` is in `check_all.sh`** and fails on drift between ledger and bibliography in either direction, on a `checked` value that is not `yes` or `no`, and on stale macros, so a page cannot print a count the ledger does not carry. The timestamp beside that count is **not** generated here: TeX computes it as the job starts, so this file stays stable between builds and its `--check` keeps meaning something |
| `section_stats.py` | Per-section counts and the generation's tells; `--seed-ledger` |
| `reader_tax.py` | What the prose charges the reader that the argument does not need (D-117). The taxonomy is read off the author's own hand edits at `331f0a5..fc65cd5`, and every class cites the edit it comes from. **Candidates for a hand read, not defects** — `deixis` is a pool of 222, measured 2026-09-01, and most of it is fine — and deliberately not in `check_all.sh`. It finds only the four classes a regular expression can find; the other six need reading |
| `xref_shapes.py` | Sorts every cross-reference by the **shape** of its sentence — signpost, restated, appended, attributive, structural, and the `imports` keep class — so a density cut can be argued rather than guessed. Built for P28 (D-089) and the instrument P53 (D-118) used to explain P28's shortfall: **the removable shapes total 47 and 307 of 398 prose references are `inline`** (re-measured at P80 on 2026-08-31; the committed report has now been found stale twice, at P57 and again at P79, so **regenerate it before reading it**), where the reference is a term in the sentence and no tool reaches it. **Candidates for a hand read, not defects.** Not in `check_all.sh` |
| `xref_pairs.py` | Writes every cross-reference's citing sentence next to its target's opening sentence, to `reports/xref_pairs.txt` (D-111). For Q-041's class — a reference that resolves and names a claim its target does not make. **Blind to anything the target's first sentence does not show**, which is what P50 found by reading instead |
| `negatives.py` | Negative claims made next to a citation — what a source *does not* say (D-126). Built for Q-056's fourth mechanism: a claim that a source says something can be checked by opening it, and a claim that it does **not** cannot, because confirming an absence means reading the whole document. Two tiers: `cited`, a negation inside a sentence carrying a citation, and `adjacent`, a negation plus a source-word whose neighbour in the same paragraph carries one. **Candidates for a hand read, not defects** — most hits are negations about the world, not about a source — and not in `check_all.sh`. The first run was 36 rows, all read: three were claims about a document's contents and all three held on checking; the one real defect it found was a fourth shape, an unbounded negative about a body of testing (D-126, corrected at D-127). Writes `reports/negatives.tsv` |
| `antithesis.py` | Censuses the corrective antithesis — *X rather than Y*, *not X but Y*, *that is not a P, it is a Q* — and locates every instance (D-159). Built for P78 after Q-038 tracked one of its forms through four passes. **Its point is `--clusters`, not the census**: applied one instance at a time the shape is defensible at 1 repair in 25 to 37, measured four times, and what the reading cannot see is density — an isolated antithesis reads as a correction and two inside sixty words do not. Overlapping matches are merged, because *not a weak version of one somebody can but a different kind of object* fires two patterns over one construction and counting patterns overstated the doubled sentences by 14 of 47 on the first run. **Candidates for a hand read, not defects**, and not in `check_all.sh` |
| `hedge_pairs.py` | Hunts the recurring defect Q-043 names and D-331 asked a later pass to hunt: one proposition conceded in one place and asserted past the concession in another (D-378). A concession lexicon (inability, and withdrawal of a ground the book itself laid down) and an assertion lexicon (necessity, inferential connective, universal), then content-word overlap weighted by inverse document frequency **over sections** so the book's own furniture — floor, bearer, operator — carries almost nothing. A sentence that concedes and asserts in one breath counts as conceding, which was the first version's loudest false positive. Scores add the two positional facts the found instances shared: the assertion in a closing position, and the two members in one paragraph. **Calibrated against the tree before the fixes** (`9505cd8`): it surfaces 3 of the 5 known instances, D-332 and D-331 ranked first in their sections, D-330 about fifth. **D-328 and D-336 are out of reach and stay out** — D-328's defect is a sweep against a *distinction*, not against a concession, and D-336 is an overclaim with no concession anywhere to pair against. **Candidates for a hand read, not defects**, and most of what it prints is the careful register working: *A shows X; it does not show Y*. Not in `check_all.sh`. Writes `reports/hedge_pairs.tsv` |
| `epigram.py` | Finds the landing line followed by the sentence that qualifies it — a conclusion-shaped sentence next to the limit, the cost, or the other half of a two-sided finding (D-255). Built for P155 after four passes made the same repair before anyone named it one class. **Its finding is negative and is the reason it exists**: 125 pairs in 59 sections, and a hand read of all 5 `balanced` pairs, every pair in the four named sections and the two densest, and the top `--tails`, found **zero clear instances** — most pairs are a verdict that opens a gap the next sentence fills, parallel list items, or a definition before its consequence, and **in two places the proposed inversion would make the prose worse**. The four named cases share the second side of a finding sitting in a weaker grammatical position, and the position differs every time, so the class has no syntactic signature. `--tails` carries the one shape a pattern does reach. Marks whether the qualifier is the paragraph's last sentence, a limit in final position being emphatic rather than discarded. **Candidates for a hand read, not defects**, and not in `check_all.sh`. Writes `reports/epigram.tsv` |
| `deixis.py` | Censuses the sentence that opens on a bare *This*, *That*, *These*, *Those*, *It* or *They* with a verb straight after it and no noun naming the referent (D-164). Built for P82. **Its point is `--hard`, not the census**: the opening is mechanical and selects **285 of 3,440 sentences**, measured 2026-09-01 after P84, and whether one is a defect is a fact about the sentence *before* it, so every hit is graded — `para-initial`, `after-long` (preceding sentence 40+ words, the author's own condition) and `after-short`. **The author's literal condition, 50 words and three clauses, selects 18 of 299 and the hand read repaired 11**; the 225 in `after-short` were sampled and left, which is what D-117 already recorded about `reader_tax.py`'s narrower `deixis` class. **Candidates for a hand read, not defects**, and not in `check_all.sh` |
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
from the spreadsheets inside the persona-device archive and is never written to disk. Material of the persona kind that is
part of the record goes into that archive, never into the tree as text; material
that must not be in the repository at all goes to `~/ethical.superintelligence-private/`.

**Commit sign-off.** `git commit -s` is mandatory. A commit without a DCO
sign-off is rejected. Don't put anything you need to keep into a trailer.
