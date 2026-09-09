# P154 — the aground image restored as a named exception to `style.md`

Author ruling, given on being told that restoring the image means accepting a
shape the style sheet rules against: **"yeah i want it back please, just make an
exception."** Reverses P152's concretion and partly reverses D-238.

## What went back, and it is not the sentence verbatim

`02_03_01.tex:13` now closes:

> Suffering is not merely hard for such a system to reach. The self it requires is
> not there. A hull that draws more water than there is does not float badly; it is
> aground.

**The original's middle sentence did not come back**, and could not: *It is not
suffering faintly; it is not in that water at all* needs `:9`'s introduction of the
figure for *that water* to point at, and `:9` went at P138. **The hull sentence
introduces its own water** — *more water than there is* — so it stands without the
setup. That was option (c)'s constraint and it still binds; what the exception lifts
is the shapes, not the dependency.

**P152's sentence is gone.** *A system with no biography to lose is in a different
state from one with little to lose* was the plain declarative `style.md` §7 asks for
in place of an aphorism. The ruling prefers the aphorism here, so keeping both would
have made the same point twice.

## The exception, stated as what it is

The restored sentence breaks two rules in the style sheet, and both were the reason
P138 cut it:

- **§2's contrastive frame.** *does not float badly; it is aground* spends its first
  clause on the wrong answer.
- **§7's aphorism.** It is the balanced two-clause epigram that *asks to be admired
  before it is checked*.

**This is a ruled exception for one sentence and not an amendment to either rule.**
Neither section of `style.md` was edited. A later pass finding this sentence and
reporting it as a defect is re-opening a decision, not making a finding.

## Two consequences worth stating plainly

**D-238 is partly reversed.** That decision gave the hull figure one home in §3.4.
§2.3.1 now carries one instance of it again. **The proportion is what P138 was
actually about**: it cut four instances from §2.3.1 against §3.4's seven, and the
motif was the complaint. Measured now, on *water*, *deep*, *depth*, *afloat*,
*aground*, *hull*, *shallow*: **§2.3.1 carries 4 and §3.4 carries 8.** Three of
§2.3.1's four are in this one sentence and the fourth is `:38`'s pre-existing *deep*.
§3.4 still owns the developed figure.

**`03_04.tex:60`'s back-reference is unaffected and reads slightly better.** It says
§2.3.1 *argued that the deepest of these harms asks for both parts together*, from
inside a paragraph that is already using *afloat* and *how deep it sits*. It now
points at a section where the figure is live rather than at one where it had been
removed.

## What the instrument says about it, which is the reason the placement matters

The restored sentence is **the paragraph's last**, and `epigram.py` — built in the
same session for the author's structural note — **does not pair it with anything**,
because a landing line is only the defect that note describes when a sentence
carrying the limit follows it. Nothing follows this one. **An epigram in final
position is emphatic rather than a line a reader stops at**, which is the
distinction the structural note turns on.

`antithesis.py` also does not see it: its patterns are *rather than*, *not X but Y*,
*is not a*, *and not*, *instead of*, *as against*, and §2's contrastive frame in a
semicolon form matches none of them. **That is a limit of that tool and not a
clearance** — the count stayed at 11 for §2.3.1 because the tool is blind here, not
because the shape is absent.

## Verification

Suite green. `refresh_order_shas.py` run. Scratchpad lualatex build: **196 pages, 0
undefined references and 0 undefined citations**; the sentence reads back out of
`pdftotext` in position.

§2.3.1's censuses are unchanged against HEAD at **11 antithesis sentences, 3
clusters, 4 `deixis --hard` hits** — and for the antithesis figure that is the tool's
blindness and not a result. **0 new shared six-word runs**, 1,622 book-wide before
and after.

## Figures

133 sections, **1 changed**. 99,571 → **99,568** words (−3); §2.3.1 1,870 → 1,867. **196 pages unchanged.** **231 cross-references unchanged.**
324 bibliography entries unchanged. 0 `\textit`.
