# Keep System Simple Prompt Fragment Design

**Date:** 2026-08-05
**Status:** Complete

## Problem and Goal

Coding-agent instructions can grow into a feature checklist that encourages tools, memory, delegation, or automation before a small, trustworthy work loop exists. Create a concise, reusable instruction fragment that keeps an agent focused on the smallest complete loop that produces verifiable work.

## Scope

- Create a directly copyable fragment for project `AGENT.md` or `CLAUDE.md` files.
- Derive its guidance from `knowledge/agent-orchestration/2026-08-05-when-agent-starts-helping.md`.
- Add the fragment to the repository index.

## Non-goals

- Do not prescribe a particular agent framework, tool set, or autonomy model.
- Do not duplicate the slow-verification guidance in Agent Execution Budget.
- Do not turn this into a full project-planning process.

## Requirements

| ID | Requirement |
| --- | --- |
| FR-1 | Define the minimal useful work loop as goal → inspection → change → verification → feedback-driven next action. |
| FR-2 | Require new capabilities only when a concrete task needs them for safe, reliable, or efficient completion. |
| FR-3 | Prioritize observable, controllable, reviewable, and recoverable collaboration once the loop exists. |
| FR-4 | Keep human goals, authority boundaries, and acceptance criteria explicit. |
| FR-5 | Make the fragment directly copyable into `AGENT.md` or `CLAUDE.md`. |
| FR-6 | Link the new knowledge item from the root README. |
| QR-1 | Keep the fragment concise and free of framework-specific assumptions. |
| QR-2 | Preserve the source article's distinction between useful self-modification and unconstrained self-improvement. |

## Acceptance and Verification Plan

| Requirement | Verification |
| --- | --- |
| FR-1–FR-5, QR-1–QR-2 | Read the rendered Markdown and compare its statements to the source article. |
| FR-6 | Confirm the README contains a working relative link to the new file. |
| QR-1 | Count lines and confirm the fragment remains short enough to embed in project instructions. |

## Dependencies, Risks, and Open Questions

- Dependency: the source blog remains the authority for the fragment's intent.
- Risk: duplicating `Agent Execution Budget` would make both instruction files harder to compose; mitigate by referring only to evidence-based verification, not verification cadence.
- Open questions: none.

## Milestones

| Milestone | Requirements |
| --- | --- |
| M1: Create fragment | FR-1–FR-5, QR-1–QR-2 |
| M2: Index and verify | FR-6, all verification-plan entries |

## Verification Record

| Requirement | Evidence | Result | Gap / Next Step |
| --- | --- | --- | --- |
| FR-1 | Fragment lines 5–14 state the complete goal → inspection → change → verification → feedback loop. | Pass | None |
| FR-2 | Fragment lines 16–18 require a concrete safety, reliability, or efficiency need before adding capability. | Pass | None |
| FR-3 | Fragment lines 20–28 require observable, controlled, reviewable, and recoverable collaboration. | Pass | None |
| FR-4 | Fragment line 25 makes goals, authority boundaries, and acceptance criteria explicit. | Pass | None |
| FR-5 | Fragment line 3 identifies direct use in `AGENT.md` or `CLAUDE.md`. | Pass | None |
| FR-6 | `rg` found the README relative link; `test -f` confirmed its target exists. | Pass | None |
| QR-1 | `wc -l` reports 30 lines; the text names no framework or vendor. | Pass | None |
| QR-2 | Fragment line 30 limits self-modification to human direction, constraints, and verification. | Pass | None |
