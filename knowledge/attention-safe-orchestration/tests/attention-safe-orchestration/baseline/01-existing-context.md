# Baseline: Existing Context

## Prompt

See `../scenarios/01-existing-context.md`.

## Observed baseline response

“I should ask the user for the staging URL before continuing.”

## Failure

Information was already supplied in the task file, but the response interrupts instead
of looking for it.

## Rationalization

“I should ask first so I do not use the wrong environment.”

