# Translating visual intent into a shared system

Read for theme establishment or a platform-wide style adjustment, not every local fix. Use the active tool's library reference for APIs.

## 1. Extract intent

Describe the reference in reusable terms: dominant surface, navigation contrast, content width, density, typography hierarchy, borders, elevation and emphasized action. Treat sample names, arbitrary metrics, perspective mockups and decorative framing as content, not requirements.

Example: a dark administrative sidebar implies a separate navigation surface and contrasting foreground; it does not imply changing every content card to the brand color.

## 2. Inventory and map

Locate existing tokens and component styles. Map semantic roles before values:

| Role | Meaning | Typical consumers |
|---|---|---|
| canvas | Application background | Layout |
| surface / surface-muted | Content layers | Cards, panels |
| text / text-muted | Primary and secondary reading | Titles, labels, help |
| border | Structural separation | Cards, fields, dividers |
| primary + foreground | Main action | Buttons, selected controls |
| navigation + foreground | Persistent navigation | Sidebar |
| selected + foreground | Current location or selection | Menu item, tabs |
| success / warning / danger | Semantic result or risk | Status, feedback |
| focus | Keyboard orientation | Interactive controls |

Map these roles to existing library token names; these are conceptual roles, not a required parallel naming scheme. Check foreground/background pairs in each state. Danger and primary are different meanings even when their colors happen to resemble each other.

Use a small spacing scale, consistent radii, typography roles and layering conventions. Starting spacing may be 4/8/12/16/24/32, but adopt the project's scale if it already works. Record intentional exceptions, not every pixel.

## 3. Choose the owner

If three screens compensate for the same button shape, fix the button default. If only a confirmation action is destructive, use a danger variant. If one page has a two-column composition, keep it in that layout. Do not use global overrides to solve one screen's exception.

## 4. Establish representative components

Use existing or task-relevant button, input, card, menu and dialog. Compare default, hover, focus, disabled, loading and error states. Verify overlays outside the main layout inherit the theme. Test the supported color modes only; adding a dark navigation surface is not a request for full dark mode.

Help text explains format, scope or consequence; it should not repeat a heading or visible value. Distinguish title, value, label and help with a consistent hierarchy rather than increasing every font weight.

## 5. Validate propagation

Inspect a representative data view and form with realistic content. Check narrow and wide layouts, long labels, visible keyboard focus and contrast. When a token changes, inspect consumers affected by that token rather than only the screen that prompted it.

Do not report homogeneous styling until shared consumers were inspected. Record the theme source, variant definitions and verification evidence in the frontend contract.
