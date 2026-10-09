---
name: react-testing-quality-workflow
version: 2.3.0
description: React-specific testing: harness providers, rerender identity, Effects and Strict Mode, asynchronous updates, mocks and regression coverage. General quality and selector contracts remain in frontend.
---

# React Testing Integration

## Scope
Child of `react-core`. Inherit the frontend verification and selector contracts; do not restate their workflow, dependency policy, completion criteria or identifier rules here. Use the existing runner and installed versions.

## Build the correct test boundary
- Pure reducers/mappers can be exercised without rendering React.
- Component integration tests render the owning component with the providers it actually requires.
- Route-level tests include the existing router/data context; do not substitute a mock route that changes production behavior.
- Share a render harness when provider setup genuinely repeats. Keep required inputs explicit; an all-purpose harness must not silently authenticate every test.
- Reuse the existing request mock/server fixture strategy. Reset handlers, store/query cache and component mounts between tests to avoid order-dependent results.

Do not add a second test framework because a library example uses it.

## React-specific behavior to exercise
### Props, identity and state
Rerender with changed props to detect state incorrectly copied from inputs. Reorder mutable lists and verify state stays with record identity; use the inherited selector contract to locate instances. Exercise provider replacement/reset when page ownership changes.

### Effects and external systems
Mount/unmount the component and check subscription/timer/request cleanup. Test changing relevant dependencies; an old callback/result must not update the new owner. If Strict Mode is part of the application/test harness, check its development setup/cleanup cycle rather than asserting one incidental Effect invocation.

### Event and asynchronous updates
Use the runner's React-aware interaction/render utilities and wait for observable transitions. Assert pending and completed/failed outcomes when relevant. Do not make tests pass through arbitrary sleeps or blanket suppression of scheduler/act warnings.

When testing debounce/timers, use supported fake timers deliberately, advance them through the React-aware harness and restore real timers afterward. Use controlled delayed responses to reproduce out-of-order completion.

### Controlled/uncontrolled bindings
Check that custom components preserve onChange/onBlur/ref bindings and do not register fields twice. Form behavior is owned by the frontend form contract; this skill tests the React binding, not a second definition of validation rules.

### Error boundaries
Exercise a render failure through the actual error boundary and its reset mechanism. Request/event errors need their own handling path; do not assume an error boundary catches them.

## Test review
Identify which React regression each new test detects: stale closure, render mutation, lost identity, missing cleanup, duplicated ownership or broken binding. Avoid tests that only inspect a Hook's internal state or compare an implementation constant with itself.

Apply the frontend reporting and acceptance requirements unchanged. If a product/selector contract is unavailable to the test harness, report that limitation through the assigned workflow rather than modifying production code from QA.
