# Backoffice profile V1

Use this profile for authenticated operational interfaces centered on records, workflows, configuration, permissions, reporting, or supervision. Apply [`backoffice-design`](../../../../backoffice-design/SKILL.md) for administrative composition and load forms, tables, or dashboard specialties only when the task triggers them.

## Selective loading

| Work | Load |
|---|---|
| Buttons, fields, cards, modal, or table geometry | [`components.md`](components.md) |
| Selection controls or status labels | [`controls.md`](controls.md) |
| Alerts, operation results, overlays, or transient feedback | [`feedback-overlays.md`](feedback-overlays.md) |
| Sidebar, app bar, tabs, menus, breadcrumbs, or pagination | [`navigation.md`](navigation.md) |
| Loading, empty, identity, files, dates, or auxiliary data views | [`data-content.md`](data-content.md) |
| Field groups, headers, filters, or table framing | [`compositions.md`](compositions.md) |
| List, create, edit, or detail screen | [`patterns.md`](patterns.md) plus required composition contracts |
| Shell or responsive transformation | [`layouts.md`](layouts.md) |

Default classification is `surface=backoffice`, `platform=responsive-web`, `composition=data-heavy|transactional`, and `density=default`. Change composition or density only from task evidence and persist the choice.

The profile does not own form behavior, table querying, dashboard meaning, operation-result feedback, or framework bindings. Their existing specialty contracts remain authoritative.
