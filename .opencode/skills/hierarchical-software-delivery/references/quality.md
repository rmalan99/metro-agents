# Delivery quality and acceptance

Canonical for delivery readiness, evidence and correction. Technical checks come from the relevant project/domain contract; do not repeat this policy in prompts.

## Before dispatch or execution
Every development/QA task attaches [Task quality](schemas/task-quality.md): criteria IDs, risk, bounded write scope, stable read dependencies, exclusive resources, accepted prerequisites and meaningful validation. Missing material ownership/behavior/prerequisites produce BLOCKED before edits. Workers do not overwrite another task's artifacts.

Select checks by requirement and risk. Include relevant negative, boundary, security and compatibility cases; explain inapplicable checks. No trivial tests merely to fill fields.

## Evidence
Use [Validation evidence](schemas/validation-evidence.md), preserving actual exit status, counts and observed outcomes. A zero exit code with zero tests does not establish a passing suite. Never weaken assertions or count skipped/unrun checks as passes.

Mandatory failed, unavailable or unexecuted checks prevent task success and acceptance. Source inspection cannot stand in for rendered/runtime behavior. A worker report is submitted for review, not self-accepted.

## Acceptance and integration
The Lead inspects actual scoped changes and evidence, checks criteria/contracts and records [Lead review](schemas/lead-review.md). Reports alone are insufficient.

Before READY_FOR_QA, commission meaningful integration validation through a Junior and review its evidence. An accepted implementation task may also supply this integration evidence when it exercised the final combined output; do not launch an identical extra check merely to create another task. Stale evidence after corrections must be rerun. The Orchestrator requires cross-team compatibility/integration evidence where relevant.

QA independently maps mandatory criteria to observations and reruns affected regression. Reuse fixtures/setup and prior evidence to plan coverage, not to substitute development's verdict for independent acceptance. Distinguish a missing prerequisite from an observed violation.

## Corrections and report
A correction identifies failed criterion, observed evidence, diagnosis, bounded scope and regression checks. After two unsuccessful attempts on the same task/defect, escalate to the Orchestrator for diagnosis/replanning. Resume only with a materially revised plan.

Work Orders include [Quality summary](schemas/quality-summary.md): integration evidence, unresolved checks, rejection/correction/defect counts and concurrency observations. Report failed/skipped/unrun work honestly. Never claim agents/models ran or parallelism occurred merely because configuration parses.
