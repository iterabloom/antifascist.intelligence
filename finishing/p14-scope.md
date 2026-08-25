# P14 — the cross-reference *content* audit

**Drafted 2026-08-24. Decision: D-050.** Numbering is post-D-043 throughout.

## Why this pass exists

D-046 built `check_xrefs.py` and stated its own limit in the file:

> What this does NOT check: whether a reference that exists points at the RIGHT
> section. That is a semantic question.

The author supplied two suspected instances of exactly that. One was right, one
was not, and checking them turned up seven more. All 604 references resolve and
always did; `check_all.sh` was green before this pass and is green after it.
Resolution was never the problem.

## What the author reported

**(1) §10.1.1 leans on §8.1.1 for a roster §8.1.1 no longer carries.** Accurate,
and worse than reported — see below.

**(2) §8.7.4 refers backward to §8.7.6 for material that follows it.** Not
accurate. §8.7.6 does contain the four-way comparison §8.7.4 attributes to it
(EU risk-tiered statute, US sectoral patchwork, UK principles through existing
regulators, China's filing-and-licensing regime), under its run-in head
"Democracy, Authoritarianism, and Diverging National Rules"; and §8.7.4's second
pointer holds too, the Council of Europe Framework Convention being §8.7.6's
human-rights treaty. Nothing is orphaned and the prose makes no backward claim.
What is real is narrower and was left alone: §8.7.4 *opens* on a forward pointer
and then argues on top of it ("Those four already diverge sharply"), so a linear
reader meets the premise two sections before the evidence. That is an ordering
question for the author, not a repair. **Recorded as Q-020.**

## Method

`finishing/tools/xref_content.py`, new here. For each reference it pulls the
citing sentence, extracts proper-noun phrases, acronyms and years, and reports
those absent from the target section. 121 candidates over 610 reference-instances
on the pre-fix text. Every candidate was read by hand against its target.

**Yield: 9 defects, 112 false positives.** The false positives are overwhelmingly
the extractor treating a sentence-opening word ("Meeting", "Refusal", "Applied")
as a proper noun, or flagging a term that belongs to the citing section rather
than the target.

**The mesh size, stated rather than implied.** A wrong pointer in a sentence that
names no proper noun, acronym or year is invisible to this tool, and that is most
sentences. Nine defects found is not nine defects existing. The tool is kept out
of `check_all.sh` for the same reason: its output needs judgment.

## The nine defects

| # | Site | Was | Is | Why it was wrong |
|---|---|---|---|---|
| 1 | §10.1.1 | four `(section 8.1.1)` pointers | one, plus five citations | P11 cut the roster from §8.1.1; see below |
| 2 | §8.4.2 | "already covered in section 8.4.1" | "section 8.4 introduces" | the Partnership on AI is introduced in §8.4's opener, with the citation; §8.4.1 never names it and explicitly delegates self-regulation to §8.4.2 |
| 3 | §10.3.2 | "(section 8.4.1, section 8.7.6)" | "(section 8.4, section 8.7.6)" | same off-by-one; §8.7.6 half was correct |
| 4 | §8.5 | "Section 8.7.4 already makes the harder point about it" | the point made in its own right, §8.7.6 cited for the general form | §8.7.4 contains no GDPR and does not make the point. §8.7.6 makes it about AI statutes, not about GDPR specifically — so the sentence now carries its own claim rather than attributing a GDPR-specific argument to a section that does not make one. "Already" was also false: §8.7.4 follows §8.5 |
| 5 | §8.4.2 | "the EU AI Act's requirements for high-risk systems" (attributed to §6.4.3) | "the EU AI Act's Article 5 prohibitions" | §6.4.3 covers Article 5's bans; the high-risk tier is §8.7.6's material |
| 6 | §6.2.3 | "covered at length in section 4.1.2 and section 4.1.3, including the Model-Agnostic Meta-Learning algorithm" | "introduced at section 4.1.3 as the family of techniques that…" | §4.1.2 has no meta-learning at all; §4.1.3 has one clause; neither names MAML anywhere in the book outside §6.2.2 and the glossary |
| 7 | glossary, Partnership on AI | §5.5.3, §5.6.3, §6.3.3, **§8.1, §8.4.1**, §8.4.2, **§9.1.5** | §5.5.3, §5.6.3, §6.3.3, §6.4.3, §8.4, §8.4.2, §8.7.6 | three locators named sections that do not contain it; §8.4, where it is introduced, was missing |
| 8 | glossary, GPAI | §8.4.5, §8.7.1 | no locator; the entry now says the book does not take the term up | GPAI appears nowhere in the book's body — checked against every commit back to the split, not only the current text |
| 9 | glossary, Three Rs | §2.4.6, §8.6.3 | §2.4.6 | §8.6.3 contains no Replacement, Reduction or Refinement |

## §10.1.1, which was not only a pointer defect

Four pointers, against the current §8.1.1:

| Cited | In §8.1.1? |
|---|---|
| AI Ethics Lab | no |
| AI Alignment Forum | no |
| Center for Human-Compatible AI | **yes** |
| Stanford Institute for Human-Centered AI | no |
| MIT–Harvard Ethics and Governance of AI Initiative | no |
| AAAI/ACM Conference on AI, Ethics, and Society | no |
| SHERPA | **yes** |

Datable cause: the roster was in §8.1.1 at `7917f1c` (P7 Tier C) and was removed
at `30451e5` — P11's chapter-8 compression cut all five names in one diff.
§10.1.1 was written at `f0d5cd2` against the version that still had them, and its
`ledger.tsv` row still names the roster as the section's evidence. The two
pointers that survive, CHAI and SHERPA, are correct and were kept.

**The second-order problem, which is the serious one.** None of those five
institutions carried a `[[cite:ID]]`; their sourcing *was* the cross-reference,
and none of them had a row in `claims.tsv`. So P11 silently converted five dated
factual claims into claims resting on nothing, and P4's "zero unresolved
placeholders" was true of them only because they never had a placeholder to
resolve. All five were verified live under D-030 and are now C0727–C0731.

**Two claims did not survive checking**, which is why this is not a pointer fix:

- **CHAI is not an endowed center.** It launched at UC Berkeley in 2016 on a
  $5,555,550 Open Philanthropy / Good Ventures grant recommended over five years,
  renewed since. The book called it an endowed university center "not a grant
  with an expiration clause," which is the reverse of the facts. The text now
  says it outlasted the five-year grant it was launched on.
- **The MIT–Harvard initiative is not an endowed university center either.** The
  Berkman Klein Center describes it as "a hybrid research effort and
  philanthropic fund," launched 2017 on $27M from named donors. **Cut**, rather
  than corrected: with the endowment framing gone it was carrying nothing the
  other examples do not carry, and its own page has not been updated since
  February 2024, so "still running" is not assertable either.

Stanford HAI keeps its place with the claim narrowed to what checks out —
launched 2019 on endowed gifts rather than a term-limited award. AI Ethics Lab
(2017), the AI Alignment Forum (2018, posting within the week at time of check)
and AIES (annual 2018–2026, ninth edition) all verified as stated.

**The section's argument is unchanged and, if anything, better supported.** Its
conclusion was never that endowment predicts survival; it is that the dialogue
closest to a deployed product is the least protected kind, which §10.1.1's third
paragraph carries on the Microsoft and Twitter evidence. The endowment sentence
was a false premise sitting in front of a sound argument.

## What was checked and found sound

Recorded so it is not re-checked from scratch: §8.3.3 → §10.3.2 (the WIOA
evaluation, 23 million records, Jacobs and Canedy) resolves and is correct;
§2.3.1 ↔ §9.2.1 (the Ekman through-line D-037 built) is correct in both
directions; §9.2.1 → §2.3.1 for the Fore study is correct; §10.3.1 → §6.1.1/§6.1.2
for the Amazon, ACLU and Clearview cases is correct; §10.3.3 → §8.7.6 for China's
2023 generative-AI filing rules is correct; §6.2.2 → §4.1.3 was left alone, its
"an algorithm like Model-Agnostic Meta-Learning" being the citing section's own
example rather than a claim about the target's contents.

## Noticed and not chased

Measuring the two sections I rewrote against the rest of the book turned up
something outside this pass's scope. **Chapter 10 runs the D-025 contrastive-
negation construction at roughly 8.6 per 1,000 words**, the highest of any body
chapter, against the band's 4.63 and a book median near 5. Chapter 2 (6.95) and
chapter 6 (6.16) also sit above it. This is the same shape as Q-017: a tic no
review found, in a chapter no tic pass has swept.

Two caveats on the number. It was produced with an ad-hoc regex written for this
check, **not** with the project's own D-025 measure — it returns 1.61 for
chapter 5 where the D-044 pass reports 1.23, so it reads high by roughly a third
and the chapter ranking is what to trust, not the absolute figure. And the
glossary's 14.2 should be ignored: definitions distinguish by contrast, so the
construction is doing real work there.

My own edits added two instances book-wide and are not the cause. Not raised as
a question because it is D-025 chapter-sweep work with an established procedure
(P12), not a cross-reference matter, and P12's own record is a warning about
running that procedure quickly.

## Not done

- The 112 false positives were read but not individually annotated.
- No sentence without a proper noun, acronym or year was checked — see mesh size.
- The P13 hand read of all references against their targets was **not** redone in
  full; this pass is the mechanical filter plus its hits, which is a different
  and weaker thing.
- `.githooks/test_hooks.sh` still covers `commit-msg` only (open since D-045).
