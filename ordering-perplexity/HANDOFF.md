# Handoff: ordering-perplexity

State as of 2026-10-05, for whoever picks this up next, human or agent. Read
`README.md` for what the notebook measures and how to run it. This file is
the state of the work, what has and has not been checked, and what will trip
you up.

## What this is

Exploratory work for the book's author: compute the perplexity of the book's
paragraph and sentence orders, and of rearrangements of them, under Qwen base
models, preferably in Colab. It is a digression from the manuscript work, not
part of the book. **Another session edits the manuscript on `main` from a
different machine.** Do not touch `manuscript/` or `finishing/` from this
work, and pull before every push.

The running worklog and design notes are in `worklog.md`, next to this file.
Append to it rather than editing earlier entries.

## Where things stand

- `01_orderings.ipynb` and `orderppl.py` are on `main` (commits `f09a719`,
  `9e80fe8`). The notebook is committed with no outputs.
- **Run end to end, locally, on an RTX 3060:** `Qwen3-0.6B-Base` in fp32,
  chapter 1, 95 s, 0 errors, 3 figures. The whole-book sweep ran once, with
  `Qwen2.5-Coder-0.5B-Instruct`, in 590 s. That model was a stand-in for
  checking the mechanics and its numbers are not findings.
- **Scorer checked against the library's own loss** (summed token NLL, same
  text) for Qwen2.5-Coder-0.5B-Instruct (681.211), Qwen3-1.7B-Base in fp16
  (518.058) and Qwen3.5-0.8B-Base in fp32 (575.785). Each matched to the
  printed precision.
- **First results, chapter 1 (“Twenty Seconds”, 20 paragraphs, 3,082
  tokens):** no shuffle beat the original. That held for all 50 shuffles
  under Qwen3-0.6B-Base (smallest Δ 63 nats), all 50 under Qwen3-1.7B-Base
  in fp16 (smallest Δ 70), and all 20 under Qwen3.5-0.8B-Base (smallest Δ 36).
  Swapping paragraphs 3 and 4 costs −0.22 nats under the 0.6B model. That
  joint is where the parser dropped the bold head “The reported system”.
- **First Colab run, 2026-10-05:** `Qwen3-1.7B-Base` in fp32 on an A100
  40 GB, chapter 1 with its two footnotes still in (see below), manuscript
  `df2b3ae`, code `fc2bf71`. Noise floor 0.000 nats (batch sizes 1, 2, 4).
  All 50 paragraph shuffles scored worse than the original (smallest Δ 67.2,
  mean 161.2, z 4.66). Swapping 3 and 4 costs −0.23 nats, as under the 0.6B
  model. The swaps the model prefers most are in the reporting block,
  paragraphs 5 to 8 (−7.4, −10.1, −17.9). In sentence shuffles, paragraphs
  19 and 20 are the only ones with negative z (`frac_beat_orig` 0.8 and 0.7,
  20 shuffles each, no correction across the 15 paragraphs tested). Not
  rerun since the footnote fix.

## Not done or not checked

- **Colab has run once, on an A100** (above); not yet on a T4 with a model
  that fits. Since 2026-10-05 the setup cell fetches two
  public repositories without a token: the manuscript from
  `iterabloom/antifascist.intelligence` (`BOOK_URL`), where the manuscript
  session pushes, and only `ordering-perplexity/` from
  `jgstern-agent/antifascist.intelligence` (`CODE_URL`), where this work is
  pushed. Rerunning the cell brings both up to date. Checked from a cloud
  container without a GPU, under a faked `google.colab` with pip skipped:
  first run and rerun of both fetches, the code checkout holding only this
  folder, `orderppl` imported from it, a rerun picking up a new commit
  (against a local repository), and the local-checkout path. The author's
  Colab run then confirmed opening from GitHub, both fetches and the model
  download. Colab's transformers version was not printed.
- **Two repositories.** `iterabloom/antifascist.intelligence` is the
  manuscript's; its `main` still carries an `ordering-perplexity/` frozen at
  `df2b3ae`, which nothing reads. This work is pushed to
  `jgstern-agent/antifascist.intelligence`, whose `main` was at `df2b3ae`
  too before it. How the two repositories' `main` branches are kept in step,
  if at all, was not checked.
- **Footnotes were scored as paragraphs until 2026-10-05.** The renderer
  writes Pandoc footnotes (`[^N]` inline, a `[^N]: …` block after the
  paragraph), which `parse_book` passed through: each definition became a
  prose paragraph at the end of its section and the markers stayed in the
  text. Fixed in `orderppl.py` the same day: markers removed, definitions
  dropped and counted (14 in the book). Every result before the fix,
  including the 2026-10-05 Colab run, carries them; chapter 1 has two. With
  them removed, chapter 1 parses to 20 paragraphs, the count of 2026-10-03,
  so the "22, not 20" this file said earlier that day was the footnotes,
  not a change in the manuscript. Whether chapter 1's text changed between
  the two runs was not checked. The longest section is now 4.1 (46,817
  characters), not 3.1.
- **Why the T4 ran out of memory** with `Qwen3-1.7B-Base` in fp32 on
  chapter 1 (2026-10-05): which cell failed and the traceback were not
  recorded. The run went through on an A100 40 GB.
- Any model at 4B or above. The `flash-linear-attention` and `causal-conv1d`
  kernels for Qwen3.5, which ran on transformers' reference path.
