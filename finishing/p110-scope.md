# P110 — the shovel-ready rows applied: 34 rulings, 24 references removed and 11 kept, 154 to 130

**The instruction.** *please implement ~/book-scratch/shovel-ready.md and then make the proofs.* The
file is the 34 rows of the P109 audit that the Opus readers ruled on, each with a finding and the
repair it implies: 11 keep-after-repair, 8 misdirected, 15 trouble. P109 left it as the next
session's work.

## What was done

The 34 rows sit in 17 paragraphs of 16 sections. Each paragraph was pulled from the tex whole, and
the targets the repairs depend on were opened before anything was written: §3.8 for the word
*accommodation*, §9.3.5 against §7.3's duplicate, §3.10 for the obligation row 456 asked to have
stated, §3.2 for the three gaps, §10.2 and §10.6 for the democratic dividend, §3.3 for Replacement's
discharge condition and the falsifier, §4.2.3 for the corrigibility identity, and §3.1 for its own
use of *accommodation* and the captured-democracy case. The eleven kept references stand as the
audit ruled. The 23 dropped rows are 24 `\ref` in the tex, one row being *chapters 4 and 5*.

Fifteen of the drops are a bare cut or a gloss of a few words. The rest, with the reason:

- **§3.1 (row 61)**: *the one chapter 7 is an account of failing* is now *the one that fails by
  recuperation*; recuperation is defined at §2.1.2, so the reader has it, and the identification
  with chapter 7 lives at §3.9, where row 127 keeps it.
- **§3.3 (row 80)**: *section 4.2.3's identity* credited §4.2.3 with an identity §4.2.3 credits to
  §3.5, which comes after; the identity is now named in the book's own words, *one property with
  the sign flipped*.
- **§3.9 (row 129)**: the tail after the dash, *with the same channel and a larger output*, was
  compressed past self-explanation and is cut; the clause before it carries the point.
- **§6.2 (rows 255, 256)**: §3.8 was credited with calling the failure *accommodation*; it says
  *slow renormalization* and uses only the verb. The noun is §3.1's own, in the sentence about the
  *Slaughter* majority, so §6.2 keeps the word and loses the pointer.
- **§7.3 (row 294)**: the slope paragraph reproduced §9.3.5 nearly verbatim, and the row asked
  which section carries the text. §9.3.5 does: the instrument sits there under its own run-in head
  with the two cautions after it. §7.3 keeps one sentence specific to pipelines and the reason a
  trend is harder to fake than a level. The stray `,.` in the paragraph above it was repaired as a
  rider.
- **§9.3.2 (row 362)**: *section 3.1 says what discharging it would take* pointed at a section that
  does not say it; the condition is §3.3's, and it is now stated in §3.3's words, *which
  construction, at what scale, against which test, and where it stopped*.
- **§12.2.1 (row 456)**: *the obligations handed to chapters 4 and 5* carried nothing without the
  numbers, and listing them among what the falsifier *breaks* was not what §3.10 says, which is
  that the obligation changes rather than lifting. The sentence now names the obligation, whether
  the thing reporting can be believed, and says the design chapters keep it in a changed form. The
  first version repeated fourteen of §3.10's words, found by searching the proof's text for the
  new sentences; a second commit paraphrased it.
- **§12.2.1 (row 457)**: *which of chapter 3's routes* is ambiguous between §3.1's four ways and
  §3.3's constructions, so the sentence now says *by which route it got there* and commits to
  neither.

Every proposal matched its line exactly once, and the applying script refused anything else. The
word diff was read whole before the first commit; one sentence of it was then recast because it
used the *not X but Y* frame style.md §2 names.

## Numbers

**154 → 130 references in all, 118 → 94 in the body; 91,207 → 91,152 words; 187 pages; 0
undefined references; 19 overfull boxes, as before; 138 sections, 16 changed; HTML 624 internal
links over 1,559 ids, none broken and none duplicated; suite green at every commit. Committed as
`f3483c5` and `228a689`, the proof pair rebuilt in place at `7d742a9`.** One page was looked at,
§7.3's, and it sets cleanly.

## Left undone, named

- **The rows set aside at P109**, outside the repository: `roadmaps.md` 18, `near-roadmaps.md` 12,
  `collateral.md` 7. Each needs a ruling before anything is done with it.
- **Nobody has read the 16 changed sections end to end**, nor P109's 111.
- **`reports/xref_shapes.tsv`, `reports/xref_pairs.txt` and `xref-paragraphs-*.md`** are stale, as
  P109 recorded.
- The audit's own preamble still says nineteen TRUE. The rows in `shovel-ready.md` are marked
  applied, with the original status kept in the cell.
- Row 156's alternative, making the priors-and-bias identification in chapter 6 where §6.1.2 is
  the nearest support, was not taken: the pointer was dropped and nothing was added.
- P103's four, the rest of P104's list, P105's one, Q-070 and Q-074 are as they were.
