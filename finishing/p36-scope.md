# P36 — the recurring-conclusion cut (D-100)

The author's instruction, in full:

> Cut approximately 5,000 words. The narrative is about 97,000 words before the glossary and
> references, and the same conclusions recur across too many chapters.

This file is the scope: what the measurement found, what came out, what did not, and the exact
distance between what was asked for and what the named class turned out to contain.

---

## The premise, checked first

**The baseline figure is off by the glossary, in the direction that matters.** By
`section_stats.py`, the book was **97,092 words** — but that total *includes* the 2,934-word
glossary, chapter 13. The narrative before the glossary was **94,158**. The bibliography is not in
the count at all; `refs.bib` is a separate file and `section_stats.py` never reads it.

So "about 97,000 before the glossary" was really about 94,000, and the glossary is out of the cut
by the instruction's own framing. Nothing in chapter 13 was touched.

## The measurement, before

Four independent measurements of "the same conclusions recur," over the 169 section files.

### 1. Semantic recurrence, paragraph level

Every paragraph of 30+ words embedded and compared against every paragraph *earlier* in the book
(`paraphrase-MiniLM-L6-v2`, cosine, backward-looking only, cross-section only). 998 paragraphs.

| threshold | paragraphs echoing something earlier | words |
|---|---|---|
| ≥ 0.75 | 60 | 7,321 |
| ≥ 0.72 | 126 | 14,986 |
| ≥ 0.70 | 193 | 22,665 |

The highest-scoring section pair in the whole book was **3.9 ↔ 11.2 at 0.896**. The next four all
involved chapter 11 or chapter 12 against the chapter the material came from.

### 2. The five-step spine chain, written out in full

Chapter 3's argument — a floor held as a reason, holding a reason requiring outcomes to matter,
mattering being affective, the bearer carrying a persistent self, suffering following — stated with
**two or more of its five links** in one paragraph:

| section | par | words | links |
|---|---|---|---|
| 1 | p2 | 291 | 3, 5 |
| 2.4.4 | p5 | 179 | 2, 3 |
| 2.4.6 | p3 | 192 | 2, 3, 5 |
| 3 | p8 | 214 | 1, 4 |
| 11.2 | p0 | 115 | 3, 4, 5 |
| 13 | p18 | 158 | 1, 3, 5 |

**6 paragraphs, 1,149 words, in 5 chapters.** This is the author's complaint in its strictest form,
and it is smaller than it feels when reading.

### 3. Pointer-plus-recap sentences

A sentence that points at another section *and* reports what that section concluded, 22 words or
longer: **288 sentences, 11,664 words, 12.4 percent of the narrative.** What gets recapped:
chapter 3 eighty times, chapter 2 sixty-five, chapter 5 forty-one.

**This is the largest pool and the most misleading.** Read one by one, most of these sentences
*use* the result they name — the sentence does not work without it. The recurrence is in the
subset where the recap is a reminder rather than a premise.

### 4. Near-duplicate sentences across sections

