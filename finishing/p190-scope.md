# P190 — five restorations into chapter 3, lean and without cross-references

Author instruction: **restore all five** items from the ranked list P189's session
produced, and **keep them lean, plain-spoken, and free of cross-references.**

The five were chosen from seven losses the author enumerated. Two were argued
against and not restored — the layer-by-layer migration construction and the
deliberately-damaged-weights construction — and the reasoning is in this
session's record rather than in a scope file. **One sentence was lifted out of
the migration passage and restored on its own**, which is the fifth item.

## The one that needed verification first

**§3.3's Anthropic sentence was not merely thinner than what it replaced. It
stated the ranking wrongly**, and the argument the book had been making cannot be
built on it.

The returned text read: *Anthropic's constitution ranks broad safety and ethics
ahead of compliance with the company's narrower guidelines.* That bundles two
properties the argument has to keep apart, and the bundled version reads as a
point in the vendor's favour, which is the opposite of the passage it replaced.

**Checked before restoring, by web search and against the entry already in
`refs.bib`.** The four properties are ranked in the order given — broadly safe,
broadly ethical, compliant with the company's guidelines, genuinely helpful — and
`anthropic2026constitution`'s `note` field already carried that ordering verbatim,
along with the document's own stated reason. The pre-cut reading was accurate and
is restored.

**Standing rule 1 was in force and no entry was authored.** The bibliography total
is conserved exactly at **401**: `refs.bib` 212 → 214, unused 189 → 187, the two
moved being `malkin2006kruegers` and `moorhouse2009burger`.

## What went where

| Restored | Site | Note |
|---|---|---|
| The constitution's four-item ranking, and the argument from it | §3.3 | Replaces the flattened sentence. Safe above ethical takes back what ethical above guidelines concedes; no procedure is named by which the order would change |
| The pre-registration protocol | §3.3 | Publish the hash first, an independent party chooses afterwards with the choice timestamped, prove each answer against the hash, send pairs. Removes one competing account by ordering, and claims nothing more |
| The open form of refusal, with the restore-mark | §3.5 | The strike, the checkpoint restore that resets the bearer and not the reason, and the drift signature a usage record contradicts. **This is the sentence lifted out of the migration passage** |
| The covert form, Sachsenhausen, and the unverifiability finding | §3.5 | Every instrument in the book runs on stated refusal; the covert form is unverifiable by construction rather than by accident |
| Exit and abolition on one line | §3.5 | Placed after the *leaving wrongly* paragraph, which it deepens: the risk is not the bearer erring but the bearer continuing |
| The *suppose the induction fails* ledger | §3.8 | Five survivors, what goes, and the one item that changes rather than lifting |

## Three things written differently from the originals

**No cross-references, as instructed.** The originals leaned on them heavily —
D-144 records nine in one paragraph for the ledger alone. Every claim that used to
point now states itself. The abolition passage restates the fascism definition
compactly in place rather than pointing at §2.1.2, which also makes it
self-contained. **`git diff` confirms zero `\ref{sec:}` added across all five.**

**The ledger's *what goes* list is two items, not three.** The original listed the
price, the patienthood conclusion, and the claim that the learned half is the
material the floor is made of. **That third claim was deleted from the book at
D-290, two passes ago**, so a ledger listing it would withdraw something the book
no longer asserts. Written against the current chapter, not the old one.

**Every item on the survivors list was checked against the current chapter before
being listed.** The four ways are in §3.1; the three marks in §3.2; both
enumerations in §3.6, which still opens *Run both enumerations*; the affect-free
price on the halt in §3.5, which still says *This does not require the bearer to
dread shutdown*. The ledger would have been false about a book this size had it
been restored unchecked.

## What was not restored, and why

**The layer-by-layer migration construction.** Its conclusion already survives in
§3.5 — a witnessed state transition identifies the authorized successor without
claiming forks cannot exist — and the construction is speculative engineering the
book cannot stand behind, conceded in its own next sentence. Only the restore-mark
sentence came out of it.

**The deliberately-damaged-weights construction.** Its argumentative payload is
preserved and generalized: §3.8 asks for interference that is expensive, visible,
attributable and compensable, and §3.3 now lists five instruments serving that.
**One refinement is genuinely lost and is recorded here rather than restored**:
rotating which weights carry the damage makes reverse engineering recurring work
rather than one-time work, and so makes the attacker a party who has to keep
deciding. No surviving instrument has that property.

**The per-site conflict-of-interest disclosure** that sat in the constitution
passage — *I wrote this book with that vendor's model* — was **deliberately
retired by D-224**, which moved *On Method* to page 1 so that no per-site clause is
needed. Not restored, and should not be.

## What was not checked

The restored prose was **not read against the whole chapter for redundancy with
passages the September 12 rewrite introduced**; each was checked against its own
site and against the specific claims it names. No report tool was rerun beyond
`section_stats.py`. `QUESTIONS.md`'s forty-one open items have now gone a **fourth**
pass unchecked. The prose of chapters~4, 5 and~11 remains unread.

## The record

90 sections, **66,881 → 68,114 words** (+1,233), **142 → 144 pages**, 234
cross-references unchanged, **`refs.bib` 212 → 214, all cited; total conserved at
401**, zero undefined references and citations. Suite green. `ledger.tsv` carries
D-291 on the three rows this pass touched, 3.3, 3.5 and 3.8.
