# P76 — chapter 11's opening enumeration cut, the sections kept, the finding moved to the close

**The author's finding.** Chapter 11 opens with numbered entries summarizing the
sections, then the sections deliver the same content at length; the *“Nearest
work:”* annotations largely duplicate each section's own. **Either the list is the
chapter and the sections compress, or the sections are the chapter and the list
becomes a paragraph.** The finding preceding the list — that the institutional
conditions are one condition, and that *Trump v. Slaughter* removed it — is the
most consequential paragraph in the chapter and is sandwiched between two
apparatuses.

**The diagnosis holds. Three of its figures do not, and one of its premises is a
defect in the chapter rather than in the finding.**

## Three corrections to the finding's figures

| The finding says | Measured |
|---|---|
| nine numbered entries | **eight.** §11.9 is deliberately off-list, and the paragraph after the list said so |
| the list runs ~900 words | **508.** The whole opener was 1,313 |
| its *“Nearest work:”* annotations duplicate each section's own | **The label appears only in the opener**, eight times, and zero times in the nine sections |

The third correction does not rescue the list. The *content* duplicates: item 4's
annotation is §11.4's argument, item 6's is §11.6's, and item 1's ranking
rationale — *the most load-bearing unsolved problem in this book* — is §11.2's
own sentence verbatim. What a reader met was not two labelled apparatuses but the
same material twice, compressed and then at length.

## The direction was settled by evidence, not chosen

| | the list | the nine sections |
|---|---|---|
| `\autocite` | **0** | **34** |
| inbound `\ref` from outside chapter 11 | **0** | **46**, from chapters 2–13 |

The list's two `\ref`s are `sec:3` and `sec:9.3.5`, neither a sole pointer —
§9.3.5 has nine other inbound references. **Cutting the list orphans no citation
and strands no pointer.** Compressing the sections into the list would have cost
the chapter its entire evidentiary basis, so *the sections are the chapter* was
not a judgment call.

## The finding could not survive literally intact, and one phrase is why

Its first sentence read *“One finding comes out of the list below rather than out
of any entry on it, and listing the entries apart is what hid it.”* **Cut the list
and the first six words point at nothing** — the class P68, P69 and P70 each
recorded, here inside the paragraph the instruction protects. The rest of the
paragraph is independent of the list. One phrase moved: *the list below* became
*the sections below*, and *listing the entries apart* became *taking each gap
separately*, which is what the sentence always meant.

## The count in the protected paragraph was wrong, and 11.6 is why

The finding read *“Every section here closes by naming an institutional
condition, and the nine conditions are one condition wearing different clothes.”*
Section 11.6 closes: *“It is also the only entry with no institutional
prerequisite, a reason to run it before the ones above it.”* **The chapter
contradicted itself, and the contradiction was load-bearing in both directions** —
the opener's second paragraph sends a reader to 11.6 as the cheapest thing
precisely *because* it has no institutional condition.

Read against the nine closings:

| | closes on |
|---|---|
| 11.1, 11.2, 11.3, 11.4, 11.7 | **a party outside the operator** — the five the finding enumerates |
| 11.5, 11.8 | a data requirement, not a party |
| 11.9 | **is** that condition rather than naming one |
| 11.6 | **no institutional prerequisite at all** |

The five the paragraph lists are exactly the five that hold. **Put to the author
before anything was edited**, the ruling was to correct the count rather than
record it or amend 11.6. So *nine* became *five*, the other four are now stated,
and 11.6's exemption stops being a contradiction and becomes the reason the
chapter's cheapest entry is cheap. *Most of this work is fundable today and cannot
be run* survives unchanged at five of nine — the five are 5,383 of the chapter's
8,946 section words.

**The same overclaim stood one paragraph earlier** and would have staged the
correction two paragraphs later, which §10 of `style.md` forbids: *“Each section
closes by naming four things: … and the institutional condition without which it
cannot run”* is now *“and, where it has one, the institutional condition.”*

## The reordering, which is what un-sandwiches the finding

The opener ran: what the chapter is → the ranking criterion → **the finding** →
the four-part close → the bounded-search qualification → the list → 11.9 is not on
it → one gap has no section here. It now runs:

1. what the chapter is
2. **the gap with no section here**, moved up beside it as the scope note it is
3. the ranking criterion
4. the four-part close
5. the bounded-search qualification
6. **the finding**, ending the opener and handing off to §11.1

The four-part close now *precedes* the finding, which is the order the argument
needs: the finding reads the institutional condition off an apparatus the reader
has been told about. The opener ends on *“Most of this work is fundable today and
cannot be run,”* which is the sentence the sections are the answer to.

**The paragraph that said §11.9 is not on the list went with the list.** Its
content survives twice over: the four-part close already names §11.9 as having no
experiment, §11.9's own last sentence says *“It belongs at the end because every
other entry's condition runs through it,”* and the finding now says §11.9 *is*
the condition.

## Two dangling referents the cut created, both repaired

- The opener's *“would invert most of the list”* → *“most of this order”*, and
  *“the cheapest useful thing on it … which says in its own entry why”* →
  *“the cheapest useful thing here … which says why”*.
- **§11.6's own text**, which the instruction does not name: *“This is the
  cheapest entry on the list”* → *“in the chapter.”* Nothing else in the nine
  sections referred to the list; swept.

## Measurements

| | before | after |
|---|---|---|
| chapter 11 | 8,983 | **8,473** |
| the opener | 1,313 | **793** |
| book | 93,796 | **93,286** |
| pages | 187 | **186** |
| `\ref{sec:}` | 547 | **547** — two cut with the list, two added by the finding |
| glossary locators | 114 | **114** |
| `refs.bib` | 300 | **300**, nothing orphaned |
| sections | 136 | **136** |

`check_all.sh` green after `refresh_order_shas.py`; 0 undefined references and 0
undefined citations.

## Named for a ruling and not acted on

**The nine sections still deliver their nearest work without a label.** The
opener's qualification paragraph promises *“Each section names the nearest work I
could find and says where it stops,”* and each does, in prose. Whether that
should be a marked apparatus — as the four-part close effectively is, through the
`\runin{The near-term work}` head every section carries — or stay unmarked is a
design question this pass did not take. It was a labelled apparatus in exactly one
place, and that place is gone.
