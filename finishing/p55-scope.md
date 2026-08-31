# P55 — the ordering constraint carried into the two closes (D-128)

**Author's finding**, forwarded: section 3.3 states that the maintained justification
and the plural arrangement get their attempt before anyone builds toward affect on
purpose, and that *"a deployment that goes straight to the bearer owes an account of
what it tried first."* Section 3.8 closes on the bearer and section 12.3 closes on the
bearer, and neither restates the ordering. A reader taking the conclusions at face
value comes away thinking the book recommends building the affective bearer now.

**The finding holds for the two closes.** It is wrong about the rest of the book in one
respect worth recording, because the correction is what shows the defect is a
propagation gap and not a decision.

## Where the ordering already was

Four sites carry it, none of them a conclusion.

- **Section 3.3**, the full statement, at the end of the section's last run-in head.
- **Section 2.4.3**, which states Replacement as the R the book's own proposal has not
  discharged and points at section 3.3 for what discharging it would take.
- **Chapter 11's opener**, priority 2: *"Chapter 3 argues for building a prospective
  moral patient once the cheaper routes have had their attempt; this is the debt that
  argument leaves."*
- **Chapter 1's roadmap**, which since P41 reads *"a prior about where to build first,
  with the cheaper routes owed their attempt, and not a proof."*

The first read of the finding reported chapter 1 as a site that states the bearer flatly
with no ordering attached. That was wrong: it read chapter 1's safety-and-ethics
paragraph and not the roadmap paragraph four lines above it, which P41 had already
repaired. Recorded because the corrected picture is the stronger evidence — P41
propagated the constraint to chapter 1 and did not propagate it to either close.

**Sections 3.8 and 12.3 carry nothing of it.** Both were read whole. A grep of the whole
manuscript for `plural arrangement`, `maintained justification`, `tried first`, `cheaper
routes`, `Replacement`, `untried` and `order of the attempts` returns the four sites
above and no others, so a paraphrase survives elsewhere only if it reuses none of those
terms, which was not checked by reading.

## Why it is an accident of composition

The sentence entered at P39 (`6d78762`), the pass that answered forwarded feedback with
two points: Replacement stated as open, and the bearer as necessary and not sufficient.
**P41 (`e50b04e`) was the propagation sweep for P39, and its commit body names section
12.3 explicitly** as a site still stating the pre-P39 modality. It edited that exact
paragraph and carried the second point across — *"the only version of that anyone can
specify"* became *"the one version of that with a working instance behind it,"* with the
custody pairing added. The ordering was not carried with it. Section 3.8 was edited by
P39 itself and by four passes since without gaining it.

The propagation pass had the paragraph open and took one of P39's two points out of it.

## 1. Section 3.8

The close serves one of its two readers. The paragraph beginning *"A reader who finds
that price too high is not thereby left with nothing"* gives the exit — the fourth
construction, the duty on the operator — to a reader who **declines** the price. There
was no corresponding sentence for the reader who **accepts** it, and that reader is the
one the ordering constrains.

A paragraph was added immediately after it, so the two readers stand in parallel. It
names the two constructions rather than pointing at them, per `style.md` §7: a
justification the system maintains, and a floor held by several systems with different
principals. It states the Replacement question, the obligation on a deployment that
skips them, and the one qualification without which the ordering reads as a counsel to
delay — that the party who pays for a delay is the party the floor exists for.

**+144 words, one `\ref`.** Nothing was cut to make room, and the paragraphs on either
side are unchanged.

## 2. Section 12.3

The book's last substantive paragraph gains two sentences' worth of the same, in one
sentence, and **the pointer to where the price is set out**.

P53 had cut that pointer: *"at the price section 3.8 sets out"* became *"at the price
the argument has already named,"* which left the final page of the book asserting a
price and naming no place to find it. It is restored. This is not a reversal of D-118 —
the pass stands — but two `\ref` calls added back at the one site where the book sums
up, with the reason on the record so a later density pass does not cut them a second
time without reading this.

**+25 words, two `\ref` calls.**

## 3. Section 3.3 — "the fourth capacity" now resolves to the wrong rung

Found while verifying the finding's quotation, and not part of it.

Section 3.3 uses the phrase **twice**, at the falsifier's middle condition and in the
ordering sentence itself. Both mean **affective concern**, which is the fourth row of
section 2.3's table — *"Only the fourth is relevant to genuine caring."* When P39 wrote
the phrase, section 3.2 carried the key: *"Affective concern is the fourth capacity in
section 2.3's table."*

**P53 cut that clause** as a cross-reference. Section 3.2's own ladder numbers affective
concern **third** and phenomenal experience fourth. So for a reader inside chapter 3 the
phrase now resolves to phenomenal experience, and two things follow:

- The falsifier states its middle condition as *"a method that installs nothing
  answering to affective concern"* and restates it two paragraphs later as *"installed
  nothing answering to the fourth capacity."* Same condition, different rungs.
- The ordering sentence reads as a bar on building toward phenomenal experience, which
  section 3.2 says explicitly cannot be aimed at from outside. The constraint is about
  affect, the rung at which a subject that can be wronged exists.

**Repaired by naming the capacity instead of numbering it**, at both sites. That is
cheaper than restoring section 3.2's bridging clause, costs no cross-reference, and is
what `style.md` §7 asks for anyway — the sentence carries itself.

**No tool in the suite could have found this.** `check_xrefs.py` sees no `\ref` in either
sentence; `xref_pairs.py` and `xref_content.py` read only sentences that carry one. The
sentence still reads fluently, which is why five passes went over it.

## Numbers

| | before | after |
|---|---|---|
| Words | 94,298 | 94,465 |
| `\ref{sec:}` calls, body | 476 | 479 |
| `\ref{sec:}` calls, glossary | 123 | 123 |
| Pages | 192 | 192 |
| Undefined references | 0 | 0 |

Three files changed: `ch03/03_03.tex` (−2 words, two phrases), `ch03/03_08.tex` (+144),
`ch12/12_03.tex` (+25). `ORDER.tsv` digests refreshed; `check_all.sh` green. **Both
changed pages were read in the rendered PDF** — page 45 for section 3.8's new paragraph
and page 154 for section 12.3's close — rather than only built, per `pipeline.md`.

## What was not done

- **Chapter 1 and chapter 11 were left alone.** Both already carry the ordering, and
  chapter 1's later safety-and-ethics paragraph states the bearer as required without
  it. That paragraph is two paragraphs after the roadmap that qualifies it, and
  compressing an introduction's rhetoric to repeat a qualification it has just made
  would cost more than it buys. Named here rather than taken.
- **The tension with Q-037 is not resolved and is now more visible.** D-111 ruled that
  the plural arrangement stays a recommendation with no institutional form, carried by
  section 11.6 as an open research problem. Section 3.3 recommends it in the first
  person — *"I recommend it whatever else this chapter recommends"* — and both closes
  now tell a reader to try it first. A reader who follows that instruction reaches
  section 11.6 and is told nobody knows how. The ordering is not thereby wrong, and this
  pass did not reopen the ruling; the visibility of the gap has changed and the author's
  ruling has not.
- **No sweep for the class of defect item 3 belongs to.** P53 cut roughly 252
  cross-references, and each cut clause may have been the anchor some distant sentence
  depended on. One instance was found here by accident. Whether there are others has not
  been checked, and nothing in the tool suite would find them.
- **The 70 sections P53 changed remain unread end to end**, as they were after P54.
