# P10 scope: the fifth editorial review, tiers 1 and 2

The fifth review arrived 2026-08-24 as a structured critique followed by two
dialogue turns between the author and a model. It was checked against the
manuscript before any ruling was sought: **nineteen of twenty checkable claims
verified verbatim.** The one error is that §5.3.5 does not hold the
interruptibility material — kill switches and circuit breakers are in §5.3's
opener; §5.3.5 is "Long-term AI safety considerations."

Author's rulings: "do tier 1", then "and then do tier 2, taking the dialogue's
version" (D-038).

## Tier 1 — the book's own epistemic standard, applied to chapter 4

The review: the book runs careful treatments of mirror neurons and Ekman, then
anchors chapter 4 on Piaget and Kohlberg with none, and cites Gilligan for care
ethics without noting her argument originated as a critique of Kohlberg.

**Verified, and worse than stated.** §4.1.1 says the stage theories "anchor what
follows" over a bare `[[cite:C0322]]`. Chapter 4's only two existing boxes are
the IBM Watson XPRIZE and the GDPR — *dated-example* boxes under `style.md` §5,
not epistemic-caution boxes. §4.7.1 cites Gilligan six sections after Kohlberg is
used as the anchor, with no connection drawn.

Also verified: the phrase "metaphor borrowed for color" appears **exactly
twice**, in the openers of chapters 3 and 4, both times asserting the transfer is
real and neither time arguing it. §4.7.1's honest admission that the playground
analogy is no more than partial is the last sentence of the section.

**Done.** §4.1.1 gains a 568-word box, "What the stage theories will and will not
carry," covering the three standing critiques and answering the question the
review actually posed — *why do these frameworks transfer when mirror neurons
didn't?* The answer that carries it: the mirror-neuron claim was that a specific
mechanism implements a specific capacity, so when the mechanism failed nothing
was left; Kohlberg's stages are not a mechanism but a description of an order,
and what the criticisms damage (universality, the top rung as maturity, judgment
predicting conduct) is not what the chapter uses. The box then states the two
limits outright: the order is not a developmental law, and the disanalogy is not
bridged by anything said there.

Three claims verified by live search **before** the prose entered the manuscript,
per D-009 and D-030:

| ID | Claim | Status |
|---|---|---|
| C0718 | Snarey's review of 45 studies in 27 countries; stage sequence broadly supported, postconventional stages rare or absent outside urban Western samples, absent entirely in Kohlberg's own village studies | verified |
| C0719 | Blasi 1980, *Psychological Bulletin* 88:1–45, on the judgment-action gap | verified |
| C0720 | Gilligan 1982, developed alongside Kohlberg at Harvard, arguing his scoring recorded relational reasoning as a lower stage | verified |

C0720 is cited **for the origin of the critique only**. The book takes no
position on Gilligan's gender thesis, which is itself contested.

Also in tier 1: §4.7.1 now names where care ethics came from; §4.1.4's
targets-per-hour indicator gets a run-in head parallel to §6.6.4's existing
"Measure the slope, not the level" (it was in paragraph 6 of 9, under a section
titled "AI in Service of Human Dignity"); and §4.6.3, §6.7.6 and §8.1.3 now
reference each other through §2.1.5.

## Tier 2 — the floor

The review's central finding, and it is correct: §4.6.3 ("None of this
substitutes for a genuine override"), §6.7.6 ("there are things it will not do to
a person no matter who wants it") and §8.1.3 ("a commitment nobody can enforce…
is a different kind of object") arrive independently at an unconditional
constraint, and none references the others. Meanwhile §2.1.1 disposes of
deontology in four sentences on grounds of rigidity, and chapters 3 and 4 —
**30.3% of the book**, measured — build learned judgment instead. §2.1's "hybrid
approach… is one plausible way through" was where the resolution belonged, and
nothing was put there.

**The author directed the dialogue's version over the review's, and the
difference matters.** The review proposed one architecture: a floor, learned
judgment above it, the antifascist question becoming what is in the floor and who
can edit it. §2.1.5 states that, and adds the argument that answers §2.1.1's
objection — rigidity is a defect in a *complete* moral theory and the entire
point of a floor. But the review's version stops where it is most persuasive. The
dialogue does not, and sets out a fork with a cost on every branch:

