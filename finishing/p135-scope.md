# P135 — advance notice in §2.2.3 that the burden it sets is two kinds of claim

An author's note: §2.2 sets up the burden without the prior/precaution split, so
a reader reaching *every agent known to have something register as mattering is
an affective agent* has no signal that the book is about to distinguish a claim a
result could overturn from one no result reaches. Two or three sentences at the
end of §2.2.3, under *What this licenses and what it does not*, stating the split
in outline and pointing to §3.3. **The machinery stays where it is.**

## Where the split actually is

**`03_03.tex:83` is the statement**, and it is one sentence: *So the prior is
stated over routes and the precaution over patienthood: the first names what to
try next and a result can overturn it, and the second names how to treat whatever
the trying produces, on a question that will still be open when the decision has
to be made.* The paragraph then runs it both ways — the patienthood conclusion
cannot be held open for a result because the decision falls due first, and the
routing claim cannot be held as settled because a result is coming.

**`03_04.tex:62` is the restatement**, in Birch's terms rather than the book's:
under uncertainty the question is whether a system is a sentience candidate, and
the answer *governs what precautions are owed rather than waiting on a verdict
nobody can deliver*.

Both as the note describes them. The phrase *prior … over routes* and *precaution
over patienthood* occurs once in the manuscript; §3.4 carries the structure
without the vocabulary.

## What §2.2.3 already had, and what it was missing

The closing run-in already declines the strong reading — *That is not a proof
that non-affective moral agency is impossible* — and already points forward,
saying chapter~3 *takes that burden up again and reduces it*. **So the gap was
not the pointer and not the concession.** It was that both existing sentences
treat the burden as one thing with one fate, and chapter~3 splits it by what
could settle each half.

## What went in

One paragraph, three sentences, at the end of the run-in:

> That burden is not one claim, and which half of it a reader is holding changes
> what could settle it. One half is about which route to build first: evidence
> can overturn it, and section~\ref{sec:3.3} names the measurements that would.
> The other half is about what would be owed to whatever the building produces,
> and no measurement reaches it, because the decision falls due while the question
> is still open.

**Its own paragraph rather than appended**, because advance notice needs a beat
of its own and the preceding paragraph is already doing two jobs.

**No labels.** *The prior* and *the precaution* are terms of art by `03_03.tex:73`
and they are not introduced here. Naming two terms in chapter~2 whose definitions
arrive in chapter~3 is the name-dropped shape `style.md` §7 rules against; the
note asked for the kinds, and the kinds are what the paragraph states.

**Each clause checked against §3.3.** *Names the measurements that would* is
`:81` — the three marks, and holding them under sustained pressure against a
held-out set nobody in the building wrote. *No measurement reaches it* is `:83`'s
*the conjunct no instrument settles*. *The decision falls due* is `:83` verbatim
in its own words.

## Two defects in my own drafting, both caught before the suite ran

**The paragraph opened on `Chapter~\ref{sec:3}`, which is how the paragraph
immediately above it opens.** Rewritten to *That burden is not one claim*. The
repair also removed a cross-reference the draft did not need, so the pass adds
one rather than two.

**The third sentence shared a six-word run with `03_02.tex:24`** — *about what is
owed to whatever*, against the author's own *what is owed to whatever meets it*.
Reworded to *what would be owed to*, which clears the run and is the more
accurate tense for a thing not yet built.

## The cross-reference

**231 → 232.** The second added in three passes, after none in the four before
them. It was named in the instruction, it is the one place the split is stated,
and the sentence carrying it makes its claim before the reference arrives.
**Recorded here because the count is now moving in a direction D-089 and D-099
set against, and a session reading the count alone should find the reasons
attached.**

## Found while checking, filed rather than repaired

**`02_02_03.tex:27` and `03_04.tex:38` share a six-word run** — *is an affective
agent and no* — inside the same argument shape stated twice: *every agent known
to have something register as mattering* against *every agent known to hold
another's welfare as a reason against its own interest*. **The predicates
differ**, so this is two applications rather than one claim written twice, and
**neither sentence was written by this pass**. Q-103, following Q-093's practice
of recording a duplication found in text the pass did not write.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
the paragraph read back out of `pdftotext` with the reference printing as
*section 3.3*. New text checked at 6, 7 and 8 words against every line of the
other 132 sections: **0 shared runs** after the `03_02.tex` repair.

## Figures

133 sections, **1 changed**. 99,134 → **99,205** words (+71); §2.2.3 1,013 →
1,084. **196 pages unchanged.** 231 → **232** cross-references. 324 bibliography
entries unchanged. 0 `\textit`. **The proof pair was not rebuilt and is now three
passes stale.**
