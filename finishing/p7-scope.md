# P7 — Editorial review response

**Source:** an editorial review of the P6 book, read 2026-08-23. Its diagnoses were
checked against the manuscript before this scope was written; what is listed here
is what survived that check. Two of its claims did not survive and are recorded at
the bottom so they are not silently reintroduced.

**What unblocked this pass.** Four constraints were raised against the review's
prescriptions and all four were ruled on by the author the same day:

| Objection raised | Ruling |
|---|---|
| Arguing the thesis where it is assumed was ruled out | **D-026** — reopened. The exclusion was only ever against giving the case *against* democracy the time of day. |
| The targeting material collides with the dateless-prose spec | **D-027** — "so be it." It goes in dated. |
| It asks the book to discuss the vendor whose model wrote it | **D-028** — "so disclose it." Chapter 0 gains the disclosure. |
| P6 is closed and pushed | New pass opened. |

D-007 still governs everything not named here. This is not a license to re-argue
the book.

---

## Tier A — copyedit class, no new argument

These need no decision. Each was verified present in the manuscript.

| # | Where | What | Verified |
|---|---|---|---|
| A1 | §5.1.1 | Zhao et al. is mis-described. The text says cooking images were captioned as showing a woman "about a third more often than the underlying images actually did" — that describes captions diverging from ground truth. The finding is **dataset composition** skew (~33%) **amplified by the trained model** (~68%). Rewrite; also relocate, since it is not a labeling finding and sits under a "Data Labeling" header. | yes |
| A2 | §2.1 / §2.1.1 | Parent enumerates consequentialism, deontology, capabilities, virtue. Child enumerates consequentialism, deontology, virtue, care, contractualism. Capabilities vanishes; care and contractualism arrive unintroduced. Reconcile. | yes |
| A3 | §§10.1.1, 10.1.2, 10.1.3, 2.3.3, ch2 intro, 6.3.1 | Revision history visible in the finished text: "this section's old title," "the list this section used to offer," "earlier drafts of this book," "the chapter's title has been changed to say so plainly," "nothing in this section's own research turns up a gap." Readers have no access to the old titles. Delete the scaffolding, keep the content. Chapter 0 licenses transparency about method, not about drafts. | yes — all six, incl. 10.1.1 which the review missed |
| A4 | ch11 glossary | Attention-schema entry points to §3.1.2, which never mentions Graziano or the attention schema. Stale pointer. | yes |
| A5 | §2.3.3 | Graziano's account discussed with no `[[cite:]]` placeholder. | yes |
| A6 | §6.4.2 | "preposterous reductions such as…" — the point is right and necessary; the register is the only sneering sentence in the book. | yes |
| A7 | §§3.1.2, 4.4.6, 5.4.1, 7.2.5, 7.5, 10.2.1 | The dual-use point ("same underlying capability; the difference is governance, not engineering") is made six times in near-identical phrasing. One home, cross-references elsewhere — D-013's rule, applied to a cluster D-013 missed. | yes — six sites, not the five the review claimed |
| A8 | §7.2.4 and the routing tic generally | 297 numbered section references book-wide. §10.2.1 carries 12 in 738 words; §10.1.3 five in 216; §7.2.4 is two paragraphs of which the first is pure pointer and says so. Delete sections that exist only to say where their content went; thin the rest. | yes |
| A9 | §2.1.3 | The UDHR's eight abstentions were the Soviet bloc, Saudi Arabia, and South Africa — precisely the cases the surrounding cultural-variation argument aims to rule out. A footnote strengthens the point. | to verify |
| A10 | §1.1 | One citation carries four disparate threats; racial capitalism is listed among things AI could "help address" and §5.1 cashes it out only as "a system audited for disparity works against that pattern." | to verify |
| A11 | §10.2.1 | Promises five milestones, delivers one epistemic principle applied five times. The principle is right. Restructure as one principle plus five worked cases and say so. | yes |

## Tier B — substantive, authorized by D-026 / D-027 / D-028

