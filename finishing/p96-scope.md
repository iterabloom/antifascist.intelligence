# P96 — the chapter 3 rulings of 2026-09-03, distilled and applied to chapters 3 through 12

**The instruction.** *Distill what it was we improved from 6e70bde and apply that to the rest of
chapter 3, and 4-12.* One sitting, after the author's own Overleaf edits and the four passes that
followed them (D-189 to D-193) and the two small commits after those (`f0cc6a5`, `4271bc8`).

## The distillation

Ten classes, each carrying the before-and-after it came from, written to
`~/…/scratchpad/rulebook.md` and given to every reader. In one line each:

1. **Say it once, plainly.** A point encoded in pronouns or a balanced pair is stated. The Leo
   paragraph's close; *fail into custody*.
2. **Cut the guard.** A claim followed by a clause defending it loses the clause. *recognizably
   worse, and worse in a way that…* became *worse*.
3. **The book does not talk about its own drafts or readers.** *which now has to carry more weight
   than it did* was cut.
4. **No self-importance.** *severe* became *significant*; *precisely a floor* became *a floor*.
5. **A true sentence at the wrong moment is cut.** The *Cook* test clause.
6. **An opener says what the section is about, without cleverness**, and does not make a later
   section's point.
7. **A list is a list of the same kind of thing.** §3.2's four became two-plus-two.
8. **Counts and paraphrases match their targets.** §3.6's restatement of §3.1; *three ways*.
9. **Where the book already has the mechanism, use it.** Formation applied to the third way.
10. **The cost gets named where the section prices costs.** *big deal* became *The cost is
    significant*.

Two things the author rejected as findings went into the rulebook so nobody would report them
again: two ordinary words for one thing, and a pointer removed on purpose.

## How the sweep ran

Classes 3, 4 and 8 are partly greppable and I ran those myself: every *exactly*, *precisely*,
*severe* and *recognizably* in chapters 3 to 12, judged one at a time; every sentence in chapters 4
to 12 that attributes a claim to a chapter 3 section, 41 of them, read against the current chapter
3; every count stated in the same sentence as a cross-reference, 46, checked against its target.

The reading classes went to eight readers on Opus, one or two chapters each, every one given the
same rulebook and the same output format: file, line, class, the sentence verbatim, a replacement
verbatim, one line of reason. They read every file of their chapters in full and opened the target
of every attributing cross-reference. **I verified every candidate in context before applying it**,
opened every target the candidate turned on, and rewrote replacements where the reader's version
changed a claim or used a contrastive frame.

## What was applied

**175 replacements in 84 section files.** 44 from my own greps and target checks; 131 carrying
out 128 of the readers' 142 candidates and one companion edit. The 14 declined candidates are
listed at the end.

**Intensifiers (class 4), 45.** *exactly* went from 37 occurrences in chapters 3 to 12 to 2 and
*precisely* from 9 to 3. The five kept do work: *followed exactly*, *precisely enough for a
person to contest*, *rewrite its own weights precisely*, *to precisely the extent*, and chapter
10's *exactly the capability an authoritarian movement that wins an election requires*, which
matches chapter 1. Also: §11.3's *data requirement is severe* is *demanding*; §3.5's *the most
concrete thing in this chapter* is gone; §8.3.3's *with full force to its own flagship proposal*
is *to this proposal*; §10.6's *the whole function … whose entire purpose* is *the function … that
binds*.

**Stale counts and paraphrases (class 8), 36.** The ones that changed a claim:
- §4 and §5.7 still said an unspecified disposition *cannot be edited*, the claim D-186 withdrew
  from §4.3.1. Both now say it offers no parameter to remove.
- Chapter 11's opener and §12.2.1 both said §11.2's third question has no near-term experiment.
  §11.2 has given it one since P43, the provenance test. Both now say so.
- §9.3.3 opened by saying §9.3.2 *closed on two concrete cases*. §9.3.2 does not; §9.3.3
  supplies the cases itself two paragraphs later.
- §9.1.4 credited §5.4.2 with a list ending in *a multi-stakeholder review body*. §5.4.2 gives no
  list; it asks for a bounded task, checkable outputs, and a body with standing to act.
