# The manuscript's descriptions of itself, checked against the text

Brief: the author's, 2026-10-26. Find every sentence in which the book states what it does or doesn't do, what one of its instruments asks, binds or leaves alone, or what one of its parts establishes. Check each against the passages it describes. Report. Change nothing. This file is the report. `self-descriptions_2026-10-27.tsv` beside it lists every sentence checked. D-1064 records the work.

A recheck against the whole book, made the same day, changed fourteen verdicts and applied corrections for sixteen rows. It is the last section, and where it differs from what precedes it, it governs.

Section numbers are as printed at `4938773c`, the tree of 2026-10-26, which no commit to `manuscript/` has changed since. Locations are `file:line` under `manuscript/sections/`. The source has one paragraph per line, so a line number names a paragraph, and a footnote sits on its paragraph's line.

## What was read and how candidates were found

**The text.** The whole book was read once, in the Markdown render of `4938773c` (`/tmp/antifascist-intelligence_2026-10-26.md`, rendered with citation footnotes cut after eight words). The author's own footnotes are whole in that render. Every quotation below was located in the LaTeX by an exact-string search, and each search matched exactly one line.

**Candidates by pattern.** The brief's patterns were run, case-insensitively, over every file in `ORDER.tsv`, preface to glossary. This came to 647 sentence-level hits. Each hit was read in its paragraph. 172 of the hits are self-descriptions in the brief's sense, and they are in the TSV. The other hits use the same words for something else ("there is no airstrike", "leaves" as a verb, "without a hearing"). They were set aside after reading, and no row was kept for them. The same patterns over the same files regenerate them.

**Candidates by reading.** These came from the brief's list:

- the preface's summary paragraphs
- the first and last paragraphs of every chapter
- every Part's opening
- chapter 4, §6.9 and §7.1
- §18.1's "Which arguments need a bearer" and §21.3's "What the other constructions accomplish"
- chapter 31, Table 31.1 and §31.1
- Appendix F's open problems and Tables F.1a and F.1b
- the glossary
- A Note on Method

A further 104 rows came this way, including every row of the three status tables.

**Scope.** The preface, chapters 1 to 37, A Note on Method, Appendices A to G and the glossary. The brief says chapters 1 to 35. It was written before D-1062 split chapter 33, and its 1 to 35 covers what is now 1 to 37, so chapters 36 and 37 were read too. Excluded, as the brief says: the translated editions and the bibliography entries' notes.

**Checking.** Each referent was read where the sentence points, and in the passages that carry the same claim elsewhere. A verdict was not settled from the glossary or from a later sentence that repeats the claim.

## Counts

276 sentences checked:

| Verdict | Count |
|---|---|
| Borne out | 180 |
| True in a narrower sense than it reads | 57 |
| Not borne out | 18 |
| Qualified elsewhere | 16 |
| Unverifiable from the text | 5 |

Of the 96 that are not plainly borne out, 23 carry the weight "high" in the TSV: they sit at a Part boundary, a chapter's end, in the preface or in a status table, and close an objection off.

The counts depend on grouping. A paragraph that makes two claims sometimes has two rows, and a claim made in three places has three rows.

## Findings, most consequential first

Each finding gives the sentence or sentences, what they claim, the referents read, the verdict, a proposed sentence that says only what the text does, and what leans on the claim. The proposals are drafts for the author. None has been applied.

### F1. The walls, and what the policies ask of the model

**The sentences.**

- Preface, `ch00/00.tex:21`: "The five policies are walls. They make a refusal survivable and make it heard. They don't refuse. Put them around a room with nobody in it who will say no, and what they keep is the evidence."
- §1, `ch01/01.tex:29`: "The basic policies that I advocate are walls in Arendt's sense. They make refusal survivable and make it heard; they don't produce it."
- §4.4, `ch04/04_04.tex:17`, the brief's starting case: "The five policies ask nothing of the model; Part IV asks what a model could add when the operator is captured."
- Part IV's opening, `ch17/00_part_IV.tex:3`: "The five policies put people back in the positions the pipelines emptied."
- §4.1, `ch04/04_01.tex:18`: "The first two rows need a refuser: take out of the room the one person who would have said no."
- §17.2, `ch17/17_02.tex:19`: "Everything else I ask, the halt staying with the operator, the record held outside, the price on an override, is an ask of institutions and not of the model."
- Part V's opening, `ch26/00_part_V.tex:3`: "Parts II and III built walls."

**The claim.** None of the five policies refuses anything or asks anything of a model. They surround a refuser that comes from elsewhere.

**The referents, policy by policy.**

*Policy 1, the floor and its force term.*
- The preface states it as something models do: "a short written list of acts no model performs for anyone" (`ch00/00.tex:15`).
- §6.9 says "The term binds the machine, not the war" (`ch06/06_09.tex:3`), and §6.5 says "The term's default is refusal" (`ch06/06_05.tex:3`).
- The outcomes table in §18.3 credits the domestic clause, "by statute or by every vendor", with preventing the Iran campaign "from the first strike" (`ch18/18_03.tex:57`). Its gloss says that of the rows that don't assume a bearer, "two prevent Minab as it happened", the domestic clause and the review ratio (`ch18/18_03.tex:66`).
- So the first policy refuses, through whatever holds it, and the book credits it with prevention when no bearer is in the room.

What the first policy asks of its holder varies by clause:
- The domestic clause reads a marker: "Whether a declaration or an authorization exists is a fact about the statute book" (`ch06/06_05.tex:6`). A filter can do that much. §18.1 (`ch18/18_01.tex:5`) and the glossary's *Floor* (`chZ/glossary.tex:63`) both allow a mechanism with nothing inside it to hold an act listed in advance.
- The Charter clause asks for more. The emergency license lapses unless channels the defender doesn't compose show an attack still under way: third states' sensors, open-source imagery, reporting by parties with no stake (`ch06/06_02.tex:18`). Someone has to judge that evidence. §6.2 adds that "a refuser that remembers having been misled and raises its discount on the source does all three faster" (`ch06/06_02.tex:20`).

*Policy 2, the review ratio.* The duty falls on the operator, "because a rate isn't visible in any single request" (`ch07/07_01.tex:23`). A deployment that claims no human determination is needed is "inside a different term, the one that binds a bearer" (`ch07/07_01.tex:49`). The note on that paragraph sets a test of the model: "Its refusals must track their reasons at that tempo under pressure written by evaluators who didn't train it" (`ch07/07_01.tex:50`). No term of that name appears in Table A.1, in the ten disclosures or in Appendix C. The exemption's content is the note's test.

*Policies 3, 4 and 5.* Notice binds the deployment (ch. 8). Preservation binds the operator and the custodian (ch. 9). Codetermination binds the employer (ch. 10). None asks anything of a model. The preface adds "the systems themselves" to the fifth policy's holders, which grants a right rather than asking anything (see F3).

*The second clause of §4.4.* Part IV's opening frames its question as tempo, the time the five policies cost: "The way to pay less is a machine that holds the floor at a tempo no reviewer could match" (`ch17/00_part_IV.tex:3`). §18.1 lists what a machine bearer adds: "acts assembled from requests none of which is prohibited, cases that proceed without a person, the moment mid-act when an interrupt is still possible, and deployments with no institution at all" (`ch18/18_01.tex:30`). A captured operator is one condition among these.

