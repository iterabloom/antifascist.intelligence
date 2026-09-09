# P147 — §9.1.5's update-channel close, split so the trade-off is the finding

Author note: the paragraph's last sentence carries two claims, the second
rescues the first and reads as a concessive tail, and the section's close has
enough genuine unanswered items that this one should not be mistaken for
another.

## The reading holds, and the risk the note names is measurable

`09_01_05.tex:37` ended:

> No version of this procedure closes that, and one that did would be a procedure
> under which no deployment could be corrected at all.

**The section's close really is dense with items that are open**, and each is
marked as open in the text: `:35`'s *What it cannot have is an account of who
decides which is which*; `:39`'s *untouched, and stands above as unanswered*;
`:41`'s *not a grant of standing*. Two more sit earlier — `:26`'s *which this book
does not specify for the floor* and `:28`'s *which nothing above prices*. **A flat
sentence saying no version of the procedure closes something is the same shape as
five neighbours that mean it.**

## Why the split alone would have made it worse, which is the departure

A pure split gives *No version of this procedure closes that.* as a standalone
sentence. **Standing alone it is more confusable with those five, not less** — the
rescue that follows is a separate sentence a reader meets afterwards, and the
paragraph would have handed them the admission first with nothing marking it.

**So the order is reversed as well as split**, which is a step past the
instruction and the reason is the instruction's own purpose. The cost leads; the
admission follows as its consequence and is named as a price in the same breath:

> A procedure that shut the channel would be one under which no deployment could
> be corrected at all. So no version of this procedure closes it, and the exposure
> is the price of every correction the procedure exists to make.

**Both claims survive as claims.** Neither is a tail.

## Two drafting constraints

**No antithesis was added, and `:37` is the reason it mattered.** The obvious
wordings — *a trade-off rather than a gap*, *a price and not an item left open* —
are `antithesis.py`'s `rather-than` and `and-not`. **`:37` carries none of the
section's eight instances**, so an addition there would have been the paragraph's
first. The count is unchanged at 8, and clusters at 0.

**The paragraph's own noun replaced a repeated one.** The first draft read *A
procedure that closed that route*, four words after *by the same route* ending the
sentence before. *The channel* is the term `:37` establishes itself — *the
amendment procedure is also an update channel* — so it names the antecedent
without the echo.

## What was not done

**The mechanism was not restated.** *Whatever makes public amendment possible
makes silent amendment possible by the same route* already stands two sentences
earlier, and it is the balanced parallel `style.md` §7 warns about. A second one
underneath it would have doubled the shape.

**Nothing else in the close was touched.** The five genuinely open items are open
and are left saying so.

## Verification

Suite green. `refresh_order_shas.py` run after each draft. Scratchpad lualatex
build: **196 pages, 0 undefined references and 0 undefined citations**; the
passage reads back out of `pdftotext` in position, and `:39` and `:41` were both
checked present in the PDF after it.

§9.1.5's censuses are unchanged against HEAD: **8 antithesis sentences, 0
clusters, 7 `deixis --hard` hits.** **0 new shared six-word runs**, 1,622
book-wide before and after.

## Figures

133 sections, **1 changed**. 99,408 → **99,424** words (+16); §9.1.5 1,923 → 1,939.
**196 pages unchanged.** **233 cross-references unchanged.** 324 bibliography
entries unchanged. 0 `\textit`.
