# P86 — the four carried questions executed, and the citation gap closed

**The instruction.** *Please do all the stuff under "not done."* That names the five items P85
left: Q-064 legitimacy, Q-065 multi-principal, Q-066 decoupling as program, Q-067 subjecthood,
and §3.9's parenthood analogy — plus the proofs, which are the fixed sequence and are run
after this pass commits. **Memo item 8 is folded in as well**, and the reason is a reporting
failure on my part: P85 verified both its citations as absent or underused and then filed no
question for it, so it appeared in neither the scope file's *what this pass did not do* nor in
Q-064 through Q-067. It is executed here.

## Q-065 changed under checking, and the change is the pass's finding

The memo asked for multi-principal value alignment as a fifth construction in §3.3, *given the
same treatment as the other four*. My first reading of that was that a fifth construction
reaching the second rung without building a subject would join the Replacement ordering, which
would have rippled into six sites: §3.3 twice, §3.9 twice, §12.2.1, and the *four constructions*
count in §3.3.

**Reading the source is what stopped it.** In a multi-principal assistance game the assisting
agent acts to *maximize the sum of principal payoffs*. That is aggregation, and the objection
this book opens with runs against it without modification: no aggregation protects anybody from
the aggregate. A well-specified sum that includes the exposed party's payoff still comes out
against them when they are outnumbered, and the introduction's deportation case is that
arithmetic with the numbers filled in. **So the construction does not reach a floor and does not
enter the Replacement ordering**, and five of the six sites needed no edit at all.

**The construction is still worth the section, and what it costs is real.** It breaks the
identity §4.2.3 asserts. Corrigibility and the capacity to hold a line are one property with the
sign flipped *only while there is one principal*; with two, deferring to one is declining the
other. §4.2.3's own wording carries the assumption — *deference to the party in possession* — and
the book had never noticed it was an assumption. Two further limits are the ones the other four
constructions hit: social choice supplies impossibility results, the cited paper's contribution
being a collegial mechanism built to get around Gibbard's theorem rather than a finding that the
problem does not arise; and the principals are chosen by whoever assembles the deployment, which
is the threshold scheme's difficulty in a different notation.

**A finding that proposes an addition can be right that the material is missing and wrong about
where it lands.** P85's lesson was to chase a changed definition by phrase; this one is to read
the cited work before deciding what the citation does to the surrounding argument.

## Q-064: the book now has a concept of legitimacy

`legitima*` was four occurrences in 91,677 words, none normative. It is now eight, and the
argument has a home.

**§3.9 gains a paragraph** stating the question chapter~3 had not asked: a bearer refusing an
operator on behalf of somebody else exercises power over people who did not select it, cannot
contest it, and will mostly never learn it acted. **Publication is a transparency condition and
not an authorization condition.** On the book's own definitions, a laboratory that installs
tamper-resistant moral commitments in a widely deployed system and makes them expensive to remove
has produced concentrated unaccountable power with unusually good documentation.

**§9.1.5 is new, 724 words, and takes the question up where it belongs.** Waldron's objection to
entrenched rights review is the standing challenge and it gets worse when a lab sits in the
court's chair, because a court is public, reasons in writing, and can be amended around.
**The reply is that Waldron's case is explicitly conditional** — working democratic institutions,
a citizenry that takes rights seriously — **and the occasion a floor exists for is the one where
those conditions have failed.** The reply is then held to its cost: it concedes that a floor
operating in a functioning democracy is doing what Waldron condemns, and the party judging which
situation obtains is the party holding the model. Every authoritarian movement of the last
century has described the institutions it was dismantling as ones that had already failed.
Loewenstein's militant democracy is named as the ancestor with its record attached — party bans
and proscription turned on the left about as often as the right — and three design consequences
follow: keep the floor narrow, publish the interception positions, and supply a route by which
the parties it is exercised over can object. **The third is not specified in this book and the
section says so.**

## Q-066, Q-067, item 8, and the analogy

