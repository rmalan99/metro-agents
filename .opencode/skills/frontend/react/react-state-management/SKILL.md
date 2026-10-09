---
name: react-state-management
version: 2.4.0
description: State ownership and scope: derived values, local state, lifted state, Context, URL state, Redux, server-state ownership, and state structure.
---

# React State Management

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.


---

## 7. State Management and Data Ownership

The frontend base owns scope/lifetime/source-of-truth decisions. Map those decisions to the React mechanisms below. The existence of Context or a store is not an ownership decision.

## 7.1 Derived values

If a value can be calculated from existing props, state, context, store data, or query data, derive it instead of creating another state variable.

```tsx
const fullName = `${firstName} ${lastName}`;
```

Do not create duplicated state just to cache a value that React can derive during render.

---

## 7.2 Local state — component scope

Use local React state when the value belongs to one component or to a very small, tightly coupled subtree.

Typical examples:

- Whether a local dialog is open.
- Input state not owned by a form library.
- A local accordion section.
- Temporary UI selection.
- Local edit mode.

```tsx
const [isOpen, setIsOpen] = useState(false);
```

A value must not be moved to Context or Redux only because those tools already exist in the project.

**Rule:** if only one independent component owns and uses the state, local state is normally the correct choice.

---

## 7.3 Lifted state — sibling coordination

Lift state to the closest common parent when a small number of sibling components need to coordinate the same value.

Do not immediately introduce Context when a direct common parent can clearly own the interaction.

```text
SearchPanel
  ├── SearchInput
  └── SearchResults
```

If `SearchInput` updates a value that `SearchResults` consumes, `SearchPanel` can own that state.

---

## React Context integration

Load `references/context.md` only when implementing this mechanism.

## 7.5 URL state — navigation-owned state

Use route params or search params for information that is part of navigation, should survive refresh, or should be shareable/bookmarkable.

Examples:

- Resource IDs.
- Search.
- Filters.
- Pagination.
- Sort order.
- Active tab when the tab represents meaningful navigation state.

Do not mirror URL state into Redux or local state unless there is a concrete synchronization requirement.

---

## React Redux integration

Load `references/redux.md` only when implementing this mechanism.

## 7.7 Server state

Remote API data is **server state**, not automatically React local state or Redux state.

Use the project's existing server-state/data-fetching mechanism when available, such as a query library, framework data API, or RTK Query.

Do not copy query/server data into local state, Context, or Redux unless there is a concrete ownership reason.

A Context may expose a resource already owned by a query to page descendants without becoming a second persisted source of truth. The provider should normally expose the query result/resource rather than clone it into independent state.

---

## 8. State Structure Rules

State should be minimal and normalized.

### Prefer

```tsx
const [selectedUserId, setSelectedUserId] = useState<string | null>(null);
```

instead of duplicating the complete selected user if that user already exists in a collection.

### Avoid

- Contradictory state.
- Duplicate state.
- Redundant derived state.
- Deeply nested state that is difficult to update.

Group values that represent one logical transition when doing so reduces inconsistent states.

For complex state transitions, prefer `useReducer` over many interdependent `useState` calls.

---
