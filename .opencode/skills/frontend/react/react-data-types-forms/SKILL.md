---
name: react-data-types-forms
version: 2.3.0
description: API/data boundaries, TypeScript contracts, async data handling, and general form design without prescribing a form library.
---

# React Data, TypeScript, and Forms

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.


---

## 12. Data Fetching and APIs

First use the project's existing data-access pattern.

Possible existing solutions include framework loaders/actions, query libraries, generated clients, or service modules.

Use the frontend async-state contract; this module owns the React data integration and typed mapping below.

## Separation

Avoid embedding endpoint construction and HTTP details throughout presentation components.

Prefer:

```text
Component -> Feature Hook / Query -> Service / API Client -> Backend
```

Follow the existing project architecture when it already defines a different valid boundary.

## API models

Do not assume the backend response is identical to the UI model.

Use mapping when necessary:

```text
API DTO -> domain/UI model -> component
```

---

## 13. TypeScript

React projects should use strict, meaningful typing.

## MUST

- Type component props.
- Type API inputs/outputs.
- Type event handlers when inference is insufficient.
- Model finite variants with unions instead of unrestricted strings.
- Reuse domain types when ownership is clear.

Example:

```ts
type Status = 'idle' | 'loading' | 'success' | 'error';
```

## Avoid

- `any` unless interfacing with unavoidable untyped boundaries, and document the reason.
- Broad type assertions used to hide errors.
- Duplicating the same domain type in several features.
- Making every field optional only to satisfy incomplete code.

Prefer `unknown` over `any` for untrusted data, followed by validation/narrowing.

---

## 14. React form binding boundary

Form behavior and reference selection belong to frontend. This module only binds its contract to React: preserve the adopted form tool's value/change/blur/ref registration, forward focus to the actual control and avoid registering a field twice. For composite controls, map their value callbacks to the tool's supported controller/adapter API; do not assume a DOM event payload.

Keep a single value owner rather than mixing uncontrolled registration, controlled props and an independent local copy. Use the installed React version's supported ref mechanism.
