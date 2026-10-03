# Worklog: ordering-perplexity

Design notes and the running log for this folder. Entries are appended in date order; earlier entries are left as written.

### 2026-10-03 00:27 EDT — repositories created

Created `antifascist-intelligence-ppl` (bare: README, .gitignore) and this notebook, at the maintainer's request. The project's scope is not yet written down.

### 2026-10-03 — scope, and where the work lives

Scope, from the maintainer: use Qwen base models, preferably in Colab, to compute the perplexity of different paragraph and sentence orderings of the book. It is an exploratory digression from the manuscript work, which runs in a separate session on another VM.

The work lives in the book's repository, `iterabloom/ethical.superintelligence`, in its own top-level folder `ordering-perplexity/`, not in `../antifascist-intelligence-ppl/`. That folder holds `orderppl.py` (text extraction, scoring, plots), `01_orderings.ipynb` and a README. Nothing in the book's tooling reads it, and the repository's invariant suite and names guard do not scan it.

This VM reaches GitHub over HTTPS through `gh` as `jgstern-agent`. The clone at `~/ethical.superintelligence` is shallow (`--depth 1`), because two full clones stalled with no data arriving.

Measured on the RTX 3060 (capped at 6 GiB; another job of the maintainer's holds a CUDA context on it): scoring in bf16 gives a 3.3-nat spread for the same text across batch sizes, fp16 0.1, fp32 0.000. The notebook defaults to fp32. Qwen3-0.6B-Base in fp32 runs chapter 1 (3,082 tokens) end to end in 96 s, and all 50 paragraph shuffles score worse than the original (smallest Δ 63 nats).

Later the same day: Qwen3-1.7B-Base (fp16, under the cap) and Qwen3.5-0.8B-Base (fp32, transformers' reference kernels) both run unchanged and match the library's own loss. The fp16 noise floor turned out to depend on the model: 1.3 nats for the 1.7B against 0.1 for the 0.5B measured first. Two local commits in the book repo, `f09a719` and `9e80fe8`, not pushed as of this entry.

Pushed to `origin/main` at the maintainer's instruction (`ee935f7..9e80fe8`, a fast-forward; the manuscript session on the other VM must pull before its next push). `../antifascist-intelligence-ppl/` held only its initial placeholder commit and is retired; this notebook now points at `../ethical.superintelligence/ordering-perplexity/` and goes to GitHub as a private repository under `iterabloom`.

### 2026-10-03 — the worklog moves into this folder

At the maintainer's instruction the lab notebook lives in one place only: here, as `ordering-perplexity/worklog.md` in the book's repository. Its three commits in the separate repository `iterabloom/antifascist-intelligence-ppl_lab_notebook` (created earlier the same day, private) carried only this file and a README that pointed here; that repository and the local `~/antifascist-intelligence-ppl_lab_notebook/` are superseded. The handoff note is `HANDOFF.md`.

### 2026-10-03 — everything in one folder

At the maintainer's instruction, everything belonging to this work is in `ordering-perplexity/`. The notebook generator, which had lived in a session scratch directory, is now `build_notebook.py`; rebuilding from it reproduces the committed notebook byte for byte. The Python environment was rebuilt from uv's cache at `ordering-perplexity/.venv`, and the test runs' figures and executed notebook moved into `results/`. Both are gitignored. Outside this folder there remain only the Hugging Face model cache, the retired `~/antifascist-intelligence-ppl/`, the local `~/antifascist-intelligence-ppl_lab_notebook/` copy, and the private repository `iterabloom/antifascist-intelligence-ppl_lab_notebook`; the last three are to be deleted.

### 2026-10-03 — folder-level agent instructions

With the author's approval, `ordering-perplexity/AGENTS.md` and a `CLAUDE.md` that imports it, mirroring the repository root. A session started in this folder loads both the root `AGENTS.md` (through the root `CLAUDE.md`) and this one. It states that the folder is a side project to the book and must not touch the manuscript, that another session pushes to `main`, and the working conventions recorded in `HANDOFF.md`.

The manuscript session renamed the repository to `iterabloom/antifascist.intelligence` the same afternoon (`badcd40`) and carried the rename into this folder's clone URL and messages. Its `fc2f47b` fixed the renderer's two-key citation bug noted in `HANDOFF.md`; the cleanup regex still handles the old form. This VM's checkout stays at `~/ethical.superintelligence` for now, with `origin` pointed at the new name.

The agent VM's checkout moved from `~/ethical.superintelligence` to `~/antifascist.intelligence` to match the repository and the manuscript VM. `ordering-perplexity/.venv` was rebuilt from uv's cache, because a venv's scripts record their absolute path; torch 2.14.1+cu130, transformers 5.18.0, JupyterLab 4.6.4, CUDA visible.
