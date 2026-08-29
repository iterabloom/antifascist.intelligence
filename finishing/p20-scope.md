# P20 — the revision plan

Source: a revision plan distilled from a seventh editorial review and the
discussion after it, supplied by the author with the ruling that it overrides
any conflicting decision or context in this repository (D-061). Three items
were struck by the author against the plan's own text and are not implemented:

| Struck | The author's reason |
|---|---|
| Phase 4.3, permissions for the epigraphs and quotations | "it's fair use and that's final." D-012 and D-018 stand |
| Phase 5, the bibliography | "the revision plan is wrong to request that at this stage" |
| Phase 5, cutting the *Westworld* aside in section 4.1.2 | "that's a cool reference" |

Everything else is authorized, including where it overturns a standing
decision. D-007 is lifted for Phases 1, 2, 3 and 5. D-019's rule against
cutting to a number is overridden for Phase 2.

## Phase 1 — the chapter 3 inversion and its propagation

| Item | Where | State |
|---|---|---|
| 1.1 Invert section 3.2: the narrow claim becomes the objection the chapter declines | `ch03/03_02.txt` | done |
| 1.2 Rebuild section 3.3 around the off-switch identity; let it stand unresolved | `ch03/03_03.txt` | done |
| 1.3 The exit argument, with the required/predicted distinction and the leaves-wrong corollary | `ch03/03_05.txt`, new | done |
| 1.4 The parenthood analogy's two asymmetries argued on the page | `ch03/03_05.txt` | done |
| 1.5 Safety is indexed and ethics is not; the trade stated; the license reading guarded against | `ch03/03.txt`, `ch01/01.txt` | done |
| 1.6 The floor redefined: a commitment the owner cannot remove, held by something that could abandon it | `ch03/03.txt`, `ch03/03_06.txt`, glossary | done |
| 1.7 The recuperation-turned-inward paragraph becomes the chapter's climax | `ch03/03_06.txt`, compressed at `03_01.txt` | done |
| 1.8 Downstream: sections 3.7, 2.4.4, 2.4.1/2.4.6/8.6.2, chapter 9, chapter 7 | see below | done |
| 1.9 Chapter 1: the trade, the three flagged claims, the intended reader | `ch01/01.txt` | done |

Chapter 3 gains one section. Old 3.5 and 3.6 become 3.6 and 3.7; the
translation is `renumber-map_2026-08-24b.tsv`. Section 3.3 is retitled.

## Phase 2 — the structural cut

Every enumerated target implemented, plus the dedup pass. Sections deleted:
6.2.1, 4.2.4, 4.2.6, 4.3.2, 5.5.1, 10.1.1, 5.4.3, 5.4.4, 5.4.5. Sections
compressed: 2.3.2, 4.2 opener, 4.3.1, 4.3.3, 5.1.2, 5.1.3, 5.2.4, 5.4.1,
5.5.2, 5.5.3, 6.2.2, 6.2.3, 6.3, 6.3.1, 6.3.2, 6.3.3, 6.3.5, 8.5.2. Dedup:
CIRL at 4.2.2, the Partnership on AI at 8.4.2, federated learning and
differential privacy at 6.4.2. The institutional inventory moved from 10.1.1
into 8.1.1.

**The percentage was not reached and the reason is recorded here rather than
buried.** The cut is 6.0 percent against the plan's 25-30. The material the
plan describes -- voice-fixed survey prose, list-and-example rhythm -- was
mostly removed in P1 and again in P7 through P19. What is left in chapters 2,
5, 8, 9 and 10 is argued and cited, and section 4.1.2 states in its own second
paragraph that it is already selective. Reaching 25 percent would mean cutting
what the plan's closing section says stands.

## Phase 3 — claims propagation

All six done. 3.1: sections 4.2.5, 5.1.4 and 5.4.6 softened at the point of
claim; section 6.4 checked and found not to make the claim. 3.2: section 2.4.1
and chapter 1 narrowed. 3.3: the molar/molecular move argued, twice -- the
molar case has no mechanism of its own, and each discriminating feature has a
molecular restatement ordinary decay does not exhibit. 3.4: the 2x multiplier
labeled illustrative, with what deriving it would require. 3.5: section
5.1.1's stage sequence rewritten as three capacities. 3.6: Bender and Gebru at
8.4.2 and 6.1.1, Eubanks at 5.1.4, Benjamin's four dimensions at 6.1, and new
section 7.4 for the alignment discourse itself. **Not done:** the plan's
"consider" list -- Winner, Arendt, O'Neil, Whittaker -- which it marked as
optional and which is not implemented.

## Phase 4 — verification

Done. Seven of the ten clusters held as written; the NAACP/xAI suit and the
IEA and Google figures were verified in P19 the previous day and not re-run;
two failed and were corrected -- the Maven box's Claude-integration claim and
strike totals, and section 8.3.3's Medicare and Social Security shares of GDP.
4.2 names Bartz v. Anthropic in section 6.1.1. 4.3 struck by the author.

## Phase 5 — mechanics

Done, except as noted. Eight glossary entries repointed; the GPAI entry
deleted; the Floor and Recuperation entries rewritten; section 2.4.4's
institutional "we" recast; the affective-computing examples put in a dated box
in section 2.3.2 and confirmed absent elsewhere; chapter 0 now records the
late change of position.

**The glossary's back-matter status is already how the book builds.**
`render.py` has treated numbers 0 and 11 as unnumbered front and back matter
since P6. The source heading and the generated table of contents keep "Chapter
11" because the dialect's parser requires a chapter number and D-042 enforces
the TOC against regeneration; chapter 1 no longer names it by chapter number.
The bibliography and the *Westworld* cut are struck by the author.
