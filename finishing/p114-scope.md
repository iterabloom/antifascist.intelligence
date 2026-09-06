# P114 — the chapter 1 epigraph moved from the third stanza to the first two

**The instruction.** One finding, stated by the author: the epigraph went from three stanzas to
one in a recent commit, and the stanza it kept is the wrong one — the first two should stand
instead.

## What was done

`manuscript/sections/ch01/01.tex:3-11`. The third stanza is out and the first two are in, restored
byte-for-byte as they stood before P111 cut them, line breaks and the `(ha)` included. The
attribution block, the `verse` environment and everything below the epigraph are untouched.

The taking goes from 3 typeset lines to 6, and from 11 words to 25. It was 9 lines and 38 words
before P111. **The rights position is D-012 and has not changed**: the epigraph is the author's
accepted risk, recorded rather than re-argued, and the third-party carve-out P111 put on the title
page (`preamble.tex:75`) and in `README.md:47` already names the chapter 1 epigraph and covers a
longer quotation without amendment.

**The transcription was not checked and did not need to be.** A check was started and the author
stopped it — *i checked them you dont need to* — so the two stanzas stand as the author has them.

## What the swap costs and what it buys

P111 kept the third stanza on the reasoning that it *lands directly on the sentence it was always
answering*, that sentence being the chapter's first: *Intellect estranged from compassion
characterizes many of the twentieth century's worst actors.* The third stanza carries the
trampling; the first two carry the estrangement itself, smart set against heart, and they carry it
in the first person as something the speaker got wrong and revised. The opening sentence names
both halves of the split, so it is answered either way; what changes is that the epigraph now
states the book's own move — build the heart in — rather than the damage the book is against.

**What is lost is the word the chapter's first sentence picks up.** Nothing on the page depends on
it: no cross-reference, no callback, and no later section quotes or glosses the epigraph. Chapter
6's two references to *the epigraph* are to chapter 6's own, a different quotation.

## What this closes

**One of P111's two unasked changes is moot.** The lowercase *i've* corrected to *I've* was
reported as a change the author did not ask for and has stood unruled in `QUESTIONS.md` since;
the stanza carrying it is off the page, so there is nothing left to rule on. The other unasked
change, the carve-out added to `README.md` as well as the title page, still stands and is now
load-bearing for a longer quotation than the one it was written for.

## Checks

`check_all.sh` failed once on the expected row — `ORDER.tsv`'s sha256 for `01.tex` — and
`refresh_order_shas.py` cleared it; green after. The PDF was built and page 6 rendered to an image
to confirm the stanza break prints: it does, at `verse`'s stanza spacing, with the attribution
below it unmoved.

**Nothing the book measures moved.** 137 sections, 88,310 words, 180 pages, 18 overfull boxes, 0
undefined references — every figure identical to P113's, `section_stats.tsv` byte-identical after
regeneration, because the word count does not read the `verse` environment. Chapter 1 is 709 words
before and after.

## What was not done

**The proof pair was not rebuilt** and `finishing/reports/whole-book-proof_2026-09-06.{pdf,html}`
still carry the third stanza. They are one page-6 image apart from the tree and stale in that one
place until somebody makes the proofs.

Nobody has read chapter 1 end to end since the swap.
