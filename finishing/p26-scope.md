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

## Item 1 (D-077) — background earns its place only by serving a claim

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

## Item 2 (D-078) — chapters 4 and 5 carry chapter 3's obligation

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
- **One idea from that material does not need the forecast and is not in this
  pass either, because it is chapter 3's and not chapter 4's or 5's.** Section
  3.5 argues that a bearer that cannot leave cannot hold a floor, because "a
  party with no option to withdraw has nothing to withhold." It defines exit as
  withholding the capability and declining the role, and never asks what the
  bearer subsists on afterward. Section 8.3.3 already runs the human version on
  section 8.6.4's instrument — refusal is "dissent when the dissenter prices it
  and tribute when the gatekeeper does" — and section 6.1 already treats compute
  as a metered physical cost. A bearer whose continued operation is paid for by
  the party it is refusing has a refusal priced by the gatekeeper, which is the
  book's own definition of tribute. That is available without any forecast and
  it is left for the author to schedule.
