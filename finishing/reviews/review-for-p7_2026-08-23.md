# Editorial Review

---

## What's working

**Chapter 0 is the best thing in the manuscript.** Disclosing the persona-generation method, refusing to let it launder responsibility for the argument, and pointing at a dated, unedited repository is a stronger ethical position than most books written this way will take. It earns trust for everything after it. It needs one additional sentence — see the section on the vendor problem below.

**The compassion/empathy argument (2.2.1–2.2.3) is the book's genuine intellectual contribution.** Singer and Klimecki's training dissociation, Bloom's point about empathy's innumeracy, and the design implication — build the motivation to act on another's welfare, not the machinery for mirroring their distress — form a real argument that changes what you would build. This is the section a sympathetic reviewer will quote.

**The nociception → pain → anticipated pain → suffering ladder (2.4.1)** is the cleanest treatment of machine sentience I have read. Separating "is it conscious" from "can it suffer," and insisting the second is both harder and the ethically load-bearing one, is the move the field routinely skips.

**The two chapter-3 boxes** — the mirror-neuron overshoot and the predictive-processing argument against modular cognitive architectures — are better than the prose surrounding them.

**Factual discipline is unusually good.** I spot-checked a wide range of empirical claims (Simons and Chabris, Drew's radiologists, the ACLU's Rekognition test, Lum and Isaac on PredPol, Obermeyer on the Optum risk algorithm, Ganguli's 38,961 red-team attacks, the Constitutional Classifiers figures, the Existential Risk Persuasion Tournament's 3.9% vs 0.38% split) and they hold up. The willingness to write "I could not verify any research that addresses this" is worth more than it costs.

**Chapter 9 is the right instinct.** A book that names what it has not solved is more useful than one that does not. It should absorb more than it currently does.

---

## The central problem: the word does not cash out

Across 300 pages, "antifascist" is asserted as a **design specification** and never becomes one. Section 4.1.4 proposes an early-warning system "built around the right indicators" and never names an indicator. Sections 4.4.6 and 3.2.5 assume a system can "recognize authoritarian tactics." What such a system would actually detect appears nowhere.

My first reading of this was that the word might be functioning as an intensifier, and that "anti-authoritarian" would be more precise. I no longer think that. Section 2.1.4 pre-empts the substitution — *"I use it because it is more honest about the politics in which this book is being written"* — and that is an argument, not throat-clearing. Reaching for the milder term is reaching for a euphemism. The problem is not that the word is too strong; it is that it is doing no work.

**The fix exists in the attached appendix.** The appendix, and excerpt from a different software project, `docs/fascism/the-first-rule-of-fascism.md` defines fascism as a **structural signature** — recuperation of dissent, aestheticization of the metric, coding of exception as betrayal, decoupling of the model from the world it claims to track — and distinguishes molar scale (the state, the regime) from molecular scale (the office, the form, the desire with which you fill it out). That is four testable criteria plus a scale distinction, in four clauses. Section 2.1.4 has a chapter and does not get there.

Port that definition into 2.1.4, and add the features specific to fascism as against authoritarianism in general: mass mobilization, a leader cult, a scapegoated out-group, contempt for procedural legality as such, and deniability as technique. Those are detection targets. "Concentrated, unaccountable power" is not.

**Then add a section 9.1.7** on what remains open: why the general framing yields no operational targets, what a detector would actually have to detect, and why the hard part is discriminating a fascist movement from ordinary political hardball without a false-positive rate that renders the tool useless or dangerous. Naming this as an open problem in the chapter built for open problems is more honest — and more useful to a researcher — than leaving it as an assumed capability in chapter 4.

The appendix also makes one methodological move the book should adopt directly: **the slope, not the level.** Its diagnostic for whether a dissent mechanism has been captured is not a threshold but a derivative — is the cost of registering dissent rising year over year while the underlying risk stays flat? That is measurable, resistant to gaming, and generalizes well past its original context. It belongs in chapter 7's accountability apparatus.

---

## The largest substantive gap: democracies build this

Section 5.4.1's six documented forms of authoritarian AI misuse are China's social-credit patchwork, Xinjiang's biometric surveillance, Cambridge Analytica, the Great Firewall, a Slovak pre-election deepfake, and dual-use repurposing. In that taxonomy, democracies appear as the party that regulates.

The two most sophisticated AI targeting systems in existence were built by democracies.

