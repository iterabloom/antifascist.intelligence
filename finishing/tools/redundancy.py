#!/usr/bin/env python3
"""Semantic redundancy across sections and paragraphs.

Runs offline against a locally cached sentence-transformer; falls back to
TF-IDF with --tfidf. Writes:
  reports/redundancy_sections.tsv   section-level pairs above threshold
  reports/redundancy_paragraphs.tsv paragraph-level pairs above threshold
  reports/redundancy_2.4_vs_7.4.tsv the known parallel treatment, in full
Matrices go to the scratchpad, not the repo.

--pure RUNS WITHOUT numpy (D-386). Neither of the two paths above can run on
this machine: numpy is not installed, so the reports had gone stale on 2026-08-29
and every pass since has recorded that the tool cannot run. --pure implements
TF-IDF cosine in the standard library -- sublinear term frequency, inverse
document frequency over the units being compared, L2 normalization, cosine as a
dot product over sparse dictionaries -- and writes the same three reports.

What --pure is not: it is the lexical tier only. It finds a sentence reused and a
sentence nearly reused, which is what the three echoes standing in the record are
(D-338 twice, D-339 once). It does not find the same claim in different words,
which is what the sentence-transformer path is for and what stays unavailable.

--pure also keeps same-section paragraph pairs, which the numpy path discards.
That exclusion is why redundancy.py would never have found D-339's echo: both of
its members are paragraphs of section 3.5, six lines apart. Pairs inside one
section carry same_section=yes so they can be read apart.
"""
import os
import re
import sys

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

MODEL = "sentence-transformers/paraphrase-MiniLM-L6-v2"
# Everything here is one domain, so baseline cosine is high; a fixed threshold
# is meaningless. Calibrate against the observed distribution and keep top-N.
SEC_TOP = int(os.environ.get("SEC_TOP", "200"))
PAR_TOP = int(os.environ.get("PAR_TOP", "400"))


def percentiles(vals, label):
    import numpy as np
    q = np.percentile(vals, [50, 90, 99, 99.9])
    print("  %s cosine: median %.3f  p90 %.3f  p99 %.3f  p99.9 %.3f  max %.3f"
          % (label, q[0], q[1], q[2], q[3], float(max(vals))))
    return q


def load_sections():
    """Sections in reading order, each carrying its label and its chapter.

    The locator is the label and the chapter comes from the path (D-470).
    `num` is kept because the 2.4-by-7.4 grid below selects on it: that grid is
    a frozen investigation into two sections identified by the numbers they
    carried when it was run, and `num` is still those identities.
    """
    labels, chapters = common.section_labels(), common.chapter_numbers()
    out = []
    for r in common.order_rows():
        with open(os.path.join(common.REPO, r["path"]), encoding="utf-8", newline="") as f:
            lines = f.readlines()
        body, quote = [], 0
        for line in lines[1:]:
            s = line.strip()
            if s == "<<quote>>":
                quote += 1
                continue
            if s == "<</quote>>":
                quote -= 1
                continue
            if quote > 0 or s.startswith(("#", "<<", "<</")):
                continue
            body.append(line)
        paras = [re.sub(r"\s+", " ", p).strip() for p in "".join(body).split("\n")]
        paras = [p for p in paras if len(p.split()) >= 25]
        out.append({"num": r["num"], "label": labels.get(r["path"], ""),
                    "chapter": chapters[r["path"]], "title": r["title"],
                    "text": " ".join(paras), "paras": paras})
    return [s for s in out if s["text"].split()]


def embed(texts, tfidf=False):
    import numpy as np
    if tfidf:
        from sklearn.feature_extraction.text import TfidfVectorizer
        X = TfidfVectorizer(stop_words="english", sublinear_tf=True,
                            max_features=40000).fit_transform(texts)
        import sklearn.preprocessing as pp
        return pp.normalize(X).toarray().astype("float32")
    import logging
    import warnings
    warnings.filterwarnings("ignore")
    for n in ("transformers", "sentence_transformers", "torch"):
        logging.getLogger(n).setLevel(logging.ERROR)
    from sentence_transformers import SentenceTransformer
    m = SentenceTransformer(MODEL)
    v = m.encode(texts, batch_size=64, show_progress_bar=False,
                 normalize_embeddings=True, convert_to_numpy=True)
    return v.astype("float32")


