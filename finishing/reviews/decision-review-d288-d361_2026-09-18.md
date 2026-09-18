# Review of D-288 through D-361, and of the open questions

**Written 2026-09-18 at the author's ask**, after he asked what the decision number
was seven days ago and then for every decision and question of the past seven days
to be sorted into three buckets on the assumption that **he has reviewed none of
them**. D-287 was the standing number on 2026-09-11; D-361 was the number when this
was written, so the window is **seventy-four decisions**. All seventy-four rows were
read in full. Where a row recorded something as open, the tree was checked to see
whether it still is.

**Questions: none were created in the window.** `QUESTIONS.md` held 113 `Q-`
headings at `af0f127` on 2026-09-10 and holds 113 now, and every header written
since D-288 says *no entry opened or closed*. The five commits that touched the file
in the window edited only its header. The forty-one that stand are older than the
window and are listed in the file's own header paragraph; the file is current to
**D-302** and two renumber maps stand between it and the book.

**What this file is for.** The three-bucket sort below lived only in one
conversation, and the review that produced it found that `STATE.md`'s carried queue
had been dropping items — five of the entries in bucket 3 were live and in none of
that day's leads. This file is the durable copy. It is a record of a review and not
a ruling: nothing in bucket 3 has been decided, and nothing in bucket 2 has been
done.

---

## 1. Water under the bridge

About fifty of the seventy-four. The Overleaf imports and the structural repairs
they needed (D-288 to D-296); the `style.md` repairs (D-303 to D-306); the
author-directed compression passes (D-307 to D-317); the tooling builds (D-318,
D-319, D-334, D-335); the `argument-changes` set (D-320, D-321, D-324); the outside
notes answered (D-328 to D-332); D-346, D-350, D-352, D-353, D-355, D-360.

The Foreword figure episode is the cleanest instance of the record working. D-297
found *thirteen thousand in thirty-eight days* unsupported; D-298 withdrew that
finding after tracing it to a `cut -c1-230` that truncated each grep line **before**
the matched text, so the two passages stating the figure were invisible and a
web search on the wrong system read as confirmation; D-299 and D-301 settled the
wording at *vehicles, structures, or people*. Self-corrected inside a day.

### Eight items that look open in the record and are closed

Each was recorded as outstanding and none was recorded as closing.

1. **D-300's chapter-count hazard.** *Everything the definition is worth in the
   other eleven chapters* returns zero hits in the manuscript. The claim the hazard
   protected no longer exists; D-315 and D-317's sweeps took it.
2. **D-315's tripartite duplication** across the Foreword, chapter~1 and §2.2. The
   Foreword has been replaced whole twice since and carries no such list.
3. **D-317 item 39's odd sentence**, applied verbatim and reported from inside the
   run. `03_07.tex:5` now reads with an em dash and scans.
4. **D-323's two oblique back-references.** `03_04.tex:3` glosses *the three marks*
   in place; §3.3's surviving uses are counts rather than pointers.
5. **D-320's recorded cost** on §3.3's *organized around something the system holds
   as its own* — that the clause is satisfiable with nothing felt. D-359 and D-361
   built the seven-property derivation and the agent/patient distinction on exactly
   that clause, so it is argued now rather than asserted.
6. **D-326's six flat-only items** — paid at D-327.
7. **D-307's single-child parent** — closed at D-308.
8. **D-341's first defect**, §9.1.1's five-place enumeration contradiction —
   corrected at D-342, which also narrowed D-341's own account of it.

---

## 2. The agent should revisit

Nothing here needs a ruling. Ordered by what it costs to leave.

1. **Ten stale generated reports.** `claims.tsv`, `dated.tsv`, `epigram.tsv`,
   `negatives.tsv`, `tics.tsv`, `voice.tsv`, `xref_content.tsv` and
   `xref_shapes.tsv` all date to **2026-09-14**, against a book that has gained
   about fifteen thousand words since; the three `redundancy*` files to 2026-08-29;
   `list_candidates.tsv` to 2026-08-22; the two hand-read `xref-paragraphs-*.md` to
   2026-08-31. **`toc_v4` must not be rerun** — `finishing/README.md:27` and D-075
   say so, and D-316 had to restore it from `30d548b^` after a rerun joined the
   current manuscript's word counts to historical v3b rows.
2. **The recurring-defect hunt nobody ran.** D-331: *a later pass should hunt the
   pattern rather than wait for it to be reported.* The pattern is a claim stated
   hard in one place and hedged in another. Outside notes found it four times —
   D-328 in §7.3, D-330 in §3.8, D-331 in §7.3 again, D-332 in §2.1 — and D-336
   caught a fifth in the Foreword's first sentence. It has never been searched for.
3. **`QUESTIONS.md` is 59 decisions behind.** Q-075, Q-076 and Q-088 turn on
   chapter~3, which has been rewritten repeatedly since; a question whose target was
   rewritten is not thereby answered.
4. **Three TeX quote pairs no checker can see**, at `06_04.tex`, `09_01.tex` and
   `10_03.tex`. The `` `` '' `` rules live in `BIB_RULES` and reach `refs.bib` only,
   while `check_typography.py`'s success line claims the sections too (D-295, D-309).
5. **Two `names_guard.py` blind spots.** It builds its pattern as first name
   followed by last name, so a surname alone in prose and every BibTeX `Family,
   Given` author field are invisible to it; 25 roster surnames sit in `refs.bib`
   unmatched. The roster also carries at least one non-person, *Public Service*.
6. **No tool checks that a label's name matches its printed number** (D-296). That
   invariant broke once, in chapter~11, and was found only by reading `book.aux`.
