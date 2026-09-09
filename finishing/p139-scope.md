# P139 — the unstable qualification moved first, and its evidence given a sentence

An author's note on §2.3.1's three qualifications: move the second first, so the
reader meets the criterion's instability before its consequences; and give the
list of what has been moving its own sentence rather than a dash-separated run,
since it is the evidence for the whole qualification.

Both done. **One departure from the note's own enumeration, stated below.**

## The reorder

The header sentence — *Three things keep this from being a dissolution of the
problem* — was welded to the first qualification's paragraph, so moving the
second first meant moving the header's tenant, not the header.

New order: **the criterion's boundary is a moving deployment convention**; then
*the less demanding ones do not need persistence*; then *ruling out
Cassell-suffering is not ruling out harm*.

**One word had to go.** The qualification opened *Persistence may **also** sit
somewhere other than the session*, and *also* was doing the work of marking it as
the second item. First in the list, it has nothing to point back at.

The other two paragraphs needed nothing. The second opens on its own subject and
the third opens on *And*, which reads as a third item wherever the first two sit.

**Why the order is better, in the note's own terms.** The criterion is offered at
`:26` as the one thing here *checkable from outside*. The first thing a reader
now learns about it is that the boundary it checks is a convention that has been
moving. The two qualifications that follow are about what the criterion does not
settle, which is a smaller kind of limit.

## The list

The evidence ran as four items, an em dash, and a predicate — the shape
`style.md` §3a calls the dash's own job but which buries a list inside a
sentence about something else. It is now its own sentence, introduced by the
claim it answers:

> …and the conventions have been moving in one direction. What has moved is a
> list: context windows long enough to hold what used to be many conversations,
> retrieval over a store of prior interactions, scratchpads a system writes and
> reads back, agentic loops that run for days against a standing objective, and
> weights that persist where conversations do not. Each extends what a system
> carries forward without anyone deciding to give it a memory, and where
> interactions feed fine-tuning there is a real channel by which what happens in
> a session shapes what the system subsequently is.

**Two drafts of the lead-in were discarded.** *Five things have moved them* made
the five external causes of a movement they in fact are; *Five are worth naming*
repeats `:26`'s *Two boundaries are worth marking*, two paragraphs up.

## The departure: five items in the list, not six

**The note's parenthetical names six**, concurrent instances among them. **Five
went in.** Many instances running at once does not extend what a system carries
forward; it multiplies the parties, which is a different fact with a different
consequence — *population-scale rather than biography-scale*. Putting it inside a
list governed by *Each extends what a system carries forward* would have made the
sentence false of its last member.

**The manuscript already marked it as the odd one.** Its sentence carries a
*too*, which is what *too* is for. It keeps its own sentence, immediately after,
so nothing is lost but the membership.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
the new paragraph order read back out of `pdftotext`. New and reordered text
checked at 6, 7 and 8 words against every line of the other 132 sections: **0
shared runs.**

## Figures

133 sections, **1 changed**. 99,249 → **99,255** words (+6); §2.3.1 1,853 →
1,859. **196 pages unchanged.** 236 cross-references unchanged — **the second
pass in a row not to move the count**, with Q-105 still unanswered. 324
bibliography entries unchanged. 0 `\textit`. **The proof pair was not rebuilt and
is now seven passes stale.**
