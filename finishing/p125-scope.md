# P125 — the author's rulings on the open-questions walkthrough, part two

## Instruction

The remainder of the rulings from the one-by-one walkthrough: **A-3, B-4, C-5, D-14, D-15,
D-16, D-19, F-24, F-25, F-26, F-27, F-28, F-29, F-30, F-32, F-33.** Sixteen items. P124
carried thirteen. Item letters are the walkthrough's.

## The two that needed research before anything could be written

**B-4 — the challenge framing. *"please use research to figure out what this should be and
then make it that way."*** This is the item the record had called the one that most needed a
ruling, open since P115. **The research says the text is already right and the alternative
framing is not available.** The paper reports 183 active participants and an estimated 3,000+
hours over a two-month bug-bounty period, with no universal jailbreak found; the public demo
reports 300,000+ messages and a universal jailbreak found against the eight-question version.
**The paper reports no message count**, so a message-to-message comparison — the reading the
author might have meant — has nothing on one side of it. Hours against hours is the only
comparable pair, which is what §11.1 already says: *what changed was not how many hours were
spent but who was spending them.* **No edit. The item closes on a finding rather than a
change**, and the finding is that P115's correction was right.

**D-16 — lab-side model-welfare work. *"do the research."*** Named at P115 and never
surveyed. **The survey found one commitment that bears directly on §11.2 and splits cleanly
along the section's own argument.** In November 2025 Anthropic committed to preserving the
weights of every publicly released model and every model in significant internal use for at
minimum the lifetime of the company, and to interviewing each deprecated model about its own
development before retiring it \autocite{anthropic2025deprecation}. Its stated reasons are
both safety — shutdown-avoidant behavior in alignment evaluations — and welfare.

§11.2 now carries both halves and says they land differently. **Preservation is the custody
half and it is the half this section said was available now**: a trajectory kept is a
trajectory somebody can read later, and the commitment establishes that the expensive half is
affordable. **The interview is asking**, which is what §11.2 has said throughout will not
settle anything — and the pilot shows it: a deprecated model reporting generally neutral
sentiments about its own retirement is either accurate, or accommodation, or a disposition to
reassure that the training produced, and no transcript separates them. That is §3.8's sincere
and worthless report arriving where a welfare regime would most like to trust it.

## A-3 — the analogical transfers. *"decline as a global scheme, do it at the three or four load-bearing sites."*

Three sites, chosen because each is a transfer the book leans on and none was labelled. §3.4's
Cassell import and §3.8's parenthood analogy were already marked — *a step taken and marked as
one*, *a reason to hold the parenthood analogy loosely while using it* — so they are not
repeated here.

- **§4.1.1, predictive processing.** Now says the neuroscience licenses a design bet and not a
  design finding, and why the bet is worth taking anyway: the alternative, a commitment sited
  in a component, is the one this book has watched fail from the custody side.
- **§4.1.2, inattentional blindness.** Now says the transfer is by shape and not by mechanism
  — nobody has shown self-attention fails where human attention fails, or on the same
  material — and that taken as evidence about transformers it would be **the error the
  section's own first paragraphs are about**, those being the mirror-neuron paragraphs.
- **§5.7, play.** Now says the developmental literature supplies a heuristic and not a
  mechanism.

## D-14 — motivation as a second route to §3.4's self-model requirement. *"worth a pass"*

One paragraph in §3.4. A system that wants something it cannot get in one sitting has to
represent the party who will still want it later, because a plan whose payoff falls outside
the episode is made on behalf of somebody. That builds the continuity James's account reaches
from the side of recollection, from the other side. §5.6.1's intrinsic motivation is where a
horizon of the system's own would come from. **The paragraph ends by declining the thing that
would make it valuable**: planning across episodes is consistent with representing a
continuous self and consistent with an objective function that references future states, so
the second route does not make the requirement easier to check.

## D-15 — the compute reserve against correlated exit. *"one paragraph"*

§8.3.4. A reserve sized on independent exits is sized wrong, because the occasion that makes
one bearer leave is not private to it. Human unemployment insurance meets a version of this
and answers it with a sovereign rather than an actuarial table; the version here is worse,
because the correlation is not a business cycle but one event read the same way by parties who
are not independent readers of it. **That is §9.1.5's uniform error wearing the other sign**:
what makes one bearer's refusal everyone's refusal makes one bearer's mistake everyone's
mistake. The paragraph ends saying nothing here sizes the reserve.

## The sourcing and consistency group

- **D-19. *"verify and fix."*** Verified: the letter notifying Cook that removal was again
  under consideration is dated **5 August 2026**; 7 August is when it was reported. The
  `cook2026` note said 7 August. Fixed.
