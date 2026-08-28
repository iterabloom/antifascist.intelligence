# P26 scope — the delta rule, and chapter 3's obligation

Source: `reviews/author-discussion_2026-08-28.txt`, a recorded discussion between
the author and a language model that had been given the finished 194-page PDF and
nothing else. Four rulings came out of it, D-077 to D-080. This file says what
each one covers, what was checked against the manuscript before the rulings were
put, and what did not survive checking.

Section numbers are post-D-043 and post-D-067 and need no translation.

## What was checked before the rulings were put

The model's claims about the book were checked against the text, because a
reading made from the PDF alone is evidence about the book and not about the
record behind it.

**Accurate.** The targets-per-hour indicator is section 5.1.4's run-in head in
those words. The twenty-second human review is section 6.4.1, quoted from the
officer. "Standing consortia work on a longer clock and are the weakest of the
three" is section 5.5.2's own sentence. Chapter 7's label, reward and discourse
sequence is its actual structure. Chapter 3's argument does concede that refusal
does not entail suffering as a matter of what the words mean, which is what the
model's steelman reconstructed.

**Did not survive checking, and is not carried into any item below.** The model
described chapter 6 as opening on a "four horsemen" frame and named a
"democratizing harm" section in it. Chapter 6 opens on bias and fairness; the
taxonomy at section 6.4.1 has six forms, not four; `democratiz*` returns zero
hits across chapter 6. The model twice reported its own lookup failing. Its
chapter 6 assessment is therefore not a basis for work, and chapter 6 is not in
this pass.

**Correct, and already the book's position.** The model advised tightening the
inference from persistent refusal to moral patiency. Section 3.2 does not claim
entailment — it concedes the logical point on the page and argues that the
alternative cannot be engineered or verified — and D-039 and D-040 argued the
negative case at length before P20 reversed the conclusion. What the reading
does establish is that a reader meets section 3.2's conclusion in its first four
words and the concession several paragraphs later. That is an ordering question
for a later pass and is recorded here rather than actioned.

---

## Item 1 (D-077) — background earns its place only by serving a claim — done

The rule is `style.md` section 2a, written in this pass. What follows is its
application, scoped to chapters 4 and 5 and the section 2.1 cluster. **The rest
of the book is not swept.** That is a limit of this pass and not a finding that
the rest is clean.

### Chapter 4 — 13 sections, 6,788 words

The chapter is not uniformly a survey. Eight of thirteen sections already carry
their weight, and the untouched 2023 material is concentrated in section 4.2 and
in the section openers.

| § | words | fate | why |
|---|---|---|---|
| 4 | 169 | revise | Describes the chapter as a survey of what a system perceives and learns from. Names no obligation from chapter 3. Item 2 rewrites it |
| 4.1 | 203 | cut to a seam | Runs through SOAR and ACT-R, which section 4.1.1 then does properly, and closes on a generic healthcare and judicial example with no claim attached |
| 4.1.1 | 557 | keep the box, cut the tail | The `esbox` adjudicates ACT-R against Society of Mind against predictive processing and states the engineering consequence. The four paragraphs after it — neural networks, ontologies, episodic and semantic memory — are definitions serving nothing |
| 4.1.2 | 2,453 | keep | The chapter's best section and the model for the rest. Its own second paragraph states D-077 before D-077 existed: "What follows are the findings that change a design decision, and in each case the decision is stated" |
| 4.1.3 | 749 | keep | Two properties of transferred judgment, each with a design consequence, and the blind-spot argument arriving a third time |
| 4.2 | 56 | rewrite as the seam | Currently a list of the four paradigms below it |
| 4.2.1 | 894 | compress | Survey with one strong close: the explore/exploit balance as "where a system decides whose interests bear the cost of its learning." Two title-case run-in heads violate `style.md` section 8 as well |
| 4.2.2 | 261 | fold into 4.2.1 | Defines IRL and CIRL, gives an autonomous-vehicle example and a domestic-robot example, and makes no claim. The CIRL point the book actually uses is made at section 5.6.3 |
| 4.2.3 | 537 | cut to its last paragraph | The specimen for the rule. Definition, then "can teach," "could learn," then a bulleted limits list. The last paragraph is real and links chapter 3: structure recovered from unlabeled text is the structure of the text, and no unsupervised method changes what an aggregate is |
| 4.2.4 | 400 | compress | Keep the self-correcting passage — "That is a hope and I should mark it as one" — and its link to section 9.1.6. The rest is application sketches |
| 4.3 | 41 | fold | Three sentences of announcement |
| 4.3.1 | 284 | keep | Argued, and load-bearing for item 2 |
| 4.3.2 | 184 | keep | Three cautions, and it already names chapter 3 |

