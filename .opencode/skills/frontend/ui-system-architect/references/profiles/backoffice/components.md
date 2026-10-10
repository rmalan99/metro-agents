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

## Variant and state resolution

In `preserve` mode, use the adopted component system's equivalent variants and states and record their paths. The following matrix applies in `adopt` mode. Names are paths under `color.semantic` in the fallback token asset; pairs are background / foreground. Do not derive colors by opacity, blending or local palette selection.

| Button variant | Default | Hover | Active | Border |
|---|---|---|---|---|
| primary | primary / onPrimary | primaryHover / onPrimary | primaryActive / onPrimary | transparent |
| secondary | surfaceMuted / text | activeSurface / text | borderStrong / text | transparent |
| outline | surface / text | hoverSurface / text | activeSurface / text | controlBorder |
| ghost | transparent / text | hoverSurface / text | activeSurface / text | transparent |
| danger | danger.base / onDanger | dangerHover / onDanger | dangerActive / onDanger | transparent |
| link | transparent / primary | transparent / primaryHover | transparent / primaryActive | transparent |

All button variants use `disabledSurface`, `disabledText` and `disabledBorder` when disabled, except ghost and link which retain transparent background and border. Disabled controls cannot activate; do not reduce the whole control's opacity. Link hover/active adds underline. Focus uses `focus` with width and offset from `control.focusRing` without replacing the variant colors. Loading preserves geometry and current variant, shows the spinner in the foreground color, retains an accessible label, exposes busy state and prevents repeated activation.

Input and select use `surface`, `text`, `textMuted` for placeholder and `controlBorder` for their default border. Hover retains background/text and uses `textMuted` for the border. Focus uses the shared focus ring and `focus` border; invalid uses `danger.base` border and `danger.text` error text with a linked error message. Invalid focus retains the error border plus the focus ring. Disabled uses the shared disabled roles and prevents editing. Read-only retains readable text and is distinct from disabled. Loading keeps the entered value and reserves the existing suffix region for its indicator. Selected menu options use `selectedSurface` / `selectedText`; hover uses `selectedHover` and active uses `selectedActive`.

Cards, tables, modals and drawers use `surface` / `text`, `border` for structural separators and `textMuted` for secondary content. Table row hover uses `hoverSurface`; selected rows use `selectedSurface`. Overlay uses `overlay`; layering and elevation come from `layer` and `elevation`. A card gains hover/active treatment only when it is an actual interactive destination.

Navigation uses `navigationSurface` / `navigationText`; hover uses `hoverSurface`, active press uses `activeSurface`, and the current destination uses `selectedSurface` / `selectedText` with a persistent non-color indicator and current-location semantics. Selected destination hover/press use `selectedHover` / `selectedActive`. Tabs and interactive chips reuse these selection states; checkbox, radio and switch use `primary` / `onPrimary` when selected, and `surface` with `controlBorder` when unselected. Indeterminate is an explicit checkbox state. All interactive elements retain the shared focus ring and their documented hit area.

Status badge and alert variants map success, warning, danger and info to that semantic group's `surface`, `text` and `border`. Neutral uses `surfaceMuted`, `textMuted` and `border`. Status is accompanied by text or an icon with an accessible meaning. A status component's action or dismiss control follows the corresponding button contract rather than inventing another interaction palette.
