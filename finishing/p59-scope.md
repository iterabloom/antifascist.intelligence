# P59 — chapter 0 removed, the method note moved to an appendix

**The author's instruction:** remove the "On Method" chapter 0 altogether; there
can be an appendix with an explanation of the writing process and a link to the
GitHub repository instead.

**What the book had.** Chapter 0 was 398 words of front matter, written at P5
under D-008 and given its vendor disclosure at P7 under D-028. It stood between
the table of contents and chapter 1, so every reader met it before the argument.

**What the book has now.** The same text, 397 words, as an unnumbered
`Appendix: On Method` at the back, carrying the repository's address. The file
was moved with `git mv` rather than deleted and rewritten, so its history
follows it.

## Where it sits, and why that was a choice

The appendix is **last**: chapter 12, then the glossary, then the appendix, then
the References. Conventional back-matter order — Chicago's — puts an appendix
*before* a glossary, and that order was not taken. Two reasons, both cost rather
than principle:

- The glossary is numbered 13 in `ORDER.tsv`, `outline.tsv`, `ledger.tsv` and
  in every historical reference across `STATE.md` and `DECISIONS.md`. Putting the
  appendix in front of it means renumbering the glossary to 14 and adding a
  `renumber-map` file so the record stays readable. That is real churn for an
  ordering few readers would notice.
- Last also reads: the appendix is the book's account of its own provenance and
  the References are the rest of that account, so the two sit together.

**This is cheap to reverse** if the author prefers the conventional order. It
costs the glossary a renumber and nothing else — nothing in the manuscript
references `sec:13`.

## The prose

Three changes to the moved text, and nothing else:

1. The heading and its label: `On Method` → `Appendix: On Method`, `sec:0` →
   `sec:14`.
2. The repository now has an address. *"…all in the repository this book comes
   from, dated and unedited after the fact"* gains
   `: \url{https://github.com/iterabloom/ethical.superintelligence}.`
3. *"The argument in the chapters that follow is mine"* → *"The argument in this
   book is mine."* The note no longer stands in front of them.

Its two cross-references were checked rather than assumed, both being older than
P57's renumbering of chapter 10. `chapter~\ref{sec:6}` reaches section 6.4.1's
Maven Smart System box, and `section~\ref{sec:10.3}` reaches the paragraph that
names the model vendor as the fourth party neither command responsibility nor
product liability reaches. Both are right.

## The three sites the move made wrong

Two sections named the note by its position, and a third collided with the word.

- **Section 7.4** opened *"The note on method that opens this book discloses that
  this text was written with a model made by a company the book criticizes. This
  section is the argument that disclosure was preparing the ground for."* Both
  sentences depend on the reader having already read it. It now **states** the
  disclosure instead of referring back to one: *"This text was written with a
  model made by a company the book criticizes, and the appendix on method sets
  out how. This section is what that disclosure is for."*
- **Section 6.1.1** had *"disclosed in the note on method that opens this book"*
  → *"as the appendix on method records"*, which also drops a repeated *this
  book*.
- **Section 3** used the word metaphorically — tamper-resistance research moved
  *"from an appendix topic to the center"* — which now competes with a literal
  appendix. One word: *"from a peripheral topic to the center."*

Neither of the first two carries a `\ref`, so no tool in the suite would have
caught them; they were found by searching the prose for the phrase.

## Q-055 taken by default, because this pass would otherwise have spread it

`\chapter*` sets no running mark, so the head left standing by chapter 12 ran
over the whole glossary — five pages reading **"CHAPTER 12. CONCLUSION AND
OUTLOOK"**. Q-055's default (a) was to fix it in `preamble.tex` at the next
preamble change. A second starred back-matter chapter would have inherited the
same wrong head, so the default was taken here rather than deferred:
`\backmattermark` in `preamble.tex`, called once in each of the two files. The
glossary page now reads **GLOSSARY**, confirmed in a rasterized page and not only
in the log.

## Machinery

- `gen_book.py` emitted `\setcounter{chapter}{0}` before chapter 1 because an
  unnumbered chapter 0 came first. Chapter 0 is gone, so the special case and its
  comment are gone. **Chapter 1 was verified to still print as 1** in the built
  PDF rather than assumed.
- `common.py` was taught two macros. `section_stats.py` warned that
  `backmattermark` and `url` were unknown and its own warning says not to trust
  the count until they are: an unknown command is dropped but its braced argument
  is not, so the running-head titles were being counted as prose.
  `backmattermark` joins `TEX_DROP_WHOLE`; `url` joins `TEX_KEEP_ARG`, counting
  an address as the one token it prints, which is the convention `\ref` already
  gets.
- `ORDER.tsv`, `outline.tsv` and `ledger.tsv` lose row 0 and gain row 14; the
  ledger row is chapter 0's own, renumbered, so its history from P5 forward is
  not lost. `sections.tex` and `table-of-contents.txt` regenerated;
  `refresh_order_shas.py` run.

## Figures

**146 sections** — one removed, one added. **96,829 words**, and the arithmetic
is worth stating because two things moved it. The manuscript edits took 96,840 to
**96,833**: one word out of the moved note, and the rest out of the three repairs
above. Teaching `common.py` took it to **96,829**, removing 4 words that were
never prose — the two `\backmattermark` arguments, which the untaught tool had
been counting. Body `\ref{sec:}` is **418**, unchanged, the appendix carrying
the two references chapter 0 carried. `refs.bib` unchanged at 309. **196 pages**,
unchanged. 0 undefined references, 0 undefined citations, `check_all.sh` green,
both builds clean.

## What this pass does not do

- **The committed proof pair is stale.** `finishing/reports/whole-book-proof_2026-08-31.{pdf,html}`
  and the README's two links point at a book that still has a chapter 0. **[Reconciled at P76: the pair has been rebuilt since, most recently at P75, and stands at 187 pages. P63's own reconciliation commit did not reach the scope files, so this line and the four like it in `p59`–`p62` went uncorrected until now.]**
- **The front matter no longer discloses anything.** Title page, table of
  contents, chapter 1. The persona device, the vendor, and the repository are
  disclosed at the back and in the README, and a reader who does not turn to the
  back does not meet them. That is what the instruction asks for, and it is
  recorded here because D-028 put the vendor disclosure in chapter 0 on purpose.
- **The ledger row is `drafted`.** The appendix has not been read in position by
  the author.
