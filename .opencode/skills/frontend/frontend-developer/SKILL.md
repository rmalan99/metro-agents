---
name: frontend-developer
version: 1.1.0
description: Framework-independent frontend workflow, architecture boundaries, shared visual system, UI selection behavior, and quality contract. Routes tool-specific implementation and product specialties only when needed.
---

# Frontend Developer — Core

## Responsibility and boundaries

Use this skill for frontend work regardless of framework. Establish a coherent technical and visual base that tool-specific and product skills extend.

Own the process for discovery, architecture decisions, UI-system selection, design tokens, component responsibilities, data-state requirements, accessibility, and verification. Delegate concrete APIs, files, initialization, lifecycle, rendering, and library integration to the tool-specific skill.

Do not prescribe React, a CSS engine, an application framework, a folder template, or a dependency. Do not rebuild a project to satisfy a local change. Scale discovery and documentation to the affected scope.

Explicit user requirements take priority over skill defaults. Follow applicable project instructions and preserve existing conventions unless changing them is necessary or requested. Skills do not override assigned worker scope, dependency policy, or delivery authority.

## 1. Discover before changing

For an existing project:
1. Read applicable instructions and inspect dependency manifests, lockfiles, entry points, navigation and global configuration relevant to the task.
2. Trace one representative feature through presentation, data access, state ownership and validation.
3. Locate adopted UI components, theme, tokens, styles and checks. Distinguish an installed dependency from a system actually used.
4. Identify reusable components and the source of truth for affected data.
5. Identify constraints: tool/version, rendering environment, data contracts, permissions, locales and supported viewports.

For a new project, establish users, tasks, tool constraints, visual references, data source and implementation scope. Ask only for missing decisions that materially alter the result. Do not ask again for decisions already made in the session.

Before structural work, state the adopted base, what will be reused, unresolved material decisions and intended scope. Routine implementation choices do not require a new approval gate.

## 2. Resolve the UI system

This behavior stays in the core; candidate libraries and technical setup belong to the active tool's skill.

1. If the user chose a system, check compatibility through that tool's guidance.
2. If a system is already adopted, continue with it unless a change was requested.
3. If several systems coexist, map their responsibilities. Do not migrate unrelated screens.
4. If no choice exists, ask which compatible UI/styling approach to use before installing or generating it. Explain relevant tradeoffs and offer a recommendation tied to the task.
5. If clarification cannot be requested by the current worker, report the missing decision to the authorized coordinator. Continue only independent work; elapsed time is not a choice.

Distinguish a component library from a styling system. Utilities or plain styles do not supply dialog focus management, menu keyboard behavior or other interaction semantics.

Record the selected system, installed version, theme location and any integration constraint. Load its implementation reference only when needed. Do not import another UI library for a convenient individual control.

## 3. Load knowledge selectively

| Task | Load |
|---|---|
| React implementation | `../react/react-core/SKILL.md`, then only the relevant child |
| Translate a reference into a shared theme | `references/design-system.md` |
| Establish persistent frontend conventions | `references/frontend-contract.template.md` |
| Generate UI elements or verify automated selectors | `references/test-identifiers.md` |
| Tables or structured record lists in any app | `../frontend-tables/SKILL.md` |
| Forms, reactive validation or specialized fields | `../frontend-forms/SKILL.md` |
| Administrative shell, navigation or management views | `../backoffice-design/SKILL.md` |
| Administrative metrics and charts | `../backoffice-dashboards/SKILL.md` |

The table is a router, not a preload list. Tool skills must route their own setup/theming/components/troubleshooting knowledge. For another tool, inspect its existing project guidance; do not invent an unavailable skill or claim it was loaded.

Read only references required by a concrete decision, implementation or failure. Verify APIs against installed versions and official documentation when uncertain. A reference's existence does not authorize adopting its technology.

## 4. Define proportional architecture

Preserve an existing architecture that meets the requirement. In a new project, assign clear responsibilities for entry/navigation, layouts, product features, shared UI, visual configuration and data access using the tool's conventions.

- Shared presentation must not depend on a particular product feature.
- Feature-specific behavior stays with the feature until actual reuse justifies sharing.
- Keep transport and substantial data transformation outside pure presentation.
- Assign each state a source of truth, owner and lifetime before sharing it.
- Keep dependency direction explicit and avoid circular imports.
- Do not create generic abstractions for hypothetical future use.

Before extracting a component, identify the responsibility it owns and at least one concrete gain: behavior consistency, accessibility, reuse or independent comprehension. A wrapper that only renames a library control is usually unnecessary.

## 5. Establish the shared visual base

Extract the requested visual style into surfaces, hierarchy, density, contrast, spacing, borders, radii, shadows and action emphasis. Compare it with the existing system before editing screens.

Use the active tool/library's native theme mechanism to define semantic colors and shared typography, spacing, sizes, layers and motion where applicable. Reuse existing tokens with the correct meaning; do not create aliases for every local value.

