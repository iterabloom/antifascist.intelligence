# Triage complete — all 282 rows ruled

Five readers, one per chapter group, each reading the section text and ruling
against `finishing/triage-brief.md`. Rulings were consolidated by
`finishing/tools/apply_triage.py`, which validates the forced fates rather than
trusting them.

**These rulings were made on the author's behalf**, inferred from eleven prior
decisions and a pattern of edits. Every one is a row in a TSV and is changed by
editing that row. Nothing here is irreversible.

## The result

| Fate | Rows | Words |
|---|---|---|
| revise | 145 | 57,937 |
| fold | 100 | 46,283 |
| move (chapter 8 → a single §7.5) | 16 | 6,001 |
| cut | 9 | 3,552 |
| fill (empty headings) | 8 | 0 |
| keep | 2 | 535 |
| merge | 1 | 482 |
| done | 1 | 734 |

Forty-seven rows carry a target: a fold destination, a compression word count,
or §7.5 for the chapter-8 material.

## What the readers found that the tooling had not

- **§10.3.2.1 and §10.3.3.2 use the identical example** — RoboCup Rescue — for the same robustness point. An exact internal duplicate, in two different sections, that the embedding analysis had not surfaced because the surrounding prose differs. Verified.
- **The introduction promises a roadmap the book does not deliver.** §10.2 is scaffolding, and §10.2.1 concedes its milestones are "not a rigid roadmap". Under D-007 (revise, not rewrite) building one is out of scope — so either the promise in the introduction changes, or D-007 gets an exception. Author's call; nothing is blocked on it.
- **§8.4.1 contains two halves that restate each other** — a "pathways" list and a digital-divide discussion.
- **My briefing was wrong about AI-safety vocabulary.** I told the readers the book has none. It has a great deal: "value alignment" 48 times across eight chapters, "AI safety" 31, "existential risk" 6, and §5.3.1 is titled "The Alignment Problem". Only "boxing", "takeoff" and "recursive self-improvement" are absent. The brief now carries the measurement.

## A schema problem the validator caught

§3.1.2.3.1.1 is the pilot section: its prose is finished and accepted. It is also
six levels deep, so its heading folds at P1. The tool refused to accept `keep`
for a row that is forced to `fold`, which was right — **"what happens to this
text" and "what happens to this heading" are different questions**, and the
triage schema had been conflating them. The row now records both: `done`, with
`pending_fold:3.1.2`.

## Judgment calls worth knowing about

- **§4.4** — the Bronfenbrenner ecological-systems apparatus — was read in full and judged to earn its place rather than being scaffolding. Six subsections kept.
- **§4.7 and §3.3 both cover play.** The 2023 reviews wanted them merged. The reader kept both, on the grounds that §4.7 carries a distinct moral and empathy apparatus while §3.3 is about curiosity and exploration, and cross-referenced them instead. This is the most reversible of the calls if you disagree.
- **§7.4 keeps only what is genuinely legal-and-accountability**; the ethics belongs to §2.4, which wins the parallel treatment. §7.4.3.1 compresses to 150 words and §7.4.3.1.1 to 80.
- **§1.3's deleted subheadings get restored** — they were removed in 2024 without reflowing the text, and level 3 is inside the depth cap.

## Projected length

Starting from 115,377 body words, with the cuts, the compressions set so far,
chapter 8 reduced to a single ~5,000-word section, and the 10,400 words of
transplants added, the book lands near **112,000 words** — against D-002's
75–90k. The cuts ruled here do not close that gap. Closing it means either
compressing the 145 revise sections as they are edited, or revisiting D-002.
