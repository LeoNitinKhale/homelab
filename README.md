# Homelab

Personal site on a Hetzner box: IT-admin links, a mnemonic portal, a trading
database, and (later) a health dashboard. Django + DRF serving a vanilla-JS SPA,
backed by two PostgreSQL databases.

> Why it's built this way — the two-database split, the app-per-domain layout,
> and the project constraints — is in [CLAUDE.md](CLAUDE.md). This README is just
> about getting it running.

## Layout

```
config/     settings, db_router (core/ops split), urls
common/     abstract base models (CreatedModel/TimestampedModel) — no tables
mnemonics/  memory pegs, images, phrases          ┐
trading/    trades & performance                  ├─ core DB (homelab_core)
health/     dashboard (stub — models TBD)         ┘
ops/        tasks & review state                  ── ops DB (homelab_ops)
portal/     landing page + SPA shell + /health/
frontend/   templates + static CSS/JS (no bundler)
```

## Getting started

Requires a local PostgreSQL. The dev setup uses a `homelab` role and two
databases (`homelab_core`, `homelab_ops`), already created on this machine.

```bash
# 1. dependencies (project venv)
python -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt   # Windows path

# 2. configure — copy the example and adjust if needed
cp .env.example .env

# 3. build both schemas
python manage.py migrate                    # core DB
python manage.py migrate --database=ops     # ops DB

# 4. run
python manage.py runserver
```

Open <http://localhost:8000> for the portal, `/admin/` for the admin,
`/health/` for the liveness + both-databases check.

A dev superuser `leo` exists (password `changeme123` — change it via
`python manage.py changepassword leo`).

## Databases

The core/ops split is enforced by `config/db_router.py`: the `ops` app's tables
live only in `homelab_ops`, everything else in `homelab_core`. Because
cross-database ForeignKeys are impossible, `ops` models reference core records by
plain id, never an FK. `migrate` (no flag) only builds the core DB; ops needs
`--database=ops`.

## Tests

```bash
python manage.py test
```

Runs against throwaway Postgres databases (`test_homelab_core` /
`test_homelab_ops`) — no SQLite fallback, so local Postgres must be running.
