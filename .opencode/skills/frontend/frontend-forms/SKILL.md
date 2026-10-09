---
name: frontend-forms
version: 1.3.0
description: Tool-independent reactive form and field contract: dirty/touched validation, inline errors, backend mapping and focus, shared field composition, specialized controls and form/data adapters.
---

# Frontend Forms and Fields

## Scope and ownership

Apply to every generated or modified form regardless of UI library or framework. Follow `../frontend-developer/SKILL.md`, `../frontend-developer/references/component-contracts.md`, `../frontend-developer/references/feedback.md` and the frontend theme/test-identifier contracts. The active tool supplies state/ref mechanics and the selected UI reference supplies supported components/slots. Reuse the project's form/validation library; do not install one merely because this skill exists.

Selection mode and option-count rules are owned by `references/fields/selection.md`.

## Reference ownership and selective loading
Frontend owns form behavior and its implementation references. The active tool supplies technical mechanisms but does not route or duplicate this contract.

| Needed for the task | Load |
|---|---|
| Field/form adapters, reactive checks or backend error/focus integration | `references/form-integration.md` |
| MUI field integration | `references/ui/mui.md` |
| shadcn/ui field integration | `references/ui/shadcn.md` |
| Chakra UI field integration | `references/ui/chakra.md` |
| Tailwind field integration | `references/ui/tailwind.md` |
| Plain CSS field integration | `references/ui/css.md` |

Load only the adopted UI system's reference when needed, not all five. For framework/library setup APIs, consult the existing tool-specific guide separately. Keep shared field behavior and future form extensions here.

## 1. Inspect and establish the contract
Identify fields, initial values, required conditions, synchronous rules, asynchronous checks, backend error shape, locale, submission semantics and current form tools. Separate display values from canonical submission values. Do not invent backend field names or validation rules.

Define one owner for each value, dirty/touched status, validation result and submission state. Shared fields consume those states; they must not maintain a competing form model.

For each field provide: name, label, required state, placeholder or equivalent empty prompt, optional helper text, value/change/blur contract, disabled/read-only state, error state, focus target, stable test-ID scope and optional leading/trailing adornments. Support helper text on every variant without requiring redundant text in every instance.

## 2. Reactive validation lifecycle
1. Initially, pristine untouched fields do not show errors. Required indicators and helpful instructions are still visible.
2. On change, immediately update the value and dirty state. Run inexpensive synchronous validation for the new value; show current errors when dirty OR touched.
3. On blur, mark touched and validate immediately, including empty required fields. Returning to the initial value can clear dirty, but must not undo touched.
4. Clear an error when its rule passes. Revalidate affected dependent fields, e.g. password confirmation or date ranges, without displaying errors on otherwise unexposed fields.
5. On submit, validate all fields, expose invalid fields even if pristine, and prevent the request when client validation fails. Focus/reveal the first invalid reachable field.
6. On successful completion/reset, reset values and validation metadata according to the actual workflow. Do not clear a failed form or all user input prematurely.

Use this visibility rule conceptually:

`showError = hasError AND (dirty OR touched OR submitted OR currentServerError)`

Debounce expensive/async checks where useful; a starting delay of 250–400ms is adjustable to the task. Do not debounce the displayed input value or postpone basic required/format feedback unnecessarily. Cancel/ignore old validation responses when value changes. Flush required validation on blur/submit; do not submit while an essential async check is unresolved.

Client validation improves feedback; server validation remains authoritative. Do not trigger a server request on every keystroke if a debounced check or local rule suffices.

## 3. Field anatomy, error and visual state
Implement the shared field through composition using the library's existing field/control primitives:

```text
Field root
├── Label + required marker
├── Control area
│   ├── Optional leading icon/adornment
│   ├── Input / trigger / specialized control
│   └── Optional trailing icon/action
├── Optional helper text
└── Inline error message
```

Every field displays its applicable error below the control. When exposed as invalid, border, label and error/helper-error text use the shared danger treatment with adequate contrast. Keep keyboard focus visible; danger styling must not erase focus indication. Do not depend only on color.

Show `*` for required fields and communicate required state programmatically through the appropriate native/ARIA mechanism. Conditional requirements must update marker, semantics and validation together. The star must not be the sole accessible explanation of requiredness.

Keep a visible label; placeholder is guidance, not its replacement. Provide a suitable empty prompt for selects/date controls. Native controls that do not display placeholder text need a visible equivalent instruction; do not claim an unsupported attribute provides it.

