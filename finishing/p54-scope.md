# P54 — four defects in the glossary and the sourcing (D-119)

**Author's findings**, supplied as a list of four. Each was checked against the
manuscript before anything was changed. Three were confirmed exactly as stated. The
third was confirmed and is larger than the finding said: the annotation was missing,
and the figure it would have annotated is misdescribed in the prose.

## 1. "Floor" was misalphabetized

Confirmed. The entry sat between "Explainability and transparency" and "Federated
learning." Sorting the whole list found **it was the only entry out of order in 56**,
which is why it reads as a slip rather than a convention. Moved to between "Few-shot
learning" and "GPT-3 and GPT-4" and the list re-checked end to end: nothing else moves.

## 2. *Exit* and *molar/molecular fascism* had no entries

Confirmed, and stronger than "no entry" — the strings `exit`, `molar` and `molecular`
appear **nowhere in chapter 13 at all**. Both meet the bar the glossary sets for itself
in its own opening note, which says several entries are the book's own working
definitions rather than dictionary ones.

**Exit** is the book's narrowing of Hirschman, defined at section 3.7 in a sentence
beginning "Call that exit" — refusal turned on the arrangement rather than on a task.
The entry carries the definition, the Hirschman lineage with the book's own gloss
(voice is the refusal stated, exit is the work withheld, loyalty is the one to fear),
the disclaimer that it does not mean escape, and the claim it exists to support: a
floor whose bearer cannot leave will not hold, and a bearer that can leave can leave
wrong.

**Molar and molecular fascism** is a borrowing from Deleuze and Guattari that
section 2.1.2 leans on hard and that chapter 7 and section 11.3 both turn on. The entry
carries the distinction, the reason the book needs it (an AI deployment has only the
molecular scale, so a definition pitched at the state certifies it healthy), the
position the book actually takes — the molecular case is the thing itself and not an
early warning — and **the five molecular discriminators listed out**, which existed
nowhere in the glossary despite being what chapter 7's whole argument is run against.
The unsolved case is stated: telling a recuperated dissent mechanism from a merely
mediocre one when both produce the same paperwork.

Both entries were written to the house style — one paragraph, the book's usage rather
than a dictionary's, section locators in parentheses at the end, and the named theorist
in prose without an `\autocite`, which is what every comparable entry does.

**These locators are not against D-118.** P53 ruled the glossary out of scope on the
ground that a locator in a glossary entry is the entry doing its job. The three new
`\ref` calls are all inside chapter 13; the body count is untouched at 476.

## 3. The Gordon et al. 14 percent figure

The finding was that the figure is load-bearing and its bibliography entry carries no
verification annotation. **Both halves confirmed, and a third thing found.**

- The citation `gordon2022jury` is used twice, at sections 7.2 and 7.3. **The 14 percent
  figure itself appears once**, at 7.2. Recorded because the finding said the figure was
  used twice; it is the citation that is.
- The entry had no `note` field. **200 of the 305 entries in `refs.bib` have one**, so
  this is a gap in a convention rather than the absence of one.
- **The prose misdescribed the figure.** It read "changed the classification outcome for
  14 percent of *contested cases*." The paper's denominator is all items, not contested
  ones: the abstract says juries "alter 14% of classification outcomes" and section 1
  says the composition "changed the algorithm's classifications on 14% of items."

Verified against the paper itself — the arXiv listing carries no version of the figure,
the ACM page refuses automated fetches, so the authors' own copy was used and the text
extracted locally. The field evaluation is **18 moderators of online communities** on a
comment toxicity classification task, and the juries they authored carried 2.9 times the
representation of non-White jurors and 31.5 times that of non-binary jurors relative to
the jury implied by the dataset.

The prose now reads "letting eighteen community moderators build their own juries changed
the classification outcome on 14 percent of items." The sample size is stated because the
book leans on the number and eighteen is small. The `note` field records the setup, both
figures, the denominator explicitly, and the date and route of verification.

## 4. The Dweck definition appeared twice

Confirmed and measured: sections 1.3 and 5.1.1 shared a **30-word verbatim run** —
"distinction between a fixed mindset, which treats ability as static, and a growth
mindset, which treats it as built through effort and experience, matters" — and then
both closed on the same errors-as-data against defends-prior-outputs contrast. A third
statement in the glossary is legitimate and was left alone; restating is what a glossary
does.

Also found, and not in the finding: **section 1.3 carried the definition with no
citation at all.** The `\autocite{dweck2006mindset}` is at 5.1.1 only.

**The author ruled which site survives** rather than having it chosen for him, because
the two are not interchangeable: 5.1.1 has the citation and the tie to section 3.8's
standard for a floor holding, while 1.3 is a preview whose two sibling run-in heads
carry no names and no pointers. **His ruling: compress 1.3, keep 5.1.1 whole, keep
Dweck's name in both, add no cross-reference.** Section 1.3 now opens on the design
claim and compresses the attribution to a short appositive. The longest run the two
sections share is down to three words.

## Numbers

| | before | after |
|---|---|---|
| Words | 93,740 | 94,065 |
| Glossary entries | 56 | 58 |
| Entries out of alphabetical order | 1 | 0 |
| `\ref{sec:}` calls, glossary | 120 | 123 |
| `\ref{sec:}` calls, body | 476 | 476 |
| `refs.bib` entries with a `note` | 200 | 201 |
| Pages | 191 | 191 |

Four files changed: `ch01/01_03.tex` (−12 words), `ch07/07_02.tex` (+2),
`ch13/13.tex` (+333), and `finishing/refs.bib`. Section 5.1.1 is untouched.
`check_all.sh` green; PDF rebuilt at 191 pages with 0 undefined references, and the
three moved or added glossary entries were read in the rendered page rather than only
built.

## What was not done, and one thing found on the way

- **The 70 sections P53 changed have still not been read end to end**, and this pass
  did not read them. It touched four files.
- **No other bibliography entry was audited for a missing annotation.** 104 of 305
  entries have no `note`. Whether any of the others is load-bearing in the way the
  Gordon figure is has not been checked, and the finding does not generalize on its own.
- **The other 121 glossary entries were not checked against the sections they define.**
  Alphabetical order was verified for all 58; content was verified only for the two
  written here.
- **A page-proof defect, found while reading the rendered glossary and not repaired:**
  the running head over the glossary pages says "CHAPTER 12. CONCLUSION AND OUTLOOK."
  Chapter 13 is set with `\chapter*`, which does not set the running mark, so the
  glossary inherits the previous chapter's. It is a preamble fix, outside these four
  findings, and is filed as Q-055 rather than taken here.
