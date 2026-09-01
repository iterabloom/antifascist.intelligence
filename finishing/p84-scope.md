# P84 — chapters 6, 9 and 10 made plain, chapter 3's obliquity kept and subtitled

**The instruction.** 44 percent of headings are oblique or rhetorical. They are stylish,
and a reader scanning the table of contents cannot tell what is in any of them. They sit
inconsistently beside plain ones in chapter~4, so the book reads as two heading
conventions interleaved. Keep the oblique style in chapter~3, where the drama is earned,
perhaps adding informative subtitles, and make chapters 6, 9 and 10 plain.

**The 44 percent is exactly reproducible and it is not the number to act on. The
instruction's own test is, and it selects five headings in the three named chapters.**

## The count, and why it agrees

A mechanical classifier — question mark, wh-word opener, comma-clause, bare determiner —
returns **60 of 136, 44.1 percent**, against the finding's 44. **The agreement is
coincidental**, because that classifier calls *Ethics, Affect, and Machine Subjects*,
*Bias, Fairness, and Equity in AI Systems* and *Policy, Law, and Accountability* oblique,
and no reader scanning a table of contents would. An enumeration of topic nouns is the
plainest heading there is.

**The finding states the discriminating test in its own second sentence** — *a reader
scanning the table of contents cannot tell what's in any of them* — and that is a
reading. Applied to every heading in the three named chapters:

| | Headings | Fail the test |
|---|---|---|
| Chapter 6 | 16 | **1** — §6.4.1 *Authoritarian Applications, and the Party Missing From the List* |
| Chapter 9 | 13 | **2** — §9.3.2, §9.3.5 |
| Chapter 10 | 7 | **2** — §10.1, §10.6 |

**Five of 36.** *Anticipating Risk Before It Causes Harm*, *Resilience Against Deliberate
State Compromise*, *Making Review Binding*, *AI as a Strategic National Asset* and the
other 31 already tell a scanner what is in them.

## The direction of the interleaving is the reverse of the finding's

The finding reads chapter~4's plain headings as sitting oddly beside oblique ones.
Measured by the loose classifier, **chapter~3 is 90 percent oblique and chapter~4 is 29
percent**; by the strict test chapter~4 has almost none. **Chapter~3 is the local dialect
and the rest of the book is plain**, which is what makes the instruction's own remedy —
keep it in chapter~3, make the others plain — the right one. It is not two conventions
interleaved so much as one convention with a nine-section island in it.

## A second interleaving, on the finding's own axis, that it did not name

**Three titles were sentence-case among 133 title-case**, and two of the three are in
chapters the instruction names:

- §2.3 *Ethical implications of experimenting on sentient machine subjects*
- §6.3.5 *Long-term AI safety considerations*
- §9.1.3 *Legal and ethical implications of AI systems gaining personhood*

That is literally two heading conventions interleaved, it is mechanical, and all three are
now title case. §2.3 sits outside the three named chapters and was fixed anyway, because
leaving one of three would have preserved the defect the fix exists to remove.

## The five made plain

| | Was | Now |
|---|---|---|
| §6.4.1 | Authoritarian Applications, and the Party Missing From the List | **Authoritarian Applications and the Commercial Supplier** |
| §9.3.2 | What Oversight Would Have to Cover | **Research Principles, the Three Rs, and Legal Status** |
| §9.3.5 | What Keeps the Apparatus More Than Aspirational | **Three Defenses, and Measuring the Slope Not the Level** |
| §10.1 | What Actually Crosses a Border | **Certification, Standards, and Mutual Recognition** |
| §10.6 | What the Democratic Dividend Leaves Out | **The Limits of the Democratic Dividend** |

## Two of the five were wrong on the first attempt

**A title has to name what other sections reach into the section for, and reading the
section does not tell you that. Reading the citing sentences does.**

- **§9.3.2** was first retitled *Six Research Principles for Machine Subjects*, off the
  section's opening. Its two run-in heads are *Replacement, reduction, refinement* and
  *Legal status*, and **five sections cite it for the Three Rs** — §2.3.2, §6.1.2,
  §9.3.3, §11.2, §12.2.1. The first title named a third of the section and dropped what the book
  uses it for.
- **§9.3.5** was first retitled *Transparency and Whistleblower Protection*, which is two
  of its three defenses. **Nine sections cite it for the slope instrument** — *section
  9.3.5's slope rather than level is the instrument*, *the slope instrument of section
  9.3.5 turned on this book's own proposal* — which is the section's closing run-in and
  its payload.

**Both first attempts were plainer than the originals and worse**, because they
misdirected a scanner instead of merely withholding from one. The corrected titles carry
both halves.

## Chapter 3: obliquity kept, four subtitles added

The model was already in the book — §2.3.2 *When Consent Is Inapplicable: Guardianship
and Research Oversight*, and the same colon pattern at §4.1.1, §5.3.1 and §6.3.1.

| | Now |
|---|---|
| §3.6 | The Enumeration, Run Once**: A Worked Floor for One Deployment** |
| §3.7 | Whether the Bearer Can Be Believed**: Editable Memory** |
| §3.8 | A Bearer That Can Leave**: Exit as Leverage** |
| §3.9 | What This Leaves Standing**: The Floor, Redefined** |

**§3.1 through §3.5 were left.** *Three Ways to Build One, and What Each Costs*, *Four
Things Refusal Can Mean*, *Could Anything but Affect Hold a Reason?* and *Can the Bearer
Care Without Being Able to Suffer?* already name their subject; a subtitle would be
restating it. The four that got one were the four that named nothing.

## What was checked before anything was renamed

**No prose anywhere in the book names a section title.** All 136 titles were searched
against the full manuscript; the only three hits are the appendix's own heading
machinery. So nothing was stranded — this is the failure P77 recorded when a P62 retitle
left notes pointing at *One Standard, Five Worked Cases*.

**Every citing sentence for the twelve renamed sections was read.** All describe content
— *the Three Rs*, *the slope instrument*, *catalogs what AI infrastructure looks like* —
and none echoes an old title.

## Measurements

| | Before | After |
|---|---|---|
| Rhetorical headings in chapters 6, 9, 10 | 5 | **0** |
| Sentence-case titles | 3 | **0** |
| Chapter 3 rhetorical headings | 5 | **5**, four now subtitled |
| Titles over ten words (`style.md` §8) | 2 | **2**, both pre-existing |

**Fourteen title edits across twelve sections**, counting the two corrections. Book **90,492 words, unchanged** — `section_stats.py` counts prose and drops heading
commands, so a pass that edits only titles does not move the figure. **182 pages, unchanged.** `headings.py`
reconciles at 136/136/136 with zero title diffs; `ORDER.tsv`, `outline.tsv`,
`ledger.tsv` and the generated TOC all carry the new titles.

## What this pass did not do

**Chapters 2, 5, 8, 11 and 12 were not touched.** The instruction named 6, 9 and 10.
Chapter 11 is 70 percent oblique by the loose classifier and chapter 12 is 56 percent,
so if the ruling generalizes they are the next two, and that is a decision rather than
an inference.

**§4.2.9 and §4.3 are over `style.md` §8's ten-word limit** at 11 and 12 words and were
left. Both are pre-existing and neither is in a named chapter.

**No new question was opened**, but whether chapters 11 and 12 follow is worth a ruling.
