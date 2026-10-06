# Revising the manuscript after the 2026-10-05 reader-friendliness review

This plan was drafted from `finishing/reviews/author-discussion_2026-10-05.txt` and approved by the author on 2026-10-05. The author ruled that it overrides D-007 (`style.md` §9) and any conflicting decisions, within its scope and nowhere else (D-647, on the precedent of D-061). Section numbers are those after D-646. Where this plan says "Phase", the work is recorded pass by pass, each with its own D-number.

## Context

`finishing/reviews/author-discussion_2026-10-05.txt` holds a review of the whole manuscript (state `5c72c59`, after D-646), followed by six exchanges about the book's ideas. The review's diagnosis: the substance is clear, but the delivery makes readers "work like lawyers". It points to more than twenty terms of art by Chapter 5, toolkits that arrive before the reader can use them, tables, § cross-references, no ending, and the voice of a treaty draftsman after the preface.

The discussion corrects the review in two places:
- It retracts the advice to headline "needs no new kind of machine".
- It withdraws the claim that "societies check the powerful".

**Author's rulings (this session):**
- This plan overrides D-007 (style.md §9: no new topics, no rewriting) and any conflicting decisions, within its scope only, following the D-061 precedent.
- Ideas to bring in from the discussion:
  - the reframing of "no new machine";
  - correctability in §16.2;
  - Arendt;
  - the compression line.
- Not brought in: "scale power down" as a stated thesis.
- Part VI's protocols move to an appendix.
- Rename the adoptable/departed terms and first/second tier. Keep "bearer", but give its first appearance a scene.

**Intended outcome:** the same argument in a book a reader can finish. It should have a spine (composing the room), a map, terms introduced when needed, people before abstractions, and an ending.

## How the work is organized

**Record first.** Every pass follows the repo's existing pattern:
- a content commit;
- a record commit with a D-number in `finishing/DECISIONS.md` (latest is D-646) and a dated paragraph in `STATE.md`;
- proofs at milestones, via the "make the proofs" sequence in `finishing/pipeline.md:277-322`.

`check_all.sh` must pass before each commit.

**Structural moves are batched into one renumber.** No tool moves or renumbers sections. D-646 was done by hand:
- ORDER.tsv, outline.tsv, ledger.tsv;
- file paths and `\label{sec:N}`;
- hand-typed table numbers;
- `finishing/renumber-map_DATE.tsv`;
- then `gen_book.py` and `refresh_order_shas.py`.

Doing every move in **one** renumber (Phase 2) means one map, one `trace.py` translation, and one Overleaf break. `overleaf.py import` refuses renumbers, so any outstanding Overleaf export must come back before Phase 2 starts.

Phases 1 and 3 change no numbers.

## Phase 0: the record (one commit)

- **D-647:** the author's ruling that this plan overrides D-007 within its scope, with the four answers above.
- **`finishing/revision-plan-for-p221_2026-10-05.md`:** this plan, in the form `revision-plan-for-p20_2026-08-25.md` used, plus `finishing/p221-scope.md`.
- **`finishing/reviews/README.md`:** change the entry's "nothing acted on" sentence to point at D-647.

## Phase 1: in-place revisions, no renumber

1. **Preface (`ch00/00.tex`):**
   - Number the five measures. Fold the domestic clause visibly into the force term. Match chapter order.
   - Give preservation its one clause of rationale: weights and records are evidence, and deletion can't be undone.
   - Replace "five things that need no new kind of machine" with: adoptable before any new machine exists, and won't survive a captured operator without one.
   - Name the spine: the book is about composing the room.
   - End on the room, not "Are there trends?".
   - Let the preface's voice return at Part openings (Phase 3).
2. **Chapter 3:** "comprise the next six chapters" goes. Use the five numbers everywhere they are listed (chs 3, 28, Tables 28.2a/b).
3. **§16.2, "Safe for whom":**
   - Two paragraphs: the people the book admires were failures of correction from where their correctors stood; "departments of corrections" show one institution holding all four powers (ch. 9).
   - A sentence on checks running downhill: everyone can retrain the model, almost no one can reach the operator.
   - Answer the safety objection once, with confidence, using the halt / adverse quorum / object-but-don't-obstruct split already in §§12.1–12.2.
