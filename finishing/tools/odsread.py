"""Minimal read-only .ods reader: stdlib only (odfpy is not importable here).

Returns rows of cell strings for a named or first sheet. Handles
number-columns-repeated and covered cells. Read-only by construction.
"""
import re
import zipfile
from xml.etree import ElementTree as ET

TABLE = "urn:oasis:names:tc:opendocument:xmlns:table:1.0"
TEXTNS = "urn:oasis:names:tc:opendocument:xmlns:text:1.0"


def _cell_text(cell):
    parts = []
    for p in cell.iter("{%s}p" % TEXTNS):
        parts.append("".join(p.itertext()))
    return "\n".join(parts).strip()


def sheets(path):
    """Yield (sheet_name, rows) for every table in the document."""
    with zipfile.ZipFile(path) as z:
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
