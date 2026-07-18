# Deployment

The homelab runs on a single Hetzner box, provisioned by
[`ansible/deploy_homelab.yml`](../ansible/deploy_homelab.yml). One playbook, run
from your laptop, brings a fresh Ubuntu server to a working state.

## What the playbook does

| Play | Provides |
|------|----------|
| 1 Base setup | swap, apt packages, UFW (22/80/443), SSH hardening |
| 2 Docker | Docker engine + compose plugin |
| 3 Caddy | reverse proxy + automatic HTTPS: `khale.net → :8000` (app), `tasks.khale.net → :3456` (Vikunja) |
| 4 PostgreSQL | `homelab` role + `homelab_core` / `homelab_ops` databases |
| 5 Redis | Redis server |
| 6 Containers | Vikunja (tasks) via docker-compose |
| 7 Deploy app | checkout → venv → `.env` → migrate core+ops → systemd `homelab.service` running `runserver` on `127.0.0.1:8000` |

Caddy terminates TLS and proxies to the Django app, which runs on plain HTTP on
localhost. The app is single-user, so it uses `manage.py runserver --insecure
--noreload` (no Gunicorn) — see CLAUDE.md.

## Prerequisites

1. **Ansible** on your control machine, plus the docker collection:
   ```bash
   ansible-galaxy collection install community.docker
   ```
2. **DNS** — `khale.net` (and `tasks.khale.net`) A-records pointing at the
   server. Caddy needs these resolvable to issue Let's Encrypt certs.
3. **SSH access** to the server as `leo` (the inventory sets
   `ansible_ssh_private_key_file`).
4. **A GitHub deploy key on the server** — Play 7 checks out the *private* repo
   as user `leo`, so `~leo/.ssh` needs a key with read access to
   `LeoNitinKhale/homelab`:
   ```bash
   # on the server, as leo:
   ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
   cat ~/.ssh/id_ed25519.pub   # add to GitHub repo → Settings → Deploy keys (read-only)
   ```

## Secrets

Real secrets live in **`ansible/secrets.yml`** (gitignored). Create it from the
example and fill in real values:

```bash
cp ansible/secrets.yml.example ansible/secrets.yml
# then edit ansible/secrets.yml:
#   db_password        — password for the homelab Postgres role
#   django_secret_key  — python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

Plays 4 (Postgres) and 7 (Deploy app) load this via `vars_files`. Non-secret
settings (hostnames, paths, repo URL) stay in `ansible/inventory.ini`.

> **⚠️ Rotate the old DB password.** An earlier commit tracked `db_password` in
> `inventory.ini` in plaintext, so it lives in git history. Set a *new* password
> in `secrets.yml`, and update the Postgres role on the server
> (`ALTER USER homelab WITH PASSWORD '…';`) so the exposed value is dead.

## Running it

```bash
ansible-playbook -i ansible/inventory.ini ansible/deploy_homelab.yml
```

Re-running is safe — every play is idempotent. To run just the app deploy after
a code change:

```bash
ansible-playbook -i ansible/inventory.ini ansible/deploy_homelab.yml \
  --start-at-task="Check out the repository"
```

## Operating the app

```bash
# on the server
sudo systemctl status homelab          # app service
sudo systemctl restart homelab         # after a manual change
sudo journalctl -u homelab -f          # logs

# migrations / management commands (as leo, from /srv/homelab)
.venv/bin/python manage.py migrate
.venv/bin/python manage.py migrate --database=ops
.venv/bin/python manage.py createsuperuser
```

Health check: `https://khale.net/health/` returns `{"status":"ok"}` when the app
and both databases are reachable.

## Notes / TODO

- `runserver` is deliberate for a single-user site. If it ever needs to scale,
  switch Play 7 to Gunicorn + a static-file strategy (WhiteNoise or Caddy
  `file_server` for `/static` and `/media`).
- The Django secret key and DB password are the only secrets; both are in
  `secrets.yml`. Nothing sensitive is committed.
