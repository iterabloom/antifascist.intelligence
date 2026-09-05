# P102 — §3.3's non-replayability claim narrowed, and training that takes more than one party added to §11.1

**The instruction.** On the findings in `p101-scope.md` and the recommendation put in the
session — rule the repair now, put the discussion in §11.1 at about 250 to 300 words with
chapter 3 held to two pointer sentences, five bibliography entries, no standalone section —
the author: *i approve you opening the Verde paper's PDF. please perform the check on the
protocol-models paper's venue. I rule as you suggest above.*

## Part one, the repair

**§3.3:19.** The two sentences saying training is not replayable, with the author's *iirc*
parenthetical, now read:

> Floating-point addition on a parallel device is not associative, so the same seed over the
> same data reproduces the same model bit for bit only where the trainer arranged that it
> would — deterministic kernels, one reduction order, the same hardware — at a cost in
> throughput, and a succinct proof that a run happened as claimed exists for models three
> orders of magnitude smaller than these. What is left at scale is re-execution: a verifier
> with the data and comparable compute reruns the training, or samples it against a tolerance,
> and either way the check runs through the builder's choices and the builder's data. So there
> is no proof of a training history to publish beside the hash, and what can be published is
> an invitation to rerun it; section 11.1 says what accepting it costs and who can.

The sources are in `p101-scope.md`. What changed in the reading after the Verde PDF was
opened: RepOps covers single-GPU programs only at publication, with multi-GPU parallelism
named as future work, so even the reproducible-operator route does not yet reach a run at the
scale the sentence is about. That sharpened *at scale* rather than softening it.

**Three ripple sites and one clause.** §3.3:25's *a specification nobody has attempted to
implement* becomes *Nobody has implemented that specification for a floor*, with the nearest
attempt, refereed delegation over providers who may lie, named and pointed at §11.1. §3.3:65's
*an answer would rest on the builder's account of their own work* gains *or on a rerun by a
party the builder handed the data to*. §12.2.1:19's *training histories not being provable*
becomes *no succinct proof of a training history existing at this scale*, and the builder's
word gains *or on a rerun the builder made possible*. §11.2:52's *the only route to formation
evidence that anyone has proposed* becomes *the only proposed route to formation evidence that
needs neither the builder's data nor the builder's cooperation*, because re-execution is a
proposed route wherever the data is available.

## Part two, the discussion

**§11.1 gains a run-in, *Training that takes more than one party*, at the section's end**, in
the chapter's format. It opens on the three things §3.3 asks for — weights held so that
retraining takes more than one party, a quorum adverse in interest, a training history somebody
other than the builder could check — and gives each its built instance: a model trained across
participants none of whom ever holds a full set of weights, with time-varying transforms at the
shard boundaries, at under 2 percent of training time for a one-billion-parameter model; a
training run over providers who may lie, checked by refereed delegation with the right answer
if one provider was honest, whose precondition is an operator library fixing the order of the
additions at about 60 percent overhead and, at publication, on one GPU at a time; and a
thirty-two-billion-parameter model trained by reinforcement learning on rollouts from anyone
who connected a consumer GPU, with the training step on trusted machines and the decision kept.
The second paragraph says what the three share, the custody objection in engineering terms,
and what they add, that verification among adverse parties is a built thing with a known
precondition and a known price. Then the four-part close: the experiment, a floor's retraining
under refereed delegation among parties one of which is a plausible adversary, at a scale
needing more than one GPU, with §12.2.1's record published; the falsifier, a forged history
accepted with fewer than all but one verifier dishonest; the data, the training set in the
verifiers' hands and reproducible operators for the collective communication nobody has written;
the institutional condition, a verifier the builder did not choose with the compute to rerun the
builder's work, which is the chapter's one condition in the place where meeting it costs a
second training run.

**Length.** 404 words by the section's delta, 777 → 1,181, against a proposal of 250 to 300.
The four-part close is about a hundred of them and the estimate did not allow for it; the
three instances are about 65 each. **Offered for cutting**: the third instance, about 60 words
and the INTELLECT-2 entry, which is the least load-bearing of the three, since §3.9's pointer
sentence already carries its shape.

