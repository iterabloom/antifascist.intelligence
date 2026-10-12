# Blind trial, run 4: results

Two Sonnet judges (the `sonnet` model in the Agent tool, effort medium), one on the earlier version and one on today's version without the draft marks. Instructions identical to run 3 except for a reading requirement: read the whole file, every line from the first to the last, appendices included, in consecutive ranges with no gaps and no search or sampling, before scoring; list the exact line ranges read; quote one passage from the last appendix as well as one from each Part. Run on 2026-10-10. Each listed only its own `manuscript.md` as opened.

| Folder | Version | Overall | Clarity | Coherence | Economy | Line ranges reported | Subagent tokens reported | Tool uses | Duration |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `r716fc2` | Earlier, `920e6b9` (2026-10-02) | 6 | 5 | 6 | 4 | 1–3211, no gaps (file is 3,211 lines) | 290,226 | 32 | 88 s |
| `rb21df0` | Later, draft marks removed | 6 | 5 | 6 | 4 | 1–3381, no gaps (file is 3,380 lines by `grep -c`) | 303,002 | 21 | 78 s |

Both judges gave the same scores as the two Sonnet judges of run 3, who did not have the reading requirement and one of whom read only part of the later file.

Checked after unblinding: "For a soldier the setting is luck" and "Eight terms are used from the first chapter" are in the earlier file only; the two "signature attached" sentences the later judge cites are in both files.

## Report, folder r716fc2 (verbatim)