| Branch | What it buys | What it costs |
|---|---|---|
| Floor in the architecture, no bearer | Real constraints that survive adversarial fine-tuning (§7.2.2) | Durability is a fact about **custody**, not the system; the custodian can be compelled (§8.3.3). Capability ablation fails here because the constituent capabilities are not separable from general competence |
| Floor with a bearer | Refusal that generalizes to unanticipated pressure, and can notice a constraint hollowed out (§2.1.4's first feature; §6.6.4's slope from inside) | **Patienthood**: a moral patient conscripted to refuse, engineered to want it, unable to consent (§2.4.4) — §2.1.4's own signature turned inward |
| Floor outside the system | The analogue of what §6.7.6 admires; IHL is a floor with no bearer inside the state it binds | **Enforcement**: the option a state can compel, which returns it to the first |

Those three costs are exactly the book's three unfinished threads.

## Deliberately not taken — tier 3

The dialogue's second turn concludes that **the capacity to refuse and the
capacity to suffer are gated by the same architectural property**: read backward,
the persistence criterion says you cannot build a system that can refuse the
school strike without building something that can be wronged.

It is not taken here, for two reasons.

1. **Its load-bearing step is asserted, not argued.** Turn one identified the
   slack precisely — the book separates persistence, a self-model (§2.3.3: "the
   self is a model"), and Cassell's narrative self, and Cassell-suffering is
   defined on the third. Turn two closes it in one clause ("months of integrated
   involvement is the biography"). **The D-034 comparison first offered here was
   wrong and is withdrawn** (see D-039): D-034 did not refuse a resolution — the
   author chose the resolving branch and §2.1.4 argues it and pays for it in the
   text. The defect in the dialogue's step is not that it resolves rather than
   defers. It is that it resolves by assertion a question that is open to
   argument, and D-039 settles it by argument instead.
2. **It would change what §2.4.4 means.** "Consent is inapplicable" becomes
   conditional on the system not being built to refuse, and "can it quit?" becomes
   live. That is a larger reopening than P7, P8, P9 or this pass, and it should be
   entered deliberately rather than as a fourth bullet.

§2.1.5 therefore names the slack as open, in §2.1.4's manner, and hands the
specification forward. **Tier 3 needs its own ruling.**

## A render bug found by looking at the proof

The first draft of §2.1.5 used markdown `**bold**` and `*italic*`. The dialect
has no such markup, `render.py` passes it through unchanged, and it rendered as
literal asterisks in the PDF. Caught on page 13 by looking at the page as an
image, and rewritten as plain prose. `check_all.sh` has no test for this.

**§2.4's Westworld epigraph carries the same defect and still does** — one
`*here*` that renders as asterisks. It is pre-existing, it sits inside a quoted
epigraph, and it was left alone rather than edited as a side effect of this pass.

## Checks

`check_all.sh` green: round-trip, structure (158 sections), named-persons guard.
`ORDER.tsv` and `outline.tsv` gained the §2.1.5 row; digests refreshed; join
rebuilt; TOC regenerated; `headings.py` reports ms-vs-outline title diffs = 0.

**D-025:** §2.1.5 measures 1 contrastive negation per 315 words and the §4.1.1
box 0 in 568 — both inside the band. Chapter 6's untouched density and §7.1.6's
1 per 136 are untouched by this pass and are still not fixed.

## Not author-accepted

Every item is drafted. Book 85,592 → 87,582 words (+1,990). Proof rebuilt, 145
pages (was 142); pages 13 and 50 were looked at as images. The rest was not read.

## Postscript: D-039 narrowed by D-040, same day

The author pressed the settled step with an architectural objection — in animals
the self-model exists because the organism has to stay viable, so the caring is
what the machinery is for — and a worked case: a bearer that has watched an
operation for months, knows the compound is a school, reports it, and is wiped
while the operators keep the coordinates it already produced and bomb the school.

Two of three points landed. The vignette's own force is partly borrowed — its
absurdity comes from flat affect toward *everything*, the school included, and
restoring a strong outward stake makes the same facts read as a deadman switch
rather than an incoherent agent. But the two hits are real and are taken:

1. **The "cannot be suborned" corollary is withdrawn.** Immunity to leverage is
   worth having only where leverage is the cheapest route. Removing a human
   inspector is expensive and conspicuous; deleting a bearer is neither, and its
   output survives. The property's value is conditional on erasure being costly
   or visible — which is custody, the first branch's problem under another name.
2. **"The floor is buildable" is withdrawn**, and instrumentally acquired
   self-concern is promoted from residual to the central engineering difficulty.

A third result came out of it: **none of the three branches escapes custody.**
They are not independent options; they fail into one another.

D-039's narrow claim — the two conditions are separate and the identity is not
established — stands, as does §2.4.4's conclusion by the second route.
