"""Write 01_orderings.ipynb, outputs empty. The notebook is generated: edit this, then run it.

    .venv/bin/python build_notebook.py        # from ordering-perplexity/

Cell ids are fixed (c00, c01, ...), so a rebuild diffs only what changed.
"""
import os
import sys
import nbformat as nbf

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_orderings.ipynb")
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# Ordering perplexity: paragraphs and sentences

Does a Qwen base model find the book's paragraph and sentence orders more probable than shuffled ones, and where does it not?

For one section this notebook:

1. scores the original paragraph order against random shuffles;
2. swaps each pair of neighbouring paragraphs, to find joints that hold and joints that don't;
3. measures how much each paragraph is helped by the paragraphs before it (context gain);
4. shuffles the sentences inside each paragraph.

An optional sweep at the end runs step 1 over every section.

All numbers are negative log-likelihoods in **nats** under the model. *Δ = shuffled − original*, so a positive Δ means the model prefers the original. Lower perplexity is not better prose. It measures what a language model finds predictable, and an argument that surprises the reader at the right moment will score worse for it. Read the results as a map of where order carries information, not as a ranking.

**In Colab:** use a GPU runtime (Runtime → Change runtime type → T4 or better). The repository is public, so the setup cell clones it without credentials. To run a branch other than `main`, set `REPO_URL` and `REPO_REF` in the setup cell to the repository and branch the notebook was opened from. See `ordering-perplexity/README.md`.
""")

md("## Setup")
code(r'''
import os, sys, subprocess

IN_COLAB = "google.colab" in sys.modules
REPO_URL = "https://github.com/iterabloom/antifascist.intelligence.git"
REPO_REF = "main"          # branch to clone in Colab

if IN_COLAB:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pysbd", "transformers>=4.57", "accelerate"], check=True)
    REPO = "/content/antifascist.intelligence"
    if not os.path.isdir(REPO):
        # The repository is public (D-629, 2026-10-04): no token
        p = subprocess.run(["git", "clone", "--quiet", "--depth", "1", "--branch", REPO_REF, REPO_URL, REPO],
                           capture_output=True, text=True, env={**os.environ, "GIT_TERMINAL_PROMPT": "0"})
        if p.returncode:
            raise RuntimeError("clone of %s at %s failed: %s" % (REPO_URL, REPO_REF, p.stderr))
else:
    # Local Jupyter: the notebook sits inside the checkout.
    d = os.path.abspath(os.getcwd())
    while not os.path.isfile(os.path.join(d, "finishing", "tools", "render_markdown.py")):
        if os.path.dirname(d) == d:
            raise FileNotFoundError("run this notebook from inside an antifascist.intelligence checkout")
        d = os.path.dirname(d)
    REPO = d

HERE = os.path.join(REPO, "ordering-perplexity")
sys.path.insert(0, HERE)
import importlib, orderppl as op
importlib.reload(op)

import numpy as np, pandas as pd, torch
import matplotlib.pyplot as plt
pd.set_option("display.max_colwidth", 90)
print("repo:", REPO, "| commit:", subprocess.run(["git", "-C", REPO, "rev-parse", "--short", "HEAD"],
      capture_output=True, text=True).stdout.strip())
print("torch", torch.__version__, "| cuda:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "none")
''')

md(r"""
## Settings

`MODEL_ID` takes any Hugging Face causal LM. Use base models rather than instruct models: they were trained to predict running text, which is the quantity being measured.

`DTYPE` is part of the measurement. The same text scored at different batch sizes differed by 3.3 nats in bfloat16, 0.1 to 1.3 in float16 depending on the model, and at most 0.002 in float32 (README, *Noise floor*). Use float32 when the model fits. A free T4 has 15 GB:

| model | float32 | float16 | on a T4 |
|---|---|---|---|
| `Qwen/Qwen3-0.6B-Base` | 2.4 GB | 1.2 GB | float32 |
| `Qwen/Qwen3-1.7B-Base` | 6.9 GB | 3.4 GB | float32 (default) |
| `Qwen/Qwen3-4B-Base` | 16 GB | 8 GB | float16 |
| `Qwen/Qwen3-8B-Base` | 33 GB | 16 GB | no; L4 or A100 runtime in float16 |
| `Qwen/Qwen3.5-0.8B-Base` | 3.5 GB | 1.7 GB | float32; slower than Qwen3 without the linear-attention kernels (README) |
| `Qwen/Qwen3.5-2B-Base` | 9 GB | 4.5 GB | float32 for short sections, float16 for long ones; untested |

