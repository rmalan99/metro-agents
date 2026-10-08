# Canonical Delivery Contracts

## Work Order

```yaml
work_order:
  id: WO-<TEAM>-001
  team: frontend | backend | qa
  requirement_id: REQ-001
  objective: <team outcome>
  requirements: []
  business_rules: []
  contracts: []
  dependencies: []
  constraints: []
  expected_result: []
  acceptance_criteria: []
  evidence_expected: []
```

## Development task

```yaml
task:
  id: FE-001 | BE-001
  parent_work_order: <id>
  objective: <bounded outcome>
  instructions: []
  scope:
    allowed: []
    forbidden: []
  requirements: []
  constraints: []
  contracts: []
  dependencies: []
  expected_result: []
  validation: []
```

## Development result

```yaml
task_result:
  task_id: <id>
  status: COMPLETED | FAILED | BLOCKED
  files_changed: []
  implementation_summary: []
  validation_evidence: []
  requirements_checked: []
  issues: []
  out_of_scope_observations: []
```

## QA result

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
