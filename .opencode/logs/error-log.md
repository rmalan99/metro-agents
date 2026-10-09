# Error log contract

File: `.opencode/logs/errors.jsonl`. UTF-8 JSON Lines: one complete JSON object per line, append-only. The helper creates it upon the first real event; do not add fictional incidents or empty placeholder entries.

## Event supplied to the logger

```json
{
  "event_id": "EVT-001",
  "error_id": "ERR-001",
  "type": "ERROR_REPORTED",
  "reported_at": null,
  "reported_by": "qa-lead",
  "team": "qa",
  "requirement_id": "REQ-001",
  "work_order_id": "WO-QA-001",
  "task_id": "QA-001",
  "description": "Exact error description supplied by the reporter",
  "evidence": [],
  "correction": null,
  "reported_result": null
}
```

All keys are required; unknown values are null or empty arrays, supplied by the reporter, not inferred by the logger. event_id and error_id must be nonempty strings. Types: ERROR_REPORTED, CORRECTION_REPORTED, RESOLUTION_REPORTED. A correction is a new event with a new event_id and the original error_id. Preserve the team's exact correction description and reported outcome. A resolution records the team's assertion, not independent verification by the logger. reported_at is the reporter-supplied timestamp, not an invented timestamp.

The helper appends without semantic analysis. Identical event IDs and payloads are skipped; conflicting payloads are rejected without rewriting history. A file lock serializes concurrent append operations. Do not send credentials or sensitive payloads. Only the logger writes this log during delivery; other agents report events upward.

## Delegation

The Orchestrator passes this contract and complete events directly to error-logger. It may run alongside team activity where the runtime supports concurrent/background delegation. Logging is outside Junior budgets, does not require Lead review, and never gates development or QA. At most one logger invocation should be dispatched at a time; batch pending events without delaying team work. If background delegation is unsupported, retain pending events in delivery reports and dispatch at the next available opportunity; report pending/failed logging honestly. Prompts do not implement a background queue or guarantee execution after a session ends.
