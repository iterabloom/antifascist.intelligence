# P31 — chapter 9 from a catalogue into a prioritized research program

**The author's instruction, 2026-08-28:** convert chapter 9 from a catalogue into
a prioritized research program — near-term experiments, falsifiers, required
datasets, and governance prerequisites — without increasing the chapter's word
count.

## The diagnosis, and why the structure was the catalogue

The instruction uses a word this project has already defined against itself.
`style.md` section 2a names **the catalogue** as a condemned shape: "a numbered
run of theories, techniques, or frameworks, one paragraph each, with an example
and a 'challenge' attached." Chapter 9 was a numbered run of research areas, one
section each, with a nearest-existing-work note attached.

Two things made it one, and only one of them was the prose.

**The section order carried no argument.** The chapter divided into 9.1 *Ethics
and Social Reasoning in AI* (seven subsections) and 9.2 *Emotional Intelligence,
Affective Computing, and Altruism* (two). That division mirrors chapter 2's topic
list — 2.1 ethical frameworks, 2.2 empathy, 2.3 affect — so the chapter's shape
was inherited from the survey it was reporting gaps in, not from anything about
the gaps. A reader reaching the end had nine problems and no reason to start with
one rather than another.

**The sections closed on restatement.** Six of the nine ended by saying again, in
general terms, that the problem was open: "no general method exists to tell the
difference before deployment"; "it remains unsolved"; "neither problem is closed."
That is the shape `style.md` section 2 deletes on sight, and it is what a
catalogue entry does instead of telling you what to do.

What was already good, and is kept: the chapter opener's bounded epistemic claim
(a search is not a survey), the nearest-existing-work note against each gap — now
carried by the section that owns the gap rather than duplicated in the opener —
and the refusal to pad a gap the book cannot specify.

## The change, in two parts

### 1. The chapter is flat and ordered by priority

The 9.1/9.2 split is dissolved. Nine sections, numbered in the order the program
runs. The ranking criterion is stated in the opener and is **what this book's own
argument fails without** — not tractability, and not what a field is ready to
fund.

| new | was | title | why it sits here |
|---|---|---|---|
| **9.1** | 9.2.2 | Interpretability, Self-Reports, and Resistance to Tampering | the book ranked this itself: old 9.1.7 calls interpretability "the most load-bearing unsolved problem in this book." A commitment that fine-tunes out for twenty cents is not a floor, and the same instrument is what 9.2 needs |
| **9.2** | 9.1.7 | What Is Owed to a Bearer, and Who Could Check | chapter 3's direct debt. The book argues for building a prospective moral patient and cannot say what is owed to it or who could check |
| **9.3** | 9.1.6 | What an Antifascist Detector Would Actually Have to Detect | the capability chapters 4 through 6 assume and no chapter specifies |
| **9.4** | 9.1.2 | When an Ethics-Embedding Method Stops Generalizing | without a pre-deployment discriminator, no method in chapters 4 and 5 can be shown to have worked |
| **9.5** | 9.1.3 | Value Learning as Unfinished Technical Research | the training regime everything above runs on |
| **9.6** | 9.1.5 | Can a Multi-Agent AI System Resist Being Captured? | a design the book proposes and cannot yet specify a training target for |
| **9.7** | 9.1.4 | Open Questions in Empathy and Theory-of-Mind Research | chapter 2's evidence base; the book's argument survives either resolution |
| **9.8** | 9.2.1 | Is Emotion Legible From a Face at All? | the book already relies on this failing, so either answer leaves the argument standing |
| **9.9** | 9.1.1 | The Responsibility Gap, Which No Experiment Closes | not a research problem at all. It is the governance prerequisite that gates deploying anything above it, and it is retitled to say so |

`finishing/renumber-map_2026-08-28b.tsv` is the map. **No section's argument was
rewritten to fit its new position.** The moved prose is the prose the author last
read, apart from the program blocks described below and the cuts that pay for
them.

Old 9.1's and old 9.2's openers (234 and 91 words) are deleted rather than
rehoused. They were previews of a topic order that no longer exists — "the first
is… the second asks… the third covers…" — which is the catalogue's own table of
contents. Their 325 words are the largest single payment toward the blocks.

### 2. Every section ends with the near-term work

One `\runin{The near-term work}` block per section, in a fixed order of four
moves: **the experiment** that could start now with means that exist, **the
falsifier** — the result that would show the approach is wrong — **the data or
access** it requires, and **the institutional condition** without which it cannot
run.

