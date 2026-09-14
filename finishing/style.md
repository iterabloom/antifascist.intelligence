# Style sheet

The operative document for the revise pass (D-007). Every section is edited
against this list. Counts come from `reports/tics.tsv` and `reports/voice.tsv`
over 115,377 body words.

Draft. The pilot section will test it, and what the pilot teaches gets folded
back in before the pass proper begins.

**Two sections are gone and their numbers are left vacant on purpose.** §4, on
lists, and §5, on dates and currency, were deleted 2026-09-13 (D-303), along with
§1's paragraph about the *we* sweep not being a search-and-replace. **Do not close
the gaps.** Eighteen references across `DECISIONS.md`, the superseded `STATE.md`
leads and the `pNN-scope.md` files cite these sections by number, and most of them
sit in the append-only record where they cannot be rewritten; renumbering §6 or
§6a to fill a hole would silently repoint every one of them at the wrong rule.
§4a, §4b and §6a already sit under numbers whose parents are gone, which is the
same arrangement.

**What §5 leaves behind, and why it was safe to go (D-304).** It had two halves.
The one telling the prose not to say *currently*, *recently* or *state of the art*
**is finished**: 117 instances when the rule was written, **15 regex matches now,
and none of them a violation** — eleven are *proposed* in its argumentative sense,
one is a consensus protocol's *latest state*, one sits inside a dated court
holding, and two are §9.1's load-bearing distinction between what an organization
*currently* intends and what it has bound itself to. The other half, that a box
carrying datable facts is dated in its title, **is live and unanimous**, and has
moved to §4b.

**The instruments outlived the rule and nothing now backs them.** `claims.py`
writes `reports/dated.tsv`, and `section_stats.py` carries a `TEMPORAL` pattern
and reports a `dated_names` count per section on every run. They were left in
place; **read their columns as noise unless somebody reinstates the rule.**

**Eight references to §5 now dangle**, which is the intended failure: a pointer
that obviously goes nowhere is safer than one that resolves to a rule its author
never meant.

## 1. Person and stance (D-008)

| Now | Becomes |
|---|---|
| "This report" (6×) | "This book" |
| Institutional "we" as author (258× in 131 sections) | "I" where the author speaks |
| "We propose / recommend / argue" (36×) | **drop the frame and make the claim** |
| "Our" as the authors' (130×) | "my", or recast |
| "In this section, we…" (22×) | delete; say the thing |

On that last row the author is explicit: not "I argue that X" but simply *X*.
"We propose an array of strategies" becomes the strategies. The hedging frame is
not replaced with a first-person frame; it is removed.

"We" survives only as reader-inclusive — "we can now ask", "what we call
attention" — where it means *you and I*, not *the authors*. When in doubt,
substitute "you and I" and see whether the sentence still means what it should.

**The author's own *we* stands (D-198, Q-079).** *We need nothing beyond
reasons-responsive refusal*; *the route by which we achieve reasons-responsive
refusal* (§3.2). It is the *we* of whoever is building the thing, the reader
included, and the author has ruled it part of the book's voice. It is not the
committee *we* this section removes, which proposed and recommended on behalf of
authors who did not exist. Do not report it, and do not recast it.

## 2. Section shape

Delete on sight:

- **Closing summary paragraphs.** 31 sections end with "In conclusion" or "In summary". A section of 400–900 words does not need to summarize itself.
- **Opening signposts.** "In this section, we will explore…" Start with the content.
- **The concluding-restatement move** generally: "Ultimately", "In essence" as paragraph openers (7 and 6 respectively).

**Cut the sentence that announces what the next sentence will do.** This is the
rule the pilot produced, and every one of the author's six edits was an instance
of it:

