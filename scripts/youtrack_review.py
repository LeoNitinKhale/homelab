#!/usr/bin/env python
"""Review-loop helper for the mnemonics YouTrack tickets.

Supports the ticket lifecycle:
    Open / In Progress   draft worked in the ticket
    Submitted            Leo is happy — go signal for Claude to canonise
    Verified             written into the implementations file (Claude sets this)
    Reopened             Claude found a peg/number or narrative error (Claude sets this)

This tool only reads tickets and moves state / adds comments. Actually writing an
entry into data/mnemonics/mnemonic_implementations.md is done by Claude as a
reasoning step, then it calls `set-state <id> Verified` here. It never writes to
the .md file itself.

Usage:
    python scripts/youtrack_review.py list                 # tickets awaiting action (Submitted)
    python scripts/youtrack_review.py list --state Open     # any state
    python scripts/youtrack_review.py show MNE-30           # full description + comments
    python scripts/youtrack_review.py set-state MNE-30 Verified -m "written to implementations.md"
    python scripts/youtrack_review.py comment MNE-30 "peg 91 -> pin encodes 92, please recheck"
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent))
from youtrack_seed import YouTrack  # noqa: E402

BASE_DIR = Path(__file__).resolve().parent.parent


def get_client() -> tuple[YouTrack, dict]:
    load_dotenv(BASE_DIR / ".env")
    try:
        base = os.environ["YOUTRACK_URL"]
        token = os.environ["YOUTRACK_TOKEN"]
        project = os.environ["YOUTRACK_PROJECT"]
    except KeyError as e:
        raise SystemExit(f"Missing {e} in .env (see .env.example)")
    yt = YouTrack(base, token)
    proj = yt.resolve_project(project)
    return yt, proj


def _state_of(issue: dict) -> str:
    for cf in issue.get("customFields", []):
        if cf["name"] == "State" and cf.get("value"):
            return cf["value"]["name"]
    return "?"


def cmd_list(yt: YouTrack, proj: dict, args) -> int:
    state = args.state
    query = f"project: {{{proj['name']}}} State: {{{state}}}"
    fields = "idReadable,summary,customFields(name,value(name))"
    issues = yt.find_issues(query, fields)
    if not issues:
        print(f"No tickets in state {state!r}.")
        return 0
    print(f"{len(issues)} ticket(s) in state {state!r}:")
    for i in issues:
        print(f"  {i['idReadable']:8} [{_state_of(i)}]  {i['summary']}")
    return 0


def cmd_show(yt: YouTrack, proj: dict, args) -> int:
    fields = (
        "idReadable,summary,description,"
        "customFields(name,value(name)),"
        "comments(author(fullName),text)"
    )
    i = yt.get_issue(args.issue, fields)
    print(f"# {i['idReadable']}  {i['summary']}")
    print(f"State: {_state_of(i)}\n")
    print(i.get("description", "") or "(no description)")
    comments = i.get("comments") or []
    if comments:
        print("\n--- comments ---")
        for c in comments:
            who = (c.get("author") or {}).get("fullName", "?")
            print(f"[{who}] {c.get('text', '')}")
    return 0


def cmd_set_state(yt: YouTrack, proj: dict, args) -> int:
    if args.message:
        yt.add_comment(args.issue, args.message)
    res = yt.set_state(args.issue, args.state)
    print(f"{res['idReadable']} -> State: {_state_of(res)}")
    return 0


def cmd_comment(yt: YouTrack, proj: dict, args) -> int:
    yt.add_comment(args.issue, args.text)
    print(f"commented on {args.issue}")
    return 0


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    parser = argparse.ArgumentParser(description="Mnemonics YouTrack review loop")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="list tickets in a state (default Submitted)")
    p_list.add_argument("--state", default="Submitted")
    p_list.set_defaults(func=cmd_list)

    p_show = sub.add_parser("show", help="show a ticket's full content + comments")
    p_show.add_argument("issue")
    p_show.set_defaults(func=cmd_show)

    p_state = sub.add_parser("set-state", help="set a ticket's State (optional comment)")
    p_state.add_argument("issue")
    p_state.add_argument("state")
    p_state.add_argument("-m", "--message", help="comment to add before the transition")
    p_state.set_defaults(func=cmd_set_state)

    p_comment = sub.add_parser("comment", help="add a comment to a ticket")
    p_comment.add_argument("issue")
    p_comment.add_argument("text")
    p_comment.set_defaults(func=cmd_comment)

    args = parser.parse_args()
    yt, proj = get_client()
    return args.func(yt, proj, args)


if __name__ == "__main__":
    sys.exit(main())
