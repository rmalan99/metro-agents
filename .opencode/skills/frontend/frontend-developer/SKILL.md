---
name: frontend-developer
version: 2.2.0
description: Framework-independent frontend owner/router. Resolves project decisions and loads only required technical contracts, tools and specialties; delivery governance remains separate.
---

# Frontend Developer — Core

## Responsibility
Own frontend technical decisions and their canonical references. The active tool implements APIs/files/rendering; specialties extend product behavior. Delivery authority, evidence schemas, statuses and acceptance gates belong to `../../hierarchical-software-delivery/SKILL.md`, not this technical core.

Respect explicit user requirements, applicable project instructions and assigned scope. Use the handed-off project/frontend contract first; inspect affected code and its source of truth before editing. Resolve material missing decisions through the authorized coordinator rather than inventing behavior.

## Single ownership and selective loading
Every rule has one owner. Children inherit it and add only concrete procedures/examples. Do not copy generic workflows or MUST lists into child skills or prompts. Update a shared rule at its owner; resolve conflicting copies rather than adding another override. Project contracts record actual decisions/paths, not copies of instructions.

Load this core once per invocation and only the triggered references below. Another agent's loaded context is not automatically available. Read technical quality for implementation/review; additional specialty acceptance checks stay with that specialty.

| Need / canonical responsibility | Owner to load |
|---|---|
| Missing project decisions, architecture change or UI-system choice | `references/project-discovery.md` |
| Establish or migrate a shared UI baseline/profile | `../ui-system-architect/SKILL.md` |
| Shared theme, tokens or platform-wide visual adjustment | `references/design-system.md` |
| Generate/change components, interactions or adaptable UI | `references/component-contracts.md` |
| State, requests, mutations, permissions or integration/performance | `references/data-and-integration.md` |
| Operation completion, backend failure or result notification | `references/feedback.md` |
| Implement/review/verify frontend work | `references/technical-quality.md` |
| Establish/update persistent project conventions | `references/frontend-contract.template.md` |
| Generate UI or work with its automated selectors | `references/test-identifiers.md` |
| Forms and specialized field behavior/reference selection | `../frontend-forms/SKILL.md` |
| Tables and structured record lists | `../frontend-tables/SKILL.md` |
| Administrative shell and management composition | `../backoffice-design/SKILL.md` |
| Administrative metrics/charts | `../backoffice-dashboards/SKILL.md` |
| React implementation and React UI/concept routing | `../react/react-core/SKILL.md` |

This is the single technical ownership/router table. It is not a preload list. For another tool use its existing project guidance; do not invent unavailable skills. Verify installed versions before consulting tool/library APIs. A reference's presence does not authorize adopting its dependency.

Generated or modified forms trigger both `references/component-contracts.md` and `../frontend-forms/SKILL.md`: the component contract owns the shared base and icon policy; the form contract owns field behavior and variants. Loading the form specialty is not permission to skip the shared component contract.

Any create/update/delete/submit flow or backend-result feedback also triggers `references/feedback.md`. The feedback contract owns `ModalAlert`, channel selection and the native-alert/toast prohibition; feature and form contracts only supply operation-specific messages and field mappings.

When adding a specialty, identify its unique responsibility and trigger. Reference inherited requirements instead of restating them; retain useful technical detail under task-driven references. For a bounded fix, extend the existing base without an unrelated reorganization or parallel visual system.