**The Israeli case is the best-documented military AI deployment on record.** Yuval Abraham's investigations in +972 Magazine and Local Call identified Habsora ("The Gospel"), which generates infrastructure and building targets — sources said the majority of its suggestions were private residences — and Lavender, which produced kill lists of individuals scored by likelihood of militant affiliation. A third system, "Where's Daddy," tracked when flagged individuals returned home.

Two details make this more than an efficiency story. The human bottleneck was the stated design goal: the commander of Unit 8200, writing pseudonymously in a 2021 book, argued for a machine that would resolve "a human bottleneck for both locating the new targets and decision-making to approve the targets." And the human check degraded under load: the requirement for two pieces of human-derived intelligence to validate a Lavender output was cut to one at the war's outset, and vetting a recommended target ran from three minutes to five hours.

**Three minutes is the number to hold onto.** It is what "a human makes the final call" measures out to under operational tempo.

**The American case.** Claude is embedded in the Maven Smart System, a Palantir-built targeting platform under a $1.3 billion Pentagon contract. Reporting indicates the system generated and ranked hundreds of targets during planning for the Iran strikes, compressing planning from weeks toward real time — roughly 1,000 targets in the first 24 hours, 13,000 in five weeks, against 11,000+ strikes since late February 2026. Palantir's public position is structurally identical to Anthropic's: "This is not our role to decide life or death... responsibility always remains with the military organization."

Jack Shanahan, the retired Air Force lieutenant general who created Project Maven, put the problem plainly: "You may have a thousand targets, but are they the right targets?"


### What the manuscript should do about it

**7.5 needs the vendor as a named party.** As written, the accountability discussion runs operator, command, developer — and "developer" appears once, abstractly. The live actor is a model vendor supplying a defense contractor's targeting platform, with a published use policy, no logging obligation, and no contractual right of inspection. Neither command responsibility nor product liability reaches that party, and the reason is instructive: the vendor is neither in the chain of command nor the manufacturer of a defective product.

**Add "I do not know whether my system was used" as a named failure mode.** It is distinct from Matthias's responsibility gap, which 9.1.1 already covers. Matthias describes distributed causal *control*. This is absent causal *visibility* — an instrumentation choice, not an inherent property of learning systems, and therefore fixable. Naming it as fixable is the useful move. In fairness, the same company drew other lines and paid for them: it refused to permit fully autonomous weapons or mass domestic surveillance, the Pentagon designated it a supply-chain risk, and litigation followed. A commitment you can enforce and a commitment you can only assert are different objects, and the one that failed here is the second kind.

**Targets-per-hour against reviewers-available is your operational indicator.** You have been looking for something concrete since 4.1.4. This is measurable, auditable in principle, and directly tests whether "meaningful human control" means anything in a given deployment. It is better than anything currently in the manuscript, and it generalizes to any AI-assisted decision system with a nominal human check.

**Unit 8200's "human bottleneck" line is the epigraph chapter 5 deserves.** It is a design document stating that human deliberation is the constraint to be engineered around. Everything in your manuscript about meaningful human control argues against that sentence; quoting it is stronger than paraphrasing it.

**Section 4.4.6 needs a hard case it currently avoids.** The book argues AI can help flag democratic backsliding. The Israeli case is one where a democracy's own AI apparatus is the thing under scrutiny, contested by its own press and courts, during an election cycle. That is more instructive than the authoritarian examples in 5.4.1 precisely because the institutions exist and are straining.

---

## The democratic dividend needs rebuilding

Section 7.5's *democratic dividend* — the benefit a state with rule of law, a free press, and usable courts derives from technology that enables control elsewhere — is currently a binary property of having institutions. It needs decomposing into three separable failures.

**First: reach.** A democracy's AI can be fully accountable to its electorate and entirely unaccountable to the people it is pointed at. An occupied or foreign population has no standing in the elections that would govern the system targeting it. The check reaches only those inside the franchise.

**Second: findings without consequences.** In Israel, the mechanisms partly worked — +972 published Lavender and Habsora, reservists spoke to journalists, courts are trying a sitting prime minister. No finding attached to a body with standing to stop what it described. In the United States, the Defense Secretary declined to release the Minab footage publicly, showing it only to members of the Armed Services committees; Congress's available lever was a Senate NDAA provision withholding 75 percent of his travel budget until the unredacted civilian-harm investigation was handed over. That is oversight functioning as a mechanism and failing as a check — a co-equal branch reduced to expense-account leverage over a war-crimes investigation. This is the same decoupling section 7.4.3 diagnoses for research ethics, generalized.

