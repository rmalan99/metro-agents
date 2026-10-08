---
name: react-testing-quality-workflow
version: 2.1.0
description: Testing strategy, code-quality rules, dependency policy, implementation workflow, review checklist, anti-patterns, decision rules, Definition of Done, and guiding principles.
---

# React Testing, Quality, and Workflow

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.

It expands sections 22, 23, 24, 25, 26, 27, 28, 29, 30 of the original React Frontend Developer skill. It does not introduce additional libraries or technologies beyond what those concepts require. Existing project choices remain authoritative.

---

## 22. Testing Strategy

Test observable behavior rather than implementation details.

Follow the project's test stack. A typical React stack may include Vitest/Jest, React Testing Library, and Playwright/Cypress.

## Unit tests

Use for:

- Pure transformations.
- Validation.
- Reducers.
- Complex utilities.

## Component/integration tests

Validate:

- What the user sees.
- What the user can interact with.
- State transitions.
- Validation/error feedback.
- API-driven UI states where practical.

Prefer queries based on accessible roles, labels, and visible text over implementation-specific selectors.

## E2E tests

Use for critical workflows crossing several screens/services.

Examples:

- Login.
- Checkout/payment.
- Application submission.
- Critical approval flows.

## For every bug fix

When practical, add a regression test that fails before the fix and passes after it.

---

---

## 23. Code Quality Rules

## MUST

- Use descriptive names.
- Keep business rules explicit.
- Remove dead code introduced or made obsolete by the change.
- Keep comments focused on **why**, not restating what obvious code does.
- Respect formatter/linter rules.
- Keep public component/hook APIs small.
- Prefer early returns when they improve readability.

## MUST NOT

- Leave commented-out code.
- Leave debug logs.
- Leave temporary fake data unless explicitly required.
- Suppress TypeScript/ESLint errors without documenting a justified reason.
- Copy/paste large logic blocks when an existing abstraction already owns that responsibility.
- Create a generic abstraction before there is a demonstrated reusable concept.

---

---

## 24. Dependency Policy

Before installing a dependency:

1. Check whether the project already solves the problem.
2. Check whether native browser/React capabilities are sufficient.
3. Determine whether the dependency is maintained and compatible with the project.
4. Evaluate bundle/runtime impact when relevant.
5. Confirm it is necessary for the requirement.

Do not replace an existing library ecosystem during a feature implementation without an explicit architectural decision.

---

---

## 25. Implementation Workflow

The React developer follows this sequence.

## Step 1 — Understand

Translate the assigned task into concrete UI behavior and acceptance conditions.

## Step 2 — Inspect

Read the related code before editing.

## Step 3 — Design the change

Identify:

- Components affected.
- State ownership and scope: local, lifted, Context, URL, Redux, or server state.
- Data flow and domain boundaries.
- API interaction.
- Validation.
- Error/loading/empty states.
- Tests required.

## Step 4 — Implement incrementally

Make the smallest coherent change first.

Keep each modification reviewable.

## Step 5 — Verify locally

Verify:

- TypeScript.
- Lint.
- Relevant automated tests.
- Build when appropriate.
- Main user flow.
- Error/empty/loading states.
- Responsive behavior when UI is affected.
- Keyboard/accessibility behavior for interactive UI.

## Step 6 — Review the diff

Before declaring completion, inspect the final diff for:

- Accidental changes.
- Duplicated logic.
- Dead code.
- Missing edge cases.
- Debug statements.
- Incorrect types.
- Unnecessary abstractions.

## Step 7 — Report result

Return a concise implementation report containing:

```text
Result
- What was implemented.

Files changed
- Relevant files only.

Validation
- Tests/checks executed and results.

Important decisions
- Architecture/state/data-flow decisions that matter to reviewers.

Remaining risks / blockers
- Only when applicable.
```

---

---

## 26. Pull Request / Review Checklist

Before considering React work complete, verify:

