# Agent Execution Budget Prompt File Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a short, copyable coding-agent prompt that prevents redundant expensive verification and document it in the repository index.

**Architecture:** Create a single focused Markdown prompt card under `knowledge/agent-execution-budget/`. It defines a risk-based verification budget, a default execution sequence, scope-selection rules, a repeat gate, and a Rust example. Link the card from the existing root knowledge index.

**Tech Stack:** Markdown, Git.

---

## File Structure

- Create: `knowledge/agent-execution-budget/agent-execution-budget.md` — Copyable instruction fragment for `AGENT.md` or `CLAUDE.md`.
- Modify: `README.md` — Adds the new knowledge topic and direct link.

### Task 1: Create the execution-budget prompt card

**Files:**
- Create: `knowledge/agent-execution-budget/agent-execution-budget.md`
- Test: `git diff --check`

- [ ] **Step 1: Write the prompt file**

Create `knowledge/agent-execution-budget/agent-execution-budget.md` with this content:

```md
# Agent Execution Budget

Copy this into a project's `AGENT.md` or `CLAUDE.md` when builds, tests, linting, or static checks are expensive.

## Verification Budget

Treat slow builds, tests, lints, and static checks as a limited verification budget, not commands to run after every edit. Run an expensive command only when it validates a new risk or when final acceptance requires it.

## Default Execution Order

For a related batch of changes:

```text
complete the implementation batch
→ format
→ run the smallest useful verification
→ run broader final verification only when warranted
```

Do not verify before formatting and then repeat the same verification solely because formatting ran.

## Choose the Smallest Useful Verification

- Local implementation change: compile/type check or targeted test.
- Shared logic or public interface change: verify the affected package, module, or test group.
- Dependency, feature, build/configuration, generated-code, or cross-module behavior change: run the required broad or full verification.

## Repeat Gate

Before repeating a slow command, identify the change made since its last successful run and the new risk that change introduces. If no relevant risk changed, reuse the existing result instead of rerunning the command.

Formatting alone normally does not require behavior tests to run again. Re-run only when formatting accompanies a semantic, generated-code, build/configuration, or other relevant change.

## Rust Example

Prefer:

```text
implementation batch
→ cargo fmt
→ cargo check -p <crate> or targeted cargo test
→ cargo test only when the change requires broad verification
```

Do not default to:

```text
implementation → cargo test → cargo fmt → cargo test
```
```

- [ ] **Step 2: Check the file is concise**

Run:

```bash
wc -l knowledge/agent-execution-budget/agent-execution-budget.md
```

Expected: at most 45 lines, excluding blank-line variations introduced by Markdown rendering.

- [ ] **Step 3: Check Markdown whitespace**

Run:

```bash
git diff --check -- knowledge/agent-execution-budget/agent-execution-budget.md
```

Expected: no output and exit code `0`.

- [ ] **Step 4: Commit the prompt card**

```bash
git add knowledge/agent-execution-budget/agent-execution-budget.md
git commit -m "docs: add agent execution budget prompt" \
  -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

### Task 2: Add the prompt card to the repository index

**Files:**
- Modify: `README.md:6` — Insert a new topic before `system-architecture-review`.
- Test: `git diff --check`

- [ ] **Step 1: Add the README section**

Insert the following Markdown immediately before the `### [system-architecture-review]` heading:

```md
### [agent-execution-budget](./knowledge/agent-execution-budget/)

一份可复制到项目 Agent 指令中的短规则卡，用于约束编码 Agent 对慢构建、测试、格式化和静态检查的执行预算。

- [Agent Execution Budget](./knowledge/agent-execution-budget/agent-execution-budget.md)

```

- [ ] **Step 2: Verify the link target exists and the diff is clean**

Run:

```bash
test -f knowledge/agent-execution-budget/agent-execution-budget.md && git diff --check
```

Expected: no output and exit code `0`.

- [ ] **Step 3: Review the rendered source structure**

Run:

```bash
grep -n -A5 -B1 "agent-execution-budget" README.md
```

Expected: the topic heading, Chinese summary, and relative link appear once and precede `system-architecture-review`.

- [ ] **Step 4: Commit the index update**

```bash
git add README.md
git commit -m "docs: index execution budget prompt" \
  -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

## Final Verification

- [ ] Run:

```bash
git diff --check
git status --short
git log --oneline -2
```

Expected: no whitespace errors; the working tree is clean after the two commits; the last two commits describe the prompt card and its README index entry.

## Self-Review

- Spec coverage: Task 1 implements the short copyable prompt, risk-based repeat gate, scope rules, and Rust workflow. Task 2 adds the required index entry.
- Placeholder scan: no unresolved placeholders or implied code changes remain; `<crate>` is intentional instructional syntax in the prompt card.
- Scope: this plan adds only the requested coding-agent prompt and its index link; it does not turn the prompt into a new skill or expand into generic orchestration policy.
