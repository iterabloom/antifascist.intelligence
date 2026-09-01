# P80 — the eight cross-references that fail the four-way test, repaired

**The instruction.** Of the 399 references sorted as pertinent in
`xref-paragraphs-related.md`, name the ones that are simultaneously pertinent,
helpful, non-distracting and reader-friendly; then kill the reference at each of the
eight that are not, bringing in a gloss of the referenced material at discretion.

**Eight of 399 fail, and they fail on only two of the four.** Nothing in the file
fails *pertinent* or *helpful*, which follows from how the file was built. What
discriminates is `style.md` §7 — *the sentence carrying a reference has to make sense
to a reader who does not follow it* — and distraction.

## Where the eight came from

Two screens, both candidate finders rather than verdicts, both hand-read after.

**§7's failing shape**, an empty head noun whose content lives in the target: 37
sentences matched, **and most of them pass**. A colon or a dash supplies the content
locally in the great majority — *the construction section 4.2.3 describes as
cooperative inverse reinforcement learning*, *the form section 5.2.1 settles on: what
is worth engineering is compassion*. Six failed on reading, two of them outright.

**References set off as asides**: 5 in parentheses, 6 in a mid-sentence dash pair.
**The parentheses are the best-behaved references in the book and the screen was
built expecting the opposite** — the sentence completes before the parenthesis, so a
reader can skip it entirely, which is exactly what §7 asks for. Only chapter~3's
opener and two other sites use the form. Two of the six dash asides failed.

## The eight, and the discretionary call at each

| site | what went | gloss? |
|---|---|---|
| §5.7.1 | *the thing chapter~3 wants* | **yes** — *what makes a commitment hold against the party that instilled it*, which is what §5.1 says chapter~3 needs and cannot get elsewhere |
| §9.3.3 | *What the instrument does not supply is the part chapter~3 says is load-bearing.* | **no — sentence cut.** It announces what the next sentence then does, which is `style.md` §2's rule; the next sentence already says a pet trust binds a caretaker and not the party the arrangement exists to constrain |
| §4.2 | *a property section~3.1 shows is not enough at any degree* | **yes** — *whoever holds the stage can still revise the decision*, stated as a colon clause |
| §5.2.2 | *the question section~3.4 has to answer about a bearer* | **yes** — *whether a bearer holds anyone's welfare as a reason when reward and instruction point the other way* |
| §11.2 | *The removal cases section~3.1 carries* | **yes** — the cases named: *Trump v. Slaughter* and *Trump v. Cook* |
| §12.3 | *at the price section~3.9 sets out* | **no — clause cut.** The section's own closing paragraph states the price at full strength four paragraphs later; a gloss here would be the repetition P69 to P72 spent four passes removing |
| §3.5 | *— section~10.6 carries the strike —* | **no — aside cut.** A gloss naming the strike would be a longer aside in the same position, which is the defect being repaired |
| §6.4.2 | a 30-word aside between *Independent third-party audits* and its verb *matter* | **no — recast.** Both claims kept, the aside promoted to its own sentence |

**A gloss was added where the reference was carrying content and cut where the
content was already on the page.** Five of the eight are cuts or recasts for that
reason, and the discretion is recorded here rather than exercised silently.

## One repair fixed a defect nobody had reported

**§11.2 used the bare *Slaughter* with no antecedent inside the section.** The
paragraph opened on *the removal cases section 3.1 carries* and closed, eleven
sentences later, on *That it is not what Slaughter reached, I can* — a case name
introduced nowhere in the section. Naming both cases at first mention supplies the
antecedent the later sentence had been borrowing from chapter~3.

## A slip, and the check that would not have caught it

The §5.2.2 gloss was written with a **curly apostrophe** in *anyone's*, against
`style.md` §8, which holds that apostrophes stay straight. **`check_typography.py`
does not check apostrophes and says so in its own docstring**, so the suite passed
on it; it was found by grep and fixed before the build.

**This is a source-convention violation and not a print defect.** LuaLaTeX sets a
straight `'` as `’` — the same glyph the curly character produces — so nothing on the
page would have differed. Recorded because an agent writing new prose is exactly the
route by which the wrong character enters, and nothing in the suite is watching that
door.

## What was checked before the cut

**Nothing was orphaned.** Inbound references after the cut: `sec:3` 48, `sec:3.1` 13,
`sec:3.4` 11, `sec:3.9` 4, `sec:10.6` 4, `sec:5.6.2` 5. No `\autocite` sits in any
removed span and `refs.bib` is untouched.

**Five paragraphs now carry no cross-reference at all** — §5.7.1, §9.3.3, §4.2, §3.5
and §6.4.2 each lost their only one — which is why the paragraph inventory falls 295
to 290 while the reference count falls 403 to 395.

## Measurements

| | before | after |
|---|---|---|
| body cross-references | 403 | **395** |
| paragraphs carrying one | 295 | **290** |
| book | 90,795 | **90,767 words**, down 28 |
| pages | 182 | **182** |
| sections · `refs.bib` | 136 · 300 | **unchanged** |

`check_all.sh` green after `refresh_order_shas.py`; 0 undefined references and 0
undefined citations.

## What this pass did not do

**The 32 paragraphs that close on a pointer sentence were left alone.** They pass all
four tests — the target is the paragraph's own subject, the sentence carries its own
content, and the end of a paragraph is the least distracting position there is. They
are removable on density grounds and they are not defective, **which is the pass's
finding: cutting for density and cutting for quality select different sets**, and the
second is now nearly exhausted at eight repairs in 399.

**Reciprocity was measured, claimed as a quality signal, and the claim does not hold.**
**The first figure was wrong**: 43 percent counted matches made through an ancestor —
§11.2 → §3.1 scoring as reciprocal because §3.1 → chapter~11 exists. **True A↔B
reciprocity is 20 percent: 72 edges, 36 pairs.**

**The claim was that reciprocity separates a division of labor from an aside, and the
test refutes it.** Paragraph-closing pointer sentences — the aside-shaped group — are
reciprocated at **26 percent against a book-wide 20**, which is the wrong direction. A
section that hands off explicitly is likely to be handed to, so the shape and the
reciprocity go together rather than apart.

**Reciprocity is a property of the pair; quality is a property of the edge.** §3 →
§12.1.2 is the bare parenthetical *(section 12.1.2)* and is reciprocated by a
substantive sentence in §12.1.2; the partner's quality says nothing about it. §3 → §4
and §3 → §5 are reciprocated, and §3's half is *Then I spend chapters 4 and 5 on
learned judgment*, which is the book narrating its own contents inside a
self-criticism paragraph. **The reciprocity in both cases comes entirely from the
other direction.**

**All 36 pairs were read, and *division of labor* describes about a third of them.**
Twelve are genuine divisions where each half names the portion the other carries —
§3↔§4, §3↔§5, §4↔§5, §8↔§9, §6↔§10.2, §10.2↔§10.6, §8.3.3↔§8.3.4, §4.3.1↔§5.7,
§11.1↔§11.2, §2.2.1↔§11.8, §2.1.2↔§11.3, §4.2.6↔§11.5. The other twenty-four are
**mutual imports**: each section borrowing a result from the other, which is
substantive and is not a division. **Neither group is decorative**, so the objection
that a reciprocal pair might be a reciprocal aside is not what the reading found —
what it found is that the label was wrong for two-thirds of them and that reciprocity
does not grade an edge either way.

**What survives is a structural fact and not an instrument.** 20 percent of edges are
two-way. A density cut might want to know when it is about to leave a one-way pointer
where a two-way one stood, and that is the only use this measurement supports.
