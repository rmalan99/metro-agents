# Refined requirement

```yaml
refined_requirement:
  id: REQ-<short-id>
  title: <title>

  objective: <business/user outcome>

  actors:
    - <actor>

  scope:
    included: []
    excluded: []

  expected_behavior:
    - <observable behavior>

  functional_requirements:
    - id: FR-01
      requirement: <requirement>

  business_rules:
    - id: BR-01
      rule: <rule>

  constraints:
    - id: CON-01
      constraint: <constraint>

  imposed_contracts:
    - id: CT-01
      contract: <already imposed external contract>

  acceptance_criteria:
    - id: AC-01
      criterion: <observable and testable outcome>

  assumptions:
    - id: AS-01
      assumption: <explicit assumption>

  unresolved:
    - id: U-01
      question: <material unresolved point>
      impact: <impact>

  non_goals: []
```

Use empty arrays when appropriate. Unresolved material decisions return to the Orchestrator.
