# QA task

```yaml
task:
  id: QA-<number>
  parent_work_order: <id>
  objective: <one validation objective>
  requirement_traceability: []
  existing_coverage: []
  valuable_manual_cases: []
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

`existing_coverage` identifies versioned automated tests to inspect or reuse. Each `valuable_manual_cases` entry identifies the case, protected behavior and target test scope; omit cases already fully represented by `existing_coverage`.