- §9.3.1 credited §2.3.2 with a four-discipline composition for the review body. §2.3.2 specifies
  interdisciplinary plus a lay member, and the lay member was the thing §9.3.1 had dropped.
- §8.3.3 credited §5.1.3 with *eroding trust, humiliation and social fracture*. None of those
  words is in §5.1.3.
- §12.2.2 named the IEEE's CertifAIEd program as an instrument that could independently verify a
  system. §8.3.5 describes it as a professional credential that *certifies that somebody sat the
  assessment, and no more*.
- §8.2.1 said §7.2 frames coerced disagreement as *clean the input*. §7.2 says the two problems
  are different and only one has a research program.
- §3.8 said *the previous section* left a dial. That is §3.5; §3.7 has been between them since
  P57.
- §3.9 said §3.8 *ended on* the failure a bearer cannot report. It names it mid-section and ends
  on continual learning.
- §3.4's *ninety seconds* is §2.2.2's *under a minute*. §3.10's *several systems with different
  principals* named §3.3's third construction with the fifth's vocabulary.
- §5.6.2's *three places* for the override requirement is two, which is what §3.5 counts.
- §5.2.1 pointed to §3.8 for the claim that self-concern is not a free property; §3.4 makes it.
- §6.2 described §6.4.4 as a state that has studied the system; §6.4.4 opens by saying the state
  does not need to, because it can compel the people who hold it.
- §11.4's *censor-everything example* is §4.2.2's *flag-everything*, and the book keeps those apart.
- §10.6 said §9.3.4 *diagnoses* a review body that cannot compel; §9.3.4 prescribes the remedy.
- §10.1 sent the reader to §10.5 for a count of compute; §10.5 counts connectivity.
- §9.3.4 said the Three Rs *are explicit* about two errors; the book's own §9.3.2 is.
- §7.4 scored four items under labels of which two were halves of one §2.1.2 sentence. The item
  about benchmarks replacing defendants is now labeled *Aestheticization of the metric*, which is
  what it describes. See the note under *left undone*.
- Chapter 3's opener and §12.1.2 called eight voluntary instruments *bodies*; a recommendation, a
  set of guidelines, a process and a compact are not, and §12.1.2 goes on to distinguish the
  bodies that can act. Both say *commitments*.
- §9.2's *a decade old* is *dates from 2018*. Three British spellings, *licence*, *neighbouring*
  and *defence*, are US.

**Plain statement (class 1), 37.** The kind of thing: §3.5's *What is one property with refusal
is not the prevention of the halt* now opens *Refusal does not prevent the halt*; §3.8's *The
second has two forms* says *Exit*; §6.3's *can harm nobody intended to harm* says *can do harm
nobody intended*; §10.4's *a law a government enforces against itself* says *against companies*,
which is what the contrast needed; §10.3's *the developer* twice in one sentence for two
companies now names the weapon's developer and the model's; §7.4's *That episode*, which named
nothing, names the dismissals §9.1.2 describes; §7.2's *Neither method* names both methods.

**Guards (class 2), 16.** §3.8's *and both hold*, when the second asymmetry *largely rescues
itself*; §3.6's *I am not proposing the list below* folded into the sentence before it; §9.1.2's
deferral to what the dismissed researchers *have made publicly themselves*; §10.2's *Whatever one
thinks of that specific policy*; §11.2's *That is not a capability to bank*; §4.2.5's *That risk
is not an argument against the method*.

**The book about itself (class 3), 4.** §3.4's *and this book has not said so*; §7.4's *The four
had been scored and the five left unrun* and *which is what this book had before*.

**Openers and duplicates (classes 5 and 6), 8.** The clause §3.3 and §3.7 both carried, *procedure
is a cheaper thing to ask of the world than custody…*, stays in §3.7 and leaves §3.3, which has the
argument without it. Chapter 8's opener carried §5.5.1's closing sentence word for word; it now
says what §8.1 does instead. Chapter 6's opener glossed its epigraph in the sentence §6.4.1 uses
when it reaches the same quotation. §6.4's opener gave the two examples §6.4.1's sixth item gives.
§10.4 characterized a roll of instruments it never lists. §9.3.2 opened mid-list; it now says six
principles govern the research. §6.3.4 listed a WIOA lever among the cases that got a harm fixed,
in a paragraph that had just said WIOA fixed nothing.

