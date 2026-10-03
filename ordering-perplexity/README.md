# ordering-perplexity

An exploratory digression from the book: Qwen base models score the
manuscript's paragraph and sentence orders against rearrangements of them.
Nothing in `manuscript/` or `finishing/` reads anything in this folder, and
nothing here edits the book.

| File | What it is |
|---|---|
| `01_orderings.ipynb` | One section at a time: original paragraph order against random shuffles, neighbour swaps, context gain per paragraph, sentence shuffles inside each paragraph, and an optional sweep over every section |
| `orderppl.py` | Text extraction, scoring and plots, imported by the notebook |
| `build_notebook.py` | Generates `01_orderings.ipynb`; edit this rather than the notebook |
| `worklog.md` | The running worklog and design notes, appended in date order |
| `HANDOFF.md` | State of the work, what has and has not been checked, and the pitfalls; read it before picking this up |
| `results/` | Written by the notebook, gitignored: CSVs, the rendered book text, and on the agent VM the 2026-10-03 test runs (`figures/`, an executed notebook) |

## Running in Colab

1. **Open the notebook.** In Colab: File → Open notebook → GitHub, tick
   *Include private repos*, and authorize Colab for `jgstern-agent`. If
   `iterabloom/ethical.superintelligence` does not appear, the `iterabloom`
   organization has not granted Colab access; an owner approves it under the
   organization's Settings → Third-party access. Uploading the `.ipynb` from a
   local checkout works as well.
2. **Give it a GPU.** Runtime → Change runtime type → T4 (free) or better.
3. **Give it read access to the repository.** The notebook clones the repo
   to get the manuscript and `orderppl.py`. Create a fine-grained token on
   GitHub (Settings → Developer settings → Fine-grained tokens) with resource
   owner `iterabloom`, only this repository, and *Contents: Read-only*. In
   Colab, open the key icon in the left sidebar, add a secret named
   `GITHUB_TOKEN` with the token as its value, and switch on notebook access.
   The setup cell removes the token from the clone's git config after cloning.
4. Run all. The default settings score chapter 1 with `Qwen/Qwen3-1.7B-Base`.

Colab clones the branch named in `REPO_REF` (default `main`), so changes to
`orderppl.py` reach Colab only once they are pushed.

Results go to `/content/results/` on the Colab VM, which is lost when the
runtime ends. Set `SAVE_TO_DRIVE = True` to write them to
`MyDrive/ordering-perplexity-results/` instead.

## Running locally

From `ordering-perplexity/` in a checkout, with a CUDA GPU:

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install torch "transformers>=4.57" accelerate pysbd pandas matplotlib nbformat jupyterlab
jupyter lab 01_orderings.ipynb
```

`.venv/` is gitignored by the repository's root `.gitignore`. On the
author's agent VM the environment already exists at
`ordering-perplexity/.venv` (torch 2.14.1+cu130, transformers 5.18.0).

The notebook is generated. To change it, edit `build_notebook.py` and run
`.venv/bin/python build_notebook.py`, then commit both files.

## What is measured

- **Text.** `finishing/tools/render_markdown.py` renders the manuscript to
  Markdown and `orderppl.parse_book` cuts it at every heading. Citation keys,
  footnotes and leftover LaTeX are removed. Epigraphs, lists, tables and
  standalone bold heads are dropped, and the dropped blocks are counted per
  section in the overview table. A paragraph that opens with a bold run-in
  head keeps it as plain text. Paragraphs that introduced a list end in a
  colon with the list gone.
- **Score.** An ordering is joined (paragraphs with a blank line, sentences
  with a space) and scored as one sequence after `<|endoftext|>` and,
  optionally, the section heading. The prefix is not scored. Every token of
  the joined text is, so two orderings of the same units are compared on the
  same text, differing only in how the tokenizer splits the joins. Totals are
  summed negative log-likelihood in nats. *Δ = shuffled − original*: positive
  means the model prefers the original.
- **Attribution.** Each token's NLL is credited to the unit its first
  character falls in, and a separator to the unit after it. That is what
  context gain uses.
- **Noise floor.** The same text scored at batch sizes 1, 2 and 4 does not
  always give the same total, because the GPU kernels change with the batch
  shape. Chapter 1 on the RTX 3060, 2026-10-03:

  | model | bf16 | fp16 | fp32 |
  |---|---|---|---|
  | Qwen2.5-Coder-0.5B-Instruct | 3.3 | 0.1 | 0.000 |
  | Qwen3-1.7B-Base | | 1.3 | |
  | Qwen3.5-0.8B-Base | | | 0.002 |

  (nats; blank = not measured). Sentence shuffles move totals by a few to a
  few tens of nats, so the notebook defaults to fp32. It measures the spread
  for the chosen section and model and shades it on every plot.

Perplexity is what a language model finds predictable. It is not a measure of
whether an argument is well ordered: a paragraph placed to surprise the reader
should score worse for it. The output is a map of where the order carries
information the model can use.

## Models

Use base models. Instruct models are tuned away from the raw distribution of
running text, which is the quantity being measured.

- **Qwen3 base** (`Qwen/Qwen3-{0.6B,1.7B,4B,8B,14B}-Base`): plain transformers,
  32k context, loaded with `AutoModelForCausalLM`. On a T4 the GPU has no
  bf16, so the notebook runs fp16 and raises if any NLL comes back non-finite.
- **Qwen3.5 base** (`Qwen/Qwen3.5-{0.8B,2B,4B,9B}-Base`): hybrid linear and
  full attention, published as image-text-to-text models. With transformers
  5.18, `AutoModelForCausalLM` loads the text-only `Qwen3_5ForCausalLM` and
  the notebook runs it unchanged. Measured 2026-10-03 on the RTX 3060 with
  `Qwen3.5-0.8B-Base` in fp32: the scorer matches the library's own loss
  (575.785 nats either way), the noise floor is 0.002 nats, chapter 1 against
  20 shuffles takes 23.6 s, section 3.1 (9,307 tokens) scores at about 4 s
  per ordering, and peak memory is 5.2 GB. That is with transformers'
  reference PyTorch path for the linear-attention layers, which it warns is
  "much slower" than the `flash-linear-attention` and `causal-conv1d`
  kernels. Installing those in Colab is untested here; `causal-conv1d`
  compiles CUDA code on install. The tokenizer has 248k entries against
  Qwen3's 152k, so compare across the two families on nats per character:
  chapter 1 scores 0.752 under `Qwen3.5-0.8B-Base` and 0.757 under
  `Qwen3-0.6B-Base`.

Longest section: 3.1, about 7,500 words, roughly 10,000 tokens. Scoring
batches are capped at `max_batch_tokens` (default 16,384), so a section that
long is scored one ordering at a time.

## Rules from AGENTS.md that apply here

The named-persons rule covers notebook output. The manuscript cites real
researchers in the ordinary scholarly way, and that text is what the notebook
prints, so commit the notebook with its outputs cleared (Edit → Clear all
outputs, or `jupyter nbconvert --clear-output --inplace`), and keep results out
of git as `.gitignore` already does. Do not point the notebook at the
persona-device archive.