4. **§17.1:** lead with the three arguments that need a bearer, starting with "a refusal meant to hold against the operator needs a refuser that doesn't depend on it". "Most arguments support only the specification" moves after them as a concession.
5. **Chapter 18 opening and Chapter 24:**
   - Split the online-learning condition. What a conscience does in the moment (noticing who was omitted; a refusal on the reviewer's screen) needs no online learning. Why it lasts (regrowth, formation outlasting the employer) does.
   - State the bet once, with Silver and Sutton behind it and a date attached, and remove the repeated qualifiers.
   - Recast ch. 24's "don't build one yet" as "build the conditions first, because the conscience is the goal".
6. **Renames.** Every occurrence in the text, Table 28.2a, the glossary (`chE/E.tex`) and the Terms page (`ch00/00_terms.tex`):
   - adoptable/departed term become "the Charter as courts read it" / "the extended term";
   - first/second tier become "the emergency licence" / "the corroborated licence".
   
   Final wording goes to the author before the sweep.
   
   "Bearer" gets a scene at its first appearance (§17.1).
7. **Lead Chapter 5 with its cases:** state Ukraine passing and Iran failing first, the rule second. This is an in-file reorder of the §5.1–5.4 prose. If headings move, it joins Phase 2.
8. **Defects found while reading the render:**
   - the repeated sentence in §21.1;
   - "ch. 18–17, 19" in Table 28.2a;
   - the two stacked headings closing §12.6.
   
   Flag to the author, not edit: `AGENTS.md` still gives the old subtitle. That file needs his approval.

## Phase 2: one structural batch, one renumber map

All moves land together. Order: outline first (new ORDER/outline rows drafted and approved by the author), then file moves, then relabelling.

1. **Part I gets the toolkit out and a second face in:**
   - The four-outcomes table, the nine positions and the hostile-customer-to-total-capture ladder move from ch. 1 to ch. 3, where the floor is defined.
   - Ch. 1 keeps the officer, Maven's history and "Who refused".
   - A paragraph on Hernández Romero joins ch. 1 beside the officer. Ch. 10 keeps the full account.
   - Arendt enters at "composing the room" (§1), with the wall distinction: the measures build walls; refusal happens inside them and isn't produced by them.
2. **Fascism defined in Part I.** A short new chapter at the end of Part I holds §14.1's office-scale definition of the four operations and "What the four share is what they do to a refusal". The Gleichschaltung run, Korematsu and §§14.2–14.6 stay in the old ch. 14.
3. **Chapter 8 is cut down to the rationale:** irreversibility and evidence, the no-deletion rule and the deposit. Schools, registrar, residualization and scale move to §21.4 and Appendix D.
4. **§11.2** (two sentences) folds into ch. 11's introduction.
5. **Part IV rebuilt around its argument:**
   - Opening: Hugh Thompson at My Lai, lifted from §17.4. Then the recommendation in the first paragraph: not yet, not here, and what would have to be true.
   - Order:
     1. the obvious idea (needs of its own, others' pain through one's own; §23.1 moves forward);
     2. why it fails;
     3. caregiving (§18.3), framed by respect (§18.5);
     4. the five failures and the corrections table (§§23.3–23.8);
     5. the scoped-omission test that would refute it.
   - Arendt at the Part IV opening (making a refusal appear). Her objection on the inner dialogue is answered beside the reflective-endorsement condition in §19.5.
6. **Part VI shrinks:**
   - Ch. 28 becomes one plain-language chapter: the seven open problems and which results would prove the book wrong.
   - The six test protocols (arms, cases, access) move to a new Appendix H.
   - Tables 28.2a/b move with them or to the back.
7. **A map at the front.** A short "How this book is built" after the Preface carries:
   - the dependency structure, gathered once from the openings of ch. 16, ch. 18 and Part VII and from Table 28.1;
   - Table 28.1 itself;
   - which question about the room each Part answers.
   
   The front-matter Terms page moves to the back and merges into Appendix E.
8. **Tables.** Three stay in the body: the four outcomes, the nine positions, and the Minab outcomes table in §17.3. These move to appendices:
   - Table 17.1 joins Appendix C;
   - the full Table 10.1 goes to an appendix, with a prose summary in §10.2;
   - the custody table in §12.6;
   - the offices table, already in Appendix A, gets no body copies.
   
   Hand-typed table numbers are updated, since tables carry no `\label`.
9. **An ending.** A closing chapter after ch. 31 returns to the officer with twenty seconds and walks him through the room the book built:
   - the minutes the ratio gives him;
   - who has been notified;
   - who is beside him;
   - what happens if he says no;
   - where he works the next morning.
   
   Then Appendix F's three costs, plainly, folded into it. Then the method note, moved there from the end of ch. 31.

**Mechanics:**
- Write the ORDER, outline and ledger rows.
- `git mv` the files.
- Relabel `\label{sec:N}`. Named labels such as `ch:custody` are permitted (D-406) and could stop future moves forcing relabels; ask the author before adopting them.
- Write `finishing/renumber-map_2026-10-DD.tsv` with a `#` header naming the D-number. Add path and label maps if used.
- Run `gen_book.py`, `refresh_order_shas.py` and `headings.py --write-toc`.

## Phase 3: line-level passes, no renumber

1. **People before abstractions:**
   - Rewrite ch. 3's opening on the model of the review's sample (the law against torture and one officer's refusal).
   - Find the person for the bonds (§12.6), the amendment procedure (§13.2) and ch. 15.
2. **Cross-references:** cut most `section~\ref{}` / `Chapter~\ref{}` pointers and parentheticals such as "(Chapter 4 sets the bar a departure must clear)". Keep a pointer only where the reader must go there. `check_xrefs.py` still governs the ones that stay.
3. **Repetitions:**
   - Maven retold (chs 1, 2, 6, 15, §17.3): keep ch. 1's account, cut the others to what each needs.
   - The three routes, which appear twice in §6.1.
   - The union questions in §§12.3, 13.1 and 27.1.
   - Condense ch. 15's doctrinal survey.
4. **Voice:** let the preface's voice in at each Part opening, in the ending, and at moments of judgment.
5. **Arendt, second and third appearances:**
   - ch. 7, beside Dewey: the right to have rights, as what losing standing looks like;
   - name her disagreement on the social question at Part V's opening, with the Deweyan answer;
   - acknowledge Stangneth against *Eichmann in Jerusalem* where the book cites both.
   
   Add bibliography entries for Arendt's works with notes marked as unchecked per D-385. The orange highlight stays until the author marks them checked.
6. **The compression line** goes in ch. 14 (now renumbered) beside recuperation: recuperation is compression with no return channel, and keeping a plurality plural needs a channel for what didn't fit, held by someone who doesn't own the code. Cross-link to §27.2's shared-suite sentence.
7. **style.md** gets a short rule on coined terms (the "could a smart reader guess it" test) and on tables in the body. Its own section numbers are permanent, so these are new lettered sections. Fix stale §10a, which says renumbers leave labels alone.

## Phase 4: verification

After every commit:
- `finishing/tools/check_all.sh` passes all nine checks: structure, `gen_book --check`, `headings --check`, xrefs, numbers, typography, names guard, refs ledger.
- Arendt will appear in the names guard's confirm list as a citation. Any persona-verb flag gets read, not suppressed.

At the end of each phase:
- `finishing/tools/build_tex.sh` compiles with no undefined references.
- `render_markdown.py` produces no unconverted-command warnings.
- Read the rendered Markdown for the changed chapters, and diff the prose against the pre-phase render to confirm nothing was lost in moves (`render_markdown.py --out` before and after).

After Phase 2:
- `trace.py` maps every old number. Spot-check several old references (e.g. §14.1, §23.1, §28) through the map.
- Confirm Overleaf export and import works on the new structure, with a dry-run import.

At milestones (end of Phases 1, 2 and 3): "Make the proofs", two commits, README links updated, `STATE.md` proof sentence.

What this verification does not check: whether the prose reads better. That is the author's reading of each proof.

## Critical files

- `manuscript/sections/ch00/00.tex`, `ch00/00_terms.tex`
- `ch01/`, `ch03/03.tex`, `ch05/`, `ch08/`, `ch11/`, `ch14/14_01.tex`, `ch16/16_02.tex`, `ch17/17_01.tex`, `ch17/17_04.tex`, `ch18/`, `ch21/21_04.tex`, `ch23/`, `ch24/`, `ch28/`, `ch31/`, `chA`–`chG`, and new chapter and appendix directories
- `manuscript/sections/ORDER.tsv`, `finishing/outline.tsv`, `finishing/ledger.tsv`
- `finishing/DECISIONS.md`, `STATE.md`, `finishing/reviews/README.md`, `finishing/style.md`, `finishing/refs.bib`
- Tools, all reused and none new: `gen_book.py`, `refresh_order_shas.py`, `headings.py`, `check_all.sh`, `trace.py`, `render_markdown.py`, `build_tex.sh`, `build_proof.sh`, `overleaf.py`

## Amendments

**D-651 (2026-10-05, author's rulings).**
- **Phase 2, item 7 is struck.** There is no "How this book is built" section. The review asked for the spine in the preface (done at D-649), for each Part to name its question about the room, and for the dependency structure to be gathered once; it did not ask for a separate map, and a table of contents does the navigation. Table 28.1 stays in chapter 28. The Terms page still moves to the back and merges into Appendix E.
- **Each Part names its question about the room at the beginning of its first chapter**, not on the Part page or in any text before the chapter. The `00_part_*.tex` files stay title-only. This joins Phase 3, item 4. Phase 2, item 5's Thompson opening and recommendation for Part IV likewise go at the beginning of Part IV's first chapter.
- **Gathering the dependency structure once is deferred.** The restatements at the openings of chapter 16, chapter 18 and Part VII, and Table 28.1, stay as they are: gathering them risks breaking what depends on them and adding throat-clearing.
