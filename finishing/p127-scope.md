# P127 — the two senses of persistence, reconciled

## Instruction

The author forwarded an outside note arguing that the book uses *persistence* for two
different properties and transfers between them silently, then: *"Please first check your
assumptions and then make the fix."* Scope was chosen from two options he was given: the
edit reaches three sites, and the deliverable is the edits plus this record and one commit,
without proofs.

## The note's claim

§2.3.1 introduces persistence as the criterion that does not route back through self-report
— architectural, verifiable by anyone with access. §3.4 then needs something else: not that
state survives but that the party *takes itself to be* the one that refused in March, which
is representational and checkable only through behavior and self-report. Two chapters, one
word, two properties, and the transfer is silent. The note proposed importing Part III of
*Reasons and Persons* and making persistence a dial rather than a gate.

## What checking the assumptions found

**The defect is real. Its shape is dated staleness, not a silent transfer.** The sentence
that reasserts the clean external check — `03_04.tex`, *the asymmetry that makes the
persistence criterion useful does not repeat* — entered at `5d6fae0`, D-040, 2026-08-24.
The upgrade that invalidates it — *persistence \emph{represented as such}* — entered at
`135936f`, P44 (D-108), 2026-08-29, eleven lines above it in the same section. P44 did not
revisit the older sentence. P85 built further on the upgrade and did not either. P125's
motivation route says *what the second route does not do is make the requirement easier to
check* and does not join the two. **Four passes have written in this paragraph's
neighbourhood since the requirement changed kind, and none of them looked up.**

**The asymmetry sentence is an author-confirmed ruling and had to survive the edit.** D-039
recorded it as the second of two residuals; D-040, which narrowed D-039 on the author's own
architectural objection, promoted it to *the central engineering difficulty* and states in
terms that instrumentally acquired self-concern *is not checkable from outside the way
persistence is*. That contrast is correct as ruled. **The repair is therefore additive** —
add the third term, do not rewrite the contrast. The first draft of this pass would have
rewritten it.

**The positive overclaim is in §2.3.1, in the sentence that limits its own criterion.** It
read *what is externally checkable is whether a continuing self is there at all*, which is
stronger than the architectural facts the paragraph had just listed. The check is sound in
the negative direction — nothing carried forward, no continuing self of any kind — and
overclaims in the positive, because the self chapter 3 needs is one the system has to take
itself to have. §2.3.1 already says persistence does not rule Cassell-suffering *in*, and
says it of the second condition only.

**One correction to my own reading, made before any edit.** I had told the author that
§2.3.2's *has persistence by design, so the party who consented is still present* was the
site where the equivocation did damage. It is not. That sentence was written under D-039 —
*section 2.4.4's conclusion stands but its stated reason does not reach a persistent
bearer, and that section now says so* — and its function is to concede that the bearer
escapes the no-continuing-party argument before reaching the same conclusion by the
ordinary route. The step feeds a concession the section immediately grants. It is loose and
it is not where the cost is. Q-069 attaches to the same paragraph and closed at D-199 on a
different worry.

**Two sites are correct and were not touched.** §3.7 uses the architectural check properly,
scoped to whether memory *contents* can be relied on rather than to identity. §3.5's
*defend its own persistence* is the ordinary continuation sense.

**Parfit was declined.** Part III answers how much identity there is; the live question is
which of two properties the word names, and degrees do not touch it — represented
persistence at any setting is as unverifiable as at full. The dial is also half-built
already and pointed the other way: §3.4 closes on *how much persistence and how many
foreclosable commitments the design puts into it*, while §2.3.1's gate sits only at zero,
which is what the shallow-water argument stands on. And §3.4's *The same water, shallower*
is built so the conclusion needs no contested theory; Parfit is cited there for Appendix I,
the three families of well-being, and the bibliography note says so. Importing a second
contested theory into the passage designed to need none would work against it.

## The three edits

All additive; nothing was deleted, and one phrase was narrowed.

1. **§3.4, at the upgrade.** After *nothing in the architecture supplies the taking*: **Carrying
   something forward is the precondition for the taking and not a test of it.** The relation
   is named where the requirement changes kind, so a reader does not carry the architectural
   reading through the two paragraphs that reinforce the representational one.
2. **§3.4, at the asymmetry sentence.** D-039 and D-040's contrast left standing, with the
   third term added after it: **The same is true of the taking, so persistence represented as
   such outruns what the criterion can supply.**
3. **§2.3.1, at the two boundaries.** *whether a continuing self is there at all* narrowed to
   *whether anything is carried forward at all*, and one sentence added: **That check is
   decisive in one direction only: nothing carried forward rules a continuing self out, and
   something carried forward does not rule one in, since the self at issue is one the system
   has to take itself to have, which is what section~\ref{sec:3.4} requires of a bearer.**
   *Rules out / rules in* is the section's own vocabulary from its next paragraph but one,
   where the same move is made about Cassell's second condition.

**Two drafting decisions the second read produced**, both from P126's finding that one read
of a diff is not enough. Edit 1 first carried a `\ref{sec:2.3.1}`, which would have been the
second pointer at that target in one file; it was cut, and §2.3.1 — which had no
cross-reference at all — carries the joint instead, which is the pairing D-185 repaired
between §3.8 and §11.2. Edit 2 first read *whether it takes itself to be the party that
refused in March*, making three near-identical eight-word runs of that formula in one
section; *the taking*, the section's own term, replaced it.

## What was not done

- **Nobody has read §2.3.1 or §3.4 end to end.** The edits were made against their paragraphs
  and the neighbours. That stands beside the 18 sections P126 left unread.
- **§2.3.2 was not touched**, on the finding above. After edit 3, its *persistence by design*
  is no longer licensed by §2.3.1 read architecturally; it is licensed read
  representationally, which is what *by design* means once §3.4 has stated the requirement.
  Q-085 records it with a default of leaving it.
- **No proof pair.** The PDF was built to the scratchpad for measurement and not committed;
  the 2026-09-08 pair on disk is one pass behind and the README still points at it.
- **Nothing was added to the argument.** The pass names a distinction the book had already
  made in two places and had not joined.
- **Six rows of `DECISIONS.md` are malformed and were left that way.** D-221 through D-226 were
  written without the Status cell the file's own header defines, so they render as four-column
  rows in a five-column table. D-226's was closed during this pass and the change reverted on
  finding the other five: assigning a status is a claim about what the author confirmed, and
  these are other passes' rows. D-227 carries its own.

## Figures

133 sections, unchanged; 2 changed. **97,915 → 97,996 words (+81)**; 194 pages unchanged; 17
overfull boxes unchanged; 0 undefined references and citations; 320 bibliography entries
unchanged; 223 → 224 cross-references, the one addition being §2.3.1's first; suite green.
