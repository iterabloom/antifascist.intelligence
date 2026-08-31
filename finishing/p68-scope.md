# P68 — §7.3's re-introduction of jury learning deleted, and the repetition census verified

**The author's instruction.** Of the eight repeated cases in the census, the §7.3
re-description of jury learning is the most fixable: §7.2 introduces it in full
and §7.3 introduces it again a page later — *“The clearest existing version is
jury learning, which predicts how each individual annotator would label an item…”*
— before making the point that actually matters, which is that representing a
split is not the same as being movable by it. **Delete the re-introduction and
start the section at the claim.**

## The instruction, and the one dependency it did not name

The re-introduction is the second sentence of §7.3's opening paragraph, and it is
close to verbatim on §7.2's — *predicts how each individual annotator would label
an item*, *lets a practitioner see how the verdict shifts depending on who is
empaneled*, and the same `\autocite{gordon2022jury}`. It is gone, along with the
two sentences after it: *“That is a real advance over a single fixed ground truth,
and it is not sufficient”* — which §7.2 already says in its own words — and *“The
gap is where the research is,”* an announcing sentence of D-117's class.

**The first sentence had to stay, and this is what reading for it turned up.**
Three run-ins later the section says *“What both instances lack is what
section~\ref{sec:9.3.5} treats as the only reliable discriminator.”* **Its
antecedent is the opening sentence** — *“Two instances of one structure invite
one fix”* — and nothing else in the section supplies one. Deleting the paragraph
whole would have left *both instances* pointing at nothing, three paragraphs
downstream and invisible from the edit site.

So the sentence moved under the run-in head rather than going with the rest, and
the section now opens on the claim:

> **Representing a split is not the same as being movable by it**
> Two instances of one structure invite one fix, and the fix that suggests itself
> is representation: stop collapsing disagreement, model it instead. **Jury
> learning does that, and it does not give the disagreeing party any purchase on
> the scheme they are disagreeing inside.**

*“Jury learning does that”* is a reference and not a description: it names the
method and says nothing about how it works, which §7.2 has just finished
explaining one page earlier.

**§7.3 now opens on a `\runin` head.** One other section in the book does — §5.1.1,
under *Three kinds of reasoning, and not three ages*. The pattern exists and this
is the second instance of it.

**Nothing was orphaned.** The deleted `\autocite{gordon2022jury}` was the second
of two; §7.2 still carries the first, so `refs.bib` is unchanged.

## The census, verified against the current tree

**The table is in pre-P64 numbering**, and three passes have moved chapter 6 since
it was taken. The maps are `renumber-map_2026-08-31d.tsv` (P64), `_e` (P65) and
`_f` (P66). Translated and re-counted:

| Case | The table | Current | What changed |
|---|---|---|---|
| Amazon résumé tool | 2 — §6.1.2, §6.3.5 | **1** — §6.3.3 | **P65 cut §6.1.2** *Ensuring Fairness and Equity*, which held the first telling, and moved its Reuters citation into the surviving narration. **Already fixed.** |
| COMPAS | 3 — §6.1.1, §6.1.3, §6.3.5 | **3** — §6.1.1, §6.1.2, §6.3.3 | §6.1.3 → §6.1.2 at P65. Count holds. |
| ACLU / Rekognition | 2 — §6.1.1, §6.3.5 | **2 — §6.1.1, §9.1.2** | §6.3.3 does not re-tell it. **§9.1.2 is the second telling and the table does not list it.** |
| PredPol | narrated twice | **1 telling + 1 pointer** | §6.1.1 tells it; §6.3.3 points. |
| Clearview AI | 2 — §6.4.3, §9.1.2 | **2**, confirmed | Plus a glossary entry. |
| Jury learning | 2 — §7.2, §7.3 | **1** | This pass. |
| Jacobs & Canedy | 2 — §6.3.6, §8.3.3 | **2** — §6.3.4, §8.3.3 | §6.3.6 → §6.3.5 at P64 → §6.3.4 at P66. |
| HireVue / 0.25 percent | 2 — §11.8, §12.1 | **2**, confirmed | |
| vTaiwan | 5 mentions in 4 places | **5 in 5 files** — §5.4.2, §8.2, §8.2.1, §12.1, §12.2.2 | §8.2.1 is the old §8.2.2, renumbered at P66. |

### Three findings the recount produced

**The opening premise is now true of one case out of four.** The instruction says
§6.1.1 narrates COMPAS, Amazon, PredPol and Rekognition and §6.3.5 narrates the
same four again, re-explaining what each case was. Against the current text:
§6.1.1 narrates COMPAS, PredPol and Rekognition and **does not narrate Amazon at
all** — §6.3.3 holds Amazon's only telling, which is a first telling and not a
second. Of the three that do appear in both, **§6.3.3 re-describes only COMPAS**,
and in one apposition: *“the recidivism-scoring tool a Wisconsin court let its
maker keep secret even from a defendant sentenced partly on its output.”* The
ACLU and PredPol cases arrive there as *“Section~\ref{sec:6.1.1} covers two
more”* plus one clause each, which is the shape the instruction is asking for.

**The two Rekognition tellings are two different studies, not two tellings of
one.** §6.1.1 is the ACLU's 2018 test of every sitting member of Congress against
a database of arrest photos, 28 false matches disproportionately of non-white
members \autocite{snow2018amazons}. §9.1.2 is an MIT Media Lab audit finding
higher error rates for darker-skinned and female faces, used to make a different
argument — that Amazon's own self-regulation did not catch it and an
uncommissioned outside audit did \autocite{raji2019actionable}. **Same system,
different finding, different citation, different work.** Cutting either loses a
result rather than a repetition.

**§8.3.3's Jacobs and Canedy mention is a pointer that restates the finding, not
the case.** It says *“Section~\ref{sec:6.3.4} reports an evaluation of the main
American channel for retraining displaced workers against twenty-three million
participation records,”* gives the result, and cites `jacobs2026wioa` a second
time — in service of an argument §6.3.4 does not make, that the evidence supports
a jobs guarantee. The researchers are not named twice. **This is the weakest of
the eight rows as a repetition claim.**

## Figures

**94,894 words**, down **55** on P67's 94,949. §7.3 goes **1,116 → 1,061**; no
other section touched. **136 sections**, unchanged. All `\ref{sec:}` **unchanged
at 551**, the glossary unchanged at 116, `refs.bib` unchanged at **304** — the
deleted citation was a duplicate. 0 undefined references, 0 undefined citations,
`check_all.sh` green.

## Not done

- **The other seven rows of the census were counted and not acted on.** The
  instruction names §7.3 as the most fixable and asks for that one. Two of the
  seven — Amazon and jury learning — are now at one telling each, the first by
  P65 and the second by this pass.
- **The committed proof pair is stale after P66, P67 and this pass**, and its page
  figure is wrong: it says 190 and the book was 189 before this pass.
- **One ledger row tagged D-149**, `drafted` already. **2 `accepted`, 134
  `drafted`**, unchanged.
- **The census counts files and passages, not judgments about which telling
  should go.** Where this file says a mention is a pointer rather than a telling,
  that is a reading of the passage, not a measurement.
