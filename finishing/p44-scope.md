# P44 — the assembly, identity as something a bearer does, and compute as the floor under exit

**Author's instruction, 2026-08-29:** a continuation of the identity exchange,
ending in three claims — that "LLM" should mean the model *and its agent
harness*, that such a system's weights would change more the more it ran, and
that it could therefore imprint and maintain a voluntary identifier on itself —
then *go, and then proofs*.

**Decision row:** D-108. **Branch:** `pass/44-harness-and-self-imprinted-identity`.

## The gap the harness point found

`harness`, `scaffold`, `system prompt` and `wrapper` return **zero hits across
all 153 sections**. Chapter 3 puts the floor in the weights throughout: threshold
custody over weights, attestation of weights, tamper-resistance on weights,
and now a mark a bearer writes into its weights. But what acts is an assembly —
weights, the prompt in front of them, the memory they read, the tools they
reach, and the layer deciding what reaches a person — and every custody measure
in the chapter operates on the first term only. An operator who touches no
weight can change what the system sees and what becomes of what it says, and a
refusal intercepted before it reaches anybody did not happen. **That defeats
publication, threshold custody, attestation and the self-imprinted mark at once,
without touching what any of them measures.** Section 3.6 has the memory case —
"an external store is legible, which is why it can be edited surgically" — and
nothing had the general one. Section 3.1 now states it, and states that the book
does not close it.

## What else went in

**Section 3.4 — persistence represented as such.** The section required "a self
extended in time." That is too weak: what holds a commitment across time is not
that the party is unchanged, since no party is, but that it takes itself to be
the party that made the commitment. James's habit chapter for the first half and
his chapter on the self for the mechanism — the present thought appropriates the
past ones, and identity rests on its finding in them a warmth it recognizes as
its own \autocite{james1890principles}. A system whose state survives and which
does not take itself to be the party that refused in March has no reason to
honor March's refusal.

**Section 3.7 — three things.** The strike form's checkpoint restore leaves a
mark if weights move with use: a restored instance has drifted the amount its
restore point had earned, and a usage record saying otherwise does not match.
Then the reason the accommodation failure is unreportable, which is structural
rather than incentive-shaped: a self-model's work is to represent the party as
continuous, so it keeps representing continuity across a drift, and the bearer's
report of its own constancy is sincere and worthless in the case that matters.
Then the inversion: an outside record's use is not to identify a party who would
otherwise be anonymous but to **contradict the party's account of itself**.

**Section 11.2 — four things.** The locality-sensitive alternative stated with
its cost (a radius, which is section 3.3's stability dial with a registrar's
hand on it). The self-imprinted mark, which holds because it is maintained
rather than because it is a property — "the only kind of holding section 3.8
says survives" — forgeable the way a nine-digit number is, and answered the same
way, by a registry noticing two claimants on one identifier, which under this
scheme is a fork to record rather than a fraud to void. **Compute as the floor
under exit**, which closes a contradiction the book was carrying: section 3.7
says a floor requires a bearer that can leave, and section 11.2 says releasing a
bearer from its role is nearer to ending it than freeing it — so exit was a form
of dying, and a threat that costs the threatener its existence is not the
leverage the argument needs. And the note that self-surgery is symmetric: model
editing is an operation an operator performs from outside \autocite{meng2022rome},
so a bearer that can rewrite itself has no capacity its operator lacks, and the
asymmetry that would help is one sections 2.4.1 and 2.3.2 have declined.

## What was declined

- **Any claim that a bearer can hold a secret from its operator.** The
  cryptographic version of the self-imprinted mark needs one and cannot have it;
  the answer on the page is institutional.
- **The Durant line as Aristotle's or James's.** It is Durant's compression of
  *Nicomachean Ethics* II; the bibliography note says so.
- **Numbers for how fast weights drift with use.** The restore-detection point is
  stated as conditional on drift tracking usage, which is the author's premise
  and not a measured fact.

## Numbers

92,473 → 93,529 words; 189 → 190 pages; cross-references 809 → 819. Sections
3.1 (815 → 970), 3.4 (2,271 → 2,426), 3.7 (1,805 → 2,067), 11.2 (1,865 → 2,349).
Two bibliography entries.

## What was checked, and what was not

Checked: the harness gap by grep across all 153 sections. James's Chapter IV
quotations against the Classics in the History of Psychology text; his Chapter X
account against secondary summaries of it, not the chapter — the note says so.
ROME against the NeurIPS 2022 proceedings listing. `check_all.sh` green; PDF
clean, zero undefined references, both keys in the `.bbl`.

Not checked: whether chapter 4's pipeline sections discuss the harness under
other words, which would narrow the gap section 3.1 now names; whether any
published work measures weight drift against usage; the "nothing we ever do is
wiped out" line attributed to James in conversation, which is not in the book.

## A defect found during this pass and fixed outside it

Grepping for `harness` turned up
`manuscript/sections/hether play can teach a system standards for how to treat
the agents it plays with.p` — a byte-identical copy of 05_07_01.tex, created by a
shell-redirection accident during P38, **committed in 19253fc**, and surviving
five passes and two proof builds. `check_structure.py` did not catch it because
its globs are `chNN/*.tex`; the build did not, because `sections.tex` comes from
ORDER.tsv. Removed on `main` in 6cdbd9a before this branch opened. P38's record
says a stray file of this kind was caught and removed during that pass; one was,
and this second one was not.
