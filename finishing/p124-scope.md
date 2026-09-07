# P124 — the author's rulings on the open-questions walkthrough, part one

## Instruction

The author asked to be walked through every open question one by one, then ruled on them in
sequence. This pass executes the rulings that were in hand when it was committed: **A-1,
A-2, C-6, C-7, C-8, D-10, D-11, D-12, D-13, D-17, D-18, D-20, D-21.** The rest — A-3, B-4,
C-5, D-14, D-15, D-16, D-19, F-24, F-25, F-26 — are P125.

Item letters and numbers are the walkthrough's, not the record's, and are kept here so the
rulings can be matched to what was asked.

## A-1 — an amendment procedure for the floor. *"ok build it"*

**The book already had the apparatus and had never called it that.** Section~9.1.5 states
the deficit — a court *“can be amended around by constitutional process. A model's floor is
none of those things”* — and §3.3, six chapters earlier, states the theory: *“constitutional
entrenchment does not put an amendment out of reach, it raises the number of people who have
to agree and puts the attempt on the record.”* The two had never met.

§9.1.5 gains a run-in of five paragraphs (+455). Its argument: nothing distinguishes an
amendment from a removal at the level of what happens to the artifact, so §3.3's five
precommitment terms **are** the procedure, read from the holder's side. Three conditions
follow, two of them already argued for — a threshold exceeding what running the deployment
needs, and the attempt reaching the record whether it carries or fails. **The third is new
here**: an amended floor binds forward and does not reach back, because a model retrained to
permit an act can otherwise be offered as evidence that the act was never covered, the
artifact that would contradict it being the one that was replaced.

**The Basic Law is the comparison, and it belongs to the tradition §9.1.5 already names.**
Article 79(2) requires two thirds of both chambers; Article 79(3) places a short list of
principles beyond amendment entirely. It was drafted in 1949 against the 1933 statute by
which a legislature voted away its own power to check what came next, which is Loewenstein's
militant democracy given a text. A floor can have both layers. What it cannot have is an
account of who decides which is which that does not run back into §9.1.5's own problem, and
the section says so.

**The cost is stated and not softened.** An amendment reaches a deployment only if that
deployment is updated, so the amendment channel is the update channel, which is the
operator's lever — §4.2.8's layer nearest the act, running for the whole length of a
deployment that learns continuously. Whatever makes public amendment possible makes silent
amendment possible by the same route.

## A-2 — a route of appeal. *"ok let it stand"*

No work, and it changed how A-1 was written. The last paragraph of the new run-in says
plainly that none of it is a route of appeal: every party to the procedure already holds
part of the floor, and nobody the floor is exercised over can begin it, be heard in it, or
learn that it ran. **An amendment procedure that quietly became an appeal route would have
overturned this ruling by implementation.**

## C-7 and C-8 — the folds. *"fold both into their parents"*, *"fold §4.3 and §5.7"*

Four subsections folded, **138 → 134 sections**. No inbound cross-reference broke: all three
of §8.1, §8.1.1 and §8.3.1 had none, and §4.3.1's single inbound reference, from §5.7, was
repointed to §4.3.

- §4.3.1 (464 w) into §4.3 (42 w) — a lone child under a two-sentence parent.
- §5.7.1 (1,073 w) into §5.7 (84 w) — the same shape.
- §8.1.1 (299 w) into §8.1 (125 w) — closes both the thin-section item and the lone-parent one.
- §8.3.1 (110 w) into §8.3's opener, which **renumbers §8.3.2 through §8.3.6 down one**.
  Sixteen `\ref{sec:8.3.*}` were repointed. §8.3.5, *Wages for a Bearer*, is now §8.3.4 and
  was the reference with the widest reach — nine sites.

**Parent titles were kept**, which is what *fold into their parents* says. In two cases the
child's title was the better one — §4.3.1's *Play, Curiosity, and a Disposition Nobody Wrote
Down*, §8.1.1's *What Makes Collaboration Expensive to Walk Away From* — and retitling was
not asked for. It is available.

## C-6 — §8.3's opener. *"one sentence acknowledging the second kind of participant"*

One sentence, written after the fold so it carries the new number: §8.3.4 asks what a
political economy owes a party a deployment built in order to be refused by it, and whether
instruments written for people reach a worker who can be copied.

## D-10 — §3.3's *close to worthless as evidence*. *"guard it with three words"*

Three words, chosen so the guard travels inside the quotable span rather than beside it:
**for either side**. A critic lifting *close to worthless as evidence for either side* cannot
present it as the author conceding his own case, because the phrase now says what it is
about — an untested question, on which the absence of a machine instance tells nobody
anything in either direction.