| Drafted | Accepted |
|---|---|
| "The conclusion is uncomfortable and important. What we experience is not…" | "What we experience is not…" |
| "Nor is this a defect. The visual system did not evolve…" | "The visual system did not evolve…" |
| "That reframing matters for machine perception, because it changes what an attention mechanism is for." | "The implication for machine perception?" |
| "…are the most consequential instance, and they make the point about blind spots concrete." | "…illustrate the point about blind spots." |
| "That claim is taken up in the discussion of machine self-models in section 2.3.3, where…" | "Section 2.3.3 expounds on this point in discussing machine self-models, where…" |
| "the design question is not how to allocate attention efficiently. It is whether a system can be built to notice…" | "the design question is how it will notice…" |

Three corollaries:

- **Prefer the positive construction to "not X. It is Y."** The contrastive frame is announcing in another costume: it spends a clause on the wrong answer.
- **Prefer an active subject to a nominalized one.** "Section 2.3.3 expounds" over "That claim is taken up in the discussion of".
- **A rhetorical question is permitted** where it replaces a paragraph of throat-clearing. "The implication for machine perception?" does the work of two sentences.
- **Drop the superlative you cannot defend.** "the most consequential instance" became "illustrate".

Keep and strengthen: the concrete example. Where a section already has one
("Consider an AI system created for customer service…"), it is the best thing in
the section and usually deserves to come first rather than fourth.

## 2a. Background earns its place only by serving a claim (D-077)

The book does not teach its fields. A passage of background survives only where
some claim the book is making would be harder to understand or harder to believe
without it, and the claim has to be nameable.

The test, in the author's own words: if you need to know what reinforcement
learning is in order to understand a particular statement I am making about how
something should be different, that is where reinforcement learning gets defined.
It does not get defined because it is a major topic.

So, for any passage of exposition, finish this sentence:

> The argument I am making would be harder to understand or believe without this,
> because …

A passage that cannot finish it is cut. Not compressed, not moved to a footnote --
cut, because a definition serving no claim is a definition the book does not need
at any length.

Three shapes this rule condemns, all present in the 2023 draft:

- **The catalog.** A numbered run of theories, techniques, or frameworks, one
  paragraph each, with an example and a "challenge" attached. Section 2.1.1's six
  ethical theories and section 5.7.1's four developmental frameworks are the
  specimens. The catalog's real claim is almost always one item long.
- **The definition with a speculative tail.** "X trains a system on Y. Applied to
  ethics, the same method could …" followed by applications nobody has built.
  Section 4.2.3 is the specimen.
- **The capability list.** A bulleted set of things a well-designed system would
  do, each generically stated. Section 5.6.3's safeguards list is the specimen.

What the rule protects, and it is most of what the good sections do: background
delivered at the point of use, in the amount the claim needs, with the design
consequence stated. Section 4.1.2 states the principle in its own second
paragraph and then follows it -- "What follows are the findings that change a
design decision, and in each case the decision is stated."

This rule lifts D-007 where it bites. A section that is only a definition has
nothing to revise into; the fates are cut and compress, and where the claim that
survives needs prose that does not yet exist, write it.

## 3. Word-level lint

Highest-frequency tics, with counts. None is forbidden; each is a flag that the
sentence is doing less work than it appears to.

| Word | Count | Sections | Per 10k |
|---|---|---|---|
| foster / fostering | **278** | 149 | 24.1 |
| robust / robustness | 148 | 88 | 12.8 |
| crucial | 118 | 93 | 10.2 |
| nuanced | 71 | 54 | 6.2 |
| navigate | 67 | 54 | 5.8 |
| leverage | 59 | 51 | 5.1 |
| intricate | 47 | 38 | 4.1 |
| harness | 34 | 28 | 2.9 |
| pivotal | 33 | 28 | 2.9 |
| landscape | 29 | 24 | 2.5 |
| realm | 28 | 26 | 2.4 |

"Foster" is the signature: it appears once every 415 words and in 53% of
sections. It almost always means *encourage*, *build*, *cause*, or nothing at
all. Prefer the specific verb; if no specific verb fits, the claim is probably
empty and the sentence should go.

Connective tics — "Moreover" (34), "Furthermore" (32), "Additionally" (30) — are
usually a paragraph pretending to follow from the one before it. Cut the word;
if the paragraph no longer follows, that is the real problem. "However" opening a
paragraph is the same tic and goes the same way. Inside a paragraph it is an
ordinary word and this section has nothing to say about it.

