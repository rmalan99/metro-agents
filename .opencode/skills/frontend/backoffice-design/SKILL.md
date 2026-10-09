---
name: backoffice-design
version: 1.0.0
description: Administrative layout and workflow composition: predefined structures, persistent or collapsible sidebar, app bar, authenticated user menu, child zones, cards and visual focus.
---

# Back Office Design

## Responsibility
Apply `../frontend-developer/SKILL.md` and the project's frontend contract. Own administrative composition, not framework architecture or a parallel theme. Load `../frontend-tables/SKILL.md` only for data views and `../backoffice-dashboards/SKILL.md` only for administrative dashboards.

Identify users, frequent tasks, modules, entities, roles and source of data. Declare the chosen structure, sidebar mode, app bar treatment, density and main action before substantial layout work. Reuse the native theme and shared components.

## 1. Choose a structure by need

| Structure | Composition | Choose when |
|---|---|---|
| Classic administration | Expanded light sidebar, discreet app bar, list/form content | Labels and module discovery matter |
| Highlighted navigation | Dark palette-derived sidebar, contrasting icons/text, clear content | Navigation needs separation from workspace |
| Focused content | Neutral/dark outer frame and dominant continuous light workspace | A limited task or summary needs attention |
| Compact operation | Collapsible icon rail and broad workspace | Frequent users and wide data views |
| Modular overview | Top indicators, main analytical zone, secondary activity | Daily supervision and prioritization |
| Transactional list | Filters, aligned rows/cards, status and next action | Invoices, payments, requests or orders |

Combine compatible patterns, such as highlighted navigation with transactional lists, while keeping one shared visual system. Do not choose by visual novelty alone. A focused frame must not squeeze a wide table into a narrow reading column.

## 2. Sidebar
Separate persistence from expansion: a sidebar can remain visible while expanded or collapsed and have its own scroll area.

- Expanded: use when labels/submenus aid understanding. Typical starting width 240–280px, adjusted to content and tokens.
- Collapsible: use when workspace width matters. Typical icon rail 64–80px. Offer an explicit toggle, accessible icon labels and tooltips reachable by keyboard and pointer.
- Keep the user's choice when practical. Do not unexpectedly collapse during a task.
- At narrow widths, use a temporary drawer with appropriate focus containment, Escape close and return focus.
- Dark backgrounds use a suitable dark tone from the palette, with foreground tokens verified against it. Do not simply apply the primary action color to every surface.
- Active item has a distinguishable background/highlight and foreground. Use current-page semantics on its link. Distinguish hover and keyboard focus from current route.
- Group by user task; headings and badges must add orientation or useful counts.
- Submenu disclosures communicate expanded state. Keep the active route's ancestor open. Prefer one submenu level; deeper structures need local navigation or breadcrumbs.

## 3. App bar and authenticated user
Use a transparent app bar over a uniform surface or a distinct surface with a subtle separator when separation helps. Avoid duplicate page titles. Include global search and notifications only if their behavior is defined.

Provide avatar/name where space permits and an accessible dropdown with Profile and Sign out, including icons. Separate Sign out visually and use the shared danger treatment with readable contrast. Do not invent a second danger color locally.

Menu keyboard behavior, outside dismissal, Escape and focus return follow the selected component pattern. If implemented as a menu, support its menu keyboard model; if a popover of ordinary links, keep normal link semantics. Closing must not accidentally trigger the underlying control.

Sign out uses the authentication mechanism and takes the user to the appropriate access view. Protect consequential unsaved changes. Do not treat hiding the avatar as logout.

## 4. Parent and child zones
Default ordering:
1. Context/breadcrumbs where needed.
2. Page title and primary action.
3. Local tools: filters, search or tabs.
4. Main content.
5. Related secondary content.

Child zones must answer a task of their parent: detail sections, related records, tabs or an auxiliary panel. Use headings, proximity and dividers rather than repeated card nesting. Global actions belong in the page header, section actions beside their section, record actions with the record.

Keep secondary information visually subordinate. Avoid repeating the title or announcing visible facts in help text; explain format, consequence or scope instead.

## 5. Cards and visual focus
Use theme tokens for subtle borders, consistent radii, spacing and hierarchy. Starting card padding/gap may be 16–24px, but the shared scale is authoritative. Align comparable cards' titles, values and edges. Use light shadows when elevation clarifies layers, not on every block.

For focused content, reduce competition in navigation/secondary zones, create one dominant surface and concentrate emphasis on priority information/actions. Do not hide context required to complete the task.

Every card representing a navigable record offers clear detail access. Informational metrics are navigable only when there is a meaningful destination. Use accessible links without enclosing independent buttons/menus inside them. Internal actions must not open the detail. Add hover/focus feedback without requiring it to discover the link.

Suggested actions use primary emphasis and explicit verbs. Status is separate from action. A pending payment is not automatically a dangerous/destructive state.

## 6. Administrative acceptance
Use the general frontend state/permission contract for requested management flows; apply the administrative checks below.

Check active route and submenu, sidebar expansion, mobile drawer, app bar, user menu, profile/logout integration, record detail and local actions. Review spacing/type consistency, long labels, keyboard focus and secondary-zone hierarchy. Use representative data and clearly label demonstration sources. Report unimplemented integrations explicitly.
