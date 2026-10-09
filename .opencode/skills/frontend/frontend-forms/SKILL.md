---
name: frontend-forms
version: 1.0.0
description: Tool-independent reactive form and field contract: dirty/touched validation, inline errors, backend mapping and focus, shared field composition, specialized controls and form/data adapters.
---

# Frontend Forms and Fields

## Scope and ownership

Apply to every generated or modified form regardless of UI library or framework. Follow `../frontend-developer/SKILL.md`, its theme and test-identifier contract. The active tool supplies state/ref mechanics and the selected UI reference supplies supported components/slots. Reuse the project's form/validation library; do not install one merely because this skill exists.

The default selection rule is: 10 or fewer options use a select; more than 10 use a searchable combobox. If the total is remote/unknown or users need to locate items by text, prefer a searchable combobox even when the current response contains fewer items.

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
Prefer composition using the library's existing field/control primitives:

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

Leading/trailing icons are supported by the base composition. Decorative icons have decorative semantics; actions use real named buttons and must not overlap typed text or steal focus unexpectedly.

## 4. Backend validation and reveal
Map the actual backend response through a feature-owned adapter to registered field paths, including nested objects and array identities. Do not place HTTP-response parsing inside a generic input.

- Attach known field errors below their fields and mark them visibly invalid regardless of prior dirty/touched status.
- Put unmapped, cross-field or nonvalidation failures in a form-level message; never silently discard them.
- Preserve entered values and allow correction/resubmission. Prevent duplicate requests while submission is pending.
- Reveal the first invalid field in logical form order, not arbitrary response order: open the containing section/tab/step where safe, render it, then focus its actual control and scroll it into view without sticky-header obstruction.
- If a field cannot be revealed/focused, provide a navigable error summary or clear form-level explanation. Do not silently move focus to a hidden/disabled node.
- Do not steal focus during ordinary on-change validation. Focus navigation is for failed submission or an explicit error-summary action. Honor reduced-motion preferences for scrolling.
- On a field edit, clear or mark stale only that field's obsolete server error and rerun validation. Do not clear unrelated server errors.
- Ignore stale server errors/results when the values or dynamic array identity no longer match the submitted snapshot. Do not attach an error for an old array position to a different record.

## 5. Required specialized controls

| Variant | Behavior |
|---|---|
| Input field | Text/numeric/email as appropriate; shared label, helper, placeholder, adornments and inline feedback |
| Password field | Mandatory internal show/hide button; named state-aware action, non-submit type, keyboard access; retain value, focus/caret where possible and suitable autocomplete |
| Phone field | Locale/country-aware mask and area/country code support; distinguish international dialing code from local area code; validate actual number rather than mask length |
| Date field | Activating its trigger/control opens an accessible date-selection dialog; support keyboard/manual entry where appropriate and constraints/format guidance |
| Combobox | Prefer for more than 10 options; internal search, selection by stable value, loading/empty/error feedback and keyboard behavior |
| Select | For up to 10 options; use a custom accessible popup from the adopted UI system, visually consistent with combobox, not a mismatched browser-native popup by default |
| Mask field | Explicit mask/format, useful prompt, partial-entry validation and separate canonical value |

Password toggling must not submit the form, clear the value or expose the secret in telemetry/test IDs. Phone formatting must not invent a country from UI language; derive it from an explicit product/default selection. Accept paste, leading zeros and editing correctly. Use a compatible phone/mask library only when current tooling lacks the needed capability.

Dates require clear date-only vs timestamp semantics and agreed time-zone handling. Do not convert a date-only selection through UTC in a way that shifts the calendar day. Closing the dialog restores focus; bounds and disabled dates must align with validation.

Custom select and combobox are separate accessible interaction patterns, not just styled divs. Reuse library primitives for roles, keyboard navigation, active option and Escape behavior. Search text is distinct from selected value. Unless allowed, typing an unknown label does not create a valid option.

For remote options, debounce search, guard stale responses, retain selected labels and use the actual paging/query contract. A result page of 10 is not proof the dataset has only 10 options.

Masks must support paste/delete/caret behavior and mobile input. Formatting characters are not automatically part of the backend payload; define normalization explicitly. A mask alone is not validation.

## 6. Composition and integration boundaries
Prefer compound components when compatible with the adopted library. Preserve equivalent public composition when it uses another supported pattern; do not force a new API for stylistic uniformity.

Build responsibilities separately:
1. **Base field:** shared anatomy, semantics, theme, slots, focus target and test-ID forwarding. No endpoint or form-library coupling.
2. **Specialized variant:** password/date/phone/select/mask behavior built on the base. No generic HTTP parsing.
3. **Data-connected component:** feature-owned adapter loads/submits actual backend data and maps results into field inputs. Generic UI components must not hard-code URLs or credentials.
4. **Form-connected adapter:** binds value, events, ref/focus, dirty/touched and error to the chosen form tool. One owner remains authoritative.

These layers may compose in either direction appropriate to the project. Do not require a wrapper for each layer if an existing supported API already satisfies the responsibility. Record the extension pattern so other skills reuse it.

## 7. Verification and handoff
Test reactive error after edit/blur, no pristine errors, correction clearing, submit validation and dirty/touched semantics. Include dependent fields, debounced races, nested backend errors, unmapped errors and stale submission snapshots where relevant.

Verify backend error reveals/focuses the correct reachable field, preserves input and does not move focus while typing. Check required marker/semantics, helper association, placeholder-equivalent guidance, danger states and keyboard focus.

For relevant variants, test password toggle without submission, phone/mask paste and normalization, date dialog/time-zone behavior, select boundary at 10/11 options, combobox no matches and stale remote search. Reuse `data-testid` scopes while asserting meaningful behavior and accessible semantics.

Record form-tool integration, backend mapping location, focus/reveal mechanism and actual checks in the frontend contract/development evidence. Report missing integration or unexecuted runtime checks honestly.
