# Translated editions

The English book (`manuscript/sections/`) is the source. Each translated edition is a directory `manuscript/<code>/` holding `book.tex` (its master, hand-edited), `translations.tsv` (which English each translated section was made from), `glossary.tsv` (the book's terms of art in that language), `sections/` (the translated section files at the English paths), and two generated files, `sections.tex` and `status.tex`. `manuscript/uk/README.md` describes the files, the record and the commands in full; they work the same way in every edition.

Every edition shares the English preamble, switched by `\booklanguage`, `\booklocale` and `\bookmainfont`, and two shared files: `edition-common.tex` (English captions pointed at the edition's, the bibliography's English notes left out of the footnotes, the status footer kept English, and the heads for editions without a babel locale) and `edition-body.tex` (the document). An untranslated or stale section prints in English, so every edition always builds whole.

Build one with `finishing/tools/build_edition.sh <code>`. "Proofs please plus Ukrainian, French" builds the named ones into `finishing/reports/edition-proof-<code>_<date>.pdf`; "proofs please all languages" builds every one (D-810).

| Code | Language | Script and direction | Typesetting | Bibliography strings |
|---|---|---|---|---|
| `uk` | Ukrainian | Cyrillic | babel `ukrainian`; P052 (URW Palladio with Cyrillic) | biblatex's |
| `es` | Spanish | Latin | babel `spanish`; Pagella | biblatex's |
| `pt-br` | Portuguese (Brazil) | Latin | babel `brazilian`; Pagella | biblatex's |
| `ca` | Catalan | Latin | babel `catalan`; Pagella | biblatex's |
| `fr` | French | Latin | babel `french`; Pagella | biblatex's |
| `de` | German | Latin | babel `german`; Pagella | biblatex's |
| `sw` | Swahili | Latin | babel `swahili`; Pagella | the edition's (`sw/biblatex-sw.lbx`) |
| `hi` | Hindi | Devanagari | babel `hindi`; Noto Serif Devanagari through HarfBuzz, Latin by fallback to Pagella | the edition's |
| `he` | Hebrew | Hebrew, right to left | babel `hebrew` with `bidi=basic`; Noto Serif Hebrew, Latin by fallback | the edition's |
| `ar` | Arabic (Modern Standard) | Arabic, right to left | babel `arabic` with `bidi=basic`; Noto Naskh Arabic through HarfBuzz, Latin by fallback | the edition's |
| `fa` | Persian (Iran) | Arabic script, right to left | babel `persian` with `bidi=basic`; Noto Naskh Arabic through HarfBuzz, Latin by fallback | the edition's |
| `zh-tw` | Chinese (Taiwan, Traditional) | Han | luatexja, Noto Serif CJK TC, JFM zh_TW (centred punctuation); no babel locale | the edition's |
| `zh-cn` | Chinese (mainland, Simplified) | Han | luatexja, Noto Serif CJK SC, JFM zh_CN; no babel locale | the edition's |
| `ja` | Japanese | Han and kana | luatexja, Noto Serif CJK JP, JFM ujis; no babel locale | the edition's |
| `ko` | Korean | Hangul | luatexja, Noto Serif CJK KR, JFM ujis; no babel locale (luatexko needs kotex-utf, not installed) | the edition's |

All the non-Latin faces are system fonts here, not part of TeX Live. None of the editions has been tried in Overleaf.

**What every edition still needs from a person.** A native reader for every translated section, every glossary term, the title, the title-page notice and, where the edition writes its own, the bibliography strings. The title is an open question in every language (D-810): find the act the English title performs in that culture, or keep the English as a known unknown. Until a reviewer confirms them, every title, term and section is a language model's draft, and each edition's title page says so.

**Known typesetting gaps.** Korean is set with luatexja, which may break a line between any two syllables. Japanese's katakana title breaks across lines on the title page. luatexja adds a small space between CJK and Latin text, which Taiwanese and mainland publishers treat differently. In the Hebrew, Arabic, Persian and Hindi editions the script's face has no Latin letters, digits or ASCII hyphen: a luaotfload fallback supplies missing glyphs from Pagella, and babel switches Latin runs and the hyphen (which the fallback can't reach, since TeX treats an explicit hyphen as a hyphenation point) to English and Pagella.
