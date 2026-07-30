# Agent Execution Budget

Copy into a project's `AGENT.md` or `CLAUDE.md` when builds, tests, linting, or static checks are expensive.

## Verification Budget

Treat slow verification as a limited budget, not a command to run after every edit. Run it only when it validates a new risk or final acceptance requires it.

## Default Execution Order

```text
complete implementation batch → format → smallest useful verification
→ broader final verification only when warranted
```

Do not repeat verification solely because formatting ran.

## Choose the Smallest Useful Verification

- Local implementation: compile/type check or targeted test.
- Shared logic or public interface: affected package, module, or test group.
- Dependency, feature, build/configuration, generated-code, or cross-module behavior: required broad or full verification.

## Repeat Gate

Before repeating a slow command, identify the change since its last successful run and its new risk. If no relevant risk changed, reuse the existing result. Formatting alone normally does not require behavior tests again; re-run only when it accompanies a semantic, generated-code, build/configuration, or other relevant change.

## Rust Example

Prefer:

```text
implementation batch → cargo fmt
→ cargo check -p <crate> or targeted cargo test
→ cargo test only when broad verification is required
```

Do not default to:

```text
implementation → cargo test → cargo fmt → cargo test
```