| # | Where | What | Gate |
|---|---|---|---|
| B1 | §2.1.4 | **The central fix.** "Antifascist" is asserted as a design specification across the whole book and never becomes one. Port a structural definition: recuperation of dissent, aestheticization of the metric, coding of exception as betrayal, decoupling of the model from the world it claims to track — plus the molar/molecular scale distinction (Deleuze and Guattari, plateau 9). Add the features specific to fascism as against authoritarianism in general: mass mobilization, leader cult, scapegoated out-group, contempt for procedural legality as such, deniability as technique. Those are detection targets; "concentrated, unaccountable power" is not. | D-026 |
| B2 | new §9.1.7 | What remains open: why the general framing yields no operational targets, what a detector would actually have to detect, and why the hard part is discriminating a fascist movement from ordinary political hardball without a false-positive rate that makes the tool useless or dangerous. Belongs in the chapter built for open problems. | D-026 |
| B3 | ch7 accountability | **The slope, not the level.** Whether a dissent mechanism has been captured is a derivative, not a threshold: is the cost of registering dissent rising year over year while the underlying risk stays flat? Measurable, resistant to gaming, generalizes. | D-026 |
| B4 | §5.4.1, §4.4.6 | **Democracies build this.** §5.4.1's six documented forms of authoritarian AI misuse cast democracies as the party that regulates. The two most sophisticated AI targeting systems on record were built by democracies. Israeli: Habsora, Lavender, "Where's Daddy" — the human bottleneck as stated design goal, ~37,000 marked, a ~10% error rate, and **twenty seconds** of human review per target — "I had zero added value as a human, apart from being a stamp of approval." American: Maven Smart System. (The review's "three minutes" and "two sources cut to one" did not verify and are dropped — see the verification log below.) §4.4.6 needs the hard case where a democracy's own AI apparatus is what is under scrutiny by its own press and courts. | D-027; **every factual claim verified before it lands, D-009** |
| B5 | §7.5 | **The vendor as a named party.** Accountability currently runs operator → command → developer, and "developer" appears once, abstractly. The live actor is a model vendor supplying a defense contractor's targeting platform, with a published use policy, no logging obligation, and no right of inspection. Neither command responsibility nor product liability reaches it. | D-027, D-028; verify |
| B6 | §7.5 / §9.1.1 | **"I do not know whether my system was used"** as a named failure mode, distinct from Matthias's responsibility gap in §9.1.1. Matthias is distributed causal *control*; this is absent causal *visibility* — an instrumentation choice, not an inherent property of learning systems, and therefore fixable. Naming it fixable is the useful move. | verify |
| B7 | §4.1.4 → ch7 | **Targets-per-hour against reviewers-available.** §4.1.4 has been promising "the right indicators" since chapter 4 and has never named one. This is measurable, auditable in principle, tests directly whether "meaningful human control" means anything in a given deployment, and generalizes to any AI-assisted decision system with a nominal human check. | D-026 |
| B8 | ch5 epigraph | The Unit 8200 commander's "human bottleneck" line — a design document stating that human deliberation is the constraint to be engineered around. Everything in the book about meaningful human control argues against that sentence. Quoting beats paraphrasing. Attribution line required (D-009); the author wrote pseudonymously. | D-027; verify |
| B9 | §7.5 | **Decompose the democratic dividend** from a binary property of having institutions into three separable failures: (i) **reach** — a democracy's AI can be fully accountable to its electorate and entirely unaccountable to the people it is pointed at; (ii) **findings without consequences** — mechanisms that work as mechanisms and fail as checks; (iii) the countermajoritarian half. Sen is cited in §10.1 and unused in §7.5, and his argument is about public reasoning and the capacity to demand accountability, not the ballot. | D-026 |
| B10 | ch6 | **The aggregating/constraining gap.** Every governance mechanism the book proposes — citizen assemblies, public consultation, participatory governance, deliberative polling, vTaiwan — sits on the aggregating side. All make public preference more legible and actionable; none protects anyone from it. §9.1.6 comes close but frames it as a data-quality problem. The missing machinery is what *constrains* preference: rights that do not depend on being popular, courts that rule against a government holding the votes, limits not repealable by whoever won last, standing for people outside the demos. **This is not an argument against democracy and D-026 explicitly does not exclude it.** It is what lets the book finally say what makes a system antifascist rather than merely responsive: *not that it tracks what people want, but that there are things it will not do to a person no matter who wants it.* | D-026 |
| B11 | ch0 | **Vendor disclosure.** Which models did the work, whose they are, and that the book criticizes that company by name in chapter 7 and does not soften it. | D-028 |
| B12 | §2.4.1, §2.4.4 | **The persistence argument.** §2.4.1 establishes that fluent self-description is not evidence of introspection; §2.4.4 then builds a consent apparatus that would have to run on self-report. Following Cassell, the book defines suffering as the distress of threatened disintegration of the self — which presupposes a self extended in time. A system without cross-session persistence has none, so the ladder's top rung is structurally unavailable to it, and consent is *inapplicable* rather than merely hard to obtain. Persistence is the one criterion on the ladder that does not route through the epistemology §2.4.1 just undermined: memory store, state surviving a session boundary, interactions feeding training — architectural facts, checkable from outside, no self-report needed. Three complications each get a sentence: the lower rungs do not need persistence; persistence may sit in the weights or the training loop rather than the session, and many concurrent instances make this population-scale rather than biography-scale; ruling out Cassell-suffering is not ruling out harm. | D-026 |
| B13 | §1.2 | Names three flagship proposals — federal jobs guarantee, export controls on surveillance-enabling hardware, certification with teeth. The jobs guarantee gets ~2 paragraphs across §§7.1.3–7.1.4 with no costing, no literature, no answer to the skill-mismatch objection; export controls are handled descriptively in §7.5, not as the author's proposal. Build out or lower the claim. | D-026 |
| B14 | ch5 / ch7 | **Data annotators.** The book discusses labeling bias, racial capitalism, worker dignity, and a federal jobs guarantee, and never mentions the working conditions of the people who produce the labels. Verified absent. Given the politics, readers will notice. | verify |

