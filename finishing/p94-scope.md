# P94 — the author's Overleaf edits imported, and the fork that lost its name

**The instruction.** *i want to work on the text manually*, then the returned package, then
*convert those 8 to emph and then make the proofs*. The pass is the author's own hand edits to
chapter~3, brought back through `overleaf.py`, plus one mechanical repair and the proofs.

## The round trip

**Exported from `6e70bde` with a clean tree, imported two passes later with the tree still on that
commit.** 144 files out, 144 back. The import reported **4 to apply, 137 unchanged, 1 skipped
(`sections.tex`, regenerated), 0 conflicts, 0 problems**; no structural change, so nothing was
refused. The manifest's whole purpose — telling an Overleaf edit from a repository edit — had
nothing to do, because no pass ran on this side in between.

**Checked before applying rather than inferred from the suite afterwards**: every heading, label,
`\ref` and `\autocite` in the four files is byte-identical to what went out. `\ref` counts 10, 5, 4,
6; `\autocite` counts 0, 2, 1, 4; all unchanged. The edits are prose only.

**Four files, all chapter~3**: §3 opener, §3.1, §3.2, §3.8. **91,457 → 91,170 words, −287. 186
pages, unchanged. 138 sections, unchanged.**

## What the edits do

**The chapter opener is rehedged and its convergence claim withdrawn.** *Three unrelated problems
in this book force the same requirement* becomes *Three problems in generative AI suggest a
particular requirement*, and each is now introduced as *the first / second / third problem*.
**`unrelated` and `force` both go**, and with them the closing move of the sequence: *Those are
three descriptions of one thing* becomes *To address all three, I introduce a constraint*. The
chapter opened by finding a floor at the point where three unlike problems met; it now opens by
proposing one. Nothing downstream was found to lean on the convergence — grep for
`three descriptions`, `three unrelated` returns nothing outside the file.

**§3.1 converts its enumeration from branches to ways.** *The first branch* → *The first way to
build the floor*, and so on through the fourth, with *What the four branches divide up* → *What the
four ways divide up* and *None is free* → *None of these four ways are free*. Four instances of
*way to build the floor* now stand where the branch vocabulary was.

**§3.2 is compressed.** *A deployed language model* → *A production large language model*; the
three-way gloss on operational refusal loses its third item, the system that has understood what is
being asked; *Three properties distinguish it, and all three are behavioral* → *Three behavioral
properties distinguish it*; and two sentences of self-description go, including *A book taking a
position on machine feeling looks as though it must have changed the engineering, and this one has
not.*

**§3.8 takes two lines.** *Parenthood has exactly this property, which is the analogy
section~\ref{sec:2.3.2}'s guardianship framework already runs on and which now has to carry more
weight than it did* → *Parenthood has this property, which is the analogy on which
section~\ref{sec:2.3.2}'s guardianship framework runs.* The flag that the analogy is being asked to
carry more than before is gone.

## The finding: §3.1 no longer contains the figure five sections still use

**This is D-182's class, in the same chapter, one pass later, and made by removal rather than by
omission.** D-182 found that §3.2's ladder was never introduced and that 27 uses across nine files
leaned on it. The same shape is now true of the fork, and it was made by an edit that reads
correctly in its own file.

**`fork` is gone from §3.1: 1 → 0.** The deleted sentence was *What it has is a fork with four
branches and a cost on each.* **Four sections still use the figure as established**, one of them
attributing a statement to it:

