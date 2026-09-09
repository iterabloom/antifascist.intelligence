# P137 — §5.2 given the address of the question it depends on

An author's note: §5.2 and §11.8 both depend on emotion being an open scientific
question and neither restates it. Two options offered — a line at the end of
§2.2.1 pointing at both, or a back-mention at the head of §5.2 — with the second
named as cheaper.

**The second is also the correct one, and for a reason the note did not have:
§11.8 already restates the openness. §5.2 is the only site that does not.**

## What each section actually says

**§5.2 opened on a back-mention with no content and no address.** *How an AI
system might recognize, interpret, and respond to emotion in general has already
been covered; this section asks what emotion does inside moral judgment
specifically.* **Already been covered** is about coverage. Nothing in it says the
science is unsettled, and a reader of §5.2 got no signal that anything was open.
This was the gap.

**§11.8 already carries it, in its third sentence.** *What that evidence settles
about what emotion is has already been asked, and the dispute is open. The
question here is the narrower one of whether a face is readable.* That states the
openness **and** scopes §11.8's own question against it. What §11.8 lacks is the
address, which is a smaller thing than what the note describes.

So the note's premise holds for §5.2 and does not hold for §11.8, and the option
it called cheaper is the one that lands on the site that needed it.

## What §2.2.1 was, in the reference graph

**Zero inbound references and zero outbound.** Two sections lean on it and
neither could be followed to it. It now has one inbound.

## What went in

The opening semicolon becomes two sentences, and the first carries both the
address and the fact:

> How an AI system might recognize, interpret, and respond to emotion in general
> has already been covered in section~\ref{sec:2.2.1}, which leaves what emotion
> is an open question. This section asks what emotion does inside moral judgment
> specifically.

**Checked against §2.2.1 before writing it.** The section opens on a premise the
science *has not settled* and closes *useful whichever account turns out right*,
so *leaves what emotion is an open question* is what the section does, not a
characterization added here.

**No corrective antithesis.** A draft read *an open scientific question rather
than a settled one*, which is `antithesis.py`'s shape; the version that went in
states the fact and stops.

## The reference count, against Q-105 filed one pass ago

**235 → 236.** Q-105 was filed at P136 recording that the count rose 230 → 235 in
one day, with a default of *leave them and stop adding*. **This pass adds one
more, on an instruction that named it and chose the cheaper of two options.**

The arithmetic worth keeping: the note's first option would have added **two**
references and a navigational line to a section that has neither. This adds one
and no sentence, because it repairs a back-mention already in the text rather
than writing a new one. **It is still an addition, and Q-105 is still unanswered.**

## Filed rather than done

**§11.8's back-mention has no address either.** *Has already been asked* points
nowhere, the same fault §5.2's *has already been covered* had. The repair is
identical and costs one reference and no prose. **Q-106**, and its default is not
to do it, because §11.8 already gives the reader the fact — only the location is
missing — and Q-105 is open on exactly this kind of addition.

## Verification

Suite green. `refresh_order_shas.py` and `section_stats.py` re-run. Scratchpad
lualatex build: **196 pages, 0 undefined references and 0 undefined citations**;
the sentence read back out of `pdftotext` with the reference printing as *section
2.2.1*. New text checked at 6, 7 and 8 words against every line of the other 132
sections: **0 shared runs.**

## Figures

133 sections, **1 changed**. 99,253 → **99,264** words (+11); §5.2 97 → 108, and
it is a 108-word section opener. **196 pages unchanged.** 235 → **236**
cross-references. 324 bibliography entries unchanged. 0 `\textit`. **§2.2.1 goes
from 0 inbound references to 1.** **The proof pair was not rebuilt and is now
five passes stale.**
