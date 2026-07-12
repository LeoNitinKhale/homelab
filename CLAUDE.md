# Project: Homelab

## What this is
Personal website running on a Hetzner linux box. Key components are:
- links to IT admin such as Synology, Hetzner, iDrive
- mnemonic portal holding my memory pegs, images and phrases for storage, learning, testing and review
- trading database tracking my trades and performance
- health dashboard - still TBD

## What this is not
Not a public portal and not intended for professional use or scaling up.

## Summary of structure

### Basic setup
Django/Python, Postgres. Single-user, so no Gunicorn — runs on `manage.py runserver`.
Two databases:
- **core** - all critical long-term data such as the memory and trading databases
- **ops** - lighter database with ephemeral data such as tasks, workflows, and spaced-repetition / failed-learning review state

The core/ops split is a database boundary, enforced by a router in `config/db_router.py`
that routes the `ops` app to the ops DB and every other app to core. It is independent of
the app boundary below: all the domain apps are durable data and live in core; only `ops`
lives in the ops DB. Cross-database ForeignKeys are impossible, so `ops` references core
records by plain id, never an FK.

### Repo structure
Durable domains are separate Django apps so tables stay cleanly namespaced (`trading_*`,
`mnemonics_*`, `health_*`) rather than crowding one shared app:
- `common/` — abstract base models (`CreatedModel`/`UpdatedModel`/`TimestampedModel`) and shared utils; creates no tables or migrations of its own
- `mnemonics/` — memory pegs, images, phrases (core DB)
- `trading/` — trades and performance (core DB)
- `health/` — health metrics (core DB); app stubbed, models TBD
- `ops/` — ephemeral operational data: tasks, workflows, review state (ops DB)
- `portal/` — landing page, IT-admin links, and the SPA shell
- `config/` — standard Django config (settings, `db_router.py`, urls, wsgi)
- `frontend/` — templates + static JS/CSS for the SPA (no bundler)
- `assets/` — static images and other assets
- `docs/` — all documentation covering architecture and technical implementation
- `original_data/` - one-off import sheets and scripts. Not required once db set up
- `scripts/` - operational scripts for e.g. backups
- `ansible/` - playbook + inventory for provisioning `dev`/`staging` targets; real secrets in `ansible/secrets.yml` (gitignored, copy from `ansible/secrets.yml.example`) — see `docs/DEPLOYMENT.md`

### Documentation
Suggested, for review:
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT.md
│   ├── TECHNICAL.md
│   ├── SPECIFICATION.md
│   └── RUNBOOK.md

## Constraints
Rules Claude must follow:
- Never commit db backups or .env file
- Prefer the ORM. Raw SQL only in a clearly-marked, read-only reporting query where the ORM is genuinely unwieldy — never for writes
- Don't refactor unrelated parts of a file without checking first
- New models needing `created_at`/`updated_at` must inherit the abstract bases in `common` (`CreatedModel`/`UpdatedModel`/`TimestampedModel`) rather than declaring those fields directly
- New models need a migration. Each app needs at least a smoke test; any model with real logic gets its own test
- Never overwrite a migration that has been applied to the Hetzner (production) database. Pre-launch local migrations may be squashed or regenerated freely
