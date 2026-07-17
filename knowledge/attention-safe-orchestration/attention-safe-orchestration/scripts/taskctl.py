#!/usr/bin/env python3
"""Safe, dependency-free task-file controls for attention-safe orchestration."""

import argparse
import sys
from pathlib import Path

STATUSES = {
    "PLANNING", "RUNNING", "WAITING_EXTERNAL", "WAITING_REVIEW_CAPACITY",
    "NEEDS_HUMAN_DECISION", "READY_FOR_REVIEW", "FAILED_SAFELY", "COMPLETED",
}
REQUIRED_FIELDS = (
    "task_id", "project_name", "repository_path", "worktree_path", "branch_name",
    "conversation_label", "terminal_label", "task_directory", "current_status",
    "current_phase", "next_human_checkpoint", "verification_status",
    "unresolved_blockers",
)
TASK_FILES = ("manifest.yaml", "brief.md", "progress.md", "decisions.md", "evidence.md", "blockers.md", "handoff.md")

def read_flat(path: Path) -> dict[str, str]:
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values

def write_flat(path: Path, values: dict[str, str], dry_run: bool) -> None:
    text = "".join(f"{key}: {value}\n" for key, value in values.items())
    if dry_run:
        print(f"DRY-RUN: would write {path}")
    else:
        path.write_text(text, encoding="utf-8")

def command_init(args: argparse.Namespace) -> int:
    task = Path(args.task)
    if task.exists() and any(task.iterdir()):
        print(f"ERROR: refusing to overwrite populated task directory: {task}", file=sys.stderr)
        return 1
    if args.dry_run:
        print(f"DRY-RUN: would initialize {task}")
        return 0
    task.mkdir(parents=True, exist_ok=True)
    defaults = {
        "task_id": task.name, "project_name": "", "repository_path": "",
        "worktree_path": "", "branch_name": "", "conversation_label": "",
        "terminal_label": "", "task_directory": str(task), "current_status": "PLANNING",
        "current_phase": "intake", "next_human_checkpoint": "none",
        "verification_status": "NOT_RUN", "unresolved_blockers": "none",
    }
    (task / "manifest.yaml").write_text("".join(f"{key}: {value}\n" for key, value in defaults.items()), encoding="utf-8")
    for filename in TASK_FILES[1:]:
        (task / filename).write_text(f"# {filename.removesuffix('.md').replace('-', ' ').title()}\n", encoding="utf-8")
    print(task)
    return 0

def command_validate(args: argparse.Namespace) -> int:
    path = Path(args.manifest)
    if not path.is_file():
        print(f"ERROR: manifest not found: {path}", file=sys.stderr)
        return 1
    values = read_flat(path)
    missing = [key for key in REQUIRED_FIELDS if not values.get(key)]
    if missing:
        print("ERROR: missing required manifest fields: " + ", ".join(missing), file=sys.stderr)
        return 1
    if values["current_status"] not in STATUSES:
        print(f"ERROR: invalid current_status: {values['current_status']}", file=sys.stderr)
        return 1
    print("VALID")
    return 0

def command_transition(args: argparse.Namespace) -> int:
    status = args.status
    if status not in STATUSES:
        print(f"ERROR: unknown status: {status}", file=sys.stderr)
        return 1
    path = Path(args.manifest)
    if command_validate(argparse.Namespace(manifest=path)):
        return 1
    values = read_flat(path)
    values["current_status"] = status
    write_flat(path, values, args.dry_run)
    print(status)
    return 0

def command_review_capacity(args: argparse.Namespace) -> int:
    path = Path(args.registry)
    if not path.is_file():
        print(f"ERROR: registry not found: {path}", file=sys.stderr)
        return 1
    values = read_flat(path)
    try:
        ready = int(values.get("ready_for_review", ""))
        limit = int(values.get("limit_ready_for_review", ""))
    except ValueError:
        print("ERROR: registry requires integer ready_for_review and limit_ready_for_review", file=sys.stderr)
        return 1
    print("WAITING_REVIEW_CAPACITY" if ready >= limit else "READY_FOR_REVIEW")
    return 0

def command_handoff_draft(args: argparse.Namespace) -> int:
    path = Path(args.output)
    if path.exists():
        print(f"ERROR: refusing to overwrite handoff: {path}", file=sys.stderr)
        return 1
    task_id = args.task_id
    content = f"""# {task_id} Handoff

Status: {args.status}

## Result

Pending summary.

## Scope

- Completed:
- Uncompleted:
- Explicitly excluded:

## Acceptance Criteria

| Criterion | Result | Evidence |
| --- | --- | --- |
| Pending | SKIPPED | Pending |

## Verification

- Tests:
- Lint:
- Type check:
- Build:
- Manual checks:

## Autonomous Decisions

- Decision:
- Reason:
- Reversibility:

## Risks and Limitations

- None recorded.

## Human Review Focus

1. Pending.

## Changed Files or Commit Range

- Pending.
"""
    if args.dry_run:
        print(f"DRY-RUN: would write {path}")
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(path)
    return 0

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Initialize and validate attention-safe task files.")
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="initialize a task directory without overwrite")
    init.add_argument("task"); init.add_argument("--dry-run", action="store_true"); init.set_defaults(handler=command_init)
    validate = sub.add_parser("validate", help="validate a flat manifest")
    validate.add_argument("manifest"); validate.set_defaults(handler=command_validate)
    transition = sub.add_parser("transition", help="set a valid task status")
    transition.add_argument("manifest"); transition.add_argument("status"); transition.add_argument("--dry-run", action="store_true"); transition.set_defaults(handler=command_transition)
    capacity = sub.add_parser("review-capacity", help="calculate review status from a registry")
    capacity.add_argument("registry"); capacity.set_defaults(handler=command_review_capacity)
    handoff = sub.add_parser("handoff-draft", help="create a non-overwriting handoff draft")
    handoff.add_argument("output"); handoff.add_argument("task_id"); handoff.add_argument("--status", default="READY_FOR_REVIEW", choices=sorted(STATUSES)); handoff.add_argument("--dry-run", action="store_true"); handoff.set_defaults(handler=command_handoff_draft)
    return parser

def main() -> int:
    args = build_parser().parse_args()
    return args.handler(args)

if __name__ == "__main__":
    raise SystemExit(main())
