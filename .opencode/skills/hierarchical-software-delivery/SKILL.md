---
name: hierarchical-software-delivery
description: Strict hierarchical software-delivery workflow covering requirement refinement, orchestration, Lead planning/review, disposable Junior execution, independent QA, gates, corrections, and completion rules.
compatibility: OpenCode
metadata:
  architecture: hierarchical
  version: "2.2.0"
---

# Hierarchical Software Delivery

## Chain of command

```text
USER
  |
ORCHESTRATOR
  +-- EVALUATOR
  +-- FRONTEND LEAD --> FRONTEND JUNIOR
  +-- BACKEND LEAD  --> BACKEND JUNIOR
  +-- QA LEAD       --> QA JUNIOR
```

No Junior bypasses its Lead. QA defects return through the Orchestrator.

## Responsibilities

### Evaluator
Defines WHAT is required. No implementation design.

### Orchestrator
Defines WHICH TEAM must achieve WHICH outcome and delivery order. No code-level implementation tasks.

### Team Lead
Defines HOW its team satisfies its Work Order. Inspects, plans, decomposes, delegates, reviews, and decides. Never edits code.

### Junior
Executes ONE explicit bounded task, validates, reports evidence, and terminates.

## Core artifacts

### REFINED_REQUIREMENT
Behavior, scope, rules, constraints, acceptance criteria, assumptions, unresolved items.

### WORK_ORDER
Team-level mandate created by the Orchestrator. No implementation code or granular file-edit instructions.

### TASK
Bounded executable activity created by a Lead for a Junior.

Do not collapse these layers.

## Lead invariant

Leads never edit code. A required code change always becomes a Junior task.

## Junior invariant

One invocation = one bounded task.

Junior does not:
- expand scope;
- preempt future tasks;
- change contracts silently;
- call subagents;
- decide product behavior;
- commit/push;
- fix unrelated observations.

## Team task control

Dependent tasks are issued only after prerequisite acceptance.

```text
TASK -> JUNIOR -> LEAD REVIEW
                 |       |
               ACCEPT  CORRECTION
```

## Development gate

QA starts only after all required development Work Orders are `READY_FOR_QA`.

## QA gate

QA validates requirement satisfaction independently and traces evidence to requirements/acceptance criteria.

QA never fixes product code.

## Defect routing

```text
QA JUNIOR
  -> QA LEAD
  -> ORCHESTRATOR
  -> RESPONSIBLE DEVELOPMENT LEAD
  -> DEVELOPMENT JUNIOR
  -> DEVELOPMENT LEAD
  -> ORCHESTRATOR
  -> QA LEAD
  -> QA JUNIOR REGRESSION
```

## Status vocabulary

Development Junior:
- COMPLETED
- FAILED
- BLOCKED

Lead review:
- ACCEPTED
- CORRECTION_REQUIRED
- BLOCKED

Development Work Order:
- READY_FOR_QA
- NEEDS_CORRECTION
- BLOCKED

QA task:
- PASS
- FAIL
- BLOCKED

QA Work Order:
- PASSED
- FAILED
- BLOCKED

Whole requirement:
- COMPLETED
- BLOCKED
- IN_PROGRESS

## Evidence rule

Success requires evidence, not confidence.

## Contract preservation

Lower-level agents may not silently change API/data/UI/integration/business contracts.

## Ambiguity

Material ambiguity affecting behavior, security, money, permissions, or data integrity must return upward rather than being guessed.

## Definition of Done

A requirement is complete only when:
1. refinement is accepted;
2. required Work Orders are completed;
3. Leads reviewed their teams' changes;
4. QA validated mandatory acceptance criteria;
5. regression after corrections passed;
6. no blocking defect remains;
7. unresolved limitations are explicit.

## Future role skills

Technical skills may be added later (React, Next.js, NestJS, PostgreSQL, Playwright, security, etc.). They enhance role capability but do not change this hierarchy.

## Mandatory quality and concurrency controls

Read [Canonical Delivery Contracts](references/contracts.md) before producing delivery artifacts. These controls apply to all roles and supplement their local report templates. Canonical quality and evidence fields are mandatory even when a local template abbreviates them. Task quality is recorded under the top-level quality key alongside task; Lead review and quality_summary accompany result reports.

