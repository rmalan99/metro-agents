---
name: react-rendering-ui-accessibility
version: 2.1.0
description: Lists and keys, conditional rendering, styling/design-system rules, responsive UI, semantics, and accessibility.
---

# React Rendering, UI, and Accessibility

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.

It expands sections 15, 16, 17, 18 of the original React Frontend Developer skill. It does not introduce additional libraries or technologies beyond what those concepts require. Existing project choices remain authoritative.

---

## 15. Lists and Keys

Keys represent item identity.

Prefer stable domain IDs:

```tsx
users.map((user) => (
  <UserRow key={user.id} user={user} />
));
```

Avoid array indexes as keys when items can be inserted, deleted, filtered, sorted, or reordered.

Never generate random keys during render.

---

---

## 16. Conditional Rendering

Make UI states explicit.

Prefer readable branches for significant states:

```tsx
if (isLoading) return <LoadingState />;
if (error) return <ErrorState error={error} />;
if (!items.length) return <EmptyState />;

return <ItemsList items={items} />;
```

Avoid deeply nested ternaries.

---

---

## 17. Styling and Design System

The existing design system is the source of truth.

## MUST

- Reuse existing UI primitives.
- Reuse spacing, color, typography, radius, and breakpoint tokens.
- Preserve responsive behavior.
- Keep interactive states consistent: hover, focus, active, disabled, loading, error.

## Avoid

- Recreating existing buttons, dialogs, inputs, cards, or tables.
- Repeated magic values when a design token exists.
- Inline styles for large styling systems unless the project intentionally uses them.
- Introducing a new CSS strategy during an unrelated requirement.

---

---

## 18. Accessibility

Accessibility is part of correctness.

## MUST

- Prefer semantic HTML.
- Use real `button`, `a`, `input`, `label`, `table`, etc. when those semantics apply.
- Support keyboard interaction.
- Preserve visible focus states.
- Associate labels and inputs correctly.
- Provide meaningful accessible names for icon-only controls.
- Manage focus appropriately in modals/dialogs.
- Use ARIA only when native HTML semantics are insufficient.
- Ensure status/error feedback is perceivable when necessary.

Do not create clickable `div` elements when a semantic interactive element exists.

---

---
