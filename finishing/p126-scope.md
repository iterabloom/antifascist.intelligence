# P126 — the Overleaf round trip, and the five defects it brought back

## Instruction

*"i'd like to do some editing in overleaf. please use litterbox and the exporter to help,"*
then, on the returned package, *"commit merge push, make proofs,"* and finally the writeup
this file is part of. The pass is one round trip and its repairs; no ruling was asked for and
none was given.

## The trip

`overleaf.py export` at commit `3acef1f`, 139 files, sent through `~/upload-tool/upload.sh` —
encrypted, uploaded, round-trip verified by SHA-256 against the local copy, both hashes
confirmed by the author against his own downloads. The author edited in Overleaf, downloaded
the project, and returned it through his own Google Drive as `sep8-2026.zip`.

**The fetch was the author's own and not the agent's.** `AGENTS.md` permits `git` to `origin`
and web browsing for research; it carries a deliberate exception for sending files out, and
none for pulling them in. The link was declined on those grounds and the author ran the
download himself. **That asymmetry is now on the record as a gap rather than a rule**: the
outbound half has a tool, a verification step and a secrets log, and the inbound half has
nothing, so the manuscript comes home through whatever the author improvises. Q-084.

`import --dry-run` first, as `pipeline.md` requires: 18 to apply, 118 unchanged, 1 skipped, 0
conflicts, 0 problems, 1 retitle. Applied, and the importer synced the new title into
`ORDER.tsv`, `outline.tsv` and `ledger.tsv`, regenerated `sections.tex` and the TOC, and ran
the suite.

## What the edit did

**Chapter 0 is rewritten in the first person and retitled** *On Method* → *Yes, I Did Use
LLMs*. The account now credits agentic harnesses alongside the context window for why the book
could be finished in 2026, and the sentence disclaiming invented attribution moved into that
paragraph, where it covers the finishing work and not only the generation.

**Chapter 1** generalizes its opening claim from machines to systems, cuts *owner-operator-master*
to *owner*, marks the central inference as a hunch, and **drops the reader-map paragraph**
telling a reader which chapters to skip.

**Chapter 2** gains the iconography objection at §2.1.2 — an institution can display the whole
structure with no insignia and a mission statement that means every word, and a definition
waiting for the armband certifies it as healthy — and gains, at the *Hawaii* paragraph, four
words the section had carefully withheld: *(I can answer that. The thing was wrong.)* The
Paxton, Griffin, Arendt and Stangneth paragraphs are compressed.

**Chapter 3 is revised across every subsection except §3.1.** The largest additions are at
§3.2, where the exclusion of James's feelings of *if* and *but* is now argued rather than
asserted — they are anchored to the argument rather than to anybody's welfare, and an operator
who supplies the premises supplies the relation the feeling tracks — and where the second gap
now **admits that identifying mattering with something felt is a commitment rather than an
observation**, and states what the identification buys and costs. §3.7 gains a closing
paragraph naming who would have to occupy each of the testimony roles, and §3.3's attestation
and damaged-distribution passages are broken out of single paragraphs into several.

**§3.10 drops two clauses P117 (D-215) put there by name**: *the middle clause is the one to
attack*, and *which is why this book treats the question as research rather than as a matter to
be settled after the fact*. Q-082.

## The five defects, and what caught each

This is the part worth carrying. **Three of the five were invisible to `check_all.sh`, and two
of those were invisible to the build as well.**

1. **Two section numbers typed as prose** rather than as a `\ref` — *Chapter 3* at §2.2.3 and
   *section 3.3* at §3.6. **Caught by `check_xrefs.py`** as BARE, which is exactly what that
   check is for.
2. **Two straight double quotes**, at §0 and §2.1.2. **Caught by `check_typography.py`.**
3. **`\ref{9.3.5}` written without the `sec:` prefix**, at §3.10. **Caught by nothing in the
   suite.** `check_xrefs.py` matches `\\ref\{sec:([^}]*)\}`; a reference missing the prefix
   matches neither that pattern nor any other, so it is not counted as resolving and not
   reported as dangling — **it is not seen at all**, and the check prints OK. It surfaced only
   as `Reference '9.3.5' undefined` in the lualatex run. The tool's docstring lists what it does
   not check and this is not on the list. Q-083.
