import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "taskctl.py"

REQUIRED_MANIFEST = """task_id: demo-1
project_name: demo
repository_path: /tmp/repo
worktree_path: /tmp/repo
branch_name: main
conversation_label: demo-chat
terminal_label: demo-terminal
task_directory: .ai/tasks/demo-1
current_status: PLANNING
current_phase: design
next_human_checkpoint: none
verification_status: NOT_RUN
unresolved_blockers: none
"""

class TaskctlTests(unittest.TestCase):
    def call(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)], text=True, capture_output=True)

    def test_init_never_overwrites_a_task_file(self):
        with tempfile.TemporaryDirectory() as temp:
            task = Path(temp) / ".ai/tasks/demo-1"
            self.assertEqual(self.call("init", task).returncode, 0)
            brief = task / "brief.md"
            brief.write_text("keep", encoding="utf-8")
            self.assertNotEqual(self.call("init", task).returncode, 0)
            self.assertEqual(brief.read_text(encoding="utf-8"), "keep")

    def test_validate_rejects_missing_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = Path(temp) / "manifest.yaml"
            manifest.write_text("task_id: demo-1\n", encoding="utf-8")
            self.assertNotEqual(self.call("validate", manifest).returncode, 0)

    def test_transition_rejects_unknown_status(self):
        with tempfile.TemporaryDirectory() as temp:
            manifest = Path(temp) / "manifest.yaml"
            manifest.write_text(REQUIRED_MANIFEST, encoding="utf-8")
            self.assertNotEqual(self.call("transition", manifest, "UNKNOWN").returncode, 0)

    def test_review_capacity_defers_third_ready_task(self):
        with tempfile.TemporaryDirectory() as temp:
            registry = Path(temp) / "registry.yaml"
            registry.write_text("ready_for_review: 2\nlimit_ready_for_review: 2\n", encoding="utf-8")
            result = self.call("review-capacity", registry)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "WAITING_REVIEW_CAPACITY\n")

if __name__ == "__main__":
    unittest.main()

