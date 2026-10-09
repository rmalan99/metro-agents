---
name: hierarchical-software-delivery
description: Delivery governance and role router: strict hierarchy, acceptance gates and selective canonical contracts. Technical quality belongs to the relevant domain skill.
compatibility: OpenCode
metadata:
  architecture: hierarchical
  version: "3.0.0"
---

# Hierarchical Software Delivery

## Authority and invariants
User → Orchestrator → Evaluator or team Lead → assigned Junior. QA defects return through its Lead and Orchestrator to the responsible development Lead.

- Evaluator defines WHAT, without implementation design.
- Orchestrator assigns team outcomes and gates, without source-code work or granular edit tasks.
- Leads plan, delegate and inspect actual changes; they never edit code.
- One Junior invocation executes one bounded task and stops. It cannot expand scope, invent product decisions, change contracts silently, delegate, commit or push. Juniors communicate through their own Lead.
- QA validates independently and never fixes production code.
- Material ambiguity returns upward. Preserve imposed contracts and resolve uncertainty before dependent work.

## Rule ownership and role loading
Delivery authority, statuses, evidence, concurrency and acceptance are owned here and in the references below. Technical skills own implementation quality and cannot redefine delivery completion. Prompts state only role-specific input, scope and dispatch destinations.

Load this core once per agent invocation, then only the active role reference. Context loaded by another invocation is not assumed to be available. Schemas are single-source: follow the role's artifact links when producing/consuming them, not every schema.

| Active role | Reference |
|---|---|
| Orchestrator | [Orchestration](references/roles/orchestrator.md) |
| Evaluator | [Refinement](references/roles/evaluator.md) |
| Frontend/backend Lead | [Development Lead](references/roles/development-lead.md) |
| Frontend/backend Junior | [Development Junior](references/roles/development-junior.md) |
| QA Lead | [QA Lead](references/roles/qa-lead.md) |
| QA Junior | [QA Junior](references/roles/qa-junior.md) |

## Delivery gates
Development opens QA only after every required Work Order has reviewed integration evidence and is READY_FOR_QA. QA independently traces mandatory acceptance criteria to evidence and verifies affected regression after corrections.

Whole-requirement COMPLETED requires accepted refinement, accepted development, passed mandatory QA and no blocking defect; limitations remain explicit. A development task's COMPLETED is not whole-delivery completion. Missing prerequisites yield BLOCKED; observed failed requirements yield the artifact's failure status.

Whole-requirement reporting uses COMPLETED, BLOCKED or IN_PROGRESS.

[Quality and acceptance](references/quality.md) owns readiness, evidence and corrections. [Concurrency](references/concurrency.md) owns slot allocation and safe parallel work. Read them only for roles/actions that require them, as routed below.

## Administrative logging
Error logging is an administrative exception outside Junior slot budgets and never a delivery gate. The Orchestrator supplies the [Error log contract](../../logs/error-log.md) and reported events to error-logger. Read it only when reporting/dispatching events. The logger does not load this skill; it receives its contract in the task.

Use TODO MCP when managing project TODOs. Shared-skill improvements require an explicitly authorized improvement task.
