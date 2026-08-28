#!/usr/bin/env python3
r"""Typographic invariants for the manuscript and the bibliography.

Two characters that LaTeX sets as something other than what they look like,
and that no other check would catch, because both compile without a warning
and both produce a page that is merely wrong rather than broken.

  1. The straight double quote. LuaLaTeX sets `"` as a RIGHT quotation mark
     wherever it stands, so a manuscript written with straight quotes opens
     every quotation with the mark that should close it. The book did this
     230 times across 44 files until D-082 swept them; write `“` and `”`.
  2. The ASCII dash runs `--` and `---`. The manuscript's dashes are the
     characters themselves, 785 em and 1 en, and mixing the two notations
     sets the same dash two different widths on the same page.

`refs.bib` is checked too, because its `title` and `note` fields print in the
References and had 142 straight quotes of their own. The one `\"` in the file is
a diaeresis on a name, not a quotation mark, and is allowed for.

Straight apostrophes are correct and are NOT checked: LaTeX sets `'` as `’`,
which is the right glyph, and the manuscript's 894 of them print properly.
"""
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

RULES = [
    ('"',   'straight double quote -- LaTeX sets it as a closing mark; use “ and ”'),
    ('---',  'ASCII em dash -- write the character —'),
    ('--',   'ASCII en dash -- write the character –'),
]

# refs.bib takes the quote rules but not the dash ones: its own convention for
# an em dash inside a note field is ` -- `, which biber passes through to TeX,
# and sweeping that is a separate question from this one.
BIB_RULES = [
    ('"',  'straight double quote -- LaTeX sets it as a closing mark; use “ and ”'),
    ('``', 'TeX quote notation -- write the characters “ and ”'),
    ("''", 'TeX quote notation -- write the characters “ and ”'),
]
ACCENT = '\\"'          # a diaeresis, e.g. Rapha{\\"e}l -- not a quotation mark


def main():
    files = sorted(glob.glob(os.path.join(common.SECTIONS, "ch*", "*.tex")))
    hits = []
    for path in files:
        with open(path, encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                for bad, why in RULES:
                    if bad in line:
                        col = line.index(bad)
                        hits.append((os.path.relpath(path, common.REPO), lineno,
                                     why, line[max(0, col - 40):col + 40].strip()))
                        break   # one report per line is enough to find it
    bib = os.path.join(common.REPO, "finishing", "refs.bib")
    if os.path.exists(bib):
        with open(bib, encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                stripped = line.replace(ACCENT, "")
                for bad, why in BIB_RULES:
                    if bad in stripped:
                        col = stripped.index(bad)
                        hits.append(("finishing/refs.bib", lineno, why,
                                     stripped[max(0, col - 40):col + 40].strip()))
                        break

    print("check_typography: %d sections, and refs.bib" % len(files))
    if hits:
        print("FAIL:")
        for path, lineno, why, ctx in hits:
            print("  %s:%d  %s" % (path, lineno, why))
            print("      ...%s..." % ctx)
        sys.exit(1)
    print("  typography OK: no straight quotes, no ASCII dashes, no TeX quote notation")


if __name__ == "__main__":
    main()
