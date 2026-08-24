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

D-007 still governs everything not named here. This is not a licence to re-argue
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
| C3 | **Genre shift at the midpoint.** Chapters 2–4 argue; 6–7 catalogue — institution, founding year, citation, one sentence of assessment, next institution. Flag it in the roadmap or rebalance. Cheap version: the roadmap flags it. |

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
