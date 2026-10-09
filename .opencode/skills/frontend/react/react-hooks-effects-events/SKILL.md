---
name: react-hooks-effects-events
version: 2.4.0
description: Hooks, domain hooks, effect boundaries, synchronization, event handling, and separation of render logic from side effects.
---

# React Hooks, Effects, and Events

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.


---

## 9. Hooks

## Rules of Hooks

- Call conventional Hooks only at the top level of React components or custom Hooks; the use(resource) exception is described below.
- Conventional Hooks cannot be conditional or called in loops, nested callbacks or event handlers. React 19+ use(resource) is a distinct exception: it may be conditional/in a loop within a component or Hook, but not inside try/catch. Check the installed version; do not apply the exception to useState/useEffect or arbitrary Hooks.
- Custom Hooks must begin with `use`.
- A custom Hook should encapsulate reusable behavior or provide a meaningful domain API, not merely move arbitrary lines to another file.

## Domain Hooks

Prefer custom Hooks as the public access layer for domain state when doing so hides implementation details and creates a clear contract.

Examples:

```text
useCurrentUser
usePropertyDetail
useRentalApplication
useRentalApplicationPermissions
useDebouncedValue
usePermission
```

A component that consumes `usePropertyDetail()` should not need to know whether the resource comes from Context, a query library, or another internal mechanism unless that distinction matters to the component.

This makes the domain boundary easier to evolve and test.

### State integration boundary

Context/Redux access patterns and typed selector hooks are owned by `../react-state-management/SKILL.md`; consult that owner when implementing a domain Hook that exposes them. This skill owns the Hook API and external-system lifecycle.

## Hook responsibility

A Hook should answer one recognizable question or expose one coherent capability.

Avoid Hooks that:

- Return dozens of unrelated values.
- Mix several independent domains.
- Hide large amounts of imperative application flow without a clear contract.
- Exist only to reduce the number of lines in a component.

---

## 10. `useEffect`

Apply the render/event boundary from `react-core`. For an external synchronization, identify the lifecycle below.

Appropriate examples:

- Browser APIs.
- Subscriptions.
- WebSockets.
- Timers requiring lifecycle cleanup.
- Third-party widgets.
- Imperative libraries.
- Network synchronization when the project's data layer does not handle it.

## Effect requirements

Every Effect must answer:

1. What external system is being synchronized?
2. What starts the synchronization?
3. What stops/cleans it up?
4. What reactive dependencies does it use?

Never silence hook dependency linting merely to suppress a warning. Fix the dependency or architecture problem.

---

## 11. Events

For a user operation, bind its event directly to the operation:

Examples:

- Submit form.
- Save data.
- Delete resource.
- Open modal.
- Navigate after a click.
- Trigger download.

Prefer:

```tsx
const handleSubmit = async () => {
  await saveApplication(formData);
};
```

instead of setting a state flag and using an Effect to detect the flag and perform the save.

---
