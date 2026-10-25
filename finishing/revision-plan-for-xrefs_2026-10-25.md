# Cross-references out of the body: a plan

Drafted 2026-10-25 from the editorial read of the same date, on the author's instruction: "Move most of the section numbers into the notes and keep in the text only the ones the sentence needs. Agreed, and maybe some of them can be cut altogether. Would you please make a plan?" Approved by the author on 2026-10-25, all five decisions as recommended ("as you suggest for all 5. godspeed"), and executed the same day: Phase 0 as D-1018, Phases 1 to 3 as D-1019. Section numbers are those of `f8407252` plus D-1017. The counts below are the plan's, taken before the pass; the pass's own counts are in D-1019.

## What the count shows

Counted on 2026-10-25 by a script over the section files: body text only (the bodies of `\note{…}` excluded), chapters 0 to 35, with references inside tables, figures and `\tags{}` set aside. The listing, one row per reference with its citing sentence, is in the session scratchpad as `xref-body.tsv`; it is disposable and Phase 0 regenerates it into the repository.

| | |
|---|---|
| References in chapter body prose | 304 |
| … to a section or chapter | 234 |
| … to an appendix | 70 |
| In the chapters' tables and figures (stay) | 79 |
| Inside notes | 49 |
| Glossary (stays) | 96 |
| Appendices' own prose and tables | 170 |

By shape, the 304:

| Shape | Count | Example |
|---|---|---|
| Parenthetical at the sentence's end | 127, of which 80 are a bare number and 47 carry words | "…a copy taken is a fork without consent (Appendix G, the membership clock's sixth rule)" |
| Parenthetical mid-sentence | 18 | "…paid for through the deployment deposit its operator posted (§9.2) and kept up from its wages" |
| "§x says", "§x's …" in running prose | 57 | "§12.3 concedes that past a released checkpoint the floor prevents nothing" |
| "chapter N's …" in running prose | 53 | "the crumple zone of chapter 7 in machine form" |
| "Appendix X …" in running prose | 49 | "Appendix G gives the rules." |

By chapter: 33 carries 34, 27 carries 33, 29 carries 28, 21 carries 20, 30 carries 19, 18 and 32 carry 17 each, 19 carries 16; every other chapter is under 12. Of the 304, 59 sit in a paragraph that already ends in a note. Six sections point at the same appendix twice (10.1 and 26.1 at C; 30.2, 33.4.6 and 34.3 at G; chapter 31 at F).

Most pointed-at targets: Appendix C (28), Appendix G (18), §32.3 (12), chapters 22, 25 and 33 (10 each), chapter 29 and §30.1 (8 each).

`xref_shapes.py --summary`, run the same day over the rendered prose, classes 89 of 437 as removable, nearly all "appended" locators. Its "inline, keep" class (345) keeps any reference with a verb, which is too generous for this pass; its 437 counts rendered "§x" strings over a wider scope than the table above. It is a first sort, not the rule.

## How they came back

D-658 (P221, 2026-10-05) cut the body chapters from 155 references to 34 under style.md §7: point only to an appendix, a table or a definition the sentence can't restate, and write the rest as prose. Three things since have put them back. The notes pass (D-906 to D-914) and the restoration (P223, D-917 to D-928) moved paragraphs down and up with their pointers. D-901 (2026-10-18) set the author's rule for a `\S\ref` used as a noun: say what it is, with the number in parentheses; that made the parenthetical the house form, and it is now the largest class. D-1000 (2026-10-25) fixed sixteen places where the author, reading as a reader, lost a referent or met a bare cross-reference where he wanted the point said; the repair was to name the thing, and the number stayed beside it. This plan keeps the naming and takes the number out of the sentence.

## The rule

A body reference has one of four fates. The test is style.md §7's: the sentence has to make sense to a reader who does not follow the reference. The fates say where the number goes when the sentence doesn't need it.

1. **Keep.** The sentence names a place the reader must go to use the book: an appendix's rules, a table, a test in Appendix F, a figure. Once per section, at the first place the reader needs it; a second pointer to the same appendix in the same section is cut. Also kept: a definition the sentence can't restate in a clause, at its first use in a Part (the two findings of §9.1 where Part VII opens on them); and the maps the book draws on purpose: chapter 4's list of the five policies with their chapters, the Part openings, the glossary's trailing pointers, figures 24.1 and 31.1, Tables 27.1 and 31.1.
2. **Prose.** The reference is a noun phrase whose content is a term: "chapter 7's crumple zone", "the cooperative facility of §16.2", "which chapter 22 says a bearer needs". Write the term and drop the number: "the crumple zone", "a cooperative facility", "which a bearer needs". A reader who has forgotten a term goes to the glossary (D-652), not to a number in the sentence. Where the sentence borrows a result and would be a bare assertion without it ("§12.3 concedes that past a released checkpoint the floor prevents nothing"), the result is restated in the clause and the number goes by fate 3 or 4.
3. **Note.** The reference carries a clause worth keeping ("as §16.5 has a cleared bearer work"), or the host paragraph already ends in a note (59 of the 304). The clause, or the bare pointer, goes to the end of that note as its last sentence, in style.md §4d's form. No new note is opened for a bare number: a note reading "(§13.6)" is a footnote to nothing.
4. **Cut.** The sentence already says the thing and the number only locates it: the 80 bare parenthetical locators, back-pointers within the same chapter, and the six repeated appendix pointers.

