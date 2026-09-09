# P133 — the theorem promoted, and the detector limit given its own sentence and a forward flag

An author's note on §2.1.2's four-feature list, in two parts: promote the Zhuang
and Hadfield-Menell theorem inside feature 2, and move feature 4's qualification
out of its trailing position, with a forward flag to §11.3 to consider.

**Both substantive claims hold. Two of the descriptions do not, and in the same
direction: the repair each part asks for is smaller than the note states,
because in both cases the sentence the note asks for already exists.** What is
wrong in both is position — the payload is the tail of a long run.

## The two claims, checked

**"The only formal support any of the four features has."** Holds. Item 1 cites
Debord, who is warning that denunciation of the spectacle can become a hollow
formula — an observation, not a result. Item 3 carries no citation. Item 4
carries no citation. Item 2 carries Benjamin for the political form and Zhuang
and Hadfield-Menell for the administrative one, and that theorem is the only
formal result anywhere in the list.

**"§11.3 inherits the limit and does not restate it."** Holds, and the
inheritance is load-bearing rather than incidental. `11_03.tex:11` builds the
whole longitudinal requirement on drift — *Every one of the four features is
defined by a change over time — dissent metabolized, a metric substituted, an
exception recoded, a model drifting from what it tracks* — and concludes *the
slope rather than the level is the instrument*. A party that declares the myth
outright has no slope to measure. Searched §11.3 for every form of *declare*,
*announce*, *myth*, *outright*, *overt* and *avow*: **zero hits in 1,724 words.**

## The two descriptions that do not hold

**Feature 2's theorem was already its own sentence, and already had a lead-in
naming it** — *Simon Zhuang and Dylan Hadfield-Menell give the administrative
form as a theorem*. What was missing was not the sentence but the stop before
it. The item ran political form → administrative form → theorem as one chain,
the middle link a semicolon, so the theorem arrived as the fourth clause of a
run a reader is already skimming. The note's diagnosis — skippable — is right
about the reading experience and wrong about the cause.

**Feature 4's qualification was not "the last clause of a long paragraph".** It
was two sentences, and it already carried a lead-in flagging it as a detector
bound: *One qualification belongs with it, because it bounds what a detector
built on this feature can find*. What trailed was the closing **57-word**
sentence, which carried the historical fact, its gloss and the detector
consequence together, with the consequence last. The consequence was the clause;
the qualification was not.

## The two edits

**A. §2.1.2 item 2.** A five-word declarative goes in ahead of the result — *The
administrative claim is also a theorem.* — and `give the administrative form as
a theorem:` becomes `prove that`, active. **This is a lead-in that asserts, not
one that announces**, which is the distinction that keeps it under `style.md` §2:
it makes a claim a reader can disagree with, rather than promising that a claim
is coming.

The third change here was not asked for and is a correction. *and a world with
finite resources supplies them* sat inside the `prove that` construction, where
it read as part of what was proved. It is the book's own bridging claim — the
finite-resource setting is an assumption of their model, not a result of it — and
it is now its own sentence outside the citation: *A world with finite resources
supplies those conditions.*

**B. §2.1.2 item 4.** The 57-word closing sentence is split. The historical fact
keeps its sentence; the detector consequence gets its own, with the forward flag:

> An instrument tuned to drift will not register a party that announces it — a
> limit that section~\ref{sec:11.3} inherits when it asks what a detector would
> have to measure.

## The cross-reference, which is the one thing here running against the book's direction

**230 → 231.** D-089 (P28) cut 79 by class, D-099 (P35) cut more, and P131
recorded adding none on purpose. Four reasons for taking this one:

1. **It carries itself.** `style.md` §7's test is whether the sentence makes
   sense to a reader who does not follow the reference. The claim is complete
   before the reference arrives; the reference says *where the limit recurs*, not
   what it is. It is not the name-dropped shape — nothing here says "which is
   §11.3's argument."
2. **The direction is right.** §11.3 has two inbound references and makes **none
   of its own**. §2.1.2 made two.
3. **It points at a place that inherits a limit and does not state it**, which is
   the condition D-013 exists for.
4. It is the **second** `\ref` inside an `\item` in the book. `08_02_01.tex:8` is
   the first, so the shape has precedent, thin as it is.

## What was checked and not changed

- **§11.3 itself.** The flag helps a reader who reaches §11.3 by the argument. A
  reader arriving at §11.3 first still gets a detector specification built
  entirely on slope with no mention that a declared case escapes it. **Q-101**,
  on the default the note's own choice of remedy implies.
- **Items 3 and 4, which carry no citation at all.** Not the note's ask, and
  D-044 is the record of what a sweep for symmetry costs three arguments.
- **The qualification's *rather than* at *asserted as a virtue rather than
  arrived at by degrees*.** It is the corrective-antithesis shape `antithesis.py`
  censuses, it is the author's existing prose, and it carries the actual
  distinction. P132's finding was one-directional cutting; this is not the pass
  to take a clause out of a sentence I am already splitting.
- **The proof pair.** Not rebuilt. The committed pair is P132's and is now one
  pass stale.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
both edits read back out of `pdftotext` output, and the new reference prints as
*section 11.3*. Checked the three new sentences at 6, 7 and 8 words against every
line of all 133 sections: **0 shared runs.**

## Figures

133 sections, **1 changed**. 99,118 → **99,136** words (+18); §2.1.2 2,615 →
2,633. **196 pages unchanged.** 230 → **231** cross-references. 324 bibliography
entries unchanged — both citations were already in place and no entry was added.
0 `\textit`.
