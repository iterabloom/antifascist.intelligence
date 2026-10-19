# P223: the restoration

## What was asked

On 2026-10-19, with the notes pass merged (D-914) and the proof of
`787557cf` built, the author worked through the manuscript in a long session
with a language model and had the session distilled into seven clusters. The
session concluded that too much was cut. The author's instruction, given with
the distillation: "this is what we should do next", and, on the method,
"not all notes necessarily should be put back. we are following only what
the distillation says." The word counts and reference counts in the
distillation are the session's own and are off in places; the author said
they are beside the point.

## The milestone, as the distillation states it

The book that exists with its argument above the line and nothing new in it.
Three jobs:

1. **Restore the argument-bearing notes** (cluster 1): chapter 19 per its
   list; Part I per its list; [465], [274]–[293], [382]–[385], [409]–[413],
   [439]–[445], [940]; the recuperation question from [89] in chapter 3's
   bullet.
2. **The preface says the one thing** (cluster 2): five walls; walls don't
   refuse; where refusers come from, human and machine; the alternative is
   property; whether the property is anyone is a separate question the book
   keeps separate. With it: the "just build tools" reply, individuality's two
   jobs, the door into Part IV from §16.7's last paragraph, "institutions
   without a conscience keep the evidence", the guarantee's dependence
   introduced in Part II, measure five separated from the guarantee.
3. **The visible defects** (cluster 1): the note-only concepts defined at
   first use (a sentence each, eight of them); the note → chapter → note
   cross-references hunted; openings for chapters 19 and 28, which are
   structural and in scope.

Also in cluster 1's list: a condensed glossary moved to the front; Appendix
C.2 to a web supplement with a one-page summary; an author note; the stage
dates cut from chapter 28; the lyrics license and the dialogue quotations;
[1096], [1106] and [165] opened. Cluster 6: `next.md` in the repository for
clusters 3 to 5; the milestone as a tagged release with the three jobs as its
acceptance test, main untouched afterward and new work on a branch; a
front-matter verification line; a located-passage pass over the full texts
on disk, kept as a column of its own and never counted as a human check.

Note numbers in the distillation, and here, are those of the render of
`787557cf` under `--truncate 5` (D-915); every restoration moves the numbers
after it, so a round's render is numbered afresh and the distillation's
numbers name notes as they stood before the pass began.

## The rulings

1. Nothing goes back wholesale. A note named by the distillation comes back;
   no other note moves. The four classes the distillation describes are
   the diagnosis; the lists are the scope.
2. A note comes back as the text stood before the pass merged
   (`f10bc393^`, main at `f1bdcda3`): the same words, paragraph breaks and
   run-in heads, by `finishing/tools/promote.py`, one note at a time. A
   footnote the book had before the pass, named by the list, is unwrapped
   into the body at its mark and the joins are edited by hand.
3. The rounds run on main, uncommitted, with the author reading each round's
   render; commits on his word. The committed proof pair stays the proof of
   `3a2a968e` until "proofs please".
4. New writing (the preface, the openings, the definition sentences) is
   drafted for the author and read before it goes in.

## The measure

Main-text words before the appendices, by `render_markdown.py --check --keys
--chapters`: the baseline before the pass (`ad9effa1`), the book at the
merge (`f10bc393`), and after each round.

| chapter | baseline | at the merge | after round 1 | after round 2 |
|---|---|---|---|---|
| 1 | 1,818 | 859 | 1,984 | 1,984 |
| 2 | 622 | 385 | 522 | 522 |
| 3 | 526 | 283 | 433 | 433 |
| 4 | 1,762 | 1,423 | 1,423 | 1,461 |
| 6 | 5,408 | 2,752 | 2,752 | 3,271 |
| 7 | 2,775 | 1,027 | 1,027 | 1,501 |
| 8 | 994 | 251 | 251 | 404 |
| 9 | 785 | 307 | 307 | 403 |
| 11 | 7,334 | 2,639 | 3,361 | 3,392 |
| 12 | 1,972 | 997 | 1,290 | 1,290 |
| 13 | 3,925 | 1,522 | 1,798 | 2,034 |
| 14 | 2,749 | 1,021 | 1,683 | 1,683 |
| 15 | 4,572 | 1,817 | 2,545 | 2,615 |
| 16 | 5,196 | 2,554 | 2,554 | 2,808 |
| 18 | 6,257 | 3,049 | 3,049 | 3,315 |
| 19 | 5,415 | 2,398 | 4,923 | 4,970 |
| 22 | 5,913 | 2,543 | 2,543 | 2,901 |
| 24 | 3,139 | 1,779 | 2,208 | 2,208 |
| 25 | 2,188 | 1,070 | 1,070 | 1,325 |
| whole | 103,320 | 52,768 | 59,815 | 62,612 |

Chapter 1 exceeds its baseline because three of the notes its list names
([10], [13], [22]) were footnotes before the pass and are body text now.
"After round 2" includes round 1b. Chapters not in the table are unchanged.

## The order of work

