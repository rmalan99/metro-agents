# Field-specific contracts

## PasswordField

`PasswordField` is the reusable controlled password base at `src/app/shared/components/fields/base/PasswordField.tsx`; it composes `Input` and `Label`, owns only local visibility state, and exposes `value`, `onChange`, `required`, `disabled`, `error`, and `helperText` states. Feature-specific validation and form-library integration belong in adapters or specialized wrappers.

## FileField

For file fields controlled by or adapted to RHF, do not combine the native `required` attribute with clearing the file input after selection. Validate requiredness in the schema/adapter and communicate it through `aria-required` and the visual error state.