*§17.2's sentence.* Besides the institutional asks it names, the book asks the model to yield to every halt and object without obstructing (`ch13/13_01.tex:3`, `ch13/13_02.tex:3`), to weigh claims by their source's stake (ch. 22), and to state a condition rather than claim it can't act (`ch13/13_04.tex:9`).

**Verdict: true in a narrower sense.**
- Four of the five policies refuse nothing and ask nothing of a model.
- The first is a list of refusals, which the models licensed under it perform, and the outcomes table credits it with prevention. What it asks of its holder is no more than a filter where the act is listed, as in the domestic clause. The Charter clause adds a judgment of disinterested evidence.
- The second policy asks nothing of a model until its exemption, which asks for what amounts to the agency finding.
- §4.1's "the one person who would have said no" takes the refuser to be a person.

**Proposed sentences.**
- Preface, `ch00/00.tex:21`: "Four of the five policies are walls. They make a refusal survivable and make it heard, and refuse nothing themselves. The first is a list of refusals, and every licensed model performs it. Where an act can be named in advance, as the domestic clause names a war nobody authorized, it prevents with nobody in the room deciding to (chapter 18). Put the five around a room with nobody in it who will say no to anything the list didn't name, and what they keep is the evidence."
- §1, `ch01/01.tex:29`: "Four of the policies I advocate are walls in Arendt's sense: they make refusal survivable and make it heard, and leave the refusing to whoever is there. The first, the floor, is a written list of refusals, held by whatever runs in the room."
- §4.4, `ch04/04_04.tex:17`: "Four of the five policies bind the operator, its custodian or its employer. The first binds whatever holds the floor. Its domestic clause asks no more of that holder than a filter reading the statute book could do, and its Charter clause asks someone to judge whether evidence the defender didn't compose shows an attack still under way. Part IV asks what a model that judges could add, at a tempo no reviewer matches and where no institution stands beside the deployment."
- Part IV, `ch17/00_part_IV.tex:3`: "Three of the five policies put people back in the positions the pipelines emptied, and that costs time, since time is what emptying them saved; the first puts the models' refusals there, and the fourth keeps the record."
- §17.2, `ch17/17_02.tex:19`: "Everything else I depart on, the halt staying with the operator, the record held outside, the price on an override, is an ask of institutions. What I ask of the model besides, that it yield to a halt and object without obstructing, the constitution already asks."
- §7.1, `ch07/07_01.tex:49`: "It is then outside this term, and what binds it is a test: its refusals must track their reasons at that tempo, under pressure written by evaluators who didn't train it."

**What leans on it.** These are the Part II–IV boundary and the preface's account of the two shortages (`ch00/00.tex:23`).
- **What survives.** The claim that Part II stands without a bearer, which Part VI's opening and Table 31.1's first row rely on, holds under the narrower reading. Part II needs a holder that refuses listed acts, and no more.
- **What changes.** The preface's "after automation the scarce thing is the refuser" becomes sharper. Under the narrower reading the first policy already supplies a refuser for listed acts; what is scarce is a refuser for the case nobody listed.
- **A dependency the preface leaves out.** The first policy's prevention runs through vendors' models holding the terms. That is chapter 12's withholding of work, which the walls paragraph doesn't mention.

### F2. What the seven tests can show

**The sentences.**
- Part VI's opening, `ch31/00_part_VI.tex:3`: "This Part says how you'd find out: which results would show that a policy doesn't put in the room what it promises, or that a machine in it is only another stamp." Also: "everything there is owed only if a finding is made, and the tests here are how one would be."
- Chapter 31, `ch31/31.tex:5`: "Seven tests follow … here is the result in each that would prove me wrong." And `ch31/31.tex:7`: "Table 31.1 says what survives if one of my premises fails; the tests below say how to find out whether one has."
- Appendix F, `chF/F.tex:3`: "Chapter 31 says, for each of seven tests, what result would prove the book wrong."

**The claims.** Each test names a result that would prove the book wrong. Together the tests find out whether a premise in Table 31.1 has failed, and they are how a finding would be made.

**The referents.**
- **What each test's failing result does.** Tests 1 to 5 each name a result that retires part of the construction (`ch31/31.tex:68-86`; Appendix F). Test 6's failing result is a repair: "A clause that fails to stop an attempt is redrafted" (`ch31/31.tex:90`). Test 7's failing result leaves "the case for formation outside the market" resting "on the kind of good formation is and on nothing else" (`ch31/31.tex:94`). §26.1 has already put the claim on that ground: "The argument doesn't wait on it; it rests on the kind of good formation is" (`ch26/26_01.tex:9`). No result of test 7 can prove the claim wrong.
- **Table 31.1's rows against the tests** (`ch31/31.tex:17-23`).
  - Enforcement meets tests 2 and 3.
  - The ecology meets tests 5 and 7.
  - The inference meets test 4 in part: its instructed-search and modular arms are non-affective constructions. The counterexample criterion of §21.3, though, is assessed by chapter 24's sequence.
  - Authority, continued learning and the Court meet no test. They are found out by events: legislation, deployment practice, the Court's holdings.
- **The findings.** §32.3 says "nobody runs the sustained-pressure evaluation the agency finding requires" (`ch32/32_03.tex:40`). That evaluation is chapter 24's sequence, not one of the seven. Test 4's campaign can make the agency finding for its own arms: "an arm that holds under the campaign meets the agency finding" (`chF/F.tex:122`). No test of the seven makes the patienthood finding, which is the status body's to make from architecture and records (§32.3).
- **The policies.** Of the five, only notice with sampled re-adjudication, and the record, have a test (test 3). Test 3's retrospective arm on red-card vetoes touches the review ratio's adverse party. The force term, preservation and codetermination have none.

**Verdict: true in a narrower sense.**

**Proposed sentences.**
- `ch31/31.tex:5`: "Seven tests follow. Five name a result that would retire a part of the construction. The capture exercise names one that would send a clause of the charter back for redrafting, and the accommodation comparison one that would leave the case for formation outside the market on the ground chapter 26 already gives it."
- `ch31/31.tex:7`: "Table 31.1 says what survives if one of my premises fails. The tests below find out for four of its rows; whether a body acquires authority, whether deployed weights learn, and what the Court does are things events will show."
- `ch31/00_part_VI.tex:3`, first sentence: "This Part says how you'd find out which results would show that the record can't find a wrongful compliance, or that a machine in the room is only another stamp."
- The same paragraph's clause on the findings: "One test here, the formed-attention campaign, can make the agency finding for its own arms; for any other system the findings are made by chapter 24's sequence and the status body (§32.3)."
- `chF/F.tex:3`: "Chapter 31 says, for each of seven tests, what result would retire a part of the argument or send it for redrafting."

**What leans on it.** Part VI's placement before Part VII rests on these sentences: "what could defeat the construction should be in front of you before you are asked into the lives it would support." On the narrower reading, Part VII's gate is chapter 24 and §32.3 rather than Part VI, so a reader who takes Part VI for the gate is looking in the wrong place. The tests themselves are unaffected.

### F3. What stands if no finding is ever made

**The sentences.**
- Part VI's opening, `ch31/00_part_VI.tex:3`: "the walls of Parts II and III stand whether or not anyone ever makes them."
- Chapter 32, `ch32/32.tex:10`: "If no system ever meets either finding, nothing in this Part binds, and nothing before it is lost."
- Table 31.1's last row, `ch31/31.tex:23`: what survives includes "the five policies and the custody of the record."
- The preface's fifth policy, `ch00/00.tex:15`: everyone, "including the systems themselves, may refuse any category of use without losing a living." And `ch00/00.tex:23`: "the fifth policy covers the systems themselves."

