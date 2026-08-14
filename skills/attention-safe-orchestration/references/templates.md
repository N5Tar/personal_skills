# Task Templates

## Manifest

~~~yaml
task_id: feature-123
project_name: example
repository_path: /absolute/repository
worktree_path: /absolute/worktree
branch_name: feature-123
conversation_label: codex-feature-123
terminal_label: feature-123-shell
task_directory: .ai/tasks/feature-123
current_status: PLANNING
current_phase: intake
next_human_checkpoint: approved-design
verification_status: NOT_RUN
unresolved_blockers: none
port_allocation:
container_name:
database_name:
environment_file:
external_service_dependency:
~~~

## Required Task Files

- `brief.md`: goal, scope, non-goals, acceptance criteria, constraints.
- `progress.md`: dated durable recovery ledger.
- `decisions.md`: decision, evidence, no-interruption rationale, rollback.
- `evidence.md`: exact command, result, skipped checks and reason.
- `blockers.md`: one aggregated list of unresolved blockers.
- `handoff.md`: final review artifact.

## Phase-One Registry

~~~yaml
running: 0
needs_human_decision: 0
ready_for_review: 0
limit_running: 4
limit_needs_human_decision: 1
limit_ready_for_review: 2
~~~

## Handoff

~~~markdown
# <task-id> Handoff

Status: READY_FOR_REVIEW

## Result

One-sentence delivered result.

## Scope

- Completed:
- Uncompleted:
- Explicitly excluded:

## Acceptance Criteria

| Criterion | Result | Evidence |
| --- | --- | --- |
| ... | PASS/FAIL/SKIPPED | path or command |

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

- ...

## Human Review Focus

1. ...

## Changed Files or Commit Range

- ...
~~~
