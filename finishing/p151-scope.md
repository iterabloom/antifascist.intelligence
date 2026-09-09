# P151 — the session's two added cross-references judged by the reader, and both removed

Author instruction: review every cross-reference this session added, ask of each
whether it makes the manuscript more or less reader-friendly, and where less,
remove it and make the passage better in the same edit. **This is P142's
instruction applied to P144 through P150, and it closes Q-108 by execution.**

## What the session actually added, by diff and not from memory

**Two, both at P145, both in `03_03.tex:79`**: `\ref{sec:11.1}` and
`\ref{sec:11.2}`. 231 → 233.

Six of the seven commits show identical added and removed reference lists —
`\ref{sec:3.3}`, `\ref{sec:3.2}`, `\ref{sec:3}`, `\ref{sec:3.8}`,
`\ref{sec:4.2.8}`, `\ref{sec:11.2}` — because each was a reference carried along in
a rewritten line rather than a new one. **P149 added and removed none at all.**
Checked per commit rather than inferred from the totals.

## Both are less reader-friendly, and §3.3 itself is the proof

P142's test: a reference helps when the reader can act on it and costs when it
interrupts something they are in the middle of to name a place they cannot use
yet; **forward, deep and mid-argument is the expensive combination.** Both sat
inside the paragraph developing the middle conjunct, pointing eight chapters ahead.

**The decisive fact is local and I missed it at P145.** §3.3 gestures at chapter~11
twice without a number — `:75`'s *The near-term interpretability work is where that
measurement is set out* and `:81`'s *the apparatus the research chapter already
specifies*. **`:81` is two lines below the addition, in the same run-in head.** The
section had a settled idiom for this and P145 broke it against itself.

**§11.1's was the weaker of the two.** It read *section~\ref{sec:11.1} is where that
question is put* — and §3.3 had just put the question itself, in its own words. The
reference told a reader that a question they had just been given is asked again
later. Nothing to act on.

**§11.2's was the better one and still fails.** It named a real thing a reader does
not have — the experiment. But **the book already spends that address where a
reader is closer to needing it**, at `12_02_01.tex:15`, and §3.3's reader is
mid-induction with no use for it yet.

## What replaced them, which is the half the instruction requires

The pointers were standing in for *this is worked on later*. What a reader at `:79`
can actually use is which of the two routes has something behind it:

> The second is whether formation can be read off the artifact where provenance
> cannot be established, and it is the nearer of the two to a result: the research
> chapter states a test for it, and a negative one would close the route. Nothing
> comparable exists for reading the machinery, and neither is close to settled.

**That is a fact about the state of the two routes, and the numbers were not.** A
reader now learns the asymmetry: one route can be closed by a result, the other
waits on an instrument. Each half is sourced — `11_01.tex:22` ranks
formation-read-off *the nearest thing to a route*, `11_02.tex:60` gives the test and
says a negative result closes it, and `11_02.tex:46` has interpretability *further
from ready than its adjacency suggests*.

***The research chapter* is §3.3's own phrase**, from `:81`, so the replacement uses
the idiom the addition had broken.

**The experiment was deliberately not described.** Importing *take models whose
training is documented and ask whether a reader can recover their provenance* would
put a second instance of §11.2's specification into chapter~3, which is what D-013's
one-home rule exists to prevent. The passage says a test exists and what a negative
result would do, and no more.

**One pre-existing sentence was absorbed.** *Neither is close to settled.* now ends
the new sentence rather than standing alone; its *neither* still means the two
routes.

## What the net of this session is

**231, the count it started at.** Eight passes, two references added, both removed
on the reader test. **Across P142 and P151 the instruction has now been run twice
and removed seven of eight.** The one that survived P142 — §5.2 → §2.2.1, backward,
at a section head, into a section with no inbound references — remains the only
cross-reference either review kept.

## Verification

Suite green. `refresh_order_shas.py` run. Scratchpad lualatex build: **196 pages, 0
undefined references and 0 undefined citations**; the passage reads back out of
`pdftotext` in position.

§3.3's censuses are unchanged against HEAD and against its pre-P145 values: **23
antithesis sentences, 7 clusters, 12 `deixis --hard` hits.** **0 new shared six-word
runs**, 1,622 book-wide before and after.

## Figures

133 sections, **1 changed**. 99,527 → **99,542** words (+15); §3.3 4,265 → 4,280.
**196 pages unchanged.** **233 → 231 cross-references**, which is where the session
began. 324 bibliography entries unchanged. 0 `\textit`.
