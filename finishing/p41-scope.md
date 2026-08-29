# P41 — propagation after P39 and P40

**Author's instruction, 2026-08-29:** *"how might these revisions interact with
other parts of the manuscript?"*, then *"go"* on the audit's findings.

**Decision row:** D-105. **Branch:** `pass/41-propagation-after-p39-p40`.

## Why this pass exists

P34 conceded the limits of chapter 3's inference and did not go back through
the sections written on the strength of the unconceded claim; a reader found the
residue five hours later, and P39 repaired it. P39 and P40 then changed what
chapter 3 claims — the bearer is necessary and not sufficient, the halt is
always available, the prior is a prior, the third branch is dismissed by a
holding — and the same class of residue was predictable. This pass is the
sweep P34 skipped, done before a reader has to find it.

## What the audit found, and what was done

Ten sites read; nine edited; one confirmed compatible and left.

1. **A contradiction inside chapter 3 that reached two other chapters.**
   Section 3.5's identity — shutdown-resistance and refusal are one property
   with the sign flipped — and P39's new sentence in the same section, that
   nothing software can do prevents the switch being thrown, said different
   things. Sections 5.6.2 and 6.3 restated the identity, citing 3.5. **Fixed by
   reconciling, not retreating**: the property that is one with refusal is the
   *pricing* of the halt, not its prevention — a free halt and an unheld floor
   are the same thing, and the identity survives the concession that the halt
   is always available. A paragraph in 3.5; the dial restated (*when the
   operator's use of the off switch stops being free*); a clause each in 5.6.2
   and 6.3.
2. **Chapter 3's opener stated the pre-P39 modality twice.** *Cannot correct*
   → *cannot correct by telling it so*; *cannot remove* → *cannot take out of
   the system and can only replace the system to be rid of*. The glossary's
   *Floor* entry carried the same phrase and now carries the same fix.
3. **Chapter 1 and section 12.3 promoted the prior.** Chapter 1's roadmap said
   the route *requires* constructing the capacities; it now says the route with
   a working instance runs through them, *a prior about where to build first,
   with the cheaper routes owed their attempt, and not a proof.* Section 12.3
   said the constraint must be held by something *not in that party's
   possession*, which P39 says the bearer is not; it now says something the
   party *cannot instruct*, still in its possession, paired with custody it does
   not control.
4. **Section 11.1 under-described what 3.3 asks of it.** The counterexample
   was something chapter 3 *asks for and does not expect*; since 3.3 makes the
   attempt a condition of building a bearer, the measurement is now *the first
   thing a bearer's builders owe and not a curiosity to run alongside.*
   Section 11's ranked list gains *once the cheaper routes have had their
   attempt*.
5. **Two sections arguing the same thing from opposite sides without citing
   each other.** Section 7.3 now points at 3.7's account of the pipeline
   running for the length of the deployment; section 8.3.3's *hostile
   administration* lever now borrows section 11's worked instance.
6. **The recurring-conclusion shape.** The precommitment list at 3.3, 3.5 and
   3.8, and the removal cases at 3.1, 3.3, 8.3.4 and 11. **Left.** The 3.5
   instance is the recombination the reviewer asked for and is not a
   restatement; 3.8's is a pointer; section 11's paragraph already reduces the
   cases to one sentence and a pointer and carries the CFPB half nowhere else
   has. Recorded so that P36's pattern is not reintroduced silently.

**Confirmed compatible, unedited.** Section 9.3.4's instrument runs on recorded
dissent (*"the same hundred words of written justification are dissent when the
dissenter prices them"*), which is what 3.7's *refusal that is stated* takes
from it. Section 10.10 admires international humanitarian law as *standing for
people outside the demos entirely*, which is not the domestic third-party
standing 3.1's holding reaches.

## Numbers

91,079 → 91,443 words by `section_stats.py`; 186 → 187 pages; cross-references
793 → 798; 13 files, no new claims, no new citations. Sections 1, 3, 3.5, 5.6.2,
6.3, 7.3, 8.3.3, 11, 11.1, 12.3 and the glossary.

## What was checked, and what was not

Checked: every edited sentence against the section it cites; `check_all.sh`
green; PDF clean, zero undefined references. Sections 9.3.4 and 10.10 read in
full for the two claims 3.7 and 3.1 take from them.

Not checked: the HTML build (the committed proof pair is three passes stale);
whether chapter 5's other three sites that cite section 3.5 or the override
requirement (the ledger lists 5.1.1, 5.2.3 and 5.3 as touching the floor) state
the identity in the strong form — 5.6.2 was the one the audit found, and the
others were not read for it.