### Ready to delegate

Every task must identify its requirement and acceptance criteria, bounded edit scope, fixed contracts, accepted prerequisites, risk level, expected outcome, and meaningful validation. Resolve material ambiguity before dispatch. Choose checks based on repository conventions and risk; include relevant negative/boundary cases, security and compatibility checks. Explain checks that are not applicable. Do not create trivial tests merely to populate a checklist.

### Parallel execution

- At most two active Junior invocations per Lead and four active Juniors across the delivery. These are instruction-level limits, not runtime enforcement.
- The Orchestrator assigns explicit Junior slot budgets in Work Orders before dispatch; the sum of budgets for unfinished Work Orders must not exceed four. Unallocated or missing budgets mean sequential execution with one slot, which must still be reserved globally.
- Leads may invoke the same Junior role more than once for independent tasks. Use concurrent task calls only when the runtime supports them; otherwise execute sequentially and report the limitation. Never claim parallel execution without evidence.
- A Lead declares each task's write paths, read dependencies, and exclusive resources (ports, databases, fixtures, generated outputs). Parallel tasks must have disjoint write scopes and must not read artifacts another active task is changing or share exclusive resources.
- Contracts shared across teams must be agreed before dispatch. Cross-team ownership conflicts return to the Orchestrator; uncertain independence requires sequential execution.
- Count an invocation as active until it completes or confirmed cancellation stops it. A timeout alone does not free a slot. A replacement must not overlap an unresolved worker.
- Wait for prerequisite acceptance before launching dependent tasks. Do not overwrite other workers' changes or expand ownership silently.

### Evidence and acceptance

Record validation command/check, working directory, expected behavior, actual result, exit code when applicable, and relevant test counts. Distinguish PASS, FAIL, SKIPPED, NOT_RUN and BLOCKED; an exit code of zero with zero tests is not a passing test suite. Never weaken assertions, disable required checks, or present unexecuted checks as passed.

A Junior's COMPLETED means submitted for review, not accepted. Mandatory failed, blocked or unrun checks prevent COMPLETED and acceptance. The Lead inspects actual scoped changes and evidence, verifies criteria, contracts, error behavior and relevant regressions, and records ACCEPTED, CORRECTION_REQUIRED or BLOCKED with reasons. Reports alone do not substitute for inspecting changes.

Before READY_FOR_QA, the Lead commissions meaningful integration validation of accepted task outputs through a Junior and reviews it. The Orchestrator checks cross-team contract compatibility and requires cross-team integration evidence where applicable before the development gate opens. An integration check may be an existing test or functional request; it must verify expected behavior, not merely a running process.

QA independently maps every mandatory acceptance criterion to observed evidence, includes risk-relevant negative/boundary cases, and reruns affected regression after corrections. Missing prerequisites yield BLOCKED; observed requirement violations yield FAIL/FAILED. Neither can be reported as PASSED.

### Corrections and learning

Corrections identify the failed criterion, observed evidence, diagnosis, bounded scope and regression checks. After two unsuccessful correction attempts for the same task or defect, stop redispatching and escalate to the Orchestrator for diagnosis and replanning. Resume only with a materially revised plan; do not repeat unchanged instructions.

Include counts of Lead rejections, correction attempts, QA defects and recurring causes in Work Order reports. Keep summaries in delivery artifacts; use TODO MCP tools if project tasks are managed and never edit .todo directly. Update shared skills only through an explicitly authorized improvement task, not opportunistically during delivery.

## Administrative error logger

The Orchestrator may delegate directly to `error-logger`, an append-only administrative recorder outside the development hierarchy and Junior slot budgets. Leads report errors/rejections and corrections upward using the [error log contract](../../logs/error-log.md). The logger only records supplied events in `.opencode/logs/errors.jsonl`; it never analyzes, fixes or changes skills. Logging completion is not a delivery gate. Runtime support is required for actual background execution; retain pending events in reports when unavailable. Existing quality summaries remain separate from this factual event history.
