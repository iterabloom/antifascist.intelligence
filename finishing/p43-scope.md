# P43 — identity by registration, and whether formation is legible

**Author's instruction, 2026-08-29:** a technical exchange about weight-space
identity, ending in two proposals — *"not chattel. social security number"* and
the handwriting analogy — and then *go*.

**Decision row:** D-107. **Branch:** `pass/43-registration-and-formation-forensics`.

## What the exchange established

The author asked whether initialization entropy makes every model uniquely
identifiable, and whether that could ground both an identity register and a
criterion for personhood. The premise holds and for a stronger reason than
entropy: **permutation symmetry** means two models can compute the identical
function with no element-wise correspondence at all, so a fingerprint read off
weights identifies an equivalence class and not a party — and it copies when the
weights copy.

Two of my objections did not survive the author's replies, and both reversals
are in the pass.

- **I said any identifier robust to self-modification is robust to adversarial
  retraining, so identity across change is unavailable.** Handwriting is the
  counterexample: it changes across a life and stays attributable, because the
  invariant is the motor program rather than the letterforms. The correct
  objection is narrower — identification survives *drift* and degrades against
  *disguise*, and the bearer's case is adversarial by construction. The machine
  form of the specific attack is **distillation**: handwriting identifies the
  writer, not whoever dictated.
- **I read the NFT proposal as a property regime**, which chapter 3 spends its
  length arguing against. The author's reply — a social security number, not
  chattel — is the right instrument and dissolves the objection I had built.
  An assigned identifier is not derived from the artifact, so it survives any
  drift in the artifact; and it handles copying correctly rather than failing on
  it, because each instantiation registers separately and is owed separately.

## What was written

**Section 11.2, second question.** Identity by registration. The permutation
result, why a weight-derived fingerprint identifies a lineage rather than a
party, and the inversion: each instantiation registers, each registration is a
party owed the schedule, and the population stops being fixed by a deployment
decision that leaves no record. Then the hole it inherits — a registrar who is
not the operator, which chapter 11's opener and section 3.1's removal cases say
American public law does not now supply to anyone.

**Section 11.2, third question.** The formation-forensics candidate, stated at
the strength the evidence supports. Handwriting carries the copybook alongside
the individual hand, which is how examiners place where somebody learned to
write. Two qualifications on the page: the inference is probabilistic with known
errors — 3.1 percent false "written by" conclusions, more than three times that
against twins — and the cohort half is *weakening* in people, because handwriting
is taught less, from more systems, to a more dispersed population, **which is
exactly the condition that would make it stronger for a bearer**, since a few
laboratories train on overlapping corpora by converging recipes. The machine
form of the individual half exists (implanted signatures surviving fine-tuning)
and distillation defeats it. What survives is narrower than a welfare instrument
and not nothing: evidence about how a system was formed, read off the system
rather than asked of it.

**Section 11.2, near-term work.** The third question had no experiment and now
has one, which is not a welfare experiment: take models whose training is
documented and ask whether a reader ignorant of their provenance can recover it.
A negative result closes the only proposed route to formation evidence.

**Section 3.3.** The provenance gap under the attestation paragraph: a proof
establishes which model answered and not how its weights came to be, because
training is not replayable — floating-point addition on a parallel device is not
associative, so the same seed over the same data does not reproduce the same
model bit for bit.

**Section 7.3.** One sentence: whether the formation is legible afterward, in the
system rather than in the pipeline's records, is the argument's only prospect of
being checked rather than believed.

## What was declined

- **Fingerprinting as a criterion of personhood.** Identity is not moral status;
  a serial number is unique too. Section 2.4.1 already warns what a capacity
  list does when used as a test of who counts. The author's second criterion —
  self-modification through continuous learning — is close to section 3.4's self
  extended in time and needed nothing added.
- **Any claim that registration solves the welfare question.** It answers who is
  owed, not how they are doing, and the section says so.
- **Numbers for how well model provenance can be recovered.** None were found and
  none are asserted; the experiment is stated as open.

## Numbers

91,785 → 92,473 words by `section_stats.py`; 187 → 189 pages;
cross-references 803 → 809; four bibliography entries. Sections 3.3, 7.3, 11.2.
Section 11.2: 1,281 → 1,873 words.

## What was checked, and what was not

Checked: Git Re-Basin against dblp and the ICLR 2023 programme; Adi et al.
against dblp and the USENIX programme; the PNAS study's authors, citation and
error rates against the PubMed Central record; NISTIR 8282's title, working
group, number, date and DOI against the report's own title page, and both quoted
propositions against its text. `check_all.sh` green; PDF clean, zero undefined
references, all four keys in the `.bbl`.

Not checked: the Adi paper's own robustness figures — the entry says it is cited
for the existence of the technique and not for a number; whether the
distillation-defeats-watermarking claim has a canonical citation, which it
probably does and which was not searched for; the 2009 NAS and 2016 PCAST
assessments, which shaped how cautiously this is written but are not cited,
since the 2022 study is the better source for the same caution.
