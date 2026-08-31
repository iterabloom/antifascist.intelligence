# P77 — the glossary cut from 57 entries to 16

**The author's finding.** The glossary is 60-odd entries and the longer ones
restate their sections without compressing them; the *Bearer* entry is a 200-word
précis of chapter~3 with five cross-references in it. **If a term needs 200 words
of gloss the reader needed the chapter; if it does not, the entry should be one
sentence.** Entries like *BERT* and *Adversarial examples* are standard-dictionary
material the book does not need to own. **Cut to the terms genuinely the book's
own and used in a non-standard sense** — perhaps fifteen. Everything else is in
the index's job description or the reader's.

**The diagnosis holds and the cut is executed at 16 entries.** Three figures need
correcting and one of the named terms had no entry at all.

## Corrections to the finding's figures

| The finding says | Measured |
|---|---|
| 60-odd entries | **57** |
| *Bearer* is 200 words with five cross-references | **169 words with seven.** *Floor* is the 197-word, nine-reference entry; the description fits it better |

Both were the shape the finding names, so the correction changes nothing about
the remedy. **Neither figure was checkable from the printed page** — the entries
carry no visible count — which is why they are recorded rather than treated as an
error in the reading.

## The glossary was fully self-contained, and that is why the cut is clean

| | |
|---|---|
| inbound `\ref{sec:13}` from the book | **0** |
| prose anywhere in the book mentioning the glossary | **0** |
| `\autocite` in any entry | **0** |

**Nothing outside chapter~13 pointed into it and no entry carried a citation**, so
cutting 42 entries orphaned no bibliography row and stranded no pointer. This is
the inverse of P72, where cutting one paragraph took two citations and a glossary
entry with it; here the dependency graph runs one way only, out of the glossary
and into the sections.

## One keep was forced, and the deixis was swept after the cut

The *Bearer* entry says a bearer must be governed *as a prospective moral patient
in the strong sense of \emph{sentience} below*. **Cutting *Sentience* would have
stranded that**, from inside the entry the instruction protects first. It is kept,
and it is the one entry on the list that the author's own selection did not name.

Every internal reference was then re-checked against the surviving alphabetical
order:

| entry | says | resolves to |
|---|---|---|
| Bearer | *\emph{sentience} below* | Sentience — last entry |
| Moral agency | *\emph{moral competence} and \emph{moral performance} below* | both follow it |
| Molar and molecular fascism | *the four features above* | Four structural features |
| Recuperation | *the first of the four features above* | Four structural features |

**All four hold. Two of them only hold because the new entry was written**, since
*the four features* previously had no entry and both referring entries pointed at
a definition the glossary did not carry.

## The entry that did not exist

*The four features* is on the keep-list and **there was no such entry**. The four
structural features of fascism are defined at §2.1.2 and were glossed piecemeal
inside *Recuperation* (which named the first) and *Molar and molecular fascism*
(which named their molecular restatements). **Written on the author's ruling**, at
58 words, naming all four and the reason the fourth is load-bearing. It is the
only addition in the pass.

## An entry that claimed more than the book does

*Humane values* read: *“The book's preferred term, chapters~\ref{sec:4} and
\ref{sec:5} onward, for the values an AI system's design should track.”* **The
phrase appears twice in the entire manuscript** — once as section~5.6.2's title
and once in section~5.4. It was also **the only entry in the glossary carrying no
section locator at all**, which is what a term with no section developing it looks
like. This is P75's class: prose stating a reason that is not true, with nothing in
the suite able to see it. The entry is kept on the author's ruling and rewritten to
what holds, with §5.6.2 as its locator. **Whether a term used twice earns an entry
is a separate question and is not settled here.**

## The opening note overclaimed in the same way

It said *several are the book's own working definitions*, which was true of 57
entries and is the selection principle for all 16. Rewritten to state the rule the
glossary now runs on: every entry is the book's own definition or a word it
narrows, terms carrying their standard technical meaning are not here, and each
points at the section developing it.

## What was cut

42 entries. Standard technical vocabulary (*BERT*, *Adversarial examples*,
*Few-shot learning*, *MAML*, *Transfer learning*, *Federated learning*,
*Differential privacy*, *LIME and SHAP*, *RLHF*, *Reward hacking*, *Scalable
oversight*, *IRL and cooperative IRL*, *Interruptibility*, *Red-teaming*,
*Theory of mind*, *Alignment problem*, *Explainability and transparency*); named
systems and cases the book cites rather than owns (*COMPAS*, *Clearview AI*,
*GPT-3 and GPT-4*, *Moral Machine*, *AIGS Index*, *Partnership on AI*, *Concept
injection*); and other people's terms the book uses as they are (*Capabilities
approach*, *Constructed emotion*, *Controlled hallucination*, *Predictive
coding*, *Attention schema theory*, *Inattentional blindness*, *Dual-process
theory*, *Growth mindset*, *Hard problem of consciousness*, *New Jim Code*,
*Racial capitalism*, *Responsibility gap*, *Three Rs*, *IRB*, *Digital divide*,
*Corporate doublespeak*, *Moral apprenticeship*, *Compassion*).

**The two closest calls, both cut, both named rather than argued.** *Three Rs*
carries the book's own adaptation of a standard framework — *the book adapts it as
a starting point for research involving candidate-sentient AI systems* — and
*Corporate doublespeak* attaches the book's own diagnosis of self-regulatory
failure to an ordinary term. Each is a standard term with the book's own use
hanging off it, which is the boundary the instruction's test draws, and each fell
on the standard side of it.

## The survivors were compressed too

On the author's ruling that the rule applies to what stays. Every entry is now a
definition plus locators, with the section-by-section résumé removed:

| | before | after |
|---|---|---|
| Floor | 197w, 9 refs | **96w, 4 refs** |
| Molar and molecular fascism | 194w | **78w** |
| Bearer | 169w, 7 refs | **91w, 2 refs** |
| Exit | 136w | **83w** |
| Recuperation | 128w, 7 refs | **95w, 3 refs** |
| Sentience | 86w | **70w** |

What went out of *Floor* is the deontology objection and the list of three places
the book reaches the requirement independently; out of *Bearer*, the walk through
sections 3.4, 3.5, 3.8 and 3.9; out of *Recuperation*, the three per-section
pointers into chapter~7. **In each case the claim survives and the tour of where
it is argued does not**, which is the finding's own rule.

## Measurements

| | before | after |
|---|---|---|
| entries | 57 | **16** (42 cut, 1 written) |
| glossary | 3,233 | **1,098 words** |
| book | 93,286 | **91,151 words**, down 2,135 |
| pages | 186 | **182**, down 4 |
| glossary locators | 114 | **30** |
| book-wide `\ref{sec:}` | 547 | **463** |
| `refs.bib` | 300 | **300**, nothing orphaned |
| sections | 136 | **136** |

`check_all.sh` green after `refresh_order_shas.py`; 0 undefined references and 0
undefined citations. Printed page 144 rasterized and read.

## Named for a ruling and not acted on

**The book has no index**, and the finding assigns work to one twice — *in the
index's job description*. A cut glossary and no index means a reader who meets
*COMPAS* or *scalable oversight* in chapter~9 has nothing to look it up in.
Whether to build one is a decision this pass did not take and the repository has
not recorded.
