# P79 — the self-locating cross-reference cut where the paragraph does not need it

**The author's finding.** 421 numbered cross-references plus 234 instances of
*this book*, *this chapter*, *this section* — one act of self-locating every ~147
words. Much of it is load-bearing, and a large fraction is defensive: an objection
is reported as handled elsewhere before any reader would have raised it. **The tell
offered: a cross-reference appearing mid-sentence in a paragraph making an unrelated
point.** The proposed remedy: drop all of them.

**The diagnosis holds and names a class no tool here reaches. The tell selects about
ten times what it describes**, because its first half is mechanical and its second
half is the whole discrimination.

## The figures

| | the finding | measured |
|---|---|---|
| numbered cross-references | 421 | **431** body (463 total, less 30 glossary and 2 appendix) |
| *this book / chapter / section* | 234 | **253** — book 132, chapter 75, section 46 |
| one self-location every | ~147 words | **133 words** |
| chapter 3 pointed at | 48 | **50** chapter-level, **95** with its sections, plus 15 from inside |
| §3.9 | 20 refs / 2,188 w | **19 / 1,958** |
| §7.4 | 16 / 1,717 | **12 / 1,444** |
| §10.6 | 15 / 2,090 | **5 / 715** |

**The 48 is the chapter-level count and it is right.** The book points at chapter~3
nearly twice that often once its sections are counted, and that is the figure a
density question should use.

**§10.6 does not reproduce and was not silently rounded to something that would.**
That file has held 4–5 references and 717–910 words in every commit since it was
created at the P32 split; no state of it has ever been near 15 in 2,090. The nearest
live sections are §11.2 (18 in 2,583) and §3.8 (11 in 2,114). **Left open rather than
guessed at.**

## The instrument, and why it over-selects

Mid-sentence position is mechanical and was measured: **226 of the 431 body
references, 52 percent.**

**A first measurement said 86 percent and was wrong.** `section~\ref{sec:X}` renders
as the word *section* followed by the number, so a classifier reading rendered prose
sees text before every reference and calls all of them mid-sentence. Corrected by
treating the naming noun as part of the reference span. **A position classifier that
finds no sentence-initial references in a book full of them has found a bug, not a
result.**

At 226, dropping all of them is a larger cut than P53's 252-of-848 and it lands on
the class three passes have read and kept: `xref_shapes.py` puts **333 of 426**
prose references in `inline`, where the reference is a term in the sentence, against
**48** in every removable shape combined.

**Position is not the discriminator; the paragraph is.** §3.9's *the test stated in
section~3.3 comes back positive* is mid-sentence and the sentence collapses without
it. §10.6's *which chapter~12 also cites* is mid-sentence and contributes nothing to
a paragraph about what makes democracy valuable.

## The reading

**All 226 were read against the second condition.** Nine sites where the paragraph's
point survives the pointer's removal, 22 reference instances — about 1 in 20. Five
further sites were reported as borderline and the author ruled them in, taking the
pass to **14 sites and 28 instances**.

| site | what went |
|---|---|
| §2.1.2 | *Section 6.4.2 and chapters 8 and 9 are where each is worked out* — the sentence before it already says *each priced elsewhere* |
| §5.6.2 | *Chapters 8 through 10 work out what each of those safeguards costs* — between the safeguard list and the paragraph's own observation |
| §6.3 | *which is the subject of chapters 8 through 10 rather than of this one* — scope disclaimer |
| §6.3.4 | *chapters 9 and 10 catalog* and the appended *(section 9.1, section 10.4)* |
| §6.4.4 | the section-opening filing sentence; the three attack surfaces restate in the sentence after it |
| §9.3.5 | *— sections 9.3.1 through 9.3.4 —*, appended to a sentence that already names all three |
| §10.4 | *Section 6.4.1 names six documented forms … and section 6.4.3 the policy levers* |
| §10.6 | *which chapter 12 also cites* |
| §11.6 | *is section 6.2's territory and section 11.1's* — scope disclaimer |
| §3.1 | *section 3.3 is where the exits are* — reader-service signpost (borderline) |
| §11 | *should turn to section 11.6, which says why it could start today* (borderline) |
| §9.3.1 | *Section 2.3.2 already specified its composition* (borderline) |
| §9.3.4 | *Section 9.3.2 already named the substantive standard* (borderline) |
| §11.4 | *Section 2.1.1 covers … and section 4.2.2 already names reward hacking* (borderline) |

## Six of the fourteen could not be cut clean

**The sentence after the pointer depended on it** — P68, P69 and P70's class, and
it was checked at every site before anything was removed.

- **§6.4.4** opened on the filing sentence, and the *However* following it named
  *a rescue robot* whose antecedent was the filed section. Recast to
  *out-coordinate a set of cooperating systems*; no claim moved.
- **§10.4** left *those levers* pointing at nothing. Repaired to *the room left by
  the policy levers available against authoritarian AI misuse*.
