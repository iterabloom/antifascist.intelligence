# P30 — §10.3's cases moved into chapter 6; the conclusion synthesizes

**The author's instruction, 2026-08-28:** move much of §10.3 into chapter 6; a
conclusion should synthesize rather than introduce another substantial collection
of cases.

The diagnosis holds and the share was larger than "much" suggests. Section 10.3
was 2,627 words of a 5,427-word chapter — **48 percent of the conclusion** — and
all of it was case material: red-teaming records, an exam-grading scandal, a
forecasting tournament, a healthcare algorithm, proctoring software, a retraining
programme evaluation, a messaging limit, a rescue-robotics league, and the
Apple–FBI order. Chapter 10 introduced more new cases than chapter 6 did.

## What moved, and where

| was | is | why there |
|---|---|---|
| 10.3.1 Anticipating Risk Before It Causes Harm | **6.3.5** | 6.3 is *AI Safety, Unintended Consequences, and Risk Mitigation*, and this is what finding a failure before release looks like |
| 10.3.2 Remediating a Harm Once It Is Identified | **6.3.6** | the same section, one step later: the harm already reached someone |
| 10.3.3 Resilience Against Deliberate State Compromise | **6.4.4** | 6.4 is *Preventing the Misuse of AI for Authoritarian Purposes*, and its opener already named this case and had nothing behind it |
| 6.3.5 Long-term AI safety considerations | **6.3.7** | moved down two to make room; it still closes 6.3 |

`finishing/renumber-map_2026-08-28.tsv` is the map. **No moved prose was
rewritten.** Labels changed, and 16 `\ref` across the book were repointed — 4 to
6.3.5, 4 to 6.3.6, 6 to 6.4.4, and 2 to 6.3.7. The moved sections' own pointers
into chapter 6 (6.1.1, 6.1.2, 6.1.3, 6.2.2) were written as references to another
chapter and now read as references within one, which is what they should have
been: three of the four already said *this section covers the case* about material
two sections earlier in what is now the same chapter.

Section 6.3 now runs: the alignment problem, deception, strategies, explainability,
anticipating risk, remediating harm, the long run. Mechanisms, then practice, then
the long run. Section 6.4 now runs: what authoritarian misuse looks like, technical
countermeasures, policy, and then the case where a state does not need any of it
because it can compel the people holding the system.

## What replaced §10.3

A synthesis, 340 words, with no cases in it. It keeps the number, is retitled from
*Addressing the Unintended Consequences* to **The Risk That Does Not Design Out**,
and makes two claims the moved material supports and never stated:

- In none of the chapter 6 cases did the fix come from the party that had promised
  to behave well. It came from somebody holding a specific lever — a research team
  with the vendor's own data, universities exercising a purchasing decision, a
  company choosing a blunt technical limit, an organization that ran the test
  nobody inside had run. Section 10.1.2 counts what a decade of voluntary
  commitment produced beside that, and section 8.6.4 is the instrument that
  separates them.
- Every lever belongs to somebody, and a government that can reach the party
  holding the lever has the lever. That is the residual risk the book cannot
  design out, and it is why the argument ends where chapter 3 ends.

That second point is the conclusion's own work and it was not being done. Section
10.3.3 contained the material for it and stopped at the observation.

## Three openers adjusted

- **6.3** said two mechanisms carry weight "and the rest is ordinary engineering
  practice," which stopped describing a section that now carries the case material
  too. It names the turn from mechanisms to practice instead.
- **6.4** promised "three things in sequence," the third ending on a government
  that can disable whatever safeguard stands in its way. It promises four now, and
  the fourth is the one 6.4.4 argues: the government that does not have to disable
  anything, because it can compel the people who hold the system.
- **10** said section 10.3 asks what could still go wrong. It now also says what
  the failure cases have in common, which is what that section does.

## Numbers

| | before | after |
|---|---|---|
| chapter 6 | 8,184 words, 18 sections | 10,790 words, 21 sections |
| chapter 10 | 5,427 words, 11 sections | 3,155 words, 8 sections |
| the book | 91,060 words | 91,394 words |

188 pages, unchanged. 801 `\ref` resolve. The book grew by 334 words: the synthesis
is 234 words longer than the frame it replaced, and the three openers account for
the other 100.

**A correction to the P29 record.** P29 reported 91,037 words. `section_stats.tsv`
was regenerated before three small P29 fixes landed — the stranded list pointer in
2.4.1, the opener repair in 4.1.3, and the restored theory name in 5.2.1 — so the
tree at P29 was 91,060. The page count P29 reported, 188, was measured from the
built tree and is right.

## What was not checked

- Whether chapter 6 now reads as one chapter rather than a chapter with three
  sections appended. Two pages were rasterized and read — the 6.3.4/6.3.5 seam and
  the new 10.3 — and the rest was not.
- Whether anything elsewhere refers to the moved material by description rather
  than by number, which no tool detects. Ten of the case names were searched for
  outside the moved files. Ofqual, Obermeyer, Optum, Proctorio, RoboCup,
  TaskRabbit, Global Witness and the forecasting tournament appear nowhere else.
  WhatsApp and Apple do, at 8.3.2, 8.4.2 and 8.5.1, in uses that have nothing to do
  with the moved sections — an acquisition, a Partnership on AI membership, and
  differential privacy. The one section that cited the moved material by number,
  8.3.3 on the retraining evaluation, was repointed with the rest.
- `xref_content.py` was not re-run.
