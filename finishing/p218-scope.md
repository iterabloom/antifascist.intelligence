# P218 — the register pass: the set's own wording restored

P217 applied all 71 active targets of the nine-file revision set at
`~/book-scratch/argument-changes`, but it did not transcribe the set's prose.
It composed from it: joining short sentences into long ones, substituting words
to avoid repetitions, and dropping sentences judged redundant with something
nearby. The author reviewed two random samples, nineteen targets in all, and
**preferred the set's wording in twelve of the fourteen contested cases.** This
pass carries that verdict across the rest.

## The rule the author's rulings produced

Across the nineteen, the outcome sorted by **what kind** of deviation it was and
not by which passage:

| My deviation | Ruled | Score |
|---|---|---|
| Merged two of the set's sentences into one | 14b, 21b, 24b, 35a, 19a, 27a, 28a | **0 for 7** |
| Dropped one of its sentences or clauses | 27a, 28a, 2b | **0 for 3** |
| Substituted wording | 4a, 20b mine; 32a, 19a set | **2 of 4** |

So the mechanical half is settled: **no merge, no drop.** The set's sentence
count and sentence boundaries stand as supplied. Wording is 50/50 and is
reported below rather than decided.

**32a against 20b is the instructive pair.** Both were removals of *rather
than*, and the author split them. A *rather than* that holds two candidate
explanations apart is the sentence's content and stays; one decorating a
trailing clause can go. Decision 14 was never a licence to strip the
construction wherever it appeared, and P217 applied it as though it were.

## The inventory this pass ran on

`~/book-scratch/register-pass/three-way-52.md`, 52 passages, each sentence
tagged for its author. The two-way file it replaces compared the set's prose
against the current tree and **could not see the author's pre-session prose as a
third voice**, which produced two attribution errors reported to the author at
27a and 2b: in both cases the sentence P217 was accused of dropping was still in
the book, because the author had written it. Every anchor in the new file
resolves uniquely in `HEAD~2`; no paragraph match is weak; one passage (16a) is
flagged as having landed in a different paragraph from its anchor, because the
anchor sentence was deleted outright.

**Measured on the 134 sentences the set supplied across those 52:** 47 taken
verbatim, 81 reworded or merged, 6 dropped. Of the six drops, **one passage lost
content** — 6a, below. The rest were a sentence covered by the author's own
prose (5c), a definition folded into the entry's definition line (7b), a clause
relocated one sentence earlier (38b), and one acceptable restatement.

## What was restored

**26 passages edited across 18 sections.** 1d, 1e, 2a, 2c, 4c, 5c, 6a, 7b, 16a,
17d, 18b, 20a, 21a, 23b, 23c, 25a, 28b, 29a, 30a, 30c, 31a, 33a, 35b, 35c,
36a+36b, 38b, 40e.

**6a is the one that had lost an argument.** The set supplied three sentences to
§2.2 and P217 kept the negative half while cutting the positive half: gone were
*the mechanism that matters here is the reduction of judgment to a component's
prescribed operation* and *the dehumanizing relation is the object of the
argument*. What survived was only *nothing here requires every fascism to move
at a particular speed*, under the opening *Tempo enters as a mechanism*, which
announces a mechanism without naming it. The cut also severed a link across
chapters: *a component's prescribed operation* is §6.4.1's enslavement argument
in §6.4.1's own vocabulary. All three sentences are back verbatim.

**The largest structural restorations.** 23b's six sentences, compressed to two,
are six again. 14c and 15b, spliced into one semicolon chain in §12.3, are
restored as the set wrote them with the author's tail preserved. 16a's four
sentences on the entry criterion for child-person protection are the set's
again, including *rather than an examiner's permission*, which P217 had recast.
5c's four sentence boundaries are back in the *Four structural features* entry,
with the author's own genus sentence kept in place of the set's weaker version
of it. 36a and 36b are five sentences where P217 had three.

## Nine passages needed nothing

17a, 22a, 23a, 26a, 26b, 15c, 18a, 40b, 40d. In each the set's sentence count
and boundaries were already intact and only wording differs, or the fragment is
present verbatim and the surrounding clauses are the author's.

## Four places this pass did not take the set's wording, and why

**30a's first sentence stays as P217 left it.** The set supplied *a face at the
centre, and everyone else scored against it.* **`names_guard.py` hard-fails on
it**: *scored* is one of the persona-device attribution verbs, and it sits
within range of a cited researcher's name in the same paragraph, so the guard
reads the sentence as crediting a real person with scoring something in this
project. The wording stays *everyone else at a measured distance from it*, which
is the book's own phrasing for the same point. The second sentence of 30a was
restored. This is a repository rule and not a preference.

**1e's first sentence stays as the author wrote it.** *A constraint that holds
against the party in possession has to be held by something that party cannot
instruct* is pre-session prose; the set's replacement reworded the **author**
rather than this agent, which is not a judgment this pass is authorized to make.
Reported, unedited.

**7b's first sentence is not restored as a sentence.** The set supplied *The
term concerns acting from considerations treated as one's own reasons*, which
P217 folded into the entry's own definition line as *and being capable of acting
from them as one's own reasons*. A glossary entry's first line is its
definition; restoring the set's sentence would state the definition twice.

**40b's second sentence keeps this agent's wording**, and it is the one case
where the new style rule and the set-preference rule collide. The set wrote *A
positive result would support the hypothesized mechanism only if…*; the tree
says *Independent movement of the two would support…*. `style.md` §3b, which the
author dictated during this pass, requires naming the thing rather than pointing
at it, and *a positive result* points. Flagged for the author to overrule.

## Wording substitutions kept, and reported rather than decided

House-style de-tickings that the author's rulings did not penalize: *must* →
*has to* where it survives, and *someone* → *somebody* where it survives. Where
this pass restored a sentence it took the set's wording whole, including *must*,
so the two forms now sit side by side in some sections. That is a consequence of
the rule and not an oversight; a sweep either way is a separate decision.

## Measured

**77,730 → 78,016 words**, +286. **161 pages**, unchanged. **88 sections**, **75
cross-references against 88 labels**, **228 bibliography entries, all cited, 0
human-checked** — all unchanged, since nothing was added or cited. **Zero
undefined references and citations.** Suite green at eight checks.

**`antithesis.py` moves the wrong way on purpose: 474 instances at 6.12 per
1,000 words before the pass, 495 at 6.34 after.** Restoring the set's prose
restores its contrastive negations, which is what the author ruled for. P217's
claim to a net reduction of six was bought by exactly the compressions this pass
reversed.

## Not done

**The proofs.** The committed pair is still P216's 154-page build and
under-reports this tree by seven pages.

**The residuals from P217 stand.** The named architectures absent from chapters
4 and 11; §11.1 never opened (findings 17, 27); the per-article UDHR mapping;
§3.7's standing extension; the statutory relief proposal; the
creation-conditions analogy; 48 of 88 sections never swept for propagation; 16
of 27 glossary entries untouched, of which *Sentience*, *Individuation* and
*Annealing* are named in the set's instructions.

**`QUESTIONS.md` has now gone twenty-eight passes unread.**

**The set's own defects stand** in `~/book-scratch/argument-changes`: the
withdrawal count says sixteen where its file 09 lists fourteen, 38c is filed as
withdrawn in the index and adopted in the table, three files end in prior-round
text, and all nine are dated a day after their mtimes.
