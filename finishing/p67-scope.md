# P67 — §4.1.1's scaffolding cut, §4.1.3's generic description compressed

**The author's findings.** §4.1.1 spends its first ~150 words setting up ACT-R
against Society of Mind in order to dismiss the comparison as a category error;
the section's actual content is the predictive-processing bet and its payoff, and
the two architectures are scaffolding for a point made in one sentence without
them. §4.1.3 describes few-shot learning generically for two-thirds of its
length, the live material being the evaluation problem and the pointer to
transfer; compress by half.

**Both hold.** §4.1.1's setup measures **150 words** on the nose — 90 in the
opening paragraph that names both architectures, 60 in the box paragraph that
dismisses the comparison. §4.1.3's generic description is paras 1 and 2, **212 of
its 399 words**, which is closer to a half than to two-thirds; the finding's
proportion is the reading experience rather than the count, and the identification
is exact either way.

## §4.1.1

### The one sentence was already in the text

*“neither a pipeline of modules nor a swarm of independent agents.”* That clause
draws the contrast the two architectures were named to draw, generically, and it
opens the paragraph that survives. **Nothing had to be written to replace them.**

### The box had to be dissolved, and this was forced rather than chosen

`\boxtitle{Which picture is right?}` is a question about ACT-R against Society of
Mind. With them gone the title has no referent, and what the box held — the
free-energy account and its engineering consequence — **is the section's main
line, not an aside.** Leaving it boxed would have left a 75-word section body
with 230 words of sidebar under it.

The environment's use elsewhere confirms the reading: `esbox` carries factual
sidebars off the main argument — §6.1's data-center energy and water figures,
§6.4.1 twice, §5.1.1, §10.5. **The book now has 5 boxes in 4 files where it had
6 in 5.** This is the one change in the pass that the instruction does not name;
it is a consequence of the cut, not an extension of it.

### The payoff is load-bearing in both places named, and one route does not run through §4.1.1

- **§4.2.7 quotes it back directly**: *“The positive result reported earlier was
  that a commitment realized as a standing bias on what a predictive loop treats
  as an error worth correcting is not a component that can be located and
  removed.”* That is §4.1.1's closing paragraph, and it is the sentence the whole
  interpretability argument turns on.
- **§3.8 reaches the same property through §4.1.2, not §4.1.1**: *“The floor as
  section~\ref{sec:4.1.2} describes it — a goal representation with the standing
  to bias every competing process, which that section says has no location to
  attack.”* §4.1.2's *Control without a controller* run-in carries that in its own
  words.

Both survive untouched. **Neither points at §4.1.1**, which is why the cut needed
no reference repair: the only inbound reference §4.1.1 has is the glossary's
*Predictive coding* entry, and that entry describes what the section is now more
purely about, not less.

### Two citations orphaned

`anderson2007human` and `minsky1986society` were cited only here and moved to
`unused_bibliography.bib`. **Checked against P65's reverse finding**: ACT-R and
Society of Mind are now named nowhere in the manuscript, no glossary entry points
at either, and no surviving claim is left holding an attributed idea without a
source.

### Two checks, both clean

- **Neither parent promised the architectures.** §4.1's opener names perception,
  memory and attention. Chapter 4's opener describes this part as *“what a system
  needs in order to perceive, remember and attend to a situation at all, and how
  much of human cognition is a usable model for that rather than a metaphor
  borrowed for color.”* No repair at either level, which is the check P66 had to
  run one level above the parent.
- **No section outside chapter 4 refers to the cut material.**

### Two things flagged and not changed

- **The title.** *Cognitive Architectures: Integrating Knowledge, Memory, and
  Reasoning* was written for a section that compared two architectures. It still
  fits — one loop integrating knowledge, memory and reasoning is exactly the
  claim — but it now names a plural the section no longer has. **One word from
  the author changes it.**
- **A pre-existing dangling demonstrative.** The closing paragraph ends *“a trade
  taken up there at the point where it becomes a claim about what not to build.”*
  *There* has no antecedent in its own paragraph and resolves only to §4.1.2,
  named two sentences earlier. **That was true before this pass and is equally
  true after** — the cut neither created nor worsened it — and repairing it means
  rewriting a sentence the finding does not name. It is D-117's class.

