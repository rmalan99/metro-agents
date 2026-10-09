---
name: frontend-tables
version: 1.0.0
description: Framework-independent table and structured-list behavior for any frontend application: columns, queries, selection, record navigation, actions, responsive presentation and validation.
---

# Frontend Tables and Record Lists

## Scope
Load for tables or structured record lists in any app, not only back offices. Apply `../frontend-developer/SKILL.md` and the project's frontend contract. Use the active tool/UI guide for implementation; do not adopt a grid library implicitly.

## 1. Define the data-view contract
Before building, identify stable record identity, source, available fields, volume, user decision, detail route, permitted actions and formatting locale. Determine whether the source supports server search, sort, filtering, paging and bulk operations. Do not simulate full-dataset operations over one fetched page.

Choose a table when users compare common fields; choose cards/list rows for heterogeneous summaries. Provide the same essential information and actions in alternative presentations.

Define each column with field, label, format, importance, alignment and supported sorting/filtering. Put identity and task-critical data first. Keep optional secondary data in details or configurable columns. Right-align comparable numbers and use consistent currency, dates and units.

## 2. Queries and pagination
- Choose client operations only when the complete relevant dataset is available and practical to process. Otherwise apply operations at the source using its supported contract.
- Define query state: search, filters, sort, page/cursor and page size. Persist in URL when sharing, navigation or restoration matters.
- Reset page/cursor after search, filter, sort or page-size changes. Keep previous/next handling consistent with cursor or offset APIs; do not invent totals for cursor-only sources.
- Make search submission or debounce behavior explicit. Ignore/cancel outdated requests so a slower old response cannot replace newer results.
- Show active filters and a clear reset action. Define inclusive/exclusive date boundaries and time zones before sending ranges.
- Sort raw values, not formatted strings. Add a stable tie-breaker when needed for paging.
- Distinguish initial load, background refresh, no records, no matches and failure. Recover without silently clearing the user's query.

Example: changing status on page 5 goes to the first result page; deleting the last item on the final page moves to a valid preceding page rather than showing a misleading empty dataset.

## 3. Record navigation and row actions
Provide an explicit, accessible link to the detail for navigable records. Optional row-click shortcuts must preserve text selection, modifier-key navigation and internal controls; do not use a generic clickable container as the sole destination.

Actions, checkboxes and menus do not trigger detail navigation. Never nest buttons inside an enclosing link. Give icon-only controls accessible names and adequate target size.

Keep the frequent action visible when useful; place secondary actions in an accessible menu. Use brand emphasis for the suggested action and danger for destructive actions. Status badges describe state and are not fake buttons.

## 4. Selection and bulk actions
Add selection only for actual multi-record operations. Key it by stable identity, not row position. Define scope explicitly: visible page, selected IDs across pages or all matching results.

Select-all controls must communicate their scope and mixed state. Filtering or reloading must not silently reinterpret the selection. Define whether selection is retained, reconciled or cleared and explain consequential changes.

For all-matching selection, require backend support and convey exclusions/count when available. Do not send only visible IDs while claiming all matches were processed.

Bulk feedback reports success and failure separately and preserves actionable failed selections where useful. Apply the inherited permission and destructive-action contract to the selected scope.

## 5. Accessibility and adaptation
Use semantic tables with headers and relationships for tabular data. Communicate sort direction on sortable headers. Use a full interactive grid pattern only if spreadsheet-like keyboard behavior is truly required and implemented.

For narrow screens, prioritize columns, allow labeled horizontal scrolling or render record cards. Do not remove identifying data, state or primary action. Sticky headers/columns must not obscure focus or controls.

Virtualize only when measured scale warrants it; check semantics, focus, selection and row identity under recycling. Use the selected library's accessible implementation rather than a partial custom grid.

## 6. Verification
Check supported query combinations, empty/matching-empty states, stale responses, formatting, detail navigation and internal action isolation. When relevant, check selection across pages, partial bulk failure and deletion of the last page item. Verify keyboard sorting/actions, narrow layouts and long values. Execute meaningful tests for these behaviors rather than tests that assert a column array mirrors itself.
