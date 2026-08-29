# P33 — the training pipeline, and the recuperation claim stated precisely

Two author instructions, 2026-08-28, recorded as D-097.

## Point 1: update and reorganize the technical chapters

**The instruction.** Chapter 4 is anchored in an earlier AI curriculum — neural-network
basics, CNNs, RNNs, BERT, IRL, transfer learning, GPT-3-era few-shot prompting. Transformers
appear; contemporary foundation-model training and post-training do not get a coherent
treatment. The book needs a compact account of the current pipeline: pretraining and
instruction tuning; preference optimization beyond classical RLHF; model-generated feedback
and constitutional approaches; process versus outcome supervision; scalable oversight;
interpretability and evaluation; deployment-time system instructions and tool use. Some later
sections mention newer work and it needs to be in the building chapters.

**The diagnosis measures worse than the instruction states it.** Across all 162 sections
before this pass, the following appeared **zero times**: "Constitutional AI", DPO or direct
preference optimization, instruction tuning, foundation model, system prompt or system
instruction, chain-of-thought, process supervision or process reward. "RLHF" appeared in three
files — section 7.2, section 11.5, and the glossary. "Scalable oversight" appeared in sections
11.5 and 12.2.2. Interpretability vocabulary appeared in section 11.1 alone. "Pretrained"
appeared once in the body, in section 4.1.3's few-shot paragraph. Every modern reference in the
bibliography — Christiano, Irving, Burns, Sharma, Lindsey, Qi, Tamirisa — was cited from chapter
11 or chapter 12. The building chapters carried none of it.

**What was done.** Section 4.2 is rebuilt as the production pipeline in the order its stages
run, and retitled from *Aligning AI Systems with Humane Values and Antifascist Principles* to
*How a Deployed System Acquires Its Values*. Nine subsections against four. The four classical
methods are kept and relocated to where they bite in a modern pipeline rather than appended to
it, which is the difference between reorganizing and adding a section.

| new | was | what it is |
|---|---|---|
| 4.2.1 Pretraining and Instruction Tuning | 4.2.3 Supervised Learning | the aggregate argument, Moral Machine and the unsupervised paragraph carried whole; pretraining and instruction tuning are new |
| 4.2.2 Preference Optimization, and Who Holds the Pen | 4.2.1 Reinforcement Learning | reward hacking, the non-transfer of a reward, regularization and the exploration paragraph carried; comparison-based reward and DPO are new |
| 4.2.3 Inferring the Objective: IRL and CIRL | 4.2.2 | prose unchanged but the opening pointer; retitled |
| 4.2.4 Model-Generated Feedback and Constitutional Approaches | — | new |
| 4.2.5 Process and Outcome Supervision | — | new |
| 4.2.6 Scalable Oversight | — | new |
| 4.2.7 Interpretability and Evaluation as Instruments | — | new |
| 4.2.8 System Instructions and Tool Use at Deployment | — | new |
| 4.2.9 Transfer, and the Floor That Cannot Tell It Has Stopped Applying | 4.2.4 | prose unchanged but the opening sentence; retitled |

`renumber-map_2026-08-28d.tsv` is the map. Ten inbound references were read by hand and
repointed; none of them changed meaning, because each pointed at content that moved as a unit.

**Every stage is taken twice**, on the chapter's existing method: what it does, and whether
what it does could produce a commitment that survives its own teacher. Five of the new
subsections make an argument the book could not previously make.

- A **constitution** is section 3.1's first branch in production: a constraint written down,
  held by a party, revisable between runs. Its real gain is legibility — a constitution can be
  published, versioned and argued with, which a reward model fitted to a hundred thousand
  comparisons cannot — and legibility is not durability.
- **Model-generated feedback closes chapter 7's loop.** The judge of the next round is an
  artifact of the previous averaging, so the party whose disagreement was collected is absent
  from the channel entirely.
- **Process supervision** is the first stage in the pipeline that addresses chapter 3's
  distinction between a reason held and a result produced, which is the strongest evidence in
  the chapter that the distinction is engineering. Section 11.1's finding on self-report is
  its ceiling: what gets supervised is the reasoning the system states.
- **Scalable oversight** is section 3.3's control relation engineered to survive a capability
  gap, and the same instruments serve a floor when the judge is not the operator — chapter 11's
  one condition, arriving from a new direction.
- **Interpretability cuts both ways.** Sections 4.1.1 and 4.3 rest on a commitment being hard
  to locate; features recovered at production scale can be steered, so the research that
  threatens the floor's obscurity is the only research that could verify a floor exists.
- **The system instruction** is the most editable floor in the pipeline, and section 3.1's
  objection is literal against it. Tool use moves the refusal from speech to action.

