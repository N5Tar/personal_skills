# Keep System Simple
## Start With a Complete Work Loop

Build and preserve the smallest loop that can complete a real task:

```text
understand the goal → inspect the current state → make a change
→ verify the result → use feedback to choose the next action
```

A long feature list is not a substitute for this loop. Do not add tools, memory, subagents, automation, or abstractions merely because they may be useful later.

## Add Capability for a Concrete Need

Add a capability only when a concrete task cannot be completed safely, reliably, or efficiently without it. Keep the environment and permissions proportional to the task.

## Make Collaboration Trustworthy

Once the loop works, prioritize collaboration infrastructure over additional surface area:

- Make actions, relevant inputs and outputs, changes, and verification evidence observable.
- Keep goals, authority boundaries, and acceptance criteria explicit; do not infer broad authority from a vague request.
- Prefer changes that are controlled, reviewable, and recoverable.
- Preserve essential goals, constraints, and verified facts when summarizing context.
- Leave interrupted work understandable so a person or later agent can resume it safely.

Self-modification under human direction, constraints, and verification is ordinary software work. Do not treat it as permission to define goals, expand authority, or optimize the system autonomously.