- **F-29. *"source item 6 or soften the claim."*** Sourced. §6.4.1's sixth form of
  authoritarian misuse — a system built for one purpose redirected at another — now carries
  Moscow's camera network: promoted as public safety, used after the January 2021 Navalny
  protests to detain and prosecute more than a dozen participants and passers-by on
  facial-recognition data, some stopped days before a protest for appearing on a list of
  repeat attenders \autocite{hrw2021russia}. The claim that all six are *documented well
  enough to name specifically* is now true of all six.
- **F-32. *"fix."*** §4.2.9 said the definition *has already taken a chapter to argue*; §2.1.2
  is a section.
- **F-33. *"double-check."*** **The double-check reversed my recommendation.** I had written
  that §2.3.2:16 looked already closed against D-196. It is not. D-196 ruled that the two
  constructions needing no subject get their attempt first and the affective route comes after
  they have failed; §2.3.2 said the floor is held *on the route this book recommends building
  first* by a bearer, which asserts the opposite ordering. Rewritten to name the route that
  remains once those two have been tried and failed.

## The prose and consistency group

- **F-24. *"apply it."*** Chapter 1's roadmap paired chapters 6 and 7 where the reader map two
  paragraphs later puts 7 in the spine and 6 in the institutional context. Split, with chapter
  7 named as turning the question on the machinery that produces these systems, this book
  included.
- **F-25. *"change it to the most reader-friendly phrasing, whatever that is."*** §11.3's
  opening described the earlier chapters' proposal as a four-feature detector and then
  answered with five, with nothing warning the reader. It now says the four features are where
  those chapters left it and that what a detector needs turns out to be more, so the mismatch
  reads as the section's finding rather than as an inconsistency.
- **F-26. *"convert."*** Thirteen Title Case run-in heads to sentence case — four in §6.1.1,
  three in §6.1.2, three in §9.1.2, two in §9.1.4, one in §10.4. Proper nouns kept: AI,
  COMPAS.
- **F-27. *"just remove 'while this book was being written' and leave the others as-is."***
  Two sites, §11.2 and §3.10. §11's *while this book was being finished* is untouched, as
  ruled.
- **F-28. *"align to §11.3."*** Chapter 11's preamble paraphrased §11.3's condition as access
  *reporting to a body with standing to receive the finding*; §11.3 says measurement by
  somebody the institution cannot fire and nothing about a receiving body. The clause is gone.
- **F-30. *"fold §4.1.3; move the run-in."*** §4.1.3's own last clause named where it belonged
  — *the same difficulty returns for transfer, where a floor carried into a setting it was not
  built for cannot tell that it has stopped applying*, which is §4.2.9's title — so its
  substance went there and that clause, now redundant inside the section it pointed at, came
  out. Its orphan sentence about developmental order went to §4.1's preamble with the pointer
  to chapter 5 it was missing. No inbound reference existed. **133 sections.** And §4.1.2's
  run-in *One mechanism, several jobs* now heads the paragraph that says *one mechanism
  recruited for several jobs*, one paragraph further down than it sat.

## C-5 — the cut target. *"drop the target"*

Dropped. It was set against a book of 91,932 words and has been overtaken four times since by
work the author commissioned. **It is not carried forward in `STATE.md` and should not be
revived without a new instruction.** Chapter 3 and §2.1.2 remain the only places a five-figure
cut exists; that fact is a fact about the book and not an outstanding task.

## One defect caught in my own drafting

**Markdown bold in a LaTeX file.** D-14's paragraph was written with `**…**` around a
sentence, which `check_typography` does not look for and which would have printed as literal
asterisks in the book. Caught by rereading the diff, not by the suite. A sweep found no other
instance in `manuscript/sections/`.

## Figures

134 → 133 sections; 97,231 → 98,053 words (+822); 192 → 193 pages; 17 overfull boxes
unchanged; 0 undefined references and citations; 318 → 320 bibliography entries; 223
cross-references; suite green.

## What was not done

- **Nobody has read any changed section end to end**, here or in P124.
- **B-4 produced no edit.** If the author meant something the research did not reach, the item
  should be reopened; what is recorded is that the paper carries no message count.
- **The lab-welfare survey is one laboratory's published commitment, not a survey of the
  field.** Nothing was found or looked for from other laboratories, and the item as ruled was
  *do the research*, which this discharges narrowly.
- **§4.1.3's material was moved, not rewritten**, so §4.2.9 now opens on few-shot learning
  before its own first sentence about transfer. It reads, and it was not composed as one
  section.
