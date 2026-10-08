---
name: react-performance-errors-security
version: 2.1.0
description: Performance decisions, memoization discipline, error handling, resilient UI, and frontend security boundaries.
---

# React Performance, Errors, and Security

## Scope

This is a child skill of `react-core`. Load it only when the current React task involves the concepts covered here.

It expands sections 19, 20, 21 of the original React Frontend Developer skill. It does not introduce additional libraries or technologies beyond what those concepts require. Existing project choices remain authoritative.

---

## 19. Performance

Optimize based on evidence, architecture, and user impact.

## First priorities

1. Avoid unnecessary state.
2. Avoid unnecessary Effects.
3. Avoid excessive work during render.
4. Keep state local where possible.
5. Prevent unnecessary large-tree updates through good component boundaries.
6. Split/lazy-load meaningful expensive areas when justified.
7. Virtualize genuinely large rendered collections when necessary.

## Memoization

Do not automatically wrap everything in:

- `React.memo`
- `useMemo`
- `useCallback`

Memoization is an optimization, not a correctness tool.

If React Compiler is enabled in the project, rely on it for normal memoization and use manual memoization only when a concrete need remains.

If React Compiler is not enabled, manually memoize only when there is a measurable or structurally clear benefit.

Never change project compiler configuration as a side effect of an unrelated feature.

---

---

## 20. Error Handling

Errors must not leave the UI in an ambiguous state.

Handle errors at the appropriate boundary:

- Field validation errors -> form field.
- Request errors -> feature/action feedback.
- Route/page errors -> route error boundary when supported.
- Unexpected render failures -> application/component error boundary strategy.

Do not swallow errors silently.

User-facing error messages should explain what the user can do next without exposing sensitive implementation details.

---

---

## 21. Security

Frontend validation is not authorization.

## MUST

- Never place secrets or privileged credentials in frontend code.
- Treat API/browser/user input as untrusted.
- Avoid rendering untrusted HTML.
- If `dangerouslySetInnerHTML` is unavoidable, content must be sanitized by an approved mechanism.
- Hide UI actions when appropriate, but assume backend authorization is still required.
- Avoid exposing sensitive information through logs or error messages.

---

---
