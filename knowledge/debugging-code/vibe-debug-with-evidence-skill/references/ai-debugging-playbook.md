# AI Debugging Playbook For Vibe Coding

## What this skill is for

Use this skill in a specific pattern: you are operating inside a vibe-coding workflow and are likely to fall into speculative bug fixing instead of disciplined diagnosis.

This skill exists because the default failure mode is predictable:

- you are often strong at local code understanding
- that strength makes it easy to generate convincing but unproven bug explanations
- without explicit constraints, you will often optimize for “produce a patch” instead of “prove the cause”

This skill adds those missing constraints.

## The default AI failure mode

In stubborn bugs, you will often drift into this loop:

1. read a local code region
2. infer a plausible explanation
3. patch the suspected area
4. observe a changed symptom
5. infer a new plausible explanation
6. patch again

This creates the illusion of progress while the real problem remains unclear.

## Step 1: Freeze the symptom, not the theory

Before any repair, capture:

- expected behavior
- actual behavior
- trigger conditions
- whether it is stable or probabilistic
- what changed recently, if known

Bad example:

> I think the reducer resets the window incorrectly.

Good example:

> After sending a new message inside a thread with compacted history, the visible history shrinks immediately and older messages can no longer be pulled upward until re-entering the thread.

The first is a theory. The second is a symptom.

## Step 2: Rebuild the whole behavior path

Identify:

- what the user action is
- what the system contract should be
- which modules participate
- which state is persisted vs derived
- which layers can overwrite visible output

The purpose is to answer:

> Is this bug likely caused by one bad local implementation, or by an unclear or conflicting system boundary?

## Step 3: Classify the problem

### Design problem signals

- repeated local fixes fail
- symptoms cross multiple stages or modules
- a new concept is awkwardly inserted into an old flow
- multiple layers maintain the same visible state
- there is no clear single source of truth

### Implementation problem signals

- ownership is clear
- contract is clear
- the issue is isolated to one transition or condition
- a focused assertion or log can isolate it quickly

### Unknown is valid

Do not force the classification. `unknown` is acceptable until evidence improves.

## Step 4: Turn suspicions into falsifiable hypotheses

Every suspicion must become:

- If hypothesis H is true, then observable X should occur.

Examples of observables:

- request `limit` or `cursor` values
- cache merge decisions
- restore version or invalidation token changes
- in-flight request markers
- first/last rendered message ids
- whether a reset or replacement occurred

If a suspicion has no observable consequence, it is too vague to guide the investigation.

## Step 5: Add observability before repair

Prefer instrumentation at boundaries:

- entry boundary
- request boundary
- state transition boundary
- projection boundary
- render boundary

When collaborating with a human, prefer diagnostics that are easy to copy:

- persistent local storage dumps
- structured logs
- concise snapshots
- stable file-backed traces

Do not rely only on transient console output if the human needs to report evidence back.

## Step 6: Reject hypotheses with evidence

Maintain a small hypothesis table:

| Hypothesis | Expected evidence | Actual evidence | Decision |
| --- | --- | --- | --- |
| state reset wipes history | reset log appears immediately after send | no reset log; projection recalculation appears instead | reject |
| bad paging request | wrong limit/cursor in request | request params are correct | reject |
| two owners rebuild visible messages | store and projection both emit competing visible ranges | confirmed | keep |

A hypothesis is removed because the evidence failed, not because a later patch changed the symptom.

## Step 7: Choose the repair path only after convergence

### If the bug is design-level

Repair in this order:

1. define the single source of truth
2. define ownership clearly
3. remove parallel maintenance paths
4. rewrite the contract if needed
5. implement from the contract down

### If the bug is implementation-level

Repair in this order:

1. patch the owner boundary
2. keep the fix local
3. add regression coverage
4. avoid opportunistic redesign during the same fix

## Step 8: Validate beyond the original symptom

Verify:

- the original path
- neighboring interaction paths
- restore / reload / re-entry paths

Stubborn bugs often appear fixed on the primary button path while remaining broken in restore or continuation paths.

## Why this skill is strict

This method is not trying to make you more expressive. It is trying to make you more disciplined.

Without these constraints, you will often:

- patch too early
- treat plausible explanations as proof
- move between local theories without preserving rejected hypotheses
- broaden the fix before identifying the single source of truth

Treat the skill as a working protocol:

- classify first
- collect evidence second
- patch only after convergence
