"""Append supplied JSON events, without interpreting their contents."""
import fcntl
import json
from pathlib import Path
import sys


def append(event, path):
    required = {
        "event_id", "error_id", "type", "reported_at", "reported_by", "team",
        "requirement_id", "work_order_id", "task_id", "description", "evidence",
        "correction", "reported_result",
    }
    if not isinstance(event, dict) or set(event) != required:
        raise ValueError("Expected exactly the documented event fields")
    for key in ("event_id", "error_id"):
        if not isinstance(event[key], str) or not event[key].strip():
            raise ValueError(f"{key} must be a nonempty string")
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