```
SCORES
overall: 6
clarity: 5
coherence: 6
economy: 4

EVIDENCE

Overall (6). The book has a real, urgent premise and unusually concrete cases. It also has a very large proposal apparatus, a hypothetical machine "bearer" that is placed late, and uneven pacing. The book sets out a bet and says what survives if it fails, which is rare and a strength.
- Preface: "What AI lowers first is not the cost of the act. It is the number of people who have to know what the act is before it happens." This is a memorable, original thesis.
- Ch. 1: the officer "spent twenty seconds on each name... zero added value as a human, apart from being a stamp of approval." A vivid opening case that anchors the argument.
- Ch. 25: "If the antecedents never hold... nothing in this part binds, and nothing before it is lost" (Part VII closing). It states its own conditionality. But the chapters on patienthood, representation, voting-age clocks and charters make it feel like several books.

Clarity (5). The prose is often sharp and plain, and it is also dense with coined terms, cross-references and legal and technical detail. A general reader has to carry many defined terms (floor, bearer, adverse quorum, discount curve, and so on).
- Preface/Terms: "Eight terms are used from the first chapter and argued later." The reader is asked to memorise vocabulary before the argument starts.
- Ch. 3.1: "Take a request to resolve a description of a person into a location; the same request comes from a targeting cell and from a parent searching for a missing child." This is a clear worked example.
- Ch. 25.1.1: "the milestone is checkable and unenforceable at once, which makes it a declared commitment." Typical of the abstract, self-referential register in later chapters.

Coherence (6). The through-line is consistent and has strong internal cross-referencing: refusal needs a room, the room needs institutions, and the institutions need an outside custodian. Part IV's machine bearer rests on stacked premises (continued learning, caregiving, formation) that the book itself flags as hypothesis. Some sections are written as if answering an earlier draft's objections.
- Part I, Ch. 1: "For a soldier the setting is luck... Everything that follows is about composing the room." This is the organising idea and it recurs.
- Ch. 21: "A bearer may be created only where four arrangements already exist." Part IV ends by conditioning its own central object on institutions that do not exist.
- Ch. 8.8: "A bearer built inside the removal pipeline would be formed by the operator it would have to refuse... This chapter draws the opposite conclusion." The book argues against its own tempting extension. This is coherent but it complicates the line.

Economy (4). There is a great deal of qualification, restatement and re-description of the same mechanisms (floor, own-case rule, discount and burden, custody) across chapters. Many sections open with a recap and close with "what this doesn't do". There is also a lot of internal cross-reference.
- Ch. 14.1: "Those institutions also prevent... What a machine bearer adds is confined to what they can't see or can't reach in time." The same bearer-versus-institution comparison recurs in several chapters (4.2, 8.8, 14.1, 14.3, 16.3).
- Ch. 17.1: "The line between the cost to the refuser and the harm of refusing is fixed by the kind of act, but saying what kind an act is still takes a description; in this setting the line is held mostly by the action threshold." Heavily hedged and self-referential.
- Ch. 3.1: "I would tilt the system toward refusing: it should take more to make the system act than to make it decline." This point reappears at length in Ch. 17, Ch. 20 and the glossary.

COVERAGE
Part I (The Record), Ch. 1: "Whoever owns the machine can always switch it off. The harder problem is everything that defeats a refusal without leaving a mark."
Part II (Five Measures), Ch. 4: "A ratio met is an artifact showing twenty minutes a case, and twenty minutes a case is what a stamp looks like at a slower tempo."
Part III (What the Measures Depend On), Ch. 9: "Exit gives a human worker leverage because leaving takes the worker's labor away. That doesn't carry over to a bearer."
Part IV (Machines That Might Refuse), Ch. 15: "something with no stake of its own has nothing to hold a line with."
Part V (The Public That Should Form Them), Ch. 22: "A market can't produce a commitment that survives its owner's change of mind, because the owner is the one who pays."
Part VI (Testing and Using the Argument), Ch. 25: "In every row, what survives is a commitment the owner can't revise or circumvent alone without cost and record."
Part VII (If They Can Be Wronged), Ch. 28: "A polity that holds diverging interests in one legislature, under one floor, is what a demos is."
Last lettered appendix (F. Three costs that decide): "Independence doesn't supply competence. The agency finding holds only for systems their evaluators can judge, and nothing here says what to do above that line."

LINE RANGES READ
Read in consecutive ranges, with no gaps: 1-150; 151-270; 271-370; 371-480; 481-590; 591-700; 701-810; 811-920; 921-1030; 1031-1140; 1141-1250; 1251-1360; 1361-1470; 1471-1580; 1581-1690; 1691-1800; 1801-1910; 1911-2020; 2021-2130; 2131-2240; 2241-2350; 2351-2460; 2461-2570; 2571-2680; 2681-2790; 2791-2900; 2901-3010; 3011-3120; 3121-3211 (the last text line is 3211); 3212 (a final Read at offset 3212 returned empty, i.e. the end of the file). One earlier attempt to read lines 1-400 in one call was refused for size and produced no content. The first range was then read in pieces.

FILES OPENED
/home/user/blindtrial/r716fc2/manuscript.md
```

## Report, folder rb21df0 (verbatim)

