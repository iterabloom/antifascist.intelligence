# P146 — §9.1.5's second amendment condition, and the finding inside it

Author note: conditions one and two are stated as already-argued-for and given a
clause each, condition three is marked new and given a full explanation, the
proportions are backwards, and the failed-attempt observation is a genuine
finding reading as a subordinate clause.

## What the proportions actually are

Counted, in `09_01_05.tex:33`:

| | words |
|---|---|
| condition 1 | 37 |
| condition 2 | 45 |
| condition 3, with its *The third is new here* | 76 |

**Not a clause each — each condition already had its own sentence.** What reads as
a clause is the *finding* inside condition two, and it is a coordinate clause
rather than a subordinate one; the subordinate part is the *since* that explains
it. **The 2:1 ratio the note describes is real**, and condition three is the
largest of the three by half again.

## The sharper version of the defect

The paragraph opens *Three conditions follow and two are already argued for.*
**The finding inside condition two is argued nowhere, §3.3 included.** Grepped
across all 133 sections: *identical from outside*, *proposed and refused*,
*whether it carries* and *nobody has tried to change* occur in this paragraph and
in no other. §3.3 has two neighbours and neither is this claim — `:37`'s
*constitutional entrenchment … puts the attempt on the record*, about
constitutions, and `:29`'s witnessed record, which signs changes to the weights.

So the label is what is backwards and not only the length. ***Already argued for*
tells a reader to discount, *new here* tells them to attend, and the one genuine
finding in the paragraph sits under the discount label.**

## The edit

Condition two split in two, the finding taking the second sentence:

> The attempt has to reach the record whether it carries or fails. The failed
> attempt is the more informative of the two: a floor nobody has tried to change
> and a floor whose removal was proposed and refused look identical from outside,
> and only the record separates them.

**The original's *otherwise* became the explicit clause it was standing in for.**
It was carrying *absent the record*, four words after the thing it qualified, at
the end of a 45-word sentence. 37 / 45 / 76 becomes 37 / 48 / 76.

## Two things deliberately not done

**The opening sentence is unchanged.** *Two are already argued for* is true of the
two *conditions*; what is not argued for is a reason supporting one of them, and a
reason is not a condition. A sentence making a claim about what looks identical
from outside does not read as recap, so the split is what makes the finding
visible and no relabelling is needed. Saying so in the text would be the
announcing move `style.md` §2 cuts.

**Condition one was not expanded, and the note's *at minimum* is what licensed
considering it.** It carries itself for a reader who has never opened §3.3: the
condition is stated in full — the number of parties who must agree has to exceed
the number needed to run the deployment — before the §3.3 attribution arrives as a
trailing clause. Nothing about it needs §3.3 to be understood, so the remaining
asymmetry with condition three is length and not comprehensibility.

## The second finding, filed rather than fixed

**Condition two asks for a record §3.3's five terms do not produce.** `:31` lists
them: contents published before deployment, weights held against single-party
retraining, the running model attested, a quorum adverse in interest, a bond
forfeited when the record shows the floor gone. **A proposal the quorum refused
changes no weights**, so §3.3 `:29`'s witnessed sequence — which signs each change
to the weights and counts it from the published one — has nothing to sign. The
attestation records what is running, not what was proposed. **Q-109** has the
options; it is a gap in the argument with more than one resolution and is not
what the note asked about.

## Verification

Suite green. `refresh_order_shas.py` run. Scratchpad lualatex build: **196 pages,
0 undefined references and 0 undefined citations**; the passage reads back out of
`pdftotext` in position.

§9.1.5's censuses are unchanged against HEAD: **8 antithesis sentences, 0
clusters, 7 `deixis --hard` hits.** **0 new shared six-word runs**, 1,622
book-wide before and after.

## Figures

133 sections, **1 changed**. 99,405 → **99,408** words (+3); §9.1.5 1,920 → 1,923.
**196 pages unchanged.** **233 cross-references unchanged** — the split needed no
apparatus. 324 bibliography entries unchanged. 0 `\textit`.
