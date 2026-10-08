---
name: react-architecture-components
version: 2.1.0
description: Project inspection, feature architecture, component boundaries, decomposition, naming, props, and component contracts.
---

# React Architecture and Components

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.

It expands sections 3, 4, 5, 6 of the original React Frontend Developer skill. It does not introduce additional libraries or technologies beyond what those concepts require. Existing project choices remain authoritative.

---

## 3. Before Writing Code

The developer must inspect the relevant codebase before making changes.

## Required analysis

1. Identify the feature/module being changed.
2. Locate related components, hooks, services, schemas, types, tests, and routes.
3. Understand the existing data flow.
4. Identify the source of truth for every relevant value.
5. Check existing reusable components before creating a new one.
6. Check the project's current libraries and patterns before introducing another solution.
7. Identify loading, error, empty, disabled, permission, and success states.
8. Identify whether the change affects accessibility, responsive behavior, navigation, caching, permissions, or API contracts.
9. Determine what should be tested before implementation begins.

Do not start by creating new files. First determine whether the requirement can be implemented by extending the existing design safely.

---

---

## 4. React Project Architecture

Prefer organization by **feature/domain** for application code.

Example:

```text
src/
  app/
  features/
    users/
      components/
      hooks/
      services/
      types/
      schemas/
      utils/
      tests/
    payments/
  components/
    ui/
    shared/
  hooks/
  services/
  lib/
  types/
  utils/
```

## Rules

- Feature-specific code stays inside the feature.
- Shared code moves to shared folders only when it is genuinely reused.
- Avoid large generic `utils`, `helpers`, or `common` files containing unrelated logic.
- Avoid circular dependencies.
- Avoid deep relative imports when the project already provides aliases.
- Do not reorganize the entire project as part of a feature change.

---

---

## 5. Component Design

## A component should

- Have a clear responsibility.
- Receive explicit inputs through typed props.
- Expose intentional events/callbacks.
- Be understandable without reading many unrelated files.
- Prefer composition when behavior or layout must vary.

## Split a component when

- It contains multiple clearly identifiable UI sections or responsibilities.
- A page-level component is coordinating several independent visual blocks.
- A section can be understood, rendered, or tested independently.
- A section has its own behavior, state, events, permissions, or data mapping.
- The same UI or behavior is reused.
- Testing the component has become difficult because too many concerns are coupled.
- The render function has become difficult to scan or understand.
- The component has grown large enough that developers must navigate through substantial unrelated JSX to modify one section.

Component size is not a strict numeric rule, but **large files are an architectural signal**. A component with hundreds of lines of JSX should be reviewed for natural boundaries even when most of those lines are presentation markup.

For example, a property detail page should not normally keep owner information, property description, keys/access information, amenities, documents, and history as one 500-line JSX block when those sections are independent concepts. Prefer a page component that composes focused sections:

```text
PropertyDetail
  ├── PropertyHeader
  ├── OwnerInformation
  ├── PropertyDescription
  ├── AccessKeysSection
  ├── AmenitiesSection
  ├── PropertyDocuments
  └── PropertyHistory
```

The parent component should coordinate page-level concerns such as data loading, permissions, mutations, layout, and page-level state. Child sections should have access only to the domain data and actions relevant to their responsibility.

For direct parent-child communication, prefer typed props. However, do not force page-level or domain-level data through several intermediate components only to reach deeply nested sections. When many components inside the same page or feature consume the same stable resource or domain state, use a focused Context and domain Hook to avoid prop drilling.

The objective is not to create the smallest possible components. The objective is to create **clear component boundaries** that improve readability, maintenance, reuse, and testability.

## Avoid unnecessary extraction when

- A fragment is very small and has no meaningful responsibility of its own.
- Extraction would create indirection without improving readability, ownership, reuse, or testing.
- The extracted component would merely rename a few adjacent HTML elements while still depending heavily on the parent's internal implementation details.

Do not use line count as an automatic refactoring threshold, but do not ignore a very large component simply because its length comes mostly from JSX.

## Naming

Use descriptive names:

```text
UserProfile.tsx
PaymentSummary.tsx
RentalApplicationForm.tsx
useRentalApplication.ts
payment.service.ts
rental-application.types.ts
```

Avoid vague names such as:

```text
Component.tsx
Helper.ts
Utils2.ts
Data.tsx
NewComponent.tsx
```

---

---

## 6. Props

Use TypeScript to make component contracts explicit.

```tsx
type UserCardProps = {
  user: User;
  onSelect?: (userId: string) => void;
  disabled?: boolean;
};
```

## Rules

- Prefer the minimum props needed by the component.
- Use props for explicit communication between a component and its direct children.
- Avoid passing entire objects when only one or two values are required, unless the object is the component's actual domain input.
- Do not use intermediate components as transport layers for data they do not use. If the same page/domain data must cross several levels, prefer a focused Context instead of prop drilling.
- Avoid boolean-prop explosions such as `isSmall`, `isBlue`, `isCompact`, `isAdmin`, `isBordered` when composition or variants would model the API better.
- Do not copy props into state unless there is a real state-lifecycle reason.
- Callback names should describe intent: `onSave`, `onDelete`, `onSelectionChange`.
- Internal event handlers should use `handle...`: `handleSave`, `handleDelete`.

---

---
