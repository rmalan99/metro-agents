# QA Work Order result

```yaml
qa_result:
  work_order_id: <id>
  status: PASSED | FAILED | BLOCKED
  acceptance_criteria: []
  tests_reused: []
  tests_created: []
  tests_executed: []
  valuable_manual_cases: []
  defects: []
  regression_risks: []
  unresolved: []
```

`FAILED` requires at least one QA Lead-confirmed [Defect](defect.md). `BLOCKED` represents a missing prerequisite and must not be counted as a product defect.

Each `valuable_manual_cases` entry traces the manual case to an executed versioned test in `tests_reused` or `tests_created`. `PASSED` is invalid while any valuable case remains uncovered.
