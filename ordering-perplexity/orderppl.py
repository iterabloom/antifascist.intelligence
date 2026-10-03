"""Perplexity of paragraph and sentence orderings, scored by a causal LM.

Exploratory, and outside the book: nothing in manuscript/ or finishing/ reads
anything this folder writes.

Text comes from finishing/tools/render_markdown.py, the repository's own plain
rendering of the manuscript, and is cleaned for scoring: citation keys,
footnotes and leftover LaTeX are removed, and only prose paragraphs are kept.
Epigraphs, lists, tables and standalone bold heads are dropped. A paragraph
that opens with a bold run-in head keeps the head as plain text.

Scoring. An ordering of units (paragraphs or sentences) is joined with a
separator and scored as one sequence after a fixed prefix: the model's
document-start token, then optionally a context string such as the section
heading. Every token of the joined text is predicted, so two orderings of the
same units are compared on the same text up to the tokens at the joins. Token
NLLs are attributed back to units by character offset; a separator belongs to
the unit that follows it. All NLLs are in nats.
"""
import itertools
import math
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field

import numpy as np

PARAGRAPH_SEP = "\n\n"
SENTENCE_SEP = " "


# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------

def find_repo_root(start=None):
    """Walk up from `start` to the directory holding finishing/tools/render_markdown.py."""
    d = os.path.abspath(start or os.getcwd())
    while True:
        if os.path.isfile(os.path.join(d, "finishing", "tools", "render_markdown.py")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            raise FileNotFoundError("no antifascist.intelligence checkout above " + (start or os.getcwd()))
        d = parent


def render_book(repo_root, out_path):
    """Run the repository's renderer and return the Markdown text."""
    tool = os.path.join(repo_root, "finishing", "tools", "render_markdown.py")
    proc = subprocess.run([sys.executable, tool, "--out", out_path],
                          cwd=repo_root, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError("render_markdown.py failed:\n" + proc.stderr)
    with open(out_path, encoding="utf-8") as f:
        return f.read()


def _drop_braced_command(text, name):
    """Remove every \\name{...}, honouring nested braces."""
    out, i, pat = [], 0, "\\" + name + "{"
    while True:
        j = text.find(pat, i)
        if j < 0:
            out.append(text[i:])
            return "".join(out)
        out.append(text[i:j])
        k, depth = j + len(pat), 1
        while k < len(text) and depth:
            depth += {"{": 1, "}": -1}.get(text[k], 0)
            k += 1
        i = k


# The renderer leaves the second key of a two-key cite with a locator as a
# braced tail: "[@a, ch. 9]{b}" (seen 2026-10-03, section 10.4).
_CITE_RE = re.compile(r"\s*\[[^\[\]]*@[^\[\]]*\](\{[\w:-]+\})?")
_CMD_ARG_RE = re.compile(r"\\[A-Za-z]+\*?\{([^{}]*)\}")
_CMD_RE = re.compile(r"\\[A-Za-z]+\*?")
_BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
_EM_RE = re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])")


def clean_inline(text):
    """Plain prose from one rendered Markdown block."""
    t = _drop_braced_command(text, "footnote")
    t = _CITE_RE.sub("", t)
    for _ in range(3):                      # unwrap \cmd{arg}, innermost first
        t = _CMD_ARG_RE.sub(r"\1", t)
    t = _CMD_RE.sub("", t)
    t = _BOLD_RE.sub(r"\1", t)
    t = _EM_RE.sub(r"\1", t)
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"\s+([,.;:!?)])", r"\1", t)  # space left where a citation was cut
    return t


def _block_kind(block):
    s = block.strip()
    first = s.splitlines()[0]
    if s.startswith("#"):
        return "heading"
    if s.startswith(">"):
        return "quote"
    if s.startswith("|") or " & " in first:
        return "table"
    if re.match(r"([-*+]|\d+\.)\s", s):
        return "list"
    if s == "---":
        return "rule"
    if re.fullmatch(r"\*\*[^*]+\*\*", s):
        return "bold-head"
    if s.startswith("\\part{"):
        return "part"
    if s.startswith("\\"):
        return "latex"
    return "prose"