Totals depend on the tokenizer, so compare models on `orig_nats_per_char`, not on NLL or perplexity.
""")
code(r'''
MODEL_ID = "Qwen/Qwen3-1.7B-Base"
DTYPE = "float32"             # "float16" for models that don't fit; avoid "bfloat16" (see above)
SECTION = "1"                 # section number as printed ("1", "3.1", "12.2.1") or the full title
N_SHUFFLES = 50               # random paragraph orders scored against the original
SENT_SHUFFLES = 20            # random sentence orders per paragraph
FIX_FIRST = False             # keep the opening paragraph in place when shuffling
HEADING_AS_CONTEXT = True     # condition every score on the section heading (not itself scored)
SEED = 0

RUN_SWEEP = False             # step 5: paragraph shuffles over every section (slow)
SWEEP_SHUFFLES = 20
SWEEP_MIN_PARAGRAPHS = 3

SAVE_TO_DRIVE = False         # Colab only: write results to Google Drive instead of the VM's disk
''')

md("## The text")
code(r'''
md_path = os.path.join("/content" if IN_COLAB else HERE, "results", "book.md")
os.makedirs(os.path.dirname(md_path), exist_ok=True)
sections = op.parse_book(op.render_book(REPO, md_path))

overview = pd.DataFrame([dict(idx=s.index, title=s.title, level=s.level, paragraphs=len(s.paragraphs),
                              words=s.n_words, dropped=", ".join("%s %d" % kv for kv in s.skipped.items()))
                         for s in sections])
print("%d sections, %d prose paragraphs, %d words" % (len(sections), overview.paragraphs.sum(), overview.words.sum()))
overview
''')
code(r'''
def find_section(key):
    key = key.strip().rstrip(".")
    for s in sections:
        num = s.title.split()[0].rstrip(".") if s.title[:1].isdigit() else None
        if s.title == key or num == key:
            return s
    raise KeyError("no section %r; see the overview table" % key)

sec = find_section(SECTION)
paras = sec.paragraphs
context = sec.title if HEADING_AS_CONTEXT else None
print("%s — %d paragraphs, %d words" % (sec.title, len(paras), sec.n_words))
pd.DataFrame({"¶": range(1, len(paras) + 1), "opens": [p[:90] for p in paras],
              "sentences": [len(op.split_sentences(p)) for p in paras]})
''')

md("## The model")
code(r'''
if SAVE_TO_DRIVE and IN_COLAB:
    from google.colab import drive
    drive.mount("/content/drive")
    RESULTS = "/content/drive/MyDrive/ordering-perplexity-results"
else:
    RESULTS = os.path.join("/content" if IN_COLAB else HERE, "results")
os.makedirs(RESULTS, exist_ok=True)

scorer = op.Scorer(MODEL_ID, dtype=DTYPE)
print(scorer.describe())
tag = MODEL_ID.split("/")[-1] + "_" + sec.title.split()[0].rstrip(".")
rng = np.random.default_rng(SEED)
''')

md(r"""
### Noise floor

The same text scored in batches of different sizes can give slightly different totals, because the GPU kernels change with the batch shape. Differences smaller than this spread are not signal. The plots shade it gray. In float32 it is usually zero, and the plots then fall back to a 0.001-nat band.
""")
code(r'''
nf = op.noise_floor(scorer, paras, op.PARAGRAPH_SEP, np.random.default_rng(SEED), context)
NOISE = max(nf["spread"], 1e-3)
print("original-order NLL by batch size:", {k: round(v, 3) for k, v in nf["by_batch_size"].items()})
print("noise floor: %.3f nats" % NOISE)
''')

md("## 1. Paragraph order against random shuffles")
code(r'''
orig, shuf = op.shuffle_test(scorer, paras, op.PARAGRAPH_SEP, N_SHUFFLES, rng, context, FIX_FIRST)
summary = op.summarize_shuffles(orig, shuf)
op.plot_shuffles(orig, shuf, "%s: %d paragraph shuffles" % (sec.title, len(shuf)), NOISE); plt.show()
pd.Series(summary).round(3)
''')
code(r'''
# The shuffles the model liked best, for reading
best = sorted(shuf, key=lambda s: s.total_nll)[:5]
pd.DataFrame({"delta": [round(s.total_nll - orig.total_nll, 2) for s in best],
              "order (1-based)": [" ".join(str(i + 1) for i in s.order) for s in best]})
''')

md(r"""
## 2. Neighbour swaps

Each bar exchanges paragraphs *i* and *i+1* and leaves everything else in place. A long blue bar is a joint the model relies on. A red bar is a pair the model would rather read the other way round.
""")
code(r'''
swaps = op.adjacent_swaps(len(paras))
swap_scores = scorer.score_orders(paras, [o for _, o in swaps], op.PARAGRAPH_SEP, context)
swap_df = pd.DataFrame({"joint": [i for i, _ in swaps],
                        "delta": [s.total_nll - orig.total_nll for s in swap_scores],
                        "first": [paras[i][:60] for i, _ in swaps],
                        "second": [paras[i + 1][:60] for i, _ in swaps]})
op.plot_swaps(swap_df, "%s: neighbour swaps" % sec.title, NOISE); plt.show()
swap_df.sort_values("delta").round(2)
''')

md(r"""
## 3. Context gain

