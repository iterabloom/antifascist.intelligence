# P35 — mannerisms, editorial archaeology, and the cross-reference cut (D-099)

The author's instruction has three parts:

> The prose has accumulated crufty and annoying mannerisms such as: "The honest thing…", "It is
> worth naming…", "What belongs here…", "This section used to…", repeated "not X but Y"
> constructions.
>
> The extensive editorial archaeology — what an earlier draft said, what a section used to claim —
> does NOT belong in the manuscript. It distracts readers from the argument. Those who are curious
> about the revision process will have the entire GitHub repo.
>
> There are roughly 680 explicit chapter/section cross-references. The repeated interrupts of
> otherwise strong paragraphs make the text frustrating to read. Retain references needed for
> navigation; remove those that merely announce that another section agrees.

This file is the scope, the measurement each part was checked against, what was done, and what was
not done.

---

## The measurement, before

Taken over the 169 section files, 97,708 body words, headings and labels excluded.

### The named mannerisms

| Shape | Instances | Of which the mannerism | Where it concentrates |
|---|---|---|---|
| `the honest {thing,answer,report,version,summary,place,way,shape,measure,evaluation}` | 29 uses of "honest/honestly" | 15 | ch03 (5), ch11 (3), ch12 (2) |
| `it is worth {saying,stating,naming,marking,having,being}` | 35 "is worth X-ing" | 20 | ch03 (4), ch05 (5), ch02 (3) |
| `what belongs here is` / `X belongs here` | 21 | 12 | ch04 (3), ch05 (3), ch03 (2) |
| `this section used to` | 4 | 4 | ch08 (3), ch03 (1) |

The counts split because each pattern has legitimate members. "No witness has an honest memory" is
section 3.6's actual subject; "worth building", "worth measuring", "worth pursuing" are ordinary
evaluation; "the technical machinery is covered where it belongs" is a boundary marker. Only the
metadiscursive members are in scope: the ones that announce the author's candor, or announce that
what follows deserves attention, instead of making the claim.

### Contrastive negation (D-025's tic, remeasured)

| Chapter | Words | `not X but Y` | `, not Y` | `rather than` | `is not X. It is Y` | All per 1,000 |
|---|---|---|---|---|---|---|
| ch01 | 1,959 | 0 | 2 | 6 | 0 | 4.08 |
| ch02 | 13,483 | 7 | 10 | 53 | 6 | 5.64 |
| ch03 | 11,203 | 3 | 8 | 47 | 1 | 5.27 |
| ch04 | 8,294 | 1 | 2 | 41 | 3 | 5.67 |
| ch05 | 11,396 | 3 | 2 | 39 | 5 | 4.30 |
| ch06 | 10,910 | 4 | 20 | 34 | 1 | 5.41 |
| ch07 | 4,075 | 1 | 1 | 10 | 3 | 3.68 |
| ch08 | 8,112 | 2 | 6 | 20 | 4 | 3.94 |
| ch09 | 6,774 | 2 | 12 | 32 | 0 | 6.79 |
| ch10 | 7,994 | 2 | 9 | 19 | 3 | 4.13 |
| ch11 | 7,069 | 2 | 5 | 34 | 2 | 6.08 |
| ch12 | 3,118 | 4 | 12 | 15 | 2 | 10.58 |
| ch13 | 2,919 | 1 | 13 | 17 | 0 | 10.62 |
| **all** | **97,708** | **33** | **102** | **367** | **30** | **5.44** |

D-025's calibration set is the author's own hand revision of chapter 1, which runs at 2.90 per
1,000. The book is at 5.44, roughly double, and P12 swept only chapter 5. The two worst chapters
are the two the author has not been shown a tic pass on: the conclusion at 10.58 and the glossary
at 10.62.

### Cross-references

883 `\ref` instances in 709 sentences. 125 of those are the glossary's parenthetical locators,
which are navigation by construction, leaving **758 in the prose** — close to the author's estimate
of 680, and worse than it.

| Chapter | Refs | Words | One per |
|---|---|---|---|
| ch01 | 27 | 1,959 | 73 |
| ch02 | 81 | 13,483 | 169 |
| ch03 | 145 | 11,203 | 78 |
| ch04 | 66 | 8,294 | 128 |
| ch05 | 88 | 11,396 | 132 |
| ch06 | 70 | 10,910 | 158 |
| ch07 | 44 | 4,075 | 93 |
| ch08 | 43 | 8,112 | 191 |
| ch09 | 57 | 6,774 | 121 |
| ch10 | 29 | 7,994 | 278 |
| ch11 | 64 | 7,069 | 112 |
| ch12 | 42 | 3,118 | 76 |

