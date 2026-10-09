# Chakra UI integration for React

Load for Chakra setup, semantic tokens, component recipes or integration issues. Determine the installed major before any setup. Version 2 and version 3 use materially different providers, configuration and several component APIs.

## Version routing
| Concern | v2 family | v3 family |
|---|---|---|
| Shared theme | `extendTheme` | System configuration, commonly `defineConfig` / `createSystem` |
| Provider | Theme-based provider | System value-based provider |
| Shared component styling | Component style configuration | Recipes / slot recipes |
| Component composition | Inspect v2 component APIs | Inspect v3 compound component APIs |

These are routing cues, not interchangeable snippets. For another major, use its official guidance. Inspect local generated provider/snippets as well as package exports.

## Setup sequence
1. Inspect packages, provider, existing theme/system, color-mode integration and component wrappers.
2. Reuse existing setup. For a new one, follow the installed major's framework installation guide, including generated snippets only when needed.
3. Place the provider at a deliberate shared boundary compatible with the framework's execution model.
4. Register semantic colors, typography, spacing and component treatment through that major's theme/system mechanism.
5. Generate or update token typings when that version requires it; do not bypass type errors with broad casts.
6. Verify a control and portal overlay in the supported modes.

## Styling decisions
Use semantic tokens for foreground/background relationships and state meanings. Use the library's responsive style properties according to project breakpoints. Shared component defaults/variants belong in component configuration or recipes; local placement belongs at composition sites.

For v3 recipes, distinguish a single-element recipe from a multi-slot component recipe. Keep slots consistent with the actual component anatomy. For v2, use its supported component-theme pattern instead of copying recipe code.

Example decision: if every card needs a subtle border and agreed radius, define a shared card treatment. If a single card spans two columns, keep that grid placement local. If every destructive action needs consistent emphasis, use the semantic danger/destructive variant rather than hard-coded red values.

## Interactions
Preserve the selected major's dialog/menu/field composition. Verify labels and errors are connected to inputs; a visible error paragraph alone is insufficient. Loading controls reflect actual operation state and prevent duplicate submission.

Inspect portal and layering configuration before changing z-index values. Do not set arbitrary enormous z-index values to compensate for incorrect overlay placement.

## Troubleshooting
| Symptom | Inspect | Correct at |
|---|---|---|
| Examples do not compile | Installed major vs example API | Version-appropriate implementation |
| Token unknown or not typed | Registration, value shape, generated typings | Theme/system setup |
| Wrong initial color mode | Existing mode provider and server/client initialization | Framework mode integration |
| Overlay styling/focus differs | Provider, portal and compound component structure | Component integration |
| Repeated local overrides | Recipe/component defaults | Shared visual configuration |

Verify modes actually supported, hydration where relevant, typed tokens, keyboard behavior and consumers of updated shared recipes. Record the major and configuration entry point in the frontend contract.
