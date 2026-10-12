# Blind trial, 2026-10-10

A first test of the longitudinal judging idea: render two snapshots of the manuscript, hide which is which, and have fresh model judges score each against a fixed rubric. `map.md` says which folder holds which version; `run1.md` to `run4.md` hold every judge's report verbatim and the checks made after unblinding.

**Versions.** `920e6b9` (2026-10-02, just after the condensed reworking replaced the LaTeX prose) and today's manuscript (identical to `683c828`), both rendered with the 2026-10-10 `render_markdown.py`, the "Rendered … from <commit>" line removed. A third folder holds today's version with the two draft marks (Chapter 1's footnote 5 bracket, §19.3's leaked `% CITE` line) removed.

**Rubric.** Overall, clarity, argumentative coherence and economy, 1 to 10 with anchors; quoted evidence for each; one quoted passage per Part as a coverage check; no revision suggestions. Main text judged as the reading experience, footnotes and appendices as optional.

| Run | Judge | 2026-10-02 | Today, no draft marks |
| --- | --- | --- | --- |
| 1, 2 | Haiku, medium | 5 / 5 / 6 / 3 | 4 / 4 / 5 / 2 |
| 3 | Sonnet, medium | 6 / 5 / 6 / 4 | 6 / 5 / 6 / 4 (read only part of the file) |
| 4 | Sonnet, medium, required to read every line | 6 / 5 / 6 / 4 | 6 / 5 / 6 / 4 |

Scores are overall / clarity / coherence / economy. Run 1 also scored today's version with the draft marks (4 / 4 / 6 / 2); at the author's instruction that result is set aside.

**What it found.** Four Sonnet judges gave identical scores to both versions; Haiku scored today's version one point lower on each dimension, which on one judge per version is within its scatter. No judge could tell the versions apart reliably. Every judge, on both versions, named the same problems: coined terms piling up faster than they are defined, a second half that reads as a specification more than a book, and repetition at the level of ideas. Two specific findings checked against the text: the later version's §6.1 says the domestic clause runs "on the Charter as courts read it" while §6.5 says it is drawn "not from the Charter"; and the Preface's "worth building on purpose" sits against Chapter 17's "not yet" without the reader being shown the reconciliation.

**Limits.** One judge per version per model; no hidden repeat on an unchanged file; the restriction to one folder was an instruction, not enforced; token counts came back as single totals, so costs are estimates.