Place changes by scope:

| Change affects | Owner |
|---|---|
| Entire application | Theme or global base |
| Every instance of one component | Component defaults/overrides |
| Repeated intentional treatment | Named component variant |
| Product-specific behavior | Shared product component |
| One screen's composition | Local layout |

Adjust the base when a requested style should propagate throughout the platform. Do not patch the same inconsistency screen by screen. Validate representative controls and overlays before spreading the theme. Load the design-system reference for the procedure.

## 6. Specify component and interaction contracts

Reuse project components first, then adopted library primitives, then add only the missing composition or behavior.

For each affected interactive component establish:
- Inputs, outputs and responsibility.
- Relevant default, hover, focus, active, disabled, loading and error states.
- Navigation versus action semantics.
- Responsive behavior and keyboard interaction.
- Data/permission prerequisites and behavior when they are unavailable.

Use links for destinations and buttons for actions. Do not nest interactive controls. Preserve the semantics and accessibility of the chosen primitives instead of replacing them for styling convenience.

### Mandatory generated-element test identifiers

Every DOM element explicitly generated by an agent in new or modified UI must expose a stable `data-testid`, including component roots, layout wrappers, text, icons, controls and feedback states. Non-DOM components expose/forward an identifier to their rendered elements; their name alone is not a selector. Preserve existing identifiers and follow `references/test-identifiers.md` for naming, repeated instances, library slots and QA handoff.

Apply this within the assigned scope; do not bulk-rewrite unrelated legacy UI or mutate third-party internal markup. Report any unaddressable generated element with its reason. Identifiers are an automation contract, not substitutes for semantics, accessible names or behavioral assertions.

## 7. Data, state and forms

Choose ownership by consumers and lifetime: interaction-local, shared application, remote/server or URL state. The tool skill supplies mechanisms; do not prescribe stores or hooks here.

- Define initial loading, empty data, filtered-empty, recoverable error, success and denied-access states where relevant.
- Prevent duplicate submissions and stale responses from overwriting newer results.
- Retain useful data during recoverable refresh failures when safe; label freshness when it matters.
- Forms require visible labels, validation rules, associated errors and submission feedback.
- Apply `../frontend-forms/SKILL.md` for every generated/modified form: reactive dirty/touched validation, inline danger feedback, required markers, helper/placeholder support, backend field-error mapping and failed-submit field reveal. Tool-specific adapters implement this same contract without changing its behavior.
- Protect unsaved changes where losing them is consequential.
- Do not invent endpoints or represent demonstration data as production data.
- Hidden controls are not authorization. Enforce permissions at the trusted boundary when a backend exists.

## 8. Responsive and accessible behavior

Adapt tasks and composition, not just font sizes. Specify changes to navigation, grids, forms, data views, overlays and primary actions. Preserve essential information on smaller screens.

Verify semantics, heading hierarchy, accessible names, keyboard reachability, visible focus and status feedback. Manage overlay focus according to its pattern; return focus on close where appropriate. Do not rely only on color.

Target WCAG AA contrast: 4.5:1 for normal text, 3:1 for large text and relevant non-text controls. Honor reduced-motion preferences for significant motion. Validate with real content, long labels and relevant locale formatting.

## 9. Integration and performance

Respect the tool's execution/rendering model. Keep secrets out of delivered frontend code. Add dependencies only for a demonstrated capability and under existing dependency rules.

Avoid duplicate requests, unnecessarily global modules and disproportionate assets. Use code splitting, virtualization or memoization when scale or measurement warrants it; use the tool's specialized guidance rather than generic optimization rituals.

## 10. Persist the frontend contract

Reuse existing project documentation. When establishing or changing a shared base, record decisions using `references/frontend-contract.template.md` if necessary. For a small fix, update only affected existing conventions.

Record actual file locations, responsibilities, tokens, component-extension rules, data conventions and verification commands. Never fill unknown fields with invented answers.

Specialty skills consult this contract and update it when an authorized change affects shared decisions. They must not introduce parallel themes or silently change stack, architecture or requirements.

## 11. Verify and report

Run project-required checks and meaningful validation for affected behavior. Include negative/edge states, viewport adaptation and keyboard interaction relevant to the change. Add tests for significant behavior, not assertions that merely reproduce implementation.

Report what changed, why shared decisions mattered, checks actually executed and material limitations. Distinguish passed, failed and unexecuted checks. Do not claim visual verification from a text-only inspection.

For generated UI, verify identifier coverage, stability, correct DOM placement and unambiguous scoped selection. Hand off selector patterns and exceptions so QA can reuse them rather than inventing selectors. Missing required identifiers remain a defect; do not claim this contract passed from source inspection alone.

Done means the requested scope works, shared conventions are preserved or intentionally updated, required checks pass, and remaining limitations are explicit.
