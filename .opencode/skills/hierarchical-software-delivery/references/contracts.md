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
  junior_slot_budget: 1 # Orchestrator reserves 1 or 2; total unfinished budgets <= 4
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

## Required task quality fields

Apply these fields to development and QA tasks in addition to role-specific fields. For read-only tasks, use empty write_paths and explain any unavailable check.

```yaml
quality:
  acceptance_criteria: [] # requirement/criterion IDs and observable outcomes
  risk: LOW | MEDIUM | HIGH
  write_paths: [] # explicit files or bounded directories
  read_dependencies: [] # artifacts that must remain stable during execution
  exclusive_resources: [] # ports, databases, fixtures, generated outputs
  prerequisite_acceptances: [] # accepted task IDs/evidence
  validation_plan: [] # check, working directory, expected behavior, mandatory flag
  not_applicable: [] # check and reason
```

## Validation evidence entry

Use this structure in validation_evidence or tests_executed. Preserve the runner's actual exit status; optional skipped checks do not count as passed.

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

## Lead review and Work Order quality report

```yaml
lead_review:
  task_id: <id>
  status: ACCEPTED | CORRECTION_REQUIRED | BLOCKED
  changes_inspected: []
  acceptance_criteria_checked: []
  contracts_checked: []
  evidence_reviewed: []
  reasons: []
  correction_attempts: 0

quality_summary:
  integration_evidence: []
  mandatory_checks_unresolved: []
  lead_rejections: 0
  correction_attempts: 0
  qa_defects: 0
  recurring_causes: []
  concurrency_observed: <parallel or sequential, with evidence/limitations>
```

READY_FOR_QA requires reviewed integration evidence and no unresolved mandatory checks. PASSED requires independent evidence for all mandatory criteria and affected regression. COMPLETED requires both development and QA gates. A partial or unavailable validation is reported explicitly, never counted as success.
