# P75 — §10.4's roll cut on its own diagnosis, the three-jurisdiction comparison to one paragraph

**The author's finding.** §10.4's four-jurisdiction comparison is competent and
**the fastest-dating pages in the manuscript**. The text already knows: it says
the roll of voluntary bodies *“is longer than it is deep”* and that *“reciting it
is the wrong instrument for the point.”* **Convert that self-awareness into
cuts.** The EU/US/UK comparison can be one paragraph; what earns its length is
the China contrast, because that one makes a structural claim — a law aimed at a
private product and a law aimed at a communications channel are different
instruments, and comparing them on a more/less axis misses it — rather than
reporting a state of affairs.

**Both halves hold, and the section is at the current numbering**, unlike the
last four findings. §10.4 goes **1,597 → 1,350 words**.

## The roll's own justification was false

The sentence introducing the roll reads: *“Three are worth naming **because the
rest of this book uses them**.”* Checked against the manuscript:

| | cited elsewhere? |
|---|---|
| `oecd2019recommendation` — the OECD Recommendation | **No. §10.4 only.** |
| `aihleg2019ethics` — the HLEG *Ethics Guidelines* | **No. §10.4 only.** |
| `partnershiponai2016` — the Partnership on AI | Yes — §9.1.2 and §9.3.5 |

**One of the three, not three.** The justification for reciting the roll was
wrong about two-thirds of it, which is a sharper argument for the cut than the
finding makes, and it is the kind of claim no tool in the suite checks: the
citations all resolved, and what was false was a sentence about them.

### What survives, and why one entry stayed

Bletchley and the AI Safety Institutes network **had to stay**: the next
paragraph is the worked case D-101 built to replace the roll — Bletchley → Seoul
→ Paris, and the closing statement the United States and the United Kingdom did
not sign — and it opens *“The summit series that produced the Bletchley
Declaration continued past it.”* Cutting the whole roll would have stranded that
antecedent and orphaned two more citations.

So the paragraph now names one entry and says why:

> Everything else in this space is voluntary, and the roll is longer than it is
> deep. Reciting it is the wrong instrument for the point… **One entry is worth
> naming, and only because of what happened to it**: the Bletchley Declaration…

~185 → ~90 words.

## The EU/US/UK comparison, four paragraphs to one

Merged: the EU paragraph, the US paragraph, the UK paragraph, and the
*which-structural-bet-is-safer* paragraph that followed the China contrast. **All
four citations kept** — `eu2024aiact`, `eu2024aiactenforcement`, `nist2023airmf`,
`dsit2023proinnovation` — along with the EU's structural principle (what a system
might do, not the technology it runs on, decides the scrutiny), the American
wager (naming AI specifically risks regulating the label rather than the
conduct), and the failure modes running in both directions.

**~485 → ~240 words.**

**The China paragraph is untouched, to the word**, and so is the closing
paragraph, which makes the same structural move a second time: *“a law a
government enforces against itself is a different instrument from one that
constrains what it does with systems it controls directly,”* and the recurring
error of treating *“AI is regulated here”* as an answer to *“is AI used against
this country's own population here.”*

## Two citations orphaned, and the check that cleared them

`oecd2019recommendation` and `aihleg2019ethics` moved to
`unused_bibliography.bib`; `refs.bib` **302 → 300**, unused **35 → 37**.

**This looked like P65's class and is not.** §12.1.2 names both — *“The OECD's
recommendation. The European Commission's expert-group guidelines”* — in a roll
of eight voluntary bodies, so cutting §10.4's citations leaves those names
unsourced. But **§12.1.2 carries no citations at all**, by design: its roll counts
bodies rather than sourcing them, which is the point it is making, and it already
names UNESCO and the Hiroshima process with no citation anywhere in the book. Two
more uncited names among eight is consistent with how that passage works, not a
new hole.

**Recorded rather than repaired**: after this pass the book names the OECD
Recommendation and the HLEG *Ethics Guidelines* in §12.1.2 and cites neither
anywhere.

## What was lost, named rather than repaired

- **The OECD Recommendation as the first intergovernmental AI standard and the
  basis for the G20's own.** Nowhere else in the book.
- **That the HLEG's seven requirements shaped the structure of the EU AI Act.**
  Nowhere else in the book, and it is the only account the manuscript had of
  where the Act's structure came from.
- **The Partnership on AI's mention here.** §9.1.2 calls it *the book's standing
  example of cross-sector voluntary coordination* and treats it at length, so
  this was the third telling of three.
- **The EU's GDPR-extraterritoriality parallel**, the UK's *wager* sentence, and
  the sentence pointing at Article 5's prohibitions as covered earlier. The
  extraterritorial reach itself is kept as a clause.

## Figures

**93,796 words**, down **247** on P74's 94,043, all of it §10.4. **136
sections**, unchanged; nothing renumbered. All `\ref{sec:}` **unchanged at 547** —
the compressed paragraph kept §6.4.1's and §6.4.3's pointers in the run-in above
it, and the merge removed none. Glossary locators **unchanged at 114**.
`refs.bib` **302 → 300**, `unused_bibliography.bib` **35 → 37**, with no cited key
missing and no entry left uncited. `check_all.sh` green.

## Not done

- **The Council of Europe paragraph was not touched**, and it is the
  fastest-dating prose in the section: *“at this writing it has not [entered into
  force], although the European Union deposited its ratification in May 2026.”*
  It is also the section's opening claim — the one binding instrument — so it
  cannot go without the opener going. **Named for a ruling.**
- **The *“None of these bodies can compel”* paragraph was not touched.** It is
  180 words of argument rather than roll, and the finding does not name it,
  though its first sentence restates the section's first sentence.
- **The run-in's two-sentence pointer opener was not touched** — *“Section 6.4.1
  names six documented forms… section 6.4.3 the policy levers”* — which is the
  shape P66 and P74 cut elsewhere. It frames the China contrast as well as the
  three-jurisdiction comparison, and the finding did not name it.
- **The proof pair is stale after P74 and again after this pass.** **[Rebuilt at P75: the pair now stands at 187 pages, covering P74 and P75 together. The date had not rolled over, so it was rebuilt in place; the README is unchanged, its links not having moved and its page figure having already been 187.]**
- **One ledger row tagged D-156**, §10.4, `drafted` already. §12.1.2 was read and
  not edited, so it carries no tag. **2 `accepted`, 134 `drafted`**, unchanged.
