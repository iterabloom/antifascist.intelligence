# P156 — the cross-reference review re-run across the whole session: nothing to act on

Author instruction, the same one given at P142 and again at P151: review every
cross-reference this session added, judge each against the reader, and where it
costs, remove it and make the passage better in the same edit.

**No cross-reference added this session survives to be judged. No prose changed.**

## The audit, per commit rather than from the totals

**231 at the session's first commit (`8a0935f`); 231 now.** That alone would not
settle it — a reference added in one pass and a different one removed in another
nets to zero — so every commit was checked for the references its diff added and
removed:

| pass | reference set |
|---|---|
| P144, P146, P147, P148, P149, P150 | added list identical to removed list |
| **P145** | **added `\ref{sec:11.1}` and `\ref{sec:11.2}`; removed none** |
| **P151** | **added none; removed `\ref{sec:11.1}` and `\ref{sec:11.2}`** |
| P152, P153, P154 | added list identical to removed list |
| P155 | no manuscript file changed |

**Two commits moved the set and they cancel.** The eleven identical-list commits
are references carried along inside rewritten lines, which is what the per-commit
check exists to distinguish. **No reference was repointed either** — a removal of
`\ref{sec:A}` paired with an addition of `\ref{sec:B}` would show as a differing
set, and none does.

## Three confirmations, because a null result is worth checking twice

**P151's removal stands.** §3.3 carries no reference to §11.1 or §11.2, and its
replacement prose — *it is the nearer of the two to a result: the research chapter
states a test for it* — is intact and untouched since P151.

**Chapter~3's three references to §11.1 and §11.2 all predate the session.** §3.8
carries one and §3.9 two, and each file holds exactly the count it held at
`8a0935f`. **They are not P145's, and nothing here reopens them.**

**Every section whose prose this session changed holds its starting count.**
§2.1.2 2, §2.3.1 1, §3.3 3, §9.1.5 10, §11.1 1, §11.3 0, §12.2.1 6 — checked
against `8a0935f` file by file.

## The standing net

**Across P142 and P151 this instruction has run on real additions twice and removed
seven of eight.** The survivor is P142's §5.2 → §2.2.1: backward, at a section
head, into a section that had no inbound references. **This third run had nothing
to remove, which is the first time that has been true.**

## Figures

133 sections, **0 changed**. 99,568 words, 196 pages, **231 cross-references**, 324
bibliography entries — all unchanged, and 231 is the count the session opened at.
