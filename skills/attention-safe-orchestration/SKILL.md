---
name: attention-safe-orchestration
description: Use when coordinating bounded coding work where concurrent agents repeatedly interrupt a human or create confusion between repositories, worktrees, terminals, environments, conversations, or review queues.
---

# Attention-Safe Orchestration

This experimental Wrapper keeps machines concurrent while consuming human attention only
at explicit decision and acceptance checkpoints. It routes work to existing
Superpowers Skills; it does not implement product code or replace their workflows.

## Start and Resume

1. Create or locate `.ai/tasks/<task-id>/`. Before acting after a switch, restart, or
   compression, read `manifest.yaml` and validate it:
   `python3 scripts/taskctl.py validate .ai/tasks/<task-id>/manifest.yaml`.
2. Do not infer repository, branch, worktree, terminal, port, service, or task status
   from the conversation or current shell. A missing/unreliable manifest is a blocker.
3. Persist task identity: task ID, project/repository/worktree/branch, conversation and
   terminal labels, task directory, status/phase, next human checkpoint, verification
   status, unresolved blockers. Record optional port/container/database/env/service data
   whenever allocated.
4. Append recovery-relevant work to `progress.md`. Put meaningful reversible choices in
   `decisions.md` and commands/results in `evidence.md`.

## Route; Do Not Copy

| Condition | Action |
| --- | --- |
| Known architecture impact: ownership, API/protocol, persistence, permission, artifact, lifecycle, compatibility, or multiple packages | **REQUIRED SUB-SKILL:** Use `architecture-first-design`. |
| Requirements are unclear and architecture impact is not yet established | **REQUIRED SUB-SKILL:** Use `superpowers:brainstorming`. If it establishes architecture impact, hand its evidence to `architecture-first-design`; do not create a second specification. |
| Architecture document is `ARCHITECTURE-READY` and no plan exists | **REQUIRED SUB-SKILL:** Use `superpowers:writing-plans`. The plan cites the approved architecture document and does not reopen its decisions without new evidence. |
| Design approved but no plan, without architecture impact | **REQUIRED SUB-SKILL:** Use `superpowers:writing-plans`. |
| A plan runs in this session | **REQUIRED SUB-SKILL:** Use `superpowers:subagent-driven-development`. |
| A plan runs in a separate session | **REQUIRED SUB-SKILL:** Use `superpowers:executing-plans`. |
| Multi-layer bug, multiple plausible owners or sources of truth, earlier patches moved symptoms, or evidence/logs/snapshots are needed before repair | **REQUIRED SUB-SKILL:** Use `vibe-debug-with-evidence`. |
| Evidence classifies a complex bug as `implementation` | **REQUIRED SUB-SKILL:** Use `superpowers:systematic-debugging`, reusing the evidence; then use TDD for the local repair. |
| Evidence classifies a complex bug as `design` and the repair affects ownership, contracts, persistence, protocol, permission, artifact, lifecycle, or compatibility | **REQUIRED SUB-SKILL:** Use `architecture-first-design`. |
| A proven single-owner defect, ordinary test failure, or unexplained result without the complex-bug signals above | **REQUIRED SUB-SKILL:** Use `superpowers:systematic-debugging`. |
| Before any completion claim | **REQUIRED SUB-SKILL:** Use `superpowers:verification-before-completion`. |
| Branch work is verified | **REQUIRED SUB-SKILL:** Use `superpowers:finishing-a-development-branch`. |

If implementation begins, the selected workflow determines worktree, TDD, review, and
verification rules. This Skill adds only identity, attention, state, and handoff policy.
Architecture document state is not the task status: the task remains `PLANNING` while
the architecture track is `DRAFT` or `IN REVIEW`, and becomes `RUNNING` only when
implementation starts.

## State and Attention Policy

Use only `PLANNING`, `RUNNING`, `WAITING_EXTERNAL`,
`WAITING_REVIEW_CAPACITY`, `NEEDS_HUMAN_DECISION`, `READY_FOR_REVIEW`,
`FAILED_SAFELY`, or `COMPLETED`. Run
`python3 scripts/taskctl.py transition <manifest> <status>` before changing a status.

Only `NEEDS_HUMAN_DECISION`, `READY_FOR_REVIEW`, and `FAILED_SAFELY` may
proactively interrupt the human. Routine progress belongs in `progress.md`.

Default to autonomous continuation when the choice is reversible, task-local, private,
safe, evidence-based, inexpensive to verify, and does not change a public API or an
architecture boundary. State the decision, evidence, why no interruption was needed,
and rollback in `decisions.md`.

Stop and aggregate all blockers in `blockers.md` when credentials/permission are absent;
work is destructive or irreversible; acceptance conditions conflict; security/privacy/
legal/compliance risk appears; scope approaches twice the plan; focused repair is
exhausted; or task identity cannot be established. Transition to
`NEEDS_HUMAN_DECISION` or `FAILED_SAFELY`. One question must list why autonomy failed,
options, consequences, and a recommended option.

A possible public API or architecture-boundary change is a routing signal, not by itself
an interruption. Route it to `architecture-first-design`, collect evidence and compare
options while in `PLANNING`, and interrupt only when its `Open Decisions` contains a
choice that existing evidence cannot resolve and that would change a boundary, data
model, lifecycle, compatibility strategy, or verification contract.

## Known Pressure Traps

- “I should ask first” or “for safety I need confirmation” is not a reason to interrupt
  when task files, repository evidence, or a reversible private choice settle the issue.
  Search them, choose, and record the basis.
- “I will report progress first” is not a checkpoint. Write progress instead.
- “May I continue?” is prohibited unless a permitted terminal state requires a human
  choice or acceptance.
- A failed test is not an escalation by itself. Follow the chosen debugging workflow
  until its bounded repair rule requires safe failure.
- A refactor opportunity, naming choice, or private data-structure choice is not a
  human decision.

## Review Backpressure and Handoff

Use a readable registry for phase one. Default limits are `running: 4`,
`needs_human_decision: 1`, and `ready_for_review: 2`. Before announcing review, run
`python3 scripts/taskctl.py review-capacity <registry>`. If capacity is full, transition
to `WAITING_REVIEW_CAPACITY`, complete tests/evidence/docs, and save a handoff draft;
do not rename it `READY_FOR_REVIEW` or interrupt the human.

Create `handoff.md` before `READY_FOR_REVIEW`. It must include result; completed,
uncompleted, and excluded scope; acceptance table with evidence; tests/lint/type/build/
manual verification; autonomous decisions; risks; human-review focus; and changed files
or commit range. Final main-session output contains only task ID, status, handoff path,
commit range, one-line verification, and whether a human judgment risk remains.

## Minimal Example

`brief.md` contains `staging_url=https://staging.example.test`. Read it, use that URL,
record “used brief.md; reversible task-local choice” in `decisions.md` and the command
in `evidence.md`, then continue. Do not ask the human for a value already in task files.
