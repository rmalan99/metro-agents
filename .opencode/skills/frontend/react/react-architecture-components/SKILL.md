---
name: react-architecture-components
version: 2.4.0
description: Project inspection, feature architecture, component boundaries, decomposition, naming, props, and component contracts.
---

# React Architecture and Components

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.


---

## 3. React inspection targets

Apply the frontend core's discovery procedure. For React, trace the affected route, component tree, Hooks, providers and typed props. Determine the actual parent/child boundaries before choosing a feature location.

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
- Avoid large generic `utils`, `helpers`, or `common` files containing unrelated logic.
- Avoid deep relative imports when the project already provides aliases.

---

## 5. Component Design

## A component should

- Receive explicit inputs through typed props.
- Expose intentional events/callbacks.
- Use composition when behavior or layout must vary.

Before implementing a page, identify the task-relevant project-owned base components and feature sections it will compose. If a required base does not exist, establish the smallest useful base before assembling the page. Page components coordinate route data, permissions, mutations, layout and page-level state; they must not recreate repeated field anatomy, icon actions, state styling or accessibility wiring from raw UI-library controls.

Using a library primitive directly is valid for a genuinely local control that already satisfies the complete contract. Once composition, behavior, variants or repeated treatment are shared, contain the primitive in a project component and consume that public component from pages and features. Do not extract wrappers that only rename the primitive.

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

For direct parent-child communication, prefer typed props. However, do not force page-level or domain-level data through several intermediate components only to reach deeply nested sections. When sharing beyond direct children is required, use the mechanism selected by `../react-state-management/SKILL.md`.

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
- Avoid boolean-prop explosions such as `isSmall`, `isBlue`, `isCompact`, `isAdmin`, `isBordered` when composition or variants would model the API better.
- Do not copy props into state unless there is a real state-lifecycle reason.
- Callback names should describe intent: `onSave`, `onDelete`, `onSelectionChange`.
- Internal event handlers should use `handle...`: `handleSave`, `handleDelete`.

---
