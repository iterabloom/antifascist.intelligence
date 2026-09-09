# P134 — the two failure directions paired before the epigram, and the detector concession moved to where it can be earned

An author's note on §2.1.2's reflexive-cost paragraph, in two parts: restructure
so both failure directions arrive before the reflexive line, and **consider**
whether the *not yet a "fascism detector"* sentence belongs in that run rather
than several paragraphs earlier.

Both executed. The second was offered as a judgment call and the reason for
taking it turned out to be stronger than the reason given.

## The restructure

The paragraph ran: accusation → epigram → false assurance → *Better engineering
fixes neither* → specification constraint. **The epigram sat between the two
failure directions**, so the second direction arrived after the line that reads
as a verdict, and a reader who stopped at the quotable sentence stopped one
failure short.

It now runs: both directions, then *Better engineering fixes neither*, then the
constraint, then the reflexive line last.

Two things changed inside that beyond the reordering.

**The second direction is split into two sentences.** It was one 30-word
sentence hinged on *since*; it is now *The opposite failure is no safer.* and
then the mechanism. The paragraph's diagnosed fault is compression, and the
repair for compression is not only order.

**One wording change the note did not ask for.** *Both are governed by what the
tool may output and to whom, which **makes them** a constraint the specification
has to carry* → *which **is** a constraint*. The original made the two failures
the constraint; what the specification carries is the rule about output and
audience. The note's own gloss — *a constraint the specification has to carry* —
reads the same way.

**The epigram is verbatim.** It is the author's line from P132 and the note
treats it as the fixed element being repositioned.

## The move, and the argument that decided it

*None of this is yet a "fascism detector". Some of it names things that are
observable in principle, but "concentrated, unaccountable power" is not one of
those things.* It closed the *What makes it fascism and not authoritarianism in
general* run-in, immediately after Griffin. It now opens the detector run, ahead
of *That a detector of the four features would find something nearly everywhere
is expected.*

The note's reason — the reader has the material to see why — holds: at the old
position the reader had the four features and Griffin's minimum but not the five
molecular restatements, and it is the five that make the concession concrete,
`:47` already saying they are *harder to observe, since each requires knowing
what was rewarded rather than what was written*.

**The stronger reason is a loop the section opens and did not close.** Line 5
poses the problem in the same words — *Opposing "concentrated, unaccountable
power" gives an engineer nothing to build. It does not say what a system would
detect, what would count as a false positive, or how anyone would know the
system was wrong* — and ends *So, first, the definition.* The moved sentence is
the report on that promise, and **it can only be delivered once the definition
has actually been given**. At its old position the definition was half done. The
phrase appears exactly twice in the section, once at each end of that loop.

**What the old position was doing, and why losing it is affordable.** It stopped
a reader from thinking the four features had been offered as a detector. The
seam it leaves is clean: `:30` now ends on *the discipline's own answer to what
is fascism rules out in advance the scale this book works at*, and the next
run-in opens *Put the two halves of this section together and they do not fit*,
which is the sentence that answers it.

## Found while restructuring, filed rather than repaired

**Two consecutive paragraphs now open on the same premise.** `:51` is *That a
detector of the four features would find something nearly everywhere is
expected*; `:53` is *A tool reporting the four features will have something to
report nearly everywhere*. Same observation, two different consequences — the
first answers the base-rate objection with slope-not-level, the second uses
ubiquity as the premise for the misuse argument — but the second restates the
premise rather than carrying it forward. **Q-102**, with the eight-word repair
named in it.

Not repaired here, for one reason: the note enumerates the paragraph's elements
and keeps the accusation as element 1, and that clause is where the restatement
sits. **P132's finding was one-directional editing inside a compression pass**,
and rewriting an element the instruction preserved is the same move in the other
direction. It costs a sentence from the author to settle.

**The suite cannot see this class** — the two openings share *nearly everywhere*
and nothing at six words, so no run check reaches it. It was found by reading.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations.**
Paragraph order read back out of `pdftotext` at the moved sentence and at the
restructured paragraph. The restructured sentences checked at 6, 7 and 8 words
against every line of the other 132 sections: **0 shared runs.**

## Figures

133 sections, **1 changed**. 99,136 → **99,134** words (−2); §2.1.2 2,633 →
2,631. **196 pages unchanged.** 231 cross-references unchanged — the move
carried none and the restructure added none. 324 bibliography entries unchanged.
0 `\textit`. **The proof pair was not rebuilt and is now two passes stale.**
