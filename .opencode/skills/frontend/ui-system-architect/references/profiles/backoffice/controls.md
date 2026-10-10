# Backoffice control contracts

## Checkbox and radio

Use `{component.selection.controlSize}` inside the minimum interactive area. Checkbox supports unchecked, checked, indeterminate, disabled, focus, and error states. Radio supports unchecked, checked, disabled, focus, and error states. Labels are clickable, visible, and associated with the native or adopted accessible primitive.

## Switch

Resolve track and thumb geometry from `{component.selection}`. Use a switch only for an immediately applied binary setting; use a checkbox when confirmation or form submission commits the choice. Expose on, off, disabled, focus, and loading when the operation is asynchronous.

## Segmented control and toggle group

Resolve group geometry from `{component.selection}`. Use mutually exclusive segments for a small set of peer views or modes, not primary navigation. Toggle buttons and groups expose pressed/selected semantics and retain visible focus without relying on color.

## Badge and chip

Resolve geometry from `{component.badge}`. Status variants are success, warning, danger, info, and neutral; business labels map to those semantics outside this profile. Removable or selectable chips are interactive controls with the corresponding keyboard behavior, not decorative badges with click handlers.
