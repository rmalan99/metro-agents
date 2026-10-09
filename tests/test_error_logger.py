import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("error_logger", ROOT / ".opencode/tools/append-error-log.py")
logger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(logger)


class LoggerTests(unittest.TestCase):
    def event(self, **changes):
        event = {
            key: None
            for key in (
                "event_id", "error_id", "type", "reported_at", "reported_by", "team",
                "source", "requirement_id", "work_order_id", "task_id", "defect_id", "reason_code",
                "reason_detail", "failed_criteria", "description", "evidence", "correction",
                "reported_result",
            )
        }
        event.update(
            event_id="fixture-1",
            error_id="BUG-001",
            defect_id="BUG-001",
            type="ERROR_REPORTED",
            source="QA_DEFECT",
            reason_code="FUNCTIONAL_FAILURE",
            reason_detail="Valid submission is not persisted",
            failed_criteria=["AC-001"],
            description="Temporary test fixture",
            evidence=[],
        )
        event.update(changes)
        return event

    def test_append_duplicate_and_conflict_preserve_history(self):
        event = self.event()
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

    def test_rejects_invalid_qa_classification(self):
        with tempfile.TemporaryDirectory(prefix="metro-logger-") as directory:
            path = Path(directory) / "fixture.jsonl"
            invalid_events = (
                (self.event(reason_code="UNKNOWN"), "Unsupported reason_code"),
                (self.event(reason_detail=""), "reason_detail must be a nonempty string"),
                (self.event(source="UNKNOWN"), "Unsupported source"),
                (self.event(failed_criteria=[]), "QA defect failed_criteria must be nonempty"),
                (self.event(failed_criteria=[""]), "failed_criteria entries must be nonempty strings"),
                (self.event(defect_id="BUG-002"), "QA defect error_id must match defect_id"),
            )
            for event, message in invalid_events:
                with self.subTest(message=message):
                    with self.assertRaisesRegex(ValueError, message):
                        logger.append(event, path)
            self.assertFalse(path.exists())

    def test_lifecycle_events_preserve_defect_classification(self):
        with tempfile.TemporaryDirectory(prefix="metro-logger-") as directory:
            path = Path(directory) / "fixture.jsonl"
            reported = self.event()
            corrected = self.event(
                event_id="fixture-2",
                type="CORRECTION_REPORTED",
                correction="Persist the validated record",
            )
            resolved = self.event(
                event_id="fixture-3",
                type="RESOLUTION_REPORTED",
                reported_result="PASS",
            )
            self.assertEqual(logger.append(reported, path), "APPENDED")
            self.assertEqual(logger.append(corrected, path), "APPENDED")
            self.assertEqual(logger.append(resolved, path), "APPENDED")
            events = [json.loads(line) for line in path.read_text().splitlines()]
            self.assertEqual({event["defect_id"] for event in events}, {"BUG-001"})
            self.assertEqual({event["reason_code"] for event in events}, {"FUNCTIONAL_FAILURE"})

    def test_accepts_lead_rejection_without_qa_defect_fields(self):
        with tempfile.TemporaryDirectory(prefix="metro-logger-") as directory:
            path = Path(directory) / "fixture.jsonl"
            event = self.event(
                error_id="ERR-LEAD-001",
                source="LEAD_REJECTION",
                defect_id=None,
                reason_code="INCOMPLETE_WORK",
                reason_detail="Junior reported completion but required behavior is missing",
                failed_criteria=[],
            )
            self.assertEqual(logger.append(event, path), "APPENDED")


if __name__ == "__main__":
    unittest.main()
