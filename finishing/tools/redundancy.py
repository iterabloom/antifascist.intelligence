#!/usr/bin/env python3
"""Semantic redundancy across sections and paragraphs.

Runs offline against a locally cached sentence-transformer; falls back to
TF-IDF with --tfidf. Writes:
  reports/redundancy_sections.tsv   section-level pairs above threshold
  reports/redundancy_paragraphs.tsv paragraph-level pairs above threshold
  reports/redundancy_2.4_vs_7.4.tsv the known parallel treatment, in full
Matrices go to the scratchpad, not the repo.
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
    _, order = common.read_tsv(os.path.join(common.SECTIONS, "ORDER.tsv"))
    order.sort(key=lambda r: common.numkey(r["num"]))
    out = []
    for r in order:
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
        out.append({"num": r["num"], "title": r["title"],
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


def main():
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
        same = a["num"].split(".")[0] == b["num"].split(".")[0]
        rows.append({"score": "%.3f" % S[i, j], "a": a["num"], "a_title": a["title"],
                     "b": b["num"], "b_title": b["title"],
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
            pair.append({"score": "%.3f" % S[i, j], "a": secs[i]["num"], "a_title": secs[i]["title"],
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
            owner.append((s["num"], k + 1))
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
