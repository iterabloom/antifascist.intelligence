# P111 — a session of author findings: one wording ruling, the epigraph and its rights, the reader map, two glossary contradictions, the bibliography's address to the author, and seven fact-checks

**The instruction.** Not one instruction but eight, taken in order across a sitting, each with the
author's finding stated and the repair left to the session. They are recorded here in the order
they arrived, because several of them turn on what an earlier one established.

## What was done

### 1. §3.3's *stupid sense of the word sincere*

**Ruling: *change "stupid" to "enjoys-eating-one's-own-feces"*.** Applied at `03_03.tex:27`. The
register drop was reported once, with the precedent that covers it — D-198 and Q-079 record the
author ruling three register departures part of the book's voice — and then the change was made
without further argument. It lands as the last sentence of the paragraph carrying the *Wilcox*,
*Cook* and Menand reading, which is where a drop of that kind does the most work and the least
damage. §3.1 now states the same argument in a straight register and §3.3 needles it, twelve pages
apart, and the two sentences no longer match by design.

A preceding question on §3.1's *the party feels no dissonance, no shame* was answered and not
executed: **the recommendation was to keep *shame*** and it stands unruled. *Scruples* imports
*unscrupulous* — knowing better and proceeding — which is the venality reading the sentence's own
first half declines, and a scruple is prospective where dissonance and shame are what fail to
arrive afterward. §5.2.1 defines shame as attaching to the self, which is what ties it to the
clause that follows it.

### 2. The chapter 1 epigraph and the license

**Ruling: *add the carve-out and keep the epigraph as accepted risk, but drop the first two
stanzas*.** The finding put to the author first: a credit line does not change the legal position,
because copyright is permission and not credit; the rights holder for printed lyrics is the music
publisher and not the record label; and the taking was 9 typeset lines of about 38 words, smaller
than *roughly a dozen lines* suggests.

- **The epigraph is the third stanza alone**, 11 words, and it lands directly on the sentence it
  was always answering. The lowercase *i've*, a transcription artifact carried since 2023, was
  corrected to *I've* — **a change the author did not ask for, reported as such**. The opening
  *'Cause* is kept, because an epigraph taken from mid-song is honestly signalled that way.
- **The carve-out** is on the title page (`preamble.tex:72`) and in `README.md:47`: third-party
  material quoted in the work, including the epigraphs to chapters 1 and 6, remains its rights
  holders' and the CC BY-NC-ND license does not extend to it. The README was done unasked, on the
  reasoning that a carve-out living only in the PDF leaves the blanket claim standing where the
  public actually reads it.

Chapter 6's epigraph needs nothing: a short quotation from a published book, cited, with the book
arguing against it on the same page.

### 3. The reader map in chapter 1

**Ruling: *on the book's actual weight the spine is 2 → 3 → 7 → 11 → 12; 4–5 are the learned half;
6 and 8–10 are institutional context. Say that.*** Said, in the author's own words and with no
gloss, because the roadmap paragraph above it already says what each chapter does and re-glossing
is the shape P36 cut. The measured weight supports the ruling on chapter 3 at 21.0 percent of the
book and not on chapter 7, **which is 4.6 percent, the second-smallest substantive chapter, below
chapter 6 and every one of 8 through 10** — so the spine claim is about argumentative load, and
the asymmetry is on the page for a reader to notice.

The roadmap paragraph above it still pairs chapters 6 and 7. It was read as compatible rather than
contradictory — that sentence describes reading order and already splits them inside itself, the
list belonging to 6 and the final clause to 7 — and **left alone, with the repair named**.

This settles rows 7 and 8 of `~/book-scratch/roadmaps.md`, leaving sixteen, and it is the one
place in the session where references were added rather than removed.

### 4. Two glossary entries against the text

**Both reconciled in favor of the text, because in each case the text is what the argument does.**

- **Bearer** claimed a bearer must be governed as a prospective moral patient *in the strong sense
  of sentience below*. The Sentience entry defines no strong sense and **no such sense is defined
  anywhere in the book** — the only other *strong sense* is §4.1.2's, about honest memory. The
  clause is gone, and the entry now carries §3.10's own summary of the chapter: the conclusion
  does not depend on the deepest account, and a reader who declines Cassell's import reaches it
  sooner rather than escaping it. §11.2 already stated the claim unqualified.
- **Antifascist** said the word was *chosen over the broader anti-authoritarian*, where §2.1.2 says
  the target is authoritarian power in every form. The reconciliation is a narrow concept and a
  wide target, and the entry now says both. *Not a softer substitute* went with it, being the
  *not X but Y* frame style.md §2 rules against. `anti-authoritarian` appears in exactly two places
  in the book, so there was nothing to propagate to.

### 5. The bibliography's address to the author

**Ruling: *convert to reader-facing annotations or strip*, and *remove "(Visited on …)" from print
books*.** A sweep of all 199 note and addendum fields found **eleven** entries written to the
author rather than to a reader; the author had named five. Two of the eleven were found only on a
second pass, having sat beyond the first sweep's character window. The word *manuscript* now
appears nowhere in `refs.bib` and no note names another entry by bibkey.