Estimated removal: 2,000–2,400 words, against a chapter of 6,788.

### Chapter 5 — 29 sections, 12,711 words

Chapter 5 is in materially better shape than chapter 4 and the D-077 exposure is
four passages rather than a section cluster. Every section not listed is a keep.

| § | words | fate | why |
|---|---|---|---|
| 5.1 | 405 | cut | Restates section 5.1.1's rules-to-principles progression and section 5.1's own Dweck and Warneken material, ahead of the sections that make the argument |
| 5.1.1 | 1,346 | cut the Growth Mindset list | The Kohlberg box and the self-driving-car passage are among the book's best. The five-item list of "design choices" that follows is generic capability description — an AI chatbot that "develops more inclusive responses" |
| 5.6.3 | 1,014 | cut two lists | The safeguards list and the deployed-systems list are catalogue. The argued half — CIRL's openness, the grid example, constrained policy optimization, and the override paragraph — stays |
| 5.7.1 | 1,174 | compress the framework list | Four developmental frameworks, one paragraph each. Constructivism and theory of mind earn their place through Hanabi and Quandary; social learning duplicates section 5.1.2's Bandura; care ethics belongs here for its origin, which section 5.1.1's box already supplies |

Estimated removal: 1,400–1,800 words, against a chapter of 12,711.

### The section 2.1 cluster — 4 sections, 1,961 words

| § | words | fate | why |
|---|---|---|---|
| 2.1 | 473 | merge with 2.1.1 | Runs through six ethical theories, one paragraph each. Its last two paragraphs — the hybrid approach, and chapter 3 giving it a shape — are the section's only claim and are worth keeping |
| 2.1.1 | 576 | merge with 2.1 | The **same six theories again**, as a numbered list, each with an example and a "challenge." The two sections are near-duplicates of one another |
| 2.1.2 | 335 | compress | The demographic-parity and equality-of-opportunity contrast is concrete and used. The four-item obstacle list is not |
| 2.1.3 | 577 | compress hard | Three problems, then six strategies, then three application paragraphs. One passage is argued and is the book's thesis in miniature: the UDHR vote count, and "It is evidence of who finds the floor inconvenient." That survives; the lists do not |

Section 2.1.4 is untouched by this item. It is 2,355 words and it is argued
throughout.

---

## Item 2 (D-078) — chapters 4 and 5 carry chapter 3's obligation — done

### What "carry it" means

Section 3.7: "once the floor is a commitment rather than a constraint, whether it
holds is a question about disposition, and disposition is what those chapters are
about." So the question the two chapters have to be answering, and to be seen to
be answering, is **what forms a disposition that holds under pressure**.

The chapters answer it in twelve places and say so in five. The work is mostly
naming what is already there, not manufacturing it.

| where | what it already argues | links ch. 3 today |
|---|---|---|
| 4.1.2, "Control without a controller" | A goal representation with standing to bias competing processes — which is what a floor would be implemented as under section 3.1's second branch, stated as a claim about what not to build | no |
| 4.1.2, "Attention decides what is seen" | The blind spot is invisible from inside | yes, → 3.4 |
| 4.1.2, "Memory is rebuilt" | No witness has an honest memory in the strong sense | yes, → 3.4 |
| 4.2.3, close | Aggregate moral judgment cannot yield a floor | yes, → 3 |
| 4.2.4 | The detector assumption is doing more work than the evidence supports | → 9.1.6 only |
| 4.3.1 | "A disposition acquired by exploration is not written down anywhere, and what is not written down cannot be edited by whoever acquires the system" — a formation argument for tamper-resistance, which is section 3.1's first branch answered from the other side | no |
| 4.3.2 | "How much room a system gets to explore is the same question chapter 3 asks about how much room it gets to refuse" | yes, → 3 |
| 5.1.1, Growth Mindset | A system that treats its moral errors as data rather than verdicts. **This is where the author's own question belongs** — whether the floor has to hold always, or whether what is wanted is a bearer that can recognize a failure as one — and it is currently unconnected to chapter 3 | no |
| 5.1.3 | The mentor is a control channel; whoever teaches a system should be as auditable as the system taught. Section 3.3's custody problem arriving at the point of formation | no |
| 5.2.4 | A fluent reconstruction after the fact is indistinguishable from the real thing at the point of use | → 2.4.1 only |
| 5.6 opener | "A moral sense that only activates when it is watched is not much of a moral sense." The floor question in different words | no |
| 5.6.2 | A system running on nothing but its own drives has no outside check on where those drives point | no |
| 5.6.3 | The override paragraph, one of chapter 3's own three arrivals | yes, → 3 and 3.3 |