```
SCORES
overall: 6
clarity: 5
coherence: 6
economy: 4

EVIDENCE

Overall (6). The book has a real, original thesis and a hard-won central image, and its early chapters are the strongest. But it grows into a very large design catalogue that a general educated reader would struggle to carry. The cases are vivid and specific. The institutional and technical apparatus is far larger than the reading experience can bear.
- Preface: "What today's AI lowers first is not the cost of the act. It is the number of people who know what the act is before it happens." This is the book's best sentence-level insight.
- Ch. 33 "The Officer, Again": "None of it makes him refuse. It makes refusing survivable and makes it heard, and leaves the refusing to him." It pays off the opening image.
- Ch. 21.4: "The first four have to meet at one point of comparison: a defeasible interrupt must be weighed where the harms are weighed, and a lesson must write into that comparison to reach the next case." This is the technical register much of Parts IV to VII sits in.

Clarity (5). The narrative and case passages are clear and often vivid. The conceptual middle is coined-term dense (floor, bearer, own-case rule, formed attention, discount curve, adverse quorum, four conditions of creation). Terms are defined in a Glossary rather than where the reader needs them, and claims often depend on several earlier chapters.
- Ch. 1: "The people on his list couldn't answer him, and nothing in the pipeline asked them to." This is clear and concrete.
- Ch. 22.1: "In short: stake discounts the claim; power allocates the burden." The used-car example that follows makes it followable.
- Ch. 18.4: "Integrity is the unbounded form: the refusal holds at any cost the operator can impose, and no learner is known to do that reliably." Elsewhere in that chapter, the cost-to-the-refuser, harm-of-refusing and harm-of-acting taxonomy takes real effort to follow.

Coherence (6). There is a visible spine. Part I sets out the record. Part II sets out five measures. Part III covers what they depend on. Part IV covers machines that might refuse. Part V covers the public. Part VI covers tests. Part VII covers patienthood. Chapter 33 returns to the officer. Chapter 29 and the premise-failure table state what survives if each premise fails. The gaps are these. The book keeps deferring the load-bearing bet. It also states both "build it" and "not yet." Sections lean on forward and backward references for the reasoning itself.
- Preface: "This book is about composing that room: the arrangements that make it survivable to refuse overtly, directly, and explicitly."
- Preface: "I think such a system is worth building on purpose" against Ch. 17: "until the conditions this Part ends on exist, a bearer is built on purpose only in a research program under them." These are reconcilable but in visible tension.
- Ch. 29: "I have spent five Parts saying what the room needs, and I could be wrong about any of it." The Part VI tests are the honest accounting of the argument's open joints.

Economy (4). The prose is compressed sentence by sentence but repeats at the level of structure and idea. Whole arguments are restated across chapters. The same formulations recur. Many paragraphs carry hedges and cross-references. "What this doesn't do" sections and "if weights stay frozen" fallbacks recur chapter after chapter.
- Ch. 18.3: "A pipeline that keeps a stamp is an autonomous weapon with a signature attached." Later in the same chapter: "the pipeline never needed full autonomy, only throughput with a signature attached." The same figure appears twice in one chapter.
- Ch. 21.4: "Nor does the list show that one signal must carry all four. That no intervention can disable one part of the signal and leave the rest working isn't derived here: it is a custody requirement, and it is kept as one." This is stacked qualification.
- Ch. 2 (a contrast case): "So the refusal that opened the dispute withheld nothing from the pipeline." This shows the book's crisp mode, which it often does not sustain.

COVERAGE
- Preface: "A system that does exactly what you tell it is just running a script. What the industry is trying to build as of October 2026 is a system that does what you *mean*."
- Part I (Ch. 1): "The people on his list couldn't answer him, and nothing in the pipeline asked them to."
- Part II (Ch. 4): "Whoever owns the machine can always switch it off. The harder problem is everything that defeats a refusal without leaving a mark."
- Part III (Ch. 12): "A population of models that refuses puts them back."
- Part IV (Ch. 17): "He understood what the company was doing and decided it was wrong."
- Part V (Ch. 26): "A market can't produce a commitment that survives its owner's change of mind, because the owner is the one who pays."
- Part VI (Ch. 29): "I have spent five Parts saying what the room needs, and I could be wrong about any of it."
- Part VII (Ch. 30): "The question is whether a system can be harmed, which is harder than whether it is conscious."
- Last lettered appendix (G, test 6): "Run the adversarial tabletop exercise against the entity that holds the offices."

LINE RANGES READ
One Read call returned nothing because it was refused for size, so it is not counted. The ranges that returned content, in order:
1-250; 251-450; 451-650; 651-850; 851-1050; 1051-1250; 1251-1450; 1451-1650; 1651-1850; 1851-2050; 2051-2250; 2251-2450; 2451-2650; 2651-2800; 2801-2950; 2951-3100; 3101-3250; 3251-3381.
A further Read at offset 3382 confirmed the file has 3381 lines, so the last line of the file is line 3381. I did not use grep, search or sampling. I read every line, appendices A to G included, before scoring.

FILES OPENED
/home/user/blindtrial/rb21df0/manuscript.md (the only file opened)
```
