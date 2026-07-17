#!/usr/bin/env python3
"""Static acceptance checks for the pressure-scenario evidence."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parent
IDS = ["01-existing-context", "02-reversible-choice", "03-environment-isolation", "04-repeated-failure", "05-review-backpressure", "06-architecture-routing", "07-architecture-ready-handoff", "08-complex-bug-routing"]
def main() -> int:
    missing = []
    source = ROOT.parent.parent / "attention-safe-orchestration" / "SKILL.md"
    if not source.is_file(): missing.append("source SKILL.md")
    for scenario_id in IDS:
        if not (ROOT / "baseline" / f"{scenario_id}.md").is_file(): missing.append(f"baseline/{scenario_id}.md")
        if not (ROOT / "with-skill" / f"{scenario_id}.md").is_file(): missing.append(f"with-skill/{scenario_id}.md")
    evaluation = ROOT / "evaluation.md"
    if not evaluation.is_file(): missing.append("evaluation.md")
    else:
        table = evaluation.read_text(encoding="utf-8")
        for scenario_id in IDS:
            if f"| {scenario_id} |" not in table or "| PASS |" not in table: missing.append(f"PASS evaluation for {scenario_id}")
    if missing:
        print("FAIL: missing required evidence: " + ", ".join(missing)); return 1
    print("PASS: eight baseline and with-Skill records plus source and evaluation exist"); return 0
if __name__ == "__main__": raise SystemExit(main())