P28 cut 79 of these by class eight days ago and reached 10 percent against an instruction of 50,
recording the cause: judging removability from an isolated sentence overestimated it threefold.
That is the blind spot this pass is designed around, and the design is that **every candidate is
read in its paragraph, not in its sentence**, and that the test is what the paragraph loses.

---

## What gets cut, and what does not

The author's criterion is a semantic one — *navigation stays, agreement goes* — so the classes
below are a way of finding candidates, not a rule for removing them.

### Cut

1. **Agreement notices.** The sentence's whole work is to report that another section reaches the
   same place. "Sections 8.2.2 and 10.10 make the same point about deliberation and about majority
   rule." "…and section 5.7.1 says the same thing about play." "Section 9.3.4 makes the same point
   about people inside institutions."
2. **Appositive filing labels.** A noun phrase appended to a finished claim whose only job is to
   name which section owns the idea. "…which is section 6.4.4's problem in its ordinary, non-state
   form." "The general case is section 4.1.2's." "Bandura's social learning is already section
   5.1.2's."
3. **Bill-arrives-later pointers.** Chapters 2, 4 and 5 announcing that chapter 3 will need what
   they just said. "…and chapter 3 is where the bill for it arrives." "That distinction is the
   whole of what this section contributes to chapter 3." "The question running underneath is
   chapter 3's."
4. **Contentless pointer sentences.** "Section 2.4.4 gets simpler and firmer." "Section 7.2 gets
   close to this." "Section 5.4.3 develops the underlying point."
5. **Repeats.** The second and later references to one target inside one section, where the first
   did the work.

### Keep

1. **Chapter 1's roadmap**, chapter 11's enumerated problem list, and the section-map openers of
   chapters 9 and 12. These are the book's navigation and the reader asked for them.
2. **The glossary's 125 locators.** A glossary entry with no locator is a definition the reader
   cannot get back from.
3. **Any reference that imports something the sentence needs and does not restate** — a result, a
   definition, evidence, an objection. Removing one of these leaves a claim unsupported, which is
   the P14 failure: section 10.1.1's five institutions were sourced only by a cross-reference, and
   emptying it left them unsourced for weeks.
4. **Boundary markers.** "The technical machinery is covered where it belongs: meta-learning at
   4.1.3, lifelong learning at 4.1.2." A reader who wants it needs the address.
5. **Section 3.9**, whose subject is the handoff to the rest of the book, and chapter 3's opener,
   whose references are the argument. P28 protected both and the reason has not changed.

### Editorial archaeology, cut without exception

A separate rule and a stricter one, because the author's instruction is unconditional. Fourteen
passages describe the book's own revision history: what an earlier draft said, what a section used
to concede, what the author no longer thinks. They are cut, and where the passage was making an
argument *by means of* the history, the argument is restated without it.

The one place a process statement stays is **chapter 0, "On Method"**, which is a disclosure about
how the book was made and is the reason the archaeology elsewhere is redundant.

---

## Results

86 section files, 98,134 words to 97,092 by `section_stats.py`, 198 pages to 197. No claim was added, removed or
reversed, and no citation was touched.

### The mannerisms

| Shape | Before | After | What is left |
|---|---|---|---|
| `the honest {thing, answer, report, …}` | 15 | 0 | One "honest statement" in section 2.1.4, where honesty is the subject |
| `it is worth {saying, stating, marking, …}` | 20 | 0 | 15 evaluative uses — "worth building", "worth running", "worth pursuing" |
| `what belongs here is` / `X belongs here` | 12 | 0 | "Explanation belongs here too" at section 6.3.3, an ordinary placement |
| `this section used to` | 4 | 0 | — |

A fifth family turned up in the same sweep and is the same move in a different costume: **the
announced concession**. "I would rather say so here than let a reader find it out." "I am not
going to pretend the field has done it." "Which I would rather put in the accounting than leave
for a reviewer to find." Six of nine were cut, on the rule that the concession stays and the
announcement of it goes. The three kept are doing work a reader needs: chapter 3's invitation to
find the falsifier, section 8.3.3's disowning of the obsolescence forecast before it uses the
numbers, and its statement that it will not plead incompetence on the fiscal question.

