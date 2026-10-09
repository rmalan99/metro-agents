# Project discovery and architecture decisions

Load when establishing/changing the base or when the handed-off project contract does not resolve the task. Reuse accepted decisions; do not repeat full project discovery in every worker.

## Discover before changing

For an existing project:
1. Read applicable instructions and inspect dependency manifests, lockfiles, entry points, navigation and global configuration relevant to the task.
2. Trace one representative feature through presentation, data access, state ownership and validation.
3. Locate adopted UI components, theme, tokens, styles and checks. Distinguish an installed dependency from a system actually used.
4. Identify reusable components and the source of truth for affected data.
5. Identify constraints: tool/version, rendering environment, data contracts, permissions, locales and supported viewports.

For a new project, establish users, tasks, tool constraints, visual references, data source and implementation scope. Ask only for missing decisions that materially alter the result. Do not ask again for decisions already made in the session.

Before structural work, state the adopted base, what will be reused, unresolved material decisions and intended scope. Routine implementation choices do not require a new approval gate.

## Resolve the UI system

Frontend owns selection behavior; candidate libraries and technical setup belong to the active tool's skill.

1. If the user chose a system, check compatibility through that tool's guidance.
2. If a system is already adopted, continue with it unless a change was requested.
3. If several systems coexist, map their responsibilities. Do not migrate unrelated screens.
4. If no choice exists, ask which compatible UI/styling approach to use before installing or generating it. Explain relevant tradeoffs and offer a recommendation tied to the task.
5. If clarification cannot be requested by the current worker, report the missing decision to the authorized coordinator. Continue only independent work; elapsed time is not a choice.

Distinguish a component library from a styling system. Utilities or plain styles do not supply dialog focus management, menu keyboard behavior or other interaction semantics.

Record the selected system, installed version, theme location and any integration constraint. Load its implementation reference only when needed. Do not import another UI library for a convenient individual control.

## Define proportional architecture

Preserve an existing architecture that meets the requirement. In a new project, assign clear responsibilities for entry/navigation, layouts, product features, shared UI, visual configuration and data access using the tool's conventions.

- Shared presentation must not depend on a particular product feature.
- Feature-specific behavior stays with the feature until actual reuse justifies sharing.
- Keep transport and substantial data transformation outside pure presentation.
- Assign each state a source of truth, owner and lifetime before sharing it.
- Keep dependency direction explicit and avoid circular imports.
- Do not create generic abstractions for hypothetical future use.

Before extracting a component, identify the responsibility it owns and at least one concrete gain: behavior consistency, accessibility, reuse or independent comprehension. A wrapper that only renames a library control is usually unnecessary.
