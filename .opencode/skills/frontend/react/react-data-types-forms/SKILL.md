---
name: react-data-types-forms
version: 2.2.0
description: API/data boundaries, TypeScript contracts, async data handling, and general form design without prescribing a form library.
---

# React Data, TypeScript, and Forms

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.

It expands sections 12, 13, 14 of the original React Frontend Developer skill. It does not introduce additional libraries or technologies beyond what those concepts require. Existing project choices remain authoritative.

---

## 12. Data Fetching and APIs

First use the project's existing data-access pattern.

Possible existing solutions include framework loaders/actions, query libraries, generated clients, or service modules.

## Requirements

Every async UI flow must consider:

- Initial/loading state.
- Success state.
- Empty state when applicable.
- Error state.
- Retry behavior when appropriate.
- Request cancellation/race conditions when applicable.
- Stale data/caching rules when applicable.
- Permission/unauthorized states.

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

---

## 14. Forms

Forms must have a clear source of truth and validation strategy.

The general frontend skill owns form behavior and reference selection. This React module only supplies data/type integration constraints; implement the active frontend contract through the existing React form tools without redefining validation, field anatomy or specialized controls.

## Rules

- Follow the project's existing form library if one exists.
- Avoid maintaining the same field value simultaneously in several state systems.
- Validate required business rules before submission.
- Follow the active frontend contract for field feedback and submission behavior. Forward value, change, blur and control references through React adapters without duplicating state.
- Preserve user input when a recoverable request fails.
- Disable duplicate submissions while a request is pending when appropriate.
- Do not rely only on client-side validation for security/business enforcement; backend validation remains required.

Every input must have an accessible label or equivalent semantic relationship.

---

---