STOP = set("""a about above after again against all also am an and any are as at be
because been before being below between both but by can cannot could did do does
doing down during each few for from further had has have having he her here hers
him his how i if in into is it its itself just me more most my no nor not now of
off on once only or other our out over own same she should so some such than that
the their them then there these they this those through to too under until up
very was we were what when where which while who whom why will with would you
your""".split())
_TOK = re.compile(r"[a-z][a-z'-]+")


def _tf(text):
    import math
    counts = {}
    for w in _TOK.findall(text.lower()):
        if w in STOP or len(w) < 3:
            continue
        counts[w] = counts.get(w, 0) + 1
    return {w: 1.0 + math.log(c) for w, c in counts.items()}      # sublinear tf


def pure_vectors(texts):
    """L2-normalized tf-idf vectors as sparse dicts. No numpy."""
    import math
    tfs = [_tf(t) for t in texts]
    df = {}
    for d in tfs:
        for w in d:
            df[w] = df.get(w, 0) + 1
    n = len(tfs)
    out = []
    for d in tfs:
        v = {w: t * math.log(n / df[w]) for w, t in d.items() if df[w] < n}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        out.append({w: x / norm for w, x in v.items()})
    return out


def pure_cos(a, b):
    if len(b) < len(a):
        a, b = b, a
    return sum(x * b[w] for w, x in a.items() if w in b)


def pure_percentiles(vals, label):
    vals = sorted(vals)
    if not vals:
        print("  %s cosine: no pairs" % label)
        return
    def q(p):
        return vals[min(len(vals) - 1, int(p * (len(vals) - 1)))]
    print("  %s cosine: median %.3f  p90 %.3f  p99 %.3f  p99.9 %.3f  max %.3f"
          % (label, q(.5), q(.9), q(.99), q(.999), vals[-1]))


def main_pure():
    secs = load_sections()
    print("%d sections with body text (pure-python tf-idf, lexical tier only)"
          % len(secs))
    V = pure_vectors([s["text"] for s in secs])
    rows, vals = [], []
    for i in range(len(secs)):
        for j in range(i + 1, len(secs)):
            c = pure_cos(V[i], V[j])
            vals.append(c)
            a, b = secs[i], secs[j]
            rows.append({"score": "%.3f" % c, "a": a["label"], "a_title": a["title"],
                         "b": b["label"], "b_title": b["title"],
                         "same_chapter": "yes" if a["chapter"] == b["chapter"]
                         else "no"})
    pure_percentiles(vals, "section")
    rows.sort(key=lambda r: -float(r["score"]))
    rows = rows[:SEC_TOP]
    common.write_tsv(os.path.join(common.REPORTS, "redundancy_sections.tsv"),
                     ["score", "a", "a_title", "b", "b_title", "same_chapter"], rows)
    print("top %d section pairs written (cross-chapter: %d); score range %s..%s"
          % (len(rows), sum(1 for r in rows if r["same_chapter"] == "no"),
             rows[-1]["score"], rows[0]["score"]))

    idx = {s["num"]: i for i, s in enumerate(secs)}
    pair = []
    for an in [s["num"] for s in secs if s["num"].startswith("2.4")]:
        for bn in [s["num"] for s in secs if s["num"].startswith("7.4")]:
            i, j = idx[an], idx[bn]
            pair.append({"score": "%.3f" % pure_cos(V[i], V[j]),
                         "a": secs[i]["label"], "a_title": secs[i]["title"],
                         "b": secs[j]["label"], "b_title": secs[j]["title"]})
    pair.sort(key=lambda r: -float(r["score"]))
    common.write_tsv(os.path.join(common.REPORTS, "redundancy_2.4_vs_7.4.tsv"),
                     ["score", "a", "a_title", "b", "b_title"], pair)
    print("2.4x7.4 grid: %d pairs, top score %s"
          % (len(pair), pair[0]["score"] if pair else "n/a"))

    plist, owner = [], []
    for s in secs:
        for k, p in enumerate(s["paras"]):
            plist.append(p)
            owner.append((s["label"], k + 1))
    print("%d paragraphs >= 25 words" % len(plist))
    P = pure_vectors(plist)
    prows, pvals = [], []
    for i in range(len(plist)):
        for j in range(i + 1, len(plist)):
            c = pure_cos(P[i], P[j])
            pvals.append(c)
            prows.append({"score": "%.3f" % c,
                          "a": owner[i][0], "a_par": owner[i][1],
                          "b": owner[j][0], "b_par": owner[j][1],
                          "same_section": "yes" if owner[i][0] == owner[j][0] else "no",
                          "a_text": plist[i][:150], "b_text": plist[j][:150]})
    pure_percentiles(pvals, "paragraph")
    prows.sort(key=lambda r: -float(r["score"]))
    prows = prows[:PAR_TOP]
    common.write_tsv(os.path.join(common.REPORTS, "redundancy_paragraphs.tsv"),
                     ["score", "a", "a_par", "b", "b_par", "same_section",
                      "a_text", "b_text"], prows)
    print("top %d paragraph pairs written (same-section: %d); score range %s..%s"
          % (len(prows), sum(1 for r in prows if r["same_section"] == "yes"),
             prows[-1]["score"], prows[0]["score"]))


