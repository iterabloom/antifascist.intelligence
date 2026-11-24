# Design note: the candidate gate, two routes by memory, and a clock on the recording route

**Status: not applied, and nothing in it is ruled.** Written on the author's word of 2026-11-24 ("ok write it up as a design note please") and recorded in DECISIONS.md as D-1266. It records positions reached in one discussion, with the author's remarks quoted where they moved it. Section numbers are printed numbers, as in the proof of 2026-11-24.

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
