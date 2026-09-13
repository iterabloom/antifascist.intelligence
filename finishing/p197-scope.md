# P197 — D-297's figure finding withdrawn, and the author's text restored

**P196's central finding was wrong.** It reported that the Foreword's *thirteen
thousand names in thirty-eight days* was unsupported and contradicted the book,
put that to the author with two alternatives, and applied the one he chose. **The
figure was exact, the book states it twice, and the clause is restored as he
wrote it.**

## What the book actually says

- **§6.3.1 `:60`** — *Thirty-eight days in, the figure given by the Pentagon's
  chief digital and artificial intelligence officer was thirteen thousand
  targets, with peak consumption around twenty billion tokens a day*
  \autocite{breakingdefense2026maven}.
- **§3.6 `:68`** — *Reporting on the 2026 Iran campaign describes thirteen
  thousand targets in thirty-eight days, including more than a thousand in the
  first twenty-four hours, at roughly ten times the previous rate.*
- **`breakingdefense2026maven`'s own note** carries the quotation it comes from:
  *Operation Epic Fury leveraged Palantir's Maven Smart System in order to conduct
  strike missions across the entire battle space, 13,000 targets in 38 days* —
  Cameron Stanley, the Pentagon's CDAO, **verified 2026-09-07**.

Both numbers, in the book, twice, sourced and already verified.

## How the finding went wrong

**The first check found the passage and the output was truncated past the match.**
The grep was

```
grep -rn 'thirty-seven thousand\|37,000\|thirteen thousand\|13,000\|thirty-eight days\|38 days' \
     manuscript/sections/ | cut -c1-230
```

and it returned three hits, two of them the passages above. **`cut -c1-230` cut
each line before the matched text.** `06_03_01.tex:60` displayed as far as *More
than one thousand targets were struck* and stopped; `03_06.tex:68` stopped inside
the Anthropic sentence that opens it. What reached the eye was the third hit,
`06_03_01.tex:14`, the Lavender box and its 37,000 — a **different system, a
different war and a different unit of count** — and the finding was built on that
one.

**Everything after inherited the error.** Two web searches were run on Lavender
and Gaza, which is not what the Foreword's clause is about, and they returned
consistent Gaza figures that looked like confirmation. **The searches were sound
and aimed at the wrong subject.**

**The check that would have caught it costs nothing**: grep for the author's own
words without truncating, before deciding a claim is unsupported. `13,000 targets
in 38 days` is one string.

## What was restored, and what was not

The clause is **verbatim as supplied**: *a weapons targeting pipeline running at
thirteen thousand names in thirty-eight days*. The author's ruling in P196 was
given on a false premise and is not treated as a ruling on the restored text.

**Nothing else from P196 is disturbed.** The Foreword's other five paragraphs, the
`Chapter~\ref{sec:7}` conversion and the em dash all stand — those were checked
against the manuscript and the suite, not against the web, and they hold.

## One distinction, left for the author

**The sources and the book say *targets*; the Foreword says *names*.** In this
book that difference carries weight: §6.3.1 separates Habsora, which marks
buildings and structures, from Lavender, which marks people and puts them on a
kill list, and the Maven figure is a target count. **The Foreword's *names* reads
the count as people.** Whether that is the intended rhetorical move or a slip is
the author's to say, and **it was not changed** — P196 changed his words once
already on a finding that did not hold, and this pass is not doing it again on a
smaller one.

## Measured

**91 sections, 74,684 words**, **156 pages**, 256 cross-references against 91
labels, 227 entries all cited, **0 undefined references and 0 undefined
citations**, suite green. The word count differs from P196's 74,681 by 3, the
restored clause being that much longer than the substitute.

## What this says about the record

`DECISIONS.md` is append-only, so **D-297 stands as written and D-298 withdraws
its figure finding**, which is the form D-289 used for the same kind of error.
**`p196-scope.md` is left in place with its false finding intact** — it is the
record of what that pass did, and this file is the correction. A reader coming to
`p196-scope.md` cold will find the finding stated confidently and should read
this file next; the D-297 row now names D-298.
