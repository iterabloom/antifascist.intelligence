# P157 — the front matter replaced with the author's Foreword, and the vendor disclosure moved to the criticism

Author instruction: replace the front matter with a supplied Foreword, with four
corrections named in the same message — *genocide* → *war crimes in Gaza and
Iran*, *Foreward* → *Foreword*, the straight quotes fixed, and the missing *of*
supplied. And a ruling on the finding P157 put to him: **the Anthropic
disclosure may sit in place at the first mention of the criticism** rather than
in the front matter.

## What went in

`ch00/00.tex` is the author's text with the four corrections applied. The
chapter keeps `\unnumberedlabel{sec:0}{0}`; nothing in the manuscript references
`sec:0`, checked. 455 words to 184.

One correction beyond the four, in the same phrase as the *of*: **loosely-related
→ loosely related.** An `-ly` adverb takes no hyphen before the adjective it
modifies. It is recorded here rather than assumed because the instruction named
the *of* and not the hyphen.

## The disclosure's new site, which is not where the note said to look

The removed paragraph named three sites: chapter~6, §10.3, and chapter~3. **The
first mention of the criticism is §3.3, not §3.6.** §3.3 `:10` introduces
Anthropic's published constitution neutrally, as an instance of the maintained
justification the section is describing; `:14` is where the book turns on it —
*it is this book's argument set down by a developer about its own product*, then
the finding that ranking broadly safe above broadly ethical takes back the
concession. §3.6 `:46`, the Palantir deployment, is the sharper case and it
comes later.

The disclosure went into `:14`, immediately after the sentence that names the
developer and before the reading begins. **A reader meets the conflict before
the criticism, not after it.** The wording is the author's own from the removed
paragraph, carried over rather than redrafted: *I wrote this book with that
developer's model, so the book criticizes, by name, the company whose product
helped assemble it.*

## One defect that was already there

`07_04.tex:34` read *This text was written with a model made by a company the
book criticizes, and the appendix on method sets out how.* **The chapter has not
been an appendix since D-224 (P124) moved it to the front**, so the pointer has
been stale for thirty-three passes, and the Foreword does not set out the method
either. The clause is removed; the sentence states the disclosure itself, which
is what D-140 repaired it to do.

**No tool in the suite reaches this.** The sentence carries no `\ref`, which is
the blind spot D-140 recorded when it made the move in the other direction. It
was found by grepping the prose for *appendix*, and that grep now returns one
hit, `06_01_01.tex:13`, which is about training data and not this chapter.

## What the Foreword claims, measured against the book

*Racial capitalism* is chapter~6's own term, at `06.tex:18`. **Gaza and Iran are
both in the book**: §6.4.1's box on the Israeli campaign carries Habsora,
Lavender and the 37,000 figure, §10.6 reads the same case, and the 2026 Iran
campaign is at §6.4.1 `:41` and §3.6 `:46`. **The phrase *war crimes* appears
nowhere in the manuscript** — §10.3 goes as far as command responsibility under
international criminal law and stops. The Foreword characterizes the book in a
register the book does not use about itself. It is the author's, and it is
recorded rather than raised.

*Genocide*, which the instruction replaced, appeared nowhere in the manuscript
either.

## What is no longer in the book, and is Q-111

The removed paragraph carried the persona-device disclosure: *None of the named
people whose expertise those personas imitated wrote a word of it, reviewed it,
or knows it exists.* **The vendor half has a site and this half has none** —
it is about how the whole text was produced, so no single passage is its first
mention. The book now carries it nowhere; the README does, and the Foreword's
link reaches the README. **A reader with the PDF and no browser does not meet
it.** Q-111 puts the options.

## Figures

133 sections, 3 changed. 99,568 → 99,319 words, −249: ch0 −262, ch3 +21, ch7 −8.
**231 → 228 cross-references**, the three being ch00's own to `sec:6`, `sec:10.3`
and `sec:3`; none added. 324 bibliography entries unchanged. **196 pages
unchanged.** Suite green. Scratchpad build: 196 pages, 0 undefined references and
citations, the Foreword and the disclosure both read back out of `pdftotext` in
position, the running head set from `\backmattermark{Foreword}`.

The proof pair is not rebuilt and is one pass stale.