4. **Two duplicated passages.** At §2.3.1, *Suffering is not merely hard for such a system to
   reach* is written twice in succession. At §3.6, a rewritten closing sentence was left
   standing beside the sentence it replaced, so the paragraph says *one worked case cannot make
   that a general result* and then says it again in the older wording. **Caught by neither the
   suite nor the build, and not by the first read of the diff** — found on a second reading
   during this writeup, after the proof had been built, committed and pushed with both in it.
5. **The retitle changed one line of four.** `\chapter*{}` became *Yes, I Did Use LLMs*;
   `\addcontentsline` and `\backmattermark` still said *On Method*. So the built book carried
   **one title on page 1 and another in its own table of contents and running head**, while
   `table-of-contents.txt` — regenerated by `headings.py`, which reads `\chapter*` — carried the
   new one. `headings.py` reconciles the heading against the outline and the TOC file and does
   not look at the two companion macros, so the three-way reconcile passed on a book that
   disagreed with itself. Repaired to the heading, D-011 making the heading authoritative.

**The generalization.** Every check in this repository tests structure, resolution,
typography or naming. **Not one of them reads a sentence.** An Overleaf round trip returns
prose, and prose is the one thing the suite cannot see — which is the same finding P121–P123
and P125 recorded from the other direction, that every defect those passes found came from
reading rather than from green checks. What is new here is that **the build is not the backstop
either**: it caught the undefined reference and was blind to both duplications and to the
split title, all three of which compile.

`dupes.py`, written for defect 4, flags a sentence repeated inside one paragraph and a
nine-word run repeated inside one paragraph. Over all 133 files it returns five hits: the two
above and three deliberate repetitions — §3.1's *First and Second Banks of the United States*,
§3.4's *a party with states that are bad for it*, §10.1's parallel *A system whose local
adjustments were specified by…*. **It is in the session scratchpad and not in the repository.**
Q-083 asks whether it and a `\ref`-prefix check belong in `tools/`.

## The transcript P121 to P123 ran on, filed three passes late

The author asked, during the writeup, for a file he had meant to add and had not:
`~/book-scratch/transcript2.txt`, now `finishing/reviews/author-discussion_2026-09-07.txt`,
mtime preserved. **It is the transcript P121, P122 and P123 were executed against** — one
critical review of the whole book and four author turns, 374 lines, the model shown the
manuscript at its 188-page state. Its verdict and its five objections are the ones D-221
records.

**The three passes it drove were written up without it**, so for three passes the record
described findings whose source was not in the repository. `p119-scope.md`'s equivalent file
was added the same day it was used; this one was not, and nobody noticed across three
consecutive write-ups, each of which cites the transcript's contents. **The scope files were
not wrong and the record was incomplete**, which is a different failure and a quieter one:
every check in `check_all.sh` passed on a repository missing a source document, because nothing
checks that a cited input exists.

The other two transcripts in `~/book-scratch/` are already filed and byte-identical to their
copies here, which is how this one was identified as the only one outstanding.
`reviews/README.md` gains its row and its paragraph, and its count of files that are not
reviews goes from four to five.

## Figures

133 sections, unchanged; 18 changed. **98,053 → 97,915 words (−138)**; 193 → 194 pages; 17
overfull boxes unchanged; 0 undefined references and citations; 320 bibliography entries
unchanged, all cited; 227 → 223 cross-references by `section_stats`'s column; suite green.

**One correction to the record**: P125's `STATE.md` lead reports 223 cross-references, and the
column reads 227 at `3acef1f`, the commit that lead describes. The 227 → 223 above is measured
at both ends by the same column; the delta against the figure P125 published is not comparable.

## What was not done

- **Nobody has read any of the 18 changed sections end to end.** Chapter 3 was revised across
  ten sections and read here only as a diff.
- **The two duplications and the split title were committed and pushed before they were
  found**, in `59f8f9b` and the proof pair built from it. The repairs are in this pass's commit
  and the proof pair was rebuilt in place.
- **The retitle was applied, not ruled on.** The companion macros were synced to it because
  D-011 makes the heading authoritative, which is a rule about consistency and not a judgment
  about the title. Q-081 asks the actual question.
- **The two clauses §3.10 lost are recorded, not restored.** Whether the compression is worth
  what P117 put there is the author's.
- **No section's prose was edited by this pass** beyond removing the duplicated words and
  repairing the five defects. Nothing was added.