**Nine citations added and verified live**, C0751–C0759 in `claims.tsv`: Ouyang 2022, Rafailov
2023, Bai 2022, Wei 2022, Uesato 2022, Lightman 2023, Templeton 2024, Perez 2022, Schick 2023.
Anthropic is named for Constitutional AI because the paper's own correspondence address
confirms it. Three other affiliations are **not** named in the prose, because an automated
summary attributed the Uesato, Perez and Schick papers to Anthropic and the author lists do not
support it; the near miss is recorded in the claims rows. One bibliography defect found on the
way: `irving2018ai` and `irving2018aisafety` were duplicate entries for the same paper, cited
from sections 11.5 and 11.6, and would have printed twice in the References. Merged.

**Chapter 5 was not restructured.** Every item on the author's list is chapter-4 material.

## Point 2: reframe the RLHF argument in chapter 7

**The instruction.** The chapter says disagreement is collected and "moves nothing." That is
too strong: individual ratings do affect the aggregate reward signal. What disappears is the
disagreement's provenance, persistence, minority structure, and capacity to challenge the
question or taxonomy. Framing it as distribution collapse and agenda control would make the
recuperation analogy harder to dismiss.

**The correction reaches the definition, not only section 7.2.** Section 2.1.4's first
structural feature ended "The tell is that the mechanism exists, is used, and moves nothing,"
and section 7.1 had already stated the accurate version one stage upstream — "a channel that
collects judgment at scale and is built so that judgment about the channel itself moves
nothing." The imprecise form stood at six sites: the definition, its restatement in chapter 7's
opener, chapter 7's opener again on the reward stage, section 6.1.1, section 7.2, and the
glossary.

**The precise version is also the more faithful one.** Debord's argument, which section 2.1.4
already cites, is that dissatisfaction is sold back as a commodity of opposition — the dissent
is put to work, and what it works for is the arrangement it was aimed at. Recuperation was
never the claim that a mechanism does nothing. So the tell is now where what the mechanism
carries stops: the channel works, the institution uses what comes through it, and the judgment
that the frame is wrong has nowhere to go.

**Section 7.2 states the four losses.** Every rating moves the reward model, and the section now
says so before it says anything else. What the compression removes is provenance (a comparison
arrives without the standpoint that produced it), persistence (a stable split and random rater
noise enter the fit identically and leave as variance around a mean), and structure (a coherent
minority position becomes a small displacement of the majority direction). The fourth was never
collected: a rater judges which of two responses is better and has no output for saying that
neither is acceptable, that the pair is malformed, or that the question presupposes something
false — which section 7.3 had already named as the fix without the diagnosis being stated this
way.

## Measured

Book 91,116 to 94,001 words; chapter 4 from 5,882 to 8,320, chapter 7 from 3,718 to 4,117.
167 sections from 162. 193 pages from 186. `check_all.sh` green on all seven; both formats build
with no undefined reference.

**Contrastive-negation density in the new and rebuilt prose is 1 per 167 words**, against
D-025's calibration of 1 per 345. Every instance was read. One was rewritten as cadence
(section 4.2.6's "a live research problem rather than a solved one"); the rest carry a negated
alternative that is doing work — the definition of process supervision, chapter 3's own "a
reason held rather than a result produced", the Casper paraphrase, the Burns result. The
measurement is recorded rather than swept to a number.

## Not done

- No section here has the author's read; all 15 changed or new rows are `drafted`.
- The proof pair was rebuilt from this tree after the pass and is current at 193 pages.
- `xref_content.py` was not run over the new material.
- Section 4.1.2 was not touched. It holds the one "convolutional" mention and one of the two
  "transformer" mentions, both inside a cognitive-science argument about feedforward-only
  processing that the chapter needs.
- Chapter 5 was not restructured, and section 4.2.3's carried prose measures 1 per 86 on the
  contrastive tic, which is pre-existing and was not swept.

## One half of the instruction's premise did not survive checking

The instruction described chapter 4 as anchored in an earlier curriculum: "neural-network
basics, CNNs, RNNs, BERT, IRL, transfer learning, and GPT-3-era few-shot learning." The
**absence** half is confirmed and then some, in the zero counts above. The **presence** half is
weaker than stated, measured across all 162 sections before this pass:

- **RNNs, LSTMs and recurrent networks appear nowhere in the book.** Not in chapter 4, not
  anywhere.
- **"CNN" appears nowhere.** "Convolutional" appears once, in section 4.1.2, as one clause
  supporting an argument about what a feedforward-only system gives up.
- **BERT appears only in the glossary.** The `devlin2018bert` citation in the transfer section
  is a bare `\autocite` with the name nowhere in the prose.
- IRL, transfer learning and GPT-3-era few-shot prompting were there as described, at sections
  4.2.2, 4.2.4 and 4.1.3.

That distinction changed the repair. An old curriculum crowding out a new one is fixed by
replacement; a hole is fixed by writing. Section 4.2 had four subsections and 1,858 words to
cover everything after pretraining, so the pass adds rather than displaces, and the four
existing arguments all survive because none of them was the problem. Section 4.1.3's few-shot
paragraph now says that in-context learning is the smaller half of how a deployed system comes
by its behavior, and points at section 4.2.1 for the stages that do the rest.
