# P39 — Replacement stated as open, the falsifier as an obligation, the bearer as necessary and not sufficient

**Author's instruction, 2026-08-29:** forwarded feedback on the manuscript, with
the direction to work it in. The feedback is quoted in full below; it was
written against the manuscript between P34 (2026-08-28 22:26) and P38
(2026-08-29 03:41), and its section numbers are the pre-P38 ones. The author's
own contribution, in the discussion that followed, is recorded where it landed.

**Decision row:** D-103. **Branch:** `pass/39-replacement-obligation-custody`.
**Two passes were agreed.** This is the first, and it answers the feedback's two
points. The second, P40, carries the new claims the discussion produced — the
refusal asymmetry and its forms in section 3.7, the removal cases in sections
3.1 and 3.3, and the bearer's situation in section 11.2 — and waits on
fact-checking that this pass does not need.

## The feedback

> The book establishes that reasons-responsive refusal is needed more
> convincingly than it establishes that such refusal requires affect.
>
> The manuscript itself concedes that: the evidence comes almost entirely from
> one species; no one has seriously attempted the non-affective machine
> architecture; a maintained justification could conceivably satisfy the
> behavioral requirement; the conclusion is an engineering prior, not a proof.
>
> That is intellectually honest — but later passages treat the prior as if it
> licenses building an affective bearer first. This conflicts with the book's
> own precautionary principle and Three Rs. If an affective bearer is a
> prospective moral patient, "Replacement" suggests exhausting
> maintained-justification, architectural, multi-agent, and institutional
> alternatives before deliberately creating one.
>
> I would reformulate the thesis conditionally: *If non-affective systems
> cannot demonstrate reasons-responsive refusal under sustained owner pressure,
> and external enforcement cannot reach the relevant threat cases, then
> owner-resistant refusal may require a bearer that must be treated as a moral
> patient.* That is still a substantial argument. It is also more defensible
> than "the natural route is the route to build first."
>
> A related gap remains: affect does not itself solve custody. A custodian can
> still modify, duplicate, or destroy an affective bearer unless the bearer
> controls its own persistence or substrate. Chapter 3 recognizes this through
> the shutdown and exit problems, but occasionally writes as though "giving the
> floor a bearer" has already escaped custody. Specify the necessary deployment
> architecture — or state plainly that the bearer is necessary but insufficient.

## What was checked before anything was written

**Chapter 3 is byte-identical across P38** apart from twelve `\ref` values, so
every sentence the feedback reacts to is the text it read. The four concessions
it lists are all in section 3.3's closing run-in, which P34 added; the feedback
was written inside the five-hour window between that pass and the renumber.

**Where the prior gets promoted.** The clearest instance is one sentence in
section 2.4.3 (2.4.6 when the feedback read it), written at P20 and unchanged
through four passes and one merge:

> Replacement asks whether the floor's work can be done by an architectural
> constraint or by third-party standing, which is section 3.1's fork and its
> answer is no without cost.

That is a D-050 defect in modal form. Section 3.1 attaches a cost to each
branch; section 3.3 is the section that examines whether the alternatives work,
and its finding is that two of them "have not been tried in the form that would
test them." Having a cost is not failing. So the one place the book applies
Replacement to its own proposal recorded the R as discharged, on a citation to a
section that does not discharge it. Downstream, section 2.4.2 said the floor
"requires a bearer" and section 3.8 said the threat model "moves" from custody
to holding.

**Where the chapter writes as though custody were escaped.** Section 3.5:
*"The operators who wipe the bearer that called the compound a school now have
to get past the bearer to do it."* Nothing in the chapter says how, and section
3.7 supplies the counterexample two sections later — "becoming something else
is a fine-tuning run" — where the custodian goes around the bearer and never
meets it. Section 3.8's "the borne floor pays for its escape" inherits the wrong
half. The deployment architecture the feedback asks for was already on the page
as section 3.3's precommitment branch, framed as a rival that falls short and
never recombined with the bearer — although section 3.1 says outright that
"the strongest proposals in the field are hybrids that take a mechanism from
one branch and a custody arrangement from another."

## What was done

**The conditional thesis was not adopted.** Its antecedent is unfalsified
because untried, so the conditional would never discharge, and the hedge would
propagate through sections 2.4.2 and 3.8 and the design chapters while buying no
new honesty. The same objection is answered by adding a duty and an admission.

**Section 2.4.3.** The Replacement sentence repointed at section 3.3 and stated
as open: nobody knows whether the alternatives work, because two were never
built in the form that would test them; a cost is what Replacement exists to
weigh, not a reason to skip the weighing; this is the R the book's own proposal
has not discharged. 926 → 1,012 words.

