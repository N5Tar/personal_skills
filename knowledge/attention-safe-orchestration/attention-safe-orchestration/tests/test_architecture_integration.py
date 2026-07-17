"""Regression checks for the architecture-design route between personal Skills."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[4]
ATTENTION = ROOT / "knowledge/attention-safe-orchestration/attention-safe-orchestration/SKILL.md"
ARCHITECTURE = ROOT / "knowledge/architecture-first-design/architecture-first-design/SKILL.md"
EVIDENCE_DEBUG = ROOT / "knowledge/debugging-code/vibe-debug-with-evidence-skill/SKILL.md"


class ArchitectureIntegrationTests(unittest.TestCase):
    def test_attention_routes_architecture_changes_without_premature_escalation(self):
        source = ATTENTION.read_text(encoding="utf-8")
        self.assertIn("architecture-first-design", source)
        self.assertIn("ARCHITECTURE-READY", source)
        self.assertIn("Architecture document state is not the task status", source)

    def test_architecture_skill_hands_off_to_writing_plans_after_readiness(self):
        source = ARCHITECTURE.read_text(encoding="utf-8")
        self.assertIn("superpowers:writing-plans", source)
        self.assertIn("ARCHITECTURE-READY", source)
        self.assertIn("hard gate ends", source)

    def test_complex_bug_route_classifies_before_repair_or_architecture_design(self):
        attention = ATTENTION.read_text(encoding="utf-8")
        evidence = EVIDENCE_DEBUG.read_text(encoding="utf-8")
        self.assertIn("vibe-debug-with-evidence", attention)
        self.assertIn("superpowers:systematic-debugging", evidence)
        self.assertIn("architecture-first-design", evidence)
        self.assertIn("`unknown`", evidence)


if __name__ == "__main__":
    unittest.main()
