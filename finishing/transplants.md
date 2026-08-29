# Transplant spec

The one exception to revise-only (D-014): roughly 12,000 words may move from
`cognition/` into the book. This spec says which words, where they land, what
each one corrects, and what has to change about them on the way.

**Committed: 10,400 words across 16 transplants. Headroom: 1,600.**
Hold the headroom — analytic prose has to *state* what case-first prose *shows*,
so several of these grow under the register edit.

## Three corrections to earlier reports

1. **§2.4.1 is 570 words, not 188.** The 188 figure was wrong and was repeated in earlier summaries. It is not a stub — it is a full-length section that is wrong, so its mode is *replace*, not *fill*.
2. **"pain" appears 5 times in the manuscript, not 3** — all five in chapter 2, and every one is a *hypothetical research protocol*, never a definition. "nociception" appears 0 times. "sentien\*" appears 235 times. The book uses the word sentience 235 times and never says what it would hurt.
3. **The level-6 targets no longer exist as sections.** Triage folds §§3.1.2.3.1.\* and §7.4.3.2 under D-010. P1 (structure) runs before P3 (revise), so every transplant below is addressed to the **fold target**, with the originating file named.

## Ordering constraint

Three transplants aim at sections that D-013 may merge away: §2.3.1 and §2.3.2
are in the emotional-intelligence cluster, §7.4.1 is in the 2.4/7.4 parallel
treatment. **Adjudicate D-013 before drafting T6**, or the budget lands in a
section that then merges.

## The transplants

Source line numbers are into `cognition/atlas of human brain_2026-08-22.tex`
unless noted. "Budget" is the text as it appears in the book, after editing.

| # | Source | Target | Corrects | Mode | Budget |
|---|---|---|---|---|---|
| T1 | ch3 L1190–1230 + `pain-suffering-self` L1–17 | §2.4.1 Defining Sentience (570 w) | Definition is awareness/consciousness/qualia; **no criterion is valence**. Imports the nociception → pain → anticipated pain → suffering ladder | replace-section | 750 |
| T2 | ch3 L903–931, L963–1019, L1074–1122 | §7.4.3 (via folded 7.4.3.2, 652 w) | Proposes measuring AI suffering by self-report, behavior, "physiological correlates", comparison — with no theory of pain | insert before item (4) | 900 |
| T3 | ch13 L5050–5122 + L5185–5229 | §2.2.1 (484 w) | "Compassion… an evolutionary extension of empathy" — the dissociation refutes it | replace-section | 900 |
| T4 | ch7 L2383–2462 | §2.2.1 | "The mirror neuron system, **which is key in empathy**" — the clearest false sentence found | boxed-case | 450 |
| T5 | ch11 L4132–4186 | §3.1.2 (via folded .4, 647 w) | A five-item DLPFC list that installs a homunculus | replace-passage | 700 |
| T6 | ch9 L3389–3442 + L3443–3518 | §2.3.1 (418 w) | Goleman's four components presented as fact; imports both camps **plus the balancing aside** | replace-section | 900 |
| T7 | ch13 L5123–5184 | §2.2.3 (611 w) | Nothing in the challenges list is that empathy itself misfires. **D-016: taken unframed** | insert-passage | 700 |
| T8 | ch10 L3650–3709 | §4.3.1 (429 w) | Dual-process presented as settled; no critic appears | insert + retitle | 550 |
| T9 | ch13 L5298–5362 | §2.3.3 (458 w) | "register its **internal frustration**" — self-awareness as an inner observer | replace-passage | 700 |
| T10 | ch5 L1580–1629 | §2.4.1 | "hard problem" appears **once in 115k words**; a zombie passes all seven of §2.4.1's criteria | insert-passage | 550 |
| T11 | ch4 L1306–1365 + L1469–1505 | §3.1.2 (via folded .1, 589 w) | Generic attention survey | replace-section | 600 |
| T12 | ch6 L1979–2033 + L2163–2201 | §3.1.2 (via folded .2, 517 w) | Predictive coding appears in the *last* paragraph as "the next frontier"; make it the premise | replace-section | 550 |
| T13 | ch1 L372–425 | §3.1.2 (via folded .3, 505 w) | Memory as "retention and recall"; storage-and-retrieval throughout | insert-passage | 650 |
| T14 | ch2 L663–710 | §3.1.2 | "akin to the short-term memory buffer"; seven → four | insert-passage | 350 |
| T15 | `human-cognition_*.mermaid` | §3.1.1 (492 w) | Lists ACT-R and Society of Mind without adjudicating | figure + caption | 350 |
| T16 | ch9 L3443–3462 | §3.1.2 (via folded .6, 821 w) | "the amygdala is **predominantly responsible**"; "insular cortex" — **this is T6's risk mitigation** | insert 2 sentences | 250 |

