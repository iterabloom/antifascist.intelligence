# P207 — §6.4's six worked examples cut to two sentences

The author's finding, given whole: *§6.3's six forms of authoritarian misuse
exists in order to be set aside. The section says so: each is recognizable as
misuse from outside, and the case this chapter takes up is the one that isn't.
Six worked examples is a lot of words to spend clearing the table. Two sentences
and the glossary entry carry it.* **Executed.** The book is **88 sections, 73,749
words and 154 pages**, suite green, 0 undefined references and 0 undefined
citations.

## The number in the finding is this morning's

**§6.3 is §6.4.** D-302 moved §2.2.1 into chapter~6 as §6.1 and displaced
everything below it downward; `renumber-map_2026-09-13b.tsv` records 6.3→6.4.
The section meant is unmistakable — *Same Robot, Worse Boss* held the enumerate
and the exact line the finding quotes, and the current §6.3, *Who Is Allowed to
Look*, is the Ofqual case and has no taxonomy in it.

**This is the hazard `QUESTIONS.md`'s header names**, arriving from the author
rather than from a record file. Two renumber maps are a day old. **A pass taking
author text in should check a section number against the map before acting on
it**, and should say so when the number moved rather than silently doing the
right section.

## What was cut and what replaced it

**The enumerate, 372 words.** Six items, each a form plus a worked case: China's
social-credit patchwork, the Xinjiang platform, Cambridge Analytica, the Great
Firewall's classifiers, the Slovak deepfake two days before the 2023 election,
and Moscow's camera network after the January 2021 Navalny protests. §6.4 goes
**525 → 153 words**.

What replaces it is two sentences. The first names the same six **in the
glossary's own words**, so the two agree term for term:

> Authoritarian misuse of AI is not one problem but several — algorithmic social
> scoring, mass biometric surveillance, psychographic micro-targeting, automated
> censorship, synthetic disinformation, and repurposed dual-use systems — each
> needing a different countermeasure, and each recognizable as misuse from
> outside \autocite{…}. The case this chapter takes up is the one that is not.

**The second sentence is the author's own, verbatim.** *Each needs a different
countermeasure* and *each is recognizable as misuse from outside* are the old
follow-up paragraph, folded into the naming sentence so the closing line keeps
its position and its punch.

## The glossary needed no edit

The entry *Authoritarian misuse, six forms* already lists all six and closes with
`(§\ref{sec:6.4})`. **§6.4 still names all six**, so the pointer resolves to a
section that uses the term rather than to one that has forgotten it — which is
the distinction that matters, and the reason no glossary change was needed.

**The glossary was the only thing in the book pointing at §6.4.** One `\ref`
across 88 sections, and it is the one the author named. Nothing else depended on
the enumerate.

## The six citations were kept, and why

`drinhausen2021chinas`, `humanrightswatch2019chinas`, `cadwalladr2018revealed`,
`hoang2021great`, `denadal2024beyond`, `hrw2021russia` — **each cited nowhere else
in the book.** Cutting the worked cases would have orphaned all six. They are
bundled onto the naming sentence instead.

**This is a judgment call and it is not what the instruction said.** The
instruction said two sentences and the glossary; it said nothing about sourcing.
Three things decided it:

**These are the same six entries that round-tripped once already.** The
2026-09-12 Overleaf cut removed this taxonomy and orphaned them; P187 moved them
to `unused_bibliography.bib`; a later pass restored both the taxonomy and the
entries, on the finding that **the glossary had gone on defining something the
book no longer contained.** That failure mode is not repeated here — the six
forms are still named in the section — but the entries would have moved out and
back a second time inside two days.

**The sources are what carry *documented*.** The sentence asserts these forms are
real and distinguishable. Without them the book names a six-part taxonomy of its
own devising and cites nothing for it.

**There was no third place to put them.** The glossary takes no citations — zero
`\autocite` across the whole chapter — so the sourcing lives in §6.4 or nowhere.

**The cost is visible and worth stating**: the bundle prints as a parenthetical of
about thirty words, *(Drinhausen and Brussee 2021; Human Rights Watch 2019;
Cadwalladr and Graham-Harrison 2018; Hoang et al. 2021; De Nadal and Jančárik
2024; Human Rights Watch 2021)*, against 372 words cut. **If the author would
rather the sentence carried no citation, the six entries move to
`unused_bibliography.bib` and the change is one line.**

## A tool defect found on the way, recorded and not repaired

`check_typography.py` prints on success:

> typography OK: no straight quotes, no ASCII dashes, no TeX quote notation

**It does not test the manuscript for TeX quote notation.** The `` `` `` and
`` '' `` rules are in `BIB_RULES`, which is applied to `refs.bib` only; the
sections are checked against `RULES`, which holds the straight double quote and
the two ASCII dash runs and nothing else. **Three pairs sit in the sections
undetected**: `06_04.tex:11` (``in the loop,''), `09_01.tex`, `10_03.tex`.

**They set correctly** — LaTeX renders `` `` '' `` as “ ”, and the printed page shows
“in the loop,” — so this is source consistency against D-082's convention rather
than a rendering fault. **What is wrong is the success line**, which claims more
than the run tested. Two repairs are available and neither was made here: move
the two rules into `RULES`, or narrow the message. **Not done because the first
would fail the suite on three pre-existing instances of the author's own prose**,
which is a ruling and not a typo fix.

## Files touched

| File | Change |
|---|---|
| `manuscript/sections/ch06/06_04.tex` | enumerate and its two framing paragraphs replaced by two sentences |
| `manuscript/sections/ORDER.tsv` | one sha256 refreshed |
| `finishing/DECISIONS.md`, `finishing/STATE.md`, `finishing/PLAN.md` | D-309, new lead, header figures |

No section was added or removed, so `sections.tex`, the contents, `outline.tsv`
and `ledger.tsv` are unchanged at 88 rows.

## Measured after

88 sections, 73,749 words, 154 pages, 258 cross-references against 88 labels, 222
bibliography entries all cited, 0 undefined references and 0 undefined citations.
Suite green. Chapter~6 is 7 sections and 5,040 words; §6.4 is 153 of them.

**The committed proof pair is stale by three pages** — 157 against the book's 154,
and `README.md` still says 157. Not rebuilt this pass.