The hazard in a template repeated nine times is that it becomes a new catalogue
with better labels. What prevents it here is that the blocks are not all the same
shape, because the problems are not: **three entries have no near-term experiment
and say so** — the third of section 9.2's three questions, the aggregation half of
section 9.5, and section 9.9 entirely. One of those is the second-ranked problem
in the chapter. Section 9.3's experiment is real but narrow, and abandons most of
what the chapter asserts. Manufacturing an experiment for the three would be the
padding this chapter's own epistemic qualification exists to prevent.

### The governance prerequisites are one prerequisite

Gathering them exposed something the catalogue had hidden by listing them apart:
they are nearly all the same condition. External weight and API access that a
vendor cannot withdraw when results embarrass it (9.1); a guardian who is not the
operator (9.2); longitudinal access by someone the institution cannot fire, and a
body with standing to receive the finding (9.3); disclosure of held-out evaluation
results (9.4, 9.5); and, under all of them, an allocation of liability that
survives the fact that no single party controls the outcome (9.9).

Every one is a party outside the operator with access it can act on. That is
section 8.6.4's instrument and section 10.1.2's finding, arriving from a third
direction, and the opener now says so. **The research program's binding
constraint is not a research problem.**

## Word count

The instruction's constraint. Measured by `section_stats.py` over the chapter's
files, before and after, in `finishing/reports/section_stats.tsv`.

- **Before: 6,960 words** across 12 files (a chapter opener, two section openers,
  nine leaves).
- **After: 6,960 words** across 10 files (a chapter opener and nine sections).
  The same number, not approximately: the first draft of this pass came in at
  **8,554**, and the 1,594 words between those two figures came out over sixty
  separate edits, measured after each.

What paid for the program: the two deleted section openers (325); the six terminal
restatements the blocks replace (about 330); the chapter opener's gap list, which
kept its ranking and lost its per-entry descriptions and nearest-work notes,
because every one of those is stated in the section that owns it (about 300); and
compression across all ten files (about 440), none of which removed a citation, a
case, a named study, or a claim. The blocks themselves total 1,004 words, 112 to a
section.

**The page count went up, from 188 to 189.** Nine headings promoted from
`\subsection` to `\section` take more vertical space than the words they replaced
saved. The instruction's constraint was words, and words are down; the page is
recorded rather than passed over.

## Exit criteria

- Every section states its near-term work, or states that it has none and why.
- The order is stated with its criterion, and the criterion is checkable against
  the book's own text rather than asserted.
- `check_all.sh` green; every `\ref` resolves; clean build in both formats.
- The chapter's word count does not rise.
- Author's read.

## What this pass did not do

- **No claim was re-verified.** The chapter's citations are P4-, D-063- and
  D-069-era verified and were carried across unexamined. The program blocks make
  no new factual claim about the world: they name experiments, and where a block
  names an existing result it is one already cited in that section.
- **The near-term experiments are proposals, not literature findings.** Where a
  block says an experiment has not been run, that rests on the chapter opener's
  standing qualification — a search under a description, not a survey — and not on
  a fresh search.
- **Chapter 10's milestone material was not reconciled with the new order.**
  Section 10.2.2 points at 9.1, 9.4 and 9.5 for evaluation practice; those pointers
  resolve and were reread, but whether the conclusion should now cite the program
  as a program was not taken up.
- **The chapter was read in the built PDF only in part.** The opener, section 9.1
  entire, and the 9.1/9.2 seam were read as typeset; the other nine pages were not.
- **`xref_content.py` was not re-run**, so the semantic half of the cross-reference
  check has not seen this pass.

## One defect found on the way, and repaired

Section 9.6 ended by saying that single-system resilience against adversarial
manipulation "is chapter 10's territory, not this one's." It was, until eight days
ago: P30 moved section 10.3.3, *Resilience Against Deliberate State Compromise*,
into chapter 6 as 6.4.4. The reference still resolved — chapter 10 exists — and
pointed at a chapter that no longer holds the material, which is exactly the
failure class D-050 named and `check_xrefs.py` disclaims. P30's own record listed
"whether anything elsewhere refers to the moved material by description rather
than by number" as not checked; this is one such thing. Repointed to sections
6.2.2 and 9.1, which is where that material actually is.
