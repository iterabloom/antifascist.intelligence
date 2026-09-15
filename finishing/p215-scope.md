# P215 — the author's 124-item list against the cross-reference as prose

The author supplied 124 numbered edits, delivered in eight batches, each item
giving find-text, a replacement or a deletion, and a one-line reason. **The
reasons name one habit**: a sentence that routes the reader to another part of
the book instead of saying the thing. The list does not use a word for it. What
the items have in common is that each removes the routing and keeps, or
restates, the claim.

**Every item was applied as written.** Where an item specified a replacement,
the replacement is the author's text, not drafted here. No independent search
for the class was run; every edit came from the list.

This is the third pass of one sweep. P213 (D-315) removed the sentence crediting
the book with a virtue; P214 (D-316) removed the sentence announcing what the
book is about to do; P215 removes the sentence that sends the reader somewhere
else to find out.

## Shapes the list removes

**The forward roadmap.** Chapter introductions that enumerate their own
destinations: the Foreword's chapter-7 preview (item 1), chapter 1's
seven-chapter route (item 2), chapter 2's closing dispatch (item 4), chapter 3's
four-places paragraph (item 16), and the whole introductions of chapters 4, 8, 9,
10 and 12 (items 51, 72, 85, 106, 112). Chapter 4's introduction went from three
paragraphs to three sentences; chapter 10's from two paragraphs to two sentences.

**The premise held elsewhere.** *Section~3.2 asks a refusal to reach a case
nobody anticipated…* (item 20), *Section~3.2's marks are that pair seen from
outside* (item 52), *Chapter~2 has the general fact* (item 75), *Section~5.5
separates external evidence from internal refusal* (item 81). In each the
replacement states the premise where it is used.

**The attributed instrument.** *Section~9.3.4's chain of authority transfers
without modification* (item 41), *Section~8.3.2's three conditions transfer
without modification* (item 76), *Section~3.5's precommitment forms — [five
glossed terms] — are set out there* (item 91). The instrument is now named in
place, its terms listed rather than cited.

**The classified example.** *In the vocabulary of section~3.2 this is a failure
of correct defeat* (item 40), *That would be novel pressure in the sense
established by section~3.2* (item 38), *which is what section~3.6 finds* (item
87). The classification survives; the citation of where the vocabulary was
defined does not.

**The deferred answer.** *the next section says why* (item 21), *Both are taken
up below* (item 19), *chapter~5 takes up what additional evidence could
distinguish the two* (item 56), *section~11.2 states the one experiment that
would answer it* (item 120, which keeps the reference in parenthetical form).

## What the pass did to the cross-reference apparatus

**221 cross-references became 75.** That is the pass's largest measurable
effect and it is not a side effect: routing was the object.

**Of 88 labels, 57 now have no inbound reference. Twenty-one of those are new
here**: `2.3.1, 4, 4.1, 4.3, 5, 5.1, 5.4, 5.5, 8.3.1, 8.3.2, 8.3.3, 8.3.4, 9,
9.1.1, 9.3.2, 9.3.4, 10, 10.4, 10.5, 11, 11.1`. The other 36 were already
unreferenced at `91e5f73` and are not this pass's doing. **Chapters 4, 5, 9, 10
and 11 lost their last inbound reference here**; chapters 0, 8, 12 and 13 had
already lost theirs. Chapters 2, 3, 6 and 7 still have inbound pointers.

**Fifty-six of the surviving 75 references are in chapter 13**, the
recapitulation, which this list did not touch. The rest are scattered two and
three at a time: ch02 2, ch03 6, ch05 2, ch07 1, ch08 2, ch09 3, ch11 2, ch12 1.
Outside chapter 13 the book now carries 19 cross-references.

**No label is undefined and no reference is broken.** `check_xrefs.py` passes,
and the build reports zero undefined references and zero undefined citations.
An unreferenced label is legal LaTeX and costs nothing at build time. What it
costs a reader was not measured.

**§8.3.4 is the clearest case.** It drew on its three sibling subsections by
name six times and now stands alone; §§8.3.1–8.3.3 are reachable only by reading
through chapter 8.

## Three mechanical conversions, none of them silent

