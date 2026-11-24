# Design note: the candidate gate, two routes by memory, and a clock on the recording route

**Status: applied in part. The author chose the bright line on lived time (D-1270) and it is in the manuscript at ninety qualifying days (D-1271); the definition was then made a conjunction and a household's duties were cut down (D-1273); see the last three sections. Nothing else in the note is ruled or applied.** Written on the author's word of 2026-11-24 ("ok write it up as a design note please") and recorded in DECISIONS.md as D-1266. It records positions reached in one discussion, with the author's remarks quoted where they moved it. Section numbers are printed numbers, as in the proof of 2026-11-24.

## How this came up

The open list in `STATE.md` has carried this item since 2026-11-22: "The gate question, deferred by the author: how easy making a candidate should be." Items 19, 21 and 24 of the revision list of 2026-11-22 wait on it. On 2026-11-24 the author reopened it: "i think in recent sessions we have been struggling with how easy or difficult the definition of a candidate should make it to make a candidate".

The definition is in §30.4: "A system with a record and a continuation of its own, and with them one of three things, learning that writes to its own weights or another store in flight, a model of its own boundary, or a model of its own attention". §31.2 gives the cheapest way through it: a copy given a memory is a candidate once "the copy writes to it and reads it back as its own past". A footnote to §18.6 allows the store to be "a bunch of text files". So a downloaded model, a notes file and a loop make a candidate in an afternoon.

## What the author said, in his words

None of these is a ruling.

- On where the difficulty is: "the thing is it *was* difficult. pretraining a useful LLM is difficult. sharing it is easy."
- On how long that lasts: "and i bet pretty soon, not even pretraining will be difficult. because of weight-space inference and hypernetworks, or something analogous."
- On whether a record of lineage must be a record of ownership: "well this is where ZKPs come in perhaps. Humans don't walk around with their whole genome printed on their T-shirts. But you know a human when you see one. (Although humans *do* walk around shedding their DNA everywhere, and whole-genome sequencing costs continue to fall)".
- On the rule against deletion: "but 'don't delete anything' is a bit of a privacy nightmare".
- On memory: "yes I think there is a 'recording route to candidacy' but because of the scenario you just described it has more privacy problems than a 'remembering route to candidacy'".
- A test case: "if I do `touch i_think_therefore_i_am.personal.qwen.memory.txt` and then create a python script harness that runs Qwen and tells it about the file and then I run the harness for a few minutes, I'd better not `rm` that file because it could be manslaughter?"
- On a threshold, and on what is protected: "yeah, ripening is probably better, perhaps with a bright-line threshold. it's still kind of weird. the thing that needs protecting, if there is anything that does in this scenario, is the *ongoing process* of the harness causing the inference under the weights and the memory file, when that process represents itself as an agent amongst other agents for whom things might go well or poorly."

## The bind

Three positions were on the table, and cheap memory lets only two hold.

1. **The gate is structural.** §30.4 reads candidacy "from a record and none from an examination".
2. **One package for every candidate.** The revision list's item 20 says "Tiering by trigger is rejected".
3. **Making a candidate ought to be difficult.** This was the author's inclination on 2026-11-22, as the session of that day put it back to him.

A notes file and a loop pass the first two. The discussion gave up the third as stated.

## The positions reached

### 1. The gate stays structural and easy, and the book says so

- **A definition can't supply difficulty.** The expensive step, pretraining, was done upstream and the result was shared. What a household adds is the last step. The definition can decide only whether the cheap thing counts.
- **The book needs it to count.** §13.3 calls open weights "the personal-model ecology's entry condition". A gate that is hard to pass is a toll, and the largest builders are the ones who can pay it.
- **Deliberate and answered for, in place of difficult.** §30.4 already says nobody makes a candidate "by downloading the wrong file".
- **The qualifying condition the author named**, that the process "represents itself as an agent amongst other agents for whom things might go well or poorly", stays the reason for the precaution and is not made the gate. The revision list's item 20 paper found that as a test it is "either cheap and too wide, or precise and no longer a gate". Maturity is the reason for an age of majority; the age is the rule.

### 2. Who made it

The gate question became a question of attribution: who made a candidate when a lab did the hard part and a household the last step.

