# Blind trial, run 1: results

Two Haiku judges (the `haiku` model in the Agent tool, effort medium), one per folder, identical instructions apart from the folder path. Run on 2026-10-10. Each was told to stay inside its folder; each listed only its own `manuscript.md` as opened. The map is in `map.md`.

| Folder | Version | Overall | Clarity | Coherence | Economy | Subagent tokens reported | Tool uses | Duration |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `r716fc2` | Earlier, `920e6b9` (2026-10-02) | 5 | 5 | 6 | 3 | 302,124 | 24 | 89 s |
| `r16e30c` | Later, manuscript as `683c828` (2026-10-10) | 4 | 4 | 6 | 2 | 316,581 | 20 | 104 s |

Checked after unblinding:
- The later judge's overall score cites two draft marks in the main text: Chapter 1's footnote 5 ("[this part might be an unnecessary reach]?") and §19.3's "% CITE" note. Neither is in the earlier file; both are in the later one.
- The earlier judge's economy examples ("A system perfectly correctable by its operator serves whoever controls the operator" at lines 160 and 1216; "The denominator can be filled…" at lines 376 and 378) are present in the earlier file as quoted. The §7.1 repetition was cut on 2026-10-10 (D-692).

Limits: one judge per version and model; no repeat on the same manuscript, so the variation between runs on an unchanged text is unknown; the reported token figure is a single total with no input/output or cache split.

## Report, folder r716fc2 (verbatim)

```
SCORES
overall: 5
clarity: 5
coherence: 6
economy: 3

EVIDENCE
Locations give the section heading and the line number in manuscript.md as the Read tool numbered it.

Overall (5): The book has real substance and a strong record. Its best material is the Part I case work and the historical passages, but its length (about 3,200 lines of long paragraphs) and its proposal chapters, which run on invented vocabulary, keep it from a general reader's reach.
- Preface, line 20: "A program that does exactly what it's told is just a script." A strong, compact opening that states the book's problem.
- Section 12.1, line 967: "What did 95.1 percent leave out, and with every other party banned, who could say so?" Historical argument carried by pointed questions.
- Section 1, line 58: "He isn't a subject operating an instrument badly. He is the part of the instrument that produces the stamp, and twenty seconds is that part's cycle time." Precise reasoning on the case.

Clarity (5): Followable with effort. The plain-English passages are clear, but many sentences run past 100 words and the terms (floor, bearer, review ratio, discount curve, own-case rule) stack up. A glossary exists at the end.
- Section 1, line 124: "Reframing and a harm made small are how pressure arrives in a pipeline, and nobody there feels a decision either." Clear.
- Section 3.1, line 247: "The first tier reads administration, not title, because deciding whose territory it is would be an administered judgment and the first tier doesn't need one." Dense but followable.
- Section 17.1, line 1729: "...and that pair can train the property as well as test it, generable without limit." Hard to parse on first reading.

Coherence (6): There is a discernible line from record to measures to machines to public institutions to testing, and each Part announces its job. Gaps remain: the book's own pivot is an unmeasured quantity, and several later conclusions lean on it.
- Preface, line 26: "The second half asks whether a machine could hold a refusal against its owner, and what it would need." Announces the book's second question.
- Section 14.2 onward, line 1419: "Regrowth depends on the same fraction, and it is unmeasured; the regrowth test is where it would be measured." The bet on continued learning rests on a quantity the text admits it cannot yet measure.
- Part VI opener, line 2334: "The argument rests on seven unsolved problems and on premises that can fail." Candid about its premises, which also limits how far the conclusions can be carried.

Economy (3): Pervasively repetitive and over-qualified. The same claims, tables and qualifying labels recur across chapters and within sections.
- Section 4.1, lines 376 and 378: "The denominator can be filled with people whose assigned role is civilian harm and whose actual role is clearance" and, two paragraphs later, "The denominator can be filled with stamps, and the ratio measures only that the time existed." One point made twice in consecutive paragraphs.
- Lines 160 and 1216 contain the same sentence: "A system perfectly correctable by its operator serves whoever controls the operator."
- The "What this doesn't do." qualifier recurs at lines 309, 397 and 1510, and similar caveat paragraphs appear in other chapters. The outcomes table is also re-run for Minab in section 8.7 (line 715) and again in section 14.3 (line 1366).

COVERAGE
Part I (line 52): "This Part gives the record: a pipeline in which nothing refused and nobody could, and a vendor's refusal that withheld nothing from it..."
Part II (line 162): "Five measures would have changed the pipeline in Part I. None asks anything of a model."
Part III (line 745): "The measures bind only if someone other than the operator holds what binds them."
Part IV (line 1208): "What a refusal would have to do. Three things separate a worthwhile refusal from what a keyword filter produces."
Part V (line 2199): "A democracy is better understood as a way of doing collective inquiry, and inquiry fails when the people who bear the consequences are outside it."
Part VI (line 2334): "The argument rests on seven unsolved problems and on premises that can fail."
Part VII (line 2568): "Everything here is conditional on findings nobody can yet make."

FILES OPENED
/home/user/blindtrial/r716fc2/manuscript.md (read in full in consecutive chunks, lines 0 to 3211; the first full-file read attempt was refused for size and was followed by chunked reads of the same file). No other file was opened or listed.
```

