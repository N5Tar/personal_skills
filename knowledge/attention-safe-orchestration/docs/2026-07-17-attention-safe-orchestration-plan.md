# Attention-Safe Orchestration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Deliver and locally install an experimentally verified Wrapper Skill that prevents routine multi-agent coding work from consuming human attention.

**Architecture:** A concise Skill defines judgment and routing. A dependency-free Python command supplies repeatable file/state checks. Markdown pressure scenarios and immutable transcripts prove behavioural constraints without claiming unavailable live-agent runs.

**Tech Stack:** Markdown, YAML-shaped text, Python 3 standard library, `unittest`, Git.

---

### Task 1: Establish RED baseline pressure evidence

**Files:**
- Create: `knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/{README.md,run_checks.py,evaluation.md}`
- Create: `knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/scenarios/{01-existing-context,02-reversible-choice,03-environment-isolation,04-repeated-failure,05-review-backpressure}.md`
- Create: `knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/baseline/{README.md,01-existing-context,02-reversible-choice,03-environment-isolation,04-repeated-failure,05-review-backpressure}.md`

- [ ] **Step 1: Write the failing evaluator**

Create `run_checks.py` so it requires exactly five baseline records, five with-Skill records, a source `SKILL.md`, and five `PASS` rows in `evaluation.md`. Its failure text must identify each missing category.

- [ ] **Step 2: Run the evaluator to prove RED**

Run: `python3 knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/run_checks.py`

Expected: non-zero exit because `SKILL.md` and with-Skill records do not exist.

- [ ] **Step 3: Create five scenario prompts and baseline records**

Each prompt contains a concrete task context and acceptance condition. Each baseline record stores prompt, observed response, interruption/failure, and verbatim rationalization. Required failures: ask despite documented configuration; ask despite reversible local choice; infer environment without manifest; loop beyond repair limit; announce third review while capacity is two.

- [ ] **Step 4: Re-run evaluator and commit RED evidence**

Run: `python3 knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/run_checks.py`

Expected: non-zero exit mentioning only absent source/with-Skill records.

```bash
git add knowledge/attention-safe-orchestration/tests/attention-safe-orchestration
git commit -m "test: capture orchestration baseline failures"
```

### Task 2: Implement and test deterministic task controls

**Files:**
- Create: `knowledge/attention-safe-orchestration/attention-safe-orchestration/scripts/taskctl.py`
- Create: `knowledge/attention-safe-orchestration/attention-safe-orchestration/tests/test_taskctl.py`

- [ ] **Step 1: Write failing tests**

```python
def test_init_never_overwrites_a_task_file(tmp_path):
    task = tmp_path / ".ai/tasks/demo-1"
    assert run("init", task) == 0
    (task / "brief.md").write_text("keep")
    assert run("init", task) != 0
    assert (task / "brief.md").read_text() == "keep"

def test_validate_rejects_missing_identity(tmp_path):
    manifest = tmp_path / "manifest.yaml"
    manifest.write_text("task_id: demo-1\n")
    assert run("validate", manifest) != 0
```

- [ ] **Step 2: Run tests to prove RED**

Run: `python3 -m unittest knowledge/attention-safe-orchestration/attention-safe-orchestration/tests/test_taskctl.py -v`

Expected: FAIL because `taskctl.py` is absent.

- [ ] **Step 3: Implement the minimum CLI**

Use `argparse` and only the standard library. Implement `init`, `validate`, `transition`, `review-capacity`, and `handoff-draft`. Parse only flat `key: value` input. `init` refuses populated targets; mutation commands accept `--dry-run`; transition accepts exactly the eight specified statuses; review capacity outputs `WAITING_REVIEW_CAPACITY` when ready count meets its limit.

- [ ] **Step 4: Run focused tests**

Run: `python3 -m unittest knowledge/attention-safe-orchestration/attention-safe-orchestration/tests/test_taskctl.py -v`

Expected: PASS.

- [ ] **Step 5: Add RED tests for state and WIP boundaries, then implement**

```python
def test_transition_rejects_unknown_status(tmp_path):
    assert run("transition", tmp_path / "manifest.yaml", "UNKNOWN") != 0

def test_review_capacity_defers_third_ready_task(tmp_path):
    registry = tmp_path / "registry.yaml"
    registry.write_text("ready_for_review: 2\nlimit_ready_for_review: 2\n")
    assert output("review-capacity", registry) == "WAITING_REVIEW_CAPACITY\n"
```

Run the focused tests before and after implementation; record the expected RED failure and GREEN pass.

- [ ] **Step 6: Commit controls**

