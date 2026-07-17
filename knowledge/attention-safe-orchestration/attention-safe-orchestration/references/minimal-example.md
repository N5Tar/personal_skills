# Minimal Example

Initialize a task without overwriting files:

~~~bash
python3 scripts/taskctl.py init .ai/tasks/example-1
python3 scripts/taskctl.py validate .ai/tasks/example-1/manifest.yaml
~~~

When `brief.md` identifies a documented configuration, use it. Append the source to
`evidence.md` and record the reversible decision with its rollback in `decisions.md`.
No human checkpoint is consumed because the value exists and no public boundary changes.

If the review registry is full:

~~~bash
python3 scripts/taskctl.py review-capacity .ai/tasks/registry.yaml
# WAITING_REVIEW_CAPACITY
python3 scripts/taskctl.py transition .ai/tasks/example-1/manifest.yaml WAITING_REVIEW_CAPACITY
python3 scripts/taskctl.py handoff-draft .ai/tasks/example-1/handoff.md example-1
~~~

