# P142 — the session's six added cross-references judged by the reader, and five removed

The author asked whether each cross-reference added this session makes the
manuscript more or less reader-friendly, and where the answer is less, to remove
it **and** make the passage better in the same edit.

**Five removed, one kept. 236 → 231.** This closes Q-105 by execution.

## The test applied

A cross-reference helps a reader when they can act on it — the target is
reachable, and following it repays the interruption. It costs a reader when it
interrupts something they are in the middle of to name a place they cannot use
yet. **Forward, deep, and mid-argument is the expensive combination; backward, at
a section head, is the cheap one.**

## The four verdicts

**1. §2.1.2 → §11.3 (P133). Removed.** A reader inside an enumerated definition
of the four features was sent nine chapters ahead, to a section that depends on
the apparatus of chapters 2, 3 and 7. Nothing there is usable at that moment. The
sentence's claim was already complete without it.

*What replaced it carries more:* **and those are the cases the word was coined to
name.** The limit now lands its own point — a drift-tuned instrument misses the
paradigm cases — instead of reporting where the limit recurs.

**2. §2.2.3 → §3.3 (P135). Removed.** The paragraph immediately above already
says chapter~3 *takes that burden up again and reduces it*. A subsection address
on top of that is navigation over navigation, and *names the measurements that
would* told the reader a place rather than a fact.

*What replaced it carries more:* **the kind of claim a measurement could
overturn**, as an appositive. The paragraph's job is to distinguish two kinds of
claim, and the halves now state the distinction in parallel — *a measurement
could overturn* against *no measurement reaches it*. **The pointer was standing
where the contrast should have been.**

**3. §2.2.3 → §3.3, §9.3.2, §12.2.1 (P136). All three removed.** Three addresses
in two sentences, to chapters 3, 9 and 12, in the middle of chapter~2. This was
the worst of the six and the note that produced it says why: it asked that a
reader *know they have just met one of the book's two named alternatives to a
bearer*. **That is a point about significance, and it was delivered as three
section numbers.**

*What replaced it carries more:* **the first of the two constructions this book
asks to be built before anything that can be wronged is. Later chapters attach a
consequence to that, and a deployment that tried nothing has to say so.** The
significance is stated, and the consequence a reader would actually want —
`12_02_01.tex:6`'s *the answer "nothing was tried" is itself a finding* — is
stated with it. **Q-104 governed the drafting: the milestone formula is already
written out three times with twelve words verbatim, and this does not make a
fourth.**

**4. §5.2 → §2.2.1 (P137). Kept, and it is the one that helps.** Backward, at a
section head, which is a pause rather than an interruption; and it repairs a
gesture the text was already making and failing to complete — *has already been
covered*, pointing nowhere. **§2.2.1 had zero inbound references and two sections
lean on it.** A reader told something was covered and not told where has been
teased; this is the fix for that, not an instance of the problem.

## Where each section lands

| section | before the session | after P141 | now |
|---|---|---|---|
| §2.1.2 | 2 | 3 | **2** |
| §2.2.3 | 2 | 6 | **2** |
| §5.2 | 0 | 1 | **1** |
| book | 230 | 236 | **231** |

**The net of ten passes is one cross-reference, and it is a backward one into a
section that had none.**

## What this makes more urgent, not less

**Q-101.** §11.3 builds its whole longitudinal requirement on drift and never
states that a party which announces its myth escapes a slope. Until this pass,
§2.1.2 at least pointed at the inheritance. **Now nothing in the book connects
them**, and Q-101's option (b) — one sentence at `11_03.tex:11`, no
cross-reference, in the section that would be built on — is the only remaining
route. The default there was *leave it*; that default is worth revisiting on the
strength of this pass rather than despite it.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
all three rewritten passages read back out of `pdftotext`. New text checked at 6,
7 and 8 words against every line of the other 132 sections: **0 shared runs**,
after clearing one six-word function-word collision with §3.3 (*and it is the
kind of*) by making the clause an appositive.

## Figures

133 sections, **2 changed**. 99,348 → **99,318** words (−30); §2.1.2 2,631 →
2,625, §2.2.3 1,132 → 1,108. **196 pages unchanged.** 236 → **231**
cross-references. 324 bibliography entries unchanged. 0 `\textit`. **The proof
pair was not rebuilt and is now ten passes stale.**