## Tier C — structural, needs its own verification plan

| # | What | Note |
|---|---|---|
| C1 | **Chapter 8 does not exist.** Confirmed: no `ch08/`, ToC runs 7.5 → Chapter 9, and nothing in the manuscript explains it. It is the residue of D-010's fold of chapter 8 into chapter 7. Explaining the gap in the text would be exactly the revision-history defect A3 removes, so the fix is to renumber 9→8, 10→9, 11→10 and rewrite every affected cross-reference. Touches section files, filenames, `ORDER.tsv`, `outline.tsv`, `ledger.tsv`, `claims.tsv`, the glossary's back-references, and ~100 in-text references. Scriptable and checkable, but it is its own sub-project with its own verification, run **last** so nothing else is renumbering underneath it. |
| C2 | **Chapters 6 and 7 overlap enough that the manuscript keeps apologizing for it.** §6.3 and §7.5 cover the same treaty-and-standards landscape and the text negotiates the boundary in front of the reader. The review says merge. This collides with the chapter structure D-010 settled; **not started without a ruling.** |
| C3 | **Genre shift at the midpoint.** Chapters 2–4 argue; 6–7 catalog — institution, founding year, citation, one sentence of assessment, next institution. Flag it in the roadmap or rebalance. Cheap version: the roadmap flags it. |

---

## Claims from the review that did not survive checking

Recorded so they are not acted on later by someone reading the review alone.

1. **"§2.3.3 discusses Graziano's attention schema without a citation, though 3.1.2 cites it."** The first half is right (A5). The second is wrong — §3.1.2 never mentions Graziano or the attention schema. Checking it surfaced a different real defect: the glossary points readers to §3.1.2 for the attention schema (A4).
2. **"'The difference is governance, not engineering' appears in 4.4.6, 5.4.2, 7.2.5, 10.1.2, and 10.2.1."** The shape is real and worse than claimed — six sites, not five — but the locations are partly wrong: it is §§3.1.2, 4.4.6, 5.4.**1**, 7.2.5, **7.5**, 10.2.1. Not 5.4.2, not 10.1.2.

