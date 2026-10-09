# Frontend skills

## Entry and responsibility

`frontend-developer` is the framework-independent base: discovery, UI-selection behavior, architecture boundaries, shared visual system, frontend contract and quality criteria. It does not prescribe React APIs or a UI library.

For React work, also load `react-core`. It translates the base into React and routes existing concept-specific child skills. For other tools, use their existing project guidance; this package does not claim adapters that are not implemented.

## Load only what the task needs

| Scope | Skill/reference |
|---|---|
| General frontend base | `frontend-developer/SKILL.md` |
| Shared theme from visual requirements | `frontend-developer/references/design-system.md` |
| Operation results and backend failure feedback | `frontend-developer/references/feedback.md` |
| Persistent conventions | `frontend-developer/references/frontend-contract.template.md` |
| Stable generated-element selectors for development and QA | `frontend-developer/references/test-identifiers.md` |
| React entry and UI integration | `react/react-core/SKILL.md` |
| React concepts | Relevant existing child from the `react-core` index |
| Tables/lists in any application | `frontend-tables/SKILL.md` |
| Forms/fields in any application | `frontend-forms/SKILL.md` |
| Administrative composition | `backoffice-design/SKILL.md` |
| Administrative metrics/charts | `backoffice-dashboards/SKILL.md` |

The five UI implementation references live under `react/react-core/references/ui/`: MUI, shadcn/ui, Chakra, Tailwind and CSS. Read only the adopted/selected system when setup, theming, component work or diagnosis requires it. Verify installed versions before applying APIs. Existence of a guide does not authorize installing its library.

## Rule ownership

The ownership table and task router in `frontend-developer` are canonical. The React concept router lives only in `react-core`; do not maintain a duplicate concept index here. General form behavior/references belong to `frontend-forms`, while operation-result channel selection and `ModalAlert` belong to the frontend feedback contract, not React.

Child skills add procedures specific to their responsibility and inherit general instructions without copying them. Prompts add role authority/handoff, and project contracts record actual decisions rather than reproducing skill rules. Reuse already-loaded context.

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
