# P87 — the D-117 reader tax worked flag by flag across chapters 3–12

**The instruction.** Given in three parts over the session. First: *use Sonnet subagents for
chapters 3-12 … the subagent reads the chapter and flags passages that qualitatively satisfy the
conditions that D-117 and/or my edits to chs 1-2 were intended to address … err on the side of
inclusion … then here in the main session, evaluate each flagged passage one at a time and
revise as needed.* Then the order to work them in: `announce`, `meta`, `selfassess`, the seven
confirmed defects, then `trailing`/`filler`, `strawman`/`pointer`, and
`deixis`/`echo`/`inventory`, with proofs at three checkpoints. Then *do the last four*, which
closed `nominal` and `origin`. The standing instruction on how hard to cut was given once and
governed the whole pass: *the book is git-tracked, so do not be shy about cutting/rewriting
stuff that will waste the reader's time or somehow otherwise annoy them.*

## What the scan was, and what it cost to get

Twelve scan units over chapters 3–12, eight by Sonnet subagents and three — `ch06a`, `ch09a`,
`ch09b` — by the main session after the subagents failed. **The failures were not scoping
errors**: seven-plus consecutive `No response from API (error type server_error)` at every
chapter size, mitigated in order by relaunching, by instructing single-command reads, and by
splitting chapters into halves, before the main session took the remainder itself.

**415 flags survived verification.** Every quote was checked verbatim against the source by
`verify.py`, and **zero rows were discarded as hallucinated** — 35 were initially discarded and
then recovered when the check turned out to be at fault, not the agent: the chapter 12 unit
wrote bare filenames where the others wrote repo-relative paths.

## The pass's finding: the quote test measures deletion, and this pass was not mostly deletion

A verbatim-quote check over all 415 flags at the end reports **seven unresolved**. Two of those
are real and deliberate. **The other five it is wrong about**, in the same way each time: the
repair kept the flagged words and supplied what they were missing. §9.1.1's count is no longer a
standalone paragraph making the reader wait for its answer — it is merged into the paragraph
that answers it. §8.3.3's undefined term is now defined five paragraphs above it. §10.3 ¶26,
§10.3 ¶32 and §10.4 ¶20 each now state, after a colon, the content the pointer had stood in for.

**So the honest count is 413 of 415 changed, and any future automated re-check of this pass will
overstate what is left by five.** The `pointer` class is the reason: it is the one class whose
repair *adds* text, which D-117 recorded in advance and which this pass confirms — eight new
`\ref`s and a gloss beside each.

## The two flags left standing, and why

- **§8.1.1**, `trailing`: *That is an argument for external standing rather than against
  proximity.* Without it the paragraph ends on a problem with no resolution, and reads as
  undercutting the recommendation it has just made.
- **§9.3.5**, `announce`: *Transparency is the first defense…* It states its claim rather than
  promising it, and it is the first term of a first/second/third series the section runs on.

## What the cutting found that the flags did not

- **A false claim about the book's own front matter.** §6 ¶22 said *this is why the introduction
  lists racial capitalism among the threats AI could help address*. `ch01/01.tex` does not
  contain the phrase and has not since P81 rebuilt the introduction and cut its roadmap (D-163).
  Cut, not repaired.
- **The epigraph gloss was doubled.** *Every argument in this book about meaningful human control
  is an argument with that sentence* stood at §6 ¶16 and again, almost verbatim, at §6.4.1 ¶35,
  each beside its own *that is a design document*. The opener now points at §6.4.1 and stops.
- **Five roadmaps named an order their sections do not follow** — §4, §6.4, §8, §10 and §12.2.
  That is what a roadmap does once the sections around it are renumbered, and it is the argument
  against carrying one at all.
- **§12.2's roadmap carried a claim made nowhere else in the chapter**, that one milestone's
  failure *carries an obligation rather than a score*. Which milestone is not recoverable from
  §12.2.1, so the claim went with the paragraph rather than being relocated on a guess. **If it
  matters it needs re-stating where the milestone is.**
- **§5.2.3's *they are the same difficulty three times* was cut as false**, not as a preview: the
  first two difficulties are the system reporting on itself, the third is surplus information
  held.
- **§3.4 ¶69 was a comparison between the current answer and a previous draft's answer**, which
  the reader has never seen. Rewritten to the one sentence carrying the route.
- **§10.4's *the room left by the policy levers available against authoritarian AI misuse* did not
  parse** and also carried a strawman definition of geopolitics. One sentence now.