Helper and error may coexist when helper instructions remain useful. Avoid duplicate messages; prioritize the actionable current error. Associate helper/error IDs with the control and expose invalid state semantically. Avoid announcing every keystroke with an assertive live region.

The base composition must expose leading/trailing icon slots. Use the adopted icon set when a field variant specifies or conventionally uses an icon; do not substitute visible action text for that icon. Decorative icons have decorative semantics; icon actions use real named buttons, accessible state-aware names and visible focus, and must not overlap typed text or steal focus unexpectedly.

## 4. Backend validation and reveal
Map the actual backend response through a feature-owned adapter to registered field paths, including nested objects and array identities. Do not place HTTP-response parsing inside a generic input.

- Process backend failures into safe user-facing language and show the operation failure through the shared error `ModalAlert`; never expose raw internals or silently discard a failure.
- Attach backend field errors below their fields, mark them visibly invalid regardless of prior dirty/touched status and summarize the failed submission in the error `ModalAlert`. Client-side validation remains inline and must not open a modal while typing or for each local rule.
- Preserve entered values and allow correction/resubmission. Prevent duplicate requests while submission is pending.
- Reveal the first invalid field in logical form order, not arbitrary response order: open the containing section/tab/step where safe, render it through its lifecycle (not an arbitrary timeout), then focus its actual control and scroll it into view without sticky-header obstruction.
- If a field cannot be revealed/focused, provide a navigable error summary or clear form-level explanation. Do not silently move focus to a hidden/disabled node.
- Do not steal focus during ordinary on-change validation. Focus navigation is for failed submission or an explicit error-summary action. Honor reduced-motion preferences for scrolling.
- On a field edit, clear or mark stale only that field's obsolete server error and rerun validation. Do not clear unrelated server errors.
- Ignore stale server errors/results when the values or dynamic array identity no longer match the submitted snapshot. Do not attach an error for an old array position to a different record.

## 5. Field variant routing

Load only the variant being implemented/verified. Its behavior and additional checks have a single owner:

| Variant | Reference |
|---|---|
| Input | `references/fields/input.md` |
| Password | `references/fields/password.md` |
| Phone | `references/fields/phone.md` |
| Date | `references/fields/date.md` |
| Select / searchable combobox | `references/fields/selection.md` |
| Mask | `references/fields/mask.md` |

## 6. Composition and integration boundaries
Use compound components when compatible with the adopted library. Preserve an existing equivalent public composition when it uses another supported pattern; do not force a new API only for stylistic uniformity.

Build responsibilities separately:
1. **Base field:** required project-owned composition for shared anatomy, semantics, theme, slots, focus target and test-ID forwarding. No endpoint or form-library coupling.
2. **Specialized variant:** password/date/phone/select/mask behavior composed from the base rather than recreated in a page. No generic HTTP parsing.
3. **Data-connected component:** feature-owned adapter loads/submits actual backend data and maps results into field inputs. Generic UI components must not hard-code URLs or credentials.
4. **Form-connected adapter:** binds value, events, ref/focus, dirty/touched and error to the chosen form tool. One owner remains authoritative.

These layers may compose in either direction appropriate to the project. An existing project component may satisfy a layer when it demonstrably owns the complete responsibility; a raw library control does not satisfy the project-owned base merely because it can render an input. Do not add wrappers that only rename primitives. Record the extension pattern so other skills reuse it, and keep page/form containers on the public project components rather than rebuilding field anatomy from raw controls.

## 7. Verification and handoff
Test reactive error after edit/blur, no pristine errors, correction clearing, submit validation and dirty/touched semantics. Include dependent fields, debounced races, nested backend errors, unmapped errors and stale submission snapshots where relevant.

Verify backend error reveals/focuses the correct reachable field, preserves input and does not move focus while typing. Check required marker/semantics, helper association, placeholder-equivalent guidance, danger states and keyboard focus.

Verify authoritative form completion opens the shared success `ModalAlert`, backend failure opens the shared error `ModalAlert`, field-specific backend details remain inline, and the flow uses no native JavaScript alert, toast/snackbar or static alert as its result feedback.

Verify pages consume the shared base and specialized variants instead of duplicating raw field composition. For icon actions, verify the adopted icon renders, the accessible name reflects current state and no visible text substitute appears unless the product explicitly requires a labeled action.

Use the active variant reference for additional acceptance cases. Reuse the selector contract for targeted behavioral/semantic checks.

Record form-tool integration, backend mapping location, focus/reveal mechanism and actual checks in the frontend contract/development evidence. Report missing integration or unexecuted runtime checks honestly.
