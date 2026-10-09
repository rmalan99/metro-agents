# QA task

```yaml
task:
  id: QA-<number>
  parent_work_order: <id>
  objective: <one validation objective>
  requirement_traceability: []
  preconditions: []
  instructions: []
  scope:
    allowed: []
    forbidden:
      - production code modifications
  expected_result: []
  evidence_required: []
```

Attach the top-level quality object from [Task quality](task-quality.md).