def main():
    if "--pure" in sys.argv:
        return main_pure()
    import numpy as np
    tfidf = "--tfidf" in sys.argv
    secs = load_sections()
    print("%d sections with body text (%s)" % (len(secs), "tf-idf" if tfidf else MODEL))

    V = embed([s["text"] for s in secs], tfidf)
    S = V @ V.T
    iu = np.triu_indices(len(secs), 1)
    percentiles(S[iu], "section")
    rows = []
    for i, j in zip(*iu):
        a, b = secs[i], secs[j]
        same = a["chapter"] == b["chapter"]
        rows.append({"score": "%.3f" % S[i, j], "a": a["label"], "a_title": a["title"],
                     "b": b["label"], "b_title": b["title"],
                     "same_chapter": "yes" if same else "no"})
    rows.sort(key=lambda r: -float(r["score"]))
    rows = rows[:SEC_TOP]
    common.write_tsv(os.path.join(common.REPORTS, "redundancy_sections.tsv"),
                     ["score", "a", "a_title", "b", "b_title", "same_chapter"], rows)
    print("top %d section pairs written (cross-chapter: %d); score range %s..%s"
          % (len(rows), sum(1 for r in rows if r["same_chapter"] == "no"),
             rows[-1]["score"], rows[0]["score"]))

    # 2.4 vs 7.4 in full
    ai = [i for i, s in enumerate(secs) if s["num"].startswith("2.4")]
    bi = [i for i, s in enumerate(secs) if s["num"].startswith("7.4")]
    pair = []
    for i in ai:
        for j in bi:
            pair.append({"score": "%.3f" % S[i, j], "a": secs[i]["label"], "a_title": secs[i]["title"],
                         "b": secs[j]["num"], "b_title": secs[j]["title"]})
    pair.sort(key=lambda r: -float(r["score"]))
    common.write_tsv(os.path.join(common.REPORTS, "redundancy_2.4_vs_7.4.tsv"),
                     ["score", "a", "a_title", "b", "b_title"], pair)
    print("2.4x7.4 grid: %d pairs, top score %s" % (len(pair), pair[0]["score"] if pair else "n/a"))

    # paragraph level
    plist, owner = [], []
    for s in secs:
        for k, p in enumerate(s["paras"]):
            plist.append(p)
            owner.append((s["label"], k + 1))
    print("%d paragraphs >= 25 words" % len(plist))
    P = embed(plist, tfidf)
    PM = P @ P.T
    piu = np.triu_indices(len(plist), 1)
    percentiles(PM[piu], "paragraph")
    prows = []
    for i, j in zip(*piu):
        if owner[i][0] == owner[j][0]:
            continue
        prows.append({"score": "%.3f" % PM[i, j],
                      "a": owner[i][0], "a_par": owner[i][1],
                      "b": owner[j][0], "b_par": owner[j][1],
                      "a_text": plist[i][:150], "b_text": plist[j][:150]})
    prows.sort(key=lambda r: -float(r["score"]))
    common.write_tsv(os.path.join(common.REPORTS, "redundancy_paragraphs.tsv"),
                     ["score", "a", "a_par", "b", "b_par", "a_text", "b_text"], prows[:PAR_TOP])
    print("top %d cross-section paragraph pairs written; score range %s..%s"
          % (min(PAR_TOP, len(prows)), prows[min(PAR_TOP, len(prows)) - 1]["score"], prows[0]["score"]))


if __name__ == "__main__":
    main()
