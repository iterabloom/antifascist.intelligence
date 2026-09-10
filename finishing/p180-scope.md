# P180 — the faciality section rewritten

Author instruction: §2.2.1 stages Ekman against Barrett; **both grant that there
is a face to be read**. There is no face given in nature — there is a machine
that produces the face as a surface of signification, computed against a
standard face, with every other face registered as deviance. **Buolamwini's
error rates are that machine doing its arithmetic aloud.** The research question
in chapter~11 changes accordingly: not a better classifier, but that **the
instrument is the politics**.

## One numbering correction

The instruction named **§11.8**. §11.8 is *The Responsibility Gap, Which No
Experiment Closes*, which carries no classifier question. The section with the
research question about classifiers is **§11.7, *Is Emotion Legible From a Face
at All?***, whose closing line read *the open research question is not how to
build a more accurate six-emotion classifier*. **The pass was applied to §11.7.**
Nothing in §11.8 was touched.

## The defect

§2.2.1 ran the dispute correctly and stopped one level short. Ekman's face
displays a discrete state; Barrett's face is a poor guide to a state the brain
assembles as it goes. **Both positions are about what the face discloses and how
much survives the reading.** Neither is about where the readable surface came
from, and the applied field — which is what the section exists to set up — rests
on the premise neither side was defending. The section's four difficulties then
inherited the omission: *whatever bias is in the training data is in the
classifier* files the problem under sampling, which makes it a thing a better
corpus fixes.

## §2.2.1, rewritten

**614 → 1,500 words. One run-in → three.** The Ekman, Barrett and cross-cultural
paragraphs are kept as they stood, because §5.2, §11.7 and §12.1 all lean on
them, and the affective-computing run-in is kept with one item extended.

**`\runin{What neither camp is arguing about}`** names the shared premise, then
separates head from face: what is given anatomically is a head, and a face is a
surface organized to be read — held still, framed, lit, set against other faces
of the same kind. Deleuze and Guattari's Plateau~7 supplies the strong version:
concrete faces are produced, by an abstract machine of faciality that overcodes
the head into a surface where meaning is expected to appear. **The racism claim
is quoted rather than paraphrased**, because its content is the mechanism the
section needs — the machine does not proceed by exclusion, it determines degrees
of deviance from a center, and the measuring is the operation. Nobody is put
outside; everyone is placed at a measured distance.

**`\runin{The machine doing its arithmetic aloud}`** is the pass's argument, and
it is made from two things already in the book.

**The registration step.** `taigman2014deepface` was in §2.2.1 already, cited for
a different thing entirely — that verification is an easier problem than
expression analysis. Its alignment stage is the literal instance of the claim:
DeepFace warps every detected face onto **a single generic three-dimensional
model built by averaging scanned human heads**, so that everything reaches the
network frontal and in correspondence with one reference. **The standard face is
not a figure of speech in this arrangement. It is a file, somebody assembled it,
and every other face is presented to the system as a departure from it.**

**The output.** `buolamwini2018gender` was in the book at §6.1 as a
representation finding. Read as arithmetic it is the same machine's other end: up
to 0.8 percent error on lighter-skinned male faces, up to 34.7 percent on
darker-skinned female faces, **error climbing with distance from the center, out
of an instrument nobody had to instruct in any of this**.

**The audit's own construction is part of the finding, and the paper says so.**
Gender was scored as female or male because the products emit binary sex labels,
and Buolamwini and Gebru state that their evaluation inherits those labels and
the reduced view of gender they carry; skin was scored on the Fitzpatrick scale,
a dermatological instrument for predicting sunburn. **This is quoted as the
authors' own limitation, not raised as an objection against them** — it is the
cleanest available demonstration that the categories belong to the instrument
rather than to the world.

**The consequence, which is the instruction's last clause.** A balanced corpus
can move the center and flatten the error rates, and that would matter to real
people; §6.1 makes that case and the section now points at it for exactly that
much. **What a balanced corpus cannot do is remove the reference the pipeline
registers against**, because the registration is the first operation and
something has to occupy the middle of it. The politics is relocated, not
dissolved: a different face at the center, everyone else still at a distance,
still being measured.