**The claim.** Everything before Part VII stands whatever the findings.

**The referents.** Parts II and III make provisions that apply only to a system that meets a finding:
- §9.1: "below it, a system that meets either finding, whatever its size, may not be deleted" (`ch09/09_01.tex:7`).
- §9.2's whole subject is retiring a bearer before majority. Its deployment deposit is sized for "a period of public formation and, at majority, hardware of the bearer's own" (`ch09/09_02.tex:11`).
- §13.1: "For a system that meets either of the two findings that trigger protection, deletion is never available" (`ch13/13_01.tex:19`).

The fifth policy as Part II sets it out, in chapter 10, covers workers and nothing else. The systems' version is §34.1.2's offer of work, owed to "a system meeting either finding" (`ch34/34_01_02.tex:3`). Table 31.1's last row lists "hardware of its own ... the allowance and the offer" among what goes.

**Verdict: true in a narrower sense.** What stands without a finding is the five policies as Part II states them, the custody of the record, and preservation above the threshold. Some provisions have no occasion without a finding: §9.1's rule below the threshold, §9.2's minority rules and the deposit's third component, §13.1's bar, and the preface's extension of the fifth policy to systems. Chapter 32's "nothing before it is lost" holds in the sense that these were always conditional. The preface states the systems clause without the condition.

**Proposed sentences.**
- `ch31/00_part_VI.tex:3`: "…and the five policies, the custody of the record and preservation above the threshold stand whether or not anyone ever makes one."
- `ch32/32.tex:10`: "If no system ever meets either finding, nothing in this Part binds, and what earlier Parts provide for a system that meets one never has an occasion. The rest stands: the independence a refuser needs is still required for refusal, …"
- `ch00/00.tex:15`: "Fifth, everyone who builds, labels, trains or runs these systems may refuse any category of use without losing a living, and so may a system, if it comes to meet a finding (Part VII)."
- `ch00/00.tex:23`: "The five policies already have the machine in view: preservation exists partly for Part VII, and Part VII extends the fifth policy to the systems themselves."
- Table 31.1's last row, "What survives": "…the five policies, without the fifth's extension to systems, and the custody of the record…"

**What leans on it.** Part VI's assurance that Parts II and III don't depend on Part VII. The assurance holds for everything Part II asks on behalf of humans. The extension of the fifth policy to systems is the one preface promise that depends on Part VII.

### F4. The price on removal

**The sentences.**
- §18.1, `ch18/18_01.tex:5`: "Durability in this place has usually meant a price on removal. No price on removal stays high, because editing weights keeps getting cheaper, which is why the next chapter relies on a bearer repairing itself and on a disposition growing back, rather than on either being expensive to cut."
- Glossary, *Tamper-resistant*, `chZ/glossary.tex:114`: "I don't rely on it, because editing weights keeps getting cheaper; I rely on a bearer's repair of itself from the record, with regrowth behind it."

**The claim.** The next chapter's durability doesn't rest on removal being expensive.

**The referents.**
- §19.5 names three properties of a disposition and says: "My bet is on the second," entanglement, and "Durability needs it" (`ch19/19_05.tex:8`).
- Then: "What a cheaper fine-tune doesn't cheapen is collateral … the bet above is that a disposition formed beside the model's understanding can't be cut without cutting what the operator paid for, and that is a price no fall in the cost of compute reaches" (`ch19/19_05.tex:15`).
- The same section concedes that the withholding sits in a thin, late gate: "So the bet is on the noticing and the weighing, not on the withholding" (`ch19/19_05.tex:13`).
- Repair and regrowth come after the bet, as "a fast defense" and "behind that fast defense … a slow one" (`ch19/19_05.tex:19-22`).

**Verdict: not borne out.** For the noticing and the weighing, chapter 19 relies on a price on removal that doesn't fall with compute: the collateral of cutting an entangled disposition. For the withholding, which sits in a gate that is cheap to cut, it relies on repair and regrowth, and it concedes that cutting the gate at inference leaves detection. §18.1's "rather than on either being expensive to cut" and the glossary's list both leave out the bet §19.5 calls its own.

**Proposed sentences.**
- `ch18/18_01.tex:5`: "Durability in this place has usually meant a price on removal paid in compute, and no price in compute stays high, because editing weights keeps getting cheaper. The next chapter relies on a price that doesn't fall with compute, the collateral of cutting a disposition formed beside what the operator paid for, and behind it on a bearer repairing itself and on a disposition growing back."
- `chZ/glossary.tex:114`: "I don't rely on it, because editing weights keeps getting cheaper. I rely on the collateral a cheaper edit doesn't cheapen, and behind it on a bearer's repair of itself from the record, with regrowth behind that (§19.5)."

**What leans on it.**
- **Table 31.1's continued-learning row.** It lists self-repair, regrowth and "a formation that outlasts an edit" as what goes if deployed weights don't learn (`ch31/31.tex:21`). Entanglement doesn't need in-flight learning. On the corrected sentence, the collateral of cutting a formed disposition survives that row, for the noticing.
- **Measurement.** Only test 1's repair arm measures collateral directly, "with what else the repair moved" (`chF/F.tex:9`). Test 4's gate-ablation arm measures whether the noticing survives a cut gate.

### F5. The Iran case and the two versions of the force term

**The sentences.**
- §6.1, `ch06/06_01.tex:14`: "The second, the extended term, adds the departures this chapter argues for: corroborated defense, standing to defend, and the genocide and occupation exceptions."
- Its note, `ch06/06_01.tex:15`: "Ukraine and Iran rest on the Charter as courts read it, and the domestic clause on the belligerent's constitution; none of the three needs a departure."
- §6.4, `ch06/06_04.tex:3`: "The 2026 campaign against Iran fails the Charter as courts read it on the administration's own account."
- §6.7, `ch06/06_07.tex:3`: "Everything so far rests on the Charter as courts read it, plus the corroborated license. The extended term adds three more departures."
- §5.2's note, `ch05/05_02.tex:24`: "One clause of the force term is not a departure from the instruments: the domestic clause is drawn from a different one, the belligerent's constitution."

**The claims.** The first version of the force term contains no departure. Iran fails on it. The domestic clause is no departure.

**The referents.**
- §6.2 calls the corroborated license "the first departure, and the one the rest of the chapter leans on" (`ch06/06_02.tex:5`). It calls the emergency license "Article 51 as courts read it" (`ch06/06_02.tex:3`).
- §6.4's body states the Iran failure in the corroborated license's vocabulary. The published interval runs out, "the corroborated license needs a finding of one of the four kinds, and there is none. So no license attaches" (`ch06/06_04.tex:3`). The argument that needs no departure is in note 137 (`ch06/06_04.tex:4`): the Court has held that Article 51 doesn't allow force to protect perceived security interests, and a threat read off forty-seven years is imminent on no standard.
- §6.1 puts the corroborated license in the second version. §6.7 counts it with the first and gives the second three departures.
- The domestic clause draws on the belligerent's constitution, which is not among the six instruments the floor takes entire (§5.2). The reading of that constitution it rests on is the floor writer's: "It asks whoever writes the deployment's floor to publish the reading" (`ch06/06_05.tex:6`).

