# Amendment to AGENTS.md — no measurements in this file — PROPOSED 2026-09-19

**Status: proposed, not applied.** `AGENTS.md` and `.githooks/**` need the
author's explicit approval, and it has not been given. This file exists because
the proposal was made in conversation on 2026-09-19 and would otherwise have
been lost; it is the third such proposal, after the P-level one and the proofs
one, both of which were approved and applied.

## The defect it fixes

`AGENTS.md:96–105` describes `render_markdown.py --tex --no-notes` and is stale
in four ways, all four derived rather than asserted (D-457, re-derived at D-460
and D-466):

| the file says | measured 2026-09-19 |
|---|---|
| strips the `note` field, "161 of the 229" | strips `note` **and** `addendum`, 233 of 280 |
| "670 KB to 608 KB" | 746 KB, read 2026-09-19 (745 KB earlier the same day, when this file was written; see below) |
| "the same 164 pages" | 186 pages |
| inlines "the generated `draft-status.tex`" | the whole draft apparatus is stripped |

Note the span: D-457 called it `101–105`, but the `draft-status.tex` claim is at
line 97, so an amendment has to reach back to 96.

## Why it went stale, and the fix that does not work

The passage arrived on 2026-09-16 through `proposed-AGENTS-amendment-render-tex.md`,
approved and applied. **It was accurate the day it went in.** D-395, two days
later, changed the behaviour it describes — `--no-notes` went from stripping one
field to stripping two — and the book grew underneath the rest of it.

The tempting diagnosis is the approval gate: the agent who notices cannot fix
it. **That diagnosis is wrong, and the evidence was in the tree.** The same facts
lived in `finishing/README.md`, which needs no approval and is edited freely, and
they were stale there too when this file was written — "199 and 30 of the 275
entries, 229 in all, taking 782 KB to 682 KB" against 203 and 30 of 280, 233 in
all. What the editable copy got right is the *behaviour* sentence, because D-395
updated it. The counts rotted on the same schedule in both files.

**D-472 has since corrected the README, and that strengthens the argument rather
than settling it.** The editable copy was not fixed by being editable; it was
fixed when a handoff check went looking for two live readings of one quantity
and found them, days after they went wrong, and it had by then been carrying
*two* figures for the same measurement with nothing marking either as dead.

**And this file's own replacement figure went stale the same day it was written.**
It said 745 KB and the export read 746 KB hours later — 170 bytes, of which 120
are a comment D-468 added to explain the marker convention, enough to cross a
KiB boundary (D-475).
A figure does not need the thing it measures to change much; it needs it to
change at all. That is the case for the rule, made by the document arguing it.

So editability buys nothing here. Genre does.

## The rule

> **`AGENTS.md` carries policy and pointers, never measurements.** The test: if
> running a tool could make the sentence false, it does not belong in this file.

A policy is a decision that holds until reversed — *page-proof the book from
`build_tex.sh`, never from this file* survives any amount of growth. A
measurement is an observation about a state that moves, and "the same 164 pages"
was doomed the day it was written.

The rest of the file already complies. Every other numeral in `AGENTS.md` is a
date (`2026-09-05`, twice), a decision ID (D-065, D-169, D-334), a
cross-reference (`style.md` section 10), or a property of a third-party service
(litterbox, 72 hours). **Three volatile figures in the whole file, all in one
passage.** This is not a document rotting throughout; it is one paragraph
written in the wrong genre.

## Current text, lines 96–105

> **`--tex` converts nothing** (D-334). It writes `manuscript/book.tex` with
> every `\input` resolved — the preamble, the generated `draft-status.tex`, and
> every section — and `finishing/refs.bib` inside a `filecontents` block, with
> each file between `%% ===== START <path> =====` and `%% ===== END <path>
> =====` so a passage can be traced back to the file that holds it.
> **`--no-notes` strips the `note` field from every bibliography entry**, 161 of
> the 229, taking 670 KB to 608 KB; it is refused without `--tex`. The file
> compiles as it stands, to the same 164 pages and the same text, but that is a
> side effect and not the point: five paragraphs break their last line
> differently, because concatenating the sections drops a space token `\input`
> contributes at each file boundary. **Page-proof the book from
> `finishing/tools/build_tex.sh`, never from this file.**

## Proposed text

> **`--tex` converts nothing** (D-334). It writes `manuscript/book.tex` with
> every `\input` resolved — the preamble and every section — and
> `finishing/refs.bib` inside a `filecontents` block, with each file between
> `%% ===== START <path> =====` and `%% ===== END <path> =====` so a passage can
> be traced back to the file that holds it. **The draft apparatus is stripped
> entirely** (D-335): `draft-status.tex` is not inlined, and the watermark and
> the status line are removed from the preamble it does inline, so the file
> reads as though it had never been a draft.
> **`--no-notes` strips both fields that print as a note in the References,
> `note` and `addendum`**; it is refused without `--tex`. The tool prints the
> entry count, the fields stripped and the size on every run, which is a truer
> figure than this file can hold. The export compiles as it stands, but **its
> pagination is not the book's**: concatenating the sections drops a space token
> `\input` contributes at each file boundary, so a few paragraphs break their
> last line differently, and the stripped notes shorten the bibliography by
> twenty-odd pages. **Page-proof the book from `finishing/tools/build_tex.sh`,
> never from this file.**

Every figure is gone. What is left is behaviour, mechanism and instruction, none
of which a tool run can falsify.

## The enforcement, proposed with it

A tenth check in `check_all.sh`, about twenty lines: **fail if `AGENTS.md`
contains a figure-shaped token** — a number against KB/MB/bytes/pages/entries/
percent, or the "N of the M" form — outside a small allowlist for dates and
decision IDs.

It lints the *genre*, not the facts. It costs nothing at runtime and can never
fail merely because the book grew, which is what a fact-checking version would
do. It fires when someone writes a figure in, which is the moment the author is
in the loop anyway, since the file needs approval to change at all.

**The honest cost:** a blocking check on an approval-gated file can stop a commit
until the author rules. It fires only on newly added figures, and
`git commit --no-verify` bypasses, so the price looks small — but it is the
author's to weigh, not the agent's.

## What is not proposed here

Rewriting `finishing/README.md`'s stale figures, which needs no approval and can
be done in any pass. It is not done yet either.
