# Redundancy findings

Generated from `redundancy_sections.tsv`, `redundancy_paragraphs.tsv`,
`redundancy_2.4_vs_7.4.tsv` (`finishing/tools/redundancy.py`, offline
sentence-transformer, cosine similarity).

## How to read the numbers

Every section of this book is about one subject, so the baseline similarity is
high: the median section-to-section cosine is **0.691**, p90 is 0.812, p99 is
0.883, and the maximum is 0.955. A fixed threshold would therefore be
meaningless. What follows uses the top 200 section pairs (0.894–0.955) and the
top 400 cross-section paragraph pairs (0.829–0.933). Paragraph-level baseline is
much lower — median 0.443, p99 0.721 — so a paragraph pair above 0.83 is a
genuine near-restatement, not a domain effect.

An earlier lexical pass found **zero verbatim duplication**. Nothing here was
copy-pasted; the book says the same things again in different words.

## Finding 1 — there are duplication *hubs*, not duplicate *pairs*

Ranking sections by how often they appear in the top 200 pairs (cross-chapter
count first):

| Section | Cross-chapter pairs | Title |
|---|---|---|
| 5.4.3 | 13 of 13 | Promoting AI Development Policies that Discourage Authoritarian Use |
| 4.6.3.1.2 | 11 of 14 | Strategies for Developing AI Systems Committed to Democratic Principles |
| 7.2.5.3 | 10 of 11 | Encouraging Global Cooperation in the Development of Anti-Authoritarian AI |
| 2.3.1 | 10 of 12 | Components of Emotional Intelligence |
| 4.2.2.1 | 9 of 12 | Challenges and Opportunities in Emotional AI Systems |
| 10.1.3 | 8 of 9 | Fostering a Global Commitment to Ethical and Anti-Authoritarian AI Development |
| 4.2.2 | 8 of 10 | Assessing and Developing AI Emotions |
| 8.2.1 | 6 of 9 | Promoting Cooperation and Responsible AI Development |
| 6.4.1.12 | 6 of 7 | Establishing Shared Ethical Principles for AI Development |

Two clusters account for most of it.

**Cluster A — "promote democratic values through international cooperation."**
`5.4.3`, `7.2.5.3`, `4.6.3.1.2`, `10.1.3`, `8.2.1`, `8.2.3`, `8.3.1`,
`6.4.1.12`, `10.3.2.1`. Nine sections spread across six chapters that make the
same recommendation in the same shape. `5.4.3 ↔ 7.2.5.3` scores 0.950 —
the second-highest pair in the book. Every one of `5.4.3`'s thirteen appearances
is cross-chapter, meaning it has no local relatives: it belongs to this cluster,
not to its own chapter.

**Cluster B — "emotional intelligence and affective computing."**
`2.3.1`, `2.3.2`, `4.2.2`, `4.2.2.1`, `3.1.2.3.1.10`, `9.2.3`. Note that `2.3.1`
is a **47-word stub** yet appears in ten cross-chapter pairs — the material it
should contain is written elsewhere, three times.

This changes what the cut is. It is not "merge these two sections"; it is
"decide where each of two recurring arguments lives, write it once, and cut the
other seven or eight instances."

## Finding 2 — §2.4 and §7.4 are one treatment written twice

The single highest-scoring section pair in the entire book is
**`2.4.4.1` Informed Consent in AI Research ↔ `7.4.3.1` Ensuring Informed
Consent and Respect for AI Autonomy, at 0.955.**

Across the full 21 × 10 grid (308 pairs), nine sit above the book-wide p99:

| Score | §2.4 side | §7.4 side |
|---|---|---|
| 0.955 | 2.4.4.1 Informed Consent in AI Research | 7.4.3.1 Ensuring Informed Consent and Respect for AI Autonomy |
| 0.923 | 2.4.6.1 Identifying and Assessing Dilemmas | 7.4.3.2 Balancing Scientific Progress with Ethical Constraints |
| 0.919 | 2.4.2.2 The Principle of Autonomy | 7.4.3.1 Ensuring Informed Consent… |
| 0.912 | 2.4.3 Balancing Scientific Progress and Ethical Constraints | 7.4.3.2 Balancing Scientific Progress with Ethical Constraints |
| 0.909 | 2.4.4.5 Promoting a Culture of Ethical Responsibility | 7.4.3.2 |
| 0.898 | 2.4.2.6 Interdisciplinary Ethical Review and Oversight | 7.4.3.2 |
| 0.896 | 2.4.4.1 Informed Consent in AI Research | 7.4.3.1.1 Establishing Criteria for Informed Consent |
| 0.889 | 2.4.6.5 Promoting Ethical Responsibility and Transparency | 7.4.3.2 |
| 0.885 | 2.4.7.4 Educating Stakeholders and Fostering a Culture… | 7.4.3.2 |

`7.4.3.2` appears six times in that list: it is a compressed restatement of most
of §2.4. And `2.4.3` and `7.4.3.2` carry nearly the same title, which an earlier
lexical pass also caught (`2.4.3` ≡ `2.4.4.3` ≡ `7.4.3.2` by title alone).

Neither section cross-references the other anywhere.

## Finding 3 — a parent and its child share one title

`3.1.2.3` and `3.1.2.3.1` are both "Cognitive and Emotional Processes" —
identical strings. The subtree beneath them is also where the outline reaches
six levels deep, and where the spreadsheet and the manuscript disagree about the
title of `3.1.2.3.1.11` (Q-006). The whole subtree needs restructuring, not
trimming.

## What this does not settle

Which home each cluster should have. That is an authorial decision, and it is
the substance of Phase 3 triage. The reports give the evidence and the candidate list;
the ledger's `action` column records the ruling.

Also unchecked: paraphrase-level redundancy that shares neither wording nor
embedding neighbourhood (nothing catches that but reading), and redundancy
between the manuscript and the 2026 quarry.
