# P160 — the running head carries the section, and the contents stop at it

The author's reading was that the table of contents goes one level too deep, and
his instruction was to do both halves of the recommended option: **give the running
head the section, then cut the contents to depth 1.** The two are one change set —
the depth cut is the second half of the first option — and both are in
`preamble.tex`. **No prose changed.**

## What the depth was buying, and why the head had to go first

At `tocdepth` 2 the contents ran pages 2 through 5 of a 196-page book: three full
pages and an 11-line stub, and the **64 subsections were most of it**.

**79 of the 228 cross-references point at an x.y.z — 35 percent.** What made that
decisive is the running head: `book.tex` declares `oneside`, where `book.cls` drops
`\sectionmark` altogether and puts the chapter mark on every page. **All 196 pages
read `CHAPTER n. TITLE`**, checked on pages 57 through 60, so the contents were the
only lookup path for a third of the book's own pointers. Cutting the depth alone
would have left those 79 with nothing to consult.

## The head

`fancyhdr`, and the head carries the deepest heading in force — subsection where
there is one, section otherwise, chapter before the first section. **`\subsectionmark`
had to be defined**: `\@sect` calls it and the standard page styles `\@gobble` it,
which is why a subsection never reached a head. A chapter's opening page keeps the
folio alone.

**Small caps rather than the class's uppercase.** An x.y.z title set in full capitals
is long and hard to read — `4.1.2. Biologically-Inspired AI: Gleanings from
Neuroscience and Cognitive Psychology` is 85 characters. `\backmattermark` is
untouched and its own uppercase marks still set as capitals, so the two agree.

Read off the built PDF: p52 `3.10. What This Leaves Standing`, p53 blank on the
chapter opening, p54 and p55 `4.1.2.`, p56 `4.2.`, p57 `4.2.2.` The glossary head
still reads `GLOSSARY` and the references `REFERENCES`, so Q-055's repair survives.

## What it cost and what it saved

**The contents are 2 pages, from 4. The book is 194 pages, from 196**, and the
Foreword moved from page 6 to page 4. **Overfull hboxes fell from 18 to 6**, the old
contents having been where most of them were.

## The HTML, which is the part worth a ruling

`tocdepth` governs both builds, and **the HTML page has no page cost to recover.**
Measured rather than assumed: its contents block held 15 chapter, 55 section and
**64 subsection entries, and the 64 are now gone** — 134 entries to 70. Total
internal links 680 to 616, a loss of exactly 64, so nothing but the contents
changed.

**Q-114** puts it. Its default accepts the loss on one setting for one source; (b)
is a `\ifdefined\HCode` conditional, which is the standard tex4ht test and **has not
been verified in this build**; (c) restores depth 2 everywhere and takes the four
print pages back.

## One measurement that was wrong before it was right

The first HTML comparison reported **0 internal anchors in both files** and was read
as the page having no contents at all. **The markup uses single-quoted attributes**
and the grep used double quotes. The corrected count is above. Nothing was written
to the record from the wrong figure.

## Figures

133 sections, **0 changed** — no manuscript file was touched. 99,458 words
unchanged. **196 → 194 pages.** 228 cross-references and 324 bibliography entries
unchanged. Contents 4 pages → 2; HTML contents 134 entries → 70. Overfull hboxes 18
→ 6. 0 undefined references and citations. Suite green.

**The committed proof pair is one pass stale** and shows the old head and the old
contents.
