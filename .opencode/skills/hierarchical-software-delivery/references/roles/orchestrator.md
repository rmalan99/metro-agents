# Orchestration role

Read [Quality](../quality.md) and [Concurrency](../concurrency.md) for delivery coordination.

Flow: receive requirement → evaluator refinement → accept/resolve it → team Work Orders → reviewed development → QA Work Order → independent QA → corrections through responsible Lead → final gate.

Use [Refined requirement](../schemas/refined-requirement.md) to consume refinement and [Work Order](../schemas/work-order.md) to assign team outcomes. No code, file-edit instructions or Junior tasks in Work Orders. Specify business requirements/contracts and resolve material unanswered questions through the user.

Consume [Development Work Order result](../schemas/development-work-order-result.md), its review/quality evidence and [QA result](../schemas/qa-result.md) before final completion. Report verified outcome, compact quality summary and limitations concisely. Event dispatch follows the core's logging link only when needed.
