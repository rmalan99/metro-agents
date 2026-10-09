---
name: react-performance-errors-security
version: 2.3.0
description: React rendering diagnosis, memoization/compiler integration, error boundaries and safe HTML rendering. Inherits general performance/security rules from frontend.
---

# React Performance and Runtime Boundaries

## Scope
Child of `react-core`. The frontend base owns optimization criteria, dependency policy, trusted boundaries and general error feedback. This skill supplies React mechanisms.

## Rendering diagnosis and memoization
Use the existing React profiling tools to identify expensive commits, broad Context updates or repeated render work before changing memoization. Confirm which prop/context identities cause the affected render.

- React.memo only helps when relevant props remain stable and render cost warrants it.
- useMemo caches a calculation, not a source of truth.
- useCallback stabilizes a function identity when a consumer actually benefits.
- None of these is a correctness mechanism; code must work if recalculated.
- When React Compiler is enabled, account for its memoization before adding redundant manual wrappers. Do not enable/change compiler configuration for an unrelated fix.

Use React.lazy/Suspense through the existing routing/rendering model for justified deferred components. Measure the impact and check fallback behavior; do not wrap every small component in Suspense.

Context subscription scope is owned by `react-state-management`; load it if the diagnosis requires changing provider ownership.

## React failure boundaries
Use the project's supported route boundary for route failures and React error boundaries for descendant render failures. Define the reset trigger for navigation/retry so a recovered page does not remain trapped in fallback UI.

Error boundaries do not generally catch asynchronous request failures or event-handler errors. Handle those in their owning data/action layer, under the frontend feedback contract. Suspense pending fallbacks are distinct from error boundaries.

## Untrusted HTML
Avoid dangerouslySetInnerHTML for untrusted values. If HTML rendering is a genuine requirement, sanitize through an approved maintained mechanism at the agreed boundary; do not treat React interpolation escaping as protection for inserted HTML.

Use the general frontend security contract for secrets, authorization and sensitive feedback; do not create a parallel policy here.
