# Style sheet

The operative document for the revise pass (D-007). Every section is edited
against this list.

**Section numbers are permanent. Do not close the gaps and do not renumber.**
§4 and §5 are vacant; §4a, §4b and §6a sit under numbers whose parents are gone.
The append-only record cites these sections by number and cannot be rewritten, so
renumbering would repoint those citations at the wrong rule.

**Two instruments have no rule behind them.** `claims.py` writes
`reports/dated.tsv`, and `section_stats.py` carries a `TEMPORAL` pattern and a
`dated_names` count. **Read their columns as noise unless somebody reinstates the
rule.**

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
included, and it is part of the book's voice, not the committee *we* this section
removes. Do not report it, and do not recast it.

## 2. Section shape

Delete on sight:

- **Closing summary paragraphs.** 31 sections end with "In conclusion" or "In summary". A section of 400–900 words does not need to summarize itself.
- **Opening signposts.** "In this section, we will explore…" Start with the content.
- **The concluding-restatement move** generally: "Ultimately", "In essence" as paragraph openers (7 and 6 respectively).

**Cut the sentence that announces what the next sentence will do.**

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

Three shapes the rule condemns:

- **The catalog.** A numbered run of theories, techniques, or frameworks, one
  paragraph each, with an example and a "challenge" attached. The catalog's real
  claim is almost always one item long.
- **The definition with a speculative tail.** "X trains a system on Y. Applied to
  ethics, the same method could …" followed by applications nobody has built.
- **The capability list.** A bulleted set of things a well-designed system would
  do, each generically stated.

What the rule protects: background delivered at the point of use, in the amount
the claim needs, with the design consequence stated.

A section that is only a definition has nothing to revise into; the fates are cut
and compress, and where the claim that survives needs prose that does not yet
exist, write it.

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

The reason to count is not that the mark is wrong. It is that the em dash is
among the most-remarked tells of generated prose, this manuscript was generated,
and a reader who holds that association brings it to the page whether or not the
association is fair. The dashes doing real work pay for the ones that are not.

The census below was taken at 662 em dashes in 92,582 words, one every 139 words,
and has not been retaken. Use the proportions, not the totals.

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

## 3b. Name the thing again (D-323)

Do not point back at a thing you have already named. Name it again.

The tic has three forms, and all three ask the reader to hold something they
have put down:

- **A demonstrative standing in for a noun.** "Quantities of that kind," "a
  change of that size," "states answering to that description." The reader has
  to reconstruct which quantity, which change, which description. Say the
  quantity.
- **A back-reference by index.** "The third mark," "the first of the four
  properties," "the second route," "the former." These work while the list is
  on the page and stop working one paragraph later. Restate the mark instead of
  numbering it. The exception is narrow: if the whole of the preceding
  paragraph was about that item and nothing has intervened, the index is
  legible.
- **A signpost that carries no claim.** "That is a bet about where engineering
  effort should go." "The research agenda states the experiment that would test
  it." A sentence whose content is the location of other content. Cut it; the
  reader will arrive there without being told.

Restating costs four or five words and buys a sentence that can be read once.
Prose in this book is read by people who put it down between sittings, and a
back-reference by index is a bill they pay later.

## 4a. Run-in heads inside long sections

The three-level cap is about the **reader-facing table of contents**, not about
forbidding internal structure. Where a section runs long, its internal divisions
keep unnumbered run-in heads:

```
\runin{What enumeration answers, and what it leaves}
```

no number, not in the table of contents. A reader still gets signposts; the
outline still reads three deep.

§9.1.1 is the working example, carrying eight of them, and the
eight read as the outline of an argument — *The reply, and how far it reaches*;
*The tradition this belongs to, and where it went wrong*; *The tradeoff this
leaves the book with* — material that would otherwise have wanted subsections and
a fourth level to hold them.

Rule of thumb: a section over about 1,500 words wants run-in heads. Below that,
paragraphs are enough. This is the escape valve inside D-010's three-level cap.

## 4b. Boxes

`\begin{esbox}` … `\end{esbox}`, with `\boxtitle{…}` as the first line inside
it. For a case study or a self-contained episode that would derail the paragraph
it sits next to — the Gaza targeting box at §6.4.1 is the model. A box is the
author's own prose and counts toward the word count, unlike an epigraph.