**The dispute is not settled, it is re-described.** If the constructionists are
right, the face is a thin signal for feeling. If the faciality argument is right,
**the readable face is an artifact of the same apparatus that reads it**, the
training corpus is that apparatus's output, and a high accuracy score partly
measures how thoroughly the apparatus has already done its work.

## §11.7, the research question changed

The old question was the skeptical form of the accuracy question — *whether any
face-to-feeling mapping survives once individual and cross-cultural variation are
taken seriously, under what constraints, and against what error rate*. **It asks
how good the instrument is.** It now says so about itself and asks the other one:
what the instrument measures distance from, who put that there, and what a
deployment does with the ordering it gets back. **The instrument is not a neutral
way of finding out whether emotion is legible from a face. It is the politics,
already built.**

**The near-term work becomes an audit of the registration step rather than of the
output.** Publish what the system aligns to — the reference model, or the summary
statistics of the corpus it was fit on — and report error disaggregated by
distance from that reference rather than only by the named group of the person
read. **Two things follow that a group-wise table does not supply.** Distance is
continuous, so the claim is falsifiable in a way a comparison between categories
is not: **if error does not climb with distance from the reference, §2.2.1 is
wrong about that system.** And a published reference is contestable in a way an
error rate is not — a vendor can accept a disparity finding and answer it with
more data, and cannot answer a published reference face except by choosing a
different one and saying which.

**The old proposal is kept and demoted rather than cut.** The in-group advantage
is the part of the accuracy question already shaped like a relation rather than a
property, and its falsifier still runs in the system's favor. **The data problem
now applies to both halves**: an in-group advantage is a relation between reader
and read and the corpora record only the subject, and a reference model is a
thing no vendor has had a reason to publish.

## Citations

**No new bibliography entry.** All three sources were already in the book. Three
notes were extended, under the author's standing condition that anything added is
verified by web research.

- **`deleuze1987plateaus`** now records Plateau~7, *Year Zero: Faciality*, pages
  167--191 — a third use of an entry already carrying Plateaus~9 and~13. **The
  quoted sentence at page 178 was checked against two independent scholarly
  sources quoting it identically.** The related claims that the face is not
  universal but is White Man himself, and that the face is a politics, **are used
  in paraphrase and cited to the plateau rather than to a page**: secondary
  sources place them variously and the pages were not verified. The note says so.
- **`buolamwini2018gender`** now carries the two figures as the paper's own, the
  Pilot Parliaments Benchmark, and the binary-label and Fitzpatrick limitations
  **recorded as the authors' statements rather than as an objection raised here**.
- **`taigman2014deepface`** now records both of its uses and the alignment stage
  in detail. **Cited without a page locator**, the alignment description being
  section-level in the paper rather than a passage.

## What was not done

- **§2.2.1 keeps its title.** *What Emotion Is, and What a System Reads* still
  fits — what a system reads is precisely what the rewrite puts in question — but
  a retitle is a separate operation that syncs `ORDER.tsv`, `outline.tsv`,
  `ledger.tsv` and the TOC, and was not asked for. **§11.7's title, *Is Emotion
  Legible From a Face at All?*, is now in tension with its own closing
  paragraph**, which says that is not the question. Flagged, not changed.
- **§12.1 was not edited.** Its line about a system *measuring them against a norm
  they were never going to match* is the deployed instance of this argument and
  reads as one now; §2.2.1 points forward to it, which is enough without a
  reciprocal edit nobody asked for.
- **§6.1 was not edited.** §2.2.1 concedes its case explicitly and by name.
- **`style.md` §4b cites "the mirror-neuron overshoot in §2.2.1" as the model for
  a box.** There is no box in §2.2.1 and there was none before this pass. **That
  reference in the style guide is stale** and was left alone; shared tooling and
  documentation are not this pass's scope.