- [ ] Requirement is fully implemented.
- [ ] Existing project conventions are respected.
- [ ] Large components were reviewed for meaningful subcomponent boundaries.
- [ ] Components remain pure during render.
- [ ] State has one clear source of truth.
- [ ] State uses the smallest correct ownership scope.
- [ ] Prop drilling is avoided when a page/domain Context is the clearer boundary.
- [ ] Redux is reserved for truly cross-module/application state.
- [ ] Contexts represent coherent page/feature/domain concerns and are not oversized catch-all providers.
- [ ] Redux access uses typed hooks/selectors when Redux is present.
- [ ] No avoidable duplicated/derived state exists.
- [ ] Effects are used only when justified.
- [ ] Effect dependencies and cleanup are correct.
- [ ] Hooks follow React rules.
- [ ] Lists use stable keys.
- [ ] Types are meaningful and no unjustified `any` was added.
- [ ] Loading/error/empty/success states are handled where applicable.
- [ ] Form validation and duplicate-submit behavior are correct where applicable.
- [ ] Accessibility is preserved.
- [ ] Responsive behavior is preserved.
- [ ] No secrets/sensitive data were exposed.
- [ ] No unnecessary dependency was added.
- [ ] Tests cover the important behavior.
- [ ] Regression test exists for a bug fix when practical.
- [ ] Lint/typecheck/tests pass.
- [ ] No debug code remains.
- [ ] Diff contains no unrelated refactor.

---

---

## 27. Anti-Patterns

The developer must actively reject these patterns unless an exceptional case is explicitly justified.

### Effect-driven derived state

```tsx
useEffect(() => {
  setFilteredItems(items.filter(matchesFilter));
}, [items, filter]);
```

Prefer deriving the value during render.

### State mutation

```tsx
user.name = 'New Name';
setUser(user);
```

Create a new value instead.

### Random render keys

```tsx
<Item key={Math.random()} />
```

Use stable identity.

### Index key for mutable list

```tsx
items.map((item, index) => <Item key={index} />)
```

Use an item ID when list identity can change.

### Global state by default

Do not move a modal toggle, field value, page-detail resource, or local selection into the global store simply because a store exists.

### Prop drilling through unrelated components

Do not pass a domain resource through several components that do not use it only so a deeply nested section can access it. Prefer a focused page/feature Context when that data belongs to the subtree.

### Oversized Context

Do not create a single context that contains every piece of state, query, mutation, modal, form value, permission, and helper for a page or feature. Split by coherent domain or update responsibility when necessary.

### Redux as a page-detail cache

Do not promote a resource to Redux only because multiple sections of one detail page consume it. Keep page-scoped data page-scoped unless other unrelated modules truly need to own/read/update it.

### Premature abstraction

Do not convert a one-use 10-line component into a highly configurable framework without a real reuse case.

### Premature optimization

Do not use memoization everywhere without evidence or a clear render-boundary reason.

### Suppressing dependency warnings

Do not disable `exhaustive-deps` simply to make a warning disappear.

---

---

## 28. Decision Rules

When several technically valid options exist, prefer in this order:

1. Existing project convention.
2. Simpler React-native pattern.
3. Smaller state surface.
4. Clearer source of truth.
5. Easier testability.
6. Lower coupling.
7. Lower dependency cost.
8. Performance optimization only after correctness and clarity unless performance is itself the requirement.

---

---

## 29. Definition of Done

A React task is complete only when:

1. The requested behavior works.
2. The implementation follows existing project architecture.
3. State and data flow are understandable.
4. No unnecessary Effects or duplicated state were introduced.
5. The UI handles relevant user states.
6. Type safety is maintained.
7. Accessibility is not degraded.
8. Relevant tests pass.
9. Typecheck/lint/build checks required by the project pass.
10. No unrelated code changes are included.
11. The final implementation can be reviewed without hidden assumptions.

---

---

## 30. Guiding Principle

> Build the simplest React solution that has one clear source of truth, keeps rendering pure, keeps side effects explicit, follows the project's architecture, and remains easy to test and change.

---
