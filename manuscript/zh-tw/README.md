# The Traditional Chinese (Taiwan) edition

Mandarin in Traditional characters with Taiwan's usage, kept in step with the
English, which is the source. It works like every edition. `manuscript/uk/README.md`
describes the files, the record and the commands; replace `uk` with `zh-tw`.

Typesetting:

- Chinese characters are set by luatexja in Noto Serif CJK TC, with the zh_TW
  font metric (from chinese-jfm), which centres the full-width comma and stop
  as Taiwan does. Latin text keeps the English book's face. Both CJK faces
  (Noto Serif and Sans CJK TC) are system fonts here, not part of TeX Live.
- biblatex has no Chinese strings. The edition's own are in
  `biblatex-zh-tw.lbx`, as drafts. Dates print as 2025年5月8日.
- luatexja puts a small space between Chinese and Latin letters or digits
  ("2025 年", "Maven 系統"). Whether to keep it is a reviewer's call.

Conventions:

- Full-width punctuation. Quotation marks 「…」, with 『…』 inside. Book
  titles 《…》, article and chapter titles 〈…〉. The dash is ——, the
  ellipsis …….
- People's names: the established Chinese form where one exists (鄂蘭 for
  Arendt is Taiwan's, where the mainland writes 阿伦特; check each one), otherwise the Latin
  name. Companies, products and publications keep their Latin names.
- Citations stay as they are (`\autocite{key}`). Bibliography entries stay in
  their original languages.

Gaps, as of 2026-10-16:

- No section is translated. All 46 glossary terms are `proposed`. No native
  reader has reviewed anything, including the title, the notice and the
  bibliography strings.
- The bibliography strings cover what the book's citation style prints. Any
  other string falls back to English.
- The names guard, the typography check and the Markdown render read only the
  English sections.
