# P13 — the cross-reference audit (D-046)

**Trigger.** The author supplied a list of ten suspected broken cross-references
and asked whether it was accurate. It was accurate in all ten. This pass
verified them, fixed them, read all 499 cross-references in the book against
their targets, and added a check so the defect class cannot recur silently.

All section numbers here are **post-D-043** numbering.

## 1. What was wrong, and why the P11 verification missed it

D-043 renumbered seven chapters and inserted two. Every cross-reference in the
book was rewritten by script. **The script matched on the words `section`,
`chapter` and `§` before a number.** A bare number — `(4.4.3)`, `the question
4.6.2 left open` — was invisible to it and silently kept its pre-renumber value.

The verification run afterwards extracted every reference and confirmed it
**resolved to an existing section**. That is a weaker test than it sounds, and
it passed two ways it should not have:

- a bare stale number that happened to name a real section resolved fine;
- a prefixed reference rewritten to the wrong number resolved fine.

P11 was reported as verified on the strength of that check. It was not verified.
The claim was wrong and is corrected here rather than left standing.

## 2. The eleven defects fixed

Nine pointed at section numbers that **do not exist**:

| in | said | now | evidence |
|---|---|---|---|
| §5.4.1 | 4.4.5 | section 5.4.5 | chronosystem, after 5.4.4's macrosystem |
| §5.6.3 | 4.6.2 | section 5.6.2 | "the question ... left open" |
| §5.7.1 | 3.3.1 | section 4.3.1 | same Hide-and-Seek case named 4 lines above |
| §6.4.3 | 6.7.2 | section 8.7.2 | technical-community standards |
| §8.3.2 | 4.4.3, 4.4.4 | sections 5.4.3 and 5.4.4 | sentence already says "Chapter 5's account" |
| §8.5 | 6.5.1, 6.5.2 | sections 8.5.1, 8.5.2 | "the two sections that follow" |
| §8.6.2 | 6.6.1 | section 8.6.1 | same sentence cites 8.6.1 twice already |

Two resolved but pointed at the wrong section:

| in | said | now | evidence |
|---|---|---|---|
| §6.4.1 | 5.4.2 and 5.4.3 | sections 6.4.2 and 6.4.3 | sentence says "technical and policy responses"; 5.4.2/5.4.3 are microsystem/mesosystem |
| §6.4.3 | section 8.3 | section 8.7 | 8.3 is political economy; the sentence is about international agreement |

One was a self-reference:

- **§9.1.6** cited "Section 9.1.6's argument for learning from disagreement."
  Cause identified: this section is old §7.1.7, and its sibling old §7.1.6
  became §7.2 through a special case in the renumber map. The script applied
  the 7.1.7→9.1.6 rule to a reference that needed the 7.1.6→7.2 rule.
  **Now §7.2.** Chosen over §5.3.3, whose title is a closer verbatim match, on
  two grounds: the surrounding argument is about annotator disagreement, which
  is §7.2's subject, and §8.2.2 independently cites §7.2 for the same claim.
  The author was offered the choice and delegated it; this is the reasoning.

One was a wrong word, not a wrong number, and predates the renumbering:

- **§5.1.3** "chapter 2.1.3" → "section 2.1.3".

## 3. One further defect, found by the full read

**§9.1.6** cited "Section 8.6's account of the slope, not the level." The slope
argument is specifically **§8.6.4**, which is how all eight other citations of it
in the book refer to it. Corrected to §8.6.4. Not strictly dangling — §8.6.4 sits
inside §8.6 — so this is a precision fix, listed separately from the eleven.

## 4. One reported defect that was not one

I initially flagged **§6.4.3's "the Partnership on AI (section 5.6.3)"** as
wrong, on the assumption that §5.6.3 does not cover the Partnership on AI. That
assumption was false: §5.6.3's safeguards list names it as "one existing venue,"
which the §6.4.3 sentence echoes with "another such venue." The reference is
correct and deliberate. **The change was made and then reverted.** It is recorded
here because a fix applied on a wrong premise is the same class of error as the
defect it was meant to repair.

## 5. The full read

All **499** cross-references were pulled with their target's title from
`ORDER.tsv` and the surrounding sentence, and read one at a time. Beyond the
items above, none was wrong. This is a human read, not a proof: it establishes
that each reference is plausible against its target's title and local context,
not that the target's *body* says what the citing sentence claims.

## 6. Sixteen bare references prefixed

Sixteen references were correct but written bare — `(5.2.1)`, `(8.3.3)`,
`the compassion system 2.2.1 describes`. Each now carries `section`. This is the
structural half of the fix: **the next renumbering can see them.** Every
cross-reference in the book is now prefixed.

## 7. The check that makes it stick

`finishing/tools/check_xrefs.py`, wired into `check_all.sh`, fails the build on:

- **DANGLING** — a reference to a section number not in `ORDER.tsv`;
- **BARE** — a section number with no `section`/`chapter`/`§` in front of it,
  which is what made the P11 defects invisible.

Quantities (`5.7 million`, `3.1 percent of GDP`, `GPT-3.5`) are excluded by a
unit test on the surrounding text. Both failure modes were exercised by
injecting one of each and confirming exit 1. Current state: **551 references
resolve, all prefixed.**

**What the check does not do.** It cannot tell whether a reference that resolves
points at the *right* section — that is the semantic question, and it is what
§5 above did by hand. After any future renumbering the hand read has to be
redone; the checker only guarantees that nothing dangles and nothing hides.

## 8. Not author-accepted

The fixes are applied and the checks pass. No section in this pass has been
read and accepted by the author at the section level.