What the rule reverses: D-901's "with the number in parentheses" for a `\S\ref` used as a noun. The naming stays; the number goes by fate 2, 3 or 4. That is decision 1 below.

## Phases

**Phase 0, the record.** This plan approved, with the decisions ruled; a D-row; style.md §7 amended with the four fates and the once-per-section rule for appendix pointers; and a triage file, `finishing/xref-fates_<date>.tsv`, one row per body reference: section, target, shape, whether the host paragraph has a note, the citing sentence, the proposed fate, and for fate 2 the rewritten sentence. The script that wrote today's counts writes the skeleton; the fates and the rewrites are an agent's read of all 304 sentences. The author reads the fate-1 rows whole, about 90, and a random 30 of the rest, and rules; the remainder goes on the proposal, each row reversible (decision 2).

**Phase 1, cuts.** Fate 4 and the repeated appendix pointers: about 90 references. Each sentence is read in the render after the cut, because a parenthetical sometimes hides that the sentence's subject is the referenced thing, which is D-1000's class of defect. No wording changes beyond the parenthesis and its punctuation.

**Phase 2, prose.** Fate 2 across the 110 running-prose references to sections and chapters, and the 65 parentheticals that carry words, chapter by chapter, heaviest first: 33, 27, 29, 21, 30, 18, 32, 19, then the rest. The rewrite names the term and nothing else. D-902's rule holds: a cut may not remove context a reader going straight through meets there for the first time, so where a reference is the reader's first meeting with a term, the term is said in words at that place.

**Phase 3, notes.** Fate 3: the 59 with a note already hanging, and the clause-bearing references. Appended as the note's last sentence; a `\S\ref` inside a note renders as the number and is fine there.

**Phase 4, optional.** The appendices' own prose (A, B and G, about 45 references) and the 49 inside notes, under the same fates. Appendix C's offices table and exclusions and Appendix F's Tables F.1a and F.1b are apparatus and stay (decision 3).

**Verification, each phase.** `check_xrefs.py`, for no dangling reference and no bare number; the suite; a build, with the undefined and overfull counts; the HTML build's link count read as `pipeline.md` reads it, a fall equal to the number cut and the id count unchanged; the count script rerun, with its totals in the D-row; and a line printed by `render_markdown.py --check` giving body references per chapter, so the number can't regrow unnoticed as it did between D-658 and today. The line is a report, not a gate (decision 4).

## What stays as it is

Figures 24.1 and 31.1 carry a section number in every box by design; the caption says the numbers mark where each box is argued. Once the body is thinned they become the map, which is where a map belongs. Tables 27.1 and 31.1 and their "Supplied in" and "Where" columns. The glossary's trailing pointers. Appendix C's offices table and exclusions, and Appendix F's tables. Chapter 4's opening list of the five policies. The Part openings.

## Risks

- **Lost referents.** D-1000 is the record of what happens when a reference goes and the thing isn't named: "which three conditions?", "what handoff?". Every fate-2 and fate-4 row is read in the render as a reader meets it, and the term is said in words. Where a term's name alone won't carry the sentence, the row's fate is 1.
- **Regrowth.** Three October passes took the body from 34 references to 304 by today's count, which is narrower than D-658's. The report line in the verification is the only thing that would show the next pass doing it again.
- **The appendices as a crutch.** Pointing at Appendix C 28 times is also a sign that some rules the chapters need are stated only there. Phase 2 lists every rule a chapter points at and never states, as a finding for the author. This plan adds no prose.
- **The Overleaf round trip.** No renumber and no file moves, so `overleaf.py` is undisturbed and an outstanding export can still come back.

## Decisions for the author

1. D-901's rule, say what it is with the number in parentheses, is amended to: say what it is; the number goes to a note, or goes. Yes or no.
2. How much of the triage to read: the keep rows whole and a sample of the rest, as proposed, or all 304.
3. Phase 4, the appendices' prose and the notes' own references: in scope now, or after.
4. The per-chapter count printed as a report by `render_markdown.py --check`, and not wired into `check_all.sh` as a gate.
5. The target. The plan aims at about 100 body references in the chapters, from 304: appendix and table pointers once per section, about 55; definitions at first use in a Part, about 25; the maps, about 20. The exact number comes out of the triage, and this is the author's number to move.

## What this plan does not do

It adds no prose and moves no section; D-007 stands. It doesn't touch the notes' own 49 references or the appendices' prose unless decision 3 says so. It doesn't judge whether a reference points at the right section; that is `xref_pairs.py`'s job and a separate read. The counts above come from one script run on 2026-10-25 and are not reconciled with `xref_shapes.py`'s 437, which counts rendered strings over a wider scope. Nothing here has been checked against the author's own count of what a reader can carry; the target in decision 5 is the agent's proposal.
