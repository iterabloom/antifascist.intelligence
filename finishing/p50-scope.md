# P50 — the manuscript read whole

**Author's instruction, 2026-08-29:** *"please read the entire manuscript."* All
153 sections, chapters 0 through 13, in `ORDER.tsv` order. This is the first read
of the book end to end since P27 rewrote chapter 3, P32 split chapter 8 and P38
distilled chapters 2, 4 and 5 — 140 of the 153 sections stand `drafted` and unread
by the author, and P49 read two of the thirteen chapters whole.

**Decision row:** D-114. **Branch:** `pass/50-whole-read`. **No manuscript file is
touched.**

**Four defects, seven rulings wanted.** The author asked for the record rather than
the repairs, so nothing here is applied. The four defects are verified against the
files and each carries the command that confirms it. The seven findings that change
an argument or cost words are entered as Q-046 through Q-052. One finding reported
to the author was wrong and is recorded here in its corrected form, because the
correction is the part a later session needs.

## What the read was, and what it cannot catch

The 153 files were concatenated in `ORDER.tsv` order and read in sequence. No tool
was run against the text before the reading; every command in this file was run
afterward, to confirm or kill something the reading had already turned up.

**What that method catches** is what a reader meets in order: a term the book uses
for a chapter before defining it, a pointer that names a claim its target does not
make, a chapter that does not carry an obligation an earlier chapter assigned it,
an allusion whose referent has not been supplied yet.

**What it does not catch, stated so the coverage is not overread.** No citation was
checked against its source; no reference in this pass was verified against the work
it cites. No figure in `STATE.md` was re-measured. The reading was for argument, so
a sentence that is merely clumsy was passed over unless it broke something. And a
single read finds what is inconsistent between two places far apart more reliably
than what is wrong in one place on its own — the four defects below are all of the
first kind, which is a property of the method rather than a finding about the book.

## The four defects

None is repaired. Each was found by reading and then confirmed, and the confirming
command is given so a later session can re-run it instead of re-reading.

### 1. Section 2.4.1 points into 3.5 for close to the inverse of 3.5's claim

Section 2.4.1 closes its disability passage: "Section~\ref{sec:3.5} turns on this:
what keeps a bearer in existence is standing held by parties outside it, which is
where moral status has rested for the hard human cases too."

Section 3.5 argues past that rather than on it. Its opening move is that something
outside the bearer "would have to make erasure expensive and the candidates are
thin," and the question then "dissolves under section 3.4's answer": the bearer
guards its own continuation from the structural interest, and what it can do about
being switched off "is the one way of getting it that does not run through a quorum
somebody else selected." The word *standing* occurs once in the section, in the
other sense.

So the citing sentence credits 3.5 with the claim 3.5 declines. This is Q-041's
class, and it is the sharpest instance found so far: the earlier instances named a
claim the target did not make, and this one names something near its opposite.
`xref_pairs.py` cannot see it, because the pairing file shows the target's opening
sentence and 3.5's opening sentence poses the question it is about to dissolve.

```sh
grep -o "Section~.ref{sec:3.5} turns on this[^.]*\." manuscript/sections/ch02/02_04_01.tex
grep -c "standing" manuscript/sections/ch03/03_05.tex   # 1
```

### 2. The section 2.4 epigraph prints a research note

The attribution block under the *Westworld* epigraph carries two lines that are
apparatus rather than attribution: a raw `web.archive.org` URL, and the line
`also see Science Fiction, Disruption and Tourism Ch 15`. Both are set in the
typeset book and both are visible in the committed proof.

They are the only raw URL and the only "also see" in the manuscript, which is what
makes them a residue rather than a convention.

```sh
grep -rn "https\?://" manuscript/sections/          # one hit, ch02/02_04.tex
grep -rn "also see\|see also" manuscript/sections/  # one hit, the same line
```

### 3. Section 3.5's allusion to the Iran school strike is uncited and unglossed

Section 3.5: "The operators who wipe the bearer that called the compound a school
do not have to get past it to do that."

The referent is the strike the book already carries at section 10.10 — "a
civilian-harm investigation into a strike that killed at least a hundred and
sixty-five people, most of them schoolchildren" — whose reference names it
directly: Military Times, *Senate Eyes Hegseth Travel Cuts Without Probes into
Iran School Bombing, Boat Strikes* (`stassis2026senate`). Section 6.4.1's Maven box
carries the campaign it belongs to, with the vendor's model inside the platform.
The author's account of the event is that the target was believed to be an IRGC
compound and was a girls' school.

Given the event, the sentence is exact: the bearer is the party that said *school*
where the operators said *compound*, and it was wiped rather than argued with. It
is the most concrete statement in chapter 3 of what the floor is for.

**The defect is the definite article doing referential work the text has not
earned.** "The compound" reads as anaphoric, so a reader who is not carrying the
news parses it as a pointer back to a case the book has introduced, and there is
none — chapter 3's only neighbouring material is 3.1's "geolocating a description"
and 3.7's "geolocate a school," which is a different scenario and comes two
sections later. The event is documented five chapters away with no pointer from
here.

It is also the one place in the manuscript where a 2026 news event is carried in
running prose rather than in a dated box. Section 6.4.1 boxes and dates the same
campaign; `style.md` §5 is the rule that produces those boxes, and this sentence
sits outside it.

