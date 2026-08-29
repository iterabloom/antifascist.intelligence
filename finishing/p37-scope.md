# P37 — inventories in chapters 8–10, and the jobs guarantee halved

The author's instruction, in two parts: *"In Chapters 8–10, replace inventories
with fewer worked cases. And the jobs-guarantee section could probably be half
its current length."* D-101 records it. This file is the scope, the measurement
behind each figure, and what was declined.

## Part one: the inventories

### The measurement, and what it does not support

A tool was written for this pass, `finishing/tools/inventories.py`. It flags a
sentence carrying a series of three or more coordinated items and reports words,
citation count and explicit `enumerate`/`itemize` items per chapter. Run over all
168 sections:

| ch | words | series sentences | uncited | words in them | % of chapter |
|---|---|---|---|---|---|
| 2 | 13,121 | 86 | 74 | 3,301 | 25.2% |
| 3 | 10,394 | 54 | 49 | 1,974 | 19.0% |
| 6 | 10,664 | 54 | 45 | 2,268 | 21.3% |
| **8** | **7,981** | **44** | **36** | **1,625** | **20.4%** |
| **9** | **6,543** | **30** | **25** | **1,255** | **19.2%** |
| **10** | **7,884** | **68** | **53** | **2,857** | **36.2%** |
| whole book | 95,041 | 551 | 469 | 21,487 | 22.6% |

**On this measure chapters 8 and 9 are at or below the book average and only
chapter 10 is an outlier.** That is the first thing to say, and it does not
refute the instruction. The syntactic test finds a series inside one sentence.
It is blind to the shape that actually produces the reading experience the
instruction names — an inventory spread across consecutive sentences or
paragraphs, one item each, no case behind any of them:

> Regulators set the legal boundaries around data, privacy, and accountability.
> Developers and researchers understand a system's actual capabilities…
> End users find the places a design breaks down… Communities already carrying
> the costs… Civil-society organizations raise the political questions…

That passage scores **one** hit on the tool, for the first sentence. The rest of
the diagnosis was made by reading all three chapters, 22,408 words, section by
section. The tool's output is in the table above and is kept because it locates
chapter 10 correctly and because the false-positive rate is itself the finding:
most three-part sentences in this book are carrying an argument, not listing.

### What was cut, and what was kept

Eleven passages were identified as inventories. Nine were changed; two were kept
with reasons.

**Changed.**

1. **§8.2** — the five-role roll call above, 139 words, one sentence per
   stakeholder and no case. Reduced to the claim and its punchline. The roll is
   gone; §8.2.1 and §8.2.2 do the work it was gesturing at.
