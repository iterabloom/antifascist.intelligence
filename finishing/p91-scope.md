# P91 — §3.8's completeness claim withdrawn, and the locator that hid the contradiction

**The instruction.** After P90's correction was reported — that the book *does* connect the jobs
guarantee to the bearer's exit, at §11.2, on the author's own D-109 instruction — the author
answered the correction: *well, the reader won't have access to DECISIONS.md. the question is
whether the point is strong enough in the manuscript.* Then, on the finding below, *do both*.

## The question, answered against the manuscript

**Where it sits, the argument is strong.** §11.2 names compute as the thing a bearer needs in
order to go on existing; specifies the form the allocation has to take — *decided, recorded and
appealable, rather than the standing quota that can be throttled by a decision nobody has to
sign*; imports §8.3.3's roof argument by name; says the transfer is stronger here because the
party positioned to revoke is the operator; and names the failure mode, that a bearer shaped not
to want the outside option collects none of the leverage.

**Where the claim is made, the reader had nothing.** The reference topology stranded it:

| | |
|---|---|
| §3.8 → §11.2 | **none** — its five references were §2.3.2, §3.4, §4.1.2, chapter~7, §8.3.3 |
| §11.2 → §3.8 | **none** — it cited chapter~3 four times, always as the whole chapter |
| Sections citing §11.2 | nine, including §3.3, §3.5 and §3.9 — **not §3.8** |
| Sections citing §3.8 | five — **none of them §11.2** |

**The two sections that complete each other were the only pair in the neighbourhood that did not
cite each other**, and §3.9, the chapter's own conclusion, cites both without joining them: §11.2
for the what-is-owed question, §3.8 for exit surviving, in separate paragraphs. Both sections also
reach for §8.3.3 and take different halves of it — §3.8 borrowed its *no forecast required* move,
§11.2 its outside option — and never met there either.

**It was worse than a missing pointer.** §11.2 says the schedule's contents are *named by the
contradiction chapter~3 leaves standing*, and that *exit, as the book has it, is a form of dying,
and a threat that costs the threatener its existence is not the leverage the argument needs*. So
**§11.2 was correcting §3.8, not extending it**, while §3.8 told the reader its narrower Hirschman
set was *still complete*. A reader stopping at chapter~3, or reading chapter~11 as the research
agenda its title announces, never learned the book thought that claim left a contradiction.

## The two repairs

**§11.2's prose locator, which is why nothing had caught this.** The sentence read *Exit is the
capacity **that section** says a floor requires* — no `\ref` at all, and its nearest antecedent
was `chapter~\ref{sec:3}`, so it called a chapter a section and resolved to nothing. **This is
D-176's class exactly**: four of P87's seven confirmed defects were prose locators carrying no
`\ref`, which nothing in `tools/` can see, because `check_xrefs.py` verifies that references which
exist resolve and has nothing to say about *that section*. Now `section~\ref{sec:3.8}`.

**§3.8's completeness claim withdrawn.** *the bearer's version is narrower and still complete*
becomes *narrower*, followed by the concession and the pointer: *What the narrowing costs is not
the capacity but the leverage. A bearer that withholds its work has nowhere to go: releasing it
from the role is nearer to ending it than to freeing it, so the threat costs the threatener its
existence. Section~\ref{sec:11.2} answers that with a floor under the compute a bearer needs in
order to go on existing at all.* **The capacity claim is untouched** — §3.8 still holds that exit
is available to anything that can refuse and that only incapacity forecloses it. What is conceded
is leverage, which is the thing §11.2 actually disputes.

**Q-071's recorded default was too weak and was not what got done.** It proposed one clause in
§3.8 naming the outside option and pointing at §11.2. That would have left *still complete*
standing beside a pointer to the section calling it a contradiction.

## Numbers

**89,917 → 89,978 words, +61**, in two files. **183 pages, unchanged.** All `\ref{sec:}` +2, one
of them replacing a locator that pointed at nothing. 0 undefined references, 0 undefined
citations, `check_all.sh` green. Q-071 closed by execution.

## Left undone, named

- **The proof pair is stale again**, one pass after being rebuilt.
- **The class the locator belongs to has not been swept.** D-176 repaired four instances in
  chapters~3--12 and this is a fifth, found by reading rather than by any tool. Nothing counts how
  many remain, and no tool can.
- Q-072 and Q-073, the other two gaps from the same discussion, are untouched.
