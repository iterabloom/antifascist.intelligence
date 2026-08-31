# P72 — the trolley narration compressed, the paperclip maximizer cut

**The author's findings.** §5.3.1's trolley material earns most of its keep,
because the book does something non-standard with it — *the cooler answer is the
one with less flinch in it, and a system built to override intuition with
deliberation whenever they disagree is built to resemble the profile of a patient
for whom losing the flinch is a symptom* — and the setup is required. **What can
go is the narration of the two cases; every reader of this book knows them.** And
§6.3.7's paperclip maximizer does not earn its keep: conceded in the same breath
as *not a forecast*, then used for a point §6.3.1 has already made better three
times over with real deployed systems. **Cut it and let the section open on the
three pressures.**

§6.3.7 is **§6.3.5** after P64 and P66; the finding is in pre-P64 numbering, as
the last three have been. `renumber-map_2026-08-31d.tsv` and `_f` translate.

## §5.3.1 — the narration, three sentences to two

> ~~Consider the trolley problem in its two classic forms. A runaway trolley will
> kill five people unless diverted onto a side track, where it will kill one;
> most people say divert it. Now stop the same trolley by pushing a stranger off
> a footbridge into its path — same arithmetic, five saved for one — and most
> people refuse.~~
>
> **The two classic forms of the trolley problem run the same arithmetic, five
> saved for one, and get opposite answers. Most people will divert the trolley;
> most will not push the stranger off the footbridge.**

57 words to 35. **The arithmetic is kept and the staging is dropped** — no side
track, no runaway, no pushing into its path — because the sentences downstream
need *the footbridge case* and *the impersonal switch case* to have referents,
and a reader who knows the cases supplies the rest.

**One correction to the finding's description.** The narration was **three
sentences inside one paragraph**, not two paragraphs. The paragraph it sits in
runs 200 words and carries Greene's imaging result and the ventromedial-lesion
evidence as well, both of which the finding keeps and both of which are
untouched here, citations included. §5.3.1 goes **586 → 562 words**.

The design argument the finding says earns its keep is not touched by a word.

## §6.3.5 — the paperclip paragraph, and the four things it was the only carrier of

The paragraph is gone. **None of what follows is named in the instruction, and
all of it had to go or move with it.**

1. **`bostrom2003ethical`** — cited only there. Moved to
   `unused_bibliography.bib`.
2. **`orseau2016safely`** — cited only there, and **the book's only citation of
   interruptibility research**. Moved with it.
3. **The glossary's *Paperclip maximizer* entry**, whose only locator was
   §6.3.5. **Cut.** After this pass the string *paperclip* appears **nowhere in
   the manuscript**, so the entry defined a term the book does not use.
4. **The glossary's *Interruptibility* entry** loses its §6.3.5 locator and keeps
   §6.3, whose opener defines the property in almost the same words — *a
   mechanism that lets a person halt a system without the system resisting or
   routing around the halt*.

**The glossary call is D-112's and not D-145's**, and the two are worth holding
side by side. D-145 repointed the explainability entry because its claim lived in
two other sections. D-112 cut the AlphaGo Zero entry because its claim lived
nowhere. Here **the claim survives and the term does not** — §6.3.1 makes the
separability point in the book's own terms, which is the finding's whole
argument — and a glossary entry is for a term. So it goes.

**The pointer at §3.5 went with the paragraph.** §3.5 has six other inbound
references, so nothing is stranded, and §6.3's opener already routes the
interruptibility question to chapter 3 on its own. Chapter 6 keeps the link at
parent level.

### The section's opening frame was kept

*“Open on the three pressures”* is what the section now does — they are its first
substantive content. **The two-sentence frame above them stayed**, because the
pressures paragraph begins *“Three pressures make the long-run version harder
than the near-term one,”* and *the near-term one* has no referent without it.
§6.3.5 goes **317 → 214 words**.

## What was lost, named rather than repaired

- **Interruptibility as the concrete research response to long-run
  misalignment**, and with it **the book's only citation of a paper on the
  technique.** §6.3's opener still defines the property, §3.5 still argues about
  what it costs, and chapter 3's whole *haltable at no cost* argument is
  untouched — **but the book now discusses interruptibility in three places and
  cites no research on it anywhere.** That is a bibliographic loss rather than an
  argumentative one, and it is the largest thing this pass removes.
- **The paperclip maximizer as a term the reader can look up.** The claim it
  carried — competence and good intentions are separable — survives in §6.3.1's
  *“the failure is usually in the objective rather than the optimization, which
  means better engineering makes it arrive faster.”*
- **The trolley cases as narrated scenes.** Kept as arithmetic and named cases.

## Figures

**94,423 words**, down **175** on P71's 94,598 — §5.3.1 586 → **562**, §6.3.5 317
→ **214**, the glossary 3,273 → **3,225**. **136 sections and 188 pages, both
unchanged.** All `\ref{sec:}` **551 → 548**: the cut paragraph's pointer at §3.5,
and the two glossary locators at §6.3.5. Glossary locators **116 → 114**, the figure having stood at 116 since P66.
`refs.bib` **304 → 302**, `unused_bibliography.bib` **33 → 35**, with no cited key
missing and no entry left uncited. 0 undefined references, 0 undefined citations,
`check_all.sh` green. Printed page 81 rasterized and read: §6.3.5 running frame →
three pressures → catastrophic scenarios.

## Not done

- **The *Interruptibility* glossary entry was not repointed at §3.5.** It now has
  one locator where it had two. §3.5, *What Can Be Switched Off Cannot Hold a
  Line*, is where the property is argued about rather than defined, so adding it
  is defensible and is an addition the instruction does not ask for. **One word
  from the author adds it.**
- **No replacement citation was found for interruptibility research.** The
  paragraph's citation was moved because its paragraph went, not because the
  literature was re-searched; whether a better citation exists for the technique
  was not checked.
- **The committed proof pair is stale after P66 through P72**, seven passes, and
  its page figure says 190 against a book at 188.
- **Two ledger rows tagged D-153**, plus the glossary's, all `drafted`. **2
  `accepted`, 134 `drafted`**, unchanged.