### The one contradiction, and its fix

T6 imports the constructionist account of emotion into chapter 2. The worry was
that this contradicts §§3.1.2.3.1.6–.10. Checked: those sections contain **zero**
hits for basic-emotion vocabulary (Ekman, six, universal, discrete, facial
action). They are not written in the basic-emotion frame — they are written in a
**localizationist** frame, which is a narrower conflict: two sentences claiming
the amygdala and insula are "predominantly responsible" for emotional appraisal
and subjective experience. **T16 fixes exactly those two sentences for 250
words.** With T16, chapter 3 concedes the narrow point and cross-references
chapter 2. Without it, the book contradicts itself quietly.

### T7 unframed (D-016): the coherence obligation

The author's ruling is that the challenge stands at full strength and chapter 2
absorbs it. That is an argument-level choice, and it creates work the transplant
itself does not pay for. Checked against the actual text, the obligation is
**three edits, all inside revise-only**:

1. **§2.2 (parent, 486 w) calls empathy and social intelligence "indispensable"** and says they "lay the groundwork" for AI understanding of human emotion. After T7 that claim is unqualified in a chapter that publishes its refutation. One sentence conceding the dissociation, pointing to §2.2.3.
2. **§2.2.3's shape changes.** It is currently an opportunities list followed by implementation challenges. T7 adds a challenge of a different kind — not "this is hard to build" but "this may be the wrong target." The section needs its two halves re-labeled so the reader sees the distinction.
3. **The chapter title.** "Foundations of Empathy and Compassion in Friendly AI" survives T7 only if compassion is doing the load-bearing work, which after T3 it is. See Q-011.

What it does **not** require: rewriting §2.2.1 (T3 already replaces it), touching
§2.2.2, or reopening the book's own title, which is about altruism and
anti-authoritarianism rather than empathy.

### A separate defect found while checking this

**Chapter 2's opener does not describe chapter 2.** Its 74 words are about
authoritarian regimes and reinforcement learning — anti-authoritarian ethics, the
subject of §2.1.4 — and say nothing about empathy, compassion, or foundations.
The openers for chapters 3, 4 and 9 do match their chapters; chapters 5, 6, 7, 8
and 10 have none at all. This is unrelated to T7 and predates it. Logged against
§2 in the ledger; the fix is a `revise`, not a transplant.

### Register edit, quantified

Across the whole Atlas: 390 second-person instances, 45 `\aside{}` boxes, 112
cross-chapter references, 123 British spellings, 122 curly quotes.

- **Only T5 (7) and T9 (12) lose real force** when the second person goes. T11 has **zero** — which is why T11 should be piloted first.
- **112 dangling cross-references are a feature.** The book has two cross-references in 115k words and style.md §7 wants one per section; the transplants supply about fifteen honest ones.
- **Three asides are load-bearing and must survive:** the basic-emotion aside (T6 — it is the balance device), the Chalmers non-physicalism aside (T10), and the nocebo/informed-consent aside (T2, the most directly relevant thing in the Pain chapter to a book about experimenting on sentient subjects).
- **~40 instances characterize named persons** — attributing motive, mental state, or intellectual trajectory to living or recently-living people. Every one must be rewritten as a claim about a *published finding*. Naming gate control theory and its authors is ordinary citation; saying a researcher "stepped back from the broader claims" is not. This is the least mechanical part of the edit and the one that cannot be delegated to a script.

## Reserve list