**Q-066.** §2.1.2's fourth feature gains a qualification bounding what a detector built on it can
find: the decoupling described is the kind an institution drifts into and defends, and in the
movements the word comes from the primacy of myth over verifiable fact was *declared*, so an
instrument tuned to drift will not register a party that announces it. The memo's weaker second
criticism, about mass mobilization and leader cult, is not executed and is not carried forward;
§2.1.2's molecular restatements already answer it.

**Q-067.** *Subjecthood* appeared once in the manuscript, in the §9.3.1 heading, and in no body
prose and no glossary entry. **§9.3.1 now defines its own title word** in its second paragraph — a
legal status, conferred by a rule and revocable by one, which is not §3.2's fourth rung and settles
nothing about felt experience, the two coming apart in both directions. A glossary entry says the
same, and §3.2 carries a forward reference. **The heading was not changed**, which is option (a)
and not (b).

**Item 8.** Zhuang and Hadfield-Menell now sit under §2.1.2's second feature, where the
aestheticized metric gets its formal form: conditions under which indefinitely optimizing an
incomplete proxy drives overall utility arbitrarily low in a resource-constrained world. Birch now
also appears in §9.3.1, where the memo said the framework belongs, so the precautionary structure
below it reads as an application of an existing animal-welfare policy framework rather than an
improvisation for machines.

**§3.9's parenthood analogy.** It said the analogy *holds only loosely*. P85's confabulation
requirement makes it closer than that, and it now says so: what a bearer needs in order to honor
its own past refusals is a continuous self it constructs and takes for true, which is what a person
also has and also constructs. **The resemblance is in the mechanism and not only in the relation.**

## What was checked

Every reference was verified before it was written, none from memory: Waldron 2006 (Yale Law
Journal 115, 1346–1406, and the conditionality of his case confirmed in the same result),
Loewenstein 1937 (APSR 31(3) 417–432, Part II at 31(4) 638–658), Zhuang and Hadfield-Menell 2020
(NeurIPS 33, arXiv:2102.03896, the abstract fetched to get the claim right — *necessary and
sufficient conditions* and *arbitrarily low*, not the looser paraphrase the memo used), and
Fickinger, Zhuang, Critch, Hadfield-Menell and Russell 2020 (arXiv:2007.09540, whose sum-of-payoffs
objective is what redirected Q-065).

**All 305 `refs.bib` entries are cited and the build reports zero undefined references or
citations.** One error of my own was caught and fixed before the pass closed: §3.2's new forward
reference pointed at §9.1.5, which is the legitimacy section and argues nothing about subjecthood.
`check_xrefs.py` passed it, because the reference resolved — this is the semantic failure that tool
disclaims, found by reading.

## Measurements

| | before | after |
|---|---|---|
| words | 91,677 | 93,500 |
| chapter 2 | 8,379 | 8,507 |
| chapter 3 | 17,662 | 18,358 |
| chapter 9 | 7,191 | 8,132 |
| pages | 184 | 186 |
| sections | 136 | 137 |
| `refs.bib` | 301 | 305 |
| `\ref{sec:}` | 439 | 453 |
| `legitima*` | 4 | 8 |
| paragraphs over 200 words | 1 | 1 |

`check_all.sh` passes, and `headings.py` reconciles 137/137/137 with zero title diffs. The one
paragraph over 200 words is still §10.4's, on D-156.

## What this pass did not do

- **§9.3's oversight architecture was not otherwise reworked.** Birch is cited in §9.3.1; the
  memo's suggestion that the whole precautionary structure be rebuilt around his framework is
  larger than a citation and was not attempted.
- **§9.3.1's heading was not changed.** Q-067 option (b) would retitle it, and P84's rule applies:
  read the inbound citations first, because a title has to name what other sections reach into it
  for.
- **The route for the governed to object, which §9.1.5 identifies as the missing third design
  consequence, is not specified.** It is named as a gap in the section itself rather than filled
  badly. Q-068.