## Report, folder r16e30c (verbatim)

```
SCORES
overall: 4
clarity: 4
coherence: 6
economy: 2

EVIDENCE
Overall (4). The main text (Preface through chapter 33, roughly lines 1 to 2680 of manuscript.md) holds a sustained argument and some strong material. The Hernández Romero case in chapter 11 and the Maven and Gleichschaltung records are specific and well sourced. The moral core also lands in places, as in §17.2 (line 1191): "We don't ask that of people. We ask them to answer for what they do, and we deny anyone the power to rewrite another person." Against that, the text carries unfinished editorial residue and a density that makes it closer to a dossier than a book for a general reader. Examples: footnote 5 (line 80), "[this part might be an unnecessary reach]?", and §19.3 (line 1422), "% CITE: one critic of Victoria's reading, not yet in refs.bib". Both are in the main text, not appendices. I put it at 4 because these are not fixable with a light pass.

Clarity (4). Plain passages exist. The Preface (line 22) states its thesis readably: "Whether someone refused turned on what kind of person they were and on the room they were in." §22.1 (line 1725) gives a clear analogy: "A report from a mechanic you hired tells you more, because the mechanic gains nothing from the sale." Many other passages stack defined and undefined terms, such as §21.5 (line 1674): "'Its own' has two senses, kept apart from here: the authorship sense, which a refusal that tracks its reason requires, and the welfare sense, which nothing carries into." §18.4 (line 1342) also reads with effort: "A finding of wrongful refusal is an instrument for defeating a refusal, so how is it distinguished from one an operator produced to defeat a correct one?" Parts IV, V and VII depend on many coined terms ("formed attention", "adverse quorum", "the four operations", "the own-case rule"), and readers must track their cross-references.

Coherence (6). The through-line is clear: composing the room, five measures, the floor, the bearer, and conditions before conscience. Two passages state it well. §25 (line 2085): "The conscience is the goal, and the way to it runs partly through the conditions under which one could refuse its operator and survive." §4 (line 212): "A commitment that sometimes errs but can't be bought protects standing better than case-by-case judgment that can, and that is the level at which ownership is tested." The argument has real gaps. The book's central proposal is explicitly untested. Table G.1a in Appendix G (line 3364) says of formed attention: "Hypothesis. Untested; to be tried after the non-affective alternatives." Chapter 19 rests on a stated bet (line 1360): "The prediction is specific: it should find kinds of affected person that neither its formation nor an instruction named, more often than a machine told to look for them does." Chapter 17 (line 1173) defers the bearer ("Not yet... Not here"), while later chapters argue for building one under conditions. The text also keeps conditional and deferred claims alongside firm recommendations, so the conclusion is less settled than the Preface suggests.

Economy (2). Repetition and over-qualification are pervasive. The captured-operator triad is restated in §11.4.4 ("A captured operator. The statute binds on paper and raises costs."), again in §11.7 (line 692, "Under total capture it leaves only the record"), and as a table in §18.3. The own-case rule is stated in §4 (line 174, "No party decides a question in which it holds the stake") and again in the glossary (line 3116). The "stamp" image recurs from the Preface onward ("Another reviewer downstream is another stamp at the same tempo," line 70). Hedging is constant, for example §22.1 (line 1719): "That is measurable in principle, and the discount curve is best understood as tracking it." The same arguments are often run through several tables and cross-references in a row.

COVERAGE
Part I (Part I, The Record, §1 "Twenty Seconds"): "An intelligence officer, describing his role in a targeting pipeline built around machine-generated kill lists, told a reporter he spent twenty seconds on each name"
Part II (Part II, Five Measures, §4 "The Floor and the Own-Case Rule"): "A floor is a written list of acts a system won't perform for anyone, with the arrangements that stop the refusal being routed around, retrained away or restored past."
Part III (Part III, What the Measures Depend On, §12 "Withholding the Work"): "Everything Part II puts in the room, whoever owns the room can take out again: a floor the operator holds is a floor the operator can lift."
Part IV (Part IV, Machines That Might Refuse, §17): "On 16 March 1968, at My Lai, a helicopter pilot named Hugh Thompson landed between an American infantry company and the villagers it was killing"
Part V (Part V, The Public That Should Form Them, §26): "Who holds what, meaning who owns it, pays for it or runs it, decides (a) what refusing costs, (b) whether the parties meant to check an operator are independent of it, and (c) who forms a refuser's values."
Part VI (Part VI, Testing and Using the Argument, §29): "I have spent five Parts saying what the room needs, and I could be wrong about any of it."
Part VII (Part VII, If They Can Be Wronged, §30): "Part IV asked whether a machine could be one of the people in the room. This Part asks what the room would owe it if it were."

FILES OPENED
/home/user/blindtrial/r16e30c/manuscript.md (read in full, lines 0 to 3382, in chunks; the first 400-line attempt exceeded the token limit and returned an error, then I paged through the file). No other path was opened, listed, searched or run.
```