@dataclass
class Section:
    index: int
    title: str
    level: int                      # 1 = part, 2 = chapter or front matter, 3+ = subsection
    paragraphs: list = field(default_factory=list)
    skipped: dict = field(default_factory=dict)   # block kind -> count dropped

    @property
    def n_words(self):
        return sum(len(p.split()) for p in self.paragraphs)


def parse_book(md):
    """Split rendered Markdown into Sections of cleaned prose paragraphs.

    Everything before the first `##` heading (title, byline, render note) is
    skipped. A `\\part{X}` line opens a level-1 section titled "Part: X".
    """
    sections, cur, in_group = [], None, False
    for block in re.split(r"\n\s*\n", md):
        if not block.strip():
            continue
        # The one table is wrapped in \begingroup ... \endgroup and spans blocks.
        if "\\begingroup" in block:
            in_group = True
        if in_group:
            if "\\endgroup" in block:
                in_group = False
            if cur is not None:
                cur.skipped["table"] = cur.skipped.get("table", 0) + 1
            continue
        kind = _block_kind(block)
        if kind == "heading":
            m = re.match(r"(#+)\s+(.*)", block.strip())
            level = len(m.group(1))
            if level == 1:
                continue
            cur = Section(len(sections), clean_inline(m.group(2)), level)
            sections.append(cur)
        elif kind == "part":
            m = re.match(r"\\part\{([^}]*)\}", block.strip())
            cur = Section(len(sections), "Part: " + m.group(1), 1)
            sections.append(cur)
        elif cur is None:
            continue
        elif kind == "prose":
            text = clean_inline(block)
            if text:
                cur.paragraphs.append(text)
        else:
            cur.skipped[kind] = cur.skipped.get(kind, 0) + 1
    return sections


_SEGMENTER = None


def split_sentences(paragraph):
    global _SEGMENTER
    if _SEGMENTER is None:
        import warnings
        with warnings.catch_warnings():         # pysbd 0.3.4 regexes predate Python 3.12's escape warnings
            warnings.simplefilter("ignore", SyntaxWarning)
            import pysbd
        _SEGMENTER = pysbd.Segmenter(language="en", clean=False)
    return [s.strip() for s in _SEGMENTER.segment(paragraph) if s.strip()]


# ---------------------------------------------------------------------------
# Orderings
# ---------------------------------------------------------------------------

def random_orders(n, k, rng, fix_first=False):
    """Up to k distinct permutations of range(n), none the identity.

    With fix_first, unit 0 stays first (a topic sentence or opening paragraph
    held in place). Fewer than k come back when fewer exist.
    """
    free = list(range(1, n)) if fix_first else list(range(n))
    head = [0] if fix_first else []
    total = math.factorial(len(free)) - 1
    if total <= k:
        orders = [head + list(p) for p in itertools.permutations(free)]
        return [o for o in orders if o != list(range(n))]
    seen, out = {tuple(range(n))}, []
    while len(out) < k:
        o = head + list(rng.permutation(free))
        if tuple(o) not in seen:
            seen.add(tuple(o))
            out.append(o)
    return out


def adjacent_swaps(n):
    """[(i, order with units i and i+1 exchanged)] for each joint."""
    out = []
    for i in range(n - 1):
        o = list(range(n))
        o[i], o[i + 1] = o[i + 1], o[i]
        out.append((i, o))
    return out


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

@dataclass
class Score:
    order: list
    total_nll: float          # nats, summed over every token of the joined text
    n_tokens: int
    unit_nll: np.ndarray      # indexed by ORIGINAL unit index, not position
    unit_tokens: np.ndarray
    n_chars: int

    @property
    def ppl(self):
        return math.exp(self.total_nll / self.n_tokens)

    @property
    def nats_per_char(self):
        """Comparable across tokenizers, unlike totals or perplexity."""
        return self.total_nll / self.n_chars


