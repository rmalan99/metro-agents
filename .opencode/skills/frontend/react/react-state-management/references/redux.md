# React Redux integration

Read only for this mechanism after ownership is selected. Inherit `../SKILL.md`.

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

Example typed hooks when the installed React Redux version supports withTypes; otherwise use that version's typed-hook pattern:

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