Use sparingly. A box is a promise that the material is worth stepping out of the
argument for.

**A box carrying facts that will date takes the period in its title** — *as
reported through mid-2026* — so the prose around it does not rot with them. All three boxes in the book do it.

## 6. Citations (D-009)

Endnotes for named studies, statutes, systems, and quotations. Nothing else.

While revising, a factual assertion gets `[[cite:CNNNN]]` keyed to
`reports/claims.tsv` (268 items in 91 sections at the start of the pass).

**Transplanted material brings its own citation debt, and its placeholders are
allocated at transplant time, not deferred.**

**The agent writes a reference entry only from metadata it has verified against
the source itself** (D-204). **An assertion nobody can source is cut, not carried
forward with a placeholder** — that is what stops the citation backlog from
becoming the project.

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

**D-137 has not been applied to brain-injured populations as a class**, and a
pass proposing to do that is opening a question rather than following a
precedent.

## 7. Cross-references

Under D-013 the surviving instance of each repeated argument is the one place it
is made; every other location that needs it gets a cross-reference instead.
Target: at least one real cross-reference per section, where honest. Without them
the same argument can appear nine times without anyone noticing.

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
  somebody's hands. The repair is not to retire the term: "a floor that holds"
  is the right image and is kept. A system does not hold a floor — it refuses,
  and the floor holds because it does.
- **The name-dropped argument.** "Which is section 6.4.4's whole argument."
  Naming a section's argument is not making it. If the claim matters here, state
  it here in a clause.

## 8. Mechanics

- **Quotation marks are the characters themselves, `“` and `”`** (D-082, Q-025).
  A straight `"` is not a neutral character in a typeset book: LuaLaTeX sets it
  as a *closing* mark wherever it stands, so a manuscript written with straight
  quotes opens every quotation with the mark that should close it.
- **Apostrophes stay straight.** `'` is the one place the ASCII character is
  correct: LaTeX sets it as `’`, which is the right glyph. Converting them would
  buy nothing and would put `'Cause` and `'90s` at risk, where the mark is an
  elision and not a possessive.
- **Dashes are the characters themselves**, `—` and `–`, not `---` and `--`.
  Mixing the two notations sets the same dash at two widths on one page. This
  rule is about the character. How many there should be is section 3a.
- `finishing/tools/check_typography.py` enforces the quote and dash rules, and
  runs in `check_all.sh`. Neither is catchable any other way: both notations
  compile without a warning and produce a page that is merely wrong.
- "AI" as a mass noun ("an AI system", not "an AI") except where the book means an individual system, which it sometimes does deliberately — that distinction is load-bearing in chapters 2 and 7 and should be made consistently.
- Spelling: US.
- Section titles: sentence-shaped, under about ten words. The current set includes titles of 20+ words.
- **A title may be a question, and may address the reader as *you*** (D-198,
  Q-079): §3.5, *If You Can Be Switched Off, Can You Hold the Line?* Part of the
  book's voice. Do not report it.
- ***e.g.* is permitted in body prose** (D-198, Q-079). Do not report it or
  expand it.
- **Emphasis is `\emph`, never `\textit`** (D-189). Edits made in Overleaf come
  back with `\textit`; convert them on import.
- **`\textbf` is not emphasis. Its two uses are structural** (D-372). It sets the
  two column heads of the book's one table, at §2.3, and it sets chapter 11's
  field labels — *Unresolved issue.*, *Test.*, *Evidence against the proposal.*,
  *Required access or authority.* — which run into their paragraphs under a
  `\subsection*` question. **Chapter 11 keeps them.** It is the only chapter with
  two levels below the section, and `\runin` would set the fields as display
  labels under a display heading and flatten the distinction it reads by.
  **Everywhere else a lead-in label is `\runin`.** Do not use `\textbf` for
  emphasis in prose.
- **`\paragraph` is not used** (D-386). It was LaTeX's own run-in head and
  survived in `04_02.tex` alone, five of them, each with a trailing period and a
  blank line after it, which cost the head its run-in behaviour anyway. All five
  are `\runin` now, without the period: none of the book's 133 run-in heads
  carries one. Nothing enforces this; §4a is the rule and this is the note that
  one file departed from it for a month.