## 3a. The em dash

662 em dashes in 92,582 words: one every 139 words, in 132 of 153 sections and in
35 percent of paragraphs. **Counted before P57**, which merged eight sections away, added one, and added about 2,900 words; the census has not been retaken and the ratios below are the ones it produced. One sentence in eight carries at least one — 291 with a
lone dash, 190 with a matched pair, none with three.

The reason to count is not that the mark is wrong. It is that the em dash is
among the most-remarked tells of generated prose, this manuscript was generated,
and a reader who holds that association brings it to the page whether or not the
association is fair. This file does not attempt to verify the impression and does
not need to: the dashes doing real work pay for the ones that are not.

What a lone dash introduces, counted by the word after it:

| After the dash | Count | What it is |
|---|---|---|
| the / a / an | 99 | an appositive: a restatement or a list. The dash's own job |
| and / but / so | 33 | a coordinating conjunction. A comma does this |
| which / that / what / whether | 30 | a relative gloss. A comma usually does this |
| not | 7 | D-025's contrastive negation, wearing a dash |

Only the first row is work no other mark does. Section 3's logic applies here
unchanged: none is forbidden, each is a flag.

**The test.** Replace the dash with the mark it is standing in for — comma,
colon, period, connective — and read the sentence again. If nothing is lost, the
dash was setting a beat rather than doing a job. Three cases in particular:

- **A dash before "and", "but" or "so"** is a comma with a drumroll. 33
  instances. Keep it where the beat is the point and it is the only one nearby.
- **A dash carrying a turn** is a connective the prose declined to write, which
  is how a book with 671 dashes ends up with six connectives. Section 3 has the
  word. A paragraph whose contrast lives entirely in its dashes has hidden the
  joints of its own argument, and the reader has to reassemble them.
- **Three or more in one paragraph.** 65 percent of paragraphs have none, 37 are
  at three or more, and 12 at four or more. The dense ones are where to look
  first; nothing about the count alone makes a paragraph wrong.

## 4a. Run-in heads inside long sections

The three-level cap is about the **reader-facing table of contents**, not about
forbidding internal structure. Where a section runs long, its internal divisions
keep unnumbered run-in heads:

```
\runin{What enumeration answers, and what it leaves}
```

no number, not in the table of contents. A reader still gets signposts; the
outline still reads three deep.

§9.1.1 is the working example: **2,946 words carrying eight of them**, and the
eight read as the outline of an argument — *The reply, and how far it reaches*;
*The tradition this belongs to, and where it went wrong*; *The tradeoff this
leaves the book with* — material that would otherwise have wanted subsections and
a fourth level to hold them.

Rule of thumb: a section over about 1,500 words wants run-in heads. Below that,
paragraphs are enough. **The book follows it**: measured 2026-09-13, 15 of the 16
sections over 1,500 words carry run-in heads, the one exception being chapter~2's
opener at 2,081 words with none. This is the escape valve D-010 always had — it
was in the decision's original form and was lost when the triage was ruled.

## 4b. Boxes

`\begin{esbox}` … `\end{esbox}`, with `\boxtitle{…}` as the first line inside
it. For a case study or a self-contained episode that would derail the paragraph
it sits next to — the Gaza targeting box at §6.4.1 is the model. A box is the
author's own prose and counts toward the word count, unlike an epigraph.

Use sparingly. A box is a promise that the material is worth stepping out of the
argument for.

**A box carrying facts that will date takes the period in its title** — *as
reported through mid-2026* — so the prose around it does not rot with them. This
is what survives of the D-008 dating policy, whose own section was retired at
D-304: the half telling the prose not to say *currently* had finished its work,
and this half had not. All three boxes in the book already do it.

## 6. Citations (D-009)

Endnotes for named studies, statutes, systems, and quotations. Nothing else.

While revising, a factual assertion gets `[[cite:CNNNN]]` keyed to
`reports/claims.tsv` (268 items in 91 sections at the start of the pass).

