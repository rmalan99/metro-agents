# Implementing the shared frontend form contract

Read alongside `../SKILL.md` only for form implementation. Inspect the installed form/schema library, UI system and generated controls before choosing APIs.

## One owner and thin adapters
Use the adopted form tool's value, validation, dirty/touched and submission lifecycle. Without a form library, model these explicitly at the form owner; do not give every specialized control an independent competing store.

A controlled field consumes value/change and passes blur/ref/focus to its adapter. An uncontrolled registered field must preserve registration's name, change, blur and ref bindings. Never overwrite a registration handler with an unrelated one or register the same field twice.

For composite controls, use the current tool's supported controller/adapter API when required. Date pickers/selects often emit domain values rather than DOM events; map these deliberately. Preserve null/empty semantics and canonical phone/date/mask submission values.

## Shared field implementation
Reuse the selected UI library's field anatomy. Expose slots/props for label, control, helper, error and adornments using its supported composition pattern. Project-owned primitives can use compound composition; do not wrap library controls in duplicate labels/roles.

Illustrative error-gating calculation, independent of any form library:

```ts
type FieldFeedback = {
  error?: string;
  serverError?: string;
  dirty: boolean;
  touched: boolean;
  submitted: boolean;
};

export function visibleError(state: FieldFeedback): string | undefined {
  if (state.serverError) return state.serverError;
  return state.dirty || state.touched || state.submitted
    ? state.error
    : undefined;
}
```

Only pass current server errors here; the owner clears/invalidates an obsolete error when its submitted value changes. Use a shared theme variant for invalid border, label and message instead of coloring each form independently.

Native control IDs may use the active tool's stable accessibility-ID mechanisms when appropriate; test IDs use the separate explicit instance contract and must not derive from those generated IDs. Forward focus refs to the actual input/trigger, not an outer div. Use the active tool's supported control-reference/focus mechanism.

## Reactive validation and asynchronous work
Configure change/blur/revalidation mode through the installed form tool or implement equivalent behavior in the owner. Do not rely on submit-only validation. Show errors only under the shared exposure rule, except current backend errors.

Cheap synchronous rules run on the new value directly. For expensive/remote rules, debounce the check, not value updates/input rendering. Clean up timers and pending checks on value change/unmount. Use cancellation or a generation/snapshot check so outdated results cannot become current errors. Keep an intentional pending state and await/flush essential checks before submit.

Revalidate dependencies through the form tool's supported mechanism; do not duplicate derived validity into another state store. If a tool's dirty semantics differ from the shared contract, adapt exposure explicitly rather than assuming configuration defaults implement it.

## Submission and backend errors
Use the actual service/client contract, not a universal guessed response shape. Map field paths in a feature adapter, including stable identities for dynamic arrays. Keep form-level errors distinct. Apply current errors to the form tool's supported error API or equivalent owner state.

After client/server submission failure:
1. Resolve invalid registered fields in logical form order.
2. Reveal their parent section/tab/step when possible.
3. Wait until the control is rendered through the framework's supported lifecycle, then use its focus handle and deliberate scrolling.
4. If it remains unavailable, show a useful summary/navigation fallback.

Do not use arbitrary timeout delays as the primary mount/focus mechanism. Do not build a reactive observer that repeatedly steals focus whenever errors change; focus only the failed submission event/reveal lifecycle. Preserve values and account for users editing while requests are pending.

## Specialized controls
- Password: a trailing `type="button"` toggles visibility with state-aware accessible name/pressed state when appropriate. Keep the same test ID and value across modes.
- Phone/mask: the adapter defines formatted display versus canonical value; the variant handles input/caret/mask behavior using a compatible existing capability or justified library.
- Date: use the adopted library's dialog/calendar primitive, explicit empty guidance, focus return and date-only/timestamp mapping.
- Select/combobox: use matching accessible popup styles; up to 10 options select, above 10 searchable combobox. Preserve stable option values while search changes.

Consult the chosen UI guide for concrete component APIs; do not load all UI guides. For the adopted form or schema library, check installed-version documentation before using resolver/registration/controller/error APIs.

## Validation evidence
Exercise generated controls through stable test-ID scopes plus role/label assertions. Check change, blur, correction, required submit, backend mapping/focus, disabled/pending state and relevant variant edge cases. Fake timers can verify debounce/races when the test stack supports them; do not write delay-heavy tests based on arbitrary sleeps.

Report what was exercised in rendered UI versus source-only review. An adapter prop named `error` alone does not prove error association, danger styling or focus navigation.
