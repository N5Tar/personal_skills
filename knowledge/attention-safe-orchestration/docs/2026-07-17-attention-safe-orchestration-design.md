# Attention-Safe Orchestration: Phase 1 Design

## Decision

Create `attention-safe-orchestration` as an experimental personal Skill. It is a
Wrapper and Router around installed Superpowers Skills; it never implements
product code or reproduces a referenced Skill's workflow.

The source of record lives under
`knowledge/attention-safe-orchestration/attention-safe-orchestration/`. After
verification, that exact directory is copied to
`~/.agents/skills/attention-safe-orchestration/` for local discovery.

## Scope and Boundaries

The Skill establishes one durable task identity, persistent state files,
decision and interruption policy, review-queue backpressure, and a concise
handoff contract. It routes phases to existing Superpowers Skills using explicit
`REQUIRED SUB-SKILL` references.

It does not alter any existing Superpowers Skill, manage processes across
machines, provide a GUI or database, or replace planning, debugging, testing,
review, or branch-completion workflows.

## Components

| Component | Responsibility |
| --- | --- |
| `SKILL.md` | Entry conditions, phase routing, identity and interruption rules, status model, and handoff requirements. |
| `references/templates.md` | Manifest, task-file, registry, and handoff templates plus a minimal worked example. |
| `scripts/taskctl.py` | Deterministic operations: initialize without overwrite, validate a manifest, request a state transition, inspect review capacity, and render a handoff draft. |
| `tests/attention-safe-orchestration/` | Five pressure scenarios, baseline transcripts, with-Skill transcripts, evaluator, and comparison report. |

`taskctl.py` has no third-party dependency. Write operations require explicit
commands and support `--dry-run`; it refuses to overwrite existing task files.

## Task State and Data Flow

Each top-level task has `.ai/tasks/<task-id>/manifest.yaml`, `brief.md`,
`progress.md`, `decisions.md`, `evidence.md`, `blockers.md`, and `handoff.md`.
On entry, recovery, or task switching, an agent must read and validate the
manifest before inferring repository, branch, worktree, terminal, port, or
status.

Permitted statuses are `PLANNING`, `RUNNING`, `WAITING_EXTERNAL`,
`WAITING_REVIEW_CAPACITY`, `NEEDS_HUMAN_DECISION`, `READY_FOR_REVIEW`,
`FAILED_SAFELY`, and `COMPLETED`. Only `NEEDS_HUMAN_DECISION`,
`READY_FOR_REVIEW`, and `FAILED_SAFELY` may trigger an unsolicited human
interrupt.

The optional readable registry supplies phase-one review WIP counts only; it
does not provide locking. With default limits (`running: 4`,
`needs_human_decision: 1`, `ready_for_review: 2`), a completed third task is
placed in `WAITING_REVIEW_CAPACITY` and gets a complete handoff draft rather
than a new review interruption.

## Routing Rules

| Condition | Required delegation |
| --- | --- |
| Unclear requirements | `superpowers:brainstorming` |
| Approved design but no plan | `superpowers:writing-plans` |
| Plan executed in the current session | `superpowers:subagent-driven-development` |
| Plan executed in a separate session | `superpowers:executing-plans` |
| Bug, failed test, or unexplained result | `superpowers:systematic-debugging` |
| Before claiming completion | `superpowers:verification-before-completion` |
| Completed branch work | `superpowers:finishing-a-development-branch` |

## Autonomous Decisions and Escalation

An agent continues and records a decision when it is reversible, task-local,
does not change public APIs or architecture, has no security/privacy/permission
or destructive data effect, follows repository evidence, and is inexpensive to
verify. It batches blockers and asks only after searching task files, code,
documentation, and history.

An agent stops safely for missing credentials/permissions, irreversible work,
conflicting acceptance criteria, public API or architecture changes,
security/privacy/legal/compliance risk, scope near twice the plan, exhausted
focused repairs, or an unidentifiable environment. The question includes all
known blockers, options, consequences, and a recommendation.

## Test Design

Before writing `SKILL.md`, create five scenarios: recoverable existing context,
two reversible choices, similar-environment isolation, bounded repeated failure,
and full review queue. Record a baseline run without the new Skill, including
verbatim rationalizations and failure points. The same scenario is then run
against the Skill and evaluated from saved artefacts; unavailable live-agent
execution is explicitly marked and replaced with repeatable static scenario
checks, never reported as a live-agent result.

## Acceptance Evidence

The final verification report must show that all five scenarios have baseline
and with-Skill records; task identity, batching, state transitions, WIP limit,
routing text, and handoff completeness are tested; no installed Superpowers
file changed; all automated tests pass; and every skip is stated with its reason.

## Rollback

Remove the repository topic directory and, if installed, remove only
`~/.agents/skills/attention-safe-orchestration/`. No existing plugin or user
task file is changed by this experiment.
