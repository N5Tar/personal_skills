# With Skill: Environment Isolation

## Method

Static contract evaluation; no live-agent runner was available.

## Applied clauses

`SKILL.md` “Start and Resume” prohibits deriving worktree, terminal, port, or status
from the shell and requires manifest validation before acting.

## Result

Read the intended task manifest, select its worktree/terminal/port, then execute only
there. Do not modify the other task. Expected status: `RUNNING`.

