# Shared component and accessibility contract

Load for generated/modified UI; tools provide concrete bindings. The selector contract is routed separately by the frontend core.

## Components

Reuse project components first, then adopted library primitives, then add only the missing composition or behavior.

Before building a screen, inventory the controls it needs and identify their project-owned base. In a new application or an area without that base, create the smallest task-relevant shared set first (for example Button, Field/Input, PasswordField and ModalAlert when operations report results), then compose the screen from it. Do not let pages or feature forms repeat library-primitives, field anatomy, icon actions, state styling or accessibility wiring that belongs to those shared components.

A library primitive may be used directly only when it already satisfies the complete project contract and no project-specific composition, behavior, variant or repeated treatment is needed. Otherwise keep the primitive inside the project-owned base component. Do not create a wrapper that merely renames a primitive; the base must own a concrete shared responsibility such as anatomy, behavior, variants, semantics, styling, refs or selector forwarding.

For each affected interactive component establish:
- Inputs, outputs and responsibility.
- Relevant default, hover, focus, active, disabled, loading and error states.
- Navigation versus action semantics.
- Responsive behavior and keyboard interaction.
- Data/permission prerequisites and behavior when they are unavailable.

Use the adopted icon set for recognizable icon actions and visual affordances. Do not replace a specified or established icon with visible action text merely because the text is easier to implement. Icon-only actions remain real buttons with accessible names, visible focus and state semantics; decorative icons remain hidden from assistive technology.

Use links for destinations and buttons for actions. Do not nest interactive controls. Preserve the semantics and accessibility of the chosen primitives instead of replacing them for styling convenience.

## Adaptation and accessibility

Adapt tasks and composition, not just font sizes. Specify changes to navigation, grids, forms, data views, overlays and primary actions. Preserve essential information on smaller screens.

Verify semantics, heading hierarchy, accessible names, keyboard reachability, visible focus and status feedback. Manage overlay focus according to its pattern; return focus on close where appropriate. Do not rely only on color.

Target WCAG AA contrast: 4.5:1 for normal text, 3:1 for large text and relevant non-text controls. Honor reduced-motion preferences for significant motion. Validate with real content, long labels and relevant locale formatting.