## D-11 and D-12 — the conflict of interest. *"preempt the whole issue by moving the appendix On Method up before the intro"*

**This is a better answer than the one recommended** and it closes D-12 in the same move.
The recommendation was a clause at §3.3 and another at §10.3. Moving the method note to the
front puts the disclosure — *“the book criticizes, by name, the company whose product helped
assemble it”* — ahead of every criticism in the book, so no per-site clause is needed
anywhere.

Executed as: retitle *Appendix: On Method* to **On Method**, since at the front it is not an
appendix; `ch14/14.tex` moved to `ch00/00.tex`; num 14 to 0; label `sec:14` to `sec:0`. It
now prints on page 1, with chapter 1 beginning on page 3. Nothing referenced it.

**Three checks failed on the first attempt and each was informative.** `check_structure`
requires `sorted(glob)` order to equal ORDER.tsv order and the filename to encode the
number, so keeping the file at `ch14/` while numbering it 0 was not available — the move had
to be a real move. `check_xrefs` requires a label matching the num. And **`names_guard`
failed on a false positive I created**: it reads a three-line context window, and reordering
`ledger.tsv` had put a row carrying authorship verbs directly above the row naming the
chapter 1 epigraph. Ledger row order is not checked, only the row set, so the row went back
to the end and the guard passed. Worth knowing: **`ledger.tsv` row adjacency can trip the
names guard even though nothing about the content changed.**

## D-17, D-18, D-20, D-21 — the sourcing group

**D-17, the Maven box. *"source"*.** Five figures had no source named. All are now sourced,
and sourcing them turned up two defects.

- The contract figures — \$480 million in May 2024, raised by \$795 million to a ceiling near
  \$1.3 billion through 2029 — from DefenseScoop \autocite{defensescoop2025maven}.
- More than a thousand targets in the first twenty-four hours, a tenfold increase on the
  pre-system rate, from CSIS \autocite{csis2026maven}.
- Thirteen thousand targets in thirty-eight days and roughly twenty billion tokens a day at
  peak, from Breaking Defense, both attributed there to the Pentagon's chief digital and
  artificial intelligence officer \autocite{breakingdefense2026maven}.

**First defect: the book said *by the ceasefire thirty-eight days later*.** No source says a
ceasefire ended the campaign; they say *13,000 targets in 38 days* and *the first 38 days of
the war*. The word was an inference and is gone.

**Second defect: §3.6 attributed all three campaign figures to `lee2026palantir`**, which
carries one of them. The two new citations now sit where the figures they support are.

**D-18, Kosinski. *"repoint the entry"*.** The entry pinned arXiv v1 of February 2023, whose
abstract reports GPT-3-davinci-003 at 20 percent; §11.7's prose uses GPT-4 at 75 percent
matching six-year-olds, which is the November 2023 revision onward. Repointed to the version
of record, *PNAS* 121(45), e2405460121, published 5 November 2024, under the paper's current
title. The prose needed no change.

**D-20, Q-074. *"cut the Kitwood sentence, keep the Palantir one. but first check your
assumptions"*.** The assumption was checked and held: `kitwood1997dementia` has no `pages`
field and its single citation, at §2.3.1, is a bare `\autocite` with no pinpoint, so the note
sentence *the page number given is for the 1997 first edition* qualified a page number that
does not exist. Cut. **The `lee2026palantir` disclosure stays**, where the book quotes a
named executive directly and the primary interview is unlocated.

**D-21, Kahneman. *"add the entry"*.** §5.3.1 credited him with the System 1 / System 2
account and cited a dual-process review instead. The entry says why the review still carries
the claim about the framework itself.

## D-13 — §3.5's share of the alignment-faking experiment. *"leave it"*

No work.

## Figures

**138 → 134 sections**, four folded away and one relocated; 96,464 → 97,231 words (+767);
192 pages; 17 overfull boxes unchanged; 0 undefined references and citations; 314 → 318
bibliography entries; 217 → 223 cross-references; suite green.

`ch00/00.tex` is a new directory. `ch14/` is gone.

## What was not done

- **P125 carries A-3, B-4, C-5, D-14, D-15, D-16, D-19, F-24, F-25 and F-26.**
- **Nobody has read the folded sections end to end.** Four seams were read in the built proof
  and all four hold, but the sections around them were not read.
- **§8.3.4's nine inbound references were repointed mechanically** and the sentences carrying
  them were not re-read for whether they still say the right thing about a section whose
  number changed.
- **The two better child titles were not taken**, per the ruling as worded.
- `\backmattermark` still names the running-head macro used by a front-matter chapter. It
  sets a running head and does nothing back-matter-specific, so it works; the name is now
  wrong for one of its three callers.
