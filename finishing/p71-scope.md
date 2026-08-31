# P71 — a verbatim duplicate, a broken reference, and two epigraphs

**Two author instructions, one pass**, the second arriving while the first was
being carried out.

**Part one.** A verbatim duplicate sentence — *“Stated that way the dividend is a
property a state either has or lacks, which it is not”* — identical in §10.2 and
§10.6; and §8.3.3's *“Section~\ref{sec:11} carries the worked instance from
2025,”* which should be **chapter** 11, the CFPB material being in the chapter
preamble rather than a numbered section.

**Part two.** Cut two epigraphs: Lady Gaga & Bradley Cooper at §5.2.1, and
Westworld at §2.3.

**All four confirmed before acting.**

## The duplicate: cut from §10.6, not §10.2

The finding names both sites and does not say which to cut. **§10.6 was the one
that could lose it, because §10.6 says the same thing twice in consecutive
sentences:**

> Stated that way the dividend is a property a state either has or lacks, which
> it is not. **Having those institutions is necessary and it is not sufficient**,
> and the ways it fails to be sufficient are separable.

So cutting there removes the cross-section duplicate **and** an intra-section one,
and the paragraph is tighter for it.

**§10.2's is the instance that earns its place.** It raises the objection and
hands it forward in the next sentence — *“Section~\ref{sec:10.6} works out three
ways in which having the institutions fails to be sufficient.”* Cutting §10.2's
instead would have left that forward pointer announcing an objection §10.2 no
longer makes.

§10.6 goes **733 → 715 words**, which is the whole of this pass's word change.

## The broken reference: fixed, and the class swept

`sec:11` is a chapter label, and the worked instance — *a bureau whose funding
stream a court had upheld, shut from inside by an at-will director who declined
to request the money* — is in `manuscript/sections/ch11/11.tex`, the chapter
preamble. **Verified by reading the file, not inferred.** `Section~\ref{sec:11}`
became `Chapter~\ref{sec:11}`.

**Swept for the whole class in both directions.** `Section~\ref` pointing at a
bare chapter label: **one instance, the one reported.** `chapter~\ref` pointing at
a numbered section: **none.** This was a singleton rather than the visible corner
of a pattern.

**No tool in the suite can find this.** `check_xrefs.py` confirms that every
reference resolves and is prefixed; this one resolved and was prefixed. What was
wrong was the English word in front of it, which no invariant reads.

## The two epigraphs

Both cut whole — the `verse` block and its `flushright` credit.

**The book had four epigraphs and now has two.** The two cut were **the only
section-level epigraphs in the book**; the survivors are both at chapter level —
the Introduction's Run the Jewels lines and chapter 6's Brigadier General Y.S.,
the design document that chapter's opener then argues with. After this pass the
device is used only where a chapter opens.

### Cutting them changed the word count by zero

`section_stats.py` counts epigraph text in its own `epigraphs` column and not as
prose. §2.3 stands at **52 words** before and after; §5.2.1 at **1,058** before
and after. The epigraph count moves **4 → 2**. **Do not read this pass's 18-word
fall as evidence the epigraphs are still there** — the whole of it is the
duplicate sentence.

### One consequence, named rather than repaired

§4.1.2 alludes to Westworld — a system should treat what it has learned to
discount as an open question rather than as *“that which, as Westworld's Hosts
often remarked, ‘doesn't look like anything to me’.”* **The §2.3 epigraph was the
book's only source credit for the show**, and it carried the full one: episode,
season, writers, director, distributor, year.

The allusion attributes in text — it names the show and the characters — and
involves no `\autocite`, so `refs.bib` is untouched and no invariant fires. But a
quoted line of dialogue now has no bibliographic source anywhere in the book.
**This is P65's class in miniature**, a cut severing a quotation from its only
credit, and it is reported rather than fixed because fixing it means adding
something to a section the instruction did not name.

## Figures

**94,598 words**, down **18** on P70's 94,616, all of it §10.6's duplicate
sentence. **136 sections and 188 pages, both unchanged.** Epigraphs **4 → 2**.
All `\ref{sec:}` **unchanged at 551** — the reference was rewritten in its prose
word, not removed — with the glossary unchanged at 116 and `refs.bib` unchanged
at **304**. 0 undefined references, 0 undefined citations, `check_all.sh` green.

## Not done

- **§10.2's sentence was kept deliberately and is now the book's only statement
  of it.** If the intent was to cut §10.2's rather than §10.6's, the swap is one
  edit and the forward pointer needs rewording with it.
- **No search was made for other verbatim duplicate sentences.** This pass fixed
  the one reported. A whole-book duplicate-sentence sweep is not something any
  tool in `finishing/tools` currently does, and building one was not in scope
  here.
- **The committed proof pair is stale after P66 through P71**, six passes, and
  its page figure says 190 against a book at 188.
- **Four ledger rows tagged D-152**, all `drafted`. **2 `accepted`, 134
  `drafted`**, unchanged.