Content-word overlap ≥ 0.42 between sentences in different sections: **40 pairs**. Two were
**word-for-word identical** (section 2.1.4 and chapter 7's opener, 57 words). Six more were
near-verbatim re-explanations of a method or a case introduced elsewhere.

---

## What was cut

### Section 3.9 removed entire — 610 words

*What Follows for the Rest of the Book* was 610 words distributing chapter 3's conclusion to five
destinations. **Every one of the five states its own version, in its own place, better:**

| 3.9 said | the destination says it at |
|---|---|
| section 2.4.4 "gets simpler and firmer" | 2.4.4 p5, 179 words |
| the Three Rs and the pet trust become applicable law | 2.4.6 p3 and 9.3.2 p3, 192 and 186 words |
| chapters 4 and 5 acquire an obligation | chapter 4's opener and chapter 5's opener |
| chapter 7 stops being fairness to annotators | 7.3 p11–p12, 239 words |
| what is owed to a bearer goes to 11.2 | 11.2 p0 |

**Nothing in the book pointed at it** — zero inbound `\ref`, against ten for section 3.8 beside it.
Section 3.8's closing paragraph already states the chapter's proposition, names section 3.3 as
where to attack it, and sends the unsettled question to section 11.2, so the chapter still ends
where it ended. Section 2.4.4 already carries the "infant, an animal, a person permanently without
capacity" formulation 3.9 restated. Nothing was carried forward.

It was the last section of its chapter, so **nothing renumbered**. 169 sections to 168.

A search for other sections of the same shape — high recap fraction, no inbound references, over
60 words — returned **no second instance**. Section 3.9 was the only one.

### The spine chain, cut to a pointer at four of its six sites

Kept in full at chapter 3 (its home) and in chapter 1's roadmap. Cut to the pointer at:

- **2.4.4** — "a bearer capable of the refusal the floor requires has to hold something as
  mattering, the only demonstrated way … is affective, and a system built that way cannot be
  certified not to be hurt" → "a bearer has interests that its situation can set back." (−44)
- **2.4.6** — the three-clause chain before the Three Rs are applied to it (−52)
- **9.3.2** — the chain before the pet-trust instrument is fitted to it (−35)
- **11.2** — the chain before the section states the gap it is about (−54)

The sentence each one was attached to still does its work; what went was the reminder in front of
it.

### Chapter 3's internal triple statement

The chapter stated its conclusion at the opener, at 3.8, and again at 3.9. With 3.9 gone:

- the opener's **five-step pre-summary** (214 words) now names the five steps and stops, instead of
  also pre-stating the conclusions of steps three and five that sections 3.3 and 3.4 then argue.
  The "steps three and four are where a reader should press" paragraph folded into it (−80)
- **3.1** stopped previewing the charge and said where it is stated: it had ended "Section 3.8
  states that charge at full strength," having just stated the charge (−57)

### Verbatim and near-verbatim duplication

- **chapter 7's opener** reproduced **two sentences of section 2.1.4 word for word** (−57)
- **11.5** re-explained debate and weak-to-strong generalization, both set out at 4.2.6 (−86)
- **9.2.1** pointed at 6.4.2 for federated learning and homomorphic encryption *and then explained
  both again*; the Gboard and Estonian tax cases, which are what is new there, are kept (−78)
- **6.1.3** restated 6.1.1's COMPAS figures while citing 6.1.1 as its source (−22)
- **7.1 and 8.3.3** each restated 9.3.4's dissent/tribute formulation, in one case verbatim (−34)
- **6.4.4** re-explained 10.8's China rules and 9.2.1's federated designs (−33)

### Recaps that reproduce a list or a case the target section holds

The pattern is a colon followed by the target's own content. Cut to the pointer at **9.3** (three
questions that are the titles of the three subsections that follow), **9.3.2** (2.4.5's three legal
options), **9.3.3** (2.4.6's Three Rs, spelled out), **10.2** and **10.8** (10.8's treaty list and
6.4.1's six misuse forms), **10.7** (11.9's responsibility gap), **12.2.1** (2.2.2's theory-of-mind
specification), **12.2.2** (11.4 and 11.5, both spelled out), **5.4.3** (6.4.1's case in full),
**5.7.1** (5.5.1's multi-agent training), **6.2.1**, **6.4.1**, **4.1.3**, **4.1.2**, **4.2.2**,
**4.2.3**, **4.2.4**, **5.1.1**, **5.6.3**, **6.1.1**, **2.2.2**.

### Chapter openers that re-derive what they inherit

**Chapter 4's opener** re-derived chapter 3's handoff in 104 words; it now names it in 55 and lets
section 3.8 carry the derivation. **Chapter 5's opener** stated the same handoff twice, once as a
pointer and once in full; the second went. **Chapter 1** argued the safety/ethics distinction at
249 words and chapter 3's opener argues it again at 382; chapter 1 now states it and chapter 3
still argues it. **Section 2.1's opener** flagged the deontology point that section 2.1.1 makes six
paragraphs later and chapter 3's opener makes a third time (−82).

**Chapter 1 and chapter 5's openers are author-hand-revised sections.** Both edits are disclosed
here and in `ledger.tsv` rather than applied silently.

---

## What was kept, and why

- **The glossary, untouched.** 2,934 words, and by the instruction's own framing outside the cut. A
  glossary entry restating a conclusion is a glossary working.
- **Chapter 3's opener and section 3.8.** 3.8 is where the chapter's conclusion lives; it is the
  home, not a recurrence. Its qualifications — that section 3.4 establishes a bearer's
  non-suffering cannot be certified rather than that a bearer suffers, and that the result does not
  depend on Cassell — are P34's work and load-bearing.
- **Most of the 288 pointer-plus-recap sentences.** Read individually, the recap is the premise of
  the sentence carrying it. Cutting them produces pointers a reader has to chase.
- **Chapter 2's opener** (52 words of chapter 3's conclusion). P29 rewrote it around exactly the
  four results chapter 3 uses; cutting it reverses standing work eight days old.
- **Chapter 11's nine-item priority list** (233 words summarizing the nine sections that follow).
  The ranking is D-092's content and the section order alone does not state it.
- **Chapter 7's three instances.** The chapter argues one structure three times because three
  instances *is* the argument.
- **The 40 near-duplicate pairs that are motifs rather than repetition** — chapter 1's "perfectly
  deliberative process … has produced a faultless output" and its variant at 8.2.2, which is the
  book's thesis restated on purpose.

---

## Results

| | before | after |
|---|---|---|
| sections | 169 | **168** |
| words (`section_stats.py`) | 97,092 | **95,041** |
| narrative, chapters 0–12 | 94,158 | **92,107** |
| glossary | 2,934 | 2,934 |
| PDF pages | 197 | **192** |
| `\ref` | 805 | 785 |

**2,051 words cut. 37 section files changed and one removed.** No claim added, removed or
reversed; no citation touched; no case, study or piece of evidence removed; nothing renumbered.
`check_all.sh` green, both formats build clean.

Two cuts went too far and were repaired on re-reading, recorded rather than hidden: section 9.3.2
was left with "those three options" after the three options were cut, and sections 12.2.2 and 10.7
were reduced to bare pointers that no longer carried why the pointed-at result mattered. All three
were restored to a working minimum.

---

## What was not done: 2,051 against approximately 5,000

**The named class does not contain 5,000 words, and this is the finding to carry forward.** Four
measurements agree:

- the whole-section instance: **one**, 610 words
- the spine chain stated in full: **1,149 words** across six paragraphs, of which the home
  statements have to stay
- verbatim and near-verbatim duplication: **about 300 words**
- the 11,664-word recap pool: read one by one, the compressible fraction is **roughly a fifth**

The reason is in the repository's own record. This book has been cut on this axis five times
already — P11 took chapter 4 down 29.9 percent, P29 took chapter 2 down 20.2 and chapters 4 and 5
down 13.5, P28 cut 79 cross-references, P35 cut 1,042 words of mannerism and archaeology and
another 78 references. The redundancy that remains is mostly load-bearing connective tissue that
D-078 and D-090 **deliberately added**, eight and one days before this instruction, to make
chapters 4 and 5 carry chapter 3's obligation. Cutting further into it reverses standing decisions
rather than removing cruft.

**Reaching 5,000 means cutting something other than recurrence.** The costed options, none taken
here because none is what the instruction names:

- **Q-027 (b)** — cut the evidence in chapters 4 and 5: the inattentional-blindness studies, the
  predictive-coding account, the Kohlberg box, the trolley literature. Reaches roughly 20 percent
  on those chapters, about **1,900 words**, and converts several claims into assertions a reader
  has to take on trust. Section 2.3.4 depends on the trolley material being somewhere.
- **Q-029 (b)** — fold the twelve leaf subsections now under 230 words. Saves little text on its
  own and renumbers chapters against 785 resolved references.
- **Chapter 11's problem statements** — each of nine sections opens by restating the problem from
  the chapter it came from. About **900 words**, and it undoes D-092's requirement that a
  researcher entering at any section finds the problem named.
- **The remaining four-fifths of the recap pool** — about **2,300 words** available by compressing
  sentences whose recap is the premise. Produces pointers a reader has to chase, which is the cost
  P28 named when it declined to cut references by rate.
- **Chapter 3's opener and section 3.8** — about **800 words** by making the chapter state its
  conclusion once instead of at both ends. This is the only remaining option inside the named
  class, and it cuts the book's central chapter.

Filed as **Q-039** with the default: stop at 2,051 and leave the rest with the author.