**Mechanism pointers (class 9), 15.** Each is one sentence naming the book's own account where a
section had reached for it without pointing: §5.1.2's apprenticeship to §3.1's formation; §6.2's
erosion by adaptation to §3.8's accommodation; §6.4.4's compelled custodian to §3.1; §8.2.1's
disbanded panel to §3.5's halt; §8.3.3's refusal rights to §3.8; §9.1.2's self-funded oversight to
§8.2.1's case; §9.3.3's guardian-operator identity to §11.2's finding; §10.1's government-specified
adaptation to formation; §11.5 and §11.6 to §3.3's multi-principal and plural constructions; §4.2.7
to §3.7's legibility trade; §7.3's slope test to §9.3.5; §3.7 to §3.8's sincere drift; §5.3.1 to
§2.2.3, which already pointed the other way.

**Lists and frames (classes 7 and 10), 4.** §3.6's fourth item gets its cost, tempo, in a
paragraph that prices the other three. §5.4.1's second ring opens on a pressure like the rings
around it. Chapter 11's *Every one is a party* summed a list three of whose members are artifacts.
§6.3's three mechanisms are now three mechanisms and not two mechanisms and a person.

## Numbers

**91,717 → 91,436 words, −281. 186 → 184 pages. 138 sections.** `check_all.sh` green; the PDF
builds with no undefined references or citations. `reports/section_stats.tsv` regenerated.

## Declined, with the reason

- §5.4.2's *the condition most readers of this book actually live under*: an argumentative point
  about the reader, not the book narrating its drafts.
- §5.7.1's *Two of the four accounts usually cited here transfer*: the four have four fates and the
  paragraph gives each one.
- §5.1.2's three cautions: the middle one is a caution about design, and the cut would lose a
  sentence of content on a category quibble.
- §6.4.2's opening sentence repeating §6.4's: it is the subsection's own thesis.
- A *Data Provenance* run-in head for §6.1.1: the section already has a *Data Collection* head, and
  where those two paragraphs belong is a structural call.
- §8.1.1's *Almost everything founded on standing money*: strengthening to *Everything* is a
  factual claim I did not check.
- §12.3's closing *A reader who takes only the instrument*: the book's last paragraph, and a
  rhetorical figure rather than revision history.
- §9.3.4's last sentence, that the Three Rs answer only what a board does inside its scope: it
  limits, it does not contradict.
- §9.3.5's shame sentence: *shame* is used twice in the section.
- §10.4's *only as durable as that agreement*: it states the dependency the second half cashes.
- §11.2's *grew in importance while this book was being written*: the author kept the same shape
  in §3.5.
- §11.3's *four features … three worked through*: not verified.
- A pointer from §4.2.9's transfer failure to §3.8's accommodation: distribution shift and drift
  are different mechanisms.
- §7.2's sentence pointing to §5.5.1 and §5.7: it makes a claim, that chapter 5's methods do not
  reach the ordinary case.

## Left undone, named

- **§7.4's labels.** After the relabel, three of its four scored items carry a feature's name and
  the fourth, *Asking why becomes the deviant act*, still carries a phrase from §2.1.2's
  molecular-scale sentence. Decoupling is not scored under its own name. Reorganizing the section
  is the author's call.
- **§6.1.1 and §7.1 share a sentence**, that an annotation pipeline built without dissent produces
  the ground truth it was built to produce. §6.1.1 hands off to chapter 7 explicitly, so I left it.
- **§11.5 says weak-to-strong generalization is *the one of the three***, two paragraphs after
  naming two candidates. The third is Democratic AI, named between them; nothing calls the three a
  set.
- **A run-in head in chapter 4, *One mechanism, several jobs*, sits over a paragraph that does not
  make the point it names**; the reader flagged it and neither of us had a one-line fix.
- **Chapters 1, 2, 13 and 14 were not swept.** The instruction named chapter 3 and 4 to 12.
- **No section was read end to end by me.** I read every changed sentence in its paragraph and
  every target it turned on. The readers read the chapters whole.
- **Ledger rows are not annotated**, following P87's practice for a class sweep; D-191's eleven rows were the exception and this pass touches 84.
- **The proof pair is behind** by this pass and the two commits before it.