### The count that made the case

Chapters 4 and 5 are 42 sections and 19,499 words, and make **5 references into
chapter 3 out of 100 outbound cross-references** — two of them bare chapter
pointers. Chapter 2, which is not asked to carry the obligation, makes 10.
Chapter 9's section 9.1.7 alone makes 4.

### What the pass does

1. Rewrite the chapter 4 and chapter 5 openers to state the obligation, in place
   of the two current openers that describe a survey.
2. At each of the eight rows above marked "no" or with a partial link, name the
   connection in the section's own prose. A cross-reference alone does not
   satisfy this — the sentence has to say what the section contributes to whether
   a commitment holds.
3. Rewrite section 4.2's four sections around the claims that survive item 1,
   and give section 4.2 an opener that is a seam rather than a list.
4. Section 5.1.1's growth-mindset material takes the fallibility question
   explicitly: a bearer that can fail and recognize the failure, against a floor
   that is claimed never to break. This is new argument and D-078's lift covers
   it.

**Not in this item.** No section of chapter 5 outside the four in item 1 is
rewritten for its own sake. The obligation is discharged by naming, not by
redrafting sections that already work.

---

## Item 3 (D-079) — "bearer" — done in this pass

Three fixes, all applied:

- **Section 3.1** defines the term where it first appears, and says the
  definition is provisional and where it grows.
- **Section 3.2** marks the change of content at the point the moral weight is
  added, instead of letting the word accumulate it quietly.
- **The glossary** gains a `Bearer` entry, between `Authoritarian misuse` and
  `BERT`, tracing the term through sections 3.1, 3.2, 3.5 and 3.6.

Sections 3.1 and 3.2 are `drafted`, so no acceptance disclosure applies. The
glossary is `accepted` and its row in `ledger.tsv` discloses the addition.

**Not done.** The theological overtone the author raised — bearer as a liturgical
word, alongside its cryptographic and philosophical senses — is left alone. He
raised it, weighed it, and did not settle it, and no fix follows from an
unsettled question.

---

## Item 4 (D-080) — fascism, and one paragraph — done in this pass

Section 2.1.4 already holds the ruled position and needs no correction. It takes
fascism as a structure rather than a costume, gives four features "visible from
outside the institution displaying it," and rules that molecular fascism is "the
thing itself at the size where it is actually lived, and not an early warning of
a regime that has yet to assemble."

What it does not say is that ubiquity is the **expected finding**. It currently
treats "a tool reporting the four features will have something to report nearly
everywhere" as a hazard for the detector to manage. Under D-080 that sentence
describes the predicted result of a correct instrument, and the question a
detector is asked stops being *is this fascism* and becomes *how far here, and
is it rising* — which is section 8.6.4's slope, and connects two arguments the
book currently makes in separate places.

**One paragraph in section 2.1.4, approved by the author and written.** It sits
immediately before "One consequence travels with the reader through everything
that follows," so that the existing paragraph's dual-use hazard — a tool whose
output is an accusation, handed to whoever holds it — now follows from a stated
expectation instead of arriving as an awkwardness. It adds the section's first
reference to 8.6.4. Nothing else in the section changed, and the section is
author-accepted, so `ledger.tsv` discloses it per-row. As written:

> That a detector of these four features would find something nearly everywhere
> is the expected result and not a defect of the instrument. The tendency is
> permanent; what varies is how far it has got in a particular place, and
> whether it is getting further. Which is why the question worth asking of an
> institution is not whether the signature is present but how much of it is, and
> in which direction it has moved since anyone last looked — section 8.6.4's
> slope rather than its level, applied to the definition rather than to the
> dissent channel alone.

---

## Found on the way