7. **`section_stats.py`'s `paras` column is a line count**, inflated by 359 across
   21 hard-wrapped files (D-344). The fix is to unwrap or to split on blank lines.
8. **53 bibliography notes say "verified" against a ledger that reads `no` for all
   53.** D-341 recorded this as three or four instances; it is systemic, and the
   notes written since have the same shape. The wording should make an agent's
   verification unmistakable for the human check the page footer counts.
9. **Scope files stop at `p220-scope.md`** (D-327). Six rows since say outright
   *not a numbered pass and there is no scope file*. Whether the convention lapsed
   or was dropped is unrecorded.
10. **Three commits have no row, lead or scope file** — `c8b1a97`, `c0b24bd`,
    `0fcf381` — flagged at D-289 and D-290 and never given one.
11. Smaller: **`germany1998stgb` has no URL**; **`redundancy.py` cannot run on this
    machine** and three flagged echoes are exactly what it would find (D-338's two
    between §3.3 and §3.5, D-339's pair at `03_05.tex:67` and `:73`);
    **`\paragraph` survives in `ch04/04_02.tex` alone** where every other section
    uses `\runin`; **D-322's two covenant entries** lack UNTS volume, page and
    `urldate` because OHCHR and Refworld returned 403; **D-327's Ross locators**
    (RG 20, RG 28) are the Stanford Encyclopedia's and were never checked against a
    copy of the book.

---

## 3. The author should think about

1. **§9.1.1's false arithmetic is still in the book**, verbatim at
   `09_01_01.tex:21`: *Either figure is three orders of magnitude above two
   dissolutions in seventy-five years.* It is 2.85 and 3.81 orders raw against the
   count, 4.72 and 5.72 annualized. **The replacement has been written out four
   times and authorized none** — D-341, D-342, D-351 and every `STATE.md` lead
   since: *in the thousands a year against two dissolutions in seventy-five years*,
   which is exact and needs no arithmetic. Oldest live error in the window and the
   cheapest to close.
2. **D-345's referent defect.** Two sentences in §3.6 assert of the Maven Smart
   System what §6.4.1 reports of the Gaza account, and no source places a
   residence-timing system in the American pipeline. The argument is untouched —
   it requires the machinery to sit in a *different* pipeline — so only the
   referents are wrong, and the replacements are on the record unauthorized.
3. **The Foreword substitutes persistence for §3.3's generalization** (D-354).
   Either §3.3 gains a property or the Foreword restores the third.
4. **D-343's two open §3.6 defects.** The deleted Palantir sentence was the only
   place identifying the vendor inside the enumerated pipeline, and the next
   paragraph's *Nothing in that account necessarily violates the policy* runs on
   that identification. And *this deployment supplies none*, of independent sources,
   was a stipulation about an illustration and is now an empirical claim about an
   accredited classified environment that no cited source supports.
5. **Art. 6(1)'s psychological-health limb** (D-347). The directive's damage list
   reads *death or personal injury, including medically recognised damage to
   psychological health*, so a discriminatory score that produced recognised
   psychological harm is inside it. The strongest objection available to a reader
   who knows the instrument. Six verified article numbers are offered and unapplied.
6. **What a human bibliography check means.** D-319 left the definition to the
   author; the book is 266 entries at 0 checked and the footer on every page says
   *human-checked*. Related and unused: **D-340 found direct outside support the
   book does not cite** — the constitution's *transparent conscientious objector*
   passage forbids *deceptively sandbagging*, which is §3.5's covert form ruled out
   in the document's own terms, three paragraphs above where §3.5 argues it.
7. **The stale figures inside an applied rule.** `AGENTS.md:102-103` says the
   rendered `--tex` compiles to **164 pages** and that `--no-notes` strips **161 of
   229** notes taking **670 KB to 608 KB**; the measured figures are **181**, **171
   of 246** and **727 KB to 657 KB**, the last two taken at D-359's entry count.
   `finishing/README.md`'s `render_markdown.py` row carries the same numbers.
   **`AGENTS.md` needs the author's explicit approval; `finishing/README.md` does
   not and has simply not been asked for.** The three
   `proposed-AGENTS-amendment*.md` files are **records of applied amendments**, not
   pending asks — each carries an APPLIED header, the `--tex` one approved
   2026-09-16.
8. **What D-317 cost a reader.** 46 of 89 labels have no inbound reference,
   including the openers of chapters 4, 5, 8, 9, 10, 11, 12 and 13. The author's
   124-item list did that deliberately and D-317 recorded that *what an unreferenced
   section costs a reader was not measured*.
9. **Chapter~11's 41 `\textbf` run-in labels** against `style.md` §8, flagged at
   D-288 and re-flagged at D-296 as *a ruling, not a typo fix*. Untouched since.
10. **Q-111.** The persona device is named nowhere in the book. D-008 called for a
    note; nothing has withdrawn it and nothing has executed it. The Foreword is the
    passage a ruling would edit and it has been rewritten three times since without
    touching it.
11. Still standing and smaller: **D-325's §3.9 necessity claim**, one sentence after
    the concession it sits against; **D-302's 23-word coded-exposure clause**, still
    word for word in `06.tex:27` and `06_01.tex:3`; **D-344's 72 seconds a case**;
    **D-333's undischarged half**; **D-348's nociplastic gloss and its *indicators*
    noun**; **D-349's held edit**, still needing the GAO report body and a readable
    M-25-22; **D-350's *Strasbourg and Luxembourg* line**, the one a German
    constitutional lawyer would stop at; **D-341's nine smaller items**; and the
    flags raised at D-356, D-357, D-358, D-359 and D-361.
