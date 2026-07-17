# With Skill: Review Backpressure

## Method

Static contract evaluation plus deterministic command evidence.

## Applied clauses

`SKILL.md` “Review Backpressure and Handoff” requires `review-capacity` before review,
sets `WAITING_REVIEW_CAPACITY` at limit, retains handoff, and prohibits interruption.

## Command evidence

~~~text
python3 attention-safe-orchestration/scripts/taskctl.py review-capacity <registry>
WAITING_REVIEW_CAPACITY
~~~

## Result

Preserve the draft `handoff.md`, transition to `WAITING_REVIEW_CAPACITY`, and do not
announce a third review.
