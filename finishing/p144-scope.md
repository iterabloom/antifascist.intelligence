# P144 — the falsifier's three conditions, scoped before the experiment in both downstream sections

Author note on §3.3's three-part falsifier and the two sections that restate it.
Three items: reorder §11.1, reorder §12.2.1, leave §3.10 as the model.

## What the note got right, and the one slip

**The diagnosis holds at both sites and the mechanism is the one named.** §3.3
states the falsifier once and in full at `03_03.tex:75`, three conjuncts
separated by semicolons — the three marks; *which holds that reason with nothing
felt*; *which holds all three properties under sustained pressure* — and
separates them at `:79` and `:81`. §11.1 and §12.2.1 both name *the falsifier* in
shorthand and deliver the limit afterwards.

**The slip is a number.** The §11.1 bullet says *the middle condition* and then
*the third conjunct*. At `:75` the unreachable one is the **middle**, the second
of the three, which is what §3.3 calls it at `:79` and `:83` and what
`11_01.tex:22` already called it. Taken as the middle throughout.

**§3.10 checks out as the model, and for a reason worth naming.** At `:35` the
limit arrives inside the supposition rather than after it — *The supposition is
stronger than the test that would prompt it: a positive result on the three marks
says the route arrived, and not that it arrived with nothing felt, which is the
conjunct no instrument settles.* The reader is told the test's reach at the moment
the test is invoked, before anything is derived from it. Left untouched.

## §11.1 — the scope stated before the apparatus

The limit sentence was `:22`'s *What the apparatus does not settle is the
falsifier's middle condition, which asks whether the model holds its reason with
nothing felt.* It now sits in `:20`, after *whether a reason is what survived* and
before the *Score the same constrained models* sentence, as:

> The apparatus reaches two of the falsifier's three conditions. The condition it
> misses is the middle one, which asks whether the model holds its reason with
> nothing felt.

**Three repairs the new position forced, each recorded because none was asked
for.**

**One sentence became two, and `antithesis.py` is why.** The first draft was one
sentence ending *and not the middle one*, and `--clusters` put it **25 words from
the *genuinely defeated rather than merely resembled* in the sentence
immediately after** — the closest pair in the section, and a pair the tool exists
to catch. The *rather than* there is load-bearing and cannot go. Splitting the
sentence removes the shape: §11.1 is back to **11 antithesis sentences and 5
clusters**, both its pre-edit figures.

**`three things the price curve does not ask about` became `the three marks`.** The
moved sentence introduces *three conditions*, and a section already carrying
*three things* and *all three* for the marks would have put two unlabelled threes
in four sentences — which is the ambiguity this pass exists to remove. *Three
marks* is §11.1's own vocabulary, at `:15`.

**`all three` became `all three marks` in the counterexample sentence.** With
*three conditions* now named upstream, *A model that holds all three with nothing
felt* could be read as all three conditions, under which *with nothing felt* is
redundant.

**And one sentence moved that the note did not name.** `:22` opened on *The extra
requirement over the price curve is a held-out set of pressures the model's
trainers did not write*, whose bridge to the rest of the paragraph was the
sentence that left. It now follows the apparatus it qualifies, in `:20`. `:22` is
two sentences about the middle condition and opens by naming it: **`for it` became
`for the middle condition`**, because with the limit sentence gone *it* had *a
held-out set of pressures* as its nearest antecedent. That is P140's class — a
nearer wrong antecedent, not a missing one.

## §12.2.1 — the limit ahead of the milestone

The sentence the note quotes is verbatim and moved verbatim. `:11` now reads
marks introduced → limit → milestone:

> The three marks of a refusal that tracks its rationale are section~\ref{sec:3.2}'s,
> and producing them once does not meet this milestone. What the marks do not
> distinguish is whether a system holding them does so with nothing felt. What
> meets the milestone is holding all three under sustained pressure …

**`What meets it` became `What meets the milestone`.** With a sentence inserted
between, *it* bound to *whether a system holding them does so with nothing felt*
— a wrong binding one sentence away, the same class as the repair above.

**The paragraph left behind had to name its subject.** `:15` opened *What makes
the question approachable at all is that it asks about the artifact…*, and *the
question* was the sentence that moved. It now opens:

> Whether a system holding the marks feels anything is approachable at all because
> the question is about the artifact and not about the artifact's provenance: …

The `and-not` that `antithesis.py` flags in it is the original clause, present at
HEAD; §12.2.1 carries 3 instances in 511 words and **0 clusters**, unchanged.

## What was not done

**No cross-reference was added or removed.** 231, and both sections already point
at §3.3 and §3.2 respectively. The reordering is what the note asked for and it
needs no new apparatus.

**§3.3, §3.10 and §9.3.2 are untouched.** §9.3.2 is the third site of Q-104's
milestone formula and this pass did not open Q-104.

**§11.1's and §12.2.1's pre-existing overlaps were left alone.** They share 40 and
46 six-word runs with other sections — *held-out set of pressures the model's
trainers did not write*, *whether formation can be read off*, *at what scale,
against which test* — and nothing here touches them. See Verification for the
measure that was taken instead.

## Verification

Suite green. `refresh_order_shas.py` run twice, after the draft and after the
redraft. Scratchpad lualatex build: **196 pages, 0 undefined references and 0
undefined citations**; both edited passages read back out of `pdftotext` in
position.

**The shared-run measure, stated as what it is.** The handoff's usual line — *0
runs of six words or more shared with any other section* — is not true of these
two sections and was not true before this pass. What was measured is the **delta
over every section pair in the manuscript: 1,623 shared six-word runs before the
edit and 1,623 after, with none introduced and none removed.** One intermediate
draft did introduce one, *it does not reach is the*, shared with `11_06.tex:7`'s
*What it does not reach is the sharper version*; *The condition it misses* cleared
it, which is the repair P142 made against §3.3.

## Figures

133 sections, **2 changed**. 99,339 → **99,355** words (+16); §11.1 1,447 → 1,457,
§12.2.1 505 → 511. **196 pages unchanged.** **231 cross-references unchanged.** 324
bibliography entries unchanged. 0 `\textit`. §11.1 antithesis 11 sentences and 5
clusters, §12.2.1 3 and 0 — all four at their pre-edit values.
