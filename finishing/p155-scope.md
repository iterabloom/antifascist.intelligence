# P155 — the structural pass: the instrument, the measurement, and no edit

Author note: four recent edits were the same defect — a two-sided finding whose
second side arrives after a sentence that already reads as a conclusion, so the
second side is discarded. §2.1.2's detector paragraph, §2.3.1's qualifications,
§9.1.5's disanalogy, §11.1's near-term work. **The general fix is to state the
trade-off before the epigram**, and *any pass that goes looking for a quotable
sentence followed by a qualifying one, and inverts them, will catch most of this.*

**This pass changes no prose.** What it produces is an instrument, a measurement of
the proposed test, a correction to the generalization, and one question.

## The four, checked

**Three are the shape.** D-234's own note on §2.1.2 records it in the author's
words before the author had them: *the epigram between the two failure directions,
so the second arrived after the line that reads as a verdict and a reader who
stopped at the quotable sentence stopped one failure short.*

**§2.3.1's is not an instance.** D-239 moved the second of three qualifications
first, so the reader met the criterion's instability before its consequences.
**There was no landing line among them.** It is the family's sibling — order the
heaviest limit earlier — and not the same defect.

**All four were repaired by the passes that named them**, at P134, P139, P147 and
P148.

## The instrument

`finishing/tools/epigram.py`, stdlib, not in `check_all.sh`. Two modes for two
readings of the shape:

- **the default**, a short or balanced sentence immediately followed by one that
  qualifies it — the author's test as stated;
- **`--tails`**, a sentence whose limit arrives in a trailing subordinate clause —
  the shape D-247 actually repaired.

It marks whether the qualifier is the paragraph's **last** sentence, because a limit
in final position is emphatic and not discarded. One bug was found and fixed during
the reading: `\runin` heads were joining the sentence after them, which gave §11.3 a
14-word landing line that was a head plus a 5-word sentence.

## The measurement, which is the finding

**125 pairs in 59 sections; 85 mid-paragraph, 40 paragraph-final. 289 tails in 84
sections.**

**Hand read: all 5 `balanced` pairs — `style.md` §7's epigram proper, in 99,568
words — every pair in the four named sections, every pair in the two densest (§3.3
at 10, §11.3 at 7), and the top tails. Zero clear instances of the defect.**

What the pairs actually are, in the proportions the reading found:

- **A landing line that opens a gap the next sentence fills.** §2.1.2's surviving
  pair is this: *Better engineering fixes neither.* → *Both are governed by what the
  tool may output and to whom.* The verdict poses the question the next sentence
  answers, so nothing is discarded. **Inverting it would remove the question.**
- **Parallel list items and structural markers.** §11.3's *Both produce a channel…*
  → *Both produce a metric…*; §9.1.5's *The third is new here.* → its content.
- **Definition then consequence**, where the order is forced: §5.2.1's *Guilt
  attaches to an act; shame attaches to the self.* → *Both motivate correction, and
  they motivate it differently.*

**Two cases where the proposed inversion would make the prose worse**, which is the
part worth knowing. §5.2.1's definition has to precede what it explains. And
§6.3.3's paragraph ends *It is not evidence that anticipation, done well, produces a
number everyone will accept* — inverting puts the concession last and ends a
paragraph about expert non-convergence on a softening note.

## The generalization, corrected

**The four do not share "epigram then qualification." They share the second side of
a two-sided finding sitting in a weaker grammatical position than the first — and
the position is different every time:**

| pass | where the second side was |
|---|---|
| D-234 (§2.1.2) | after a line that reads as a verdict |
| D-239 (§2.3.1) | third of three qualifications |
| D-247 (§9.1.5) | a concessive tail inside one sentence |
| D-248 (§11.1) | the last of three prepositional phrases |

**That has no syntactic signature, and that is why reading found all four and a
pattern finds none.** It is the limit `inventories.py` already carries on the record
— the syntactic test missed the shape that produced the reading experience — and
the one `antithesis.py`'s docstring states about its own class.

**What the author's test does reliably find is the silhouette**: a short sentence
next to a limiting one. The census is worth keeping for that, and
`reports/epigram.tsv` carries it.

## The one live disagreement, filed as Q-110

**§11.1 is the case where the rule, read literally, inverts something this session
did this morning.** P148 put the held-out-set requirement *after* *making the attempt
is a condition of building a bearer at all*, on the chapter's pattern of closing an
experiment on its institutional condition. **The rule says the trade-off goes
first.**

**`epigram.py` cannot see it** — the conclusion sits inside a 35-word sentence, over
the 24-word ceiling, which is the blindness the docstring declares.

**I did not invert it**, and Q-110 has the reasoning: the memorable line is
mid-paragraph where a reader continues, and the limit is in the emphatic final
position, so the mechanism the rule exists to prevent is not operating. That is a
judgment about one paragraph and it is the author's to overrule.

## Verification

Suite green. **No manuscript file changed**, so no build was needed for a prose
check; the suite was run for the tool and the report. `epigram.py` is stdlib-only
and reads the sections the way `antithesis.py` does.

## Figures

133 sections, **0 changed**. 99,568 words, 196 pages, 231 cross-references, 324
bibliography entries — all unchanged. One new tool, one new report, one new
question.
