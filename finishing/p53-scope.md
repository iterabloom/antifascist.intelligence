# P53 — the cross-reference density pass (D-118)

**Author's finding:** *"it's all way too cross referenced. the cross references are
distracting."* Ruled on the method before anything was cut: **restate, then cut** —
where a pointer carries meaning, replace it with a short restatement of the claim and
delete the reference; where the sentence already carries the claim, delete the reference
and nothing else. The glossary was ruled out of scope, because a locator in a glossary
entry is the entry doing its job.

## The measurement that set the method

848 references in 92,728 words of prose, one every 109 words. **51 percent of the book's
paragraphs carried at least one; 21 percent carried two or more.** The introduction and
the conclusion were the two densest body chapters — one per 70 and one per 67 — which are
the two places a reader is least willing to be sent elsewhere. Chapter 10 ran at one per
243 with nobody having complained it read as disconnected, and that was taken as evidence
of what the book could stand.

**Why P28 (D-089) got 10 percent when the instruction asked for 50.** `xref_shapes.py`
sorts every reference by the shape of its sentence. The five shapes it calls removable —
signpost, appended, restated, attributive, structural — total about **100 references
between them**, and P28 cut those. **625 of 806 are "inline": the reference is a term in
the sentence.** That mass is not lint, and no tool reaches it. Cutting it means rewriting
the sentence, which is what this pass did and what the route the author chose licensed.

## What was cut, by class

| Class | Treatment |
|---|---|
| **Self-indexing openers** | A chapter or section opener mapping its own children, immediately before the reader meets them in order. Chapter 11's numbered list gave each item a `(section~\ref{sec:11.N})` locator where the *n*th item was already section 11.*n*. Cut outright. |
| **Within-chapter pointers** | *"Section 3.5 left a dial with no recommended setting"* — the reader passed it two sections ago. Replaced by *"The previous section"* or by the claim itself. |
| **Repeat targets inside one section** | Section 8.3.4 cited 8.3.3 four times; section 11.2 cited chapter 3 and 2.4.1 repeatedly. First kept, later ones restated. |
| **Pointer with the content beside it** | *"Section 5.4.2 covers Taiwan's vTaiwan process, the clearest existing case of…"* — the content is in the same sentence, so only the number came out. |

## What was kept

**Imports.** A sentence that borrows a result and cannot stand without saying whose it is.
Chapter 3's opening paragraph names four separate sections at which the book arrived at
the same requirement; that convergence *is* the argument and all four stay.

**Genuine navigation.** *"A reader who is going to get off this argument somewhere should
know that section 3.3 is where the exits are."*

**Chapter 1's roadmap.** Twelve references in one paragraph, kept deliberately. In a
roadmap the reader is not being sent anywhere — they are being told the shape of the book,
and the numbers are the subject rather than an interruption. **This is a judgment, not a
measurement, and it is the one place a reader might reasonably overrule the pass.**

## Numbers

**848 → 596 references book-wide; the body 728 → 476**, the glossary's 120 untouched by
ruling. **One per 122 words of body prose to one per 188.** Paragraphs carrying a
reference **51 → 36 percent**; carrying two or more, **21 → 10 percent**.

| ch | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| before | 2 | 27 | 60 | 147 | 57 | 64 | 72 | 46 | 36 | 55 | 31 | 86 | 45 | 120 |
| after | 2 | 15 | 51 | 53 | 46 | 51 | 57 | 32 | 28 | 43 | 30 | 61 | 7 | 120 |

**70 section files changed. 94,017 → 93,740 words**, a net loss of 277 for 252 references
removed — the restatements bought most of the words back, which is what the chosen route
costs and why a reference cut is not a length cut. **191 pages before and after. 0
undefined references.** `check_all.sh` green.

**Chapter 3 went 147 → 53**, the largest single change, and it is where the pass found the
most within-chapter pointing: the chapter mapped its own eight sections in its opener, in
section 3.1, and again in 3.8.

**Chapter 12 went 45 → 7.** A conclusion restates rather than indexes, so nearly every
pointer in it converted.

## What this pass did not do

No claim changed and no reference was repointed. **No citation was checked against a
source.** The four chapters that remain densest — 11 at one per 143, 9 at 146, 7 at 148,
4 at 153 — were thinned but not driven to the book's new average, because their references
are doing the work D-013 built the regime for: chapter 11 points each gap back at the
place it arose, and chapter 7 applies chapter 2's definition and has to say so.
**Nobody has read the 70 changed sections end to end since the pass.**

## The finding this pass owes the record

Six repairs made immediately before it — the glossed ordinal pointers of D-117's class —
**made the problem marginally worse and then were partly undone by this pass.** Glossing a
pointer puts the content on the page and leaves the number beside it, which is heavier than
either alone. In four of the six the gloss made the pointer redundant, and the pointer came
out here. **The general lesson: when a cross-reference needs explaining, check first
whether it needs deleting.**
