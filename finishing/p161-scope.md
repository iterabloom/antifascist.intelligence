# P161 — twenty-three titles retitled, and the register changed with them

Two author instructions in sequence. First: *Foreword → Sup*, and chapter~6's
*Overcoming Challenges, Risks, and Authoritarianism in AI Development → Deterring
Haters and Other Wack Elements in AI Development*, **retitled again before the pass
closed to *Neutralizing and Preventing Fascism in AI Development***. Then twenty-one more, named by
number, with the instruction that the current titles are **really boring** and want
pizzazz.

**No prose changed.** Twenty-three headings, and the four files that copy a title.

## The register was asked before it was applied

Three registers were put to the author with drafted samples: the book's own
argumentative style, an irreverent one, and a mixed proposal keeping sections
plain. **He chose irreverent throughout**, so the twenty-one are written in the
register of *Sup* and *Deterring Haters* rather than the register of chapter~3.

The question was asked because twenty-one titles is a large share of the book's
surface and the two registers produce different books. It was asked **after** all
twenty-one sections had been read, so the samples were accurate rather than
generic.

## What went in

| | |
|---|---|
| 1 | Why You're Going to Hate This |
| 2 | Yes, It Has to Have Feelings |
| 2.1 | Six Theories, None of Which Will Save You |
| 2.2 | Going Numb Won't Make You Fair |
| 4 | Where the Caring Gets Built |
| 4.1 | You Can't Hold a Line You Didn't Notice |
| 4.2 | The Assembly Line for a Conscience |
| 5.4 | Nobody Raises a Machine Alone |
| 6.1 | Garbage In, Bigotry Out |
| 6.2 | Holding Up When the World Moves On |
| 6.3 | It Was Supposed to Help |
| 6.4 | Same Robot, Worse Boss |
| 8.1 | Everybody Knows a Different Piece |
| 8.2 | Ask the People It Happens To |
| 10.5 | Built for the Rich Parts of the World |
| 10.6 | Democracy Is Not a Force Field |
| 11 | Everything I Couldn't Figure Out, Ranked |
| 12 | What I Actually Think Happens Now |
| 12.1 | Better, Not Just Less Bad |
| 12.2 | How You'd Know It Was Working |
| 12.3 | The One That Gets You Anyway |

Each was written off the section's own opening rather than off the old title. Three
drafts were changed for repetition before anything was applied: *Nobody* had opened
three of them and now opens one, and *X Is Not Y* had been the shape of two.

## One edit the instruction did not name

`00.tex:15` read *The initial draft of this Foreword was all about…* — the piece
naming itself. ***This Sup* does not parse**, so the word is now lowercase and
generic: *the initial draft of this foreword*. The piece is a foreword; *Sup* is its
title.

## What was checked before the swap

**No title is quoted in the prose.** All twenty-three current titles were counted
across every section file, discounting the heading line itself; the total was zero,
so no sentence needed repair. Chapter~6's old title survives in
`manuscript/previous/`, which is provenance and untouched.

## One record defect found on the way

`ledger.tsv`'s row for chapter~2 carried **`Foundations of Compassion and Empathy in
Friendly AI`**, a generation-era title, so the ledger had been stale since whatever
pass renamed chapter~2 to *Ethics, Affect, and Machine Subjects*. **All 133 rows
were compared against `ORDER.tsv` and it was the only one.** Now synced.
`check_structure.py` does not compare ledger titles, only row parity, which is why
nothing had caught it.

## What the change makes visible

The contents now carry two registers on one page: chapter~2's new titles sit
directly above chapter~3's, which are argumentative and were left alone. **By the
same test that flagged the twenty-one, seventeen titles remain in the
generation-era register** — 2.3, 4.3, 5.2.3, 5.3.3, 5.4.2, 5.6, 5.6.2, 5.7, 6.1.1,
6.1.2, 6.3.2, 6.4.3, 8.3.1, 9.1.3, 9.1.4, 9.2 and 2.2.2 — and they read flatter
beside the new ones than they did beside the old. Not filed as a question, because
the author is working through this list by hand and naming the numbers himself.

## One flag changed a title

Chapter~6's opening page set *Deterring Haters and Other Wack Elements in AI
Development* directly above its epigraph, which is a pseudonymous Israeli
signals-intelligence commander on being unable to produce enough targets per day,
with §6.4.1's Gaza box nine pages later. **Reported as a fact about the rendered
page, not as an objection**; the author had not seen it and cannot from a title
list.

**He read it and retitled the chapter *Neutralizing and Preventing Fascism in AI Development*.** That is the
book's own vocabulary rather than a retreat to the old title — §2.1.2 defines the
structural signature the word names, and the chapter is where the book applies it.

**Chapter~6 therefore ends the pass outside the register the other twenty-two are
in.** That is a deliberate exception, recorded here so a later pass reads it as one
rather than as a title somebody forgot.

## Figures

133 sections, **23 headings changed, 0 words of prose**. 99,458 words unchanged.
**194 pages unchanged.** 228 cross-references and 324 bibliography entries
unchanged. 0 undefined references and citations. Suite green.

**The committed proof pair is one pass stale** and shows the old titles.
