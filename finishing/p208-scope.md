# P208 — §3.8's recap cut, the induction-failure passage surfaced

The author's finding, given whole: *§3.8 summarizes chapter~3 for someone who
just finished chapter~3, and chapter~12 summarizes it again. The genuinely new
material is the “suppose the induction fails” passage, which is excellent and
currently buried under recap.* **Executed.** The book is **88 sections, 73,494
words and 153 pages**, suite green, 0 undefined references and 0 undefined
citations.

§3.8 goes **1,151 → 896 words**. Sixteen body paragraphs become thirteen, plus a
run-in head.

## What went, and where each already lived

| Cut | Words | Its other home |
|---|---|---|
| §3.2's three marks, restated | 13 | `03_02.tex:35`, `03_03.tex:3`, `12_02_01.tex:11` |
| §3.1's four ways, recapped whole | 91 | §3.1, whose title is the phrase |
| The try-the-alternatives-first rule | 22 | `12_02_01.tex:6` **and** `12_03.tex:7` |
| §3.5's custody argument | 75 | §3.5; `12_03.tex:7` makes it again |
| §3.6's worked deployment | 67 | §3.6 |

**The chapter~12 half of the finding checks out.** The try-the-alternatives-first
rule is stated in §12.2.1 *and* §12.3, so §3.8 was its third site. §12.3 also
restates the custody argument, and §12.2.1 restates the three marks. **§12.1 is
not a chapter~3 recap** — it is the capability-approach argument — so the
duplication is with §12.2.1 and §12.3 specifically.

## The paragraph that was nearly cut whole

`03_08.tex:7` reads, in full before the edit:

> Holding does not mean that the floor is never crossed. A floor holds when a
> violation is legible in terms the bearer accepts as reasons, registers as a
> violation, and changes what happens next. The behavioral specification is
> reasons-responsive refusal: novel pressure, correct defeat, and priced cost.

It reads as recap and two thirds of it is not. **The second sentence is the
book's only statement of what it is for a floor to hold** — the phrases *holds
when*, *legible in terms* and *registers as a violation* return this one line and
nothing else across 88 sections. **It is P51's repair**: P50 found that the
book's only operational definition of *holding* sat in what was then §5.1.1 and
that chapter~3 never cited it, and P51 moved the definition into chapter~3. This
is where it landed.

**Only the third sentence went.** The three marks are §3.2's, named there as
*the chapter's test for meaningful refusal*, restated at §3.3's opening and again
in §12.2.1.

**The general point is worth carrying.** A closing section is where a book puts
the one sentence it wants a reader to leave with, and that sentence looks exactly
like recap from the outside. **Check whether a summary paragraph is the only site
of what it states before cutting it.**

## Two paragraphs that look like recap and are anchors

Both are cited from outside the section, for content the cut would have removed.

**`03_08.tex:5`** — *What remains is a commitment that the owner cannot revise or
circumvent unilaterally without cost and record, held by something that could in
principle abandon the commitment itself.* The glossary's **Floor** entry closes:
*what survives is a commitment the owner cannot take out of the system, held by a
bearer that could in principle abandon it (§3.1, §3.8).* Near-verbatim. It is
also the redefinition the section's title promises.

**`03_08.tex:9`** — the threat model's two questions, *can the commitment be
edited or routed around?* and *will the commitment continue to hold?*
`12_02_01.tex:13` reads: *a refusal that survives an attack has passed a
tamper-resistance test, which answers section~3.8's other question and leaves
this one open.* **The phrase *other question* has no referent without this
paragraph.**

Cutting either would have left a cross-reference that resolves while naming a
claim its target no longer makes — **Q-041's class**, and the failure D-050
describes.

**An accident of the cut order is worth noting**: `03_08.tex:9` opens *The threat
model therefore has two questions*, and with the four-ways paragraph gone the
*therefore* now follows `03_08.tex:5` directly, whose two halves are exactly the
two questions. The transition is better after the cut than before it.

## One defect created and repaired in the same pass

The publication paragraph opened:

> Publication makes those commitments and interception positions testable…

**Both antecedents were in paragraphs cut above it** — the commitments in §3.5's
custody recap, the interception positions in §3.6's worked-deployment recap. Left
alone it would have been a bare demonstrative with nothing to bind to, which is
`deixis.py`'s class. It now reads *the floor's commitments and the positions where
a refusal can be intercepted*.

## The run-in head is this pass's addition

`\runin{The chapter without its central inference}`, placed before *Suppose the
induction fails.*

**This is not in the instruction.** The instruction was that the passage is buried
under recap, and removing the recap is the fix it names; the head is a second,
additive fix and **should be struck if the subtraction was meant to do the work
alone.**

Three things argue for it. **§3.8 was the only section in chapter~3 with no
run-in heads** — §3.2 carries four at 1,227 words, §3.4 four at 1,309, §3.3 five,
§3.6 four, §3.7 four. **Eighteen sections below §4a's 1,500-word threshold carry
them**, so the length is no objection. And the head is on the register of the
chapter's others — §3.3's *What would change the engineering conclusion*, §3.6's
*What the exercise exposes* — declarative rather than imperative, and it does not
echo the paragraph's own first sentence.

## Three paragraphs kept that are not recap

Named here so a later pass does not read them as work this one missed.

**The legitimacy paragraph is chapter~3's only pointer to the authority
question.** *Publication… does not make them legitimate. A bearer refusing on
behalf of people who did not choose it exercises power over them.* Checked: no
file in chapter~3 contains *legitimacy*, *authority to define*, or any `\ref`
into chapter~9. Cut it and the chapter hands off to chapters~4 and~5 and to
nothing else.

**The recuperation paragraph is a new move, not a summary.** It turns chapter~7's
definition of recuperation on the book's own central proposal — *the bearer
occupies the post of exception-filer, so being the exception is the job* — and
says so: *Chapter~7 runs this definition on the provenance of these systems and
on this book. Here it runs on the book's own central proposal.*

**The chapter~4/5 handoff is structural**, stating what each of the next two
chapters inherits.

## One small loss, recorded and not repaired

*Custody survives, for the reason each of the four ways failed on* had a local
gloss in the cut four-ways paragraph. Its antecedent is now §3.1's title,
*Four Ways to Build One, and What Each Costs*, and that section's opening
sentence, *A floor can live in four places.* **The phrase *four ways* appears in
the chapter's body only here.**

Left as it stands: the reader reaches this line minutes after that heading, and
the alternative is a cross-reference in a book that has cut them from 848 to 258.

## Files touched

| File | Change |
|---|---|
| `manuscript/sections/ch03/03_08.tex` | four recaps and one sentence cut; one demonstrative repaired; one run-in head added |
| `manuscript/sections/ORDER.tsv` | one sha256 refreshed |
| `finishing/DECISIONS.md`, `finishing/STATE.md`, `finishing/PLAN.md` | D-310, new lead, header figures |

No section added or removed, so `sections.tex`, the contents, `outline.tsv` and
`ledger.tsv` are unchanged at 88 rows.

## Measured after

88 sections, 73,494 words, 153 pages, 258 cross-references against 88 labels, 222
bibliography entries all cited, 0 undefined references and 0 undefined citations.
Suite green. Chapter~3 is 9 sections and 12,876 words; §3.8 is 896 of them.

**The committed proof pair is stale by four pages** — 157 against the book's 153,
and `README.md` still says 157. Not rebuilt this pass.
