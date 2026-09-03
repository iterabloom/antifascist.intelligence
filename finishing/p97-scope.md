# P97 — §3.3's human evidence for the maintained justification withdrawn

**The instruction.** The author, shown the sentence below at its place in §3.3: *this is a
problematic passage. as you acknowledged "reverence for reason" is a phrase from the Kennett
paper. it portrays autistic people like Vulcans from Star Trek. it exotifies a demographic. the
fact that this move is obscured by not referencing the paper does not make anything better.
furthermore, reverence is itself a subjective experience. Kennett might not call it an emotion,
but I would. so this whole line of argument needs to be dropped.*

Then, on scope: *this does not mean "don't try to build a machine that does reasons-based
refusal without caring". it just means we have no business holding up autistic people as an
example of why we think it is possible to build such a machine.*

## The sentence

The last sentence of the maintained-justification paragraph, `ch03/03_03.tex` line 8:

> Moral agents whose seriousness runs on a reverence for reason rather than on felt resonance are
> the human evidence that this is a real way to be, and the case is careful about what it shows:
> that empathy is not the required mechanism, which leaves open whether anything has to matter.

**Where it came from.** P34 (2026-08-28, D-098) wrote §3.3 while §2.3.3 still cited Jeanette
Kennett's 2002 paper on autism and moral agency, recorded in `reports/claims.tsv` as C0749 in
the paper's own terms: moral seriousness running on a reverence for reason rather than on
empathic resonance. The sentence restates that claim without the population and without the
citation.

**How it survived P58.** P58 (2026-08-31, D-137 to D-139) cut the Kennett citation under the
disabled-population rules, moved the entry to `unused_bibliography.bib`, rewrote §2.3.3, and
repaired §3.3's induction paragraph, which had named the psychopathy literature. The repair
stopped there. Nothing in the pass grepped for the paper's vocabulary, and *reverence for reason*
would have found this sentence in one call.

**It contradicted the book.** §3.3's own cut-down, three run-in heads later, says the induction
has *no case of the capacity present and the affect absent to test it against*. §3.4 says *no
demonstrated example exists of reasoning alone generating non-instrumental concern*. The sentence
asserted the case both deny.

## What was checked

**The manuscript, for other remnants.** A grep over every section for *reverence*, *felt
resonance*, *empathic resonance*, *moral seriousness*, *Kantian*, *Humean*, *rationalist*,
*autis*, *human evidence*, *real way to be*, *without empathy*, *absence of empathy*, *lack of
empathy* and *reason-guided*. Three hits outside the sentence, none of them the argument:
§11.8 and §12.1 report the HireVue case, a scoring technique that screened out candidates with
disabilities such as autism, which is a documented harm the book cites; §3.8's *human evidence*
is the Gallup engagement survey.

**Whether anything downstream leaned on the sentence.** §3.10 names the maintained justification
as one of the two mechanism routes whose success would falsify the chapter's inference; §3.3's
Three Rs paragraph orders those two routes before the bearer; §3.4 summarizes §3.3's induction as
a claim about routes. None of them cites a human instance. §3.3's *It has not been tried* is
true without exception once the sentence is gone.

## What was done

The sentence is cut and nothing replaces it. The paragraph now ends on *what the mechanism
consults is the rationale and not the asker*, and the next paragraph opens *I do not have an
argument that this cannot work. It has not been tried.* The construction is described exactly as
before, is still called open, and is still ordered ahead of the bearer, which is the scope the
author drew.

`ORDER.tsv`'s digest for the file refreshed; `reports/section_stats.tsv` regenerated; D-195;
ledger row 3.3 annotated; this file; the leads of `STATE.md`, `PLAN.md` and `QUESTIONS.md`.

## Numbers

**91,436 → 91,385 words, −51**, in one file. **184 pages, unchanged**, built to the scratchpad
with no undefined references or citations. No `\ref` or `\autocite` added or removed.
`check_all.sh` green.

## Left undone, named

- **Committed with this write-up**, and the proof pair rebuilt in place after it on the author's *make the proofs*.
- **`reports/claims.tsv` row C0749 is unchanged.** It is the historical record of the claim
  as verified at P27 and its section number is pre-renumber; the file is not maintained as
  current.
- **D-098 and `p34-scope.md` still describe the sentence as part of what P34 built.** They are
  the record of that pass and stand.
- **No section was read end to end.** What was read is §3.3 whole, §3.4's induction paragraph,
  and every grep hit in its sentence.
