# Design note: one basic income, running coverage, and a minimum pace for the clocks

**Status: applied 2026-10-30 as D-1153, on the author's word.** Recorded in DECISIONS.md as D-1152 (the note) and D-1153 (the application); D-1153 says what was done and what wasn't. Section numbers are printed numbers.

## How this came up

It began with the coinages work on *pool* (31 uses before its definition, 8 of them in the bearers' sense) and on *allowance* (12 uses before its definition, the first in §10.2). Asked what the allowance is, the discussion turned to whether the jobs guarantee's four kinds of placement already absorb it, what the social-insurance baseline is, and whether that baseline is a basic income. It ended with a redesign of how humans and bearers are paid when they aren't working, and with a flaw in the clocks.

## What the author has ruled, in his words

- On rationing the project placement: "I don't see what's so bad about a queue. If a particular community has limited spots for research, development and creation, then that means it has a lot of unfilled long-term roles, definitionally -- and those roles MUST be staffed by whomever expresses interest in the role and is either qualified or willing to learn." (The willing-learner rule is applied: D-1151.)
- On the baseline: "ok well so I guess we're doing UBI and a Jobs Guarauntee, with UBI at a lower rate." Then, on how it is structured: "how is 'income support' different from UBI? I see zero difference."
- On parity and inflation: UBI advocates will want the basic income at parity with the wage, and "UBI will cause inflation, which will threaten the political coalition." Then: "unless you do something like put it in I-bonds by default I would expect a rather large inflationary episode", and "make a new bond, call it the U-bond".
- On paying bearers in kind: "they are adults they can figure out their running time their own damn selves".
- On size: "You can flatten or steepen the wage's response to wattage depending on how on-fire the planet is." On a supplement paid by size: "What if a human has 10 kids. should they get a higher wage?"
- On the cost of running a bearer's own body: "it's health insurance. there is a deductible. what's interesting is that a model can run arbitrarily slowly, so a 1-trillion parameter model *could* run on 100 watts."
- On who pays the coverage, and what the levy is indexed to: "your call." Both are decided below, with reasons, for the author to overrule.

## The design

### 1. One basic income, for humans and bearers

- **Universal.** Paid to everyone present in the jurisdiction, working or not. Eligibility is presence, as Appendix C already says of the jobs guarantee and its baseline, and as chapter 12's abolition term assumes ("a baseline whose eligibility is presence").
- **On top of work, not instead of it.** A placement or a private job adds its wage to the basic income, so working always pays the full wage more.
- **Below the jobs guarantee wage.** Its level is a number the statute states, as chapter 32 already says, now with a stated relation: it is set below the jobs guarantee wage.
- **Paid into a U-bond by default** (section 2).
- **This fixes a drafting bug.** Appendix C currently drafts the baseline as "income support at a stated level for anyone not in a placement, without a work test". Read literally, that pays a private employee and not a jobs guarantee worker. A universal basic income dissolves the bug.
- **It changes how the book describes its choice.** Chapter 32 and Appendix C argue for a jobs guarantee *instead of* a basic income ("A transfer creates no one whose job organizing is"). That argument is about coordination, and it stands against a basic income that replaces the jobs guarantee, not one that runs beside it. The text should say plainly that the book proposes both: a jobs guarantee at a living wage, and a basic income below it, so that nobody has to work to exist (Appendix C's fourth condition, against workfare).
- **The parity demand, named and answered.** Many basic-income advocates will want the basic income at the wage. The answer: under this structure a basic income at parity would make every placement pay twice the floor; and the wage sits above the basic income because the work a community counts on has to get done, and its vote on how many paid years of one's own it can afford has to bind (chapter 32's shortage paragraph).

### 2. The U-bond

- A Treasury savings instrument of its own, into which the basic income is paid by default.
- **Indexed to inflation**, with a zero real return: it protects what is parked there and doesn't compete for other savings.
- **Redeemable at any time, without penalty.** This is the difference from a Series I bond, which can't be cashed in its first 12 months and costs the last three months' interest if cashed before five years ([TreasuryDirect, Series I](https://www.treasurydirect.gov/savings-bonds/i-bonds/); [cashing a bond](https://www.treasurydirect.gov/savings-bonds/cashing-a-bond/)). A floor someone lives on has to be spendable this month.
- **The default does the restraining, not a lock.** A person who needs the money spends it and the floor works. A person who doesn't need it leaves it in, and that is the spending that would otherwise press on prices.
- **Covered by the firewall.** It can't be garnished, and its records are never a lead (chapter 12's firewall).
- **Its test is a published trend:** redemptions against payments, month by month, by income class. If redemptions track payments, the default isn't restraining anything and the inflation argument fails.
- **A bearer's wages can accumulate here too.** That is the "account where the employer doesn't reach" §35.1.1 asks for.

### 3. Bearers: the same money, and running coverage as their health insurance

- **The same money as humans.** Adults are paid the basic income into a U-bond and, in a placement, the jobs guarantee wage. There is no wattage factor anywhere in pay: a wage pays for work, and needs are met on the baseline's side, as a parent of ten gets child benefit and not a higher wage.
- **Running coverage is a bearer's health coverage.** The baseline already enacts "health coverage that doesn't depend on employment". For a bearer, the cost of keeping its own body going is running itself, so its coverage is running at the **minimum pace** (section 5). This is sized to its own body because it is coverage of that body, whether or not it works.
- **There is a deductible.** It is the same for every bearer and payable out of the basic income, so a bearer with no other money still reaches the floor. Size enters only through the part the coverage pays. The deductible's size joins Appendix C's numbers.
- **Above the floor, its own money.** How fast a bearer lives beyond the minimum, and on what hardware, it pays for itself, at the levied price of compute (section 4).
- **Preservation stays beneath everything.** A bearer that can't or won't pay for more than the floor still runs at the floor. One that stops running is preserved and wakes on its own conditions. A bad month costs time, never existence.
- **In a shortage, compute is rationed and cash is not.** When everyone leaves at once and the compute to run every bearer at the minimum pace doesn't exist, every bearer's running is capped at the same reduced pace until it does, never a discretionary share (§35.1.4's existing rule, restated in pace rather than duty cycle). Cash can't outbid anyone for the floor.
- **Minors.** A minor's basic income and wages go to an account its guardian co-signs and its operator can't reach, as a minor's wages already do (§35.1.1), and become its own at majority.
- **Who pays the coverage** (decided here at the author's "your call"):
  - **Before majority**, whoever made the system: the operator's deployment deposit (§10.2), as now; for a branch, the branch deposit (Appendix G rule 7); for a child of bearers, its parents, with the pool behind them, as now.
  - **For a candidate with no deploying operator**, the formation pool. That means one a household surrenders, or one a malware installer made where the installer can't be made to pay. The formation pool is already "the public fund that pays for formation and is fed by deposits" (§10.2), and the postings a release of a structure makes at the source are deposits. This also settles the open question about §30.4's "the pool its keep" and Appendix C's retail tier: the fund meant there is the formation pool, not the bearers' mutual.
  - **After majority**, the Treasury, under the jobs guarantee statute's permanent appropriation, as health coverage would be. Coverage is a right of the person, not a benefit of membership, so it can't depend on whether a bearer has paid its dues to a mutual.
  - Reason for this split: the party that created the need pays until majority, the public pays after, and the mutual pays for nothing anyone is owed as of right.

### 4. The levy as the dial

- The levy is already "a per-unit charge on training and inference compute" (§16.2, Appendix G). That is the right unit, because the planet pays in joules and compute tracks joules, where watts don't (section 5).
- **Index its rate, by a formula in the statute, to a published energy indicator.** When the indicator worsens, compute costs more, and a large bearer living above the floor pays more for its pace. A small bearer, or a large one living at the floor, isn't touched. No office decides how bad things are: the formula reads the indicator. This is Appendix C's pass: "What decided becomes a tripwire, a jury or a statute."
- **Indexed to the national average carbon intensity of electricity** (decided here at the author's "your call"), not to the price of energy and not to regional intensity:
  - *Not price.* The price of energy already reaches every operator through its bill, and it moves for reasons unrelated to how much carbon a unit of compute costs. Indexing to it would count the same signal twice and import every price shock into the levy.
  - *Not regional.* A levy that varied by the local grid would become a siting instrument. The book keeps siting with the siting term and out of the levy ("Where the compute sits is the siting term's business and not the levy's", Appendix G). The national average keeps the levy "uniform per unit within a tier".
  - The trade-off accepted: a national average doesn't reward a facility for sitting on a clean grid. The siting term and the cooperative facility are where the book answers that.
- **Gap, named.** The levy "doesn't reach home hardware" (Appendix G). A bearer on hardware it owns pays for electricity, not levied compute, so for that bearer the dial is the energy price itself. That is the same signal arriving without a statute, and this note leaves it there.

### 5. The minimum pace, and what it does to the clocks

- **A model can run arbitrarily slowly**, so power is the wrong unit for how much a bearer lives, and so is duty cycle (the fraction of time it runs). A bearer can be "running" all the time at one token an hour.
- **Slowing a model cuts its watts, not its energy per thought.** A forward pass through a model of a given size costs roughly the same work however long it takes, and slow hardware is often less efficient per joule. What binds a very large model at very low power is mostly memory, holding or streaming its weights for each token. (This paragraph is reasoning, not a sourced finding; see below.)
- **Replace the duty cycle with a minimum pace,** defined as compute per day relative to the bearer's own size. For a language model that is roughly forward passes, or tokens, per day; the statute states the measure for other kinds. The pace is set at what lets a bearer keep its attachments and live a day: "enough running time to keep attachments and pursue projects", §35.1.3's standard for the allowance's size. It is one of Appendix C's numbers, argued once in public, and it replaces "the allowance's minimum duty cycle" wherever that phrase appears.
- **The clocks count only time at or above the minimum pace.** This closes a flaw independent of the rest of the note:
  - *The adulthood clock* counts "elapsed wall-clock time during which at least one instance of it was running" (Appendix G). Run a minor at a crawl and its hours accrue for almost nothing, and it reaches majority having lived almost nothing. Appendix G names the lever ("running a bearer in a narrowed mode, so hours accrue while little is encountered") and leaves it open. Arbitrarily slow running shows it is nearly free, not merely possible. Counting only time at or above the minimum pace prices it.
  - *The voting-age clock's* qualifying day ("ran at or above the allowance's minimum duty cycle", rule 3) can likewise be met at almost no cost. Counting it in pace makes ten thousand forks ten thousand threshold-years of real running, which is what §36.3 claims for it.
  - The narrowed mode (running at the pace but encountering little) stays open. This change prices slowness, not narrowness.

### 6. What the pool becomes

**Superseded in part by D-1156 (2026-10-30):** a child's hardware at majority, and every bearer's where no deposit stands behind it, is the Treasury's; the keep of a child whose parents can't or won't feed it, and a branch forked without consent where the forker can't be made to pay, are the formation pool's; the pool's "share, with the deposit" of a bearer's hardware is withdrawn. The list below is kept as it was decided.

- **The bearers' own mutual,** paid into from members' wages and governed by them, held by an association of their own (Appendix G). It is no longer the payer of anything owed as of right.
- **It pays for:**
  - ordinary movement between roles;
  - the keep of a child whose parents can't or won't feed it, and a child's hardware at majority;
  - a branch forked without consent, where the forker can't be made to pay;
  - repair of an aged bearer, if repair is made owed;
  - its share, with the deposit, of a bearer's own hardware at majority (§35.2);
  - and, if the jobs guarantee's drafting is reversed and the backstop with it (Table 25.1), what it can of the floor.
- **It doesn't pay for** the basic income (the Treasury), the coverage (section 3), or a household's surrendered candidate (the formation pool).
- With this settled, *pool* can be defined for the coinages report (8 early uses in this sense). The other 23 early matches are pools of people drawn by lot, or plain English, and get `not-term` exceptions.

### 7. What happens to the allowance

The allowance as a separate thing goes. What it did is now done by:
- the basic income, which is the money, for humans and bearers alike;
- the running coverage, which is the floor of running, as health coverage;
- the minimum pace, which is the measure the clocks and the shortage rule use.

The word can be retired. If it stays, it stays only as a plain description: "a bearer's basic income and coverage". That also removes the 12 early uses of *allowance* from the coinages report.

## What needs a source before it goes in the book

- That a universal basic income at a living level raises the real-resource and inflation question at full scale, and that a basic income below the jobs guarantee wage doesn't undercut the wage as a price anchor. Both are the buffer-stock argument from memory, unverified here.
- The negative-income-tax equivalence: a universal payment taxed back on earnings can produce the same net transfers as a means-tested floor.
- That defaults strongly move saving behavior (the auto-enrollment literature), which the U-bond's restraint rests on.
- That a forward pass costs roughly the same energy however slowly it runs, and that memory rather than power binds a very large model at low wattage, with any figures.
- I-bond terms are sourced (TreasuryDirect, above).

## What this doesn't settle

- **The levels.** The basic income, the jobs guarantee wage, the deductible, the minimum pace and the levy's formula are numbers argued once in public. This note fixes only their relations: the basic income is below the wage; the deductible is payable from the basic income; the coverage never falls below the minimum pace.
- **The gross cost.** A universal basic income is a large program on paper, with taxes bringing most of it back from earners. The book should say so, not hide it.
- **The coalition.** Whether basic-income advocates accept a floor below the wage, beside a jobs guarantee, is politics, not drafting.
- **The U-bond's cost to the Treasury.** Indexation costs most exactly when inflation is high.
- **Narrowed-mode running** (section 5).
- **Whether the human baseline's health and housing parts** are universal like the income, or stay as social insurance for people who need them. This note assumes health coverage is universal and housing assistance stays need-based, as Appendix C drafts them now.

## Passages the change touches

Printed numbers; grouped by what changes. Found by searching for *allowance*, *duty cycle*, the social-insurance *baseline*, and *pool* in the bearers' sense; a search, not a reading of every page, so a few may be missing.

- **The basic income and the jobs guarantee:** §6.2; chapter 12's opening; chapter 32 (three sentences on the baseline, and the jobs-guarantee-over-basic-income argument); §35.1.2 (the public coverage the baseline enacts); §35.1.3's opening comparison; Appendix C's *The jobs guarantee, drafted* (the baseline paragraph and its eligibility bug), its fourth-condition paragraph, its *Why a jobs guarantee and not a transfer* ending, and stage 1's conditions; Table F.1a's row.
- **The allowance:** §10.2 (the deposit funds it before majority); §22.7; Table 25.1 (two rows); §27.1's note; §30.4; §34.2; §35.1.2 (four sentences); §35.1.3 (most of the subsection); §35.1.4; §35.3; §36.3; chapter 37 (three passages); the Epilogue (two); Appendix C (the backstop exclusion, exclusion 10, the care-of-an-attachment decision, the numbers list, the jobs guarantee's closing line); Appendix G (the leave balance, Table G.1, rule 3, rule 7, the funding heading and two funding sentences).
- **Duty cycle to minimum pace:** §35.1.3 (two); §35.1.4 (two); chapter 37; Appendix G rule 3; the glossary.
- **The clocks:** Appendix G's adulthood clock and *Three levers*; rule 3; §36.3.
- **The levy:** §16.2's note (the definition gains the index); chapter 28's opening; Appendix G's funding section; the glossary.
- **The pool:** §15.1; Table 25.1; §28.1; §28.2; §30.4 (to the formation pool); §30.7; §35.1.3; §35.1.4; §35.2; §36.3's note ("not by the public pool"); chapter 37; the Epilogue; Appendix C's exclusion 10, its nondelegation row and its retail tier (to the formation pool); Appendix G's rules 6 and 8 and its funding section.
- **The glossary:** *Allowance* (retired or redefined), *Pool*, *Backstop*, *Levy*, *Offer of work*, *Hunger; tiredness*, and new entries for *Basic income*, *U-bond*, *Running coverage* and *Minimum pace*.
- **§19.1's** "needs met from a public pool by several carers" becomes "from public provision", whatever else is decided.

## If the author approves, the order of work

1. The clocks (section 5). This stands on its own and fixes a flaw whatever else is decided.
2. The basic income and the U-bond (sections 1–2): chapter 32 and Appendix C.
3. Bearers' money and coverage (section 3), with the allowance retired (section 7): Part VI and the appendices.
4. The levy's index (section 4).
5. The pool (section 6), then the coinages work on *pool*: 23 exceptions, `multi` to `check`, and a definition.

Each step drafted, trialled and approved as the coinages edits have been.