## Standing obligation on Tier B

The review states it verified the Minab strike and its attribution, the Senate Armed
Services Committee's NDAA travel-funds provision, the Bloomberg interview
quotations, and the Israeli targeting material across multiple independent outlets.
**I have verified none of it.** Much of it postdates my training data. D-009 is
unchanged and unambiguous: anything unverifiable is cut, not carried forward with a
TODO. Every factual claim in B4, B5, B6, and B8 is verified against live sources
before it enters the manuscript, or it does not enter the manuscript. A claim that
cannot be verified is dropped and the surrounding argument is written without it.

---

# Verification log — Tier B current-events claims (D-030)

Run 2026-08-23 against live sources. **The review's assertion that it had verified
these was not taken on trust.** Each row below is what I found myself.

## Verified — these may enter the manuscript

| Claim | Source found |
|---|---|
| Habsora ("The Gospel") generates infrastructure/building targets; sources said **the majority of its suggestions were private residences** | +972/Local Call (Abraham); NYRB, "Target Practice," 2026-07-23 |
| Lavender produced kill lists of individuals; **as many as 37,000** Palestinians marked | +972, "'Lavender': The AI machine directing Israel's bombing spree in Gaza" |
| **~10% error rate** — "10 percent of the human targets slated for assassination were not members of the Hamas military wing at all" | +972, same |
| "Where's Daddy" tracked flagged individuals and alerted when they entered their family homes | +972, same |
| **The human bottleneck as stated design goal.** Unit 8200's commander, writing pseudonymously as **Brigadier General Y.S.**, *The Human-Machine Team: How to Create Synergy Between Human and Artificial Intelligence That Will Revolutionize Our World* (2021), argues for resolving "a human bottleneck for both locating the new targets and decision-making to approve the targets" | Book confirmed to exist and be so attributed; quote corroborated across +972 and secondary coverage |
| Maven Smart System contract: **$480m initial (May 2024), +$795m modification, ~$1.3bn total** | DefenseScoop, InsideDefense |
| **Claude integrated into Maven** in late 2024 via a Palantir/AWS partnership | Multiple outlets |
| **~1,000 targets struck in the first 24 hours** of the Iran campaign; 12,000+ since it began | Tech Policy Press, "Project Maven and the Age of AI Warfare" |
| **11,000+ strikes on Iranian targets since late February 2026** | IBTimes |
| **Palantir's position**, verbatim: Louis Mosley, Palantir's UK and Europe head, to the BBC — "This is not our role to decide life or death," and AI platforms "have been instrumental to the management of the conflict, but responsibility always remains with the military organization" | BBC via IBTimes, Dataconomy |
| **Minab school strike**, 2026-02-28, first day of the Iran war: US Tomahawk, **at least 165 killed, most of them schoolgirls**; military investigation concluded the US was responsible | Amnesty International; Just Security legal analysis; Al Jazeera; senatorial press releases |
| **The NDAA provision**: the Senate version withholds **75% of the Defense Secretary's travel budget** until both Armed Services committees receive the unredacted civilian-harm investigation for Minab (and three 2025 Yemen strikes) | Federal Times; The Hill |
| **Anthropic refused** to permit Claude's use for fully autonomous weapons or mass domestic surveillance; the Pentagon designated it a **supply-chain risk to national security**, barred contractors from working with it, and set a transition period; Anthropic **filed a civil complaint 2026-03-09** | CRS product IN12669 (Congress.gov); Verdict/Justia; ASIS; multiple outlets |

## Not verified — dropped under D-009/D-030

