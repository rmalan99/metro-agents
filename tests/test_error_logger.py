import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("error_logger", ROOT / ".opencode/tools/append-error-log.py")
logger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(logger)


class LoggerTests(unittest.TestCase):
    def test_append_duplicate_and_conflict_preserve_history(self):
        event = {key: None for key in ("event_id", "error_id", "type", "reported_at", "reported_by", "team", "requirement_id", "work_order_id", "task_id", "description", "evidence", "correction", "reported_result")}
        event.update(event_id="fixture-1", error_id="fixture-error", type="ERROR_REPORTED", description="Temporary test fixture", evidence=[])
        with tempfile.TemporaryDirectory(prefix="metro-logger-") as directory:
            path = Path(directory) / "fixture.jsonl"
            self.assertEqual(logger.append(event, path), "APPENDED")
            first = path.read_bytes()
            self.assertEqual(logger.append(event, path), "DUPLICATE")
            self.assertEqual(path.read_bytes(), first)
            with self.assertRaisesRegex(ValueError, "Conflicting"):
                logger.append({**event, "description": "conflicting fixture"}, path)
            with self.assertRaisesRegex(ValueError, "documented event fields"):
                logger.append({"event_id": "missing"}, path)
            self.assertEqual(path.read_bytes(), first)


if __name__ == "__main__":
    unittest.main()
