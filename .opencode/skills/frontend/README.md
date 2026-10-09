# Frontend skills

## Entry and responsibility

`frontend-developer` is the framework-independent base: discovery, UI-selection behavior, architecture boundaries, shared visual system, frontend contract and quality criteria. It does not prescribe React APIs or a UI library.

For React work, also load `react-core`. It translates the base into React and routes existing concept-specific child skills. For other tools, use their existing project guidance; this package does not claim adapters that are not implemented.

## Load only what the task needs

| Scope | Skill/reference |
|---|---|
| General frontend base | `frontend-developer/SKILL.md` |
| Shared theme from visual requirements | `frontend-developer/references/design-system.md` |
| Persistent conventions | `frontend-developer/references/frontend-contract.template.md` |
| Stable generated-element selectors for development and QA | `frontend-developer/references/test-identifiers.md` |
| React entry and UI integration | `react/react-core/SKILL.md` |
| React concepts | Relevant existing child from the `react-core` index |
| Tables/lists in any application | `frontend-tables/SKILL.md` |
| Forms/fields in any application | `frontend-forms/SKILL.md` |
| Administrative composition | `backoffice-design/SKILL.md` |
| Administrative metrics/charts | `backoffice-dashboards/SKILL.md` |

The five UI implementation references live under `react/react-core/references/ui/`: `mui.md`, `shadcn.md`, `chakra.md`, `tailwind.md`, `css.md`. Read only the adopted/selected system when setup, theming, component work or diagnosis requires it. Verify installed versions before applying APIs. Existence of a guide does not authorize installing its library.

## React concept skills
- `react-architecture-components` — discovery, architecture, composition and props.
- `react-state-management` — ownership, state shape and sharing.
- `react-hooks-effects-events` — Hooks, synchronization and events.
- `react-data-types-forms` — APIs, typing and forms.
- `frontend-forms/references/form-integration.md` — shared form integration procedure, owned and routed by frontend.
- `frontend-forms/references/ui/` — selected-system field integration, loaded only as required by form work.
- `react-rendering-ui-accessibility` — lists, rendering, styles and accessibility.
- `react-performance-errors-security` — performance, errors and security.
- `react-testing-quality-workflow` — testing, dependency policy and delivery.

## Runtime integration

Frontend Lead and Junior prompts load the general core; their skill permissions explicitly allow these frontend skills and the existing React modules. Other agent permissions remain unchanged. Missing essential choices are escalated through the existing Orchestrator rather than silently resolved by a worker without question authority.

Examples:

```text
React invoice list with existing MUI
→ frontend-developer → react-core → frontend-tables
→ MUI reference only if library-specific implementation needs it

Administrative shell without charts
→ frontend-developer → tool skill → backoffice-design

Dashboard with pending-record table
→ frontend-developer → tool skill → backoffice-design
→ backoffice-dashboards → frontend-tables
```

These are task-driven routes, not mandatory preloads. Reuse an already-loaded contract and preserve bounded assignment scopes.