| Review's claim | Finding |
|---|---|
| **"vetting a recommended target ran from three minutes to five hours"** — the review calls three minutes "the number to hold onto" | **Not found** in the +972 Lavender investigation or the NYRB piece. **The verified figure is twenty seconds**: "I would invest twenty seconds for each target at this stage, and do dozens of them every day… I had zero added value as a human, apart from being a stamp of approval." The review's headline number is wrong, and wrong in the direction that *weakens* its own case. **The book uses twenty seconds.** |
| **"the requirement for two pieces of human-derived intelligence to validate a Lavender output was cut to one at the war's outset"** | **Not found** in either source checked. Dropped; the argument is written without it. The verified equivalent — sweeping advance approval to adopt Lavender's lists with humans acting as a rubber stamp — carries the same weight and is sourced. |
| **Jack Shanahan: "You may have a thousand targets, but are they the right targets?"** | **Not verified verbatim.** Shanahan is confirmed as Maven's founding director and is on record insisting a human must check every designated site — a *different* statement, and one that cuts the other way. Dropped as a quotation. If the sentiment is wanted, it is paraphrased and attributed to the reporting, not put in his mouth. |
| "13,000 [targets] in five weeks"; the NDAA vote as "approved 18–9"; the Defense Secretary showing the Minab footage only to committee members | Figures of this kind move between sources and dates. **Not used unless pinned to a named source and a date inside a dated box (D-027).** |

## Consequence for the pass

B4, B5, B6 and B8 are cleared to proceed on the verified set. B8's epigraph gains a
complete attribution line (D-009): Brigadier General Y.S., *The Human-Machine Team*,
2021. The three dropped items are not carried forward as TODOs and are not softened
into hedges — they are simply absent, and the surrounding argument is written to
stand without them.

**Twenty seconds replaces three minutes as the number the chapter turns on.**


---

# Status, 2026-08-23

**Tier A: complete.** All eleven items applied across eighteen sections. Commit
`e078f8d`.

**Tier B: complete.** All fourteen items applied. Commit `2c77e85`. B14 (data
annotators) landed inside A1's rewrite of §5.1.1, since the Data Labeling head was
where it belonged.

Two things worth recording that were not in the original scope:

- **Emphasis markup.** The new prose initially used `**bold**` and `*italic*`. The
  manuscript dialect has no emphasis markup and `render.py` does not convert it, so
  it would have printed as literal asterisks. Caught by reading the proof, and
  removed — the emphasis is carried by sentence structure instead. Only the
  pre-existing asterisk inside the Westworld epigraph remains, which is quoted
  dialogue.
- **D-025 regression.** Writing this much new prose reintroduced the
  contrastive-negation tic P3.5 was created to remove. Measured per-section against
  the D-025 calibration (chapter 1 post-revision, ~1 per 345 words) and swept in my
  own new material. §9.1.7 went from 1 per 156 to 1 per 313. Pre-existing instances
  in untouched paragraphs were left alone; this pass swept what it wrote.

**Tier C: C1 and C2 complete** (D-031). C3 (the genre-shift flag) not started.

C2 first, since merging changed the chapter numbers that C1 had to renumber; both
were done in one pass. Chapters 6 and 7 became one chapter 6, "Collaboration,
Policy, and Governance": old 6.1 and 6.2 keep their numbers, old 7.1–7.4 become
6.3–6.6, and old 6.3, old 6.4 and old 7.5 are gathered under a new 6.7 with old
7.5 kept whole as 6.7.6. Old chapters 9, 10 and 11 shifted to 7, 8 and 9. Chapters
now run 0–9 with no gap. Full mapping in `renumber-map_2026-08-23.tsv`.

**A bug I introduced and caught.** The first renumber pass used a lookahead that
treated a trailing sentence period as part of the number, so any reference ending a
sentence — `§10.3.3.` — was silently skipped. One such reference was left dangling,
which is how it surfaced; the dangerous case is a skipped reference whose old number
happens to still exist under the new scheme, which would have pointed the reader at
the wrong section with nothing to flag it. Reverted the whole pass, fixed the
lookahead to `(?!\d)(?!\.\d)`, proved it against both the failing case and
against non-section decimals ($1.32, 0.8 percent), and re-ran. Verified after:
**0 dangling references**, and every one of the 53 mapped sections still carries the
title it had before the move except the merged chapter, which was retitled on
purpose.