## §4.1.3

**399 → 225 words, which is 44 percent and not the half the instruction
estimates.** The figure is reported rather than the estimate, which is what D-101
did when the author put §8.3.3 at half and the pass reached 57 percent.

### What stopped it at 44 percent

**Four glossary entries depend on the generic description.** *Few-shot learning*
locates at §4.1.3 and nowhere else. *MAML*'s own text says *“The technique itself
is not named in the text; §4.1.3 introduces the family it belongs to.”* *Transfer
learning and domain adaptation* locates at §4.1.3 and §4.2.9. And `brown2020fewshot`
is cited only here, for the result the *GPT-3 and GPT-4* entry describes — a task
performed from a handful of prompted examples with no parameter update.

Cutting the description to nothing would have left four glossary entries pointing
at a section that no longer says what they say it says. **This is the same class
as P65's finding**, reached from a third direction: there a cut severed a claim
from its citation, at D-123 from its correcting cross-reference, and here it
would have severed a definition from the passage it is a definition of.

### What went

The two deployment illustrations — disaster recovery working from a handful of
precedents, and a system flagging authoritarian speech patterns extending to new
phrasings and languages. The restatement of few-shot's appeal for an ethical
system, which said twice what the opening sentence says once. The aside that
prompting is now *“the smaller half of how a deployed system comes by its
behavior,”* the tuning stages doing the rest. And the three-stage enumeration
inside the developmental-arc sentence, which is now reduced to its pointer and
says where rather than what, per `style.md` §7.

**The evaluation paragraph is untouched, every word of it.** That is the live
material the finding names, and compressing around it rather than through it is
the whole shape of the pass.

### What was lost, named rather than repaired

- **The comparative claim about where a deployed system's behavior comes
  from** — that few-shot prompting is now the smaller half and the tuning stages
  do most of it. §4.2 is that pipeline and chapter 4's opener frames it as such,
  so the frame survives; **the explicit comparison does not appear elsewhere.**
- **The two deployment illustrations.** Neither is a claim and neither is used
  again.
- **The developmental arc's three stages.** §5.1.1 carries the stage theories,
  and its opening run-in is titled *“Three kinds of reasoning, and not three
  ages”* — the pointer that survives is a hedge against the section it points at,
  which is why the sentence was kept rather than cut with the rest.

## Figures

**94,949 words**, down **336** on P66's 95,285 — §4.1.1 465 → **303**, §4.1.3 399
→ **225**, and nothing else in the book touched. Chapter 4 goes 7,287 → **6,951**;
the 7,287 is P66's, one word above the 7,286 this session opened on, P66 having
added a word to §4.2.2's repointed sentence. **136 sections, unchanged.** **189
pages**, down 1 from 190.

All `\ref{sec:}` **unchanged at 551**, the glossary **unchanged at 116**: §4.1.1
kept its one pointer at §4.1.2 and §4.1.3 kept its one at §5.1.1, and neither cut
removed a reference. `refs.bib` **306 → 304**, `unused_bibliography.bib` **31 →
33**. `esbox` **6 → 5**, in 4 files rather than 5. 0 undefined references, 0
undefined citations, `check_all.sh` green.

Printed page 45 rasterized and read: §4.1.1 opening directly on *“The most
ambitious unifying account in contemporary computational neuroscience,”* with no
box, under §4.1's opener.

## Not done

- **The committed proof pair is stale after P66 and again after this pass**, and
  is now wrong on the page count as well: it is 190 pages and the book is 189.
  `pipeline.md`'s end-to-end verification line still reads 190 and is right as
  written — it records a run made against that pair, not against the current
  tree. I changed it to 189 in this pass and changed it back.
- **Two ledger rows tagged D-148**, both `drafted` already and neither moved
  status. **2 `accepted`, 134 `drafted`**, unchanged.
- **The predictive-processing account was not re-verified against Friston.** The
  paragraph is the manuscript's existing wording, moved out of a box and not
  rewritten; `friston2009freeenergy` travels with it unchanged.
- **§4.1.2 was read but not touched.** It is 1,663 words, by a wide margin the
  longest section in chapter 4, and it carries the same predictive-coding account
  at length. Whether §4.1.1 and §4.1.2 should both exist is a structural question
  this pass does not answer.
