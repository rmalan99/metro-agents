# Generated UI test-identifier contract

## Ownership and coverage

This framework-independent contract applies to frontend development and QA. Load it when agents generate UI or create/verify selectors for that UI.

Every DOM element explicitly emitted by agent-authored UI carries `data-testid`: component roots, layout containers, headings, text wrappers, labels, inputs, links, buttons, icons, table cells, status messages and overlays. Identifiers must reach rendered DOM, not remain on an abstract component prop.

Fragments, providers, hooks and text nodes without an element cannot carry attributes. Do not add wrapper elements just to label them. Stylesheets, scripts and non-UI document configuration are outside this UI-element contract.

For adopted library components, label their publicly addressable roots and slots through supported APIs. Do not patch private third-party internals, inject attributes through DOM traversal or copy vendor components solely for coverage. Report inaccessible slots as bounded exceptions. Project-owned/generated component source is within this contract; preserve its semantics when adding attributes.

Apply the rule to new elements and UI elements touched by the assigned change. Do not silently expand a local task to label every legacy screen. Record legacy gaps relevant to QA separately.

## Stable naming

Use the project's existing stable convention when compatible. For a new convention use lowercase kebab-case:

`<feature>-<component-instance>-<element-purpose>`

Examples: `users-editor-root`, `users-editor-name-input`, `users-editor-save-button`, `users-editor-error-message`.

- Name by responsibility, not appearance, DOM position or current value.
- Preserve names across rerenders, copy changes, styling, sorting and state changes.
- Never derive names from random numbers, timestamps, array positions, translated labels, CSS classes, framework-generated IDs or private/personal data.
- Use opaque stable fixture/domain identity only when safe and already available to the UI; otherwise scope through a stable instance contract.
- Keep a control's ID unchanged when it becomes disabled/loading. Distinct conditional feedback elements get their own purpose-specific IDs.
- Treat renaming/removing an ID as a selector-contract change: identify consumers and update affected tests or report the migration.

## Repeated components

Each component instance has an explicit stable scope. A shared component must accept a scope/identifier through the project's normal attribute or prop mechanism and forward/derive it for its owned DOM elements. Do not hard-code one global ID into a component used several times.

Two supported patterns:
1. Unique instance prefixes, e.g. `invoice-a7-open-button` and `invoice-b8-open-button`.
2. Unique row/container IDs with repeated child-purpose IDs, e.g. row `invoice-a7` containing `invoice-open-button`. QA must query the row first, then the child.

For the second pattern, duplicate IDs across independent scopes are intentional; within a chosen scope, a singular selector must resolve exactly one element. Do not use `.first()` or an array index to conceal ambiguity. Document the scope.

Example framework-neutral markup:

```html
<article data-testid="invoice-a7">
  <h2 data-testid="invoice-title">Invoice A7</h2>
  <a data-testid="invoice-detail-link" href="/invoices/a7">View invoice</a>
  <button data-testid="invoice-pay-button" type="button">Register payment</button>
</article>
```

The detail link and payment button are separate targets with separate behavior. Identifiers do not justify making the article itself a nonsemantic button.

## Portals, composite controls and icons

Identify trigger, overlay root, title, actions and relevant states independently. Portal content may sit outside the trigger container: QA locates it through its own instance ID rather than assuming DOM ancestry.

When label/input/help/error are separate generated elements, each has an ID. Preserve native `id`/label relationships and ARIA attributes; `data-testid` does not replace them. Label generated icon elements while retaining appropriate decorative or accessible semantics. Do not force identifiers into private SVG paths supplied by a dependency.

## Selector strategy for QA

Reuse these IDs for deterministic discovery and scoped targeting, especially when copy, localization or layout may vary. Use the current test runner's native test-ID query when available; if configured for another attribute, reconcile configuration explicitly rather than silently searching the wrong attribute.

Continue role/label queries and accessible-name assertions for semantic and accessibility verification. A test-ID match alone does not prove visibility, enabled state, accessibility or correct behavior.

Example with a runner exposing `getByTestId`:

```ts
const invoice = page.getByTestId('invoice-a7');
await invoice.getByTestId('invoice-pay-button').click();
// Assert the expected business outcome using the project's actual API/UI.
```

Do not assert only attribute existence for every node as the complete test suite. Coverage checks support specialized workflow tests; they do not replace them. Avoid selectors based on DOM depth, generated classes or position when the contract exists.

## Development verification and handoff

Before completion:
1. Inspect the rendered affected UI, including conditional/loading/error states and portals. Verify attributes reached native elements; source props alone are insufficient.
2. Check explicitly generated elements for missing/empty IDs and singular selectors for duplicates within their declared scope.
3. Rerender, reorder/filter repeated records and change supported state/locale where relevant. Identity must remain attached to the same logical element.
4. Exercise meaningful interactions through the identifiers and assert behavior. Check roles, labels and keyboard operation independently.
5. Report selector scopes/patterns, additions or renames, exceptions and checks actually executed. If runtime is unavailable, state that rendered coverage was not verified.

Keep stable shared rules and patterns in the frontend contract; include task-specific selectors in development evidence/QA work orders. Do not maintain a second exhaustive manually copied inventory of every DOM node.

QA reports missing, ambiguous or unstable required IDs as development defects through the existing coordination path. QA must not modify production code or weaken tests to hide a selector-contract failure.
