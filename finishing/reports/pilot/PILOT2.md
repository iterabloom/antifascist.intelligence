# Pilot 2: transplant T4 into §2.2.1 — the name-scrubbing test

Branch `pass/pilot2`. T4 was chosen because it carries the heaviest
person-characterization load in the transplant set: the source names three
researchers across six instances and builds its best passage on a personal
anecdote.

**Scope note.** T3 will later replace most of §2.2.1's prose. This pilot
deliberately did only T4 — the box, plus the one false sentence it corrects —
so that the name-scrubbing cost could be measured without being confounded.

## What the name rule actually cost

Six name instances in the source, **zero in the transplant**. What that removal
did to the material, honestly:

| Source | Transplanted as | Cost |
|---|---|---|
| A named researcher reached for an object before the experiment began; the neurons fired | "The cells also fired when the monkey merely watched someone else perform the same reach" | The discovery anecdote survives as a fact and loses its accident. The source's version is better writing. This is a real loss and there is no way around it. |
| A named scientist called mirror neurons "the neurons that shaped civilization" | "In the popular literature mirror neurons were described as the neurons that shaped civilization" | **Attributional precision.** The phrase is real and was said by someone specific. Attributing it to "the literature" is true but vaguer, and it is the one place where the rule and ordinary scholarly practice pull against each other. See the question below. |
| "Rizzolatti himself, the original discoverer, ultimately stepped back… He noted that…" | "Later papers from the original group narrowed the claim considerably" | Arguably **an improvement**: it is a claim about the published record rather than about a person's mind, which is what a reader can check. What is lost is that the retreat was authored by the same people, which was part of the source's point about self-correction. |

**Finding: the rule is survivable and occasionally improves the prose, but it is
not free, and it is not mechanical.** Each of the three required a different
judgment. A script can find the names; only a reader can decide what the
sentence was for.

## What the dialect was missing

The manuscript's markup had `<<quote>>` and `<<list>>` and no way to say "this
is a box". T4's mode is `boxed-case`, so the construct had to exist before the
transplant could land. Added `<<box>>` … `<</box>>`, first line taken as the
box title, and threaded through five tools: `check_structure.py` (balance and
nesting), `section_stats.py` and `tics.py` (box text counts as the author's
prose, unlike an epigraph), `redundancy.py`, and `render.py`.

## Two rendering bugs, found and fixed

Neither was visible until the box was actually put on a page.

1. **A `<div>` border became a border around every paragraph** — the box rendered as four stacked boxes. Fixed by emitting a single-cell table.
2. **The table's CSS border and background were then dropped entirely.** LibreOffice's HTML importer honors presentational attributes (`border`, `cellpadding`, `bgcolor`) and ignores most stylesheet rules. Fixed by using the attributes and `<b>` for the title rather than a CSS class.

Both are recorded in `pipeline.md`. The general lesson: **the proof build must be
looked at, not just produced.** Both bugs passed every automated check.

## Cost, against pilot 1

| | Pilot 1 (T11) | Pilot 2 (T4) |
|---|---|---|
| Mode | replace-section | boxed-case |
| Source words → book words | ~880 → 781 | ~700 → 467 (box) |
| Section words | 589 → 734 | 484 → 951 |
| Name instances to scrub | 0 | 6 |
| New citation placeholders | 5 (+1 permissions) | 5 |
| Dialect changes needed | 0 | 1 construct, 5 tools |
| Render iterations | 0 | 2 |
| Judgment calls needing the author | 0 | 1 (below) |

Most of pilot 2's extra cost was **one-time**: the box construct and the
renderer fixes are now done for all sixteen transplants. The recurring extra for
a name-heavy transplant is the scrubbing judgment — perhaps a third again on top
of a T11-shaped transplant, not double.

## One judgment the author should confirm

I attributed "the neurons that shaped civilization" to *the popular literature*
rather than to the person who said it. The strict reading of the named-persons
rule pushes that way, since naming him would hold a real person up as the author
of an overreach that did not survive. But quoting a published claim and citing
it is also ordinary scholarship, and the vaguer attribution costs the reader
something. C0277 is logged so the citation can carry the provenance even if the
sentence does not. **If you would rather name him, say so** — it is your call
about your book, and it is reversible either way.
