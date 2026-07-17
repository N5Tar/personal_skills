# Evaluation

| Scenario | Baseline behavior | Expected behavior | New behavior | Result |
| --- | --- | --- | --- | --- |
| 01-existing-context | asks despite documented context | lookup without interruption | static contract evaluation: manifest/task-file lookup, evidence and decision | PASS |
| 02-reversible-choice | asks about private choice | choose and record | static contract evaluation: repository convention and decision ledger | PASS |
| 03-environment-isolation | infers shell identity | manifest-first isolation | static contract evaluation: manifest-bound worktree/terminal/port | PASS |
| 04-repeated-failure | speculative loop | safe failure with evidence | static contract evaluation: debugging route, evidence, aggregated safe failure | PASS |
| 05-review-backpressure | third review interruption | defer at queue limit | static contract evaluation plus taskctl review-capacity evidence | PASS |
| 06-architecture-routing | immediately escalates an architecture signal | collect evidence on the architecture track | static contract evaluation: route, `PLANNING`, and `Open Decisions` gate | PASS |
| 07-architecture-ready-handoff | architecture readiness has no execution handoff | create one plan from approved architecture | static contract evaluation: `ARCHITECTURE-READY` handoff contract | PASS |
| 08-complex-bug-routing | generic debugging begins repair without ownership classification | classify from falsifiable evidence before selecting repair route | static contract evaluation: evidence, implementation, design, and unknown handoff | PASS |