- **§9.3.1** left *What that section left open* naming a section no longer there.
  Repaired to *What that leaves open*.
- **§11.4** left *What neither asks* with nothing to count. The two problems are now
  stated rather than filed.
- **§9.3.1** and **§9.3.4** carried content inside the filing — a board's composition
  and a substantive standard — so the pointer went and the content stayed.

**Nothing was orphaned.** No `\autocite` sits in any removed span, `refs.bib` is
unchanged at 300, and no section lost its only inbound pointer. §11.6 keeps two
inbound references from chapter~11's own opener; **the sentence cut there was the
second of two saying §11.6 could start today**, so the cut removes a repetition
inside one section — P71's class — as well as a signpost.

## The class no tool in the suite reaches

**Ten of the eleven candidate sites are `inline` in `xref_shapes.py`**, its keep
class, described there as *reference is a term in the sentence and no tool reaches
it*. Only §10.4's was flagged, as `signpost`.

Everything about these resolves and is well formed. What is wrong is the sentence's
relation to its own paragraph. **It is adjacent to P75's class and not the same one**:
P75's is prose stating a reason that is false, and this is prose stating a true thing
the paragraph did not need. Both are defects in what a sentence claims about the
surrounding text rather than about the world, and neither is reachable by a check that
verifies references resolve.

## The self-location half, measured and not cut

**The proposed remedy does not reach the 253 phrases**, and the cut confirms it: 28
references came out and the self-location count did not move.

| shape | n | book / chapter / section |
|---|---|---|
| other | 97 | 46 / 30 / 21 |
| stance — *this book declines*, *does not take a system's word* | 54 | 38 / 11 / 5 |
| locative — *nothing in this book closes it* | 43 | 23 / 15 / 5 |
| possessive — *this chapter's argument* | 39 | 18 / 11 / 10 |
| narration — *this chapter opened with*, *has been asking for its whole length* | 20 | 7 / 8 / 5 |

**`narration` is the removable class and it is 20 of 253.** The other four scope a
claim or make one. Chapter~3 carries the density: §3.5 one per 187 words, §3.9 one
per 150, §3.1 one per 117, §3.2 one per 131, with §7.4 at one per 111.

**Two instances of a class D-099 recorded as cleared are back**, both in §3.5:
*the question this section used to open with* and *this section used to rest on it
as though it were*. P35 cleared four; §3.5 was rewritten at P57 and the tic returned
with the rewrite. **Revision history visible to a reader who has no access to the old
draft** — the same thing P7 cut from chapter~2's opener. Nothing in `check_all.sh`
looks for it.

## Measurements

| | before | after |
|---|---|---|
| body cross-references | 431 | **403** |
| mid-sentence share | 52.4% | **51.9%** |
| *this book / chapter / section* | 253 | **253** |
| book | 90,981 | **90,795 words**, down 186 |
| pages | 182 | **182** |
| sections · `refs.bib` | 136 · 300 | **unchanged** |

`check_all.sh` green after `refresh_order_shas.py`; 0 undefined references and 0
undefined citations.

## What this pass did not do

**The 209 mid-sentence references left standing were read and kept**, not skipped.
They are the `inline` class, where the reference is a term in the sentence.

**That does not mean every one of them needs a rewrite, and the claim was checked
rather than inherited.** About **34 sentences** carry the reference as a deletable
modifier — *the sources section~6.1.1 describes*, *the board section~2.3.2
describes*, *the methods chapter~4 describes* — where striking the pointer leaves a
grammatical sentence. On a 14-sentence read, **8 delete clean and 6 do not**: *the
counterexample chapter~3 asks for*, *built the way chapter~5 describes*, *for the
reasons section~9.1.2 sets out* and *at the price section~3.9 sets out* all leave a
noun phrase with nothing in it. So the mechanically-deletable population is on the
order of **20 references, not zero** — and not the 226 the tell selected either.

**The phrasing was inherited and had not been re-checked since it was written.**
P53 wrote *cutting it means rewriting the sentence, which is what this pass did* —
a description of the method the author had ruled for that pass, restate then cut.
P57 carried it over as *removing it means rewriting the claim*, now a general
statement about the class, and this pass repeated it before testing it. **A sentence
describing what one pass chose to do becomes, two passes later, a claim about what
is possible.**

**Deleting clean as grammar is not the same as the claim surviving.** In all eight,
the pointer was carrying *which* — which sources, which board, which removal cases —
and the sentence after the deletion says something true and vaguer. **The edit is
mechanical; the decision to make it is not**, which is the same place P53 and P57
stopped.

**No self-location phrase was cut.** The census above is the whole of the work on
that half, by the author's ruling, and the ruling on what to do with the 20
`narration` instances is open as Q-061.

**The proof pair is stale after this pass**, having been rebuilt at P78; its page
figure of 182 still matches.
