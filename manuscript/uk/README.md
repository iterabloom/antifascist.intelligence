# The Ukrainian edition

A Ukrainian translation of the book, kept in step with the English, which is
the source. Translation goes one chapter at a time. A chapter is translated
once the author calls its English settled.

- `sections/chNN/*.tex`: one Ukrainian file per English section file, at the
  same path under `uk/`. Each keeps the English file's heading command and
  `\label` line unchanged, so every cross-reference resolves. The label is
  checked, and the heading's title is translated.
- `translations.tsv`: one row per translated section. It records the sha256
  of the English file the translation was made from (or last brought up to
  date against), its status (`draft` or `reviewed`), who did it, and when.
- `glossary.tsv`: the book's terms of art and the Ukrainian chosen for each,
  `proposed` until the author approves it. Draft against approved terms only.
- `book.tex`: the edition's master. `sections.tex` is generated; don't edit it.

Commands:

- `finishing/tools/uk_edition.py --record PATH --status draft --by WHO`, after
  writing or updating the translation of English section `PATH`.
- `finishing/tools/uk_edition.py --stale` lists translations whose English has
  changed since they were made. `check_all.sh` runs `--check`, which lists the
  stale ones too but does not fail on them.
- `finishing/tools/build_tex_uk.sh` builds `/tmp/es-build-uk/book.pdf`. Any
  section not yet translated is set in English in its place.

Conventions:

- Quotation marks «…», with „…“ inside. Dashes are the em dash, tied to the
  word before (`ціль~— чоловік`) so no line begins with one.
- People's names are transliterated into Cyrillic (Арендт, Мілграм, Ернандес
  Ромеро). Companies, products and publications keep their Latin names, as
  Ukrainian press usage does (Anthropic, Claude, Maven Smart System, Palantir,
  +972 Magazine). Numbers group thousands with a thin space (`37\,000`). Locators
  are Ukrainian (`п.~92`, `пп.~92–93`).
- Citations stay as they are (`\autocite{key}`). Bibliography entries stay in
  their original languages. biblatex supplies the Ukrainian strings.
- Quotations from English sources are translated in the text, with no
  reference to an official Ukrainian version unless one exists and is cited.

Gaps, as of 2026-10-16:

- No section is translated. Every glossary term is `proposed`. No native
  reader has reviewed anything, and a reviewer has not been found.
- The edition's face is P052, a system font (urw-base35), not part of TeX Live.
  It has no small caps, so the running heads print upright. Overleaf has not
  been tried.
- The bibliography's `note` fields are English and are left out of this
  edition's footnotes until they are translated. (The references carry no
  notes in either edition.)
- The names guard, the typography check and the Markdown render read only the
  English sections.
