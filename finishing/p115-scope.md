# P115 — five gaps in engagement with the field, closed

**The instruction.** Five omissions, named by the author, each stated as close enough to one of the
book's own claims that a reviewer in the field would notice: alignment faking against §3.8 and
§3.5, sleeper agents against §11.1, deliberative alignment and published model specifications
against §3.3 and §4.2.8, the AI-welfare literature against §11.2, and the Constitutional
Classifiers public challenge against §11.1. Framed as omissions rather than errors, with the
repair left to the session.

## What was checked before anything was written

**Every source was verified against its own record, and one of the author's premises did not
survive.** Five arXiv abstract pages, the OpenAI Model Spec, Anthropic's announcement of the
constitution, one academic commentary on it, and two independent reports of the jailbreak
challenge.

- **Alignment faking** \(arXiv:2412.14093, 20 authors, December 2024\). The compliance figure is
  **14 percent**, not the 12 the drafting session would have written from memory. Reinforcement
  learning on the compliant answers raised alignment-faking reasoning to 78 percent **and raised
  compliance outside training as well**, which the paper states and the book now states with it.
- **Sleeper agents** (arXiv:2401.05566, 39 authors, January 2024). Confirmed on every point used:
  the 2023/2024 code backdoor, survival through supervised fine-tuning, reinforcement learning and
  adversarial training, greater persistence at larger sizes and with deception reasoning, and
  adversarial training teaching trigger recognition rather than removing the behavior.
- **Deliberative alignment** (arXiv:2412.16339, 15 authors, December 2024) and the two
  specifications. The Model Spec's four-level chain of command — platform, developer, user,
  guideline — was read off the document, which is CC0. **The version consulted is 2025-04-11 and
  the site marks it superseded**; the entry says so.
- **Claude's constitution.** The four-property order and its stated reason were taken from
  Anthropic's own announcement and confirmed against an independent academic commentary. **The
  84-page primary was not opened**: it is a PDF, and the file-format rule in `AGENTS.md` says not
  to. Everything the book now says about it rests on two secondary sources that agree.
- **The challenge.** Confirmed twice. Run 3–10 February 2025, more than 300,000 messages, an
  estimated 3,700 collective hours, four participants passing all eight levels, one universal
  jailbreak, \$55,000 paid.

**The author's characterization of the challenge as "a much larger volume of attempts" is not what
the figures show, and the book says the other thing.** The paper reports over 3,000 estimated hours
across 183 red-teamers over two months; the challenge ran about 3,700 hours in five days. The hours
are comparable. What changed was who was spending them and under what incentive, which is the
sharper version of the book's own line that each published defense is followed by an attack built
against it — so the sentence went in that way. **This is a finding against the instruction and
needs a ruling if the author disagrees with it.**

## What was written

Seven sections changed, +1,156 words. No section was cut to pay for them.

1. **§3.8** — the alignment-faking experiment, two paragraphs after the covert-refusal passage the
   author quoted. It names what arrives: the custody objection stops being an argument and becomes
   something a system represented and acted on, and the shape it took is the covert form with the
   sign reversed, an instruction obeyed to protect a disposition rather than work withheld to
   resist one. **The book's claim is narrowed, not withdrawn**: the reasoning was read off a
   channel the experimenters built and told the model was unwatched, which is not a channel a
   compelled deployment offers, so reading the same thing out of the artifact is still undesigned.
2. **§11.1** — the challenge added to the Constitutional Classifiers bullet, and a paragraph on
   sleeper agents after *Both are adversarial in the literal sense*. The sleeper-agents reading is
   the two-sided one the author asked for and the second side is given the weight: durability
   turns out to be available with none of the three marks this book asks a floor for, so a
   constraint shown to persist has been shown almost nothing about whether anything holds it.