**Chapter 3's two pointers.** §3.3:25, above. §3.9:17, after *Custody moves up a level and
does not leave*: *The runs that now train one model across volunteers on several continents
have the same shape, the contributors many and the training decision kept by the few who hold
the step, which section 11.1 takes up.*

**Dating.** No year in the prose; the entries carry them. The prose says what exists and at
what size, which will age, and the style sheet's §5 exception for the targeting material is
the precedent.

## The bibliography

Five entries on instruction (D-009; P95 precedent), each with a note stating what the book
takes from it and the figures it relies on:

- `abbaszadeh2024kaizen` — Kaizen, CCS 2024, DOI 10.1145/3658644.3670316. VGG-11 at 10 million
  parameters, batch 16, 15 minutes of proving per iteration.
- `arun2025verde` — Arun, St. Arnaud, Titov, Wilcox, Kolobarić, Brinkmann, Ersoy, Fielding and
  Bonneau, arXiv 2502.19405, February 2025. **The PDF was opened on the author's permission**,
  for the author list and the limitations section: correctness if at least one provider is
  honest; if all are dishonest the referee identifies k−1 dishonest providers and still accepts
  a wrong output; RepOps under 30 percent overhead on large matrix multiplications, about 60
  percent on Llama-3.1-1B on an A100, 200 to 300 percent on small matrices and DistilBERT on
  some setups; IEEE-754 compliance assumed, which FP16 hardware does not widely give; single-GPU
  programs only, multi-GPU left to future work.
- `choi2023verifying` — Choi, Shavit and Duvenaud, NeurIPS 2023, arXiv 2307.00682.
- `long2025unextractable` — Long, Hewa Koneputugodage, Ajanthan, Zuo, Avraham, Shevchenko,
  Mohaghegh Dolatabadi and Ramasinghe. **The venue check**: the arXiv posting is v1 of 22 May
  2026 and its comments field says *Accepted at NeurIPS 2025*; the conference's own site lists
  the poster at neurips.cc/virtual/2025/poster/118911. So the paper was accepted at NeurIPS
  2025 and posted to arXiv five months after the conference. Keyed and dated 2025, with the
  posting date in the note.
- `primeintellect2025intellect2` — Prime Intellect Team and thirteen named authors, arXiv
  2505.07291, May 2025.

biber: 0 errors; 10 warnings, all pre-existing legacy-month notices on other entries, none on
the new five. All five render in the References.

## Named and not cited

The search for the protocol-models paper's venue also returned *Protocol Learning,
Decentralized Frontier Risk and the No-Off Problem* (arXiv 2412.07890, December 2024), from
the same group: a model trained and run across a protocol that no single party can switch off.
§3.5 opens on *The halt is always available* and grounds the chapter's identity claim on it.
The paper was not read past its title and abstract listing, it is outside this ruling, and it
is named here because it bears on a premise the chapter leans on.

## Numbers

**91,206 → 91,796 words, +590.** By section: §11.1 +404, §3.3 +133, §3.9 +32, §12.2.1 +11,
§11.2 +10. **184 → 185 pages**, built to the scratchpad; **0 undefined references; 20 overfull
boxes against P100's 20; 138 sections; 516 `\ref`.** Six `ORDER.tsv` digests refreshed.
`reports/section_stats.tsv` regenerated. `check_all.sh` green, including the typography check
over `refs.bib`. **Nothing committed at the time of writing, and P101 is uncommitted beneath
this.**

## Left undone, named

- **The run-in is a third over the proposed length**, and the cut is offered, not made.
- **The no-off problem is not read and not cited.**
- **`pipeline.md`'s source-layout table says `refs.bib` has 300 entries**; it had 303 before
  this pass and has 308 now. Not corrected.
- **Chapters 4 to 14 were not read.** The ripple sites were found by grep for the claim's
  phrases, not by reading; §11.1 was read in full before the run-in was written.
- **No figure in the five notes was checked beyond the sources named in `p101-scope.md`** and
  the Verde PDF's first six pages.
