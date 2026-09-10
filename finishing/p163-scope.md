# P163 — the Overleaf round trip, and 55 annotations kept as written

The manuscript went out to Overleaf on 2026-09-09 and came back on 2026-09-10 as
`~/book-scratch/Sep10.zip`. The export was verified before it left: 139 files,
`\addbibresource` rewritten to `refs.bib` as the single intended change, and
`\documentclass` in `book.tex` alone so Overleaf would pick the right main file.
It was sent through `~/upload-tool/upload.sh` on the author's ask.

**One question was worth asking before publishing.** The author said "catbox";
the tool's default is `litter.catbox.moe`, 72 hours, and all five previous sends
had used it, while `UPLOAD_HOST=catbox` is the permanent host. Those differ in a
way nothing could undo — the tool uploads anonymously, so a permanent URL could
not have been deleted afterward. He meant litterbox.

## What came back

**15 files, 3 retitles, 0 conflicts, 0 structural problems.** The manifest
matched, so the import could separate Overleaf edits from repository edits, and
there were none of the second kind to collide with. Retitles: chapter~1 to *This
Is a Long-Ass Book With No Protagonist and No Personal Anecdotes*, §2.1
*…Save You* to *…Save Us*, and chapter~3 *The Floor* to *A Floor* — the last
being the one with an argument in it, the indefinite article matching a floor
that is one of four routes. The prose edits are a first-person pass over the
foreword and chapter~1 in the direction `style.md` §1 asks for.

## The finding

**The returned files carry 55 editorial annotations written inline into the
prose**, in 10 files across chapters~2 and~3, in two forms: `[passage] -- CAPS
NOTE`, and a bare `[CAPS COMMENT]` dropped mid-sentence. **They are book text as
far as LaTeX is concerned and they typeset into the proof.** The count is exact
rather than estimated: it was taken by diffing the returned files against the
pre-import baseline, so it counts insertions attributable to this trip and not
pattern matches in the tree.

**The author's instruction was to leave them completely as-is**, which is what
happened. They print in the proof, which he was told before he asked for it.

## Two regressions, both predicted

**Q-087 recurred for the fourth time**: 0 `\textit` in the baseline, 7 in the
return, 5 of them in genuine prose. Still unconverted at the close of this
session — see `p172-scope.md`. **Straight quotes: 0 in the baseline, 18 in the
return**, two of them in prose the author wrote and wants (`01.tex:22`,
`03.tex:15`) and the rest inside annotations.

`check_all.sh` therefore fails on typography, and every commit from here to the
end of the session is made with `--no-verify` against a knowingly mid-repair
tree, which is the case `.githooks/pre-commit` documents for the bypass.

## Figures

133 sections, 15 changed, 3 retitles. 99,458 → 99,729 words. 194 → 195 pages,
the extra page being the annotations. 0 undefined references and citations.