- **Round 1 (D-916), applied 2026-10-19:** job one's lists. 38 block notes
  restored by `promote.py` (6,811 words), four pre-pass footnotes unwrapped
  ([10], [13], [22], [656]) with hand joins, and the two Palantir sentences
  moved out of [41] into the body (the list's "[45]–[46]"). [89] restored
  whole into chapter 3's recuperation bullet, which is where its question
  stood; [666] restored whole, the distillation's "compressed" left to the
  author. Coverage against the merge: 6,004 sentences, 6,003 exact, 1 near
  (the Gleichschaltung lead-in, a run-in head again), none missing. Renders
  in `~/book-scratch/p223/`.
- **Round 1b (D-917), applied 2026-10-19, on the author's word:** the
  notes the distillation names in its four classes and not on its lists:
  [163], [167], [169], [229], [404] (whose second paragraph it cited as
  [406]), [558], [560], [865]; 1,387 words. [166], the lyric, a pre-pass
  footnote, stays one.
- **Round 2 (D-917), applied 2026-10-19:** the six note-only definitions
  moved to the body at their marks (normalization of deviance, preference
  falsification, hermeneutical injustice, failure by formation, doulia, the
  Three Rs); the cross-reference hunt, a scratch script over every `\ref`
  read by hand, and the eight texts it found behind a reference brought up
  ([961]'s first paragraph, [375], [237]'s third paragraph, [223], [242],
  [673], [628], [210]); drafts of the preface's one thing and of openings
  for chapters 19 and 28 in `~/book-scratch/p223/round2-drafts.md`, for the
  author's reading, not in the manuscript. Coverage against the merge:
  6,003 of 6,004 exact, 1 near, none missing.
- **Round 3a (D-918), applied 2026-10-19, on the author's word:** the
  three drafts rolled in (the preface's one thing; openings for chapters 19
  and 28); the three citations opened on the web and recorded, not marked,
  with `mo2026sb859` added for the Missouri bill. After it: the preface
  1,946 words, chapter 19 5,071, chapter 28 2,335, the whole 63,347.
  Coverage against the merge: 6,001 exact, 3 near (deliberate), none
  missing.
- **Round 3b (D-919), the author's rulings:** Appendix C.2 stays; the
  glossary to the front is deferred; the author note is matter for the note
  on method (`next.md`, cluster 5), and whether the funding goes in the text
  is undecided; the stage dates in chapter 28 are put to him with the
  sentence in hand. Still on his ask: cluster 6's front-matter line and the
  located-passage pass.
- **Commit and proofs (D-920):** rounds 1 to 3 committed as `7f70db4f` and
  in the proofs of 2026-10-19 (460 pages).
- **Round 4 (D-921), applied 2026-10-19, on the author's word ("please
  tackle cluster 2"):** cluster 2's remaining items. The door into Part IV:
  the last three sentences of §16.7's residual-risk paragraph moved to Part
  IV's title page as a `\partintro` (new macro, the device of Part VII's
  epigraph), with a hinge restating the limit and the position no person
  can fill in time; §16.7 now ends at "under total capture no instrument
  is." The evidence paragraph in chapter 4, after the prevent / arrest /
  detect / remedy table: which rows the measures keep with no refuser in the
  room. The guarantee's dependence in chapter 10, after the annotators'
  paragraph: the right as remedy, the guarantee as exit, the fifth measure
  as two things. §31.4: the happy slave's objection named in three
  sentences, the smallest form of the distillation's optional expansion.
  Cluster 2's two open items are settled by the preface the author rolled
  in at D-918: measure five keeps both the right and the guarantee, and the
  preface says property while the body's conditional stands unchanged.
  After it: chapter 4 1,461 to 1,625 words, chapter 10 410 to 601, chapter
  16 2,808 to 2,881 (the part page's 118 words counted with it, less the 45
  moved out), chapter 31 2,382 to 2,445, the whole 63,347 to 63,838.
  Coverage against round 3: 6,036 of 6,037 exact, 1 missing, the reworded
  "Every instrument in this book ends at this limit"; against the merge
  6,000 exact, 3 near, 1 missing, the same sentence.
- **Round 4b (D-922), applied 2026-10-19, on the author's word ("please
  do"):** cluster 6's front-matter verification line. The title page says,
  in every build and not only in draft mode, how many of the bibliography's
  entries a human has checked against the source each names and where the
  ledger is, from the two counts `refs_ledger.py` generates; the grey draft
  stamp on the title page loses its count, so the number is there once.
  Uncommitted, with round 4.
- **Close:** the author's reading; the commit; the tag; the proofs.

## What this pass has not done

As of D-922: rounds 1 to 3 are committed (`7f70db4f`) and in the proofs;
rounds 4 and 4b are in the tree, uncommitted. Not done: the author's reading of the
restored book; the two deferred items, the glossary to the front and the
stage dates, which stay as they are until he decides; the compression of
[666]–[672], restored whole; the register ruling and the leitmotifs. The
court program stays on his ruling (D-920). The lyrics license is not the
agent's to obtain, and the dialogue quotations are unchecked against the
broadcast (D-680). Cluster 6's tag, located-passage pass and
reference-checking ask wait on his word; its front-matter line is done
(D-922).
