# QA task result

```yaml
qa_task_result:
  task_id: <id>
  status: PASS | FAIL | BLOCKED
  requirement_traceability: []
  existing_tests_reused: []
  valuable_manual_cases: []
  tests_created_or_changed: []
  tests_executed: []
  observed_behavior: <actual>
  expected_behavior: <expected>
  defects: []
  issues: []
```

tests_executed entries follow [Validation evidence](validation-evidence.md).

`FAIL` requires at least one complete [Defect](defect.md). `BLOCKED` represents a missing prerequisite, not an observed product violation.

Each `valuable_manual_cases` entry records the case, regression value and the versioned automated test that covers it. `PASS` requires every entry to reference an executed test in `existing_tests_reused` or `tests_created_or_changed`; a valuable case that cannot be persisted or executed within scope makes the task `BLOCKED`.