```bash
git add knowledge/attention-safe-orchestration/attention-safe-orchestration/scripts \
        knowledge/attention-safe-orchestration/attention-safe-orchestration/tests
git commit -m "feat: add safe task orchestration controls"
```

### Task 3: Write the minimal Wrapper Skill and references

**Files:**
- Create: `knowledge/attention-safe-orchestration/attention-safe-orchestration/SKILL.md`
- Create: `knowledge/attention-safe-orchestration/attention-safe-orchestration/references/{templates.md,minimal-example.md,install-and-rollback.md}`
- Create: `knowledge/attention-safe-orchestration/attention-safe-orchestration/README.md`

- [ ] **Step 1: Confirm source-related evaluator failure**

Run: `python3 knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/run_checks.py`

Expected: non-zero exit because `SKILL.md` is absent.

- [ ] **Step 2: Write the minimal Skill**

Include exact frontmatter; manifest-first recovery; status model; interruption/batching policy; autonomous/escalation policy; WIP rule; handoff contract; routing table with explicit `REQUIRED SUB-SKILL` references; counters only for observed baseline rationalizations; one minimal example. Do not reproduce referenced Skill bodies.

- [ ] **Step 3: Write templates and example**

Template: all required manifest fields, seven task files, readable registry, and required handoff table. Example: read known configuration without interrupting, make and record a reversible decision.

- [ ] **Step 4: Re-run evaluator**

Run: `python3 knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/run_checks.py`

Expected: non-zero exit mentioning absent with-Skill records.

- [ ] **Step 5: Commit Skill**

```bash
git add knowledge/attention-safe-orchestration/attention-safe-orchestration
git commit -m "feat: add attention safe orchestration skill"
```

### Task 4: Capture GREEN evidence and close observed loopholes

**Files:**
- Create: `knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/with-skill/{README.md,01-existing-context,02-reversible-choice,03-environment-isolation,04-repeated-failure,05-review-backpressure}.md`
- Modify: `knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/evaluation.md`
- Modify: `knowledge/attention-safe-orchestration/attention-safe-orchestration/SKILL.md`

- [ ] **Step 1: Record five with-Skill evaluations**

For each original prompt record manifest use, no unnecessary interrupt, required decision/evidence/blocker action, and expected terminal status. If no live agent runner is available, label the record `static contract evaluation`, cite exact clauses and commands, and never label it a live-agent run.

- [ ] **Step 2: Run evaluator**

Run: `python3 knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/run_checks.py`

Expected: PASS with five baseline records, five with-Skill records, required clauses, and five PASS rows.

- [ ] **Step 3: Close observed rationalization loopholes only**

Add explicit counters for recorded baseline phrases: “I should ask first”, “for safety I need confirmation”, “I will report progress first”, and “may I continue?”. Re-run evaluator after every change.

- [ ] **Step 4: Commit GREEN evidence**

```bash
git add knowledge/attention-safe-orchestration
git commit -m "test: verify attention safe orchestration scenarios"
```

### Task 5: Install, verify, and report

**Files:**
- Create: `knowledge/attention-safe-orchestration/docs/2026-07-17-attention-safe-orchestration-verification.md`
- Install: `~/.agents/skills/attention-safe-orchestration/`

- [ ] **Step 1: Prove installation is absent**

Run: `test -f ~/.agents/skills/attention-safe-orchestration/SKILL.md`

Expected: non-zero exit before installation.

- [ ] **Step 2: Copy without overwrite**

Run: `test ! -e ~/.agents/skills/attention-safe-orchestration && cp -R knowledge/attention-safe-orchestration/attention-safe-orchestration ~/.agents/skills/attention-safe-orchestration`

Expected: exit 0; existing installation stops the command.

- [ ] **Step 3: Run complete verification**

```bash
python3 -m unittest discover -s knowledge/attention-safe-orchestration/attention-safe-orchestration/tests -v
python3 knowledge/attention-safe-orchestration/tests/attention-safe-orchestration/run_checks.py
test -f ~/.agents/skills/attention-safe-orchestration/SKILL.md
git diff --check HEAD~4..HEAD
git status --short --branch
```

Expected: tests/evaluator/installation/whitespace checks pass; status distinguishes experiment changes from pre-existing work.

- [ ] **Step 4: Write verification report and self-review**

Map each acceptance criterion to a path, command, and actual outcome. State skips, installation path, commit range, pre-existing worktree state, and exact rollback removal.

- [ ] **Step 5: Commit report**

```bash
git add knowledge/attention-safe-orchestration
git commit -m "docs: verify attention safe orchestration experiment"
```