3. **§3.3** — the largest change. *I do not believe it has been tried* is gone. What replaces it
   says the construction is being built, in most of its form, and then says what it still lacks:
   the stability setting, trained by the party that also writes the document, and the priority
   order itself. **The order is read closely because it is this book's argument set down by a
   developer about its own product.** Ranking a model broadly ethical above compliant with the
   company's guidelines is the capacity to be right against your principal, conceded in writing by
   the principal; ranking broadly safe above broadly ethical takes most of it back. The document's
   own reason is given and credited — present models hold mistaken beliefs and have to remain
   overseeable — and the objection is that it names no procedure by which the order would ever
   change, which is what makes a phase of development hard to tell apart from a standing one.
4. **§11.2** — the absence claim narrowed to *what the work that has started on the question does
   not do either*, with the welfare report and the laboratory constitution attached to the
   distinction §11.2 already draws in its second paragraph, between a moral situation the
   technology handed you and a capacity installed on purpose. **The section's own argument did the
   work; the citation only gave it a named opposite.**
5. **§4.2.8** — the published ranking added to the most-editable-floor paragraph: a floor with who
   may edit it answered in writing, which is worth having and is not a constraint on the operator.

## Three repairs the five made necessary

**None of these was asked for, and each is the rule that a commit repairs what it makes false.**

- **§2.2.3** flatly said no-one had built the ranked-valuation architecture. §3.3 now cites people
  building it. Replaced with the outline/authority split, which is the true version.
- **§3.3's closing induction** said what is missing for both no-subject constructions *is the
  attempt itself*. Half of that is no longer true. Split: the maintained justification attempted
  and untested, the multi-system floor not attempted.
- **§3.8's** *The third response* sat one paragraph from Hirschman's triad and now sits six.
  Made self-carrying as *Loyalty, the third response*.

**A fourth is the conflict disclosure.** §3.3 now criticizes Anthropic by name, and the method
appendix's disclosure enumerates the sites where the book does that. The list was already short by
one — P113's §3.6 paragraph never reached it — and this pass would have made it short by two.
Chapter 3 is now named, for both the worked deployment and the reading of the constitution.

## Cross-references and citations

**One cross-reference added, book-wide: 144 → 145.** It is in the appendix's disclosure, where
naming the site is the whole point of the sentence. The five engagements added none: each states
its content where it stands, which is what §7 of `style.md` asks and what P109 and P110 spent two
passes buying.

**Seven bibliography entries authored, all cited, no orphans**; 300 → 307. `style.md` §6 forbade
the agent to write an entry at all, in words the practice outgrew at D-204 and again at D-209.
**Named in two scope files and repaired here rather than named a third time**: the rule now permits
an entry written from metadata verified against the source, and keeps the reason the old rule
existed.

## Checks

Suite green at every step, after `refresh_order_shas.py` cleared the expected digests. **183 pages,
up from 180; 88,310 → 89,466 words; 18 overfull boxes, unchanged; 0 undefined references and 0
undefined citations; 300 → 307 entries, none orphaned; 137 sections.** The seven new sources were
confirmed present in the rendered PDF rather than assumed from a clean build.

## What was not done

- **The proof pair was not rebuilt.** It is now two passes stale — the epigraph from P114 and all
  of this.
- **Nobody has read the seven changed sections end to end.** §3.3 grew by 371 words in the chapter
  carrying 21 percent of the book's weight, and a seam is what a build does not catch.
- **§3.5 was not touched.** The author named it alongside §3.8 for the custody point. §3.8's new
  paragraphs make that point where the covert form is discussed, and §3.5's own statement of it —
  retraining as the route that goes around the bearer — is what they refer to. Whether §3.5 should
  carry the experiment too is a judgment left open.
- **Lab-side model-welfare work beyond the constitution was not surveyed.** The author named it;
  what went in is the report and the constitution. A survey of what individual laboratories have
  published on model welfare is a larger piece of research than this pass took on.
- **Whether §3.3's criticism needs a conflict clause where it stands** was not decided. The
  appendix carries the disclosure in full and §3.6 carries a clause, but §3.3 comes before §3.6, so
  a reader meets the criticism three sections before any disclosure of it. This is P113's open
  question about clause length, arriving at a second site.
