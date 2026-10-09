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

## Binding asynchronous checks and responses

Use the adopted tool's validation/error APIs to implement the lifecycle owned by `../SKILL.md`. Associate request generations/snapshots with their field registration and dispose pending work when that registration unmounts. Translate the feature's actual backend paths to current registered controls, including stable dynamic-array identity.

Expose focus/reveal handles for registered controls through the active tool's mount lifecycle. Keep transport/error-shape parsing in the feature adapter; a generic field only consumes normalized feedback.

## Specialized controls and acceptance

Field-variant behavior and validation cases are owned by `../SKILL.md`; do not redefine them in adapters. Read only the selected UI integration guide from that owner's router when concrete control APIs are needed. The active tool's testing guidance supplies scheduler, timer and rendering-harness mechanics.
