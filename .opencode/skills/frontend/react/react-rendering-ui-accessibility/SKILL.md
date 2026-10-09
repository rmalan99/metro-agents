---
name: react-rendering-ui-accessibility
version: 2.3.0
description: Lists and keys, conditional rendering, styling/design-system rules, responsive UI, semantics, and accessibility.
---

# React Rendering, UI, and Accessibility

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.


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

## 17. Styling and Design System

The frontend base owns theme scope and the selector contract. This module implements prop/ref forwarding to React DOM and provider/portal integration.

Example of a project-owned component (illustrative prop name; preserve existing conventions):

```tsx
type SaveActionProps = {
  testId: string;
  busy: boolean;
  onSave: () => void;
};

export function SaveAction({ testId, busy, onSave }: SaveActionProps) {
  return (
    <button data-testid={testId} disabled={busy} onClick={onSave}>
      <span data-testid={`${testId}-label`}>{busy ? 'Saving' : 'Save'}</span>
    </button>
  );
}
```

React key is reconciliation identity, not a DOM selector. React useId is for accessibility relationships, not the inherited explicit test-ID contract. Forward native IDs/ARIA props independently of test identifiers.

Verify provider placement and style inheritance for dialogs, menus and other portals. In server-rendered frameworks, follow the installed framework/library's style integration and client-boundary guidance; do not make the whole application client-rendered merely to theme a control.

## 18. React accessibility binding

Map native DOM attributes correctly through custom components: htmlFor on labels, native id on inputs, aria-describedby/aria-invalid when supplied by the active field contract. Forward refs to focusable controls rather than layout wrappers. Preserve these bindings through clone/composition APIs.

When a conditional section mounts or a portal opens/closes, coordinate focus with its render lifecycle using the adopted primitive. Do not use an Effect on every render to refocus the control. Generic keyboard, contrast and semantic requirements are inherited from frontend.
