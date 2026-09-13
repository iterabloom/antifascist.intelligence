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

**Nothing downstream rested on it**, and the cut is better than a cut — it is a
de-duplication. **Chapter~7's own opener carries the same claim almost verbatim**,
at `07.tex:7`: *and this chapter is where the book does it. Everything the
definition is worth in the other eleven chapters is owed here.* The Foreword
sentence was that line restated from the front matter, so removing it is D-013's
one-home rule rather than the retirement of a claim.

**The arithmetic P196 verified therefore stays in the book**, at one site instead
of two, and still has to survive any restructuring that changes the chapter count.
**Nothing in the suite counts chapters against that phrase**, so a later pass has
to find `07.tex:7` by reading.

*(Corrected at D-300. This paragraph first said the arithmetic went out of the
book with the sentence, and cited §7.4 `:3` rather than the chapter opener. The
probe that caught it was run against the rebuilt HTML proof, expecting the phrase
to be absent.)*

## Checked

`check_all.sh` green at 91 sections, `build_tex.sh` at 156 pages with 0 undefined
references and 0 undefined citations, `ORDER.tsv` digest refreshed, the page
rasterized and read. `Chapter~\ref{sec:7}` still prints *Chapter 7*. No new
typography: the edit introduced no dash, quote or TeX-notation character, and the
em dash in the paragraph above it is untouched.

**74,663 words**, down 21: the cut sentence is 19 of them and the clause rewrite
is the other 2.
