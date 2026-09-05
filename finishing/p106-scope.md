# P106 — the author's offline-payments manuscript read against §3.3: ten sites in chapters 3 and 11 repaired on rulings, six verified entries

**The instruction.** *the following is a different manuscript i've been working on. I think it might
have relevance to this book's discussion of zkLLM and friends.* The manuscript is a design for
peer-to-peer payments that complete while neither phone is connected; it is not in this repository
and is not cited by the book, on D-049's precedent for a document from another project, and its
public upstream is the author's OptAttest preprint (Cryptology ePrint 2025/974, confirmed live).
Six findings were reported. Rulings followed one at a time: the defect at §3.3:19 *agreed; please
fix*; the boundary case *agreed*; the two convergences *agreed, although I think p2p networks should
be on the page, in light of the state of US public law*; on the grounding point *so what are the
implications for the book?*; on the correction to §3.3:17 *I'm inclined to agree although I wonder
if hardware secure elements are practically easier for developers to leverage when developing on a
mobile phone versus when developing for something that will run in eg a qemu linux vm?*; on the
rollback citations *I'm inclined to agree but I wonder if there isn't a way to do it fully in
software*; then *please apply all of "What the grounding point implies" and "Phones versus a VM, and
doing it in software"*; *proofs please*, twice.

The whole manuscript was read, with the book's §3.1, §3.2, §3.3, §3.5, §3.7, §3.8, §11.1, §11.2 and
§12.2.1 and the three verifiable-training entries read beside it.

## What the manuscript is, as far as the book needs

A double-spend guard built from a primitive the phone already ships, a counter the hardware will
sign at most once per value, consumed in strict succession inside a recursive proof that is anchored
in a registered, bonded genesis record. Prevention rests on that one vendor property; where it
fails, or on hardware that lacks it, the guarantee degrades to detection, attribution to the purse,
and compensation from the bond. Its threat model is the payer's own device in the payer's hands. Its
governance section says in the author's own words what the book's §3.3:17 says about vendors: two
non-optional issuers, and a state compelling one converts the fleet to receive-only.

## The six findings, and what happened to each

- **Where it fits best: the rollback problem §3.5:7 and §3.8:23 name and did not cite.** The
  paper's first threat is snapshot rollback, its answer a counter that will not re-sign a value, and
  its related-work section names the systems literature behind both of the book's sentences. On the
  author's second question, whether the test can be run fully in software, the answer given was yes
  on one condition, an outside party that remembers: one honest witness with a public log gives
  detection, a quorum that co-signs each step gives prevention, hardware buys only doing it offline
  and alone, and a bearer is never offline in that sense. **Applied.** §3.5:7 now says each test
  needs a record the restore does not reach and that two kinds exist, the hardware counter, cited to
  attested append-only memory and the trusted incrementer, and the witness set, cited to
  decentralized witness cosigning; and that a restored system asking either for the last state it
  signed hears of one it does not remember. §3.8:23 gives the instances behind *the instrument
  already exists*: the public log built for certificates and rollback protection kept by a group of
  machines, cited to Laurie 2014 and the enclave paper that built it.
- **Where it corrects the book: §3.3:17's second clause.** The book said hardware attestation
  assumes the machine is not in the adversary's hands. The observer literature the paper descends
  from has designed trusted hardware for a hostile holder since 1992, and the paper's own threat
  model is the device in the adversary's hands. What such hardware assumes is that the holder
  cannot defeat it and that the manufacturer is honest. On the author's first question, phones
  against a VM: phones are easier because the vendor built attestation for the app developer against
  the device's holder, which is the floor's shape; the server equivalent exists and was built for a
  tenant against a cloud operator, so an operator attesting to itself gets nothing; a plain VM with a
  software TPM has no hardware root at all; and physical possession is the access under which server
  enclaves have been broken. **Applied as a recast, not a cut**: the manufacturer clause stands, the
  second clause now says these designs hold against an adversary who controls the software, which is
  where a phone's user stands, and the operator owns the hardware, the access under which AMD's
  confidential-VM design was defeated with a memory module modified for about ten dollars, cited to
  BadRAM.
