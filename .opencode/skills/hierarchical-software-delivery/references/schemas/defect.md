# Product defect

```yaml
defect:
  id: BUG-<number>
  severity: CRITICAL | HIGH | MEDIUM | LOW
  requirement_reference: <id>
  failed_criteria: []
  area: frontend | backend | cross-team | requirement
  reason_code: REQUIREMENT_MISMATCH | FUNCTIONAL_FAILURE | REGRESSION | VALIDATION | ACCESSIBILITY | MISSING_TESTS | UNSTABLE_SELECTOR | OTHER
  reason_detail: <specific reason for returning the change>
  title: <title>
  preconditions: []
  steps: []
  expected: <expected>
  actual: <actual>
  evidence: []
  regression_scope: []
```

`failed_criteria` contains at least one acceptance-criterion ID for an observed violation. `reason_detail` is always specific and is mandatory for `OTHER`; do not use `OTHER` when a defined code applies.
