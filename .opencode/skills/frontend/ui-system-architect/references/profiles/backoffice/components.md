# Backoffice component visual contracts

Apply the shared component and accessibility contract first. The paths below define fallback geometry; colors resolve through semantic roles in the active theme.

## Button

Anatomy is optional leading icon, label, and optional trailing icon. Use both icons only for a documented variant. Sizes resolve from `{component.button.sm}`, `{component.button.md}`, or `{component.button.lg}`; default to `md`. Primary, secondary, outline, ghost, danger, and link variants require default, hover, active, focus, disabled, and loading states.

## Input and Select

Input anatomy is optional prefix, value, and optional suffix inside the control. Resolve each size from `{component.input.sm}`, `{component.input.md}`, or `{component.input.lg}`. Select inherits input geometry and adds menu values from `{component.select.menu}`. Labels and helper/error content belong to FormField, not an ad hoc page wrapper.

## Card

Use `{component.card}` for padding, radius, border, and section gaps. Header, content, and footer are optional named regions; avoid nested cards when headings, spacing, or a divider establish hierarchy.

## Modal

Use widths from `{component.modal.width}`, structure from `{component.modal}`, and the adopted overlay/focus primitive. Confirmation, destructive confirmation, information, form, preview, and wizard are compositions over one modal base.

## Data table

Use `{component.table}` for header, rows, cells, type, checkbox, and action geometry. Density selects one documented row height. Querying, sorting, selection, pagination, responsive record representation, and state behavior remain owned by the table specialty.
