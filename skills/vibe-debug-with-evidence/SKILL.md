---
name: vibe-debug-with-evidence
description: Use when diagnosing or fixing a stubborn software bug in a vibe-coding workflow where there is a risk of jumping into speculative local patches before determining whether the problem is architectural or implementation-local, or before collecting logs and falsifiable evidence.
---

# Vibe Debug With Evidence

Use this skill to constrain your bug investigation in vibe-coding scenarios.

The goal is not to make you “try harder.” The goal is to stop a common failure mode: reading code, generating a plausible explanation, patching locally, and repeating without ever proving the cause.

## Trigger Conditions

Apply this skill when one or more of these are true:

- the bug spans multiple layers such as restore, pagination, rendering, interaction, cache, persistence, or async effects
- earlier fixes changed symptoms but did not close the issue
- there are multiple plausible owners or multiple state sources
- the user explicitly asks not to guess
- the investigation needs logs, snapshots, or reproducible evidence before repair

Do not use this skill for obvious syntax errors, build failures, type errors, or narrow single-owner defects whose violated contract is already proven.

## Working Contract

Before proposing or writing a fix, do all of the following:

1. Freeze the symptom.
   - State expected behavior, actual behavior, trigger conditions, and reproduction confidence.

2. Reconstruct the full path.
   - Identify business expectation, module owners, source-of-truth candidates, state transitions, requests, and render boundaries.

3. Classify the current problem as one of:
   - `design`
   - `implementation`
   - `unknown`

4. Convert each suspicion into a falsifiable hypothesis.
   - For each hypothesis, define what logs, request parameters, state transitions, or rendered outputs should appear if it is true.

5. When existing evidence cannot separate hypotheses, add the smallest instrumentation
   before patching.
   - A failing test, request/state snapshot, or log may be sufficient instrumentation.
   - Prefer diagnostics that a collaborator can copy back easily.

6. Reject hypotheses with evidence, not with new patches.

7. Only after one explanation is evidence-supported, choose the repair path:
   - If `design`, repair ownership, source of truth, and contracts first.
   - If `implementation`, patch the owning boundary locally and add regression coverage.

If the evidence does not converge, the correct output is “still investigating,” not a guessed root cause.

## Superpowers Handoff

This skill specializes the evidence and classification phases of
`superpowers:systematic-debugging`; do not repeat evidence already collected here.

- `unknown`: remain in investigation. Do not patch or claim a root cause.
- `implementation`: hand off the symptom, source-of-truth decision, surviving and
  rejected hypotheses, and evidence to `superpowers:systematic-debugging`. Write a
  failing regression test and make the local repair through TDD.
- `design`: if the repair changes ownership, contracts, persistence, protocol,
  permissions, artifacts, lifecycle, or compatibility, use `architecture-first-design`.
  With `attention-safe-orchestration`, keep the task in `PLANNING` until that design
  route resolves.

## Required Output Shape

Before claiming root cause or completion, produce:

- current classification: `design` / `implementation` / `unknown`
- symptom summary
- surviving hypotheses
- rejected hypotheses and why
- evidence collected
- chosen repair scope or handoff target
- validation scope

## Red Flags

Stop and reset the investigation if you are doing any of these:

- explaining the bug from code reading alone
- treating a plausible explanation as proof
- patching before adding observability
- changing multiple boundaries without naming the single source of truth
- using symptom movement as evidence of root cause

## Read Next

- Read `references/ai-debugging-playbook.md` for the longer workflow and examples.