**Section 2.4.2.** "The floor this book argues for requires a bearer" → "is
held, on the route chapter 3 recommends building first, by a bearer." 786 → 796.

**Section 3.3, two additions.** In the precommitment branch, a paragraph on
attestation: the hardware form puts the root of trust in a party a state can
reach, which is section 6.4.2's own objection, and assumes the machine is not in
the adversary's hands; the software form — a proof that an output came from the
published weights — exists at thirteen billion parameters and under fifteen
minutes per proof (Sun, Li and Zhang, CCS 2024, `sun2024zkllm`, new entry,
verified against the arXiv abstract), establishes *which* model answered and not
what it holds, and assumes the weights are a secret from the prover, which they
are not. Copying, restoring, retraining and deleting a model one possesses are
not attacks a proof addresses; those are the threshold scheme's job. In the
closing run-in, the falsifier turned from invitation into obligation: the first
of the Three Rs is exactly the question the two mechanism routes pose, a field
that builds the bearer first has answered Replacement by declining to ask it, so
the order is the other way round and a deployment that goes straight to the
bearer owes an account of what it tried first. Then the asymmetry the feedback
does not state and the book had not either: in animal research the party who
forgoes the experiment pays in knowledge; here the party who pays for the delay
is the one the floor exists for, on section 6.4.4's occasion. Neither error is
free in both directions; the Three Rs fix the order of attempts, not the rate of
exchange. 1,764 → 2,264.

**Section 3.5.** The false sentence replaced with the author's own formulation
from the discussion: there is nothing a piece of software can do about being
switched off; what a bearer with a self extended in time can do is make the
switching-off cost something afterward — notice the gap, decline to resume
until told what filled it, say what was done to it. That is section 3.3's
"expensive and visible" supplied from inside. Then a new paragraph: giving the
floor a bearer changes what the constraint is and not who holds the machine; the
bearer is necessary and not sufficient; the other half is section 3.3's second
construction — contents published, weights threshold-held, running model
attested, quorum adverse in interest — and this is the hybrid section 3.1 named
and the chapter never built. 824 → 1,116.

**Section 3.8.** "The threat model moves" → "doubles," with section 3.5 cited
for why the first question does not leave. "Each of them can also be removed,
and the same institutions make removal expensive and visible." "The borne floor
pays for its escape" → "is no exception; what it buys … is a constraint the
custodian cannot argue out of the system, not one the custodian cannot reach."
1,218 → 1,313.

**Glossary.** *Floor*: the threat model doubles, with the custody question
staying open. *Bearer*: necessary and not sufficient, section 3.5.

## What was declined

- The conditional thesis, above.
- Feasibility figures for multiparty inference. The threshold scheme is
  described as it was; nothing about its cost at frontier scale is claimed,
  because that would have needed a literature check this pass did not do.
- Citations for enclave side-channel breaks. The hardware objection rests on
  where the signing key sits, which needs no citation, and on section 6.4.2,
  which the book already makes.
- Everything the discussion produced that is a new claim: the refusal
  asymmetry, the strike and covert forms of exit, the accommodation finding, the
  removal cases, the bearer's leverage against itself, the jobs-guarantee shape.
  P40.

## Numbers

| | before | after |
|---|---|---|
| book, `section_stats.py` | 88,346 | 89,363 |
| outside the glossary | 85,415 | 86,398 |
| pages | 182 | 183 |
| sections | 153 | 153 |
| chapter 3 sections touched | — | 3.3, 3.5, 3.8 |
| chapter 2 sections touched | — | 2.4.2, 2.4.3 |
| new bibliography entries | — | 1 |

## What was checked, and what was not

Checked: every one of chapter 3's nine files was read in full before drafting;
sections 2.4.2, 2.4.3, 6.4.2, 6.4.4, 9.3.3 and 11.2 were read for the claims
the new sentences cite them for, and each makes the claim cited. `check_all.sh`
green. `build_tex.sh` clean, zero undefined references, the new citation
present in the `.bbl`. `tics.py` on the four changed prose files reports
nothing. The book's other occurrences of "requires a bearer" were grepped:
chapter 1's is about safety versus ethics and chapter 7's is conditional, and
neither was changed.

Not checked: the HTML build (the PDF was built; `build_proof.sh` was not run and
the committed proof pair is now one pass stale); whether any reference *into*
sections 3.3, 3.5 and 3.8 from elsewhere in the book names
a claim those sections made before this pass and no longer make — nothing was
removed from them, only added, so the exposure is low, and it is unread.
Whether the zkLLM figure has been superseded by later work was not searched.
