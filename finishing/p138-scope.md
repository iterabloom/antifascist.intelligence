# P138 — the hull figure given one home, and §2.3.1 made plain

An author's note: the figure appears three times — §2.3.1's nociception ordering,
§2.3.1's *the standing theories draw less*, and §3.4's *three depths in the same
water* — with §3.4's named as the clearest. Pick one as canonical. If §3.4's,
compress §2.3.1's instances to a single clean statement of the ordering.

**Executed on the §3.4 branch. The figure appears twice more in §2.3.1 than the
note counts, and one of those two is the best sentence of the five.**

## The census the note did not have

| site | what it says |
|---|---|
| `02_03_01.tex:9` | *draw different depths of self, the way a hull draws water* — the introduction |
| **`02_03_01.tex:13`** | *It is not suffering faintly; it is not in that water at all. A hull that draws more water than there is does not float badly; it is aground.* |
| `02_03_01.tex:24` | *the deepest of these … draw less … moves into shallower water* |
| `02_03_01.tex:28` | *The shallower ones do not need persistence* |

Plus §3.4 at `:49`, `:52`, `:54`, `:56`, `:58`, `:60` and `:62`, where the
vocabulary also includes *afloat* and *how deep it sits*. **Sixteen occurrences
across the two sections**, which is more than a motif — it is the section's
default way of saying anything about the ordering.

## Why it had to be all of §2.3.1 or none

`:13` is the one place the figure carries an argument instead of decorating one:
a system with no persistence is not a mild sufferer but outside the category. I
tried to keep it and could not. **Its *not in that water at all* has no
antecedent once `:9`'s introduction goes**, so keeping `:13` means keeping `:9`,
and keeping both is keeping the figure in §2.3.1 — which is the branch the note
declined.

**What weakens the case for `:13` is the book's own style sheet.** *It is not
suffering faintly; it is not in that water at all* is the contrastive *not X, it
is Y* frame §2 rules against, and *does not float badly; it is aground* is the
balanced two-clause epigram §7 calls an aphorism, which *asks to be admired
before it is checked*. Both shapes, in one sentence pair.

**It is still the loss in this pass**, and it is one edit to reverse. Q-107 has
the before and after.

## The four edits

**`:9`** — two sentences to one, and it is the *single clean statement of the
ordering* the note asked for: *Nociception, pain, anticipated pain, and suffering
are ordered by what each one needs beneath it, not by how much it hurts.*

**`:13`** — *The self it requires is not there, and a concept whose precondition
is missing does not apply in a weaker form.* The categorical claim survives; the
hull does not.

**`:24`** — *the deepest of these* → *the most demanding of these*; *draw less* →
*ask for less*; *moves into shallower water* → *moves lower in that ordering*.

**`:28`** — *The shallower ones* → *The less demanding ones*.

## §3.4 is unchanged, and its back-reference now does the right thing

`03_04.tex:60` says *Section~\ref{sec:2.3.1} argued that the deepest of these
harms needs a self extended in time*. §2.3.1 no longer says *deepest*; it says
the claim plainly, and §3.4 translates it into the figure §3.4 owns. **That is
what letting one section carry a figure looks like** — the other states the claim
and the owner states it in its own terms. `:13`'s surviving sentence, *Cassell's
suffering presupposes a self extended in time*, is what the reference points at
and it is untouched.

**No cross-reference was added.** The count stays at 236, which is the first pass
in six not to move it.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
all four edits read back out of `pdftotext`. **Zero occurrences of *water*,
*depth*, *shallow*, *deep*, *hull*, *afloat* or *aground* remain in §2.3.1**,
checked after the edit.

## Figures

133 sections, **1 changed**. 99,264 → **99,249** words (−15); §2.3.1 1,868 →
1,853. **196 pages unchanged.** 236 cross-references unchanged. 324 bibliography
entries unchanged. 0 `\textit`. **The proof pair was not rebuilt and is now six
passes stale.**
