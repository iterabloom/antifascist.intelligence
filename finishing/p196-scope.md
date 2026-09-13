# P196 — the Foreword replaced, and its one figure corrected against the book

The author supplied a complete replacement Foreword and asked for it to go in
whole. It is in. **176 → 249 words**, six paragraphs for the previous seven, and
the book is 156 pages either way.

**One thing in the supplied text was checked rather than typed, and the author
ruled on it.** The rest went in as written, with two mechanical conventions
applied.

## The figure

The supplied text read *a weapons targeting pipeline running at thirteen thousand
names in thirty-eight days*. **Neither number is in the book or in its source.**

- **§6.3.1 says 37,000**: *Lavender scored individuals by estimated likelihood of
  militant affiliation and produced kill lists; as many as 37,000 Palestinians
  were marked*, citing `abraham2024lavender`, whose own `note` field carries the
  same figure.
- **The source says 37,000 over the first weeks.** Abraham's +972/Local Call
  investigation reports as many as 37,000 marked during the first weeks of the
  war, reported elsewhere as the first six.
- **No reporting gives 13,000, and none gives a 38-day window.** Two searches,
  one on the Lavender figure and one on the pairing itself, returned the same
  cluster of figures every time: 37,000 marked, about ten percent error, Habsora
  at up to 100 targets a day against roughly 50 a year before it, more than 1,500
  targets struck in the first month.

**Put to the author with the evidence and the alternatives; he chose the book's
own figure.** The clause reads *a weapons targeting pipeline that marked
thirty-seven thousand names*. **The day-count is gone rather than corrected**,
because the book states no window at §6.3.1 and adding one to the Foreword alone
would have opened the same gap from the other side.

## Two mechanical conventions applied

**`Chapter 7` became `Chapter~\ref{sec:7}`.** Required, not preferred:
`check_xrefs.py`'s `BARE` rule matches `[Cc]hapters?\s*\d`, so the literal number
fails the suite and therefore the pre-commit hook. `Chapter~\ref{sec:7}` is the
book's established form for a sentence-initial chapter reference — 33 instances
across the manuscript, 6 of them to chapter~7 — and it prints *Chapter 7*.

**A spaced hyphen became an em dash.** *raising a child - in other words* now
carries `—`, which is `style.md` §8. **Nothing in the suite would have caught
it**: `check_typography.py` tests for `--` and `---`, and a lone spaced hyphen is
neither. It would have printed as a hyphen where the sentence wants a dash.

## What was checked and holds

**The chapter~7 claim.** The Foreword says chapter~7 runs the book's definition of
fascism on three things. All three are there: §7.1 on the labeling pipeline and
§7.2 on RLHF for the machinery, §7.4 on the field — *Alignment and AI ethics are,
among other things, a channel through which objections to what is being built are
solicited, funded, published, and answered* — and §7.4 again on the book itself,
at `:34`: *This text was written with a model made by a company the book
criticizes.*

**The arithmetic.** *the other eleven chapters* is right. The book has twelve
numbered chapters, 1 through 12; the Foreword is unnumbered and chapter~13 is the
glossary.

**`\url` resolves.** `hyperref` is loaded in `preamble.tex` and the link sets in
monospace on the page.

## What the replacement dropped

The thought-experiment opening — *Is it possible to write something that literally
nobody agrees with?* — the audience-annoying framing, *You hold the result*, and
the line about the first draft having been about prompting strategies. **Gaza and
Iran are no longer named in the front matter**; §6.3.1 and §6.3.2 still name both.

**The caps opening went with it and was not reproduced.** The old text began
*THIS BOOK began*, and `00.tex` was **the only file in the manuscript** that
opened that way — no other chapter does — so the styling was a one-off rather
than a convention the new text should inherit. It was left off.

## Q-111, which this bears on without settling

Q-111 records that the persona-device disclosure has no site in the book: it is
about how the whole text was produced, so no passage is its first mention, and
the README carries it while the book does not. **The new Foreword does not change
that and slightly weakens the pointer.** The old text said *My first draft of this
foreword was all about the different strategies I used to prompt LLMs to generate
the text*, which at least gestured at method; the new one says *I used LLMs
extensively in writing this book* and gives the repository link. **The device —
models prompted to write as named real people — is still named nowhere in the
book.** D-008 originally called for a note that names it. **Q-111 stays open**,
and this is now the passage a ruling on it would edit.

## Measured

**91 sections, 74,681 words** (74,608 before, +73, all of it chapter~0's 176 →
249), **156 pages**, 256 cross-references against 91 labels, 227 entries all
cited, **0 undefined references and 0 undefined citations**, suite green. The page
was rasterized and read.

## What was not done

**No other file was touched.** The Foreword's claims were checked against
chapters~6 and~7 and its figure against §6.3.1, and nothing else in the book was
re-read against the new front matter.
