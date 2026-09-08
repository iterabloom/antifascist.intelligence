# P128 — the one sentence that outran the book, and two italics the importer let through

## Instruction

*"What do you think of the following feedback?"* on a note titled **State that the
patienthood conclusion is unfalsifiable, and defend it as the design**, then *"Please first
check your assumptions and then make the needed revisions."* The note asked for the
asymmetry §3.3 draws to be moved to the front of §3.4 and named as the argument's design
rather than left as its residue, on the ground that a reader who assembles it from three
passages *feels handled*.

## The note's reading is accurate and its remedy inverts the defect

Both structures the note describes are on the page verbatim: §3.3:83 distinguishes the
routing claim from the patienthood conclusion in those terms, and §3.4:66 closes the
phenomenal-experience escape by observing the negative verdict is *available to nobody*.
Birch is cited, at §3.4:62 and §9.3.1:7.

**But the book does not hold that the conclusion is closed to evidence.** One sentence
does, and it is the only one in 133 sections:

> The patienthood conclusion cannot be held as provisional, because no result is coming
> that would revise it. — `03_03.tex:83`, P117 (`e444fdd`, D-215)

It contradicts four things, three of them inside chapter 3.

1. **`03_03.tex:79`, four lines above it**, on the same middle conjunct: *Neither is close
   to settled. Both are questions somebody can work on.*
2. **`03_03.tex:75` and `03_10.tex:39`**: building the counterexample takes *the
   patienthood conclusion* off. Line 75's clause entered at P35 (`b015856`), long before
   P117, and **`p117-scope.md` affirms it in P117's own words** — *on the repaired account
   the patienthood conclusion does then go.*
3. **`03_02.tex:31`** (P85, D-167): *the argument from suffering reaches the same
   precautionary conclusion, now resting on a question somebody could make progress on.*
   And **`03_02.tex:19`**, whose clause *which interpretability can bear on* is **the
   author's own Overleaf edit of 2026-09-08**, checked against the `59f8f9b` diff rather
   than inferred from `git log -S`: the paragraph previously ended at *those are one
   question and not two*. It is the most recent authorial sentence on the question and it
   is on the open side.
4. **`11_02.tex:60`**, which names an experiment whose negative result *closes the only
   proposed route* and whose positive one *gives a guardian something to read*;
   **`12_02_01.tex:15`**; and **chapter 11's own stated standard at `11.tex:11`**, which
   forbids this move in terms — *the claim is bounded: I looked for published work under a
   particular description and did not find it, which is weaker than no such work existing.*

**The verb that reconciles everything else is *settle*.** §3.2:19 (*no inspection settles
the question*), §3.3:83's first half (*the conjunct no instrument settles*), §3.10:35 and
§11.1:22 all say nothing settles it, which is compatible with interpretability bearing on
it. Only *revise* and *cannot be held as provisional* overshoot, and they are claims about
the future rather than about available instruments. **§3.10:35 needs no repair.**

**Adopting the note's label would reverse D-167**, whose recorded gain was relocating the
uncertainty from metaphysical to evidential so the load-bearing claim would stay
falsifiable. **And it would go against Birch**, whom the note names as the structure: the
book's own paraphrase, in both places, is that candidate status *governs what precautions
are owed rather than waiting on a verdict nobody can deliver* — a framework for acting
while a question is open, not for closing it.

**The repaired sentence is P117 drafting and not the author's finding.**
`p117-scope.md`'s account of finding (d) and D-215's row both stop at the asymmetry and
name neither *provisional* nor *no result is coming*; the `e444fdd` diff added the whole
paragraph as one block. Checking that first is what separates this from P127, where the
sentence in the way turned out to be an author-confirmed ruling that had to survive.

## Two corrections to the account already given the author

1. **§3.4 needed nothing, and I had said it needed a pointer.** I told the author §3.4
   states the conclusion without naming its epistemic status and that one sentence would
   close it. `03_04.tex:75` already carries the correct deadline-indexed form — *on
   evidence that will not resolve further before somebody has to decide whether to build
   one* — as the section's last sentence, and `03_04.tex:62` carries Birch's precaution
   vocabulary. **Reading the section for the edit is what found that the edit was not
   needed.**
