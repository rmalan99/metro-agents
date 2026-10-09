---
name: react-core
version: 2.3.0
description: React-specific render invariants, compatible UI integration and task-driven routing to concept skills. Inherits the general frontend contract without repeating it.
---

# React Core

## Inheritance
Use `../../frontend-developer/SKILL.md` as the frontend base; load it once if not already available. Its workflow, shared visual decisions, component contracts and quality requirements remain authoritative. This skill owns React mechanics only.

## React render invariants
- Components and Hooks are pure during render; never mutate props, state, context or other render inputs.
- Describe UI from props/state/context. Derive calculated values during render rather than copying them into state through an Effect.
- Effects synchronize external systems; user-triggered operations belong in event handlers.

Detailed procedures belong to the concept owner below. Do not copy them into this entry point.

## React UI compatibility and integration
The frontend base owns selection behavior. React supplies these compatible approaches:
- MUI and Chakra: themed React component libraries.
- shadcn/ui: project-owned components and primitive composition.
- Tailwind or CSS: styles requiring explicit React interaction implementation.

Inspect the actual React framework/version before configuring providers, stylesheet insertion, client/server boundaries or hydration. Exact configuration belongs to the selected reference.

| Adopted system | Load only if setup/theme/component integration requires it |
|---|---|
| MUI | `references/ui/mui.md` |
| shadcn/ui | `references/ui/shadcn.md` |
| Chakra UI | `references/ui/chakra.md` |
| Tailwind | `references/ui/tailwind.md` |
| Plain CSS | `references/ui/css.md` |

## Concept routing
| React task | Owner |
|---|---|
| Feature folders, JSX decomposition, props and component boundaries | `../react-architecture-components/SKILL.md` |
| useState/useReducer, Context, URL mapping, Redux or query-state exposure | `../react-state-management/SKILL.md` |
| Hook APIs, external synchronization, dependency cleanup and events | `../react-hooks-effects-events/SKILL.md` |
| React data/type boundaries and form event/ref binding | `../react-data-types-forms/SKILL.md` |
| Keys, conditional rendering, attribute/ref forwarding and portal semantics | `../react-rendering-ui-accessibility/SKILL.md` |
| Profiler/memoization, error boundaries or untrusted React HTML | `../react-performance-errors-security/SKILL.md` |
| React test harness, scheduler/Strict Mode regressions and test isolation | `../react-testing-quality-workflow/SKILL.md` |

Read only the relevant owner(s); do not preload this table. Product behavior and generic selectors/forms remain routed by frontend, not by React. Reuse already-loaded instructions.