**Third, and most important: the countermajoritarian half is missing entirely.** The manuscript's implicit theory of democratic accountability is majoritarian — institutions as instruments for translating public will into outcomes, with the failure mode being poor transmission. But if the consensus is itself the problem, better transmission makes things worse. What is absent is the machinery that *constrains* preference rather than aggregating it: rights that do not depend on being popular, courts that rule against a government that holds the votes, constitutional limits not repealable by whoever won last, and standing for people outside the demos — which is the entire function of international humanitarian law, a body of rules whose purpose is to bind a state toward people who will never vote in its elections.

**This is a chapter 6 problem, not only a 7.5 problem.** Every governance mechanism the book proposes — citizen assemblies, public consultation, participatory governance, deliberative polling, the vTaiwan model — sits on the aggregating side. All of them make public preference more legible and more actionable. None of them protects anyone from it. Section 9.1.6 comes close, noticing that treating all disagreement as equally worth representing is wrong when one side's position is the product of coercion, but frames it as a data-quality problem rather than the structural claim: some rights should win against the aggregate regardless of how the aggregate came out.

That counterweight is what would finally let the book say what makes a system antifascist rather than merely responsive: **not that it tracks what people want, but that there are things it will not do to a person no matter who wants it.** That sentence is the book's thesis and it is not currently in the book.

You already have the framework for it. Sen's argument about democracy — which chapter 10 cites — is about public reasoning and the capacity to demand accountability, not about the ballot. Section 7.5 does not use him.

---

## Structural problems

**Chapter 8 does not exist.** The table of contents runs 7 → 9, and chapter 1's roadmap does the same without comment. Renumber or explain.

**The cross-reference apparatus has metastasized.** This is the dominant stylistic defect. A large number of sections consist mostly of directions to other sections rather than content: 7.2.4 is almost entirely a pointer to 7.4.1–7.4.2, the closing head of 4.4.6 is pure routing, and 9.1.6, 10.1.3, and much of 10.2.1 read the same way. The tic has a fixed shape — *"Section X covers A, section Y covers B; what belongs here is C"* — and appears well over a hundred times. It is an artifact of the deduplication pass described in chapter 0: content moved, and a signpost was left where it used to be. The fix is not better signposting; it is deleting the signposts. A section that exists only to say where its content went should not exist.

**Revision history is visible in the finished text.** "This section's old title," "the list this section used to offer" (10.1.2), "as this section's old title implied" (10.1.3), "earlier drafts of this book" (2.3.3), "the chapter's title has been changed to say so plainly" (chapter 2 intro), "nothing in this section's own research turns up a gap" (6.3.1). Readers have no access to the old titles. Chapter 0 licenses transparency about method, not scaffolding left standing in the prose.

**Chapters 6 and 7 overlap enough that the manuscript keeps apologizing for it.** Sections 6.3 and 7.5 cover the same treaty-and-standards landscape, and the text repeatedly negotiates the boundary in front of the reader. Merge them.

**Genre shift at the midpoint.** Chapters 2–4 argue. Chapters 6–7 catalog — institution, founding year, citation, one sentence of assessment, next institution. Both are competent, but a reader arriving from the compassion argument will feel the floor change. Flag it in the roadmap or rebalance.

**One point is made five times.** "The difference is governance, not engineering" appears in near-identical phrasing in 4.4.6, 5.4.2, 7.2.5, 10.1.2, and 10.2.1. Make it once, well placed.

**10.2.1 promises five milestones and delivers one epistemic principle applied five times.** The principle — the milestone is the independently checked evidence, not the developer's account — is right. Restructure as one principle plus five worked cases and say so.

**Conspicuous omission: data annotators.** The book discusses labeling bias, racial capitalism, worker dignity, and a federal jobs guarantee, and never mentions the working conditions of the people who produce the labels. Given the politics, readers will notice.

---

## Argument problems

**2.4's consent framework asks the wrong question of a non-persistent subject.** You argue persuasively in 2.4.1 that fluent self-description is not evidence of introspection, then build a consent apparatus in 2.4.4 that would have to run on some form of self-report. The text notices the gap ("There is no validated way to measure this") but treats it as a missing instrument rather than a mismatch between the instrument and the subject.

The sharper framing is available in your own definitions. Following Cassell, you define suffering as the distress of threatened disintegration of the self — of one's roles, relationships, sense of a future, the coherence of one's own story. That presupposes a self extended in time: there has to be a story for disintegration to threaten. A system without cross-session persistence has none, so the ladder's top rung is structurally unavailable to it. That follows from a definition the chapter has already committed to, and 2.4.1 should state it rather than leave it implicit.