- **Where it sharpens without changing the conclusion: ungrounded proofs.** The paper refuses any
  proof that does not recurse to a registered genesis, because a single-step proof proves succession
  from a state the verifier has no reason to trust. That is §3.3:19's point about zkLLM in one word.
  Asked for the implications, three were given and **all applied**: §3.3:19 splits the claim that no
  training history can be proved into the pretraining nobody can prove and the sequence after the
  published hash that anyone can record, signed and counted, by a hardware counter or by witnesses,
  with no proof of what any change did, so that a model off the head of the sequence is off the
  record and a restore shows as two successors to one state; the same line states the demand, that
  an inference proof without the sequence back to the published hash establishes only that some
  model answered and the sequence is worth what holds its record; §3.3:21 names two forms that
  depend on no manufacturer, the threshold scheme and the witnessed record; and §3.3:25 says the
  bond's holder and the record's witnesses are selected like the threshold parties unless both sit
  where no party can release the one or rewrite the other, with a pointer to §11.2, which is where
  the chain's root lands.
- **Two convergences.** §11.2:18 already records two claimants on one identifier as a fork, two
  parties, which is what the paper's settlement frontier does. And the paper's bond adds a third
  term to §3.3:23's *expensive and visible*: compensated, from collateral posted in advance.
  **Applied**, with the network the author asked for: §3.3:23 gains the bond; §3.5:42's list of the
  precommitment forms gains it too, so the two lists agree; and §11.2:18, after the sentence that
  public law now supplies no registrar, names two forms outside public law, the trust already there
  and a peer-to-peer network, a ledger kept by many parties in many jurisdictions and a contract that
  runs on it, outside the holding of the removal cases for the same reason as the trust, on which
  the fork rule is a contract and the bond can be held where no party to the deployment can release
  it, and whose reach by a government is a fact about how many nodes there are and where they run.
- **One contrast that cuts the other way.** The paper's first sentence, a thing in the payer's own
  hands that will refuse to do the same thing twice, is the book's subtitle in a domain with one
  act, and its whole security case is that the refusal is not reasons-responsive. **Applied** at
  §3.1:11, before the sentence on a pressure nobody anticipated: where every pressure has been
  anticipated the first method is the right one and a refuser that could be argued with would be a
  defect, the payment device covering one act with its whole misconduct space written down before it
  shipped; the problem the chapter is about begins where that list cannot be closed. Written
  generically, so it needs no entry.
- **A defect found on the way.** §3.3:19 said zkLLM *assumes the weights are a secret from the
  prover*; a prover holds the witness by construction. **Applied**: the secrecy in it is the
  operator's, since the operator is the prover, and the proof keeps the weights from whoever is
  checking and nothing from the party being checked.

## The bibliography

Six entries on instruction, each verified against a dblp listing or the project site for authors,
title, venue, year, pages and DOI before entry; no paper's full text was opened. Attested append-only
memory (SOSP 2007), TrInc (NSDI 2009), ROTE (USENIX Security 2017), decentralized witness cosigning
(IEEE S&P 2016), Laurie's Certificate Transparency (CACM 2014), and BadRAM (IEEE S&P 2025), whose
project site puts the bill of materials at about ten dollars and says Intel's newer designs carry
countermeasures. The notes print in the References and are written as reader-facing text. 308 to
314 entries, all cited.

## Offered and not ruled on

- **§3.5:5's sentence that the bearer's noticing does not run through a quorum somebody else
  selected** sits in soft tension with the witness form now named at §3.5:7. The pricing is still
  done from inside; the memory it consults is outside. Left as written.
- **The GPU clause.** The running model lives on an accelerator, and accelerator attestation is
  newer than the CPU kind. Context in the answer, not a proposed repair; it would need a source.
- **The manuscript itself** stays a pointer. When it has a public posting the reviews README can
  point at it as it points at OptAttest.

## Numbers

**91,749 → 92,304 words, +555**, by `section_stats.py`: §3.1 +75, §3.3 +220, §3.5 +102, §3.8 +38,
§11.2 +120. **185 → 187 pages; 0 undefined references; 20 overfull boxes against P105's 20; 138
sections; 529 → 530 `\ref`**, the one added pointing §3.3 at §11.2. biber 0 errors and the ten
pre-existing month warnings, none on the new entries. Digests refreshed, section stats regenerated,
suite green. **Committed as `48971ca`, the proof pair rebuilt in place at `81804f1` on *proofs
please*.**

## Left undone, named

- **No chapter was read whole.** The check was §3.3 and every site the paper's structure reached,
  read at the target; chapters 1 to 2 and 4 to 14 were touched only where a pointer led.
- **Everything under *Offered and not ruled on*.**
- **The correction at §3.3:17 rests on the paper's own text and on the design goal of remote
  attestation**, not on a source opened this pass, except BadRAM's site for the one instance cited.
