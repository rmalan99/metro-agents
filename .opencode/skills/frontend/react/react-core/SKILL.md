---
name: react-core
version: 2.2.0
description: Compact core of the React Frontend Developer standard. Contains always-on React rules and an index that routes deeper topics to child skills derived from the original skill.
---

# React Frontend Developer — Core

## Purpose

Use this skill as the **main React skill**. It is the compact entry point for the full React Frontend Developer standard.

For frontend work, load `../../frontend-developer/SKILL.md` as the framework-independent base. This skill translates that contract into React; it does not own a second visual system or a competing architecture. If the base was already loaded, do not reload it unnecessarily.

It must stay small. Its job is to:

1. define the React rules that always apply,
2. preserve the decision model of the original skill,
3. identify which original section is relevant to the current task,
4. load only the child skill that contains the deeper guidance for that concept.

Do **not** load every child skill by default. Do **not** introduce a library, framework, or architectural tool merely because a child skill exists. The current project stack and explicit technical decisions remain authoritative.

---

## Always-on React rules

### MUST

- Treat components and Hooks as pure during render.
- Build UI declaratively from props, state, context, and derived values.
- Prefer composition and clear domain/component boundaries.
- Review large components for meaningful subcomponents; hundreds of lines of JSX are a design signal, not something to ignore.
- Keep state at the narrowest correct owner.
- Derive values instead of duplicating state when possible.
- Use Effects only for synchronization with external systems.
- Avoid prop drilling when data belongs to a page/domain subtree; use the state-management guidance to choose the correct owner.
- Respect the existing project architecture, conventions, design system, and dependencies.
- Reuse existing components, hooks, utilities, and patterns before creating new abstractions.
- Make the smallest safe change that completely satisfies the requirement.
- Preserve type safety, accessibility, important UI states, and testability.
- Apply the general `data-testid` contract to every explicitly generated DOM element. Forward identifiers through custom components to native roots/slots and give repeated instances stable scopes; React `key` is not a DOM selector.

### MUST NOT

- Mutate props, state, context, store data, or render inputs.
- Perform side effects during render.
- Use `useEffect` to calculate values that can be derived during render.
- Duplicate a source of truth without a lifecycle/ownership reason.
- Put local/page-specific state into global state without a cross-module requirement.
- Pass the same domain object through unrelated intermediate components only to reach deep descendants.
- Add dependencies or new architectural technologies unless they are already part of the project or explicitly selected for the task.
- Refactor unrelated code unless required for correctness.

---

## How to use the child skills

### UI system selection and integration

The selection behavior belongs to `frontend-developer`; React owns compatible options and integration. Inspect the actual React framework, installed versions, stylesheet strategy, providers and adopted UI components before deciding.

- Keep the existing system or explicit user choice. If no choice exists, ask through the authorized channel before setup; do not repeatedly ask after selection.
- Offer compatible approaches: MUI, shadcn/ui, Chakra UI, Tailwind without a component library, or plain CSS. MUI/Chakra provide themed components; shadcn supplies project-owned component code; Tailwind/CSS provide styling, not full interactive behavior.
- Load only `references/ui/<selected-system>.md` for setup, shared styling or library-specific component work. Do not preload all five guides.
- Establish native theme/tokens and application-level providers only where required. Respect server/client boundaries, style insertion, portal inheritance and hydration in the installed framework.
- Use the existing hooks, modules and data tools to implement the base's ownership rules. Derived state stays derived; Effects synchronize external systems.
- Before adding dependencies, review compatibility, maintenance and the actual missing capability. Preserve the current dependency policy.

| Selected system | Reference |
|---|---|
| MUI | `references/ui/mui.md` |
| shadcn/ui | `references/ui/shadcn.md` |
| Chakra UI | `references/ui/chakra.md` |
| Tailwind without component library | `references/ui/tailwind.md` |
| Plain CSS | `references/ui/css.md` |