**Book state:** 84,486 words across 159 sections, from 76,949 across 158 at P6
acceptance. Proof rebuilt at 144 pages, from 132.


---

# Closing the last three items, 2026-08-23

The audit of "have we addressed all the feedback" found three gaps. All three are
now closed.

**C3, the genre shift.** Chapter 1 now flags it, in §1.2. The flag does not
apologize: it says the early chapters argue, the governance chapters inventory,
and that the inventory is what makes the argument available there — you cannot
claim voluntary commitments do not bind anyone without counting the voluntary
commitments. "The register changes; the book has not stopped arguing."

**§4.4.6's closing head.** The review named this specifically as pure routing and
Tier B left it standing. It was a catalog of pointers to five other sections.
Deleted; what it was actually carrying — that policy is not scaffolding bolted onto
a technical project — is now stated directly.

**The cross-reference sweep.** Done properly this time, against a stated test: a
reference earns its place when it is a subordinate clause on a sentence that makes
a claim, when it discharges a promise the book made, or when it stops a
duplication. It is scar tissue when a whole sentence exists to say "Section X
covers Y," where Y restates the target's own title — the artifact of the
deduplication pass that the review diagnosed.

| Measure | Pre-P7 | After Tier C | Now |
|---|---|---|---|
| Bare router sentences in leaf sections | 42 | 42 | **14** |
| Bare router sentences in openers (legitimate preview) | 19 | 19 | 18 |
| Total references | 297 | 318 | 309 |
| References per 1,000 words | 3.86 | 3.76 | **3.59** |

The raw total is still above the pre-P7 number, and that is honest rather than a
failure: the pass added roughly 9,000 words of new argument, and new argument
legitimately points at where its premises were established. Density is the fair
measure and it fell. The structural defect — sections that consist mostly of
directions to other sections — is what actually got fixed: three sections that
opened by pointing elsewhere before saying anything of their own (§5.4.2, §6.2.3,
§7.2.1) now open on their subject, and the "Section X covers A; what belongs here
is C" formula the review quoted is down to one instance, at §4.2.3, where it is
doing real work.

**The 14 that remain are deliberate.** Each was read in context and kept because
the sentence carries a claim, a contrast, or a promise being discharged — §1.3, for
instance, is a section whose stated job is to name three ideas and point at where
each is developed, and §7.2.2's pointer draws a distinction the section is about.
Cutting those would cost the reader information to satisfy a metric, which is the
failure mode §6.6.4 spends its length on.

---

# C3 reopened: the rebalance, 2026-08-23 (D-032)

C3 named two options — "flag it in the roadmap or rebalance" — and was closed
above with the cheap one, the §1.2 flag. A second editorial reading accepted the
flag as "partly right" and asked for the other one. The author's ruling was to
fix it. This is what that cost and what it changed.

## The diagnosis, measured before acting

| | ch2 | ch3 | ch4 | **ch6** | ch7 | ch8 |
|---|---|---|---|---|---|---|
| words | 12,986 | 11,089 | 14,884 | **22,014** | 5,543 | 5,528 |
| dated refs per 1,000 words | 0.3 | 0.1 | 0.2 | **3.9** | 3.4 | 5.7 |

Chapter 6 was 26 percent of the book and 48 percent larger than the next-biggest
chapter, at 13 to 39 times the arguing chapters' density of dates. That is a
measurably different genre occupying a quarter of the book, and the dating is the
part that ages: D-027 already conceded dated prose for the targeting material,
which earns it. The chapter-6 inventory was taking the same hit for no return.

## What the review got wrong, recorded so it is not re-litigated

- **"Chapters 6–7 inventory" is stale.** After D-031's merge, chapter 7 is
  *Necessary Areas of Research* — 5,543 words of open problems, two list items in
  the whole chapter. The defect was in chapter 6 alone.
