# Shared component and accessibility contract

Load for generated/modified UI; tools provide concrete bindings. The selector contract is routed separately by the frontend core.

## Components

Reuse project components first, then adopted library primitives, then add only the missing composition or behavior.

For each affected interactive component establish:
- Inputs, outputs and responsibility.
- Relevant default, hover, focus, active, disabled, loading and error states.
- Navigation versus action semantics.
- Responsive behavior and keyboard interaction.
- Data/permission prerequisites and behavior when they are unavailable.

Use links for destinations and buttons for actions. Do not nest interactive controls. Preserve the semantics and accessibility of the chosen primitives instead of replacing them for styling convenience.

## Adaptation and accessibility

Adapt tasks and composition, not just font sizes. Specify changes to navigation, grids, forms, data views, overlays and primary actions. Preserve essential information on smaller screens.

Verify semantics, heading hierarchy, accessible names, keyboard reachability, visible focus and status feedback. Manage overlay focus according to its pattern; return focus on close where appropriate. Do not rely only on color.

Target WCAG AA contrast: 4.5:1 for normal text, 3:1 for large text and relevant non-text controls. Honor reduced-motion preferences for significant motion. Validate with real content, long labels and relevant locale formatting.