**Transplanted material brings its own citation debt, and its placeholders are
allocated at transplant time, not deferred.** The pilot appended five rows to
`claims.tsv` as it went; doing that retroactively across sixteen transplants
would mean re-reading all of them. Expect the debt to rise during P3, not fall —
imported material makes specific empirical claims where the original made
general ones. **The agent writes a reference entry only from
metadata it has verified against the source itself.** The rule here forbade it
outright until D-204; the practice outgrew the words, and D-204, D-209 and D-213
record entries authored that way. What has not changed is the reason behind the
old rule: an assertion nobody can source is cut during the revise pass, not
carried forward with a placeholder — that is what stops the citation backlog
from becoming the project.

## 6a. Claims about a disabled population (D-137, D-138)

A finding about a disabled population may not be used as a premise unless the
population took part in producing it, or the population's own literature supports
it. Where neither holds, the finding and the assertion resting on it are **cut**,
not hedged.

The test is participation and standing: whether the population was included in
producing the finding, and what their own literature says about it.

Participation means a hand in producing the finding -- the question asked, the
measure chosen, the result interpreted. Being a subject is not participation, and
the distinction is the rule's whole content: the literatures this rule is aimed at
have no shortage of subjects.

The figure the rule was written against, and the one to measure a source by:
across 142 human-robot-interaction papers on autism from 2016--2022, about 90
percent did not include autistic people in the design process, 93.75 percent
pathologized their communication behaviors, and nearly 20 percent took autistic
perspectives into account nowhere in the research process at all (Rizvi, Wu,
Bolds, Mondal, Begel and Munyaka, *Are Robots Ready to Deliver Autism Inclusion?
A Critical Review*, CHI 2024). That is a fact about method, checkable against a
paper. Record it that way.

Where the population's own literature exists it is evidence and not a
complication. The double empathy problem and the review of theory-of-mind's
empirical failures are both the work of autistic researchers answering the
literature this book has been citing.

**Research that harms a disabled population gets no oxygen at all (D-138)**, and
that includes stating a finding in order to dismiss it. There is no version of
this rule under which the book rehearses a harmful claim first and answers it
after. Whatever the rehearsal wins back in argument is not worth its price, which
is the ruling and not a weighing to be redone case by case.

The two rules test different things and a passage is checked against both. D-137
asks about method: was the population a party to producing the finding. D-138 asks
about effect: does the research harm the population. A study can fail one and pass
the other.

**Both rules have been applied once, at P58**, and Q-058 records how far they
reached. The reach is narrower than the rules read: the autism material at
sections~2.3.3 and 2.2.1 went on these rules, while section~2.3.3's psychopathy
and ventromedial-prefrontal material went on evidence quality instead, and
Koenigs was kept although its subjects are the same population as Bechara's. So
**D-137 has not been applied to brain-injured populations as a class**, and a
later pass proposing to do that is opening a question rather than following a
precedent.

## 7. Cross-references

The book currently contains one backward reference and one forward reference in
115k words, which is why the same argument can appear nine times without anyone
noticing. Under D-013 the surviving instance of each repeated argument is the
one place it is made; every other location that needs it gets a cross-reference
instead. Target: at least one real cross-reference per section, where honest.

**A cross-reference says where, not what.** The sentence carrying it has to make
sense to a reader who does not follow it. A reference that supplies the meaning
the sentence is missing sends the reader out of the paragraph to find out what
was just said, and most readers will not go.

The failing shape is a noun phrase whose content lives elsewhere: "the form
section 8.6.4 identifies as worthless," "section 8.6.4's slope, measured from
inside," "in the phrase the criteria at the end of section 2.4.1 arrive at."
Say the thing, then name the section:

| Sends you away | Carries itself |
|---|---|
| "a refusal that costs the refuser nothing it could have kept is the form section 8.6.4 identifies as worthless" | "a refusal that costs the refuser nothing is worth nothing — which is section 8.6.4's test for telling a real objection from a performed one" |
| "looks like it requires something with standing — section 8.6.4's slope, measured from inside" | "requires a party that can notice its own objections getting more expensive to make, which is section 8.6.4's measure, taken from inside" |