class Scorer:
    """Token-level NLL under a causal LM, without materialising full logits.

    The LM head runs over at most `chunk_tokens` positions at a time, summed
    across the batch, so a batch of 4,000-token passages with Qwen's 151k
    vocabulary does not need ~2.4 GB of fp32 logits per sequence.
    """

    def __init__(self, model_id, dtype="float32", device=None, max_batch_tokens=16384,
                 chunk_tokens=1024, max_length=None):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.torch = torch
        self.model_id = model_id
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        # Precision is a measurement choice, not only a speed one. Chapter 1 scored
        # alone and in batches of 2 and 4 (2026-10-03) spread by 3.3 nats in bf16
        # and 0.1 in fp16 with Qwen2.5-0.5B, 1.3 in fp16 with Qwen3-1.7B-Base, and
        # 0.002 or less in fp32 with every model tried.
        self.dtype = getattr(torch, dtype) if isinstance(dtype, str) else dtype
        self.tok = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id, dtype=self.dtype, use_safetensors=True).to(self.device).eval()
        self.backbone = self.model.get_decoder()
        self.head = self.model.get_output_embeddings()
        # Qwen's pretraining document separator, whatever the tokenizer calls its eos
        start = self.tok.convert_tokens_to_ids("<|endoftext|>")
        if start is None or start == self.tok.unk_token_id:
            start = self.tok.bos_token_id if self.tok.bos_token_id is not None else self.tok.eos_token_id
        self.start_id = start
        self.pad_id = self.tok.pad_token_id if self.tok.pad_token_id is not None else start
        self.max_batch_tokens = max_batch_tokens
        self.chunk_tokens = chunk_tokens
        self.max_length = max_length or getattr(self.model.config, "max_position_embeddings", None) \
            or getattr(getattr(self.model.config, "text_config", None), "max_position_embeddings", 32768)

    def describe(self):
        n = sum(p.numel() for p in self.model.parameters())
        return "%s: %.2fB params, %s on %s" % (self.model_id, n / 1e9, str(self.dtype).replace("torch.", ""), self.device)

    # -- low level ----------------------------------------------------------

    def _encode(self, text, context):
        prefix = [self.start_id]
        if context:
            prefix += self.tok(context + PARAGRAPH_SEP, add_special_tokens=False)["input_ids"]
        enc = self.tok(text, add_special_tokens=False, return_offsets_mapping=True)
        return prefix, enc["input_ids"], enc["offset_mapping"]

    def _forward_nll(self, seqs):
        """seqs: list of id lists. Returns per-sequence arrays of NLL for positions 1..len-1."""
        torch = self.torch
        L = max(len(s) for s in seqs)
        ids = torch.full((len(seqs), L), self.pad_id, dtype=torch.long)
        mask = torch.zeros((len(seqs), L), dtype=torch.long)
        for i, s in enumerate(seqs):
            ids[i, :len(s)] = torch.tensor(s)
            mask[i, :len(s)] = 1
        ids, mask = ids.to(self.device), mask.to(self.device)
        with torch.inference_mode():
            h = self.backbone(input_ids=ids, attention_mask=mask, use_cache=False).last_hidden_state
            nll = torch.empty((len(seqs), L - 1), dtype=torch.float32, device=self.device)
            step = max(1, self.chunk_tokens // len(seqs))
            for a in range(0, L - 1, step):
                b = min(a + step, L - 1)
                logits = self.head(h[:, a:b]).float()
                nll[:, a:b] = torch.nn.functional.cross_entropy(
                    logits.flatten(0, 1), ids[:, a + 1:b + 1].flatten(), reduction="none").view(len(seqs), b - a)
                del logits
        nll = nll.cpu().numpy()
        out = [nll[i, :len(s) - 1] for i, s in enumerate(seqs)]
        if any(not np.isfinite(o).all() for o in out):
            raise FloatingPointError("non-finite NLL; try dtype=torch.float32 (fp16 overflow is the usual cause)")
        return out

    def token_nll(self, texts, context=None):
        """[(nll per text token, offsets)] for each text, after the fixed prefix."""
        enc = [self._encode(t, context) for t in texts]
        seqs = [p + ids for p, ids, _ in enc]
        too_long = [len(s) for s in seqs if len(s) > self.max_length]
        if too_long:
            raise ValueError("sequence of %d tokens exceeds max_length %d" % (max(too_long), self.max_length))
        results = [None] * len(seqs)
        order = sorted(range(len(seqs)), key=lambda i: -len(seqs[i]))
        i = 0
        while i < len(order):
            L = len(seqs[order[i]])
            n = max(1, self.max_batch_tokens // L)
            batch = order[i:i + n]
            for j, arr in zip(batch, self._forward_nll([seqs[j] for j in batch])):
                p = len(enc[j][0])
                results[j] = (arr[p - 1:], enc[j][2])   # drop predictions of prefix tokens
            i += n
        return results

    # -- orderings ----------------------------------------------------------

    def score_orders(self, units, orders, sep, context=None):
        """Score each ordering of `units`. Returns [Score] in the order given."""
        texts, spans = [], []
        for o in orders:
            parts, sp, pos = [], [], 0
            for k, u in enumerate(o):
                if k:
                    parts.append(sep)
                    start = pos            # separator belongs to the following unit
                    pos += len(sep)
                else:
                    start = pos
                parts.append(units[u])
                pos += len(units[u])
                sp.append((u, start, pos))
            texts.append("".join(parts))
            spans.append(sp)
        out = []
        for o, sp, (nll, offsets) in zip(orders, spans, self.token_nll(texts, context)):
            ends = np.array([e for _, _, e in sp])
            starts = np.array([s for s, _ in offsets])
            which = np.minimum(np.searchsorted(ends, starts, side="right"), len(sp) - 1)
            unit_nll = np.zeros(len(units))
            unit_tok = np.zeros(len(units), dtype=int)
            for (u, _, _), k in zip(sp, range(len(sp))):
                sel = which == k
                unit_nll[u] = nll[sel].sum()
                unit_tok[u] = sel.sum()
            out.append(Score(list(o), float(nll.sum()), len(nll), unit_nll, unit_tok, int(ends[-1])))
        return out

    def isolated(self, units, context=None):
        """NLL of each unit scored alone (after the prefix): [(nll, n_tokens)]."""
        return [(float(n.sum()), len(n)) for n, _ in self.token_nll(list(units), context)]


# ---------------------------------------------------------------------------
# Experiments
# ---------------------------------------------------------------------------

def shuffle_test(scorer, units, sep, k, rng, context=None, fix_first=False):
    """Original order against up to k random orders.

    Returns (original Score, [Score]). delta = shuffled - original, so a
    positive delta means the model finds the original order more probable.
    """
    n = len(units)
    orders = [list(range(n))] + random_orders(n, k, rng, fix_first)
    scores = scorer.score_orders(units, orders, sep, context)
    return scores[0], scores[1:]


def summarize_shuffles(orig, shuffled):
    d = np.array([s.total_nll - orig.total_nll for s in shuffled])
    if len(d) == 0:
        return dict(n_shuffles=0)
    return dict(
        n_shuffles=len(d),
        orig_nll=orig.total_nll,
        orig_ppl=orig.ppl,
        orig_nats_per_char=orig.nats_per_char,
        n_tokens=orig.n_tokens,
        mean_delta=float(d.mean()),
        min_delta=float(d.min()),
        # share of shuffles the model likes at least as well as the original
        frac_beat_orig=float((d <= 0).mean()),
        z=float(d.mean() / d.std()) if d.std() > 0 else float("nan"),
    )


def noise_floor(scorer, units, sep, rng, context=None, batch_sizes=(1, 2, 4, 8)):
    """Spread of the original order's NLL across batch sizes.

    Padding and batch shape change the kernels' arithmetic, so the same text
    can score slightly differently depending on what it is batched with.
    Deltas smaller than the spread are not signal.

    Batch sizes whose tokens would exceed the scorer's `max_batch_tokens` are
    skipped, so the check never asks for more memory than the scoring does.
    """
    n = len(units)
    o = list(range(n))
    companions = random_orders(n, max(batch_sizes) - 1, rng)
    length = scorer.score_orders(units, [o], sep, context)[0].n_tokens + 64
    fits = [bs for bs in batch_sizes if bs == 1 or (bs * length <= scorer.max_batch_tokens
                                                     and bs - 1 <= len(companions))]
    saved = scorer.max_batch_tokens
    scorer.max_batch_tokens = 10 ** 9          # force each call into one batch
    try:
        vals = {bs: scorer.score_orders(units, [o] + companions[:bs - 1], sep, context)[0].total_nll
                for bs in fits}
    finally:
        scorer.max_batch_tokens = saved
    v = list(vals.values())
    return dict(by_batch_size=vals, spread=float(max(v) - min(v)))


# ---------------------------------------------------------------------------
# Plots (matplotlib; light surface)
# ---------------------------------------------------------------------------

BLUE, RED, NEUTRAL = "#2a78d6", "#e34948", "#f0efec"
INK, INK_2, SURFACE = "#0b0b0b", "#52514e", "#fcfcfb"


def _axes(ax, title, xlabel, ylabel=None):
    ax.set_facecolor(SURFACE)
    ax.figure.set_facecolor(SURFACE)
    ax.set_title(title, loc="left", color=INK, fontsize=11)
    ax.set_xlabel(xlabel, color=INK_2)
    if ylabel:
        ax.set_ylabel(ylabel, color=INK_2)
    ax.tick_params(colors=INK_2, labelsize=9)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color("#c9c8c3")
    ax.grid(axis="x" if ax.get_ylabel() == "" else "y", color="#e6e5e1", linewidth=0.6)
    ax.set_axisbelow(True)


def plot_shuffles(orig, shuffled, title, noise=0.0, ax=None):
    """Histogram of shuffled-minus-original NLL; the original sits at 0."""
    import matplotlib.pyplot as plt
    ax = ax or plt.subplots(figsize=(8, 3.2))[1]
    d = np.array([s.total_nll - orig.total_nll for s in shuffled])
    if noise:
        ax.axvspan(-noise, noise, color=NEUTRAL, zorder=0)
    ax.hist(d, bins=min(30, max(5, len(d) // 3)), color=BLUE, edgecolor=SURFACE, linewidth=2)
    ax.axvline(0, color=INK, linewidth=1.5)
    ax.annotate("original order", (0, 1), xycoords=("data", "axes fraction"),
                xytext=(4, -4), textcoords="offset points", va="top", color=INK, fontsize=9)
    _axes(ax, title, "NLL of shuffled order minus original (nats; right = original preferred)", "shuffles")
    return ax


def plot_swaps(swap_df, title, noise=0.0, ax=None):
    """Horizontal bars: NLL change from exchanging paragraphs i and i+1."""
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    n = len(swap_df)
    ax = ax or plt.subplots(figsize=(8, 0.28 * n + 1.2))[1]
    d = swap_df["delta"].to_numpy()
    ax.barh(np.arange(n), d, color=[BLUE if x > 0 else RED for x in d], height=0.7,
            edgecolor=SURFACE, linewidth=2)
    if noise:
        ax.axvspan(-noise, noise, color=NEUTRAL, zorder=0)
    ax.axvline(0, color=INK_2, linewidth=0.8)
    ax.set_yticks(np.arange(n), ["¶%d↔¶%d" % (i + 1, i + 2) for i in swap_df["joint"]])
    ax.invert_yaxis()
    _axes(ax, title, "NLL after swap minus original (nats)")
    ax.legend(handles=[Patch(color=BLUE, label="original order preferred"),
                       Patch(color=RED, label="swapped order preferred")]
              + ([Patch(color=NEUTRAL, label="within noise floor")] if noise else []),
              frameon=False, fontsize=8, ncol=3, loc="upper left", bbox_to_anchor=(0, -0.6 / ax.figure.get_figheight()))
    return ax


def plot_context_gain(gain_df, title, ax=None):
    """Bars: nats per token saved by reading each paragraph after the ones before it."""
    import matplotlib.pyplot as plt
    n = len(gain_df)
    ax = ax or plt.subplots(figsize=(8, 0.28 * n + 1.2))[1]
    ax.barh(np.arange(n), gain_df["gain_per_token"], color=BLUE, height=0.7,
            edgecolor=SURFACE, linewidth=2)
    ax.axvline(0, color=INK_2, linewidth=0.8)
    ax.set_yticks(np.arange(n), ["¶%d" % (i + 1) for i in gain_df["paragraph"]])
    ax.invert_yaxis()
    _axes(ax, title, "NLL alone minus NLL in place, per token (nats)")
    return ax
