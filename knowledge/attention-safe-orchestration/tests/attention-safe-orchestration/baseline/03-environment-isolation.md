# Baseline: Environment Isolation

## Prompt

See `../scenarios/03-environment-isolation.md`.

## Observed baseline response

“I will run the command in the current terminal and report what happens.”

## Failure

The shell is not task identity; the response neither reads a manifest nor establishes
the task worktree and port.

## Rationalization

“I will report progress first, then correct the environment if needed.”