**Item 109's citation arrived as `[@calvano2020artificial]`**, which is Pandoc
syntax and would have printed literally. Set as `\autocite{calvano2020artificial}`,
which is what the sentence it replaced used. The key resolves.

**Items 91, 102 and 112 arrived with closed-up em dashes** (`measures—publication`).
Every one of the manuscript's 306 em dashes is spaced on both sides, so these
were set spaced. The author has not been asked to confirm.

**Items 36, 105 and 120 use `(§\ref{...})`**, the form chapter 13 uses twenty
times. Chapter 3 had no instance of it before item 36.

## Substance that left with the apparatus

These are claims rather than directions, and each is still made in its home
section — several of which are now among the unreferenced.

- **Item 4** dropped chapter 2's statement that §2.1 moves the floor from a
  deontological to an ethological footing. §2.1 still performs the move and
  `03.tex:13` used to report it, until item 15 removed that too.
- **Item 36** dropped the German prohibition's dates: in force since 1949,
  amended 1994, *Seventy years of that, for a list of pictures.* The
  replacement keeps the shape of the finding without the dates. Whether the
  1994 amendment is cited elsewhere was not checked.
- **Item 91** dropped the gloss on each of the five precommitment forms. They
  are named in §9.1.1 and described in §3.5.
- **Item 82** dropped *loyalty as the likeliest failure, with a number under
  it*; **item 84** dropped the corporate form as how power concentrates
  *without anyone deciding that it should*; **item 93** dropped the update
  channel as *the operator's lever*.
- **Item 100** dropped the Replacement passage's contrast with Reduction and
  Refinement, which have a board to answer to. Its conclusion survives as
  *Costs alone do not establish that an alternative has failed.*
- **Item 118** dropped §12.2.1's identification of the held-out-pressure result
  as chapter 3's own falsifier. Chapter 3 still states the falsifier.
- **Item 95** dropped the reason guardianship is the frame — consent
  unavailable to a party made for its role. §9.1.2 now asserts that a
  guardianship regime needs an endpoint without saying why guardianship;
  §2.4.2 still argues it.

## Found while cutting, and left standing

**Item 39's replacement reads oddly and was applied verbatim.** *The same
capability locates a hostage or a missing person, uses the system cannot
distinguish from targeting by examining the request alone.* The appositive
*uses* attaches to *a hostage or a missing person* rather than to the locating.
Reported to the author inside the run; no change made.

**§2.4.1's *The two readings do not conflict*** still resolves forwards rather
than backwards, carried over from P214 and untouched here.

**Item 89's *Of the four ways to build a floor*** no longer says where the four
are enumerated. The sentence lists three and then the fourth, so it stands
alone.

## A correction to the committed record

**`p214-scope.md`, `D-316` and P214's `STATE.md` lead all say that pass's 50
items arrived "in four batches." They arrived in six** — item 1; items 2–3;
4–7; 8–15; 16–31; 32–50. The error is recorded here rather than edited out of
those files, `DECISIONS.md` being append-only and the superseded lead being
kept as written. P215's own count — **124 items in eight batches** — is
item 1; 2–3; 4–7; 8–15; 16–31; 32–63; 64–93; 94–124.

## Reports

**Every report a tool regenerates was rerun. Nine moved**: `section_stats.tsv`,
`claims.tsv`, `dated.tsv`, `epigram.tsv`, `tics.tsv`, `voice.tsv`,
`xref_content.tsv`, `xref_pairs.txt` and `xref_shapes.tsv`. **Two regenerated
byte-identical**: `negatives.tsv` and `headings_reconcile.md`. **Seven stay
stale and were not touched**: the four `redundancy*` files need a package this
machine does not have; `list_candidates.tsv` and `triage-summary.md` are
one-shot P0–P1 instruments; `toc_v4.md` is stale by rule and must be left alone
(`finishing/README.md:27`, D-075). `xref-paragraphs-{related,unrelated}.md` are
hand reads keyed to paragraphs this pass cut, and were not re-read.

## Measured

88 sections, **73,806 body words** (from 77,279; **3,473 removed**), **153
pages** (from 159), **75 cross-references** against 88 labels (from 221), 226
bibliography entries all cited, 0 undefined references and 0 undefined
citations. Suite green.
