# Mnemonics — ticket-based development workflow

How birth/death mnemonic instances are developed through YouTrack. The reference
implementation format and encoding rules live in
[`data/mnemonics/mnemonic_implementations.md`](../../data/mnemonics/mnemonic_implementations.md);
this doc covers the *process* around it.

## Sources of truth

| Artifact | Role |
|---|---|
| `data/mnemonics/mnemonic_implementations.md` | **Canon.** Human-readable, confirmed entries. Nothing lands here without Leo's approval. |
| `data/mnemonics/figures.yaml` | Structured mirror of the canon (+ the controlled `vocabulary:` block). Drives ticket seeding; future DB seed. |
| YouTrack project **Mnemonics** (`MNE`) | The **working/review space** — one ticket per figure. Drafts live here until canonised. |

Leo edits drafts **in the ticket** (YouTrack), not in the files. The files are only
written at canonisation time.

## The gate

Leo is the sole gate. Claude may *propose* a scene into a ticket, but **nothing is
written into `mnemonic_implementations.md` until Leo has moved the ticket to
`Submitted`** (or explicitly asked). A mnemonic only counts once it sticks for Leo.

## State machine

```
Open ── Claude drafts ──▶ AI Proposed ── Leo ──▶ In Progress ──▶ Submitted
                                             └──────────────────▶ Submitted
                                                                     │
                                                        Claude canonises
                                                                     │
                                                     ┌───────────────┴───────────────┐
                                                     ▼                               ▼
                                                 Verified                        Reopened
                                          (written to canon)              (peg/narrative error;
                                                                            nothing written)
```

| State | Meaning | Who sets it |
|---|---|---|
| **Open** | backlog ticket, no scene yet | seed (initial) |
| **AI Proposed** | Claude has drafted a candidate scene into the ticket | **Claude** |
| **In Progress** | Leo is developing / refining it | **Leo** |
| **Submitted** | Leo is happy — the go signal to canonise | **Leo** |
| **Verified** | written/updated in the canon file | **Claude** |
| **Reopened** | Claude found a peg-number or narrative error; wrote nothing | **Claude** |

The traffic-light **status** in the canon (🟢 green / 🟡 amber / 🔴 red) is a separate,
quality axis and is always **Leo's call**. A `Verified` ticket can still be amber.

## Claude's responsibilities

- **Drafting (Open → AI Proposed):** propose birth/death pegs (from the candidates or a
  stronger word, brand names welcome where the first two consonant sounds match), a
  scene tied to the figure's real life, and a derived Position. Set `AI Proposed`. Stop.
- **Canonising (Submitted → Verified/Reopened):** validate that each peg word encodes the
  stated number and that the narrative/history is sound. If good: write/update the entry in
  `mnemonic_implementations.md`, sync `figures.yaml`, refresh the ticket, set `Verified`,
  add a comment. If an error is found (e.g. a peg encoding the wrong number): set
  `Reopened` with a comment and write nothing.
- **Do not** warn about pegs/characters clashing across figures — overlaps are expected.

## Tooling

- `scripts/youtrack_seed.py` — create/refresh tickets from `figures.yaml`.
  - `--dry-run`, `--only completed|backlog|all`, `--limit N`
  - `--update` refreshes summary/description only and **skips tickets in a working state**
    (AI Proposed/In Progress/Submitted/Reopened) so drafts aren't clobbered; `--force` overrides.
  - `--set-state` re-baselines State/Type from status (initial seeding only).
- `scripts/youtrack_review.py` — the review loop.
  - `list [--state Submitted]`, `show <id>`, `set-state <id> <State> [-m msg]`, `comment <id> <text>`
  - state names with spaces need quotes: `set-state MNE-30 "AI Proposed"`

Credentials (`YOUTRACK_URL`, `YOUTRACK_TOKEN`, `YOUTRACK_PROJECT`) live in the gitignored
`.env`.