Promote from headroom in this order: **phantom limb pain** (ch3 L1020–1073) —
the cleanest demonstration that pain needs no body; **central sensitization**
(ch3 L1123–1189) — a mechanism by which a persistent system's harm outlasts its
cause, directly relevant to long-running deployments; **relational personhood**
(`pain-suffering-self` L36–70) — "personhood is a standing granted in
relationship, not a cognitive achievement", a direct rival to §7.4.1's
six-criteria approach, **revisit after D-013**; **blindsight** (ch5 L1815–1858,
unread). Held back mainly to avoid a fourth pain passage in the same fold.

## What not to use

**`ChatGPT-gorilla_2022-12-19.md` — drop it entirely.** Four reasons: despite
the filename it contains no inattentional-blindness probe (it is a
physical-reasoning and gaze probe), so it does not connect to T11 as assumed;
its interest is that a 2022 model needed four turns of coaxing to say a dropped
cup spills, which is a dated capability claim about a superseded system; lines
14–36 are thick with characterization of a living scientist including two
book titles that appear to be model confabulations about a real person's
bibliography; and where its subject matter is genuinely needed — attention
schema — the book already has it and T11 strengthens it. If it belongs anywhere
it is a one-line pointer in the "On method" note, not a transplant.

**`pain-suffering-self_2026-08-22.txt` — use pairs 1–3 only** (T1 draws on
lines 1–17). The rest is a voice transcript with disfluent prompts and
chat-formatted answers, carries 17+ named people with characterized positions,
and its later pairs are saturated with 2026 model-research claims that would
each need a dated box and a verifiable citation. **Line 219 names a vendor and a
shipped product; no transplant touches it and it must not enter the book.**

## The figure (T15)

The `.mermaid` file cannot be rendered here — no mermaid-cli, no Node packages,
no network — and rendering it as-is would not produce a printable figure anyway:
32 nodes, 41 labeled edges, three type sizes per node, HTML tags inside labels,
and nine `classDef` styles whose meaning is carried by *dash pattern*, which at
book column width is indistinguishable.

Treat the file as the **specification** and have the figure redrawn to print
spec: ~12–15 nodes, the four "ghost rival" nodes kept (they are what make it
honest — it draws its own opposition), the confidence tiering preserved, the
legend rebuilt as a proper key. That is a design task, not a build step. The
`.mermaid` stays in `cognition/` as provenance and as the machine-readable
record of what the figure claims.

**Placement caveat:** the diagram asserts pain-as-verdict and the borrowed
self — T2's and T3's arguments, which land in chapters 2 and 7. In §3.1.1 it
forward-references material the reader has not met. Either move it later or
caption it as a map of the book's cognitive commitments with pointers.

## Where a cross-reference beats importing

Four places where the material is excellent and the import is wrong:

1. **The fourteen "Why the maps disagree" sections.** The Atlas's structural signature and its best writing — but they are *meta-scientific*, about how reference works carve cognition differently. This book has no such frame and building one for a single passage is a rewrite.
2. **§3.1.2 after the fold**, if it gets crowded. Six transplants land in one folded section, adding ~3,100 words to a chapter already at 24k. The honest move for the two weakest (T14, T16) would be a sentence plus a pointer.
3. **Language.** The book has no language-as-cognition section and PLAN.md rules out adding topics. A one-line pointer closes an acknowledged gap honestly.
4. **The Mind's Eye / aphantasia.** Its opening — "Picture an apple, and a private theatre lights up — or, for some readers, it does not" — is the one passage whose entire value *depends* on the second person: it works by the reader discovering something about themselves mid-sentence. Third-person recasting destroys it. **Never import this.**

Cost of all four as pointers: under 150 words from headroom, plus a back-matter
line establishing the *Atlas* as a companion work in progress.

## Pilot

**T11 first.** 600 words, zero second-person instances, replaces rather than
argues, lands in the chapter P3 starts with, and carries the lightest
person-scrubbing load in the set. The Atlas is nearly free of the manuscript's
signature tic ("foster", 278×), so transplants will read as a different voice
even after editing — that is PLAN.md's register-clash risk. If the register
survives T11, it survives the rest.
