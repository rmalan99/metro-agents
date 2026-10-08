---
name: react-hooks-effects-events
version: 2.1.0
description: Hooks, domain hooks, effect boundaries, synchronization, event handling, and separation of render logic from side effects.
---

# React Hooks, Effects, and Events

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.

It expands sections 9, 10, 11 of the original React Frontend Developer skill. It does not introduce additional libraries or technologies beyond what those concepts require. Existing project choices remain authoritative.

---

## 9. Hooks

## Rules of Hooks

- Call Hooks only at the top level of React components or custom Hooks.
- Never call Hooks conditionally, inside loops, nested functions, or event handlers.
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

### Context Hooks

Expose domain Context through a dedicated Hook:

```tsx
export function usePropertyDetail() {
  const context = useContext(PropertyDetailContext);

  if (!context) {
    throw new Error('usePropertyDetail must be used inside PropertyDetailProvider');
  }

  return context;
}
```

Do not repeat raw `useContext(PropertyDetailContext)` across many feature components when a domain Hook can define the intended API and provider invariant once.

### Redux Hooks

When Redux is used:

- Prefer application-typed hooks such as `useAppSelector` and `useAppDispatch`.
- Prefer selectors over direct knowledge of deep store structure in components.
- Use feature/domain Hooks when several components repeat the same selector/action composition.
- A domain Hook may coordinate Redux selectors and actions, but it must not hide unrelated state or become an all-purpose store facade.

Good:

```text
useCurrentUser
usePropertyPermissions
useCheckout
```

Poor:

```text
useHelpers
useEverything
useReduxData
useComponentLogic
```

## Hook responsibility

A Hook should answer one recognizable question or expose one coherent capability.

Avoid Hooks that:

- Return dozens of unrelated values.
- Mix several independent domains.
- Hide large amounts of imperative application flow without a clear contract.
- Exist only to reduce the number of lines in a component.

---

---

## 10. `useEffect`

`useEffect` is an **escape hatch for synchronization with systems outside React**.

Appropriate examples:

- Browser APIs.
- Subscriptions.
- WebSockets.
- Timers requiring lifecycle cleanup.
- Third-party widgets.
- Imperative libraries.
- Network synchronization when the project's data layer does not handle it.

## Do NOT use an Effect for

- Calculating a value for rendering.
- Filtering or sorting local data for display.
- Updating one state variable because another state variable changed when the value can be derived.
- Handling a user action that belongs directly in an event handler.

Bad:

```tsx
const [fullName, setFullName] = useState('');

useEffect(() => {
  setFullName(`${firstName} ${lastName}`);
}, [firstName, lastName]);
```

Good:

```tsx
const fullName = `${firstName} ${lastName}`;
```

## Effect requirements

Every Effect must answer:

1. What external system is being synchronized?
2. What starts the synchronization?
3. What stops/cleans it up?
4. What reactive dependencies does it use?

Never silence hook dependency linting merely to suppress a warning. Fix the dependency or architecture problem.

---

---

## 11. Events

User-driven operations belong in event handlers.

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

---