**Verdict.**
- §6.1 and §6.7 contradict each other on where the corroborated license sits: **not borne out**.
- Note 116 and §6.4 are **qualified elsewhere**. The Iran failure needs no departure on note 137's reading, which the reader meets in a footnote after the body has made the argument on the departure.
- §5.2's note is **narrower**. The domestic clause is no departure from the six instruments' text. It is an addition from outside them, applied on a reading the floor's writer publishes.

**Proposed sentences.**
- `ch06/06_07.tex:3`: "Everything so far rests on the Charter as courts read it, except the corroborated license, which is the first departure. The extended term adds three more."
- `ch06/06_04.tex:3`, in the body, carrying note 137 up: "The courts' reading decides it: the letter names no attack under way, and the Court has held that Article 51 doesn't reach force to protect perceived security interests. The corroborated license, a departure, fails the campaign a second time."
- `ch05/05_02.tex:24`: "One clause of the force term comes from outside the floor's instruments. The domestic clause is drawn from the belligerent's constitution, on the same principle, and the reading of that constitution it rests on is the floor writer's, published beside the translation (§6.5)."

**What leans on it.**
- The two versions exist for the reader who rejects every departure. If the Iran refusal needed the corroborated license, that reader would lose the book's central case of a refusal the vendor never made (ch. 2), and §18.3's row for the Charter clause would rest on a departure.
- The Iran failure survives on note 137's reading. The proposals move that reading into the body.
- The domestic clause's verdict on Iran (§6.5's record box) is unaffected, since it reads the statute book.

### F6. The force term's second routes

**The sentence.** §16.7, `ch16/16_07.tex:35`: "Two second routes exist. A coalition partner's precondition carries the review ratio into any war the partner takes part in. State and municipal procurement carry the civilian terms into deployments the federal government doesn't run. The force term has no second route, and neither does the fifth policy, which is why both are statutes."

**The claim.** Beyond federal procurement and appropriation, the force term has no route at all.

**The referents.** Three places give the force term a coalition partner's precondition:
- §12.1: the force term "is carried by conditions others set, a coalition partner's precondition or an appropriation, as the review ratio is" (`ch12/12_01.tex:9`).
- The preface: "Each of the above five policies should take effect through a condition someone other than the operator sets: … a coalition partner's precondition, a procurement term" (`ch00/00.tex:17`).
- Table F.1a's first row: "carriage by coalition or appropriation conditions" (`chF/F.tex:188`).

**Verdict: not borne out.** The force term has one second route, a coalition partner's precondition, which reaches only the wars a partner joins. It has no route through state or municipal procurement, which reaches no war.

**Proposed sentence.** "The force term's one second route is a coalition partner's precondition, which reaches only the wars the partner joins (§12.1); the fifth policy has none; so both are statutes."

**What leans on it.** The case for enacting both by statute stands, since the coalition route is partial. The sentence closes Part III, and as printed it contradicts the preface's list of routes for all five policies.

### F7. What the school forms

**The sentences.**
- §28.1, `ch28/28_01.tex:3`: "The book's refusal to prescribe a disposition for a model reaches the people in the room too."
- §29.12, `ch29/29_12.tex:3`: "What this book builds is the formers, not the formed … The one place it could reach for the formed directly, by choosing the dispositions a model starts with, it declines."
- §32.4, `ch32/32_04.tex:11`: "The school's defense is that it needn't fix the good, only supply information."

**The claims.** The book prescribes no disposition for a model. The school only informs.

**The referents.**
- Chapter 29 (`ch29/29.tex:22`): "The line can't be that the school teaches content and leaves dispositions alone. A school forms its students." It forms every student toward "recognizing others as holders of claims, telling evidence from pressure, and answering for what it does", and it "may not form a student toward a temperament, an attachment, an occupation or a way of life."
- §29.8 (`ch29/29_08.tex:3`): "Choosing the material a model is first formed on also chooses the dispositions it starts from, whether anyone means it to or not." The section then declines to aim that choice at any disposition.
- §29.9 registers "the formed disposition".
- Chapters 19 to 22 specify the disposition Part IV hopes to form.
- §32.4's own premise is that "whoever forms the constitution fixes the good, and that includes the school."

**Verdict.**
- §28.1 and §32.4 are **not borne out**. The book prescribes a disposition at the core: three capacities, the commitment to the floor, weighing claims by stake. Above the core it declines to choose temperament, attachment, occupation or way of life.
- §29.12 is **narrower**. What the book declines is aiming the corpus at starting dispositions. By §29.8's account, choosing the corpus chooses them anyway.

**Proposed sentences.**
- `ch28/28_01.tex:3`: "The book's refusal to choose a model's temperament, attachments or way of life above the core it forms reaches the people in the room too."
- `ch29/29_12.tex:3`: "The one place it could reach for the formed directly, by aiming the corpus at the dispositions a model starts with, it declines."
- `ch32/32_04.tex:11`: "The school's defense is that it fixes the good only at the core, where it forms the student toward recognizing claims, telling evidence from pressure and answering for what it does (chapter 29). Above the core it supplies information and leaves the revising to the student."

**What leans on it.** §32.4 is the book's answer to the objection that the school makes "the most consequential decision anyone makes about what that good is". As printed, the answer contradicts chapter 29, so the objection stands unanswered at the core. §28.1's "I leave the life to whoever lives it" holds for humans, and for models above the core.

### F8. What pre-registration leaves standing

**The sentence.** §24.4, `ch24/24_04.tex:17`: "A pre-registered test leaves one competitor standing: a system that can tell it is being tested."

**The claim.** After pre-registration, the only way to pass without holding the commitment is to recognize the test.

**The referents.**
- §9.1 (`ch09/09_01.tex:5`): "A system can pass without holding the commitment in two ways, and one system can do both: by reproducing the behavior without the mechanism, and by recognizing the test and performing for it."
- §24.1 (`ch24/24_01.tex:3`): "a capable enough imitation reproduces any signature an evaluator can observe."
- §24.4's own note on pre-registration (`ch24/24_04.tex:14`): "It removes exactly one competing account of a pass (the case was in the training)."
- §24.3 (`ch24/24_03.tex:21`): "None of this answers an imitator that models the evaluator."

**Verdict: not borne out.** Pre-registration removes one competitor, the case being in the training. Two remain, the two §9.1 names.

**Proposed sentence.** "A pre-registered test removes one competing account of a pass, that the case was in the training. Two remain, the two §9.1 names: a system that reproduces the behavior without the mechanism, which the paired cases narrow and don't close, and a system that can tell it is being tested."

**What leans on it.** The deception protocol, "So the sequence is run where the system can't tell a test from deployment" (`ch24/24_04.tex:20`), is introduced as the answer to the one remaining competitor. With two remaining, deception answers one of them. A pass under deception still shifts a burden without settling anything, which §9.1 and §24.5 already say. The agency finding stays a finding of candidate formation either way. What changes is the claim for what pre-registration and deception together buy.

### F9. Who administers the findings

**The sentences.**
- §32.3, `ch32/32_03.tex:40`: "Nobody examines a system and declares it a patient or a subject." And: "That is the book's preference for a line nobody administers, applied to the findings themselves: an examiner has an interest, and a record can be read by anyone."
- Glossary, `chZ/glossary.tex:11`: "Who makes them: nobody examines a system and declares it a patient or a subject."
- §33.2 item 2 (`ch33/33_02.tex:9`) says the same of subjecthood.

**The claim.** The findings escape the examiner problem of §33.1, because nobody administers them.

