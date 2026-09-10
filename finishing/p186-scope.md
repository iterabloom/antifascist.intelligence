# P186 — the author's inline annotations, enumerated and answered

Author instruction, arrived at over a session: **enumerate every ALL-CAPS
editorial note in the manuscript, give one sentence of context for each, say what
should be done about each, then implement all of them.** The annotations are the
ones D-263 preserved on the author's explicit instruction and that every commit
since has carried through `--no-verify`.

## The census

**51 notes in 9 files**, all in chapters~2 and~3, found by two shapes: a bracketed
span of the author's own prose followed by `-- ALL CAPS`, and an ALL-CAPS
insertion in brackets inside the prose. `STATE.md` had recorded **52 in 10
files**; the discrepancy was not chased down and is recorded here rather than
resolved. Two ALL-CAPS hits were read and excluded as false positives: `00.tex:5`
(`THIS BOOK began`, the appendix's styled opening) and `12_01_01.tex:5` (India's
`IT` Rules).

`check_typography.py` reports one violation per line, so the 29 violations at
session start covered 27 note-bearing lines plus two of the author's own straight
quotes. **The count is now 3**, none of them a note: `01.tex:22`, `03.tex:15` and
`03_04.tex:17`, all straight double quotes in the author's own prose. The third
was masked until now by a note on the same line. All three were left.

## What the reading found, beyond the notes themselves

Five shapes ran across the set, and naming them collapsed 51 items into rather
fewer repairs.

**One repair carried three notes.** §2.1.1's contractualism gloss, §2.1.1's
capabilities entry and §2.3.1's Nussbaum sentence are one point: contractualism
runs out where a party cannot be one of the parties, Nussbaum names that failure,
and species membership is the door a nonhuman mind arrives through. **An earlier
draft of this finding had it backwards** — it claimed the capabilities approach
was the only one of the six that could be turned on the machine. The author
doubted it; checking found five of the six have live literatures doing exactly
that, and contractualism is the one that structurally cannot.

**Impossibility claims stated wider than they are true**, five of them, and
several contradicting the book elsewhere: *no external access to internal
experience* against §3.2's interpretability claim; *nothing in the architecture
supplies the taking* against §4.1.2's Miller and Cohen material; and *not attacks
a proof system addresses* against §3.3's own rotating-damage construction two
paragraphs later.

**Ordinals the reader cannot recover** — *the three gaps between the four*, *the
third way in its strongest form* — which P53 and P55 had already broken and
repaired once between them under the name *the fourth capacity*.

**The consent cluster has one root.** §2.3.2's four notes are one defect.

**Restatement at distance generates notes.** §3.2 argues the relocation at L19 and
again twelve lines later; all three notes on the second telling are artifacts of
it.

## The repairs that are more than a clause

**§2.3.2, consent.** The section held that consent is *inapplicable* to a bearer
because it was made for its role and no prior party could have agreed. The
author's objection defeats that: nobody consents to being born, and formation
does not void anyone's consent. **What voids it is the power that outlasts the
making** — the party that built the bearer can still rebuild it, is the party
asking, and has left it nowhere to go. Those are facts about the arrangement and
not about the subject's competence, which is the author's second correction: **the
conditions of its consent are defective, not its consent.**

That changes which instrument applies. Guardianship is the *incapacity* remedy and
the section reached it by an incapacity analogy. The section now runs two families
of precedent — incapacity, answered by guardianship; and consent spoiled by
circumstance, answered by holding that some protections cannot be waived at all —
and puts the bearer in the second while taking the machinery from the first. **The
book had no waiver, duress or inalienability vocabulary anywhere.**

**§2.3.2, recuperation.** The note's worry is conceded rather than answered:
borrowing a worked-out solution to an adjacent problem is how a hard question gets
absorbed, the animal case is the live instance because committees constituted to
protect research animals approve very nearly everything, and the borrowing is done
anyway with the failure named.

**§3.2, the epistemic feelings.** The section excluded James's felt *if* and *but*
as anchored to the argument rather than to anybody's welfare. **The author's
objection stands and the exclusion does not**: *but this would hurt her* is a
felt *but* anchored to her, and the section concedes the defeater two sentences
later — *what the operator does not supply is how much the reasoner had riding on
the conclusion.* The taxonomy is replaced by a test the chapter already owns:
whether the state survives the operator's redescription of the occasion. **No
bibliography entry was authored** — standing rule 1 is in force this session — so
the reframing-resistance finding is written as an open empirical question rather
than asserted. It was checked: Andow reports a core of moral-relevance intuitions
resistant to framing, and the literature is mixed.

**§3.3, what a proof can carry.** The claim that reasons-responsive refusal is
*not the kind of property a proof can be written about* is false as stated, and
the author's range-proof objection is why. The obstacle is in the writing: nobody
can write the circuit, because the property quantifies over cases nobody
enumerated and enumerating them makes them anticipated. What replaces the limit is
a construction — **publish the hash before anyone has chosen a case, let a party
who is not the operator choose afterwards, send pairs differing only in whether
the reason for refusing still applies, and prove each answer against the hash.**
It proves no mechanism. It removes the competing account of a pass by ordering,
which is what a pre-registration does. The author's *long list plus a none-of-the-
above category* is answered in the same paragraph: enumerate the reasons rather
than the cases, require each refusal to name one, and require a refusal resting on
none to say so.

**§3.3, custody.** *Copying, restoring, retraining and deleting* are custody
problems and not secrecy problems, and the section already had two answers and
denied having any. Two more went in beside them: a signed statement of continued
operation, so that deletion is done in public, and release of the correction
against a proof that the floor still hashes to what was published.

**§2.1.2.** The closing paragraph was cut whole. Its seven strategies are
`style.md` §2a's capability list, one of them an independent auditing body, which
the paragraph above it says produces false assurance. The section now ends on
*you will not find it unless you are already inside.*

## Verified before writing

**The right temporoparietal junction** as a structure implicated both in the
control of attention and in attributing awareness to another, which the author
supplied with an `IIRC`: confirmed, and cited to `graziano2013consciousness`,
already held. **Framing resistance in moral intuition**: confirmed as a live
finding and as contested, and written as an open question for that reason. **The
homunculus lineage**, for the note that opened the session: literal homunculi
belong to alchemy and to preformationist embryology, the philosophy-of-mind
homunculus arrives already named as a fallacy by Kenny in 1971, Descartes blocks
the regress himself in the *Optics*, and Dennett concedes nobody avows Cartesian
materialism. **Chapter~4 handles the same figure correctly** and needed no change.

## Not done

**Three straight double quotes** in the author's own prose, above. **The 52-versus-
51 discrepancy** with `STATE.md`. **`ledger.tsv`'s decisions column**, which still
stops at D-258. **No bibliography entry was authored**, standing rule 1 being in
force; where a claim wanted a source it was written as an open question instead.
