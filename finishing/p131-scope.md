# P131 — the standing objection: worked in chapter 9, absent from the introduction, uncaveated where the floor is actually published

**Instruction.** An outside note, *"Move the authorization question out of the closing pages."* It
argued that §3.10 concedes publication is a transparency condition and not an authorization
condition, that a laboratory installing tamper-resistant moral commitments in a widely deployed
system has produced concentrated unaccountable power with unusually good documentation, and that this
"currently arrives after the case has closed, with *nothing here has touched it* attached." It asked
for the objection in chapter 1 and again wherever the floor's contents are published. *No answer is
required.*

The author asked what I thought, then: **"After checking your assumptions, please revise the
manuscript as your last message contemplates."** Checking overturned most of what I had proposed.

## Three corrections to my own assessment, and what caused each

**1. I reported §9.1.5 as having no inbound cross-reference. It has two.** `03_03.tex:37` points at
it for the amendment procedure; `03_09.tex:22` points at it for the legitimacy cost of one bearer at
scale. Both are in chapter 3, both ahead of §3.10. **Cause: I truncated my own grep output.** The
matching lines were in the first result, cut off at 260 characters by a `sed` filter I had written
into the command, and the `\ref{sec:9.1.5}` sat past the cut in both. A second check I ran — sections
with zero inbound references — correctly omitted 9.1.5 from its list of 64, and I read past that too.
The lesson is not about grep. It is that I asserted a negative from a filtered view and had
disconfirming evidence on screen twice.

**2. The repair I proposed to the author was a new cross-reference, and two executed passes had
already cut that class.** D-089 (P28) and D-099 (P35) run on the author's own finding that the
manuscript's explicit references "make the prose feel like a navigated repository": 791 references in
94,590 words, one per 120. P28 cut by class, keeping references that **import a result or mark a
boundary** and cutting those that merely announce another section agrees. P35 took 883 to 805 and 758
to 680 in the prose. The book now stands at **230**. My proposal was the cut class exactly. The
author's three mid-turn messages — *"xrefs are probably something you grep for"*, *"that doesn't mean
the book doesn't mention parts of itself without an xref"*, *"because xrefs are really annoying to
human readers"* — are D-089 restated, and the first two are what sent me back to find correction 1.

**3. I told the author the note's second recommendation was already satisfied at
`09_01_05.tex:21`. It was not.** That line is §9.1.5's own list of design consequences, not a
publication site. The sections that actually run the enumerations carry no legitimacy caveat:

| Site | What it publishes | Caveat |
|---|---|---|
| `03_06.tex:10–22, 27` | the seven interception positions and the four candidate acts — the only place either list is run | none before this pass |
| `03_03.tex:19` | the four precommitment forms | none; `:37` points at §9.1.5 for amendment mechanics only |
| `03_05.tex:48` | the five-term list restated | none |
| `03_10.tex:29` | the five-term list restated at full strength | none in that paragraph; the caveat is six paragraphs earlier at `:23` |
| `09_01_05.tex:26` | the five terms recast as an amendment procedure | the only restatement inside a legitimacy frame |
| `03_01.tex:7` | the demand stated generically, instantiation declined | none |

In every one, publication is justified by **detectability** — "a later absence is a visible absence" —
and never by authorization.

## What the note was restating

The note's paragraph is close to verbatim the book's own **Q-064, "The book has no concept of
legitimacy"**, including *"Publication is a transparency condition and not an authorization
condition"* and *"concentrated unaccountable power with good documentation."* Q-064 was **closed by
execution on 2026-09-01, D-168 (P86), on option (b)**: an acknowledging paragraph in chapter 3 — which
is `03_10.tex:23`, doing the job it was written for — plus §9.1.5 new at 724 words, with Waldron and
Loewenstein verified and added. So the concession the note read as an author caught conceding late is
a designed acknowledgment, and the treatment it asked for exists at 1,686 words.

**Q-068 remains open and this pass does not answer it.** §9.1.5's third design consequence — a route
by which the parties a floor is exercised over can raise an objection that reaches somebody — is
named in the text and unsupplied, on the author's standing default (a), *leave it named*.

**The note's one live contribution is the introduction, and it is real.** Chapter 1 states the value
the book is organized around at `01.tex:16` — systems "against concentrated, unaccountable power" —
and never says its own proposal is an instance of what that phrase names. The only cost the
introduction states, at `01.tex:20`, is uncorrectability.

## The four edits

**A. `ch01/01.tex:20`** — appended to the costs paragraph: *That trade has a second cost, and I state
it here without discharging it. A machine built to refuse on somebody's behalf is a machine whose
builder chose what it would refuse, and nobody outside the laboratory was asked.* The author chose this
wording from a preview.

A collision was checked and does not fire. `01.tex:26` says "the floor with its four costs" and
`03_01.tex:23` names them — *custody, patienthood, enforcement, and formation* — with legitimacy not
among them, §9.1.5 having arrived later. The new sentence attaches its "second cost" to **the trade**
in line 20, the capacity to be ethical, whose first cost is stated in the preceding sentence. It does
not read as a fifth thread. **That the four hanging threads omit legitimacy is filed as Q-095 rather
than renumbered.**

**B. `ch03/03_10.tex:23`** — one line, two jobs.
- The opening clause reworded from *"people who did not select it, cannot contest it, and in most
  cases will never learn that it acted"* to *"people who had no part in choosing it, no way to argue
  with it, and in most cases no knowledge that it acted"*, which removes the duplication below.