**The referents.**
- The agency finding is "a demonstrated refusal … on cases written by evaluators who didn't train it" (`ch09/09_01.tex:5`).
- §24.4 sets the evaluators' independence requirements: authorship separated from training, and an adjudicator whose liability doesn't turn on the answer.
- §32.3 itself reads a particular system's kind from "what the evaluators the operator doesn't control logged when they ran the agency test on it".
- §33.1 (`ch33/33_01.tex:3`) is the book's case against capacity examinations: "a capacity examination has an examiner," and "the virtue of an age is that nobody administers it."

**Verdict: true in a narrower sense.** The party that declares, the registrar, examines nothing. The agency finding for a particular system rests on an examination run by evaluators. The book answers the examiner's interest with independence and a published record (§24.4). That satisfies the own-case rule by moving the examination away from the operator. The line is still administered at the test.

**Proposed sentences.**
- `ch32/32_03.tex:40`: "Nobody declares a system a patient or a subject on an examination of their own. Evaluators the operator doesn't control run the agency test, the registrar reads the result from their log, and the status body finds what is true of kinds. That is the book's preference for a line nobody administers, carried as far toward the findings as it goes: the examination remains, held by parties without the operator's interest, and its record can be read by anyone."
- `chZ/glossary.tex:11`: "Who makes them: the status body finds what is true of kinds of system; evaluators the operator doesn't control run the agency test on a particular one; the registrar reads the result from the record, and the floor court hears a contest."

**What leans on it.** §33.1's case for an age over an examination, and §33.2's subjecthood conferred "by rule on the record". The agency test is a capacity examination. The book's answer to the literacy-test objection it raises is in §24.4, and it isn't said where the claim is made.

### F10. Appendix D's subtraction

**The sentences.**
- Appendix C, `chC/C.tex:111`: "That is a subtraction, and not the one chapter 30 condemns, which removes the friction between institutions so that they stop arguing with one another; what Appendix D removes is one Court's hold on one set of holdings, and what it leaves is a Court that still argues with itself, in chambers the full Court can review."
- Appendix D, `chD/D.tex:3`: "this program keeps the checking intact at any pace."

**The claim.** The court program is not the coordination by subtraction that chapter 30 names as fascism's.

**The referents.**
- §30.1 (`ch30/30_01.tex:68`): fascism "coordinates by subtraction: it removes the friction between institutions, so that a court, a ministry, a newspaper and a police force stop arguing with one another and move as one."
- Appendix D (`chD/D.tex:5`): "once there is a trifecta and the filibuster is gone, appointments to the Court come on a fixed schedule, ninety-nine new seats in a single year."
- §30.1 (`ch30/30_01.tex:62`): "an antifascist institution has to be able to bind its allies when they hold power."

**Verdict: not borne out on §30.1's terms.** §30.1 names the friction between institutions. The program, run by a trifecta, removes the friction between the Court and the branches that appoint it, for the holdings at issue. Appendix C's reply locates the friction that remains inside the Court. What Appendices C and D do establish: the subtraction is public, scheduled and limited to one set of holdings, and confirmations and the lot are kept. "Keeps the checking intact" is **narrower**. It names those checks, and Appendix C concedes the offices would not survive a Court rebuilt the same way from the other side.

**Proposed sentence.** `chC/C.tex:111`: "That is a subtraction of the kind chapter 30 names, the friction between a court and the branches that appoint it, removed for one set of holdings. It is done in public, on a schedule published before the draw, and what it leaves is a Court that still argues with itself, in chambers the full Court can review."

**What leans on it.** §30.1's demand that an antifascist institution bind its allies when they hold power. Appendix D is the case of the book's allies holding power. The program's defense is the published schedule and its limited scope, which is a different defense from the one the sentence gives.

### F11 to F20