References are version-aware procedures, not permission to migrate the application. Consult the installed version's official documentation for exact APIs when needed.

Start with this file. Inspect the task and the affected code. Then use the index below to load **only** the child skill that owns the relevant concept.

A task may require more than one child skill, but loading must be driven by the task itself.

Example:

```text
Change a detail page with a very large component
→ react-core
→ react-architecture-components

Nested detail sections need the same stable resource
→ react-core
→ react-architecture-components
→ react-state-management

Bug caused by an incorrect Effect
→ react-core
→ react-hooks-effects-events
```

---

## Original skill index

The original React skill had 30 numbered sections. Sections 1–2 are represented directly by this compact core. Sections 3–30 live in the child skills below.

| Original section | Topic | Load child skill |
|---:|---|---|
| 1 | Purpose | `react-core` |
| 2 | Core React Principles | `react-core` |
| 3 | Before Writing Code | `react-architecture-components` |
| 4 | React Project Architecture | `react-architecture-components` |
| 5 | Component Design | `react-architecture-components` |
| 6 | Props | `react-architecture-components` |
| 7 | State Management and Data Ownership | `react-state-management` |
| 8 | State Structure Rules | `react-state-management` |
| 9 | Hooks | `react-hooks-effects-events` |
| 10 | `useEffect` | `react-hooks-effects-events` |
| 11 | Events | `react-hooks-effects-events` |
| 12 | Data Fetching and APIs | `react-data-types-forms` |
| 13 | TypeScript | `react-data-types-forms` |
| 14 | Forms | `react-data-types-forms` |
| 15 | Lists and Keys | `react-rendering-ui-accessibility` |
| 16 | Conditional Rendering | `react-rendering-ui-accessibility` |
| 17 | Styling and Design System | `react-rendering-ui-accessibility` |
| 18 | Accessibility | `react-rendering-ui-accessibility` |
| 19 | Performance | `react-performance-errors-security` |
| 20 | Error Handling | `react-performance-errors-security` |
| 21 | Security | `react-performance-errors-security` |
| 22 | Testing Strategy | `react-testing-quality-workflow` |
| 23 | Code Quality Rules | `react-testing-quality-workflow` |
| 24 | Dependency Policy | `react-testing-quality-workflow` |
| 25 | Implementation Workflow | `react-testing-quality-workflow` |
| 26 | Pull Request / Review Checklist | `react-testing-quality-workflow` |
| 27 | Anti-Patterns | `react-testing-quality-workflow` |
| 28 | Decision Rules | `react-testing-quality-workflow` |
| 29 | Definition of Done | `react-testing-quality-workflow` |
| 30 | Guiding Principle | `react-testing-quality-workflow` |

---

## Routing by concept

| Current task involves... | Load |
|---|---|
| Project structure, component decomposition, page/detail composition, props, component contracts | `react-architecture-components` |
| `useState`, lifted state, Context, Redux, domain state, ownership, prop drilling | `react-state-management` |
| Hooks, custom/domain hooks, `useEffect`, synchronization, events | `react-hooks-effects-events` |
| API data, TypeScript boundaries, forms | `react-data-types-forms` |
| Lists, keys, conditional rendering, styling, design system, accessibility | `react-rendering-ui-accessibility` |
| Rendering performance, memoization, errors, security | `react-performance-errors-security` |
| Tests, code quality, dependencies, implementation/review workflow, anti-patterns, Definition of Done | `react-testing-quality-workflow` |

---

## Core decision model

When making a React decision, prefer this order:

```text
Understand existing code and source of truth
        ↓
Choose the smallest correct ownership scope
        ↓
Create clear component/domain boundaries
        ↓
Use React primitives before unnecessary abstraction
        ↓
Reuse the project's established patterns
        ↓
Implement the smallest safe change
        ↓
Verify behavior, edge states, accessibility, and tests
```

When deeper guidance is needed, follow the index instead of expanding this core.
