# P217 — the rest of the `argument-changes` set, after auditing the objections to it

P216 applied the four self-contradictions from `~/book-scratch/argument-changes`
and reported objections to most of the rest. The author's instruction was to
re-check each of those objections, and to implement every item where the
objection did not hold.

**Nine objections were audited. Three were wrong, two were overstated, four
stood.** None of the four that stood was a reason to leave an item unimplemented;
three of them were reasons to compose rather than transcribe, and one — the bar
on authoring a bibliography entry — is a repository rule, so the item it blocks
goes to the author.

## The audit

| Objection reported at P216 | Verdict | What followed |
|---|---|---|
| Decision 10's replacement of *Keep the floor narrow* orphans §9.1.1's next paragraph, whose "with how much the floor covers, which the paragraph above prices" would have nothing above it pricing coverage | **Wrong** | The set's own file 03 instructs *State the costs*, naming coverage explicitly. The objection misread the instruction's scope. Implemented, with a sentence pricing coverage, so the back-reference resolves |
| Taking Arts. 3–21 entire carries nineteen articles of unscoped drafting | **Wrong** | File 03 says the worked floor "becomes four worked instances of a stated set rather than a four-item invention." A reference set, not nineteen prohibitions. Implemented at the three passage targets and in §9.1.1 |
| The tempo demotion and the accord repair collide in the *Four structural features* glossary entry | **Wrong** | On re-reading, "acceleration is what opens the gap the other three protect" is a mechanism claim and survives decision 11 untouched. The collision was a composition task, which the set's index asks for in terms. Both applied to one entry |
| The hours-of-operation clock discards the property §9.1.2's argument turns on | **Overstated** | The four candidates §9.1.2 rules out are all free for a guardian to move; hours are movable only by forgoing the asset's use, which is a difference in kind. But idling is an unnamed lever and "the argument survives intact" overclaims. Implemented, with **three** residual levers named in the text where the set named two |
| Arts. 3–21 leave §3.6's rate constraint with no parent in the book's own normative reference | **Overstated** | §3.6 already discloses that the rate constraint has no UDHR parent. A pre-existing and stated limit, not one the decision introduces. Implemented; the disclosure stood — and is **superseded by the addendum below**, which found the parent the search had missed |
| The §3.3 clause swap may hollow out the step it saves | **Stood** | Applied at P216 with the cost recorded in D-320 and `p216-scope.md`. Nothing here revisits it |
| 24 contrastive negations in 3,584 words of supplied prose break decision 14 | **Stood** | Composed in plainer register throughout. Measured on the diff: **41 *rather than* added against 45 removed, and 2 *, not* against 4 — a net reduction of six** |
| Three of the nine files end in un-deleted prior-round text, and `02_welfare_and_consent.md` gives a glossary instruction opposite to the revised one above it | **Stood** | Resolved for the revised text in every case. No *Developmental age* entry was added, which two files say and one stale tail contradicts |
| The two covenant entries the rights foundation needs cannot be authored here | **Stood** | `PLAN.md` standing rule 1 and D-009 both bar the agent from authoring a reference entry, and neither has been superseded. The covenants are named in §9.1.1 without a citation, which is what the book already does for China's 2023 rules. **Superseded by the addendum below**: the author lifted the bar and the entries are in |

## What was implemented

**All 71 remaining active targets.** Of the set's 94, fifteen are withdrawn, four
are retain-only, and four were done at P216; the rest are applied. Thirty-eight
section files changed.

**The largest pieces.** §3.3's four signal properties now carry the Foreword and
chapter~2's thesis, in place of the route claim, with the induction kept out of
the space the repair left. The floor's protected interests are grounded in the
Declaration's civil and political articles, taken entire, in §2.1, §3 and the
glossary. §9.1.1's design instruction becomes *enumerate the floor and state it
over acts*, with the affirmative case for taking a set somebody else drew up and
the coverage cost both stated. §9.1.2's clock is amended from elapsed civil time
to elapsed hours of operation per registered party, and the standing decoupling
is stated in the same subsection, where making adulthood inheritable becomes
cheap. §10.5's dividend is narrowed to the electoral meaning and renamed, with
courts, rights and public reasoning held outside the term in four places.
Chapter~11 gains three entries: the operating-record study, the embodied-concern
comparison, and the pipeline-transfer study, with the engineered-persona attack
folded into the existing provenance entry.