- §3.3 — *the fork's third branch in its strongest version*
- §3.4 — *The first branch of the fork fails for the same reason*
- §3.5 — *The fork was never four options*, and *as the fork itself said*
- (§11.2's *a fork to be recorded as two parties* is the ordinary sense and is unaffected)

**`branch` survives 22 times as the term for §3.1's items, across ten files, and §3.1 introduces it
nowhere.** The count breaks down as §3.3 five, §3.9 four, §3.5 three, §3.10 two, §3.4 one, §2.1.1
one, §4.2.4 one, §4.3.1 one, §5.1.2 one — **and §3.1 itself two**, which is the sharpest form of it:
the section now says *the four ways* and then, in the same section, *It is the one branch nothing
can dismiss* and *hybrids that take a mechanism from one branch and a custody arrangement from
another*.

**Four of the outside sites name §3.1 by cross-reference and call its items branches**: §2.1.1's
*section~\ref{sec:3.1}'s first branch — the floor as a property of the artifact*, §4.2.4's
*section~\ref{sec:3.1}'s first branch in production*, §4.3.1's *Section~\ref{sec:3.1}'s first branch
tried to make a floor tamper-resistant*, and §9.3.2's *section~\ref{sec:3.1} attaches a cost to each
of its branches*. **A reader following any of those four arrives at a section that does not use the
word.**

**§3.9 is the worst-placed of them because it is nine days old.** D-187 built it as *the fourth
branch*, it opens *That points at a location the fork has not used. The three branches put the floor
in the artifact, in a party inside it, or in institutions around it*, and it carries a run-in head
*Why this is not the third branch*. It is written entirely in a vocabulary its parent section has
stopped using.

**No repair was made.** The vocabulary is the author's to choose and both directions are cheap —
restore *fork* and *branch* to §3.1, or convert the 22 downstream uses. The choice is Q-075.

## The mechanical repair

**Eight `\textit{}` commands came back and were converted to `\emph{}` on the author's instruction.**
They were the only ones in the manuscript: these three files carried zero before the import, and the
book uses `\emph` 46 times elsewhere, including in the same four files, so both spellings had ended
up within a few paragraphs of each other. `style.md` has no rule on emphasis either way, so nothing
flagged it and nothing could have — the practice was uniform until now, not written down. **8
converted, `\textit` now zero, `\emph` 46 → 54.** The converted spans: `bearer`, `fail`,
`specifically`, `actually`, `it`, `look`, `superficially resembles`, `mattering`.

**The conversion staled three `ORDER.tsv` digests and `check_all.sh` caught it**, because the import
had already refreshed them and the `sed` ran afterwards. `refresh_order_shas.py` cleared it. Worth
recording as the ordering trap it is: **any edit after an import has to refresh the digests again.**

## Numbers

**91,457 → 91,170 words, −287. 186 pages, unchanged. 138 sections, unchanged.** 0 undefined
references, 0 undefined citations, `check_all.sh` green. The proof pair is rebuilt and redated
2026-09-02 → 2026-09-03, the old pair removed in the same commit, and the README's two links follow
it. Two commits, `929e311` for the prose and `2affd9b` for the generated output.

## Left undone, named

- **Q-075 is open and nothing was repaired for it.** The fork and its branches are unintroduced as
  of this commit, and the book ships that way in the 2026-09-03 proofs.
- **One sentence in §3.2 may be a slip rather than a cut, and it was not touched.** *Defining
  mattering that way moves the uncertainty and does not dispose of it, and where it moves to is the
  gain* became *Defining mattering that way moves the uncertainty to the gain*, which does not parse
  the way the paragraph after it needs. It is recorded here and in Q-075's neighbourhood rather than
  fixed, because it is the author's sentence. **Not checked**: whether the same shape occurs
  elsewhere in the four files.
- **§3.2's opening no longer announces the enumeration its own title promises.** The clause *the
  distance between the two is hidden by a word that covers four different capacities* is gone, so
  the four-way split arrives without being set up. The heading still says *Four Things Refusal Can
  Mean*. Not repaired.
- **The prose was not read end to end.** What was checked is the structural half — headings, labels,
  references, citations, digests, the suite, the build — plus the vocabulary grep that produced the
  finding above. Whether the compressed §3.2 still carries its argument is a hand read that has not
  happened.
- Q-074 is untouched, as it has been since P88.