**Section 5.4.3 pointed at itself.** Its second paragraph read "Section 5.4.3
covers the mesosystem and exosystem forces — regulation, corporate culture,
cross-disciplinary contact — that determine whether an AI system actually gets
built this way." Section 5.4.2, "The Rings Outside the Lab," is what covers
those; it carries the cross-training, the internal culture, the market-financing
argument and the GDPR box. Corrected to 5.4.2 in this pass. This is D-050's
class — a reference that resolves and points at the wrong thing — and
`check_xrefs.py` cannot catch it by design. `xref_content.py` cannot either: a
self-reference shares every proper noun with its target.

**`xref_content.py` still scans nothing.** D-067 recorded that the tool was never
ported to `.tex`. D-070 ported it. The self-reference above was found by reading,
not by the tool, and no claim is made here about what the tool would have found.

## What this pass does not touch

- Chapter 6, for the reason in the checking section above.
- The wage, personhood, copying and Sybil material from the last third of the
  transcript. Section 3.5 makes a discipline of requiring no forecast — "I am not
  going to abandon that discipline in the one chapter where a forecast would be
  most flattering to the argument" — and a subsistence-wage regime for an AI
  requires the forecast. Nothing on copying, forking or duplicated identity
  exists anywhere in the 162 sections, and none is added here.
- **One idea I proposed from that material did not survive checking, and is
  recorded here rather than dropped.** I put it to the author that section 3.5
  argues a bearer that cannot leave cannot hold a floor, never asks what the
  bearer subsists on afterward, and that a bearer whose compute is paid for by
  the party it refuses therefore has a refusal "priced by the gatekeeper," which
  is section 8.6.4's definition of tribute. Two things are wrong with it.

  The quoted phrase is not section 8.6.4's argument. That section argues for
  measuring the **slope** — whether the cost of registering dissent is rising
  year over year while the underlying risk stays flat — because a level can be
  presented and a trend cannot be curated after the fact. The dissent/tribute
  sentence is the last line of its second caution about how to build the
  measuring instrument: an audit has to be refusable, and "the same hundred words
  of written justification are dissent when the dissenter prices them and tribute
  when the gatekeeper does." It is a point about audit design, and it is the most
  quotable sentence in the section, which is how it came to be used as the
  section's thesis.

  And the substance is already in the book, in plainer words, in the section
  whose title is the claim. Section 3.3: "A system that can be reliably switched
  off by whoever holds it is, for exactly that reason, a system that cannot hold
  anything against whoever holds it." It goes further than my version — shutdown
  resistance and the capacity to refuse an owner are one property with the sign
  flipped; all three of section 3.1's branches fail into custody for that reason;
  and the tension is left unresolved on the ground that a graduated scheme would
  be an assurance of exactly the kind section 8.6.4 says is worthless in advance.
  Whether the operator's lever is a power button or an unpaid invoice does not
  change that argument.

  What is left after checking is thin and is not scheduled: section 3.3 sets its
  dial over the **acts** the floor covers, and does not take up shutdown for a
  pretext unrelated to a refusal that has already happened. Sections 3.2 and 3.3
  partly cover it — a bearer with a stake in its own continuation guards its
  persistence, and "the operators who wipe the bearer that called the compound a
  school now have to get past the bearer to do it." No item follows from it.

---

## Items 1 and 2 as executed, 2026-08-28

**The cut estimate was wrong in a way worth recording.** Item 1 projected
2,000–2,400 words out of chapter 4 and 1,400–1,800 out of chapter 5. What
happened instead was substitution: the survey passages went, and in most of the
sections a real claim was available to write in their place, so the chapters are
argued rather than shorter. Chapter 4 went 6,788 to 6,667, chapter 5 12,711 to
12,640, the section 2.1 cluster 1,961 to 1,739. The book went 92,710 to 92,632,
and 192 pages from 195.

That is the honest result and it is not the one the estimate implied. A reader
comparing word counts would conclude almost nothing happened in chapter 4. What
happened is that section 4.2, four sections and 2,148 words of definitions and
speculative applications, is now four sections and roughly the same length in
which every one of the four methods is taken twice — for what it does, and for
whether it could produce a commitment that survives its own teacher.

