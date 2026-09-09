# P152 — Q-107 closed on option (c), and what (c) could not deliver

Author ruling on Q-107: **"try it."** Option (c) was the concrete, categorical
image rebuilt without the dependency that forced P138's cut.

## The edit

`02_03_01.tex:13` ended on the abstract replacement P138 wrote — *a concept whose
precondition is missing does not apply in a weaker form.* It now ends:

> The self it requires is not there, and a system with no biography to lose is in a
> different state from one with little to lose.

**It needs nothing that was cut.** *Biography* is §2.3.1's own word, at `:16` and
`:28`, and *anything to lose* is `:38`'s. The paragraph's own *Suffering is not
merely hard for such a system to reach* still sets it up.

## What (c) could not deliver, and the reason is structural

**I could not rebuild a physical scene.** The original was *A hull that draws more
water than there is does not float badly; it is aground*, and every physical
version I drafted landed on one of the two shapes `style.md` rules against:

- *A bridge with no far bank is not a short bridge* — §2's contrastive frame, and
  `antithesis.py`'s `is-not-a`.
- *A door with no lock is not locked lightly* — the same.
- Anything balanced enough to be vivid is §7's two-clause epigram, which *asks to
  be admired before it is checked*.

**That is why the original carried both shapes at once.** The vividness came from
the contrast, and the contrast is the banned construction. **The claim resists a
scene; it does not resist concreteness.** What went in is a quantity contrast
anchored to a concrete noun — nothing to lose against little to lose — which is the
barest and most checkable form of the claim and is duller than what it replaces.
`style.md` §7 asks for exactly that trade: *Write the declarative sentence instead,
even where it is duller.*

**If the physical image is wanted back, it means accepting one of those two shapes
for this sentence.** That is a ruling, not a drafting problem, and it is not filed
as a question because Q-107 has just been ruled on.

## Two images rejected on collision, checked before drafting

**The water family stays out.** §3.4 owns it under D-238, and reintroducing *hull*
or *aground* would undo the pass this one follows from.

**`dial` is unavailable.** It has **12 uses** in the manuscript and a settled sense
— §3.5's and §3.6's *where on that dial to stand*, the graduated refusal setting,
and §6.2's *not two settings of one dial*. A new sense here, degrees of a concept's
applicability, would collide with a load-bearing one. *Threshold* was considered and
dropped for the same reason, §3.3's threshold scheme being a term of art.

## Record repair: P138's measurement was wrong

P138 recorded **"Zero occurrences of *water*, *depth*, *shallow*, *deep*, *hull*,
*afloat* or *aground* remain in §2.3.1, checked after the edit."** **Six of the
seven are zero. *deep* is one**, at `:38` — *how deep in that range the system sits*
— and it was present before P133, so the pass reported zero for a word it had not
removed and had not needed to.

**The prose is left alone** and the record is corrected instead. `:38`'s *deep* is
position in an ordering, which is how §3.2 `:11` uses *depths* for the same axis,
and not the hull scene §3.4 owns. **What P138 was entitled to claim is six of
seven.**

## Verification

Suite green. `refresh_order_shas.py` run. Scratchpad lualatex build: **196 pages, 0
undefined references and 0 undefined citations**; the sentence reads back out of
`pdftotext` in position.

§2.3.1's censuses are unchanged against HEAD: **11 antithesis sentences, 3 clusters,
4 `deixis --hard` hits** — the replacement carries none of the banned shapes, which
was the constraint it was drafted under. **0 new shared six-word runs**, 1,622
book-wide before and after. Water vocabulary in §2.3.1: **0 of six, plus the
pre-existing *deep*.**

## Figures

133 sections, **1 changed**. 99,542 → **99,547** words (+5); §2.3.1 1,865 → 1,870.
**196 pages unchanged.** **231 cross-references unchanged.** 324 bibliography
entries unchanged. 0 `\textit`.
