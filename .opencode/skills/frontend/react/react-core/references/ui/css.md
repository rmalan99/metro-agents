# Plain CSS for React

Load for CSS-based setup, tokens, component styling or cascade issues without introducing a UI library.

## Discovery
Identify global styles, component-scoped styles/modules, reset, import order, naming conventions, custom properties and build support. Preserve the adopted strategy rather than introducing CSS Modules or a CSS-in-JS engine during an unrelated change.

## Base setup
1. Define shared tokens in the existing global source using semantic custom properties.
2. Apply a deliberate normalization/base, checking effects on native controls.
3. Establish typography and layout primitives with Grid/Flexbox.
4. Scope component styling through the current module/naming convention.
5. Add local composition styles without overriding the global system.

Example of a small shared foundation:

```css
:root {
  --surface: #fff;
  --text: #18202a;
  --border: #d7dce2;
  --focus: #3347b0;
  --space-4: 1rem;
  --radius-card: .5rem;
}
.record-card {
  color: var(--text);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-card);
  padding: var(--space-4);
}
.record-card a:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
```

Adapt values and naming to the contract. Define a reusable token for a shared responsibility, not every isolated measurement. Verify actual foreground/background pairs; example values are not a substitute for validation.

## Components and cascade
Use variants via explicit classes or data attributes under the adopted convention. Avoid deep selectors tied to incidental page markup. Keep specificity low; inspect winning declarations before adding `!important`.

Use cascade layers only if supported and intentionally ordered; unlayered styles can outrank normal layered styles. CSS Modules scope names, not all inheritance or global resets. Portals outside a styled container may need globally available tokens; fix scope rather than duplicating colors.

Use content-driven breakpoints and intrinsic sizing. Check flex/grid children for min-width overflow before hiding content. Respect reduced-motion preferences when adding movement.

## Behavior and diagnostics
CSS does not implement dialog semantics, keyboard menus, validation or focus return. Build those with native/platform mechanisms or an explicitly selected accessible primitive.

| Symptom | Inspect | Fix |
|---|---|---|
| Style unexpectedly overwritten | Cascade, specificity, import order, layers | Correct ownership/order |
| Overlay lacks tokens | Custom-property scope and portal location | Shared token boundary |
| Narrow layout overflows | Intrinsic width, grid/flex minimums, long values | Layout constraints |
| Focus invisible | Reset and focus selectors | Accessible shared focus rule |
| Repeated hard-coded values | Actual shared meaning | Tokens/variants |

Verify affected component states, keyboard operation, supported widths and global reset consumers. Record style scope and import conventions. Avoid building a custom CSS framework for a few components.