- The sweep with a base model. Sentence-level results for any base model,
  beyond the mechanics run.
- Statistics beyond the z-score and `frac_beat_orig`: there are no confidence
  intervals and no correction across sections.

## What will trip you up

- **Precision is part of the measurement.** For chapter 1, the spread in the
  original order's score across batch sizes 1, 2 and 4 was 3.3 nats in bf16,
  0.1 to 1.3 in fp16 (it depends on the model), and at most 0.002 in fp32.
  Sentence shuffles move totals by a few to a few tens of nats. Keep fp32
  unless the model does not fit. If you must use fp16, read the noise-floor
  cell before reading any small Δ.
- **Compare across tokenizers on `orig_nats_per_char`**, not on total NLL or
  perplexity. Qwen3.5's vocabulary is 248k against Qwen3's 152k.
- **The renderer belongs to the manuscript session.** Report a bug in
  `finishing/tools/render_markdown.py` rather than editing it. One is already
  fixed: it rendered a two-key citation with a locator as `[@a, ch. 9]{b}`
  (section 10.4), and since `fc2f47b` (2026-10-03) writes
  `[@a, ch. 9; @b]`. `orderppl._CITE_RE` strips both forms.
- **Text extraction drops some blocks.** Epigraphs, lists, the tables and
  standalone bold heads are removed, so section boundaries inside a heading
  span are invisible to the scorer. A paragraph that introduced a list now
  ends in a colon with nothing after it. The overview table counts the dropped
  blocks per section.
- **The commit-msg hook rewrites model and vendor names** in commit messages
  (`.githooks/brand-patterns.txt` lists Qwen, Claude, GPT, Llama and others)
  into filler phrases. Write "base LM" in commit messages, not the model name.
  File contents are not affected.
- **Hooks are not on in a fresh clone.** Run `git config core.hooksPath
  .githooks` so the pre-commit suite runs as it does on the author's
  machines. The suite and `names_guard.py` do not scan this folder. Before a
  commit, run `python3 finishing/tools/names_guard.py --paths
  ordering-perplexity/*`.
- **Named persons.** The rule covers notebook
  output. The book's own text is fine to print, but commit notebooks with
  outputs cleared, keep `results/` out of git, and never point anything here
  at `persona-device-files_*.zip`.
- **The notebook is generated.** Edit `build_notebook.py` and rerun it, not
  the `.ipynb`; a hand edit is lost at the next rebuild. Cell ids are fixed
  (`c00` to `c25`), so diffs show only real changes, and a rebuild of an
  unchanged script reproduces the committed notebook byte for byte.

## Environment notes (the author's agent VM, `jgstern_agent`)

- The repository was renamed on 2026-10-03 from `iterabloom/ethical.superintelligence`
  to `iterabloom/antifascist.intelligence` (`badcd40`); GitHub redirects the
  old name. Both VMs keep their checkout at `~/antifascist.intelligence`.
  The agent VM's was moved there from `~/ethical.superintelligence` the same
  day. It is a shallow clone (`--depth 1`), because two full clones stalled
  with no data arriving. Pushing from it works.
- GitHub access is HTTPS through `gh`, logged in as `jgstern-agent`.
- Start agent sessions for this work from
  `~/antifascist.intelligence/ordering-perplexity/`, where this folder's
  `AGENTS.md` loads.
- **Hugging Face downloads crash on the VM's proxy settings.** `NO_PROXY`
  contains an IPv6 CIDR (`fd00:200::/40`), which `httpx` rejects as a URL
  port. Override it per command:
  `NO_PROXY=localhost,127.0.0.1,10.200.0.0/16 no_proxy=$NO_PROXY ...`.
  The network was slow (1–14 MB/s) on 2026-10-03.
- Cached in `~/.cache/huggingface/hub`: `Qwen3-0.6B-Base`, `Qwen3-1.7B-Base`,
  `Qwen3.5-0.8B-Base`. The Python environment is `ordering-perplexity/.venv`
  (torch 2.14.1+cu130, transformers 5.18.0, JupyterLab), gitignored. The
  2026-10-03 test runs are in `results/` on that VM: the chapter-1 figures
  for `Qwen3-0.6B-Base` in `results/figures/`, and the executed sweep
  notebook for the Qwen2.5 stand-in.
- **The RTX 3060 (12 GB) is shared.** Another of the author's jobs held a
  CUDA context on it. Check `nvidia-smi` first, and cap your process, for
  example with `torch.cuda.set_per_process_memory_fraction(0.5)`.
- A Claude Code cloud session gets this repository from GitHub, not this VM:
  no GPU is documented, and whether its network allowlist reaches
  huggingface.co was not checked.

## Reasonable next steps

1. Run the notebook in Colab on a T4 with the defaults, and fix whatever the
   setup cell gets wrong.
2. Run the sweep with `Qwen3-1.7B-Base` in fp32, then read the sections
   where shuffles beat the original (`frac_beat_orig` high, `z` low or
   negative) against the text.
3. Sentence-level runs on a base model, reading `sent_best` for paragraphs
   whose best shuffle scores within the noise floor of the original.
4. One larger model (`Qwen3-4B-Base` in fp16 on a T4, or 8B on an L4 or
   A100) on the same sections, compared on nats per character, to see which
   results survive a change of model.
