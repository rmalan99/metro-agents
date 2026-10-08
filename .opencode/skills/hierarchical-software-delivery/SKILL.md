---
name: hierarchical-software-delivery
description: Strict hierarchical software-delivery workflow covering requirement refinement, orchestration, Lead planning/review, disposable Junior execution, independent QA, gates, corrections, and completion rules.
compatibility: OpenCode
metadata:
  architecture: hierarchical
  version: "2.0.0"
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
