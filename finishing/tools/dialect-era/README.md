# Dialect-era tools (retired 2026-08-25, D-065)

These read or wrote the manuscript dialect — `<<quote>>`, `<<list>>`, `<<box>>`,
`<<h>>`, `[[cite:ID]]` — and the joined `parseable_text_v4.txt`. The manuscript
is LaTeX now: `manuscript/sections/**/*.tex`, pulled in by `manuscript/book.tex`.
Nothing here runs against the current tree, and none of it is wired into
`check_all.sh`.

They are kept, rather than deleted, because they are how the dialect era's
artifacts were produced, and those artifacts are still in the repository:
`parseable_text_v3b_2024-07-07.txt` and `parseable_text_v4.txt` are frozen
provenance, and `finishing/tools/check_frozen.py` guards both.

- `render.py` — dialect → HTML, the front end of the HTML → LibreOffice → ODT
  → PDF path. Replaced by LaTeX. Three fidelity gaps found in it during the
  migration are recorded in D-065; all three were forced by what survived the
  ODT importer, and all three are fixed by the LaTeX target.
- `join_manuscript.py` — concatenated the sections into `parseable_text_v4.txt`.
  `book.tex` now pulls the sections in directly, so there is no join step.
- `split_manuscript.py` — the original 2024 split of v3b into one file per
  section. Historical: it is what created the layout the book still uses.
- `apply_p1.py` — a one-shot P1 edit applier, dialect-specific.
- `render_tex.py` — dialect → LaTeX. This is the converter the migration ran;
  it has nothing left to convert. `migrate_to_tex.py` (also here) drove it.
- `check_tex_roundtrip.py` — inverted `render_tex.py` and diffed the result
  against the dialect sources, proving the migration lost no prose (1342 lines,
  exact). One-shot: the `.txt` sources it compares against are gone.