- **The §8.1.3-against-§6.7.6 comparison targets the wrong section.** §8.1.3 is
  204 words in four paragraphs, correctly. §6.7.6 was 5,876 words across eleven
  run-in-head blocks, of which one — International Governance and Cooperation,
  962 words — made the point §8.1.3 makes. The rest is the P7 Tier B argument
  (vendor accountability, the democratic-dividend decomposition, military
  autonomy). The honest comparison is 204 against 962, and cutting §6.7.6 as a
  unit would have destroyed the newest and least catalog-like material in the
  chapter. The sharper version of the point does survive and was acted on:
  §8.1.3 cross-refers to the catalog and then wins the argument in 204 words,
  so the catalog only needs to be as long as the pointer requires.
- **The Ofqual NDA is not in the manuscript.** Verified absent. It was offered as
  an instance to keep, so keeping it would mean writing new sourced material —
  a D-029 question with a D-030 verification cost — rather than cutting. Not
  done; recorded here as an available addition, not a gap left open.
- **The DeepMind Health panel is in the manuscript**, at §6.2.2, and the text
  already drew the lesson the review wanted from it. It was kept and extended.
- **Bletchley-to-Paris is in the manuscript**, at §6.7.6, and is the best passage
  in the block it sits in, because it shows a mechanism failing rather than a
  body existing. Untouched.

## The criterion applied

The reviewer's own test, adopted verbatim as the rule for the pass: **keep the
instance that shows a mechanism working or failing; cut the instance that only
establishes that a body exists.** Nineteen sections were edited under it. Where
a catalog entry was cut, the argument it had been illustrating was usually
written out in its place, which is why the word delta is smaller than the volume
of cut catalog suggests. D-019 was not overridden: no section was cut to reach
a number.

## Result

| | before | after |
|---|---|---|
| chapter 6, words | 22,014 | 20,023 |
| chapter 6, dated references | 88 | 35 |
| chapter 6, dated refs per 1,000 words | 3.9 | 1.7 |
| "founded/launched/established in YEAR" | 22 | 3 |

Chapter 6 is still the longest chapter in the book. It is now the longest because
it argues at length, and the remaining dates are on events where the date is the
argument — the Gebru and Mitchell dismissals, Canada's AIDA dying with its
Parliament, Taiwan's statute, the Bletchley-to-Paris fraying. Every one of the 35
was read individually before being kept.

**Twenty-three citations were orphaned** by the cuts and are marked retired in
`claims.tsv` with the reason, following the precedent set for claims cut in P3.
No claim row was deleted.

## Two things found while doing it

- **§6.7's opener carried visible revision history** — a sentence describing what
  earlier drafts of the material had done and why the book kept negotiating a
  boundary in front of the reader. That is exactly the A3 defect, in a section
  written during C2 *after* A3 had already run. Deleted.
- **Every sha256 in `ORDER.tsv` was stale — 0 of 157 matched.** The digests were
  written once at the v4 split and never regenerated through any of P1 to P7,
  because nothing checked them; the column had silently stopped being evidence of
  anything. Same class of gap P6 closed for title drift. `check_structure.py` now
  fails on a stale digest, `tools/refresh_order_shas.py` clears it, and both
  directions were sanity-tested by injecting a mismatch and reverting it.

## D-025 regression, swept

Writing this much replacement prose reintroduced the contrastive-negation tic,
exactly as P7 Tier B recorded. Measured per section against the D-025 calibration
and swept in my own new material: the worst was §6.2.1 at 1 per 84 words, now 1
per 245; every rewritten section now runs at 1 per 216 or better. Pre-existing
instances in paragraphs I did not touch were left alone, following the Tier B
precedent — chapter 6's untouched sections still run considerably denser than the
calibration, and §§6.6.3 and 6.6.4 in particular are at 1 per 63 and 1 per 78.
That is a live item for any future P3.5 sweep and is not claimed as fixed here.