The repair is small and the sentence earns it: a few words of gloss and a pointer
to section 10.10.

```sh
grep -rno "compound[a-z]*" manuscript/sections/     # ch03/03_05.tex is the only use in this sense
grep -o "sec:[0-9.]*" manuscript/sections/ch03/03_05.tex | sort -u   # no pointer to 6.4.1 or 10.10
```

### 4. Section 6.3.4 states unqualified what 6.1.3 and 6.3.3 qualify

Three subsections of chapter 6 treat explanation, and the limit is in two of them.

- **6.1.3** explains LIME and SHAP and closes on the limit: "Neither tool can tell
  you that the model is aimed at the wrong thing. Both take the training target as
  given."
- **6.3.3** says explanation makes a system's failures *contestable* and "not a
  system whose failures are visible, because an account of a decision can be
  produced after it." That sentence is D-106's repair; before P42 it said *visible*.
- **6.3.4** opens: explainability and transparency "let developers, users,
  regulators, and the people affected by a decision inspect the reasoning that
  produced it," and later that a risk-assessment system "that discloses how it
  weighs its inputs makes it possible to catch and correct bias." It then explains
  LIME and SHAP again, at greater length, carrying neither limit.

**D-106's repair reached 6.3.3 and not the subsection three heads later.** This is
Q-043's class inside one section of one chapter, which is a tighter radius than any
of the nine instances recorded across the five previous passes.

The duplication that goes with it is a separate question and is entered as Q-049,
because deciding which of the two treatments survives is not mechanical.

```sh
grep -rn "LIME\|SHAP" manuscript/sections/ch06/     # 06_01_03.tex and 06_03_04.tex
grep -n "contestable\|inspect the reasoning" manuscript/sections/ch06/06_03_03.tex manuscript/sections/ch06/06_03_04.tex
```

## The seven rulings wanted

Each is entered in `QUESTIONS.md` with its evidence, options and default.

| Entry | Subject | Default |
|---|---|---|
| Q-046 | The book's operational definition of a floor *holding* is at section 5.1.1, and chapter 3 does not cite it | (a) pointer from chapter 3 |
| Q-047 | Section 3.3's falsifier requires a training provenance the same section says cannot be proved | (a) concede it in a clause |
| Q-048 | Chapter 7 applies four of the nine tests section 2.1.2 builds | (a) leave, and say so |
| Q-049 | LIME and SHAP are explained twice in chapter 6 | (a) cut 6.3.4's, point at 6.1.3 |
| Q-050 | The vendor is named for the criticism and unnamed for the credit | (a) leave |
| Q-051 | How an authoritarian movement wins is exogenous to the book | (a) leave |
| Q-052 | Chapter 1's advance note does not carry section 2.4.1's own caveat | (a) leave |

Two of the seven are worth more than their defaults and the entries say so:
**Q-046**, because chapter 3 uses *holds* in three section titles and defines it
nowhere, and **Q-048**, because running the five discriminators is the one chance
in the book to show the definition discriminating rather than only accusing —
which is what section 11.3 says has not been demonstrated.

## The finding the author corrected

Reported to the author: that section 3.5's "the bearer that called the compound a
school" was a dangling reference to an example cut from the manuscript, on the
evidence that no case in the book establishes it.

**Wrong.** The referent is external and real, and is recorded above as defect 3 in
its corrected form. The evidence that produced the wrong reading was sound — the
scenario is genuinely absent from the book — and the inference from it was not,
because a reader who has the news needs no scenario.

It is recorded here for two reasons. A later session that finds the same sentence
will reach the same wrong conclusion from the same grep, and this file is where it
would look. And the error is the method's characteristic one: reading the book as a
closed system finds what the book has not supplied, and cannot tell an omission
from an allusion.

## What was checked and held

Named so a later session does not re-open them.

**Chapter 3's central inference is not equivocating between 3.2 and 3.4.** Section
3.2 states the requirement behaviourally and says an engineer who thinks machine
feeling is a category error "can accept everything in this section"; section 3.4
restates it as holding another's welfare as a reason against the system's own
interest, and runs the induction over that. The bridge — "That is section 3.2's
second rung with the content filled in" — is asserted rather than shown, and 3.2
forecloses the objection by naming the question as empirical and handing it to 3.3
explicitly. The chapter is doing what it says.

**Section 4.2.3 does not dismiss CIRL and leave the hybrid unconsidered.** Its
closing paragraph gives the bounded use — inference above the floor, where the
question is what a person wants rather than what may never be done to them — which
is the synthesis section 2.1.1's pluralism recommends.

**Chapter 5 does reference chapter 3.** 18 references across 11 of its 23 sections,
against 20 in chapter 4 and 22 in chapter 2. The uptake P26 (D-078) was opened to
fix is real at the reference level. What the references are is a different matter
and is Q-046's subject: most are concessive, saying why each mechanism falls short
of the floor, and the one place chapter 5 builds rather than concedes is the
sentence Q-046 is about.

## What this pass does not do

It repairs nothing. It does not touch `ledger.tsv`, since no section's prose
changed. It leaves Q-035 where P49 left it, awaiting a ruling on chapter 5's
citation age, and Q-043 and Q-045 open. It checked no citation against a source,
which means the four defects are defects of internal consistency and the book's
factual claims were not audited by this pass at all.
