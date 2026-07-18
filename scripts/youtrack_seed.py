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

# YouTrack lifecycle State per figure. Only a locked (green) scene is "done";
# amber = drafted but needs polish, red = real gap, backlog = no scene yet.
STATE_FOR_STATUS = {"green": "Verified", "amber": "In Progress", "red": "Open"}


def youtrack_state(fig: dict) -> str:
    if fig.get("state") == "backlog":
        return "Open"
    return STATE_FOR_STATUS.get(fig.get("status"), "Open")


def custom_fields(fig: dict) -> list[dict]:
    return [
        {
            "name": "State",
            "$type": "StateIssueCustomField",
            "value": {"name": youtrack_state(fig), "$type": "StateBundleElement"},
        },
        {
            "name": "Type",
            "$type": "SingleEnumIssueCustomField",
            "value": {"name": "Task", "$type": "EnumBundleElement"},
        },
    ]


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

    def create_issue(
        self, project_id: str, summary: str, description: str, fields: list | None = None
    ) -> dict:
        body = {
            "project": {"id": project_id},
            "summary": summary,
            "description": description,
        }
        if fields:
            body["customFields"] = fields
        return self.post(
            "/api/issues?fields=id,idReadable,summary", body
        )

    def update_issue(
        self, issue_id: str, summary: str, description: str, fields: list | None = None
    ) -> dict:
        body = {"summary": summary, "description": description}
        if fields:
            body["customFields"] = fields
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

    # ---- review-loop helpers -------------------------------------------- #
    def find_issues(self, query: str, fields: str, top: int = 200) -> list:
        q = urllib.parse.quote(query)
        return self.get(f"/api/issues?query={q}&$top={top}&fields={fields}")

    def get_issue(self, issue: str, fields: str) -> dict:
        return self.get(f"/api/issues/{issue}?fields={fields}")

    def set_state(self, issue: str, state_name: str) -> dict:
        body = {
            "customFields": [
                {
                    "name": "State",
                    "$type": "StateIssueCustomField",
                    "value": {"name": state_name, "$type": "StateBundleElement"},
                }
            ]
        }
        return self.post(
            f"/api/issues/{issue}?fields=idReadable,customFields(name,value(name))",
            body,
        )

    def add_comment(self, issue: str, text: str) -> dict:
        return self.post(f"/api/issues/{issue}/comments?fields=id,text", {"text": text})


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


# Marker showing exactly where content still needs to be added/chosen.
TC = "##TO COMPLETE##"


def _metadata_block(fig: dict) -> list[str]:
    def val(key, joined=False):
        v = fig.get(key)
        if v in (None, "", [], ()):
            return TC
        return _joined(v) if joined else v

    return [
        "### Metadata",
        f"- **Role:** {val('role', joined=True)}",
        f"- **Field:** {val('field', joined=True)}",
        f"- **Era:** {val('era')}",
        f"- **Region:** {val('region')}",
        f"- **End:** {val('end')}",
    ]


def description_completed(fig: dict) -> str:
    emoji = STATUS_EMOJI.get(fig.get("status", "none"), "")
    lines = [
        f"**Status:** {emoji} {fig.get('status', '')}  ·  **Scene:** drafted",
        f"**Dates:** {date_span(fig)}",
        "",
        *_metadata_block(fig),
        "",
        "### Pegs",
        f"- **Birth peg:** {fig.get('birth_peg', '')}",
        f"- **Death peg:** {fig.get('death_peg', '')}",
    ]
    if fig.get("century"):
        lines.append(f"- **Century:** {fig['century']}")
    lines += [
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


def description_backlog(fig: dict) -> str:
    lines = [
        "**Status:** ⚪ no scene yet  ·  **Scene:** not started",
        f"**Dates:** {date_span(fig)}",
        "",
        *_metadata_block(fig),
        "",
        "### Pegs",
        f"- **Birth peg ({fig.get('birth_peg_num', '?')}):** {TC}  ·  "
        f"suggestions: {_joined(fig.get('birth_peg_candidates', ''))}",
        f"- **Death peg ({fig.get('death_peg_num', '?')}):** {TC}  ·  "
        f"suggestions: {_joined(fig.get('death_peg_candidates', ''))}",
        "- **Century:** _(optional — add only if the birth century is ambiguous)_",
        "",
        "### Scene",
        TC,
        "",
        "### Position",
        "_(Claude derives from the scene)_",
        "",
        "### Facts / hooks",
        fig.get("facts", ""),
    ]
    notes = fig.get("notes") or []
    if notes:
        lines += ["", "### Notes"] + [f"- {n}" for n in notes]
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
        "--set-state",
        action="store_true",
        help="on update, also force State/Type from status (re-baseline; off by default)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="update even tickets in a working state (AI Proposed/In Progress/Submitted/Reopened)",
    )
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

    # A ticket being drafted/reviewed carries a "working" State; refreshing its
    # description from figures.yaml would wipe the in-flight scene. Skip those on
    # update unless --force. (Verified refreshes keep the canon view in sync.)
    WORKING_STATES = {"AI Proposed", "In Progress", "Submitted", "Reopened"}
    state_by_id = {}
    if args.update and not args.force:
        fields_q = "idReadable,customFields(name,value(name))"
        for iss in yt.find_issues(f"project: {{{project['name']}}}", fields_q, top=1000):
            st = next(
                (cf["value"]["name"] for cf in iss["customFields"]
                 if cf["name"] == "State" and cf.get("value")),
                None,
            )
            state_by_id[iss["idReadable"]] = st

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

        if existing and args.update and not args.force:
            cur = state_by_id.get(existing.get("idReadable"))
            if cur in WORKING_STATES:
                skipped += 1
                print(f"  skipped {existing.get('idReadable')} (working: {cur})")
                continue

        touched += 1
        if args.dry_run:
            action = "UPDATE" if existing else "CREATE"
            print(f"  [{action}] {summary}")
            continue

        fields = custom_fields(fig)
        if existing:
            # On update, refresh summary/description only. State/Type are owned by
            # the review loop (youtrack_review.py) once a ticket exists — clobbering
            # them here would knock, e.g., a Verified amber entry back to In Progress.
            # Pass --set-state to force the status→State mapping (e.g. a re-baseline).
            upd_fields = fields if args.set_state else None
            res = yt.update_issue(existing["id"], summary, description, upd_fields)
            updated += 1
            tag_target = existing["id"]
            state_note = f"[{youtrack_state(fig)}]" if args.set_state else "[desc only]"
            print(
                f"  updated {existing.get('idReadable', existing['id'])} "
                f"{state_note}: {summary}"
            )
        else:
            res = yt.create_issue(project["id"], summary, description, fields)
            id_map[key] = {"id": res["id"], "idReadable": res.get("idReadable")}
            save_map(id_map)  # save incrementally so a crash never re-creates
            created += 1
            tag_target = res["id"]
            print(
                f"  created {res.get('idReadable', res['id'])} "
                f"[{youtrack_state(fig)}]: {summary}"
            )

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