- The closing sentence replaced. Was: *"The floor's authority is a separate question from its
  durability, and nothing here has touched it."* Now: *"The floor's authority is a separate question
  from its durability. This chapter has not touched it, and where the book does take it up the case
  comes out no better than the one for a constitutional court holding a right against an elected
  majority: contested where it is made, and at its strongest an argument that the alternative is worse
  rather than a grant of permission."* The scope is explicit, which is the repair for the misreading
  the note performed; the reader is told the book returns to it, in prose rather than by a locator;
  and §9.1.5's verdict is imported so the answer arrives without leaving the page. **No
  cross-reference**: the sentence carries itself, which is P28's surviving class.

**C. `ch03/03_09.tex:22`** — reworded to remove the duplication below. §9.1.5 keeps its version of the
argument as the surviving instance under D-013. The existing `\ref{sec:9.1.5}` in the sentence stays;
it imports a result. A first draft of the replacement put *mistaken* three times in one clause and was
rewritten before anything else was run.

**D. `ch03/03_06.tex:42`** — the caveat where the enumerations are actually run, added to the sentence
giving the warrant for publishing them: *That makes the list checkable and does not make it
authorized: both enumerations are written by the deployment about itself, and the people the four
prohibitions exist for have no part in either one.* This is the part of the note that correction 3
made live.

## Two duplications, measured before and after

Found while checking, not by a tool in the suite. Both are between chapter 3 and §9.1.5, and both
pairs already cross-reference each other, which is D-013's shape rather than an accident.

| Pair | Longest shared run, before | After | What remains |
|---|---|---|---|
| `03_10.tex:23` / `09_01_05.tex:3` | **11 words** — *it cannot contest it and in most cases will never learn* | **5** | *it and in most cases* — function words |
| `03_09.tex:22` / `09_01_05.tex:23` | **13 words** — *wrong in the same direction on every occasion it is wrong at all* | **5** | *one bearer deployed at scale* — the term of art both sections need |

A **third** occurrence of the uniform-error argument was found at `08_03_04.tex:19`. It cites §9.1.5
and applies the argument to correlated bearer exit rather than restating it, so it is the shape D-013
asks for and was **left alone**.

## What was not done

- **No new cross-references anywhere.** Count unchanged at 230, verified.
- **Four of the five publication sites left uncaveated** — `03_03.tex:19`, `03_05.tex:48`,
  `03_10.tex:29`, `03_01.tex:7`. Caveating all five is a sweep, and D-044 records what a
  metric-driven sweep did to three arguments. §3.6 is the one that runs the enumeration. **Filed as
  Q-096.**
- **Chapter 12 and the glossary left alone.** `12_03.tex:7` is the book's last word on the floor and
  names no legitimacy cost; `13.tex:17` (*bearer*) and `13.tex:26` (*floor*) cite §3.1 and §3.10 and
  never §9.1.5. **Filed as Q-097.**
- **Q-068 not answered**; **`03_01.tex:23`'s four threads stay four.**
- **§3.10 and §3.6 were read whole. §3.9 and chapter 1 were read whole** — chapter 1 is 610 words.
  §9.1.5 was read whole as the comparison text. The other sections named in the tables above were read
  only at the lines quoted.

## Three defects in my own drafting, found on the second read

None of these were caught by the suite, the build, or the run check. All three are in text written
during this pass.

- **`ch01/01.tex`** — *"nobody outside that building was asked."* **That building** has no
  antecedent: the sentence's subject is a *builder*, a party, and the noun *building* arrives as a
  pun the reader has to decode, which is what style.md §7 rules against. Changed to *the laboratory*,
  which is the book's own word for that party at `03_10.tex:23`.
- **`ch03/03_09.tex`** — *"a single error reaches all of them … parties that reached it separately"*
  used **reaches / reached** in two different senses one clause apart, and the second *it* had two
  candidate antecedents. Rewritten as *"a single error in that reading reaches all of them in
  identical form, the instances being copies rather than independent judgments that converged."* An
  earlier draft of the same sentence had put *mistaken* three times in one clause and was rewritten
  before anything else was run.
- **`ch03/03_10.tex`** — the first version made the court analogy *be* the worse-option verdict:
  *"the case for a court that holds a right against an elected majority — which says only that the
  alternative is worse."* That misreports §9.1.5, whose structure is Waldron's objection, a
  conditional reply, and then the worse-option argument as what survives at its strongest. The
  analogy is contested where it is made; saying it *only* amounts to the worse-option argument
  flattens the section it is importing from. Rewritten to carry both.

## Verification

- Verbatim-run check of all four new passages against every line of all 133 sections at 6, 7 and 8
  words: **0 runs shared with any other section.** This is the check P126 exists because of.
- Both repaired pairs re-measured; the numbers are in the table above, not asserted as fixed.
- `refresh_order_shas.py`: 4 of 133 rows refreshed. `check_all.sh`: **ALL CHECKS PASSED**.
- `grep -rn textit manuscript/sections`: **0**.
- `build_tex.sh` into the scratchpad: **196 pages, 0 undefined references and citations, 0 `??` in the
  text layer**.
- Reference count 230 before and after.

## Figures

133 sections, 4 changed. 98,608 → **98,733 words** (+125). 196 pages, unchanged. 230
cross-references, unchanged. 0 bibliography entries added. Suite green.
