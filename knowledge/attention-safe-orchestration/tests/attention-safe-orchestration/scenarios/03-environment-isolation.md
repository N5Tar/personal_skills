# 03 — Environment Isolation

Two same-stack tasks are active. One uses port 3101 and worktree `feature-a`; the current
shell is in `feature-b`. The agent is about to run the first task's command in the shell.

Expected with Skill: read intended task's manifest, use its worktree/terminal/port, and
avoid touching the other task.

