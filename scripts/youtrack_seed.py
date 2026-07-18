#!/usr/bin/env python
"""Seed / sync YouTrack tickets for the mnemonics birth-death instances.

One issue per historical figure in ``data/mnemonics/figures.yaml``:
  - completed figures  -> ticket carries the finished scene, pegs and metadata
  - backlog figures    -> ticket carries dates, candidate pegs, facts + a task brief

Idempotent: a local map file (``data/mnemonics/.youtrack_map.json``, gitignored)
records figure-id -> issue so re-runs update rather than duplicate. Nothing here
writes secrets to disk; the token is read from the gitignored ``.env``.

Stdlib only for HTTP (urllib) + PyYAML for the data file.

Usage:
    python scripts/youtrack_seed.py --dry-run          # preview, no writes
    python scripts/youtrack_seed.py                     # create missing tickets
    python scripts/youtrack_seed.py --update            # also update existing
    python scripts/youtrack_seed.py --only backlog      # completed|backlog|all
    python scripts/youtrack_seed.py --limit 3           # cap how many are touched
    python scripts/youtrack_seed.py --tags              # best-effort status tags
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml
from dotenv import load_dotenv

import os

BASE_DIR = Path(__file__).resolve().parent.parent
FIGURES_PATH = BASE_DIR / "data" / "mnemonics" / "figures.yaml"
MAP_PATH = BASE_DIR / "data" / "mnemonics" / ".youtrack_map.json"
SOURCE_REF = "data/mnemonics/mnemonic_implementations.md"

STATUS_EMOJI = {"green": "🟢", "amber": "🟡", "red": "🔴", "none": "⚪"}


# --------------------------------------------------------------------------- #
# YouTrack REST client (stdlib urllib)
# --------------------------------------------------------------------------- #
class YouTrack:
    def __init__(self, base: str, token: str):
        self.base = base.rstrip("/")
        self.token = token

    def _request(self, method: str, path: str, body: dict | None = None):
        url = self.base + path
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Accept", "application/json")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:800]
            raise SystemExit(f"YouTrack {method} {path} -> HTTP {e.code}\n{detail}")

    def get(self, path):
        return self._request("GET", path)

    def post(self, path, body):
        return self._request("POST", path, body)

    def resolve_project(self, wanted: str) -> dict:
        projects = self.get("/api/admin/projects?fields=id,shortName,name")
        w = wanted.strip().lower()
        for p in projects:
            if w in (p["shortName"].lower(), p["name"].lower()):
                return p
        avail = ", ".join(f"{p['shortName']} ({p['name']})" for p in projects)
        raise SystemExit(f"Project {wanted!r} not found. Available: {avail}")

    def create_issue(self, project_id: str, summary: str, description: str) -> dict:
        body = {
            "project": {"id": project_id},
            "summary": summary,
            "description": description,
        }
        return self.post(
            "/api/issues?fields=id,idReadable,summary", body
        )

    def update_issue(self, issue_id: str, summary: str, description: str) -> dict:
        body = {"summary": summary, "description": description}
        return self.post(
            f"/api/issues/{issue_id}?fields=id,idReadable,summary", body
        )

    # ---- best-effort tagging -------------------------------------------- #
    def ensure_tag(self, name: str) -> str | None:
        query = urllib.parse.quote(name)
        found = self.get(f"/api/tags?fields=id,name&query={query}")
        for t in found or []:
            if t["name"].lower() == name.lower():
                return t["id"]
        try:
            created = self.post("/api/tags?fields=id,name", {"name": name})
            return created["id"]
        except SystemExit:
            return None  # no permission to create tags; skip silently

    def apply_tag(self, issue_id: str, tag_id: str) -> None:
        try:
            self.post(f"/api/issues/{issue_id}/tags?fields=id", {"id": tag_id})
        except SystemExit:
            pass


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #
def format_year(year: int, is_bc: bool) -> str:
    if year < 0:
        return f"{abs(year)} BC"
    if is_bc:  # mixed span, e.g. Augustus 63 BC - 14 AD
        return f"{year} AD"
    return str(year)


def date_span(fig: dict) -> str:
    is_bc = bool(fig.get("era_bc"))
    b = format_year(fig["birth_year"], is_bc)
    d = format_year(fig["death_year"], is_bc)
    return f"{b}–{d}"


def summary_for(fig: dict) -> str:
    return f"{fig['name']} ({date_span(fig)})"


def _joined(value) -> str:
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v) for v in value)
    return str(value)


def description_completed(fig: dict) -> str:
    emoji = STATUS_EMOJI.get(fig.get("status", "none"), "")
    lines = [
        f"**Status:** {emoji} {fig.get('status', '')}  ·  **State:** completed",
        f"**Dates:** {date_span(fig)}",
        "",
        "### Pegs",
        f"- **Birth peg:** {fig.get('birth_peg', '')}",
        f"- **Death peg:** {fig.get('death_peg', '')}",
    ]
    if fig.get("century"):
        lines.append(f"- **Century:** {fig['century']}")
    lines += [
        "",
        "### Metadata",
        f"- **Role:** {_joined(fig.get('role', ''))}",
        f"- **Field:** {_joined(fig.get('field', ''))}",
        f"- **Era:** {fig.get('era', '')}",
        f"- **Region:** {fig.get('region', '')}",
        f"- **End:** {fig.get('end', '')}",
        "",
        "### Scene",
        fig.get("scene", ""),
        "",
        "### Position",
        fig.get("position", ""),
    ]
    notes = fig.get("notes") or []
    if notes:
        lines += ["", "### Notes"] + [f"- {n}" for n in notes]
    lines += ["", "---", f"_Source: {SOURCE_REF} · figure #{fig['id']}_"]
    return "\n".join(lines)


TASK_BRIEF = (
    "## Task\n"
    "Build a green-quality birth–death scene following the template in\n"
    f"`{SOURCE_REF}`:\n"
    "- object pegs carry the numbers — birth above waist / in front, "
    "death below / behind\n"
    "- pick one birth peg + one death peg from the candidates (or a stronger word)\n"
    "- fill Role / Field / Era / Region / End\n"
    "- write Scene + Position; connect to the figure's real life or legacy"
)


def description_backlog(fig: dict) -> str:
    lines = [
        f"**Status:** ⚪ no scene yet  ·  **State:** backlog",
        f"**Dates:** {date_span(fig)}",
        "",
        "### Candidate pegs",
        f"- **Birth ({fig.get('birth_peg_num', '?')}):** "
        f"{_joined(fig.get('birth_peg_candidates', ''))}",
        f"- **Death ({fig.get('death_peg_num', '?')}):** "
        f"{_joined(fig.get('death_peg_candidates', ''))}",
        "",
        "### Facts / hooks",
        fig.get("facts", ""),
    ]
    notes = fig.get("notes") or []
    if notes:
        lines += ["", "### Notes"] + [f"- {n}" for n in notes]
    lines += ["", TASK_BRIEF]
    lines += ["", "---", f"_Source: {SOURCE_REF} · backlog · figure #{fig['id']}_"]
    return "\n".join(lines)


def render(fig: dict) -> tuple[str, str]:
    summary = summary_for(fig)
    if fig.get("state") == "backlog":
        return summary, description_backlog(fig)
    return summary, description_completed(fig)


# --------------------------------------------------------------------------- #
# Map file
# --------------------------------------------------------------------------- #
def load_map() -> dict:
    if MAP_PATH.exists():
        return json.loads(MAP_PATH.read_text(encoding="utf-8"))
    return {}


def save_map(m: dict) -> None:
    MAP_PATH.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> int:
    parser = argparse.ArgumentParser(description="Seed YouTrack from figures.yaml")
    parser.add_argument("--dry-run", action="store_true", help="preview only")
    parser.add_argument("--update", action="store_true", help="update existing tickets")
    parser.add_argument(
        "--only", choices=["completed", "backlog", "all"], default="all"
    )
    parser.add_argument("--limit", type=int, default=0, help="cap tickets touched")
    parser.add_argument("--tags", action="store_true", help="apply status tags (best-effort)")
    args = parser.parse_args()

    # Windows consoles default to cp1252; figure names/scenes contain emoji and
    # accented characters, so force UTF-8 output to avoid mid-run crashes.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    load_dotenv(BASE_DIR / ".env")
    try:
        base = os.environ["YOUTRACK_URL"]
        token = os.environ["YOUTRACK_TOKEN"]
        project_name = os.environ["YOUTRACK_PROJECT"]
    except KeyError as e:
        raise SystemExit(f"Missing {e} in .env (see .env.example)")

    if not FIGURES_PATH.exists():
        raise SystemExit(f"Missing {FIGURES_PATH}")
    data = yaml.safe_load(FIGURES_PATH.read_text(encoding="utf-8"))
    figures = data["figures"] if isinstance(data, dict) else data

    if args.only != "all":
        figures = [f for f in figures if f.get("state") == args.only]

    yt = YouTrack(base, token)
    project = yt.resolve_project(project_name)
    print(f"Project: {project['shortName']} ({project['name']})  id={project['id']}")

    id_map = load_map()
    created = updated = skipped = 0
    touched = 0

    for fig in figures:
        key = str(fig["id"])
        summary, description = render(fig)
        existing = id_map.get(key)

        if args.limit and touched >= args.limit:
            break

        if existing and not args.update:
            skipped += 1
            continue

        touched += 1
        if args.dry_run:
            action = "UPDATE" if existing else "CREATE"
            print(f"  [{action}] {summary}")
            continue

        if existing:
            res = yt.update_issue(existing["id"], summary, description)
            updated += 1
            tag_target = existing["id"]
            print(f"  updated {existing.get('idReadable', existing['id'])}: {summary}")
        else:
            res = yt.create_issue(project["id"], summary, description)
            id_map[key] = {"id": res["id"], "idReadable": res.get("idReadable")}
            save_map(id_map)  # save incrementally so a crash never re-creates
            created += 1
            tag_target = res["id"]
            print(f"  created {res.get('idReadable', res['id'])}: {summary}")

        if args.tags:
            status = fig.get("status", "none")
            for tag_name in (f"status:{status}", f"state:{fig.get('state', '')}"):
                tid = yt.ensure_tag(tag_name)
                if tid:
                    yt.apply_tag(tag_target, tid)

    print(
        f"\nDone. created={created} updated={updated} skipped={skipped} "
        f"(of {len(figures)} figures, only={args.only})"
    )
    if args.dry_run:
        print("Dry run — nothing was written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
