"""Append supplied JSON events, without interpreting their contents."""
import fcntl
import json
from pathlib import Path
import sys


REASON_CODES = {
    "REQUIREMENT_MISMATCH",
    "FUNCTIONAL_FAILURE",
    "REGRESSION",
    "VALIDATION",
    "ACCESSIBILITY",
    "MISSING_TESTS",
    "UNSTABLE_SELECTOR",
    "INCOMPLETE_WORK",
    "CONTRACT_VIOLATION",
    "OTHER",
}

SOURCES = {"QA_DEFECT", "LEAD_REJECTION", "ORCHESTRATION_ERROR", "AGENT_ERROR"}


def append(event, path):
    required = {
        "event_id", "error_id", "type", "reported_at", "reported_by", "team", "source",
        "requirement_id", "work_order_id", "task_id", "defect_id", "reason_code",
        "reason_detail", "failed_criteria", "description", "evidence", "correction",
        "reported_result",
    }
    if not isinstance(event, dict) or set(event) != required:
        raise ValueError("Expected exactly the documented event fields")
    for key in ("event_id", "error_id", "reason_detail"):
        if not isinstance(event[key], str) or not event[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
    if event["source"] not in SOURCES:
        raise ValueError("Unsupported source")
    if event["reason_code"] not in REASON_CODES:
        raise ValueError("Unsupported reason_code")
    if not isinstance(event["failed_criteria"], list):
        raise ValueError("failed_criteria must be a list")
    if any(not isinstance(value, str) or not value.strip() for value in event["failed_criteria"]):
        raise ValueError("failed_criteria entries must be nonempty strings")
    if event["defect_id"] is not None and (
        not isinstance(event["defect_id"], str) or not event["defect_id"].strip()
    ):
        raise ValueError("defect_id must be null or a nonempty string")
    if event["source"] == "QA_DEFECT":
        if event["defect_id"] != event["error_id"]:
            raise ValueError("QA defect error_id must match defect_id")
        if not event["failed_criteria"]:
            raise ValueError("QA defect failed_criteria must be nonempty")
    if event["type"] not in {
        "ERROR_REPORTED", "CORRECTION_REPORTED", "RESOLUTION_REPORTED"
    }:
        raise ValueError("Unsupported event type")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise ValueError("Log must not be a symlink")
    with path.open("a+", encoding="utf-8") as log:
        fcntl.flock(log, fcntl.LOCK_EX)
        log.seek(0)
        for line in log:
            previous = json.loads(line)
            if previous["event_id"] == event["event_id"]:
                if previous != event:
                    raise ValueError("Conflicting event_id; log unchanged")
                return "DUPLICATE"
        log.write(json.dumps(event, ensure_ascii=False, allow_nan=False) + "\n")
        log.flush()
    return "APPENDED"


if __name__ == "__main__":
    try:
        event = json.load(sys.stdin)
        root = Path(__file__).resolve().parents[2]
        path = root / ".opencode" / "logs" / "errors.jsonl"
        print(append(event, path))
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