Two related tics come out in the same sweep, because they fail the same way — the
reader has to decode rather than read.

- **Riddle constructions.** "A party with no option to withdraw has nothing to
  withhold." "Costs the refuser nothing it could have kept." The near-rhyme reads
  as precision and is doing the opposite. The test the author applied to the
  second one: enumerate the variants. Costs you nothing you could not have kept.
  Costs you something you could have kept. Costs you something you could not have
  kept. If three of the four readings are noise and the intended one is not
  recoverable at reading speed, the formulation is broken however exact it looks.
  Plain: a system with no way out can object and be overruled, and then it has no
  move left.
- **Aphorism.** The balanced two-clause epigram — "if refusing costs it nothing,
  refusing changes nothing" — is the same fault wearing better clothes, and
  chapter 3's own opener already rules against it: "ethical, not safe," delivered
  as an aphorism, "prices the risk in advance." An aphorism asks to be admired
  before it is checked. Write the declarative sentence instead, even where it is
  duller.
- **The mixed idiom.** You hold a *line*; you set a *floor*, or put one under
  something. "Hold a floor" welds the two and puts a horizontal surface in
  somebody's hands, which is what the author saw when he read it. Six instances,
  all repaired. The repair is not to retire the term: a floor holding is what
  floors do, "a floor that holds" is the right image and is kept in all nine of
  its uses, and what changed is who is doing the holding. A system does not hold
  a floor — it refuses, and the floor holds because it does.
- **The name-dropped argument.** "Which is section 6.4.4's whole argument."
  Naming a section's argument is not making it. If the claim matters here, state
  it here in a clause.

## 8. Mechanics

- **Quotation marks are the characters themselves, `“` and `”`** (D-082, Q-025).
  A straight `"` is not a neutral character in a typeset book: LuaLaTeX sets it
  as a *closing* mark wherever it stands, so a manuscript written with straight
  quotes opens every quotation with the mark that should close it. The book did
  that 230 times across 44 sections until it was swept. **This replaces the rule
  that stood here** — "Apostrophes and quotation marks: straight, consistently.
  Currently 734 straight to 38 curly, 178 straight double to 6 curly. Normalize
  in P0, not by hand." — which was right while the manuscript was plain text and
  wrong from the LaTeX migration (D-065) onward, and was not revisited then.
- **Apostrophes stay straight.** `'` is the one place the ASCII character is
  correct: LaTeX sets it as `’`, which is the right glyph. All 894 print
  properly. Converting them would buy nothing and would put `'Cause` and `'90s`
  at risk, where the mark is an elision and not a possessive.
- **Dashes are the characters themselves**, `—` and `–`, not `---` and `--`.
  671 em dashes and 1 en, counted 2026-08-30; mixing the two notations sets
  the same dash at two widths on one page. This rule is about the character.
  How many there should be is section 3a.
- `finishing/tools/check_typography.py` enforces the quote and dash rules, and
  runs in `check_all.sh`. Neither is catchable any other way: both notations
  compile without a warning and produce a page that is merely wrong.
- "AI" as a mass noun ("an AI system", not "an AI") except where the book means an individual system, which it sometimes does deliberately — that distinction is load-bearing in chapters 2 and 7 and should be made consistently.
- Spelling: US.
- Section titles: sentence-shaped, under about ten words. The current set includes titles of 20+ words.
- **A title may be a question, and may address the reader as *you*** (D-198,
  Q-079): §3.5, *If You Can Be Switched Off, Can You Hold the Line?* The
  author's own title, ruled part of the book's voice. Do not report it.
- ***e.g.* is permitted in body prose** (D-198, Q-079). The book has two, at
  §2.1.2 and §3.4, the second the author's own. Do not report either or expand it.
