# Agent Execution Budget Prompt File Design

**Date:** 2026-07-30  
**Status:** Approved design; implementation plan pending

## Goal

Create a short, reusable prompt file for coding agents that prevents wasteful repeated builds, tests, formatting, and static checks. The prompt must make expensive verification intentional without weakening the final verification expected for meaningful changes.

## Audience and Scope

- Audience: coding agents working in software repositories.
- Primary motivating case: Rust projects with expensive `cargo` builds and test suites.
- Scope: code-change batching, formatting, verification scope selection, and the decision to repeat slow commands.
- Out of scope: task planning, autonomous agent orchestration, database/data-retrieval constraints, CI configuration, and language-specific command catalogs beyond a short Rust example.

## Artifact

Create `knowledge/agent-execution-budget/agent-execution-budget.md` as a directly copyable instruction fragment for a project's `AGENT.md` or `CLAUDE.md`.

Update the root `README.md` with a link and one-sentence description.

## Content Design

Keep the prompt under roughly 40 lines and organized as five concise sections:

1. **Verification budget principle** — Slow builds, tests, lints, and static checks must provide incremental validation evidence; they are not a default ritual after every edit.
2. **Default execution order** — Batch related edits, format, run the smallest useful verification, then run final broad verification only when warranted.
3. **Verification scope** — Local implementation changes receive compile checks or targeted tests; shared/public changes receive affected module/package checks; dependency, feature, build configuration, or cross-module changes may require full verification.
4. **Repeat gate** — Before re-running a slow command, identify the change and newly introduced risk since the prior run. Reuse the prior result when no relevant risk changed. Formatting alone normally does not warrant re-running behavioral tests.
5. **Rust example and anti-pattern** — Show `cargo fmt`, `cargo check`, targeted `cargo test`, and final `cargo test`; explicitly reject the default sequence `implementation → cargo test → cargo fmt → cargo test`.

## Expected Behavior

The agent should explain its chosen verification command only when a slow command is warranted or it deliberately skips/reuses a prior expensive result. The prompt must not require a verbose per-command audit log for ordinary work.

## Acceptance Criteria

- The file is short enough to embed in project instructions.
- It clearly requires a risk-based reason before repeating a slow command.
- It provides an actionable Rust workflow without making Rust a requirement.
- It distinguishes focused checks from broad final verification.
- The repository README links to the new knowledge item.
