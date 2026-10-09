# Canonical delivery contract index

Compatibility entry point; no schemas are defined here. The core routes active roles to only their required artifacts.

| Artifact | Owner |
|---|---|
| Refined requirement | [Schema](schemas/refined-requirement.md) |
| Work Order | [Schema](schemas/work-order.md) |
| Development task/result | [Task](schemas/development-task.md), [Result](schemas/development-result.md) |
| Development Work Order report | [Schema](schemas/development-work-order-result.md) |
| QA task/task result | [Task](schemas/qa-task.md), [Result](schemas/qa-task-result.md) |
| QA Work Order report | [Schema](schemas/qa-result.md) |
| Defect | [Schema](schemas/defect.md) |
| Task quality | [Schema](schemas/task-quality.md) |
| Validation entry | [Schema](schemas/validation-evidence.md) |
| Review/quality summary | [Review](schemas/lead-review.md), [Summary](schemas/quality-summary.md) |

Read [Quality](quality.md) or [Concurrency](concurrency.md) only for their applicable role/action. Do not load the whole artifact catalog for every invocation.