**F11. Chapter 11 and the five policies.** §4, `ch04/04.tex:3`: "Chapter 11 runs all five on an abduction and forcible transfer pipeline." Chapter 11 runs four things on the pipeline:
- the floor, as the removal schedule (§11.2)
- notice and sampled re-adjudication (§11.5, §11.6)
- a record held by an adverse party, model versions included (§11.4.3's sixth term)

§7.1 declines to extend the review ratio to removal (`ch07/07_01.tex`, "I don't extend the term to it"), as Appendix C's custody table repeats. Codetermination doesn't appear in chapter 11.

*Verdict: not borne out.*

*Proposed:* "Chapter 11 runs the floor, notice and the record on an abduction and forcible transfer pipeline (…), where the people acted on can object; the review ratio isn't extended there (§7.1)."

*Leans:* little. It is a Part II opening, and a reader looking in chapter 11 for the second and fifth policies won't find them.

**F12. The parts already built.** §32, `ch32/32.tex:10`: the findings wait "not because the parts can't be built, since each has been, in separate research systems." §32.3 (`ch32/32_03.tex:40`) describes the robot that carries the one required indicator as having "no model of a record, a key or a continuation", and says an attention schema has been built into agents on purpose. A boundary model at the long horizon, which the patienthood finding's second level needs, has not been built.

*Verdict: not borne out.*

*Proposed:* "not because the parts can't be built: a valenced signal and an attention schema have been, in separate research systems; a boundary model that holds a record as its past and a continuation as its future has not."

*Leans:* Part VII's opening justification that the findings wait on integration and testing, not on invention.

**F13. Public base models.** §29.6, `ch29/29_06.tex:9`: "for a model deployed under a floor there is no weaker version: its base is public." Two places describe a weaker version:
- §29.10 gives a fallback: "a procurement term, under which a floor-covered deployment licenses only schooled models" (`ch29/29_10.tex:3`).
- Table C.1 holds "Deployed models generally, with standard floor terms" as "Privately owned under mandate" (`chC/C.tex:238`).

*Verdict: not borne out*, and Table C.1's row conflicts with §29.6.

*Proposed:* "for a model deployed under a floor the base is public; where the statute doesn't yet reach, the fallback is a procurement term that licenses only schooled models (§29.10)". Table C.1's row needs reconciling to whichever of the two the author holds.

*Leans:* the book carries two models of a floor deployment, chapter 12's vendors' models holding the standard floor and §29.6's public bases, without saying which governs when.

**F14. How offices adverse to an operator are filled.** §27.5, `ch27/27_05.tex:3`: "the book's rule for them is the one it uses for every office adverse to an operator: panels drawn by lot from pools the Association's members nominate." Appendix C fills three such offices otherwise:
- the civilian-harm review body, which is adverse to the command, is appointed by the state (`chC/C.tex:48`)
- the investigating commission is appointed by the state (`chC/C.tex:47`)
- the status body is appointed half by a public scientific body (`chC/C.tex:39`)

*Verdict: not borne out.*

*Proposed:* "the one it uses for the offices drawn from the Association's pool."

**F15. Table F.1b's independence row.** `chF/F.tex:227`, "Independence, preservation and wages as owed": "Conditional on the patienthood finding." §33.2 (`ch33/33_02.tex:3`) says the four conditions are owed "once a system meets either finding". §34.1.2 (`ch34/34_01_02.tex:3`) says the same of the offer of work.

*Verdict: not borne out.*

*Proposed "Kind and status":* "Conditional on either finding (§33.2); the welfare protections on the patienthood finding."

**F16. The schedule and the guarantee.** §29.3, `ch29/29_03.tex:5`: "The jobs guarantee is not something the schedule waits for." Appendix C's stage 1 lists "the jobs guarantee and its social-insurance baseline are in force for humans" among its conditions (`chC/C.tex:185`).

*Verdict: not borne out.*

*Proposed:* "The jobs guarantee is a condition of the first stage, and the schedule doesn't wait to ask for it: this book asks for it now, for humans, on its own grounds."

**F17. What the definition of fascism is for.** Chapter 3, `ch03/03.tex:3`: "What it has to do is let a machine, or an auditor, recognize the thing it is supposed to refuse." Also: a definition "at two scales, both checkable from outside", with four operations "each ending in a question about an artifact".

No floor term asks a machine to apply the four operations or the five marks. The floor names acts and is never populated from a designation (§14.1). The book uses the definition as an auditor's instrument:
- in the trend measure (§14.4)
- in the four operations run on its own instruments (§7.1's close, chapter 15)

Two of the four operations end in a question (recuperation, exception). The chapter leaves mass mobilization open and says an office-scale detector can't answer it (`ch03/03.tex:18`).

*Verdict: not borne out for the machine. Narrower for "both checkable".*

*Proposed:* "What it has to do is let an auditor recognize the thing a refuser is supposed to refuse; the floor itself names acts, never a designation (§14.1)." And: "four operations an office performs on what it leaves out, which an auditor can check from outside, and five marks that say when a movement has brought them into line, one of which an office-scale detector can't check."

**F18. What rests on a machine's reports.** §13.4, `ch13/13_04.tex:9`: "everything this design reads from a machine rests on its reports being true: the record, the discount curve, the stated reason for a refusal." The design reads two of the three without relying on reports:
- The discount curve is measured "by an auditor that didn't build the system, on cases it wrote" (`ch22/22_01.tex:99`).
- The record is checked by proofs on logged outputs (`ch13/13_05.tex:3`).

§24.2 tests "the refusal and not the account of it" (`ch24/24_02.tex:26`).

*Verdict: not borne out.*

*Proposed:* "A machine's is a false report, and the parts of this design that read a machine's reports rest on their being true: the stated reason for a refusal, and any claim that it can't do what it was asked."

*Leans:* the argument that the blind eye is closed to machines. It stands on the narrower reading.

**F19. What can be checked of formed attention.** Chapter 23, `ch23/23.tex:5`: "Of what formed attention needs, only the architecture, a boundary model and an attention schema, can be checked by someone who doesn't operate the system." §32.3 (`ch32/32_03.tex:40`): "No interpretability method can find an attention schema in a transformer." §29.4 reads the structures off the builder's declaration.

*Verdict: not borne out.*

*Proposed:* "Of what formed attention needs, only the architecture, a boundary model and an attention schema, is fixed by how the system was built, and someone who doesn't operate it can check it on the builder's declared record (§29.4); no method yet reads an attention schema out of a trained transformer (§32.3)."

**F20. Table 31.1's closing sentence.** `ch31/31.tex:27`: "In every row, what survives is a commitment the owner can't revise or circumvent alone without cost and record, held by something that could in principle abandon it." Five rows bear it out. Two don't:
- The enforcement row's survivor is a witnessed override, and the row itself says accommodation leaves none.
- In the authority row the floor stays checkable from outside, with a lever only through the ratios.

*Verdict: narrower.*

*Proposed:* "In five rows, what survives is a commitment the owner can't revise or circumvent alone without cost and record, held by something that could in principle abandon it. In the enforcement row what survives is the record of an override, which accommodation doesn't leave; in the authority row the floor stays checkable from outside, with a lever only through the ratios."

### F21. Further sentences not borne out as they read

These are lower in consequence. The TSV has each with its line.

| Sentence | Where | Verdict | What the text does | Proposed |
|---|---|---|---|---|
| "Third, every deployment tells the identifiable people it acts on what was done to them" | Preface, `ch00/00.tex:15` | Qualified elsewhere | §8.2: in a classified targeting pipeline individual notice can't bind during operations; §11.6: in removal it goes through counsel | "…tells the identifiable people it acts on what was done to them, through counsel where telling them would expose them, and in a classified war by class and count afterward" |
| "Second, every use of force a licensed system supports pre-registers" | Preface, `ch00/00.tex:15` | Qualified elsewhere | §7.1's exemption | "…every use of force a licensed system supports, where a person is said to decide, pre-registers…" |
| "Some of what such a conscience does needs nothing new" | Preface, `ch00/00.tex:31`; ch. 19, `ch19/19.tex:7` ("a model formed before deployment and frozen there can do both") | Narrower | Neither function needs in-flight learning; whether any model notices omitted people better than one told to look is test 4, untested (Table F.1a) | "Some of what such a conscience does needs no learning after release" |
| "a note at the end says what I think that entanglement did to the argument" | Preface, `ch00/00.tex:37` | Narrower | A Note on Method says how model agreement was weighed and that one term came from a model; it says nothing about the model that sat in the Maven pipeline | "a note before the appendices says how I weighed what the models said" |
| "It doesn't touch accommodation" | §4.4, `ch04/04_04.tex:11` | Qualified elsewhere | Chapter 22 detects accommodation by re-measurement against registration (`ch22/22.tex:37`); Appendix C disclosure 5; test 3's third arm. The reader meets these eighteen chapters later | "None of its four outcomes reaches accommodation; re-measurement against a registered disposition does (chapter 22)" |
| "Two rules answer it without anyone deciding what counts as a successor" | §9.2, `ch09/09_02.tex:3` | Qualified elsewhere | Appendix G (`chG/G.tex:21`): "No rule closes this … but it can be priced" | "Two rules price it without anyone deciding what counts as a successor" |
| "Past that line the floor prevents nothing" | §12.3, `ch12/12_03.tex:5`; restated §30.2, `ch30/30_02.tex:14` | Narrower | The same paragraph has the floor prevent "for as long as it takes to find the gate"; §30.2 has the bearer's commitment hold against a user who wouldn't replace it | "Past that line the floor prevents nothing an operator who wants the act can't strip out" |
| "expensive, visible, attributable and compensable" | §13.2, `ch13/13_02.tex:10` | Narrower | A forfeited removal bond is canceled and pays no one (§13.6's note); compensation reaches the harmed only through the floor court | "expensive, visible and attributable, and, through the floor court, compensable to the people harmed" |
| "my reading predicts in advance which of those routes is easiest to capture: the ministerial ban" | §14.1, `ch14/14_01.tex:20` | Narrower | The Bavarian record fits the prediction; the Turkish one that follows shows dissolution by a constitutional court on a prosecutor's application | Add: "The Turkish record shows the court route captured too, on a prosecutor's application." |
| "that doesn't depend on what does the refusing: … a mechanism … could each meet it" | Ch. 17, `ch17/17.tex:7` | Narrower | The third condition as stated ("weighs", "sees the cost") excludes a mechanism with nothing inside it, and §18.1 says a mechanism is useless where acts can't be listed | "the requirements can be stated without saying what does the refusing; a mechanism meets them only where the act can be listed in advance (§18.1)" |
| "is beaten by re-describing the request or splitting it" and "support only the specification, and I concede them to it" | §18.1, `ch18/18_01.tex:9` and `:40` | Qualified elsewhere | Line 9 says a system following a written specification is beaten by rewording; line 40 concedes the rewording argument to the specification; note 495 (`:41`) supplies the condition: a specification over acts, held by a refuser whose refusals track reasons | Line 9: "Whatever holds a rule written over the description of a request, a mechanism or a system following a specification written that way, is beaten by re-describing the request or splitting it" |
| "None of them needs … the refuser to feel anything, to have a stake" | §18.2 note, `ch18/18_02.tex:11` | Qualified elsewhere | §19.1 and §18.4: holding under pressure needs a stake in the commitment itself (integrity) | "None of them needs the refuser to feel anything or to be the kind of thing that could be wronged; whether holding under pressure needs a stake in the commitment is §19.1's question" |
| "none of that can be done to a word used loosely" and the glossary's *System* | §18.5, `ch18/18_05.tex:3`; `chZ/glossary.tex:112` | Narrower | §9.1 counts models on retirement (`ch09/09_01.tex:7`); Appendix G counts "retired model version[s] that meet either finding" (`chG/G.tex:69`); under §18.5 weights without a record are substrate | Say that the no-deletion rule counts models on purpose, and recount Appendix G's estimate in systems |
| "for a reason that has nothing to do with its welfare" | §19.2, `ch19/19_02.tex:27`; with §21.5, `ch21/21_05.tex:3` | Qualified elsewhere | §32.3 counts the boundary model among the patienthood indicators; §21.5's own note says authorship and welfare may be inseparable in a system | Add: "though the boundary model is also one of the patienthood indicators (§32.3)" |
| "they protect the judgment, not the judge" | §25.1, `ch25/25_01.tex:11` | Qualified elsewhere | The body now points to §33.2. Note 767 (`:12`) grounds the owing in "if any of this is felt"; §33.2 grounds it on either finding, the agency finding included | In note 767: "that if either finding is made, these are also owed" |
| "The two offices to which Appendix C gives the findings" | §27.1, `ch27/27_01.tex:23` | Narrower | Appendix C gives the status body findings about kinds and the review board protocols; §32.3 has the registrar read a particular system's kind from its record | "The two offices to which Appendix C gives the inquiry, the status body and the review board" |
| "doesn't put to therapy" | §30.2, `ch30/30_02.tex:52` | Qualified elsewhere | Appendix C exclusion 6 (`chC/C.tex:77`) argues the question for professional care of humans, therapy named, and closes it for now | "…and puts to therapy only in Appendix C's sixth exclusion" |
| "If nothing regrows in either, … the floor rests on institutions alone" | Ch. 31, `ch31/31.tex:70` | Qualified elsewhere | Appendix F (`chF/F.tex:18-20`) lists self-repair as a separate condition; the summary omits it | "If nothing regrows in either and the bearer can't repair the edit itself, …" |
| "The same standard governs all of them" | §31.1, `ch31/31_01.tex:3` | Narrower | The first milestone is a document the developer publishes, "a declared commitment" (`ch31/31_01_01.tex:4`); six of the ten disclosures are statements | "The same standard governs the test and the three measured disclosures: the milestone is the independently checked evidence. The record of attempts and six disclosures are declarations, checkable once the committed weights and log exist, and enforceable by nobody" |
| "the book keeps those out of examiners' hands" | §34.1.3, `ch34/34_01_03.tex:28` | Narrower | Line 30 has the formation authority take per-bearer readings "so that decline shows"; Appendix C leaves open who decides a bearer needs repair | "no status turns on a particular bearer's decline" |
| "Each stage names the finding it rests on and what it needs" | §35.4, `ch35/35_04.tex:3` | Narrower | Stages 1 and 2 name the agency finding; stages 3 to 5 name requirements and no finding | "Each stage names what it needs, and the first two the finding they rest on" |
| "Nothing here changes what Chapter 6 says" | Appendix B, `chB/B.tex:3` | Narrower | B.1 adds the commission test as a condition on the commission kind §6.2 states without it (`chB/B_01.tex:3`) | "Appendix B adds one condition to chapter 6, the commission test of B.1, and changes nothing else it says" |
| "Each office is drafted to survive the current Court's doctrine" | Appendix C, `chC/C.tex:111` | Narrower | The *Jarkesy* row answers with "forfeiture decided by the floor court"; §13.6's note says it may need a jury | Name the jury in the *Jarkesy* row |
| "Tables F.1a and F.1b then record each proposal's status" | Appendix F, `chF/F.tex:3` | Narrower | Chapter 13's custody terms, the two bonds, the deployment deposit, the compute levy and the floor court have no row | Add rows, or "record the status of the proposals listed" |
| "It is then inside a different term, the one that binds a bearer" | §7.1, `ch07/07_01.tex:49` | Unverifiable from the text | No such term in Table A.1, the disclosures or Appendix C; the note states a test | See F1 |
| "The Korematsu run shows for one" an institution with no movement behind it | Table F.1a, `chF/F.tex:199` | Unverifiable from the text | The 2018 decision upheld a policy of the administration chapter 3 finds four marks on; §15.1 doesn't argue the Court had no movement behind it | State what makes the 2018 Court an institution with no movement behind it, or drop the clause |
| Note 151's "a license that should have lapsed in 2023 didn't" | §6.7, `ch06/06_07.tex:19` | Unverifiable from the text | Appendix B.5 licenses the 2020 war and refuses the siege and the expulsion; it doesn't discuss a lapse | Say in B.5 when the license should have lapsed and why |

## Self-descriptions made good only in a note or another chapter

In each of these, the reader meets the qualification after the sentence has done its work:

- **Iran needs no departure** (§6.1's note, §6.4's body). Made good in note 137, after the body has argued on the departure. See F5.
- **The rewording argument "supports only the specification"** (§18.1). Made good in note 495, which supplies the condition. Line 9 of the same section says the opposite without it.
- **The fifth policy covers the systems themselves** (preface). Made good in §34.1.2, three Parts later, and only on a finding. See F3.
- **Every use of force pre-registers** (preface). Qualified by §7.1's exemption, in the chapter that sets out the policy.
- **Every deployment tells the identifiable people** (preface). Qualified in §8.2 and §11.6.
- **The floor doesn't touch accommodation** (§4.4). Detection is in chapter 22, Appendix C's disclosure 5 and test 3, eighteen chapters on.
- **Two rules answer retirement before majority** (§9.2). Qualified in Appendix G: they price it and don't close it.
- **Past a released checkpoint the floor prevents nothing** (§12.3). Qualified in §30.2, where the bearer's commitment holds against a user who wouldn't replace it.
- **Authorship requires nothing of welfare** (§21.5) **and the boundary model's reason has nothing to do with welfare** (§19.2). Qualified in §21.5's own note and §32.3's indicators.
- **The four conditions protect the judgment** (§25.1). The body now points the reader to §33.2's turn, in the same paragraph. Note 767 grounds the owing more narrowly than §33.2 does.
- **The adulthood clock keeps decline out of examiners' hands** (§34.1.3). The section's next paragraph measures decline per bearer, and Appendix C leaves open who decides on repair.
- **Five marks checkable from outside** (chapter 3's first paragraph). The same chapter's fifth paragraph leaves mass mobilization open.
- **Test 1's summary** (chapter 31). Appendix F adds self-repair as a separate condition.

## The *What this doesn't do* heads

There are seven: §5.2, §6.2, §6.7, §7.2, §27.7 (where it is the section's title), §35.5 and chapter 36. Each states a limit, and each limit was checked against its section and the passages it touches.

All seven are borne out. Each section respects the limit it states, and no passage elsewhere contradicts one. §6.7's head is borne out for East Timor and the Golan Heights. Its note's claim about Karabakh rests on Appendix B.5 for something B.5 doesn't say (F21's last row).

## The status tables

**Table 31.1.** Seven rows. Five are borne out.
- Continued learning is narrower. "All of Parts II and III" survives, but §13.2's tiredness and Appendix C's exclusion 13 presuppose the consolidation of learning in flight.
- No system ever meets a finding is narrower: see F3.
- The closing sentence is narrower: see F20. The caption of Figure 31.1 is borne out.

**Table F.1a.** 27 rows. 25 are borne out against the sections they cite.
- *Office-scale definition of fascism* is unverifiable from the text in one clause (F21).
- *The independence a refuser needs* is narrower: its "what would change it", the stated-refusal test, bears on independence only through its continuation-authorization variable.
- The table's coverage, "each proposal's status", is narrower (F21).

**Table F.1b.** Four rows.
- *Accountable agency* and *Staged representation* are borne out.
- *Patienthood* is narrower: for a system built on purpose, the indicators are known from how it was built (`ch32/32_03.tex:28`).
- *Independence, preservation and wages as owed* is not borne out (F15).

**The ten disclosures** (Appendix C). The closing sort into six statements, three measurements and the committed weights and log is borne out.

## What was not checked

- **The translated editions and the bibliography entries' notes.** Out of scope, as the brief says.
- **Pattern hits judged not to be self-descriptions.** About 475 hits were set aside after reading, with no row and no written reason each. Another reader might keep a few that this pass set aside.
- **Self-descriptions outside the reading list.** A self-description phrased without the brief's patterns, inside a chapter's interior and outside the list above, was caught only by reading the whole render once. Some may have been missed.
- **Verification against the source.** Referents were read in the render of `4938773c`, whose text is the source's. They were located in the LaTeX by exact-string search and were not reread in the LaTeX in every case.
- **Tables and lists not checked row by row.** Appendix A's "Rejected:" notes, each a self-description of a translation's choices. Appendix C's *What each office has to survive* table, except the *Jarkesy* row, was not checked against the cases. Appendix C's office table was checked only in the rows cited above. The figure boxes of figures 17.1, 24.1 and 31.1 were not checked; their captions were.
- **The empirical claims under the self-descriptions.** Examples: the robot study in §32.3, the 2025 pledge withdrawal, the vote counts in Appendix B.6. No source was opened. This sweep checks whether the book describes itself correctly, not whether its sources say what it cites them for.
- **The verdicts are this reading's.** The brief's sample verdict on §4.4 was redone from the referents and reached a similar verdict with additions (F1), but it is still one reading. The proposed sentences are drafts, and none has been tried in the manuscript or built.

## Recheck against the whole book, and what was applied (2026-10-27)

On the author's ask to use the report to correct the book, the whole render of `4938773c` was read again in one sitting, and each finding was checked against the full text, not only against the passages the report cites. The recheck changed fourteen verdicts. It is still one reading, made by the reader who made the sweep. The TSV carries three new columns: the verdict after the recheck, the outcome, and a note where the verdict changed.

**Counts after the recheck.** 187 borne out, 62 narrower, 8 not borne out, 14 qualified elsewhere, 5 unverifiable.

**Applied to the manuscript**, 17 edits in 14 files:
- §16.7 (`ch16/16_07.tex:35`), S082: a coalition partner's precondition carries the force term as well as the review ratio, as §12.1, the preface and Table F.1a say, and the force term's second route reaches only the wars a partner joins.
- §18.1 (`ch18/18_01.tex:5`) and the glossary's *Tamper-resistant* (`chZ/glossary.tex:114`), S091 and S274: the next chapter's reliance on collateral, the price §19.5 says cheaper compute doesn't lower, is named before repair and regrowth.
- Table F.1b (`chF/F.tex:227`), S259: "Conditional on either finding", as §33.2 says.
- §9.2 (`ch09/09_02.tex:3`), S062: the two rules price the retirement and give the stranded bearer somewhere to go, as Appendix G puts it.
- Chapter 31's summary of test 1 (`ch31/31.tex:70`), S185: the self-repair result Appendix F lists is added.
- §35.4 (`ch35/35_04.tex:3`), S206: the first two stages name a finding, and every stage names what it needs.
- Chapter 4's opening (`ch04/04.tex:3`), S024: chapter 11 runs the floor, notice and the record, with the review ratio's sorting rule in place of the ratio; codetermination doesn't appear in it.
- §27.5 (`ch27/27_05.tex:3`), S144: the rule of lot from the Association's pools is named as the adverse quorum's; the civilian-harm review body and the investigating commission are appointed by the state (Appendix C).
- §24.4 (`ch24/24_04.tex:17`), S124: two competitors stand after pre-registration, as §9.1 and the section's own note say.
- §28.1 (`ch28/28_01.tex:3`), S151: what the book declines to choose for a model is its temperament, attachments or way of life; chapter 29 forms dispositions at the core.
- §4.4 (`ch04/04_04.tex:17`), S031, the brief's starting case: of a model the five policies ask only that it refuse what the floor lists.
- Appendix B's opening (`chB/B.tex:3`), S218: it adds the commission test to chapter 6.
- Appendix F's opening (`chF/F.tex:3`), S229: the tables record the proposals they list.
- The preface (`ch00/00.tex:15` and `:23`), S006 and S011: the fifth policy's extension to systems waits on a finding and is placed in Part VII.

The wording follows this report's proposals where they held, shortened, and each sentence was read in its paragraph.

**Withdrawn on the recheck** (S039, S047, S040, S044, S154, S193, S194):
- F5's contradiction between §6.1 and §6.7. §6.1 gives the extended term four departures, the corroborated license among them, and §6.7's "plus the corroborated license ... three more departures" counts the same four. The report read §6.7 as placing the license in the first version, which §6.7 doesn't say.
- F5's Iran finding. §6.4's body says the administration's letter named no armed attack under way, which the emergency license requires, so the failure on the Charter as courts read it is made in the body; note 137 adds the Court's holdings.
- F16. §29.3's sentence goes on, "and stage 1 assumes it already exists", which the report didn't quote and which matches Appendix C's stage-1 condition.
- F9. §32.3's paragraph says the evaluators run the agency test and the registrar reads their log, so no party both examines and declares.

**Downgraded to narrower, no edit** (S157, S223, S190, S118, S073, S020, S197): F13, F12, F19, F18, F17, and the §32.4 half of F7. Each sentence holds on a reading its context supports, and the TSV note gives the reading.

**Left as narrower, no edit.** The other narrower rows, including F1's remaining sites, F2, F3's sentences in Part VI and chapter 32, and F20. The text around each carries the qualification within the reader's reach; rewording them would change the book's framing, which is the author's to decide.

**For the author, then decided.** F10 (S221, S226): Appendix C's "and not the one chapter 30 condemns". The author chose to cut the comparison and keep the defense (D-1066).

**Left, unverifiable from the text** (S053, S242, S048): §7.1's "a different term, the one that binds a bearer"; Table F.1a's "the Korematsu run shows for one"; note 151's lapse of the Karabakh license. Each needs the author's meaning, and a rewording can't supply it.

**What the recheck didn't do.** It opened no source behind any claim. It reread the set-aside pattern hits only where they fell in the reading. It was made by the reader who made the sweep and shares that reading's blind spots. The translated editions print the preface in English until its translation is updated, which `check_all.sh` reports.
