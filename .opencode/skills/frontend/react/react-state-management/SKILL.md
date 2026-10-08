---
name: react-state-management
version: 2.1.0
description: State ownership and scope: derived values, local state, lifted state, Context, URL state, Redux, server-state ownership, and state structure.
---

# React State Management

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.

It expands sections 7, 8 of the original React Frontend Developer skill. It does not introduce additional libraries or technologies beyond what those concepts require. Existing project choices remain authoritative.

---

## 7. State Management and Data Ownership

Choose state by **ownership, scope, lifecycle, and source of truth**.

The default hierarchy is:

```text
Derived value
    ↓
Local component state
    ↓
Closest common parent / lifted state
    ↓
Page or feature Context
    ↓
URL state
    ↓
Redux / application-global state
```

This hierarchy is not a rigid sequence that every value must pass through. It is a decision model: keep the value in the smallest scope that correctly represents its ownership.

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

## 7.4 Context — page, feature, or domain subtree

Use Context when data or behavior belongs to a **specific page, feature, domain, or component subtree** and several descendants need access to it.

Context is especially appropriate when passing the same domain object through intermediate components would create prop drilling.

Typical examples:

- A resource loaded by a detail page.
- Page-level edit state.
- Page-specific permissions.
- A wizard or multi-step flow contained inside one feature.
- A table feature whose filters/actions are consumed by several descendants.
- A form section shared by many deeply nested field components when the form library does not already provide its own context.

### Detail-page pattern

A resource detail page normally loads or receives one main domain resource and composes several specialized sections.

```text
PropertyDetailPage
  ├── PropertyHeader
  ├── OwnerInformation
  ├── PropertyDescription
  ├── AccessKeysSection
  ├── AmenitiesSection
  ├── PropertyDocuments
  └── PropertyHistory
```

If all or most of those sections need information from the same `property`, do not pass the full object through every layer of the tree merely to reach them.

Prefer a domain provider:

```tsx
function PropertyDetailPage() {
  const property = usePropertyQuery();

  return (
    <PropertyDetailProvider property={property}>
      <PropertyDetail />
    </PropertyDetailProvider>
  );
}
```

Then each specialized section consumes only the domain data it needs through a domain Hook:

```tsx
function OwnerInformation() {
  const { property } = usePropertyDetail();

  return <OwnerCard owner={property.owner} />;
}
```

This keeps the page composable and prevents components such as layout wrappers, tabs, grids, or section containers from receiving props they never use.

### Context rules

- A Context must represent a coherent domain or concern.
- Prefer a domain name such as `PropertyDetailContext`, `RentalApplicationContext`, or `CheckoutContext` over vague names such as `PageContext` or `GlobalContext`.
- Expose Context through a custom Hook such as `usePropertyDetail()` instead of importing `useContext` throughout the feature.
- The custom Hook should fail clearly when used outside its provider when that usage is invalid.
- Keep the provider as close as possible to the subtree that needs it.
- Do not place page-specific state in an application-root provider.
- A page may use **more than one Context** when the concerns have different ownership or update patterns.
- Split large contexts when unrelated values cause broad re-renders or make ownership unclear.
- Avoid putting every query result, mutation, form control, modal flag, and helper function into one giant context value.
- Keep context values stable when necessary, but do not add `useMemo`/`useCallback` mechanically. Optimize when context identity is causing unnecessary consumer renders.

Example of valid separation:

```text
PropertyDetailPage
  ├── PropertyDetailContext       -> resource/domain data
  ├── PropertyPermissionsContext  -> page permissions
  └── PropertyEditContext         -> edit workflow/state
```

Multiple contexts are preferable to one oversized context when they model independent concerns.

---

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

## 7.6 Redux — application or cross-module state

Redux is for state whose ownership extends beyond a single page or feature subtree and must be consistently shared across unrelated parts of the application.

Typical examples:

- Authenticated/current user state.
- Session information used across the application.
- Global authorization/permission state.
- Cross-module workflow state.
- Application-wide preferences when they are not better represented by another dedicated mechanism.
- Shared business state that several routes or modules must read/update independently.

Example:

```text
Authentication module
        ↓
   Redux user/session
   ↙      ↓       ↘
Dashboard Properties Payments
```

A logged-in user affects several independent modules, so Redux is an appropriate owner.

By contrast:

```text
PropertyDetailPage
        ↓
PropertyDetailContext
   ↙      ↓       ↘
Owner  Keys  Documents
```

The loaded property belongs to that page/domain subtree, so Context is normally more appropriate than promoting it to Redux solely to make it available to descendants.

### Redux rules

- If Redux is already part of the project, use **Redux Toolkit** for modern Redux logic unless the codebase has an explicit established alternative.
- Organize Redux state by business domain/feature using slices.
- Keep each slice responsible for a coherent domain.
- Use selectors as the read boundary for store state.
- Components should select the smallest value they need instead of subscribing to the entire store or an oversized slice object.
- Prefer typed application hooks such as `useAppSelector` and `useAppDispatch` instead of repeatedly using untyped `useSelector` and `useDispatch`.
- Infer `RootState` and `AppDispatch` from the configured store instead of manually duplicating those types.
- Keep reusable selectors close to the feature/slice that owns the state.
- Do not dispatch actions from render.
- Do not mirror Redux values into component state without a real local lifecycle requirement.
- Do not store ephemeral component UI state globally by default.
- Do not use Redux merely to avoid passing a prop one level.
- Do not place a page-detail resource in Redux only because many children need it; Context is normally the better page-scoped boundary.
- Do not duplicate server/query cache data in Redux when the project's server-state solution already owns it.

Recommended typed hooks:

```tsx
// app/hooks.ts
export const useAppDispatch = useDispatch.withTypes<AppDispatch>();
export const useAppSelector = useSelector.withTypes<RootState>();
```

Prefer reusable selectors:

```tsx
const currentUser = useAppSelector(selectCurrentUser);
const canManageProperties = useAppSelector(selectCanManageProperties);
```

rather than repeatedly exposing store structure throughout components:

```tsx
const state = useAppSelector((state) => state);
```

### Redux domain hooks

When a feature repeatedly combines selectors, dispatches, and domain actions, a custom domain Hook may provide a cleaner feature API.

```tsx
function useCurrentUser() {
  const user = useAppSelector(selectCurrentUser);
  const permissions = useAppSelector(selectCurrentUserPermissions);

  return { user, permissions };
}
```

A domain Hook must improve the feature boundary. It must not become a generic `useEverything()` wrapper around the whole Redux store.

---

## 7.7 Server state

Remote API data is **server state**, not automatically React local state or Redux state.

Use the project's existing server-state/data-fetching mechanism when available, such as a query library, framework data API, or RTK Query.

Do not copy query/server data into local state, Context, or Redux unless there is a concrete ownership reason.

A Context may expose a resource already owned by a query to page descendants without becoming a second persisted source of truth. The provider should normally expose the query result/resource rather than clone it into independent state.

---

## 7.8 State ownership decision table

| Need | Preferred owner |
| --- | --- |
| Value can be calculated from existing data | Derived value |
| Used by one independent component | Local state |
| Shared by a few siblings | Closest common parent |
| Shared deeply inside one page/feature/domain | Context |
| Belongs to navigation/shareable URL | Route/search params |
| Shared across unrelated pages/modules | Redux/global store |
| Remote resource/cache lifecycle | Server-state/query layer |

### Governing rule

> State belongs to the smallest domain that truly owns it. Do not promote data to a broader scope only for convenience.

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

---
