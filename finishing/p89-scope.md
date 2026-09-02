# P89 — the ladder replaced by an anchorage, and the figure finally introduced

**The instruction.** Given across a conversation that began with a question about one
paragraph: *is that ladder introduced or explained anywhere? because I thought we had changed
over to a boating metaphor.* Then, in order: *i am inclined to go full boating, however … let's
just make sure that the ladders and rungs are all talking about the same thing as the boat hulls
and the water*; *could we find some kind of boating-adjacent metaphor in which boats might be
involved peripherally but not centrally*; *i am a bit hesitant about further overloading of the
word "hold"*; *seabed it is*; *yes, run the sweep*.

## The defect this pass repairs

**§3.2's ladder was never introduced.** `03_02.tex:11` was the first appearance of both words,
in this order: *The **third rung** asks that something be felt … One word to keep clear of **this
ladder***. Before that line the section defines four capacities in four `\emph` paragraphs and
never says they form a ladder, never numbers them, never calls them rungs. The figure arrived as
a definite reference to something that had not been established, and **27 further uses across
nine files leaned on it**. This is the D-117 `pointer` class — a term carrying weight with no
definition behind it — and P87's scan did not catch it, because every instance reads fine
locally and the defect is only visible book-wide.

## What the check found before anything was changed

The author's recollection of a boating metaphor was correct, and it is **not** in chapter 3.
§2.3.1 carries it: *Nociception, pain, anticipated pain, and suffering draw different depths of
self, **the way a hull draws water***, paying off four paragraphs later at *A hull that draws
more water than there is does not float badly; it is aground*. That figure **is** introduced, in
the sentence that first orders its terms.

**The two are not the same ordering, which is what the author asked to have verified.** There
are three four-item sets in the book, and they order different things:

| | §2.2 | §2.3.1 | §3.2 |
|---|---|---|---|
| Figure | a table, none | hull drawing water | ladder with rungs |
| 1 | Recognizing emotion | Nociception | Operational refusal |
| 2 | Simulating emotion | Pain | Reasons-responsive refusal |
| 3 | Instrumental valuation | Anticipated pain | **Affective concern** |
| 4 | **Affective concern** | Suffering (Cassell) | Phenomenal experience |
| Ordered by | what each shows | what each needs beneath it | what each asks be true |
| Direction | — | deeper is more | higher is more |

They intersect without coinciding: **affective concern is §2.2's fourth and §3.2's third**, which
the glossary's *mattering* entry already says, and §2.3.1's fourth and §3.2's fourth are both the
persistence argument. **§2.2 uses no rung or ladder language at all** — chapter 2 has zero
instances — so the conversion did not touch it.

**One of the 28 uses was a different ladder.** `05_01_01.tex`'s *its top rung is where moral
development is heading* is Kohlberg's stage model, where a ladder is the conventional figure. It
is untouched, and it is the only rung left in the book.

## Why an anchorage, and why not the obvious verb

**The figure had to be boating-adjacent without being §2.3.1's figure**, because those two
passages are the most confusable in the book — adjacent chapters, four items each, the same
prerequisite relation — and different figures were the main thing keeping them apart. An
anchorage is about what the bottom is made of; a hull drawing water is about how deep a vessel
sits. Same seascape, different question, and they cannot be read as one scale.

**The author's hesitation about `hold` was correct and checking sharpened it.** `hold*` runs 80
in chapter 3 and 229 book-wide, doing four jobs: *holds a reason* (a term of art, tied to the
Fischer and Ravizza guidance-control citation, ~8), *holds the floor / the line* (~5), *holds
against the party* (2), and the ordinary logical *holds that / holds for* (6). Only about seven
were convertible, and the largest cluster could not be touched without cutting the argument loose
from its citation. **The obvious relief verb was already spoken for**: `bite` has three
metaphorical uses meaning *takes effect* (§8.1.1, §9.3.2, §3.5), so borrowing it would have given
the book two unrelated metaphorical bites. `set` (183) and `weigh` (70) are saturated with
ordinary senses; `scope` (8) would collide with *scope of the floor*; `grip` (2) already means
the designer's control in §3.8.

**So the figure names nothing and explains how you tell.** It supplies epistemics, not position:
you cannot see which capacity produced a decline, and you find out by putting load on it. The
four are then referred to by their own names. `hold*` in chapter 3 is **80 before and 80 after**.

**Dropping the vertical was a gain, not a cost.** The ladder implied *higher is more*, which the
text then had to walk back — *nothing above the second rung is part of the requirement*. The
book stops at the second not because it is high enough but because the other two are further
facts, and the run-in now says so without the correction: **The floor requires reasons-responsive
refusal and asks nothing further.**

## The noun

`seafloor` was proposed and rejected on measurement. `floor` runs **246 book-wide, 126 in chapter
3, 6 in §3.2**, and the clause the figure attaches to is *Whatever **the floor** needs, that is
not it* — twelve words upstream, in a chapter titled *The Floor Beneath Learned Values*. It would
have put four `floor`s in four clauses in two senses. `seabed` has zero prior uses and no
collision. `ground` was rejected too: 24 uses, all abstract (*grounds for*, *grounded in*).

## Numbers

**25 replacements across 9 files**, closing 27 of the 28 rung/ladder sites. **89,854 → 89,889
words**, +35, all of it the two introduced sentences; **183 pages, unchanged**. New vocabulary is
deliberately light: `seabed` 3, `anchorage` 1, `anchor` 2, `drag` 2. `reasons-responsive` 8 in
§3.2 and 4 in §3.3, replacing a shorter ordinal — the one real cost of the conversion. 0
undefined references, 0 undefined citations, `check_all.sh` green.

## Left undone, named

- **The proof pair was already stale after P88 and is staler now.** Not rebuilt.
- **§2.2 still has no figure** and is a bare table. Whether the book wants one ordering device or
  two remains open; this pass made the two it has distinguishable rather than unifying them.
- §2.3.1's hull figure is untouched to the word.
- The glossary's *mattering* entry is still the only place the §2.2 and §3.2 sets are put side by
  side. It now reads *the third of the four capacities section 3.2 separates*, which is accurate.