How much cheaper each paragraph is to predict in place, after the paragraphs before it, than read alone (after the heading only). A paragraph with low gain could stand anywhere, and one with high gain leans on what precedes it. The first paragraph's gain is near zero by construction. It is not exactly zero, because the token at a paragraph's end can merge with the blank line after it.
""")
code(r'''
alone = scorer.isolated(paras, context)
gain_df = pd.DataFrame({"paragraph": range(len(paras)),
                        "tokens": orig.unit_tokens,
                        "nll_in_place": orig.unit_nll,
                        "nll_alone": [a for a, _ in alone]})
gain_df["gain_per_token"] = (gain_df.nll_alone - gain_df.nll_in_place) / gain_df.tokens
op.plot_context_gain(gain_df, "%s: context gain per paragraph" % sec.title); plt.show()
gain_df.round(3)
''')

md(r"""
## 4. Sentence order inside each paragraph

For each paragraph with three or more sentences: the original sentence order against up to `SENT_SHUFFLES` shuffles. `frac_beat_orig` is the share of shuffles the model likes at least as well as the original. Sentence splitting uses `pysbd` and will occasionally split at an abbreviation.
""")
code(r'''
rows, sent_best = [], {}
for i, p in enumerate(paras):
    sents = op.split_sentences(p)
    if len(sents) < 3:
        continue
    o, sh = op.shuffle_test(scorer, sents, op.SENTENCE_SEP, SENT_SHUFFLES, rng, context)
    rows.append(dict(paragraph=i + 1, sentences=len(sents), **op.summarize_shuffles(o, sh)))
    b = min(sh, key=lambda s: s.total_nll)
    sent_best[i + 1] = (b.total_nll - o.total_nll, [sents[j] for j in b.order])
sent_df = pd.DataFrame(rows)
sent_df.round(3)
''')
code(r'''
# Paragraphs where some shuffle scored at least as well as the original, with that shuffle
for k, (d, s) in sorted(sent_best.items(), key=lambda kv: kv[1][0]):
    if d <= NOISE:
        print("¶%d  Δ=%.2f\n  %s\n" % (k, d, "\n  ".join(s)))
''')

md("## 5. Sweep: paragraph shuffles in every section")
code(r'''
if RUN_SWEEP:
    sweep = []
    for s in sections:
        if len(s.paragraphs) < SWEEP_MIN_PARAGRAPHS:
            continue
        ctx = s.title if HEADING_AS_CONTEXT else None
        try:
            o, sh = op.shuffle_test(scorer, s.paragraphs, op.PARAGRAPH_SEP, SWEEP_SHUFFLES,
                                    np.random.default_rng(SEED), ctx, FIX_FIRST)
        except (ValueError, torch.cuda.OutOfMemoryError) as e:
            print("skipped %s: %s" % (s.title, type(e).__name__))
            torch.cuda.empty_cache()
            continue
        sweep.append(dict(section=s.title, paragraphs=len(s.paragraphs), **op.summarize_shuffles(o, sh)))
        print("%-60s z=%6.2f  beat=%.2f" % (s.title[:60], sweep[-1]["z"], sweep[-1]["frac_beat_orig"]))
    sweep_df = pd.DataFrame(sweep).sort_values("z")
    sweep_df.to_csv(os.path.join(RESULTS, "sweep_%s.csv" % MODEL_ID.split("/")[-1]), index=False)
    display(sweep_df.round(3))
''')

md("## Save")
code(r'''
meta = dict(model=MODEL_ID, dtype=DTYPE, section=sec.title, seed=SEED, n_shuffles=N_SHUFFLES, fix_first=FIX_FIRST,
            heading_as_context=HEADING_AS_CONTEXT, noise_floor=NOISE,
            repo_commit=subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip())
pd.Series({**meta, **summary}).to_csv(os.path.join(RESULTS, "summary_%s.csv" % tag), header=False)
pd.DataFrame({"delta": [s.total_nll - orig.total_nll for s in shuf],
              "order": [" ".join(map(str, s.order)) for s in shuf]}).to_csv(os.path.join(RESULTS, "shuffles_%s.csv" % tag), index=False)
swap_df.to_csv(os.path.join(RESULTS, "swaps_%s.csv" % tag), index=False)
gain_df.to_csv(os.path.join(RESULTS, "context_gain_%s.csv" % tag), index=False)
sent_df.to_csv(os.path.join(RESULTS, "sentences_%s.csv" % tag), index=False)
print("wrote", RESULTS)
''')

for i, c in enumerate(cells):
    c["id"] = "c%02d" % i          # stable ids, so a rebuild diffs only what changed
nb = nbf.v4.new_notebook()
nb.cells = cells
nb.metadata = {
    "kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
    "language_info": {"name": "python"},
    "accelerator": "GPU",
    "colab": {"provenance": [], "gpuType": "T4"},
}
nbf.write(nb, out)
print("wrote", out)
