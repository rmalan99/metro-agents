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
  "source": "QA_DEFECT",
  "requirement_id": "REQ-001",
  "work_order_id": "WO-QA-001",
  "task_id": "QA-001",
  "defect_id": "BUG-001",
  "reason_code": "FUNCTIONAL_FAILURE",
  "reason_detail": "Submitting valid input does not persist the record",
  "failed_criteria": ["AC-003"],
  "description": "Exact error description supplied by the reporter",
  "evidence": [],
  "correction": null,
  "reported_result": null
}
```

All keys are required and supplied by the reporter, not inferred by the logger. `event_id`, `error_id`, `reason_detail` and every populated `failed_criteria` entry are nonempty strings. Sources are `QA_DEFECT`, `LEAD_REJECTION`, `ORCHESTRATION_ERROR` and `AGENT_ERROR`. Allowed `reason_code` values are `REQUIREMENT_MISMATCH`, `FUNCTIONAL_FAILURE`, `REGRESSION`, `VALIDATION`, `ACCESSIBILITY`, `MISSING_TESTS`, `UNSTABLE_SELECTOR`, `INCOMPLETE_WORK`, `CONTRACT_VIOLATION` and `OTHER`. Use `OTHER` only with an explicit reason that explains why no defined code applies. A QA defect requires `defect_id`, matching `error_id`, and at least one failed criterion; fields that do not apply to other sources are null or empty arrays. Types: `ERROR_REPORTED`, `CORRECTION_REPORTED`, `RESOLUTION_REPORTED`. A correction is a new event with a new `event_id` and the original classification. Preserve the team's exact correction description and reported outcome. A resolution records the team's assertion, not independent verification by the logger. `reported_at` is the reporter-supplied timestamp, not an invented timestamp.

The helper appends without semantic analysis. Identical event IDs and payloads are skipped; conflicting payloads are rejected without rewriting history. A file lock serializes concurrent append operations. Do not send credentials or sensitive payloads. Only the logger writes this log during delivery; authorized Leads and Orchestrator dispatch events directly to it.

## Delegation

Frontend Lead, Backend Lead, QA Lead and Orchestrator may pass this contract and complete events directly to error-logger. Leads report rejected Junior work and QA defects as soon as they confirm them; Orchestrator reports coordination or integration errors it observes. Logging is a passive audit action for the user: it does not escalate, gate, pause, retry or otherwise change normal correction and delivery work. The caller reports an actual write failure honestly and continues its workflow. At most one logger invocation per reporting agent should be active at a time.
