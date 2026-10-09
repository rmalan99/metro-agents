# QA Work Order result

```yaml
qa_result:
  work_order_id: <id>
  status: PASSED | FAILED | BLOCKED
  acceptance_criteria: []
  tests_created: []
  tests_executed: []
  defects: []
  regression_risks: []
  unresolved: []
```

`FAILED` requires at least one QA Lead-confirmed [Defect](defect.md). `BLOCKED` represents a missing prerequisite and must not be counted as a product defect.
