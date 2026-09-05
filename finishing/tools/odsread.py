"""Minimal read-only .ods reader: stdlib only (odfpy is not importable here).

Returns rows of cell strings for a named or first sheet. Handles
number-columns-repeated and covered cells. Read-only by construction.
"""
import glob
import io
import os
import re
import zipfile
from xml.etree import ElementTree as ET

# Since 2026-09-05 the persona spreadsheets live inside the persona-device
# archive at the repository root, as one binary file that no rendered page
# indexes, rather than as files in the tree. A reader asked for a path that is
# not on disk looks for it there, by its repository-relative path. The bytes
# are read into memory and never written out.
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARCHIVE_GLOB = os.path.join(REPO, "persona-device-files_*.zip")

TABLE = "urn:oasis:names:tc:opendocument:xmlns:table:1.0"
TEXTNS = "urn:oasis:names:tc:opendocument:xmlns:text:1.0"


def _cell_text(cell):
    parts = []
    for p in cell.iter("{%s}p" % TEXTNS):
        parts.append("".join(p.itertext()))
    return "\n".join(parts).strip()


def _archive():
    hits = sorted(glob.glob(ARCHIVE_GLOB))
    return hits[-1] if hits else None


def _open(path):
    """ZipFile for an .ods on disk, or for one inside the persona-device archive."""
    if os.path.exists(path):
        return zipfile.ZipFile(path)
    rel = os.path.relpath(path, REPO) if os.path.isabs(path) else path
    arc = _archive()
    if arc:
        with zipfile.ZipFile(arc) as outer:
            if rel in outer.namelist():
                return zipfile.ZipFile(io.BytesIO(outer.read(rel)))
    raise FileNotFoundError(path)


def exists(path):
    """True if the .ods is on disk or inside the archive."""
    try:
        _open(path).close()
        return True
    except FileNotFoundError:
        return False


def sheets(path):
    """Yield (sheet_name, rows) for every table in the document."""
    with _open(path) as z:
        root = ET.fromstring(z.read("content.xml"))
    for table in root.iter("{%s}table" % TABLE):
        name = table.get("{%s}name" % TABLE, "")
        rows = []
        for row in table.iter("{%s}table-row" % TABLE):
            cells = []
            for cell in row.findall("{%s}table-cell" % TABLE):
                txt = _cell_text(cell)
                rep = int(cell.get("{%s}number-columns-repeated" % TABLE, 1))
                # A huge repeat count is trailing padding; cap it.
                cells.extend([txt] * min(rep, 64))
            while cells and not cells[-1]:
                cells.pop()
            rows.append(cells)
        while rows and not rows[-1]:
            rows.pop()
        yield name, rows


def first_column(path, sheet_index=0):
    """Column A only. Used where later columns hold persona names we must not copy."""
    for i, (_, rows) in enumerate(sheets(path)):
        if i == sheet_index:
            return [(r[0] if r else "") for r in rows]
    return []
