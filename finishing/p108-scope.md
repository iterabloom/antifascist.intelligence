# P108 — the persona-device record becomes one binary archive before the repository goes public

**The instruction.** *could you please make an opus subagent that searches through files OTHER THAN
the manuscript, in the book repo (eg ipynb files), for uses of living people's names in a
role-playing exercize, and zips those files? my motivation here is that I want to make the github
repo public, but I want to avoid having living author names indexed by search engines next to
llm-generated "dialog"*. The agent was briefed to write the zip to `~/ethical.superintelligence-private/`,
the location AGENTS.md then named for such material; that was the agent's briefing and not the
author's instruction, and the author corrected it: *i did not say private*; *i think it is ok to be
public*; *besides they are already part of the git commit history*; *the point is for it to be a
binary blob*; *people can still inspect it and look at it*; *the point is to avoid search engines
indexing*. On the three questions the audit left, the ruling was *1. yes 2. approve 3. either way
whatever makes the most sense*: remove the plain files, approve the tool and AGENTS.md changes, and
decide the archive index's fate on the merits. *proofs please commit and merge all*.

## The audit

Scope was every tracked file except the book text and its two proofs: 744 files, all read,
including both notebooks' cell outputs, where the generated sections live, and the spreadsheet and
document containers opened as zip archives. The roster came from the names guard's own loader, held
in memory and never written; two tests ran on each file, roster hits and role-play shapes
independent of the roster.

**43 files carry the device**, 22,168,647 bytes: all of `genesis/`, `personas/` and `editorial/`;
four files in `generation/`, the elite-team transcript, the two notebooks, and one prompt fragment
whose filename itself carries a person's name and the instruction; both copies of a 2022 transcript
in `cognition/`; and `original-layout-and-mtimes.txt`, for the one line that repeats that filename.
**Sixteen files name people only as cited scholars** and stay: the two earlier whole-book texts, the
Atlas draft, the bibliography, generated reports that quote book paragraphs, and two of the reviews.
**685 have no device.** The summary triangle, 471 files, has no roster hit and stays whole. Four
borderline calls went toward the archive and the author kept none in the open: the genesis seed
report, in the team's voice and naming nobody; the archive index, for one line; the 2022 transcript,
where the model plays nobody but makes claims about a named living researcher, one a book title
that does not appear to exist; and one empty triad file kept for the set.

**The roster was incomplete.** The guard's token pattern dropped one persona name containing a
lowercase particle, so that name had been invisible to every guard run since the guard was written.
Thirteen further real people appear in role-play prompts and are on no spreadsheet, eleven of them
in the feedback file's candidate list. All are in archived files. The names are in the manifest, per
file, at `~/book-scratch/persona-device-manifest_2026-09-05.tsv`, outside the repository.

**History.** All 43 entered at the import commit `0a0b58f` and 30 were touched once more by the
spelling normalization; no renames, no earlier paths. Publishing the repository publishes that
history, and the author accepted it in the words quoted above. Nothing was rewritten.

## What was done

- **The archive**, `persona-device-files_2026-09-05.zip` at the repository root, 43 entries with
  repository-relative paths, every entry's hash matching the file it replaced, marked undiffable in
  `.gitattributes` like the proofs. The 43 plain files were removed from the tree; the three
  emptied folders are gone.
- **The spreadsheet reader** falls back to the archive when a path is not on disk, reading the
  bytes into memory. The names guard and the outline extractor work through it unchanged.
- **The names guard** reads all six spreadsheets and accepts a lowercase particle between a name's
  first and last tokens; the matcher tolerates one in text. **105 names loaded where there were
  104.** The persona the audit found is now guarded.
- **AGENTS.md.** The author approved editing the provenance paragraph, and it now names the archive
  and what it holds. Two other bullets were edited so the file would not contradict itself, and the
  author was told so: the named-persons bullet, which had sent this material to the private
  directory and told readers to cite reviews in `editorial/`, now says the record is kept as the
  archive, cites reviews from inside it, and keeps the private directory for material that must not
  be in the repository at all; and the file-conventions bullet says where the archive index is.
- **The README's folder map** gains a row for the archive saying what it holds and why it is an
  archive, and drops the rows for the three folders; the finishing README and the reviews README
  stop naming folders that are not there.

The archive index went into the archive rather than staying in the tree or being redacted: it
indexes exactly what the archive holds, it was already inside it, the one line it carries is the
kind of string the change exists to keep off rendered pages, and redacting it would have edited a
record AGENTS.md says not to regenerate.

## What the change does and does not do

Search engines and GitHub's code search index rendered text on the default branch, and no rendered
page now carries a real person's name beside generated text. The record stays complete and anyone
can download the archive and read every file. Every past version of the 43 files remains readable at
its commit, unchanged by any of this; only a history rewrite and force-push would remove the bytes,
and that was neither asked for nor done.

## Incidental

Both notebooks carry an OpenAI organization identifier in plain text, no key; it is in the archive
with them. The local branch `tools/name-the-outside-tools` has no commit main lacks and was left in
place. The decision log, STATE and ledger still mention the old folders in their historical rows,
which are records and were left alone.

## Numbers

No manuscript file changed. **Committed as `b838941`, the proof pair rebuilt in place at
`cfbcff6` on *proofs please commit and merge all*: 188 pages, the HTML byte-identical to the
previous pair, 0 undefined references, suite green with the guard reading from the archive.** 43
deletions, 7 modifications, 1 addition; the tree lost 247,776 lines of text and gained 4,432,764
bytes of archive.

## Left undone, named

- **History is as it was.** Removing the bytes is a rewrite, and a decision the author has so far
  made the other way.
- **The manifest is outside the repository and is the only record of the off-roster names by
  file.** It is not backed up anywhere else.
- **Image outputs inside the notebooks were not scanned.** A name rendered in a picture would not
  have been found; whether any such output exists was not checked.
