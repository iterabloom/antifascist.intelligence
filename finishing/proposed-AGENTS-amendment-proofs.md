# Amendment to AGENTS.md — "make the proofs", and the build line

**Status: proposed, not applied.** `AGENTS.md` requires the author's explicit
approval, and "I think this should be explained in AGENTS.md, what do you think?"
is a proposal put to me, not the yes the file asks for. This is the exact text,
ready to apply on a word.

## Why AGENTS.md and not somewhere else

`CLAUDE.md` is one line, `@AGENTS.md`, so `AGENTS.md` is the only file in this
repository that is loaded into every session before anything is read. A trigger
phrase has to be in it or it does not fire: `pipeline.md` and `STATE.md` are read
at session start **by convention**, and a convention is exactly what an agent
skips when the instruction looks simple. "Make the proofs" looks like a build
command. If the sequence is only written in `pipeline.md`, the session that most
needs to read it is the one least likely to.

What should **not** go in `AGENTS.md` is the sequence itself. That file is short
and rule-shaped, it is the one file that needs approval to change, and the steps
will move whenever the build does. So: the phrase and what it commits to in
`AGENTS.md`, the steps and the reasons in `pipeline.md`, which already has them.

## Change 1 — a new section, after "File Conventions"

> ## Author's Shorthand
> - **"Make the proofs."** This phrase — or "do the proofs," or a near variant —
>   names a fixed sequence and not just a build. In order: commit whatever is in
>   the tree, to `main`, and push; run `finishing/tools/build_proof.sh`; remove
>   the previous dated pair if the date has rolled over; point the README's two
>   links at the new files; commit and push again. **Two commits**, so the work
>   is legible in the first diff and the second carries only generated output.
>   `finishing/pipeline.md` has the steps in full and the reason for each.

## Change 2 — one sentence in "Architecture & Context"

The **Authoritative text** bullet still names one build script, and there are
three.

### Current text

> `finishing/tools/check_all.sh` checks that both are current, along with the
> rest of the invariant suite. Build with `finishing/tools/build_tex.sh`.

### Proposed text

> `finishing/tools/check_all.sh` checks that both are current, along with the
> rest of the invariant suite. Build the PDF with
> `finishing/tools/build_tex.sh`, the HTML page with `build_html.sh`, or both
> into `finishing/reports/` with `build_proof.sh`.

## What changes in practice

Nothing about any boundary. No rule is added, removed, or loosened: the
named-persons prohibitions, the secrets and network boundaries, the frozen
files, the read-only provenance list, the filename conventions, the weasel-word
lists, and the approval requirement for this file are all untouched. The diff is
a new seven-line section and one sentence.

## Three things the phrase leaves open, which the wording above does not decide

1. **GitHub does not render a committed `.html`.** Following the README's HTML
   link gets the source or a download, not a page. The PDF link opens in
   GitHub's own viewer and works. Making the HTML a page needs either GitHub
   Pages or a third-party renderer, and both depend on whether the repository
   is public, which I have not checked and will not guess at.
2. **The dated filename churns the README.** Every rebuild on a new day makes a
   new pair and the README's two links must be repointed, which is why step 4
   exists. Dropping the date from these two files — which `AGENTS.md`'s own
   convention permits, since "new files may omit the suffix" — would make the
   links stable and each rebuild an overwrite. That is a change to a file
   convention and is the author's.
3. **"Commit everything" needs a floor.** As written the phrase commits whatever
   is in the tree, straight to `main`, which is what it should do and which also
   bypasses `PLAN.md`'s one-branch-per-pass rule for this gesture. The wording
   above accepts that deliberately. What it does not license is committing a
   surprise silently: if the tree holds more than the work just discussed, say
   what is going in before it goes in.