- **`echo` confirmed a measurement rather than only cutting text.** Eight of its eleven were the
  *not-Y* half of an *X rather than Y*, and in every one Y was literally X with a negation on it.
  That is D-159's corrective antithesis, and cutting the negated half changed no claim anywhere.

## The seven confirmed defects, with the author's ruling on each

Four were misdirected **prose locators carrying no `\ref` at all**, which is why nothing in
`tools/` had ever seen them: `check_xrefs.py` verifies that a `\ref` resolves and has nothing to
say about *that section* or *the paragraph above*.

| where | was | now |
|---|---|---|
| §3.3 | *Four constructions occupy it* | *Five* — against five `\runin` heads and §3.9's own count |
| §3.9 | *the reason the paragraph above gives* | *the above discussion about the three branches* |
| §7.4 | a clause restated inside its own sentence | the repetition cut |
| §10.5 | *the voluntary instruments earlier in this section* | §10.4, where they are |
| §5.6.2 | bare *that section* | §3.5 |
| §6.3.5 | *the distinction drawn earlier* | §6.2 |
| §6.4.1 | *the question that section is left with* | §10.3 |

**§6.4.1 is the one the evidence could not settle.** The nearest reference before that sentence
is §10.2, two paragraphs up and inside an `esbox`, so a reader had no way to recover the target
and a guess would have named the wrong section. The author ruled it §10.3, the
weapons-and-vendor-chain section.

**§3.3's neighboring clause was checked before the numeral moved.** *Three of them are being
built by people who would not describe themselves as working on this problem* holds at five —
precommitment, plural systems and CIRL are live engineering, Bratman and the operator duty are
not — so only the numeral changed.

## Where the judgment sat in each class

- **`meta`** — cut self-reference that only says where the reader is; keep self-reference that is
  part of the argument. §6.1.1 still names the vendor whose model helped produce the book, §7.4
  still says there is no procedure for checking whether these objections are the ones the channel
  reliably produces, §7.3 still says *I do not have an answer to it*. A book arguing that
  provenance should be visible cannot cut its own provenance.
- **`selfassess`** — cut the grading, keep the admissions. Where a superlative wrapped an
  admission, the wrapper came off and the admission stayed. AGENTS.md's no-weasel-words rule is
  what makes this the line.
- **`strawman`** — the author's standing ruling from 2026-09-01 governed: cut the prevalence
  claim rather than expand scope to prove it. No citations were added and no claim was hedged
  into vagueness.
- **`inventory`** — the test was whether the second and third items are used again anywhere. None
  was. §4.2.1 is the case worth recording: of three examples of supervised ethics data, only the
  Moral Machine project is referred to again, and it is now the only one given.

## Counts

**93,049 → 89,854 words**, a loss of **3,195**. **185 → 183 pages.** Cross-references measured
**449** after D-176, **457** after D-178 and **462** after D-179 — the `pointer` class adding
thirteen. Suite green at every commit; the pre-commit hook ran it each time.

## What this pass did not do

- **Chapters 1–2 and 13–14 were never scanned.** Everything here is chapters 3–12.
- **Nothing outside the 415 flags was swept.** The `filler` class in particular is larger than
  its flags: the book-wide census before the pass was *exactly* 68, *actually* 57, *genuinely*
  17, *precisely* 12, *simply* 10, *very* 7, and after it 44, 55, 15, 10, 8, 6. **`exactly` still
  stands at 44 book-wide**, most of it in sentences the scan did not flag or chapters it did not
  reach. That sweep is the author's call and was not taken.
- **Three defects from `defects.md` were seen and left**, being outside the seven the author
  ruled on: §7.4's five-feature test assesses only three of five factors for the discourse
  instance while §7.4 ¶23 claims all three instances clear; §9.3.5 ¶14's *(of the oversight
  machinery against the institution it is supposed to bind) is:* reads as an unfinished edit; and
  §3.6's *The harder enumeration is the first one* has an unclear referent.
- **The scan's own record is not in the repository.** `combined.tsv` (415 rows), `defects.md`,
  `verify.py` and the twelve per-unit TSVs live in `~/book-scratch/reader-tax/`, outside git.
  Whether they belong in `finishing/` was offered and not decided; the precedent for keeping them
  is `xref-paragraphs-{related,unrelated}.md`, described in `README.md` as **a hand read, not
  regenerable by a tool**, which is what this is.
