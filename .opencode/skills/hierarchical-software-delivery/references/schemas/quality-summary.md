# Work Order quality summary

```yaml
quality_summary:
  integration_evidence: []
  mandatory_checks_unresolved: []
  lead_rejections: 0
  correction_attempts: 0
  qa_defects: 0
  recurring_causes: [{ reason_code: <code>, occurrences: 0, defect_ids: [] }]
  concurrency_observed: <parallel or sequential, with evidence/limitations>
```

Derive `recurring_causes` from registered QA defects grouped by `reason_code`; do not infer categories from free text.