**§2.1 is retitled** *Six Theories and the Floor*, per finding 3, which is the
one thing that finding asks for. The title is synced in `ORDER.tsv`,
`outline.tsv`, `ledger.tsv` and the regenerated contents.

**Two glossary entries are new**: *Legal adulthood* and *Formation provenance*.
*Developmental age* was not added; it is what the withdrawn weight-geometry
clock would have defined.

## Two things the suite caught, and both were mine

**`names_guard.py` hard-failed on finding 30a.** The supplied replacement reads
"a face at the centre, and everyone else scored against it," and *scored* is one
of the persona-device attribution verbs the guard tests for. It sat within range
of a cited researcher's name in the same paragraph, so the guard read the
sentence as crediting a real person with scoring something in this project. The
wording is now "everyone else at a measured distance from it," which is the
book's own phrasing for the same point two paragraphs later. **The guard was
right and the supplied prose was the problem.**

**I added two cross-references and had to remove them.** The new glossary
entries pointed at §9.1.2 with `\ref`, which decision 15 forbids in terms. Both
are restated instead. The count is back to 75 against 88 labels, where it was.

## Measured

**At the close of the pass proper** — the addendum below moves both — **73,908 → 77,394 words**, +3,486, and **154 → 160 pages.** **88 sections**,
unchanged — the retitle moved no number. **75 cross-references against 88
labels**, unchanged. **226 bibliography entries, all cited, 0 human-checked**,
unchanged: no source was added, because none could be. **Zero undefined
references and citations.** Suite green at eight checks.

`antithesis.py` reports 474 instances at 6.12 per 1,000 words on the current
tree. The pass's own contribution is negative: six fewer contrastive negations
than it removed.

## Not done, and not checked

**Finding 2c's overlap was composed, not resolved.** The set flags 2c as unruled
and notes 2a imported half its content. The manuscript already stated the point
at §2:78, 2b adds the construction claim there, and 2c rewrites the same
sentence. One statement of each half survives; whether the author wants the
paragraph shaped that way has not been put to them.

**§4.1's next paragraph was left alone.** The set asks whether it should be
trimmed the way §2:64 was, now that 27a duplicates it, and does not rule. 27a
was composed to avoid the duplication instead, so nothing was cut.

**The glossary was not read end to end** against the revised body. Nine entries
were edited and two added; whether any of the remaining sixteen now reads
against a changed section was not checked.

**`QUESTIONS.md` was not read**, and has gone twenty-seven passes unchecked.

**The set's own defects stand in `~/book-scratch/argument-changes`.** Nothing
here edits those files: the withdrawal count still says sixteen where its own
file 09 lists fourteen, 38c is still filed as withdrawn in the index and adopted
in the table, three files still end in prior-round text, and all nine are still
dated a day after their mtimes.

## Added after the pass, on two further instructions (D-322)

**The rate constraint has a parent after all.** §3.6 recorded it as having "no equally direct parent" in the Declaration, and the audit above repeated that as a cost of taking Arts. 3--21 entire. The author's instruction was to add it to the foundation, and doing so showed why the search had failed: **what it protects is a condition rather than an act.** Article 6 gives everyone the right to recognition everywhere as a person before the law; Article 10 states the procedural form that interest takes. Every article in the set presupposes that somebody determined whether this person, this case, falls under it, and a rate removes the determination without refusing it, which is a mechanism the drafters in 1948 had no occasion to write against. So the constraint rides with the set as a condition on all of it rather than as a nineteenth item, and that is also the reason the duty attaches to the operator. Stated in four places, and **decision 10's revision of §9.1.1's four limits, which this pass had left outstanding, went in with it**.

**The bar on authoring a reference entry is lifted.** `un1966iccpr` and `un1966icescr` are in `refs.bib`, cited where §9.1.1 attributes the division to the covenants. Verified: both adopted by UNGA resolution 2200A (XXI) of 16 December 1966; the economic covenant in force 3 January 1976, the civil and political one 23 March 1976. **Two things are deliberately missing from the entries.** No UNTS volume or page, because I did not verify them. And no `urldate`, because I never retrieved the instrument pages: OHCHR and Refworld both returned 403, so the facts rest on a search summary that cited OHCHR. Both entries land unchecked, 0/226 becomes 0/228, and that is what the refs ledger exists to record.

**Measured after the addendum:** 77,730 words, 161 pages, 88 sections, 75 cross-references, 228 entries all cited and 0 human-checked, 0 undefined, suite green.
