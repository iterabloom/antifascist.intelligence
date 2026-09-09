# Editorial reviews

The source text of the outside editorial reviews the book was revised against.
Kept because `AGENTS.md` describes this repository as the book **plus the
complete record of how it was made**, and until 2026-08-24 the reviews existed
only in temporary files while the responses to them were fully documented.

**Read-only, like the rest of the provenance record.** These are received documents. Do not edit,
renumber, "correct" or reformat them — including the section numbers inside
them, which are the numbering in force when the review was written and are
therefore *pre*-D-031 and *pre*-D-043. Use `renumber-map_2026-08-23.tsv` and
`renumber-map_2026-08-24.tsv` to translate. What the book actually did with each
review is in the matching `p*-scope.md`, which is the authoritative record;
these files are the input, not the verdict.

## What is here

| File | Review | Answered by |
|---|---|---|
| `review-for-p7_2026-08-23.md` | The first editorial review, read 2026-08-23 | P7 — `p7-scope.md` |
| `review-for-p7-appendix-first-rule_2026-08-23.md` | Pointer to the appendix attached to it, held upstream — see below | P7 — `p7-scope.md` |
| `review-for-p11_2026-08-24.md` | The sixth editorial review, 2026-08-24 | P11 — `p11-scope.md`, D-043 |
| `revision-plan-for-p20_2026-08-25.md` | The revision plan distilled from the seventh review and the discussion after it, supplied by the author 2026-08-25 | P20 — `p20-scope.md` |
| `author-discussion_2026-08-28.txt` | A recorded discussion between the author and a language model shown the 194-page PDF, 2026-08-28. Not a review — see below | P26 — `p26-scope.md`, D-077 to D-080 |
| `author-discussion_2026-09-02.md` | An editorial review and the discussion after it, from a language model shown the 183-page proof, 2026-09-02. **Excerpted by the author** — see below | P88 — `p88-scope.md`, D-181 |
| `author-discussion_2026-09-05.txt` | Four questions from the author to a language model, on whether compassion needs empathy, whether perspective-taking is empathy, whether caring is a feeling, and whether deliberation is one, with the model's answers, 2026-09-05. Not a review, and not shown the book — see below | P107 — `p107-scope.md`, D-205 |
| `author-discussion_2026-09-06.txt` | The device a fourth time and much the longest, at 3,896 lines: chapter-by-chapter recaps of the book and the discussion that ran off them, from a language model shown the manuscript at its 187-page state, 2026-09-06. **Excerpted by the author.** Not a review — see below | P119 and P120 — `p119-scope.md`, `p120-scope.md`, D-217 to D-220 |
| `author-discussion_2026-09-07.txt` | The device a fifth time and much the shortest, at 374 lines: one critical review of the whole book and four author turns against it, from a language model shown the manuscript at its 188-page state, 2026-09-07. Not a review in the numbered series — see below | P121 to P123 — `p121-scope.md`, `p122-scope.md`, `p123-scope.md`, D-221 to D-223 |
| `author-discussion_2026-09-09.txt` | The device a sixth time, at 600 lines: one review of the whole manuscript and fourteen author turns arguing with it, from a language model shown a pre-P158 manuscript, 2026-09-09. Not a review in the numbered series — see below | P158 — `p158-scope.md`, D-258 |

Files are named for the pass that answered them, not by review number, because
the numbering has a gap (below). Date suffixes are the source files' own
last-modified dates, per the `AGENTS.md` filename convention.

## The appendix, and why it is a pointer

`review-for-p7_2026-08-23.md` arrived with an appendix attached: an excerpt from
the documentation of **a different software project**, cited in the review as
`docs/fascism/the-first-rule-of-fascism.md`.

That appendix is load-bearing provenance. It is the source of the four-feature
structural signature of fascism — recuperation of dissent, aestheticization of
the metric, exception coded as betrayal, decoupling of the model from the world
it claims to track — and of the *slope, not the level* instrument. Those became
§2.1.4 and §8.6.4, which are among the most-cited passages in the book.

**By the author's instruction (D-049), the file holds the upstream URL rather
than a copy of the text.** The source is public and versioned at its origin, so
a pointer preserves the provenance without duplicating another project's
documentation into this repository — and without carrying that project's
operational detail, which the copy did. The link was verified live on
2026-08-24: it resolves, and it carries both the four features and the slope
argument, in the words above.

A URL is a weaker guarantee than a copy — it can move or go private. The claim
it supports is recorded independently here and in D-048, so what the appendix
contributed to the book survives in this repository even if the link does not.

## What is NOT here

**The second, third, fourth and fifth reviews were not preserved.** They existed
only in temporary files, which are gone. What survives of them is the quotation
and disposition inside `p8-scope.md`, `p9-scope.md` and `p10-scope.md` — which
records what was checked, what was accepted, and what was declined with reasons,
but is not the source text.

**The numbering has a gap.** `p8-scope.md` answers "the second editorial review"
and `p9-scope.md` answers "the fourth." No pass is recorded as answering a third.
Whether a third review was folded into P8, or the count simply skipped, is not
determinable from the record. It is written down here rather than smoothed over.

**Six files here are not reviews.** `author-discussion_2026-08-28.txt` is a
transcript of the author thinking aloud with a language model that had been given
the finished PDF and nothing else — no `finishing/`, no decision log. The prompts
are the author's; the completions are the model's. It is kept for the same reason
the revision plan is: the four rulings in D-077 to D-080 came out of it, and
`p26-scope.md` records what was checked against the manuscript and what did not
survive checking. Two of the model's claims about chapter 6 correspond to nothing
in the text and are identified there; nothing in the file is a finding until it
has been checked.