2. **Q-082 is a rewrite and not a compression.** The question records two dropped clauses.
   The `3acef1f` diff shows the author rewrote §3.10's closing paragraph: *anybody has an
   instance of* → *anyone has \emph{definitely} reproduced*, *\emph{in silico}* added,
   *what is owed to it* → *owed to them*, and the hedge *rather than a ruled-out one*
   dropped alongside the two clauses. Restoring them would undo an authorial rewrite of
   chapter 3's last sentence, which is a different act from restoring a deletion. **Closed
   on default (a) by the author's answer, with that finding on the record.**

## A sixth P126 import defect, of a class already documented

The same rewrite left **two `\textit` at `03_10.tex:41`, the only two in the manuscript.**
`style.md` §8 states the rule (D-189, applied again at D-197), names this exact
mechanism — *Edits made in Overleaf come back with `\textit`; convert them on import* —
and records that it has happened twice before, eight instances and then twelve, **caught by
reading and not by any check.** It compiles, so the build does not see it either. This is
the third import and the third recurrence, and `overleaf.py` still has no conversion step;
grep for `textit` in it returns nothing. Q-087.

That makes six defects from the P126 round trip rather than five, and **four of the six
were invisible to `check_all.sh`.**

## The two edits

### 1. `manuscript/sections/ch03/03_03.tex`, line 83

> The patienthood conclusion cannot be held as provisional, because no result is coming that would revise it.

becomes

> The patienthood conclusion cannot be held open for a result, because the decision falls due first.

*Held open* against the next sentence's *held as settled* is a tighter parallel than the
original had, and it keeps P117's verb. The paragraph's design is a statement followed by a
two-sided recap — the routing-claim sentence recaps a sentence four earlier in the same
way — so compressing *a question that will still be open when the decision has to be made*
into *the decision falls due first* is the recap doing its job rather than a repetition.
**The wording deliberately avoids §3.4:75's and §12.3's phrasings of the same timing
point**, both of which say it at length; P126's finding was two near-identical runs
surviving the suite, the build and a first read.

**The first draft was *cannot be deferred to a result*, changed on the second read.**
*Defer to* carries the yielding sense, and *held open* recovers the parallel.

### 2. `manuscript/sections/ch03/03_10.tex`, line 41

`\textit{definitely}` → `\emph{definitely}`, `\textit{in silico}` → `\emph{in silico}`.

## What was not done

- **§3.4 is not edited.** See correction 1.
- **§3.10's two clauses are not restored.** Q-082 on (a), the author's answer.
- **§3.2:17 and §12.2.1:13 are not repaired.** *The only gap in the chapter that an
  inspector can work on at all* sits against §3.2:19's *which interpretability can bear on*
  two paragraphs later. The author's 2026-09-08 sentence created the tension and he left
  line 17 alone; reading *an inspector* there as the behavioral one is an authorial
  judgment about which instruments count, not a repair. Q-086.
- **`overleaf.py` is not modified.** Q-087 asks; the tool is left alone.
- **Q-085 does not fire.** It applies at the close of the next pass touching chapter 2, and
  this pass touches only chapter 3.
- **§3.10 was read only at the passages named**, and nobody has read §3.3 or §3.10 end to
  end. §3.2 and §11.1 were read whole for this pass; §3.3 and §3.4 were read whole in the
  turn before it. That stands beside the 18 sections P126 left unread.
- **No proof pair was built.** The PDF went to the scratchpad for measurement, so the
  committed 2026-09-08 pair is one pass behind and the README points at it.

## Figures

133 sections unchanged, 2 changed. **97,996 → 97,995 words (−1)**; 194 pages unchanged; 17
overfull boxes unchanged; 0 undefined references and citations; 320 bibliography entries
unchanged; 224 cross-references unchanged; zero `\textit` in the manuscript; suite green.
