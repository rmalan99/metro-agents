# Backoffice feedback and overlay contracts

## Alerts and operation results

Alert anatomy is icon, title, optional description, optional action, and optional dismiss control. Resolve geometry from `{component.alert}` and semantic status roles. Inline alerts provide contextual information inside content. Operation completion and backend failures use the canonical `ModalAlert` feedback contract; toast or notification is limited to passive, non-critical updates that do not require acknowledgement.

## Modal and drawer

Modal geometry remains in the base component contract. Use a drawer for contextual inspection or editing that benefits from preserving page context; resolve widths and regions from `{component.drawer}`. Both patterns require labelled structure, initial focus, containment, Escape handling when safe, dismissal rules, scroll ownership, and focus return.

## Tooltip, popover, and menus

Resolve tooltip geometry from `{component.tooltip}` and menu geometry from `{component.menu}`. Tooltips supplement concise controls and never carry critical or interactive content. Popovers contain ordinary controls or content. Menus implement menu keyboard behavior; a popover of links retains normal link behavior.

## Loading and progress

Resolve spinner, progress, skeleton, and empty-state geometry from `{component.feedback}`. Prefer skeletons for predictable content shape, progress for measurable work, and spinners for short indeterminate waits. Preserve the content region and announce meaningful asynchronous status without repeated noisy updates.
