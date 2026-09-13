# P198 — the author's two tweaks to the Foreword, landed

The author edited `ch00/00.tex` in the tree and said so. Two changes, both in the
paragraphs P196 and P197 had been working in. **Suite green, 156 pages, 0
undefined references and citations, 74,684 → 74,663 words.**

## The targeting clause

*a weapons targeting pipeline running at thirteen thousand names in thirty-eight
days* becomes **a weapons pipeline targeting thirteen thousand locations in Iran
in thirty-eight days.**

**This answers the distinction P197 left open** — the sources and the book say
*targets*, the Foreword said *names*, and in this book that difference carries
weight. *Names* is gone.

**Iran is right and is an improvement.** The figure is from Operation Epic Fury,
the 2026 Iran campaign, which is what §6.3.1 `:60` and §3.6 `:68` both attribute
it to, and the Foreword previously gave the number with no theatre attached.

**One observation, and it is small.** *Locations* is as much an interpretation of
the source as *names* was, pointed the other way. Every statement of the figure —
the CDAO's quotation in `breakingdefense2026maven` (*13,000 targets in 38 days*),
§6.3.1's *generating and ranking targets*, §3.6's *thirteen thousand targets* —
says **targets**, and none says what kind. A strike target is usually a place and
may be a vehicle, a structure or a person; the book keeps the unspecified word and
spends §6.3.1 distinguishing Habsora, which marks buildings and structures, from
Lavender, which marks people. **Nothing was changed**: the author has now chosen
this wording having seen the distinction raised, and *targets* is available to him
if he wants the book's own word.

## The chapter 7 paragraph

Its second sentence is cut: *It is the only test the definition gets, and whatever
it is worth in the other eleven chapters is owed there.* The paragraph now stops
after naming the three things chapter~7 runs the definition on.

**Nothing downstream rested on it.** The arithmetic P196 verified — *the other
eleven chapters*, against twelve numbered chapters — goes with the sentence, so
that claim is no longer in the book and no longer needs to survive a
restructuring. The claim that chapter~7 is the definition's only test is also
gone; **§7.4 still makes the substance of it in its own voice**, at `:3`, *There
is a third instance and it is the one this book is inside.*

## Checked

`check_all.sh` green at 91 sections, `build_tex.sh` at 156 pages with 0 undefined
references and 0 undefined citations, `ORDER.tsv` digest refreshed, the page
rasterized and read. `Chapter~\ref{sec:7}` still prints *Chapter 7*. No new
typography: the edit introduced no dash, quote or TeX-notation character, and the
em dash in the paragraph above it is untouched.

**74,663 words**, down 21: the cut sentence is 19 of them and the clause rewrite
is the other 2.