**The obligation, measured the way D-078 measured the problem.** Chapters 4 and
5 made 5 references into chapter 3 out of 100 outbound. They now make **33 out of
162**. The count is not the point and is reported because it is the number the
ruling was made on; what matters is that the twelve places where those chapters
were already making chapter 3's argument now say so, including the eight that
did not.

**What was written rather than cut, section by section.** Chapter 4's opener and
section 4.1's now state the obligation instead of describing a survey. Section
4.2's opener says what the four methods have in common and why none of them
builds a floor. Section 4.2.2 argues that CIRL is the most corrigible design in
the chapter and therefore, on section 3.3's identity, the least able to hold a
line — the sharpest new claim in the pass. Section 4.2.3 argues that supervised
learning learns an aggregate and chapter 3 has already said what an aggregate
cannot deliver, using the Moral Machine cross-cultural finding as the concrete
case. Section 4.1.1 ends on what the predictive-loop picture implies for a
commitment: no component to excise, and none to inspect either. Section 4.1.2's
"control without a controller" now says that a goal representation with standing
to bias competing processes is the mechanism the floor would have to be.
Section 4.3.1 says why a disposition acquired by exploring is the one thing in
these chapters that answers section 3.1's first branch, and marks that it is not
proof against retraining.

In chapter 5: the opener and section 5.1's, rewritten for the obligation.
Section 5.1.1's growth-mindset half now carries **the author's own question** —
whether a floor has to hold always, or whether what is wanted is a bearer that
can recognize a failure as one. The answer written there is the second: a floor
holds, in the sense chapter 3 can deliver, when the bearer can be shown to have
violated it in terms it accepts, so that the violation registers and changes
what happens next. Section 5.1.3 says the mentor is section 3.1's custody
problem arriving at the point of formation. Section 5.6's opener says the
watched-only morality problem is chapter 3's problem in a domestic register.
Section 5.6.2 says the intrinsic/extrinsic pairing stops being a balance and
becomes section 3.3's contradiction. Section 5.6.3's two catalogue lists are
replaced by the one observation specific to autonomy: every safeguard on the
list is external, external mechanisms find out what a system did after it did
it, and declining is available only to something inside.

In chapter 2: sections 2.1 and 2.1.1 no longer run the same six theories twice.
Section 2.1 is a short opener that flags deontology as the awkward case;
section 2.1.1 keeps the six and ends on the pluralism the book is actually
recommending, which is not the blend-and-hope version. Section 2.1.2 drops its
obstacle list for the point that the translation is where the ethics now lives.
Section 2.1.3 keeps the UDHR argument and drops both lists.

**No section was deleted and nothing was renumbered.** The triage had proposed
folding section 4.2.2 into 4.2.1 and merging 2.1 into 2.1.1. Both would have
cascaded — 4.2.2 has six inbound references — and in both cases a real argument
was available that made the section earn its place instead. That is a change
from the plan and it is a better outcome than the plan.

**Three defects this pass caused.** Cutting section 5.6.3's deployed-systems
list orphaned the Full Fact citation, whose claims row C0349 is retired with the
reason. It also falsified section 8.6.4, which said the Partnership on AI was
"cited already in section 5.6.3"; it now points at section 8.4.2, which takes
the body apart properly. Both are the D-050 class and both were caused by this
pass, which is why they are named here rather than in a findings list.

**The third was missed when this was written and is recorded on 2026-08-28**, on
a count run for D-081. Rewriting section 5.1's opener also cut the sentence
citing `warneken2006altruistic` — "young children display helping, fairness, and
reciprocity through interaction and observation well before they can put any of
it into words." The rewritten section 5.1 is signposting only, and section
5.1.2, which took over the interaction argument, makes an observational-learning
claim citing Bandura instead. So `refs.bib` now defines two entries the book
does not cite, `fullfact2023ai` and `warneken2006altruistic`, and biblatex
prints neither. **No citation was moved to a sentence that does not support it,
which is the failure worth avoiding here**; the finding is that this pass
reported one orphan when it had made two, and the second is a claim the book no
longer makes rather than a claim left uncited.

**Prose sweep.** Chapters 4 and 5 checked against `style.md` section 7's three
tics. Four aphorisms in my own new prose were removed after being written,
including one in a run-in head. Chapter 5's title-case run-in heads — "Growth
Mindset", "Medical Diagnosis", "The Hard Case" — are sentence-shaped and carry a
claim now, on section 4.1.2's model. "Foster" appears zero times in either
chapter.