- **Emphasis is `\emph`, never `\textit`** (D-189, applied again at D-197).
  The book's practice was uniform and unwritten, so the eight `\textit` that
  came back from the first Overleaf pass and the twelve from the second were
  caught by reading and not by any check. Edits made in Overleaf come back with
  `\textit`; convert them on import. `\textbf` is not used in the prose at
  all: its only use is a table header in §2.2. The one that stood in §3.3, a
  working note's marking, was cut at D-199.

## 9. What this pass does not do (D-007)

Not rewriting the argument. Not filling the stub sections. Not adding topics the
book lacks. Not arguing the anti-authoritarian thesis where it is currently
assumed. If a section is wrong rather than badly written, the fate is Cut or
Merge, not a rewrite — and if that turns out to be true of many sections, that
is evidence to bring back to D-007, not a license to start writing.

## 10. The same rules, applied to reports to the author

Sections 1-9 govern the book. This one governs the prose the agent writes *about*
the book: findings put to the author, status reports, commit bodies, and the
entries in `DECISIONS.md`, `STATE.md`, `QUESTIONS.md` and the `pN-scope.md` files.

The failure is the one section 2 already names, pointed the other way. This
repository's own record is written in a terse, verdict-first register where the
correction lands one beat after the claim — "One was, one was not"; "The defect is
real and the description of it is not"; "The serious finding is not a pointer."
An agent reading a great deal of that will reproduce it, the more so because
agent harnesses generally instruct it to match the style around it. The result is
a report that
withholds: the reader gets the verdict, then the complication, then the
qualification, and reads three beats to learn what one would have carried.

**Give the finding and its limits in the same breath.**

| Drafted | Accepted |
|---|---|
| "Diagnosis accurate, premise overstated, and the remedy would cost something the critique doesn't price" | "The quotations check out. Section 3.2's opening sentence is the one unguarded spot; everything else the critique asks for is already in sections 3.1 and 3.5." |
| "The serious finding is not a pointer." | "The serious finding is a sourcing hole at section 10.1.1." |
| "Substantially fair, with two factual corrections and one thing it missed that's worse" | "Fair. Two of its specifics are wrong, and section 3.6's title is a separate defect it did not name." |

Four corollaries, three of them section 2's own:

- **No reveals.** A finding is not improved by staging it. State it, then state
  what limits it, with no beat between them built to be overturned.
- **A heading names a subject, not a conclusion.** "Why the proposed remedy is
  worse" is a headline. "The remedy's cost" is a heading.
- **The contrastive frame is D-025 wherever it appears.** "X is not Y, it is Z"
  spends a clause on the wrong answer in a report exactly as it does in the book.
- **Do not open with a scorecard.** "Right that X, wrong that Y, and Z unpriced"
  makes the reader parse a verdict before reaching anything checkable.
- **Do not cite the work already done as context for the work outstanding.**
  "Chapter 4 was cut 29.9% in P11 and these sections survived it" offers the
  reader a credit they did not ask for and cannot act on. A reader does not care
  what they were saved from. They care what they were not saved from. Prior
  passes belong in a finding only where they are the cause of the defect --
  P11's split stranded a pointer, P11's cut stranded five citations -- and there
  the pass is named as the mechanism and not as a mitigation.

A rule from section 1 that belongs here too, because it applies to the book and
to reports alike (D-055): **specify what a demonstrative refers to.** In
persuasive argumentation "that," "this" and "it" should name their referent --
not for the reader's sake alone but because naming it forces the writer to be
precise about what is being claimed. The bare demonstrative is a casual-register
expedient, and it hides exactly the imprecision an argument cannot afford. When
the noun is hard to choose, that difficulty is the finding: section 3.2's opener
needed three candidates checked against the chapter before one was available.

**This is not a license to hedge.** `AGENTS.md`'s no-weasel-words rule is
unaffected and outranks this section: say what was checked, what was found, and
what was not checked, and say "I don't know" where that is the answer. Plainness
is not vagueness, and a flat sentence that reports an uncertainty precisely is
what this section is asking for. What it forbids is the *shape* — the withheld
qualification, the staged correction — not the qualification itself.