- **`\runin` does not run in.** It expands to
  `\par\medskip\noindent\textbf{#1}\par\nopagebreak\smallskip`, which sets the
  label on its own line with space above and below. What runs in is a bare
  `\textbf` followed by a newline, the newline being a space. Read the definition
  before choosing between the two.

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

The failure is the one section 2 already names, pointed the other way: a
verdict-first register in which the correction lands one beat after the claim.
The report withholds — the reader gets the verdict, then the complication, then
the qualification, and reads three beats to learn what one would have carried.

**Give the finding and its limits in the same breath.**

| Drafted | Accepted |
|---|---|
| "Diagnosis accurate, premise overstated, and the remedy would cost something the critique doesn't price" | "The quotations check out. Section 3.2's opening sentence is the one unguarded spot; everything else the critique asks for is already in sections 3.1 and 3.5." |
| "The serious finding is not a pointer." | "The serious finding is a sourcing hole at section 10.1.1." |
| "Substantially fair, with two factual corrections and one thing it missed that's worse" | "Fair. Two of its specifics are wrong, and section 3.6's title is a separate defect it did not name." |

Five corollaries, three of them section 2's own:

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
  what they were saved from. They care what they were not saved from. A prior
  pass belongs in a finding only where it is the cause of the defect, and there
  it is named as the mechanism and not as a mitigation.

A rule from section 1 that belongs here too, because it applies to the book and
to reports alike (D-055): **specify what a demonstrative refers to.** In
persuasive argumentation "that," "this" and "it" should name their referent --
not for the reader's sake alone but because naming it forces the writer to be
precise about what is being claimed. The bare demonstrative is a casual-register
expedient, and it hides exactly the imprecision an argument cannot afford. When
the noun is hard to choose, that difficulty is the finding.

**This is not a license to hedge.** `AGENTS.md`'s no-weasel-words rule is
unaffected and outranks this section: say what was checked, what was found, and
what was not checked, and say "I don't know" where that is the answer. Plainness
is not vagueness, and a flat sentence that reports an uncertainty precisely is
what this section is asking for. What it forbids is the *shape* — the withheld
qualification, the staged correction — not the qualification itself.


## 10a. Cite a section by its label, not by its number (D-461)

Sections 1-9 govern the book, section 10 the prose written about it. This one
governs one habit inside that prose, and it is the cheapest rule in this file to
follow: **in `DECISIONS.md`, `STATE.md`, `QUESTIONS.md`, the `pN-scope.md` files
and commit bodies, name a section by its label or its file, not by the number it
printed on the day of writing.** Write `sec:3.6`, or `ch03/03_06.tex`, where the
habit is to write \S\,3.6.

**A number is only true as of a date.** Twenty-two renumbers stand between the
earliest entries in this record and the book, and the record already carries
**7,022 section numbers against 228 labels**. `QUESTIONS.md`'s own header calls
reading its entries through those maps the largest gap in that file.

**A label is stable by construction.** D-406 separated a file's identity from
its position for exactly this reason: a file keeps the label its filename and
its ledger row know it by while the number it prints moves underneath. Every one
of the twenty-two renumbers left the labels alone. `check_numbers.py` resolves a
label to the number the book prints today, so a label costs the reader nothing
and never needs a map.

**The exception is a sentence about what the book prints.** A page proof, a
printed table of contents, the number a reader sees on the page — there the
printed number is the fact being reported, and the rule is the ordinary one:
give it with the date or the commit it was read from.

**Reading a number already in the record** is `finishing/tools/trace.py`:

```
trace.py 6.3 --as-of D-302        # a date, a decision, or a pass
trace.py --list-maps
```

It composes the maps and reports the chain, and **it refuses to answer without
`--as-of`**, because numbers are reissued — `6.3` is dissolved on 2026-08-23,
becomes 6.2 on 2026-09-12 and 6.4 on 2026-09-13 — and chained from the wrong
date it would return a confident wrong answer rather than an error. It says
where the chain ends in a cut, where a hop crossed the September 12 rewrite, and
where it propagated a number from its parent chapter rather than reading a row.

**Nothing about the book's own prose changes.** The manuscript has always used
`\ref`, which reads the counter; `check_xrefs.py` reports no number left in
prose, and the last audit of literal chapter numerals found eleven, all
`chapter~2`, all correct.