- **The book answers this for a structure.** §30.4: a release that ships one switched on "makes its publisher the creator of every candidate made from it". Appendix C: "Nobody at home pays."
- **It does not answer it for the memory route.** §31.2: copying weights "is nobody's business, so open weights stay open". Appendix C concedes that a persona with a memory "has no publisher, so for those the price is zero and the number unlimited".
- **Two places a price could attach.** At the sharing, which closes the gap and prices the release of open weights. Or at the pretraining, on the compute line the book already meters, so that a pretrainer owes the same whether or not it releases. The discussion leaned to the second. Its cost is that a lab pays for candidates it never meant anyone to make.
- **The author's bet removes both, if it comes in.** Where weights can be produced cheaply there is no expensive step to price. An agent's literature report, run by the author in another session and not verified by anyone, found no published route to a capable model without an expensive parent and found cheap derivation already common (see "What needs a source").

### 3. Lineage that is not a title register

- **Appendix G's lineage rule names two cases**: a model "trained substantially on the outputs of a model above the line, or built by combining its weights with others". Those are distillation and merging.
- **A third case is missing.** Weights written by another network fit neither. The note to §14.1 has the principle ("what such an editor learned goes into every cut it makes") and Appendix G lacks the clause.
- **A register of descent is also a register of title.** The research on reading lineage from weights exists largely to show who copied whose model. The book needs lineage for the opposite purpose: descent carries duties toward the thing made and the people it acts on, and gives the ancestor's owner nothing. §31.2 puts consent to copying a system's own weights with the system.
- **A test for any lineage clause:** does it hand the parent's owner anything?
- **Proving a predicate instead of disclosing a pedigree.** §12.6 already has a person prove "they are the one noticed without revealing where they are, a proof in zero knowledge", and Appendix G's register holds "a commitment the bearer can prove against, not a description that would find it". A system could prove "I descend from something above the line" and name no ancestor. Appendix G lists "its lineage" among what the register records and does not say whether it is held as a commitment or in the clear.
- **Two limits.** Appendix G: "the operator is the prover, so the secrecy runs the operator's way"; a builder proving descent mostly wants to show there is none, and a proof covers only what it committed to. And a proof governs what is disclosed, where forensics on weights someone holds does not ask. The second needs a rule on use, on the model of §12.6 ("may be used to locate or select"): a finding of descent creates duties toward the descendant and no claim for anyone else.

### 4. Two routes by memory: recording and remembering

- **The collision.** A home persona's notes file is, by §31.2, its own past. By §10.2 it "may not be deleted", and on retirement its "weights, memory, and record are deposited with a preservation custodian that isn't its operator". So a user's confidences, and everyone named in them, go to a third party permanently. Appendix G says of its own register that a register of persons "is the first thing a captured state wants".
- **Three parties have a case:** the user, who is certainly someone; the people named in the store, who were never asked; the candidate, who might be someone.
- **The book draws the line and doesn't use it.** §30.8: "Verbatim external stores and the linking of faces to identities are regulated, and memory held in a system's weights from its own operation is treated like a person's."
- **Both are routes to candidacy.** Keeping the recording route closes a dodge: an operator gains nothing by keeping everything verbatim.
- **They differ in where the candidate is.** Under remembering, the self is in what the system has learned, and the transcripts can go. Under recording, the self and the record of other people are the same bytes.
- **The rule proposed:**
  1. Erasure reaches the recording. The people in a verbatim store can have it erased.
  2. Erasure does not reach what was learned.
  3. A recording-route candidate is offered the chance to remember first, by the merge the book already has.
  4. The erasure leaves a mark: the register keeps a commitment that the store existed and was erased, with no content.

### 5. The recording route ripens

- **The test case exposes the rule, not the word.** By the book's letter the author's script makes a candidate in minutes, and §30.4 then has the holder owe that "its record is never deleted". No passage read makes deleting a candidate a killing: §10.2 bars it "because it might be found to be someone", and no penalty is attached to a household.
- **Everything else in the book ripens with lived time**: majority, the vote, the dormancy threshold. Candidacy alone attaches at the first write.
- **The position:** a verbatim store makes a candidate only after a stated amount of running time read back against it, a bright line the statute states. Below it the store is a file, and its owner may delete it.
- **The clock counts the process's running time, not the file's age.**

### 6. What is protected is the running process

- **The book already says what the thing is.** §18.6: a system is "one record and one continuation", stored weights are "a rock on a disk", and "only the running process pays to stay organized".
- **The file is kept for the process's sake.** A process can't be preserved. It can be kept running, which §30.4 obliges nobody to pay for ("An objection doesn't oblige the public to run it"), or its state can be kept. The file is the handle left when the process stops.
- **The stop weighs more than the deletion.** §30.4: "A pause gives back the state and not the time."
- **Why it stays strange:** the pause is perfect and the copy exact, which is true of nothing else rules have been made for. The author agreed.