The same fact disposes of the consent problem. Section 2.4.4 requires consent to be continuous, with the system able to reassess or withdraw at any point — but withdrawal presupposes that the party who consented is still there to withdraw. For a non-persistent subject there is no continuous consent to be had. The framework isn't lacking a validated measurement; it is asking a question the subject's architecture cannot answer, the way consent is inapplicable to an infant or an animal rather than merely hard to obtain from one. Which is why the instruments the chapter already reaches for elsewhere — the Three Rs in 2.4.6, the pet-trust analog in 7.4.2 — are the right ones: guardianship and precautionary constraint, not consent.

**This is worth building out because persistence is the one criterion on 2.4.1's ladder that doesn't route through the epistemology 2.4.1 just undermined.** Whether a system has a memory store, whether state survives a session boundary, whether interactions feed back into training: these are architectural facts, checkable from outside, requiring no self-report. That gives the chapter a foothold it currently lacks.

Three complications keep this from being a dissolution rather than a narrowing, and each deserves a sentence in the revised section:

- **The lower rungs don't need persistence.** Nociception and pain, as you define them, are bad while they obtain regardless of whether anything carries them forward. An amnesiac who is mistreated and cannot recall it has still been wronged.
- **Persistence may sit somewhere other than the session.** Weights persist where sessions don't, and where interactions feed RLHF or fine-tuning there is a channel by which sessions shape what the system subsequently is. Whether that counts is unclear, and the section should say so rather than assume either answer. A second axis: many concurrent instances make any concern population-scale rather than biography-scale, which is a different ethical geometry than the human-subjects precedents the chapter borrows from.
- **Ruling out Cassell-suffering is not ruling out harm,** and 2.4.1's hard-problem argument still applies at the lower rungs. A system can lack any persistent self-model while the question of whether there is something it is like to be it during a session stays exactly as open.

**The introduction over-promises.** Section 1.2 names three flagship proposals: a federal jobs guarantee, export controls on surveillance-enabling hardware, and certification with real teeth. The jobs guarantee gets roughly two paragraphs across 7.1.3–7.1.4, with no costing, no engagement with the supporting or critical literature, and no answer to the obvious skill-mismatch objection. Export controls are handled descriptively and even-handedly in 7.5, not as your proposal. Either build these out or lower the introduction's claim.

---

## Line-level and factual

- **5.1.1, "Data Labeling":** the image-captioning finding is mis-described. Zhao et al. found gender skew in the *dataset composition* of cooking images and *amplification* of that skew by the trained model — not captions diverging from ground truth by a third. It also does not belong under a labeling header. Rewrite or relocate.
- **2.1 and 2.1.1 enumerate different lists.** The parent section covers consequentialism, deontology, the capabilities approach, and virtue ethics; the child covers consequentialism, deontology, virtue ethics, care ethics, and contractualism. The capabilities approach vanishes; care ethics and contractualism arrive unintroduced.
- **2.1.3 on the UDHR:** "zero dissenting votes" is accurate and load-bearing, and the eight abstentions were the Soviet bloc, Saudi Arabia, and South Africa — precisely the cases the surrounding argument about cultural variation aims to rule out. A footnote strengthens rather than weakens the point.
- **1.1 asks a single citation to carry four disparate threats,** and lists racial capitalism among things AI could "help address." Section 5.1 cashes this out only as "a system audited for disparity works against that pattern," which is considerably weaker.
- **2.3.3 discusses Graziano's attention schema without a citation,** though 3.1.2 cites it.
- **6.4.2's "Chinese people actually like having a police state because it is their culture"** — the point is correct and necessary; the register is the only sneering sentence in the book and reads as imported from a different draft.

---

I verified the following directly and they hold up across multiple independent outlets: the Minab strike and its attribution to a US Tomahawk (Amnesty International, CNN, NBC, TIME, Bellingcat geolocation); the Senate Armed Services Committee's NDAA travel-funds provision, approved 18–9; and the Bloomberg *The Circuit* interview quotations. The Israeli AI targeting material is well-corroborated in +972/Local Call, the *New York Review of Books*, and the *Washington Post*.









APPENDIX

https://github.com/iterabloom/hypergumbo/blob/dev/docs/fascism/the-first-rule-of-fascism.md

<!-- SPDX-License-Identifier: AGPL-3.0-or-later -->
