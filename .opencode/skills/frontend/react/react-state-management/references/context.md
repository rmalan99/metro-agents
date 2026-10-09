# React Context integration

Read only for this mechanism after ownership is selected. Inherit `../SKILL.md`.

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

### Page-owned Context integration

For a resource consumed throughout a page subtree, expose the existing resource through a domain provider:


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
