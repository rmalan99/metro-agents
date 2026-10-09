# Validation evidence entry

```yaml
- check: <command or functional check>
  working_directory: <path>
  mandatory: true
  expected: <observable outcome>
  actual: <observed outcome>
  result: PASS | FAIL | SKIPPED | NOT_RUN | BLOCKED
  exit_code: null # actual code for commands; null for non-command checks
  test_counts: null # actual passed/failed/skipped counts when available
  evidence: <output summary or artifact reference>
```
