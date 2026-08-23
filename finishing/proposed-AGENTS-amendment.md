# Proposed amendment to AGENTS.md — needs your approval

D-017 changes how the named-persons rule is applied. `AGENTS.md` still carries
the strict wording, and a future agent reading it will re-apply the strict
reading and re-scrub the citations we just restored. Amending it needs your
explicit approval, so here is the exact change, not applied.

## Current text

> - **Named real persons.** This repository names many real people because language
>   models were prompted to write *as if* they were those people. That device is
>   confined to text **about the book** (drafting sections, reviewing structure).
>   Never generate, commit, restore, or re-derive anything that characterizes,
>   rates, ranks, scores, or attributes personal views or conduct to a real named
>   person — in any file, notebook output, or commit message. If such material
>   turns up or is needed for some reason, it goes to
>   `~/ethical.superintelligence-private/` (outside the repo), never here.
>   The README's named-persons disclaimer is load-bearing; do not weaken it.

## Proposed text

> - **Named real persons.** This repository names many real people because language
>   models were prompted to write *as if* they were those people. That device is
>   confined to text **about the book** (drafting sections, reviewing structure).
>   Never generate, commit, restore, or re-derive anything that presents such
>   simulated material as a real person's own view, conduct, or contribution —
>   and never rate, rank, or score a real person — in any file, notebook output,
>   or commit message. Reviews in `editorial/` are cited by file and index or
>   line range, never by persona name. If such material turns up or is needed for
>   some reason, it goes to `~/ethical.superintelligence-private/` (outside the
>   repo), never here.
>   **This is not a bar on ordinary scholarly citation.** Naming the researchers
>   who published a finding, quoting a published claim with a citation, and
>   describing a documented event in a laboratory are normal nonfiction and are
>   allowed, in the book and in `finishing/`. The test is whether a person is
>   being credited with something no source supports.
>   The README's named-persons disclaimer is load-bearing; do not weaken it.

## What changes in practice

Nothing about the disclaimer, the private directory, or the editorial record.
The single change is that citing published work by name stops being a violation
and becomes what it is. `finishing/tools/names_guard.py` already implements the
new test and still fails on "reviewed by X, who rated it highly" — verified.

Say the word and I will apply exactly this.
