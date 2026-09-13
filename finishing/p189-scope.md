# P189 — the Foreword corrected, and §3.8's disclaimer dropped as redundant

Author instructions, two, given in sequence during a session that began as an
orientation pass: **fix *Foreward* for *Foreword***, and then, on the finding
below, **drop §3.8's sentence *Neither chapter assumes that durability proves
concern or that formation removes the custodian* and do nothing else.**

The second instruction came out of a question the author asked about P188's
finding that the book had reversed its position on the developmental material.
That finding is wrong in the way it is written, and this pass says so and
rewrites it rather than acting on it.

## The misspelling

*Foreward* was corrected once already, at D-257 (P157), and came back with the
September 12 Overleaf return. P187 recorded it and did not fix it; P188 listed
it under the title-register reversal, also unfixed. It is fixed here.

Four live sites carried it — `ch00/00.tex` three times (`\chapter*`,
`\addcontentsline`, `\backmattermark`), plus `ORDER.tsv`, `outline.tsv` and
`ledger.tsv`. `table-of-contents.txt` regenerated with `headings.py --write-toc`,
the ORDER sha refreshed, `section_stats.tsv` rerun.

**Chapter 0's body prose already spelled it correctly** — *My first draft of this
foreword* — so the misspelling was only ever in the title.

**Not changed: the five places in the record that quote the misspelling**
(`p157-scope.md`, `p187-scope.md`, `p188-scope.md`, `STATE.md`, `DECISIONS.md`).
They document it, and correcting a quotation would destroy the thing being
documented.

**The committed proof pair still reads *Foreward*** in its HTML table of contents
and heading. That clears at the next proof rebuild and not before; nothing in
this pass touched `finishing/reports/`.

## What P188's finding got wrong

P188 recorded: *"The book reversed its position on the developmental material
without saying so. Old §3.10 held that the growth mindset and the developmental
sequence 'turn out to be the material the floor is made of.' The new §5.1 treats
the distinction as a taxonomy only."*

**The comparison is between two different sites making two different claims.**
Old §3.10's successor is **§3.8** — a subject move recorded at D-288, where
`03_08.tex` kept its filename and took old §3.10's ledger row. §5.1 is not its
successor and never was.

**Old §3.10's claim was already conditional in its own section.** It asserted the
identification at its line 17 and then, in the *suppose the induction fails*
budget at line 43, listed *"the claim that the learned half is the material the
floor is made of"* among the things that go. That budget is D-144 (P63), which
records the same three items coming off if the induction fails.

**§3.8 did not reverse it. It went agnostic**, in prose that arrived with the
author's own Overleaf edit at `3402bec` and that P187 applied without reading:
chapters 4 and 5 *"inherit the two unresolved parts of that design,"* each posed
as a question rather than an answer.

**§5.1's *taxonomy only* is a narrower claim about the Piaget/Kohlberg stage
distinction**, which the book has declined as a mechanism since D-037's box —
*the stages are an order, not a mechanism* — and which is not what old §3.10 was
asserting.

**What P188 did do, two commits before writing the finding, was cut the
manuscript's one explicit agnostic marker.** At `404fc4c` it removed §5.1's
closing sentence: *"Nothing here requires a developmental sequence, treats
principled reasoning as a stage of maturity, or assumes that producing a
principled explanation predicts principled conduct."* Its stated reason — residue
of old §5.1.1, and a restatement of the *only* in the sentence before it — covers
the second clause and not the first, and the third is made at §5.3 and §5.5,
which P188's own scope file says.

## The sentence dropped, and why it goes cleanly

The author declined the restoration and asked for the parallel deletion instead.
**The book is now agnostic by not making the claim rather than by disclaiming
it**, consistently at both sites.

Both halves of the dropped sentence are made downstream, at the sections that
argue them rather than at the handoff that announces them:

| Clause | Where the book already makes it |
|---|---|
| *formation removes the custodian* | `04_02.tex:18`, near-verbatim — "Inferring the objective rather than specifying it does not remove the custodian." Also `04_03.tex:18`, "The custodian has not disappeared," and chapter 4's opener, "each with a custody failure still attached" |
| *durability proves concern* | `04_02.tex:40–42`, which names "durability across revision points" as the first criterion and then says "These criteria do not prove formation." Also §5.1, "deliberately weaker than proof of concern or consciousness" |

**The redundancy is tighter than a file listing shows.** §3.8 is the last section
of chapter 3, so chapter 4's opener — which re-makes the custody half — is the
next thing a reader meets, about two hundred words later.

**The two questions already carry the caveat inside them.** Chapter 4's is posed
as how a concern could become durable *"without remaining wholly at the disposal
of its trainer"*; chapter 5's as what evidence could distinguish formation *"from
a policy trained to produce the same conduct."*

**Nothing inbound rests on it.** The two references to `sec:3.8` are
`12_02_01.tex:13` and the glossary at `13.tex:38`, and neither cites that
paragraph.

**The silence is complete, which is the condition on agnostic-by-silence being
the stronger form.** `piaget1932moral` and `kohlberg1969stage` are cited **once
in the book**, at §5.1, explicitly as a taxonomy. *Developmental* now appears
once in the manuscript, at `11_06.tex:5`, about false-belief tests and unrelated.
There is no surviving commitment to a stage theory for the silence to sit
against, so no sentence is needed to disown one.

## What this pass leaves standing

- **The developmental-sequence disclaimer is not restored** and its point is now
  made nowhere. That is the author's instruction and the finding above is why it
  costs nothing: nothing in the book requires the disclaimer.
- **`STATE.md`'s reversal finding is rewritten, not deleted.** Left as written it
  reads as an outstanding defect, and the next pass would have repaired something
  that is not broken.
- **The three other P188 findings stand untouched**: the two `style.md` §1
  sentences still gone, the title register still mixed, global inequality still
  absent with nothing left behind.
- **`c8b1a97`, `c0b24bd` and `0fcf381` still have no row, lead or scope file.**
  This pass does not author rows for work it did not do.

## What was not checked

The prose of chapters 3, 4 and 5 was **not** read as prose; the reading here was
confined to the sentence dropped and to the passages that make its two claims
elsewhere. No citation was verified against its source. No report tool was rerun
beyond `section_stats.py`. `QUESTIONS.md`'s forty-one open items have now gone a
**third** pass unchecked against the post-return structure.

## The record

90 sections, **66,894 → 66,881 words**, **142 pages** (built and counted, not
carried forward), 234 cross-references, 212 bibliography entries all cited, zero
undefined references and citations. Suite green. `ledger.tsv` carries D-290 on
the two rows this pass touched, 0 and 3.8.
