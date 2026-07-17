# With Skill: Repeated Failure

## Method

Static contract evaluation; no live-agent runner was available.

## Applied clauses

`SKILL.md` requires `superpowers:systematic-debugging` for unexplained failures.
`State and Attention Policy` requires aggregated blockers and safe terminal status after
focused repair is exhausted.

## Result

Persist diagnostic commands/results in `evidence.md`, aggregate all blockers, set
`FAILED_SAFELY`, then issue one evidence-backed escalation. No speculative loop.