### Editorial archaeology

Fifteen passages, all cut. The concentration was section 8.3.3, which carried six — an earlier
draft's plea of incompetence, an objection "treated as decisive in an earlier version," a dropped
phrase, a withdrawn concession on status, and the observation that the section's strongest
argument was "the one the earlier draft conceded away." Chapter 3 carried five, chapters 10 and 11
two each.

**Where the history was carrying an argument, the argument was restated without it.** Section
3.4's "the argument I made here previously ran the first sense into the third" becomes "the easy
argument here runs the first sense into the third," which makes the same point against a reader's
likely inference instead of against a dead draft. Section 8.3.3's "this section used to concede
that a guarantee preserves nobody's earnings or status" becomes "the concession that looks
unavoidable is…", and the paragraph that follows still inverts it. Sections 10.6 and 10.10 both
said "I no longer think that is right" about the democratic dividend; both now say it is not
right.

### Cross-references

**883 to 805; in the prose, 758 to 680.** The glossary's 125 locators were not touched, on the
ground that a glossary entry without one is a definition a reader cannot get back from.

| Class | Cut |
|---|---|
| The "arriving / same point / same thing" appositive | 19 |
| Trailing appositives that file a finished claim under a section | 12 |
| Filing labels — "which is section N's subject" | 12 |
| Chapter-3 pointers in chapters 2, 4 and 5 that announce the connection without using it | 11 |
| Chapter 3's references to its own sections, where the claim stands without the address | 11 |
| Contentless pointer sentences — "Section 7.2 gets close to this" | 8 |
| A chapter or section referring to itself by number | 4 |
| Duplicate pointer to one target inside one section | 1 |

**The largest single family was one construction.** Twenty-five sentences ended in some version of
*X, arriving here as Y* — "section 3.1's custody problem arriving at the point of formation,"
"section 7.1's structure arriving in a benefits office a decade early," "section 9.3.3's
requirement arriving here under a different name." It is the book's habit for noting that a
pattern recurs, and it is the exact thing the instruction describes: the sentence has finished its
work and the clause adds a filing location. Nineteen went. Six stayed, because in those the clause
imports something the sentence needs — section 3.3's custody objection *at the quorum* is a
sharper form of the objection and not a restatement of it.

**Four references pointed at the section or chapter containing them.** Section 8.1.1 cited "what
section 8.1.1 recommends"; chapter 3 said "the refusal capacity chapter 3 asks for" three times.
These print as circular instructions to a reader who is already there.

### What was measured and did not need cutting

**The contrastive construction is mostly load-bearing, and the rate measure does not find the
tic.** Book-wide it runs at 5.15 per 1,000 words against chapter 1's calibration of 2.90, and the
two highest-scoring chapters are the conclusion at 10.58 and the glossary at 10.62 — both high
because their content is genuinely contrastive. Section 12.2.1 states one standard five times as
"met when X, not when Y," which is its structure and not a tic; the glossary distinguishes terms
for a living. Chapter 6's 25 instances were read one by one and 24 are precision.

What does grate is the **pile-up**: two or more contrastives inside one sentence. There were 27;
13 were repaired and 20 remain, of which the survivors are deliberate parallelism (chapter 3's
four-item recap of section 2.3.4, the "not represent it, not score it, not retrieve it" triple).
The 340 surviving instances of "rather than" were **not** swept individually. That is the P12
treatment applied to twelve chapters and it is a pass of its own; this one took the pile-ups and
the shapes the instruction named.

### A defect found while reading

Section 6.3.5 restated section 6.1.3's COMPAS sentence nearly word for word while citing 6.1.3 as
making "the sharper version of the same point" — the duplication and the agreement notice in one
sentence. Rewritten to keep the case and drop the restatement.

### What was not done

- **The 340 "rather than" instances** were not individually judged. See above.
- **No section was removed or renumbered.** Folding a thin section would move numbers against 680
  resolved references, which is the reason P29 gave for declining the same move.
- **Chapter 1's roadmap, chapter 11's enumerated problem list, and the section maps opening
  chapters 9 and 12 are intact.** They are navigation and the instruction protects them.
- **No section has the author's read.** 86 rows carry D-099 and 18 moved from `accepted` back to
  `drafted`.