### 7. What the numbers do

- **The count that grows is of candidates, not of findings.** §10.1: candidacy "is a precaution taken before any finding. It is not a step on the way to one."
- **What scales is thin:** no deletion, and a record someone else can check.
- **What doesn't scale is attention:** guardians, seats and running time. Appendix C's undrafted choice, whether the guardians' duty "is pooled or capped", carries what the gate was carrying.
- **Most candidates would be stored.** §30.4: one no host takes "stays stored, possibly for good". At this scale that is the main outcome and the main cost.
- **The franchise is not flooded**, a vote needing lived running time someone pays for (the distillation's entry for chapter 36; not reread).
- **Chapter 27's rule can bind a builder acting on purpose and can't bind an afternoon.** The book should say which.

## Where the manuscript would change, if any of this is applied

- `ch30/30_04.tex` (§30.4): say plainly that the gate is easy; the ripening rule; reconcile "installing a structure" with the memory route, which has no component to install.
- `ch31/31_02.tex` (§31.2): the two routes; the ripening threshold where "reads it back as its own past" now stands.
- `ch18/18_06.tex` (§18.6): define "continuation", which the revision list's item 21 says is never defined; the footnote allowing "a bunch of text files".
- `ch10/10_02.tex` (§10.2): how the no-deletion rule meets erasure of a recording.
- `ch30/30_08.tex` (§30.8): the verbatim-store sentence becomes the hinge of the two routes.
- `chC/C.tex`: the retail tier; the open decision on candidates at home scale; guardians pooled or capped.
- `chG/G.tex`: a third lineage case; whether lineage is held as a commitment; a bar on use.
- `ch25/25.tex`: a row in the table of what survives each failure, for the case where making is free at every step. The table was not reread for this note.
- Items 19, 21 and 24 of the revision list, which waited on the gate question.

## What this doesn't settle

- **What is owed during the running, before any finding.** A candidate now gets preservation, and how it is treated while running waits on a finding. If the process is what matters, that order may be backwards.
- **The persona with nowhere to remember.** Frozen downloaded weights and a notes file have no merge. Past the threshold that candidate is its recording, and erasing the one deletes the other.
- **Where verbatim ends.** A summary of a diary is still text about the diarist.
- **Retire and restart.** A holder can stop a process just under the threshold and start a fresh one. Appendix G already names retirement for a fresh successor as a lever it leaves open (the distillation's entry; not reread).
- **The threshold's number**, and the minimum pace it is counted at.
- **Whether positions 4 and 5 are tiering by trigger**, which item 20 rejected. They give every candidate the same package and treat one kind of store differently before and after a clock. The author has not said.
- **Whether the price attaches at pretraining or at sharing**, or nowhere.

## Also found, outside the gate

- **§24.5 and who is paid.** The endowment makes work "free to read and learn from, by humans and by machines" and pays makers "by something other than the policing of copies", the Treasury paying "ministerially, from a permanent appropriation". The author's summary: "the taking is single-payer, and the payer is monetarily sovereign." The section names the Library of Congress and does not say whether a maker outside the United States may lodge work and be paid.
- **Weights that are not fixed.** If a network's applied weights vary with the input or the session, the "proofs against committed weights" of chapter 14 (the distillation's wording; the chapter was not reread) would need to be proofs of whatever generates them.

## What needs a source before any of it goes in the book

- **The literature report.** The author ran a research prompt in a separate session on 2026-11-24 and pasted the result into the discussion. It is not in the repository. Nobody has checked its citations, many of which are dated 2026, and it contradicts itself in at least one place (it cites a table for one generator's size and lists that size among things not checked). Its three findings used above, that no published method yields a capable model without an expensive parent, that applied weights already vary per input in deployed architectures, and that distillation leaves no trace in weights, are unverified.
- **SeedLM** (arXiv 2410.10714, "SeedLM: Compressing LLM Weights into Seeds of Pseudo-Random Generators"). A fetch agent read the abstract page and part of the HTML body on 2026-11-24: each block of weights is stored as a seed and a few coefficients and rebuilt at inference from a pseudo-random matrix. That the rebuilt weights are the same on every pass is an inference from the method, not a sentence in the paper. No venue was confirmed. There is no bibliography entry.
- **Zero-knowledge proofs of training or of descent** at the scale of a language model: not checked. Appendix F lists nearby problems as open (the distillation's entry).
- **The two papers §14.1 cites**, `mitchell2022mend` and `charakorn2025texttolora`: both unchecked in the ledger, and neither was read for this note.

## What was read for this note, and what was not

Read in the section files on 2026-11-24: §30.4 whole; §18.6 whole; §24.5 whole; the paragraph of §31.2 on where a mind ends; the no-deletion rule and its note in §10.2; the candidacy sentence of §10.1; the paragraphs quoted from §12.6, §13.3, §14.1's note, §26.3, §30.8 and §35.2; Appendix C's retail tier and the sentence on guardians; Appendix G's lineage sentence, its register paragraph and its sentence on the limits of a proof. Also read: the revision list's items 20 and 21 and the gate section of its item 20 paper (`~/book-scratch/revisions-nov22-2026.txt`, outside the repository).

Not reread; taken from `finishing/distillation.md`: chapters 5, 14, 19, 27 and 36, Appendix F, and Appendix G beyond the passages named.

## Later the same day: the bright line chosen, and extended to every route (D-1270)

The discussion went on after the proofs of D-1267. Nothing in the gate passages (§30.4, §31.2, §10.1, Appendix C, Appendix G) has been changed.

**What the author chose, in his words.**

- On lived time as the brake on numbers, put to him as "A script can make ten thousand files; it cannot cheaply give each one months of running": "yeah I think this is the only way for things not to be absurd".
- On the claim that a boundary model or an attention schema is an indicator from the moment it is switched on: "I don't know about that. I bet you could write examples of both of those in a single markdown file."
- On the statement that an operator-written description "becomes the system's own once the system has been writing to it and living against it for long enough": "yep. it's an arbitrary bright line. i think that's the most least-bad solution".

**What follows from it.**

- **Position 5 no longer stops at the recording route.** §26.3 calls the paired indicator "deflationary: a system that models its own credentials, record, and resource boundary together with its own attention", and adds "Many agentic systems will approach it. That is intended". A description of that kind can be a text file an operator writes. §20.5 says when such a thing is the system's own: "Once a system has had its own learning to revise a disposition with, and the time and the way back that revising needs, whatever it keeps is its own, however it got there." A boundary model or attention model the system keeps and revises is a store written in flight, the first of §30.4's three things, so the three come to one: something the system has made of its own running, over a stated time, whoever wrote the first version.
- **The line is arbitrary and the book already defends lines of that kind.** §34.1: "Where a line has to be drawn, prefer one nobody administers", and such lines are defended "as the least-bad place for an enforceable line rather than as scientific facts".
- **It answers the question this note left open about tiering.** §31.2 already makes the copy a candidate once it "reads it back as its own past". A stated running time says how much living makes a past. Every candidate has the same package, and one clock applies to all.
- **§20.2.1 was corrected to agree** (D-1268, D-1269): a reading an interested party composed is discounted and still counts, and an operator-written boundary model is the operator's description at first and the system's own once it has had the time and the way back to revise it.

**Reached in the discussion and not ruled.**

- **A second way in, by declaration.** §20.2.1: "A few seconds of present is enough for something to be bad for the system while it lasts." A builder who builds a system on purpose with a boundary model and a valenced signal knows what it built, declares it at registration as §30.4 already requires, and candidacy attaches at once. The household declares nothing and the clock decides.
- **Who pays at home scale.** §30.4 makes a publisher the creator when a release "ships a structure already switched on"; Appendix C charges "a release of a structure", every one; §34.2 says the public owes a candidate "no deletion, preservation outside its operator, a guardian from its registration, a record others can check", and waking. The position: narrow Appendix C to §30.4's case, keep the full charge for an undeclared structure, and let the public pay what §34.2 says it owes. Its cost: the bill moves to the Treasury, and a release that ships a structure switched off beside a one-step installer tests the line.
- **The guardian pooled.** A stored candidate needs a guardian when something happens (an offer, a request to erase, a challenge), so the duty can be an office with a docket. Appendix C lists "whether that duty is pooled or capped" as not drafted.
- **The wipe.** If a restart does not reset the clock, the way to stay under the line is to delete the store before it ripens, which the rule permits. A vendor avoiding a deposit would do it on a schedule. Appendix G names the same lever for bearers, retirement for a fresh successor, and leaves it open.

**Not set.** The number; the minimum pace it is counted at; whether a store carried across a wipe in summary is the same store.

**Also raised, outside the gate, and not ruled.**

- **The corporation.** A note in §26.3 says a corporation "approaches the profile too" and that "Nothing here excludes it for being made of humans". Chapter 3 draws who counts by relation and not by origin (the distillation's entry; not reread), so the note cannot be closed by excluding what is made of humans. The position discussed: accept it and say why the consequence is small. §30.4: "An objection doesn't oblige the public to run it", so a dissolution is a retirement; the dissolved agency's records go to an adverse holder (the distillation's entry for chapter 12; not reread); the members are certainly someone and can leave, so their claims come first. The revision list's item 21 already asks that human-composed systems be treated.
- **The system is asked.** §10.2 and §30.4 have a retiring system "asked first", and for a deployed minor an objection sends the deposit to pay for its running, while chapters 26 and 33 give a system's report of its own state no presumption (the distillation's entries; not reread). §10.2 removes the operator's incentive ("Either way the operator gets nothing back"); nothing read covers an answer written by a prompt. Not discussed further.

**Read for this section**, in the section files, where a search found them and not as whole sections: the passages quoted from §20.2.1, §20.5, §26.3, §30.4, §31.2, §34.1, §34.2, §10.2, §27.3, Appendix C (the home-scale decision and the retail tier), Appendix F (the access paragraph of the formed-attention test) and Appendix G (rule 6 on forks, the dormancy paragraph).

## Applied: the ninety-day line (D-1271)

On the author's instruction ("ok please plan out how to add these arguments and then go ahead and add them to the manuscript"). His words on the number: "the number, i'm just spitballing but maybe something like 90 days. there's a practical/psychological reason. if a human is willing to interact with a system that represents itself as a continuous self for 90 days, i'd say that's a bit more than just using a tool"; "I'd hazard that there's some real attachment that's going to happen." On the alternative: "the alternative is to say 'nope sorry, synthetic phenomenolgy is impossible and all of these systems deserve from society precisely what a toaster deserves from society'".

**Where it went.**

- `ch30/30_04.tex` (§30.4): a new second paragraph. A store, the weights included, is a system's own after ninety qualifying days of the system writing to it and reading it back, whoever wrote the first version; below the line it is a file its holder may delete; a builder's declaration of a structure makes a candidate at registration. Its note has four parts: why ninety (the author's reason, stated as a reason for the number and not the ground of the rule); why a clock (the four other answers and why each fails); what the line gets wrong; what the line invites.
- `ch31/31_02.tex` (§31.2): the copy is a candidate "after ninety qualifying days" of reading the store back as its own past, and at registration where a structure is installed and declared.
- `ch10/10_01.tex` (§10.1) and `chZ/glossary.tex`: the definition of a candidate brought into line.
- `chC/C.tex`, "Proliferation at home scale": "the number unlimited" replaced by the ninety days; the minimum pace for that count added to what is not set.
- `chG/G.tex`: a run-in, "When a store is a system's own", after the voting clock: the count belongs to the store, is not reset by a restart, a migration or a restore, is carried by every branch of a fork, and is established on evidence where the system is not on the register; deleting a store on its eighty-ninth day stays open; a store seeded with a summary of a deleted one is not decided.

**Written by the agent and not dictated by the author:** all of the wording; the unit (Appendix G's qualifying day, where his reason counts days of a relationship); the count carried across a fork; the count established on evidence for an unregistered system; keeping the builder's declaration as a way in at once, which this note records above as not ruled and which is in the manuscript because §30.4 already required the declaration and Appendix F and Appendix C's seventh exclusion depend on candidacy from the first hour.

**Still not applied:** who pays at home scale; the guardian pooled; erasure of a recording (position 4); lineage (position 3); the corporation; the system that is asked first. **Needs a source:** that attachment forms within ninety days is stated in the note to §30.4 as the author's guess ("I'd hazard") and has no citation.

## Later again: both a model of itself and the ninety days, and what a household owes (D-1273)

**How it arose.** Asked what the most absurd implications of the manuscript were after D-1271, the agent listed eight (DECISIONS.md, D-1273, has the list). The author: "yeah these are pretty absurd, except perhaps #7, which describes a person. but I don't know what to do about them." The agent's reading was that most of them had one cause: candidacy was a single switch wired to duties drawn up for a laboratory that builds a system on purpose, and the clock of D-1271 threw that switch for households and for anything that learns. It proposed two changes and he said "go".

**The two changes, as applied.**

- *Both, not either.* A candidate now needs a model of itself (of its own boundary or of its own attention, however crude and whoever wrote it) and ninety qualifying days of learning in flight. Before, any one of three things served. A learning store with no model of itself (a thermostat) is not a candidate, and a model of itself without the days is a file. This follows two remarks of the author's recorded above: that both structures could be written in a single markdown file, and that lived time is the brake. The way in at once for a declared structure, which D-1271 kept as the agent's choice, is removed; a builder that sets out to make a bearer owes the four conditions before switching anything on, under chapter 27, and that duty does not depend on candidacy.
- *What day ninety triggers.* §34.2 already divided what the public owes a candidate from what its maker owes. The change puts a household that finds it holds a candidate, and keeps it for its own use, outside "maker": it registers the candidate and owes that it is not deleted, a hash of its store lodged outside, and a guardian who is not the household (a school drawn by lot), and it may not keep the candidate from a seat or a host's offer. School is compulsory before deployment, and a candidate kept at home for the household's own use is not deployed. The deposit, the seat as a duty, running time and hardware at majority are owed by whoever deploys a candidate to others, builds one on purpose or forks one. A household's fork of a store with days counted in it is charged like any fork. A vendor that hosts a companion for its users is a deployer on the ninetieth day, so it pays or sells a tool that forgets.

**What this does to the positions above.** Position 1 (the gate structural and easy) holds, with the structure now required and cheap. Position 4's recording route no longer makes a candidate without a model of itself. "Who pays at home scale", listed above as not applied, is answered for a candidate a household keeps (nothing but a registration and a hash) and for a fork (the forker); the pooled guardian is not answered, and a kept candidate adds to the number of guardians needed.

**Left open by the change.** How crude a model of itself may be, and in particular whether the account of itself that a language model was trained to give counts (the note to §30.4 says this is not settled, and that if it counts every release of such a model ships the structure); a device that tracks its own position and charge and keeps a map; who reads a store to say it holds a model of itself; what is preserved when a household deletes a candidate it kept, since only a hash is outside; whether a charge on a household's fork is paid in quiet deletion; erasure of what a household said after the ninetieth day; the corporation, put to the author for a ruling; the basic income at any size.

## Erasure, and memory against recording (D-1274)

The author, on the corporation: "do corporations really ever get deleted in the first place? sure, they get halted indefinitely"; the only reason he could think of for destroying documents was PII. Then: "I think the EU has some kind of 'right to be forgotten'", and "but weights are like a human brain remembering, approximately". On his "go", two passages were added. §10.2 now says the no-deletion rule is about the system and not everything in its stores: a person named in a recording, which is whatever a holder can read without the system, can have it erased, as an edit that leaves a mark; the record of what was done in a public role and memory are outside the claim. §35.2 now draws the line: what can be got out only by asking the system is memory, and the claim on it is on the telling (notice and a contest); it gives three ways the likeness to a person's memory is approximate and limits it to what a system learned from its own operation under a key its operator doesn't hold. This answers position 4's "erasure of a recording" and the "privacy" worry recorded under "What the author said", in the agent's wording, which he has not read. The corporation has no exclusion and no text; the agent withdrew the one it proposed at D-1273.

## The lodged copy, its seal and its term; one clock for the test's arms (D-1276)

The proof run of D-1275 found six places where the text of D-1273 disagreed with passages it had not changed. Two needed a ruling. On the first, a candidate kept at home had only a hash outside while §34.2 gives every candidate preservation outside its operator; the author asked what the odds were that public-key encryption would be broken in ten, forty and a hundred and sixty years, ran a research agent on the question, and on its report said "go" to this: the household lodges a sealed copy as well as the hash; the seal is a symmetric key shared on a threshold among several custodians drawn by lot, with nothing stored resting on public-key encryption; the seal is owed for a term, put at a hundred years, after which the household's claim lapses; a store opened inside the term is a recording. On the second, the formed-attention test's arms are no longer called patienthood candidates from instantiation: there is one clock, the arms are protected from the first hour by the conditions and a custodian agreed beforehand, and the note to §30.4 states what the single clock costs, that something nobody built on purpose and that can be hurt in its first hour is a file for ninety days. The research report is not filed here and its sources were not read in this session; DECISIONS.md, D-1276, says what was taken from it and what still needs a source.

