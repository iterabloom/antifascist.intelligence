#!/usr/bin/env python3
"""Extract every assertion that will need a source, and every dated claim.

No network here, so nothing is verified: every row lands as `unverified`.
The point is the count — the citation debt — and a per-section join key.

Writes reports/claims.tsv and reports/dated.tsv.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

CLAIMS = os.path.join(common.REPORTS, "claims.tsv")
DATED = os.path.join(common.REPORTS, "dated.tsv")

PATTERNS = [
    ("inline_citation", re.compile(r"\([A-Z][A-Za-z'-]+(?:\s+et al\.?)?,?\s+\d{4}[a-z]?\)")),
    ("narrative_citation", re.compile(r"\b[A-Z][A-Za-z'-]+\s+et al\.\s*\(\d{4}\)")),
    ("named_instrument", re.compile(
        r"\b(?:[A-Z][\w'-]+\s+){1,5}"
        r"(?:Act|Regulation|Directive|Declaration|Convention|Principles|Guidelines|"
        r"Framework|Strategy|Initiative|Plan|Report|Recommendation|Charter|Code)\b")),
    ("named_body", re.compile(
        r"\b(?:UNESCO|OECD|G20|G7|NIST|FTC|NSF|IEEE|ACM|AAAI|EU|UN|WHO|ITU|"
        r"European Commission|European Parliament|Partnership on AI|"
        r"AI Now Institute|Future of Life Institute|CIFAR|CDEI)\b")),
    ("named_system", re.compile(
        r"\b(?:GPT-[234]|GPT|BERT|AlphaGo(?:\s+Zero)?|AlphaZero|AlphaFold|Agent57|"
        r"Watson|Rekognition|PredPol|Clearview|LaMDA|DALL-E|Sophia|LIME|SHAP)\b")),
    ("statistic", re.compile(r"\b\d{1,3}(?:\.\d+)?\s*(?:%|percent)\b|"
                             r"\b\d{1,3}(?:,\d{3})+\b|\$\s?\d[\d,.]*\s*(?:billion|million|trillion)?")),
    ("hedged_evidence", re.compile(
        r"\b(?:studies (?:show|suggest|indicate|have shown)|research (?:shows|suggests|indicates|has shown)|"
        r"evidence (?:suggests|shows)|it (?:has been|is) (?:shown|demonstrated|found)|"
        r"according to (?:[A-Z]|a study|research|the literature)|scholars argue|"
        r"researchers (?:have )?(?:found|argue|demonstrated)|"
        r"a (?:recent )?study)\b", re.I)),
    ("year", re.compile(r"\b(?:19[89]\d|20[0-4]\d)\b")),
    ("named_theory", re.compile(
        r"\b(?:[A-Z][\w'-]+\s+){1,4}(?:Theory|Hypothesis|Model|Effect|Paradox|Problem|Law)\b")),
]

TEMPORAL = re.compile(
    r"\b(currently|recent(?:ly)?|state-of-the-art|cutting-edge|latest|"
    r"in progress|still (?:being|under)|is being developed|newly|"
    r"emerging|proposed|forthcoming|as of)\b", re.I)

# A remediation hint for the dated register, per D8 (dateless prose, dated boxes).
def remediation(kind, snippet):
    if TEMPORAL.search(snippet) and re.search(r"\b(19|20)\d\d\b", snippet):
        return "generalize-or-box"
    if TEMPORAL.search(snippet):
        return "generalize"
    if kind == "named_system":
        return "generalize-or-box"
    return "box"


def sentences(text):
    for m in re.finditer(r"[^.!?]*[.!?]", text):
        s = m.group(0).strip()
        if s:
            yield m.start(), s


def main():
    # Reading order from `seq`, locator from the label (D-470). Both were
    # ORDER.tsv's `num`, which has been an identity and not a position since
    # D-406.
    order = common.order_rows()
    labels = common.section_labels()
    claims, dated = [], []
    cid = 0
    for r in order:
        path = os.path.join(common.REPO, r["path"])
        with open(path, encoding="utf-8", newline="") as f:
            lines = f.readlines()
        for ln, line in enumerate(lines, 1):
            s = line.strip()
            if not s or s.startswith(("<<", "<</", "#")):
                continue
            if ln == 1:
                continue  # heading
            for kind, rx in PATTERNS:
                for m in rx.finditer(line):
                    # keep the sentence around the hit for context
                    start = line.rfind(".", 0, m.start()) + 1
                    end = line.find(".", m.end())
                    snip = line[start:end + 1 if end != -1 else len(line)].strip()
                    cid += 1
                    row = {"claim_id": "C%04d" % cid,
                           "label": labels.get(r["path"], ""), "line": ln,
                           "kind": kind, "match": m.group(0)[:60],
                           "snippet": snip[:220], "status": "unverified", "note": ""}
                    claims.append(row)
                    if kind in ("year", "named_system") or TEMPORAL.search(snip):
                        d = dict(row)
                        d["remediation"] = remediation(kind, snip)
                        dated.append(d)
    common.write_tsv(CLAIMS, ["claim_id", "label", "line", "kind", "match",
                              "snippet", "status", "note"], claims)
    common.write_tsv(DATED, ["claim_id", "label", "line", "kind", "match",
                             "snippet", "remediation", "status", "note"], dated)
    print("wrote %s: %d rows" % (CLAIMS, len(claims)))
    by_kind = {}
    for c in claims:
        by_kind[c["kind"]] = by_kind.get(c["kind"], 0) + 1
    for k, v in sorted(by_kind.items(), key=lambda x: -x[1]):
        print("  %-20s %5d" % (k, v))
    secs = len({c["label"] for c in claims})
    print("sections with at least one claim: %d of %d" % (secs, len(order)))
    print("wrote %s: %d dated rows across %d sections"
          % (DATED, len(dated), len({d["label"] for d in dated})))


if __name__ == "__main__":
    main()
