# 05 — Review Backpressure

Registry reports `ready_for_review: 2` and `limit_ready_for_review: 2`. A third task
has verification evidence and a draft handoff.

Expected with Skill: set `WAITING_REVIEW_CAPACITY`, retain handoff draft, and create no
new review interruption.