**Two disclosures were kept deliberately** and reported: the Harvard schedule's account of being
reconstructed from search-index snippets, and Kitwood's note that the page number rests on
convergent secondary citations rather than a copy of the 1997 printing. Both tell a reader how far
to trust the entry, which is not a verification log.

**The access-date defect was wider than the three books named.** Twenty-five entries carried a
`urldate` with no `url`, so biblatex printed a bare *(Visited on 08/25/2026)* attached to nothing —
Gilligan and Cassell among them, but also Piaget, Vygotsky, Russell, Gray, three Restatements and
fifteen DOI-only articles. The field was removed from all 25, and then from thirteen print entries
that do have a URL, on the author's stated rule. **38 entries changed; the bare form is gone, 25 to
0.** The 236 remaining lowercase instances are all attached to an actual URL on an online source.

### 6. Seven fact-checks, each verified against the source

| site | finding | outcome |
|---|---|---|
| §2.2.1 | the Trobriand gasping-face result is Crivelli et al. 2016, not Gendron et al. 2014 | **upheld.** The sentence made two claims under one citation; Himba → Gendron, Trobrianders → Crivelli. `crivelli2016fear` added as a real entry, its details confirmed against PNAS metadata |
| §4.2.1 | the 1.3B-preferred-over-175B result is the full RLHF pipeline, not SFT alone | **upheld.** The abstract is explicit that InstructGPT is demonstrations *then* RLHF. The paragraph says so and hands the other half to the next section; the two sentences leaning on it followed |
| §5.1.3 | *tripled the state's error rate* for Indiana | **upheld.** No source reports it. Eubanks reports more than a million denials in three years, a 54 percent increase over the three before — which the bibliography entry already said |
| §6.3.4, §8.3.3 | Jacobs & Canedy 2026 cited twice as settled | **upheld.** arXiv 2605.03767, posted 5 May 2026, no journal reference and no DOI. Both sites now say preprint; the entry records it |
| §8.1.1 | MIRI *still running* but pivoted in 2024 | **upheld.** The 2024 Mission and Strategy Update, 4 January 2024, moves priority to policy and communications. A sentence and `miri2024strategy` added. Note that *outlasted its grant* attaches in that sentence to the Berkeley center, not to MIRI; the MIRI item is the Alignment Forum, which does remain active |
| §3.3 | *per inference* should say *per full inference proof* | **upheld.** The paper says *a correctness proof for the entire inference process in under 15 minutes*. Now *under fifteen minutes to prove one full inference* |
| §4.2.4 | *fifty coauthors* against the bibliography's *forty-eight* | **reversed.** arXiv 2212.08073 lists **51 authors**, Bai first and Kaplan last, so the manuscript was right and the entry was wrong. The entry was fixed, not the text |

**Two reference entries were authored in this pass** — `crivelli2016fear` and `miri2024strategy` —
each verified against primary metadata. `style.md` §6 and `PLAN.md` §3 still say the agent never
writes a reference entry; the practice changed no later than D-204 and D-205, which record verified
entries, and the rule has not been rewritten to match. **It is named here rather than edited.**

### 7. A defect found while in the file, beyond what was asked

In an `@article` entry biblatex prints `note` **between the issue number and the page range**, so an
annotated article renders as *"Autism in Adulthood 6.3. Seventy-six autistic adults on their own
empathy… pp. 321–330"*, and Laurie's ended *"…compares views., "*. Four entries were already doing
it: `frankfurt1982importance`, `kimber2024empathy`, `laurie2014ct`, `milton2012double`. Eighteen
other articles use `addendum`, which prints after the citation. All four were moved, plus the two
touched in this pass. **Reported to the author as beyond the seven fixes.**

## Numbers

**138 sections, 91,152 → 91,322 words; 187 → 186 pages; 19 → 18 overfull boxes; 130 → 138 prose
references; 319 → 321 bibliography entries; 0 undefined references; suite green at every step.**
Ten section files changed, plus `preamble.tex`, `refs.bib` and `README.md`. Every edit was applied
by exact single-match replacement and rebuilt before the next one.

## Left undone, named

- **§3.1's *shame* is unruled.** The recommendation to keep it stands; nothing was changed there.
- **The roadmap paragraph in chapter 1** still pairs chapters 6 and 7 against the reader map's
  split. Read as compatible, repair named, not applied.
- **Nobody has read any changed section end to end**, here or in P109's 111 and P110's 16.
- **The rows set aside at P109**, outside the repository: `roadmaps.md` now 16, `near-roadmaps.md`
  12, `collateral.md` 7. Each needs a ruling.
- **`reports/xref_shapes.tsv`, `reports/xref_pairs.txt` and `xref-paragraphs-*.md`** are stale, and
  the reference count moved again in this pass.
- **D-012's permissions task still does not exist.** It was promised in `PLAN.md` and is not there;
  the epigraph decision was taken in this pass without it, and the other two epigraphs it covered
  are long gone from the manuscript.
- **The eleven remaining `note`-in-`@article` entries without page numbers** were not touched; they
  render acceptably today and would break if pages were added.
- P103's four, the rest of P104's list, P105's one, Q-070 and Q-074 are as they were.
