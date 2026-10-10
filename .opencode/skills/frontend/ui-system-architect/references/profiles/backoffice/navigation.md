# Backoffice navigation contracts

## Sidebar and app bar

The sidebar contains brand/home destination, task-grouped navigation, optional badges, and an authenticated-user region. Resolve shell dimensions from `{layout.shell}` and item geometry from `{component.navigation}`. Expanded, collapsed, active, hover, focus, disabled, nested, and narrow-screen drawer states remain distinguishable. The app bar may contain breadcrumb or contextual title, global search, notifications, help, quick actions, and user menu only when their behavior exists.

## Breadcrumb and tabs

Resolve breadcrumb geometry from `{component.navigation}`. Breadcrumbs represent hierarchy and use links except for the current location. Resolve tab geometry from `{component.tabs}`; tabs switch peer panels in one context, preserve a visible selected state, support the adopted keyboard model, and do not replace route navigation without an explicit URL contract.

## Pagination and stepper

Resolve pagination geometry from `{component.pagination}`. Pagination exposes current page, available navigation, disabled boundaries, and total/range context when known. A stepper communicates ordered progress through a bounded process; completed, current, upcoming, error, and disabled steps must not depend only on color.

## Dropdown and command menu

Resolve menu geometry from `{component.menu}`. Dropdown actions stay close to their owner and separate destructive actions. Command menus are reserved for broad, searchable navigation or actions and require deterministic filtering, keyboard traversal, an empty result, and an accessible invocation label.