`author-discussion_2026-09-02.md` is the same device a second time, and its header carries two things this
folder has not had to record before. **It is an excerpt**: the author removed some of the model's completions
before supplying it, so the file is verbatim in what it keeps and silent about what it drops. And **one
speech-to-text error in an author prompt is preserved rather than corrected** — *shit* for *ship* — because
the model answered the text as transcribed. `p88-scope.md` records which of its claims were checked against
the manuscript, which held, and which did not; four of its bibliography findings were repaired at D-181.

`author-discussion_2026-09-05.txt` is the device a third time, with one difference: the model was shown nothing of the
book. The four prompts are the author's and the four completions the model's, kept whole and verbatim, blank lines
included. It was supplied on 2026-09-05 with the question of what its points were worth to the book, and the answer,
with what was checked against the manuscript and what was taken, is in `p107-scope.md`. Its factual claims are a
model's until a source is opened; the works it names were verified separately before any entry was written. The real
people it names are named as scholars, which is ordinary citation under `AGENTS.md`, and the names guard lists them as
citations to confirm.

`author-discussion_2026-09-06.txt` is the device a fourth time and much the longest of the four. The model was shown the
manuscript, and most of the file is its recaps of chapters 3 through 12 and the appendix, with the author's questions running
off them into exit, migration, compute, wages, personhood, cryptographic self-licensing and autonomous weapons. **It is an
excerpt in five places**, and the author's bracketed notes say so and say why: the attached manuscript, one whole completion,
some back-and-forth, and three passages he removed on their content rather than their length. What was taken from it is in
`p119-scope.md`; the editorial recommendation it closes on — cut ten to fifteen thousand words — was executed and came in at
2,372, and `p120-scope.md` records why, with D-219 and D-220 correcting the first account of that.

The recaps are a model's summaries and were checked against the text before anything was taken from them; `p119-scope.md`
records how the manuscript it saw was dated, which matters because two of its findings would read differently against an
earlier draft. Its factual claims are a model's until a source is opened. The real people it names are named as scholars,
which is ordinary citation under `AGENTS.md`, and the names guard lists two of them to confirm — both from the chapter 9
recap, describing a documented dismissal the book already cites at §9.1.2.

`author-discussion_2026-09-07.txt` is the device a fifth time and much the shortest of the five, at 374 lines
against the previous file's 3,896. The first completion is a critical review of the whole manuscript, delivered in
one pass and reaching a verdict — that the constitutional argument is strong and the affective-bearer inference is
not yet earned — and the four author turns after it argue with that verdict rather than collecting more of it. Only
the attached manuscript is omitted, marked in the author's own bracket on line 3; nothing else is excerpted.
**It was filed late, at P126 on 2026-09-08**, the three passes it drove having been written up without it; the
delay is a gap in the record and not a judgment about the file.

`author-discussion_2026-09-09.txt` is the device a sixth time: one completion reviewing the whole
manuscript, then fourteen author turns arguing with it, over §3.6's worked case, whether decomposition
argues for a bearer or against one, transhumanism, and whether anyone has shown a frontier model lacks
affect. **Only the attached manuscript is omitted**, marked in the author's own bracket on line 3;
nothing else is excerpted.

**Which draft it saw is settled in one direction and not the other.** It quotes §3.6's pre-P158 finding
twice — *a hint about where to look* — so the manuscript it read predates P158. **Whether it predates
P157 is not determinable from the file**: it names no front-matter content at all, so the replacement
of chapter~0 with the Foreword leaves no trace in it either way. That is written down rather than
guessed.

Two things about it are worth having in front of anyone who opens it. **Its headline objection was
withdrawn under a leading question** — that §3.6 damages the thesis, given up when the author asked
how any of it works against the argument for a bearer — which is the failure §11.5 documents. The
withdrawal is reasoned rather than accommodating, since the same model held §3.2's relocation objection
through three presses and argued back on the author's *no harm no foul* branch; but nothing in the file
is a finding until it has been checked. And **it is wrong about what §3.6 already says**, reporting the
section settling for an operator duty when `:42` already carried *A floor written over acts had no
survivor here at all*.

What was taken is in `p158-scope.md`: two of its four proposals were executed and two filed as Q-112
and Q-113. **Its other eight findings were not verified against the manuscript and are not filed**, and
`p158-scope.md` lists them so that is visible. Its factual claims are a model's until a source is
opened. The real people it names are named as scholars, which is ordinary citation under `AGENTS.md`,
and the names guard lists none of them.

Two things about it are worth having in front of anyone who opens it. **The model read the current book**, which
`p121-scope.md` establishes and which the previous transcript's model did not — 309 references and §8.3.5 material
written the day before are both named in it, so its cut estimates are costed against the manuscript that existed.
And **four of its five objections describe passages that already exist**; D-221 lists them so a later pass does not
reopen them, and `p121-scope.md` records which of its findings were live. Its factual claims are a model's until a
source is opened.

`revision-plan-for-p20_2026-08-25.md` is a plan distilled from a review and the discussion following it, and it arrived with the author's ruling that it overrides conflicting decisions (D-061). Its section numbers are post-D-043 and need no translation. Three of its items were struck by the author against its own text; `p20-scope.md` records which and why.
