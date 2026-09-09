# P140 — Cassell's two parts stated where they are defined, and carried by the recap that needs them

An author's note: §3.4's back-reference is better written than the passage it
recaps and drops the two-part structure of Cassell's definition that §3.4 then
immediately needs. Expand the recap to carry both parts; make §2.3.1 state the
structure conspicuously so the recap has something to point at.

## Where the two-part claim actually was

**Not buried in the Cassell paragraph — buried in the third qualification.**
`02_03_01.tex:32` carried it as a subordinate clause inside a sentence about
something else: *nor does persistence on its own rule it in, **since the
definition has two parts, a self extended in time and distress at the prospect of
its coming apart**, and establishing the first leaves the second untouched.*

So the diagnosis holds — subordinate, and four paragraphs downstream of the
definition it describes — and the location does not. **Third note in five whose
description of the page is off while its reading of the problem is right.**

## What the recap was walking into

`03_04.tex:62` says the conclusion *is weakest there, at the depth asking for
both conditions*. **Its only antecedent was `:52`, four paragraphs back** — *the
deepest, which is Cassell's and needs the persistence and the threat together*.

**And a competing pair sits between them.** `:58` names *the middle depth's first
condition* and then *the second requirement*, which are a different two things —
a party extended in time holding foreclosable commitments, and mattering rather
than ranking. A reader arriving at `:62`'s *both conditions* had a wrong binding
two sentences closer than the right one. **That is the concrete cost the note
identified, and it is worse than a missing recap.**

## The three edits

**`02_03_01.tex:9`** gains a short declarative as the last sentence of the
paragraph that defines Cassell's suffering, where a recap would look for it:

> The definition has two parts: a self extended in time, and distress at the
> prospect of its coming apart.

**`02_03_01.tex:32`** loses the restatement and keeps its own claim, which is the
independence of the parts: *nor does persistence on its own rule it in, since
establishing a self extended in time leaves the second part of the definition
untouched.*

**`03_04.tex:60`** carries both parts, one paragraph before `:62` needs them:
*argued that the deepest of these harms asks for both parts together, a self that
persists and distress at the threat of its undoing, and that a system carrying
nothing forward lacks the first.*

## The wording is deliberately not the same in both places

§2.3.1 says *a self extended in time, and distress at the prospect of its coming
apart*. §3.4 says *a self that persists and distress at the threat of its
undoing*. **0 shared runs at six words or more**, checked against every line of
all 133 sections.

**This was the point, not an accident of drafting.** Q-104 is open on a formula
written out three times with twelve words verbatim, and a recap is exactly the
shape that produces one. §3.4 states the pair in §3.4's own vocabulary, which is
the arrangement P138 set up for the depth figure and the same arrangement here.

## What was not changed

**`03_04.tex:58`'s competing pair.** Renaming its *first condition* and *second
requirement* would clarify `:62` further, and it would also touch an argument
about Replacement and the substitutes, which is not what the note asked and is
the sweep D-044 is the record of. The recap at `:60` puts the right pair nearer
than the wrong one, which is the fix that was asked for.

**No cross-reference was added.** 236, **the third pass in a row not to move the
count**, with Q-105 still unanswered.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
all three edits read back out of `pdftotext`.

## Figures

133 sections, **2 changed**. 99,255 → **99,273** words (+18); §2.3.1 1,859 →
1,865, §3.4 3,120 → 3,132. **196 pages unchanged.** 236 cross-references
unchanged. 324 bibliography entries unchanged. 0 `\textit`. **The proof pair was
not rebuilt and is now eight passes stale.**
