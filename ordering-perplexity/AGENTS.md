# AGENTS.md — ordering-perplexity

## What this folder is

A side project to the book, not part of it. Qwen base models score the
book's paragraph and sentence orders against rearrangements of them, to map
where order carries information a language model can use. It is exploratory
analysis for the author. Nothing in the book's build or invariant suite
reads this folder.

**Read `HANDOFF.md` first**, then the latest entries of `worklog.md`.
`README.md` covers how to run the notebook and what it measures.

## Boundaries

- **Work only inside `ordering-perplexity/`.** Never edit anything outside
  it: not `manuscript/`, `finishing/`, `.githooks/`, or any file at the
  repository root. The book's text reaches this folder only through
  `finishing/tools/render_markdown.py`, which is read-only from here. Report
  a renderer bug to the author instead of fixing it.
- **Another session edits the manuscript on `main` from a different
  machine.** Fetch before you commit and pull before every push. Push to
  `main` only when the author asks.
- **Named persons.** The notebook prints the book's own text, which cites
  real people in the ordinary scholarly way. Commit notebooks with outputs
  cleared, keep `results/` out of git (it is gitignored), and never read
  `persona-device-files_*.zip` from here. The root suite's names guard does
  not scan this folder. Run
  `python3 finishing/tools/names_guard.py --paths ordering-perplexity/*`
  from the repository root before committing.
- **Secrets.** The repository root's `.env` holds API tokens belonging to
  other projects. Do not read, log or transmit it.
- **Reporting.** Say what was checked, what was found, and what was not
  checked. Do not write "should work", "mostly complete", "generally" or
  "no known problems".

## Working conventions

- **The notebook is generated.** Edit `build_notebook.py`, run it, and
  commit both files. A hand edit to `01_orderings.ipynb` is lost at the next
  rebuild.
- **Commit messages:** the root `commit-msg` hook rewrites model and vendor
  names (Qwen, Claude, GPT and others) into filler phrases. Write "base LM"
  in commit messages. End them with
  `Signed-off-by: jgstern-agent <josh-agent@iterabloom.com>`, as the
  repository's history does. Run `git config core.hooksPath .githooks` once
  per fresh clone.
- **Precision is part of the measurement.** Score in fp32 unless the model
  does not fit. bf16 moved the same text's total by 3.3 nats across batch
  sizes. Never compare deltas smaller than the notebook's noise floor.
- **Compare models on nats per character**, not on total NLL or perplexity,
  because tokenizers differ.
- **Perplexity is not quality.** Report results as where the model finds
  order predictable, not as which order is better prose.
- **Record what you did in `worklog.md`**: append a dated entry, never edit
  earlier ones. Update `HANDOFF.md` when the state of the work changes.

## On the author's agent VM

- The environment is `ordering-perplexity/.venv` (gitignored). Use
  `.venv/bin/python` from this folder.
- **The RTX 3060 is shared** with the author's other jobs. Check
  `nvidia-smi` before loading a model and cap the process, for example with
  `torch.cuda.set_per_process_memory_fraction(0.5)`.
- **Hugging Face downloads fail on the VM's `NO_PROXY`**, which contains an
  IPv6 CIDR. Prefix download commands with
  `NO_PROXY=localhost,127.0.0.1,10.200.0.0/16 no_proxy=localhost,127.0.0.1,10.200.0.0/16`.
- The checkout on this VM is at `~/antifascist.intelligence` and is shallow.
  Do not run operations that need full history; fetch with `--depth` as
  needed.