2. **§8.2.1** — the four-mechanism list. Kept, because the following paragraph
   takes it apart ("Three of the four make an AI system better informed. One of
   them can stop it"), which is the move the instruction asks for. Only the
   relative clauses hanging off each item were trimmed, since three of the four
   are dismissed in a clause anyway.
3. **§8.1.1** — the survivals roll under *Which of these institutions actually
   lasted*: five institutions, five citations, one sentence each. The prose
   already says the failures are the sharper pattern. Compressed to one sentence
   carrying all five citations; the two failure cases are untouched.
4. **§8.3.1** — the closing remedies inventory ("Public funding for AI research
   that prioritizes democratic values, inclusivity, and human rights… Grants and
   commissions aimed at non-profits…"), 66 words, nothing checkable in it. Cut.
   **This left the section arguing that incentives run one way only**, which was
   caught on re-reading and repaired with one sentence pointing at §9.1, where
   the book treats research funding as a policy instrument.
5. **§8.3.2** — *"Countermeasures exist and are not exotic: antitrust
   enforcement…, mandated data-sharing…, transparency requirements…, and
   funding…"*. Four remedies, no case, none costed. **Replaced with the worked
   case, which was already half-present in the section**: the FTC sued Meta in
   December 2020 over the Instagram and WhatsApp acquisitions the section
   describes; the district court held in November 2025 that the agency had not
   shown present-day monopoly power, TikTok and YouTube being reasonable
   substitutes; the FTC appealed in January 2026. Verified live (below). Two of
   the four remedies survive as the ones that do not depend on winning that
   argument. **This section got longer**, 504 → 559 words, which is what
   "replace an inventory with a worked case" costs and is the instruction
   working as stated.
6. **§8.3.4** — the closing three-measure inventory, 100 words. Reduced to the
   one measure doing work the floor cannot: social insurance reaches people a
   guarantee by construction does not reach. **Two policy claims were removed
   with it** — designing work so AI augments rather than substitutes, and giving
   smaller firms access to AI resources. Neither had a case or a citation.
7. **§9.1** — the four-instrument roll, one paragraph each. Compressed. Two
   inbound pointers constrained this and both were checked first: §8.1.1 points
   here for the split-funding argument and §6.3.6 points here for the
   self-regulation coalition. Both survive.
8. **§9.1.1** — the six-item "predictable shape" of a national AI policy. Kept
   as a list, because the section's whole move is to dismiss it ("The list is not
   where national policies differ"), but shortened: a list that exists to be
   dismissed does not need six items with sub-clauses.
9. **§9.1.2** — the closing run-in carried **three** inventories in four
   paragraphs: a "measurable" triple, a "third-party audits, external advisory
   boards, cross-stakeholder collaboration" triple, and a "four things do the
   checking" quad. Compressed to the record-based test. The OpenAI Charter
   sentence went with them as a single-company restatement of the Partnership on
   AI point made immediately before it.
10. **§9.2.1** — five privacy techniques, one worked. Restructured around the
    two deployed cases and what separates them: Gboard shipped inside a product
    a company was already selling; Estonia's Sharemind pilot processed a month of
    national tax data and was never carried into production. **Nothing technical
    separates them**, which is the finding the parade of five techniques was
    hiding. Data minimization and k-anonymity stay, named, in one sentence.
11. **§9.2.2** — six defenses in one sentence with five citations. Split: the
    four that are practice stay as practice; defensive distillation and
    randomized smoothing are worked against each other, because one was published
    as hardening and broke under attacks written for it while the other offers a
    certified radius — a smaller promise and a kept one.
12. **§9.3.4** — the five-emotion inventory re-explains §2.3.4's account without
    its citations. Reduced to the one signal the paragraph's argument uses,
    shame, with the pointer to §2.3.4 for the rest.
13. **§10.3** — the clearest inventory in the three chapters: four domains,
    one paragraph each, all four making the point the closing paragraph makes
    once. **Cut to two worked cases.** Climate stays because its content is a
    correction (the named framework does not have machine learning in it yet, and
    the real work is national weather services benchmarking against shared data).
    Disease stays because the section's conclusion depends on it. Poverty's null
    result stays as its own paragraph, because a negative finding the book
    actually searched for is not an inventory item. **Conflict prevention and the
    PeaceTech Lab case were cut**, a worked case removed to satisfy "fewer" —
    the one place in this pass where that happened.
14. **§10.4** — the opening re-summary of the EU/US/UK/China bets that §10.8
    then works out at length, and Taiwan as a third jurisdiction after Canada and
    Singapore. The re-summary is now one clause naming the four and pointing at
    §10.8; **Taiwan is cut**. Canada and Singapore stay because the US–Singapore
    certification case at the end of the section runs through Singapore.
15. **§10.8** — **the single clearest instance in the three chapters.** Seven
    bodies in one paragraph, one clause each, seven citations, no case, and the
    prose itself calls it a roll: *"Everything else in this space is voluntary,
    and the roll is longer than it is deep."* Three are kept because the rest of
    the book uses them — the OECD Recommendation (§10.2 refers to it), the HLEG
    Ethics Guidelines (§6.3.6 names them), and the Partnership on AI (§9.1.2,
    §9.3.4 and the glossary) — plus Bletchley and the Safety Institute Network,
    which the paragraph after it needs. **UNESCO, the Global Partnership on AI
    and the G7 Hiroshima process are cut.** What the roll was trying to show, the
    Bletchley → Seoul → Paris summit case shows properly, and it now says so.
16. **§10.7** — the Campaign to Stop Killer Robots paragraph made the point the
    CCW paragraph before it already makes. Compressed to its one distinct fact,
    the UN General Assembly resolution that passes and produces no treaty.

**Kept, with reasons.** §10.9's five development remedies, because the section's
argument *is* that they have been correctly named in successive declarations for
years and the connectivity gap is what happened anyway — an inventory whose
listing is the evidence. §10.7's four-question `itemize`, because the section
then argues that the list misses a fourth party, so the list is load-bearing.
Chapter 8's and chapter 10's opening roadmaps, under P28's rule that a
chapter-level roadmap survives.

### One expectation that failed on inspection

**§9.1.2 was expected to be the chapter's largest inventory and is not.** It
runs nine cases in 1,659 words — Project Maven, GPT-2 and the capped-profit
restructuring, Gebru and Mitchell, *Stochastic Parrots*, the Meta Oversight
Board, Clearview, Rekognition, the Partnership on AI, the OpenAI Charter — and
on reading them one at a time, each carries a claim the others do not. Maven is
the test of a pledge after it is made; the OpenAI pair is erosion *without*
dishonesty, which is the more interesting half; Rekognition is the failure an
outside audit caught and self-regulation did not; Clearview is overstated
capability as a form of the same thing. Only the closing run-in is inventory.
The cut there is 150 words rather than the 400 the section's length suggested.

Cutting Clearview was considered and reversed **because it would have stranded
half a glossary entry**: the glossary calls Clearview "the book's standard case
of overreach and regulatory response: marketed accuracy claims independent
testing did not support, and fines from French and Italian regulators," and
§6.4.3 carries only the fines. That is the D-050 failure class, and it would have
been created by this pass rather than found by it.

### The pointer this pass did break, and fixed

Cutting §10.3's poverty paragraph removed the sentence carrying its only mention
of the digital divide, and the glossary's *digital divide* entry pointed at
§10.3 for it. The entry now points at §10.1, which treats the resource line as a
membership condition on cross-border collaboration, and §10.9, which is the
section about it.

## Part two: the jobs guarantee

**3,212 words → 1,842, which is 57 percent and not half.** The number is reported
rather than the instruction's estimate, which carried "probably."

The first attempt trimmed every head proportionally and reached 2,214 words, 69
percent. That was the wrong method and is recorded because the second method is
the finding: **halving needs a decision about what the section is for, not a
tighter version of everything it already does.** The title says what it is for —
a jobs guarantee, and the objection it has to answer — and the objection is the
placement lever under a hostile administration, which the section reaches in its
last head.

What changed structurally: eight run-in heads became five. *The budget frame is
this book's own signature*, 424 words, is gone as a head; its load-bearing
sentence — that reading this as an arithmetic question is §2.1.4's second
structural feature working on public finance — survives inside *What it would
cost*. What went with it was the meta-commentary on why arithmetic felt like the
question and the note about not sorting an argument by who is making it. *Skill
mismatch is not the objection*, *Training is the mechanism* and *Status, and
against which baseline* were three heads answering three imported objections at
full argumentative length; they are one head now.

**Every citation but one is kept**, and every argument. The exception is
`justcapital2018amazongo`, the Amazon Go cashier-less store, a second
displacement case where the 5.7-million-manufacturing-jobs figure already carries
the point — the same "fewer worked cases" rule applied inside the section.

**What was deliberately not cut**, because cutting it would remove the honesty
the section runs on: the note that the 4-percent figure is stipulated rather than
derived and is not a bound; the admission that the strongest objection to the
monetary premise has no settled answer here (`palley2015money`); and the residual
that a guarantee cannot preserve relative standing within a profession. Each is a
place the section concedes something, and a compression that quietly dropped
concessions would be reporting a shorter and more confident section than the book
actually has.

**Two defects found by reading the rewrite, one of them pre-existing.**

- §8.3.3 said the understaffed job categories are "those in section 8.3.4's
  list." **§8.3.4's list has never contained a job category** — it lists
  retraining, social insurance, work design and small-firm access. The reference
  resolved and named a claim its target does not make, which is exactly the class
  `check_xrefs.py` states it cannot catch and `xref_content.py` did not flag,
  because the citing sentence names no proper noun. It predates this pass and is
  now fixed by naming care and environmental repair directly.
- Renaming the merged head to *Skill, training, and status* left a paragraph
  opening "The third is that a guarantee preserves nobody's earnings or status,"
  which had lost its antecedent. Found on the rasterized page, not in the source.

## Verification

One claim in this pass is new and was verified live on 2026-08-29, per D-030:

- **C0760** — *FTC v. Meta Platforms, Inc.*, No. 20-3590 (D.D.C.), judgment for
  Meta 18 November 2025 after a six-week bench trial; the court found the FTC had
  not shown Meta currently holds monopoly power, TikTok and YouTube being
  reasonable substitutes, so the personal-social-networking market as pleaded was
  too narrow. Verified against a law-firm case summary carrying the caption and
  docket number and against contemporaneous reporting.
- **C0761** — the FTC filed a notice of appeal to the D.C. Circuit in January
  2026. Verified against the Commission's own press release.

`ftc2020metaplatforms`'s note field, which already recorded the November 2025
ruling in one sentence, now carries the caption, the docket number, the ground of
decision and the appeal.

## Citations left uncited

**Eight** bib keys lose their only manuscript citation in this pass and join the
count Q-030 tracks: `justcapital2018amazongo`, `openai2018charter`,
`moda2025basic`, `peacetechlab2019monitoring`, `unesco2021recommendation`,
`gpai2020joint`, `g72023hiroshima`, and `deepmind2016partnership` — the last
because §10.8 now cites the Partnership on AI through `partnershiponai2016`, the
key §9.1.2 and §9.3.4 already use, rather than through a second entry for the
same body, which is the de-duplication P33 did for Irving. Counted rather than
estimated: `refs.bib` has 304 entries, 282 are cited, and **Q-030's figure moves
from 14 to 22**. No entry was deleted; the decision to prune is Q-030's and has
not been taken.

## Numbers

| | before | after |
|---|---|---|
| chapter 8 | 7,981 | 6,447 (−19.2%) |
| chapter 9 | 6,543 | 6,390 (−2.3%) |
| chapter 10 | 7,884 | 7,515 (−4.7%) |
| chapters 8–10 | 22,408 | 20,352 (−9.2%) |
| §8.3.3 alone | 3,212 | 1,842 (−42.7%) |
| whole book | 95,041 | 92,986 |
| pages | 192 | 189 |

Chapter 9 moved least, and the reason is the §9.1.2 finding above rather than a
lighter hand: its cases mostly carry distinct claims and its inventories are
confined to section openers and one closing run-in.

Sections changed: 18, across four chapters and the glossary. Four moved from `accepted` back to `drafted` (§§8.2.1, 8.3.2, 9.1.1, 9.2.2), leaving 16 accepted and 152 drafted. No section added or
removed, nothing renumbered. `check_all.sh` green; both formats build clean, no
undefined references.

## What is not done

No section has the author's read. The proof pair in `finishing/reports/` is the
2026-08-29 P36 build and does not carry this pass.
