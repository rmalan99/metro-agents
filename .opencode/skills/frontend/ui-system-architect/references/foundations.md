# Fallback foundations

Use [`../assets/tokens.json`](../assets/tokens.json) only under the resolution rules. It contains palette values, semantic roles, typography, spacing, radii, icons, control sizing, elevation, motion, layers, breakpoints, layout, and component geometry.

## Invariants

- Components consume semantic roles such as canvas, surface, text, border, action, focus, and status. Raw palette values are theme construction inputs, not local component choices.
- Normal text targets WCAG AA 4.5:1; large text and relevant non-text controls target 3:1. Verify every foreground/background state in the implemented stack.
- A 32px visual control keeps at least the `{control.hitArea.minimum}` interactive area unless adjacent targets would overlap.
- Focus remains visible, status never relies on color alone, and significant motion respects reduced-motion preferences.
- Supported spacing, radius, icon, and sizing values come from tokens. A missing value is an extension request, not permission to interpolate.
- Existing project fonts and icon sets remain authoritative in `preserve` mode. The fallback font and icon family apply only in `adopt` mode.
