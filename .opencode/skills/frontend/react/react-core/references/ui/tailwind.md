# Tailwind without a component library

Load for utility-based React styling or Tailwind configuration. Tailwind supplies styles, not the interaction behavior of a UI library.

## Discovery and version routing
Inspect the installed Tailwind major, build integration, stylesheet entry, token definitions, content/source discovery, class-composition helpers and existing components.

- v3 commonly uses JavaScript configuration, content paths and Tailwind directives.
- v4 uses CSS-first configuration and different integration/source mechanisms.
- Do not assume a v3 configuration file is automatically consumed by v4 or copy v4 directives into v3.

For setup, consult the installed major's official guide for the actual bundler/framework. Do not install several integration paths at once.

## Shared styles
Map semantic roles to the native theme and existing CSS variables. For v3 this often involves configuration mappings; for v4 use its supported CSS theme mechanism. Keep global typography/normalization in the base layer and shared component treatment in intentional components/variants.

Do not duplicate long class strings across screens. Extract a component when it owns an actual repeated pattern; for a purely visual repeated treatment, use the project's variant/composition strategy. Avoid adding a variant library merely to choose between two styles.

## Class detection
The compiler must be able to discover full class names. Do not construct utility names from arbitrary runtime strings.

```tsx
const statusClass = {
  paid: 'bg-emerald-50 text-emerald-800',
  pending: 'bg-amber-50 text-amber-800',
};
// Illustrates static detection; use the project's semantic tokens
// instead of these literal colors in the shared product component.
```

For truly dynamic numeric values, use a scoped style/custom property when appropriate rather than generating a new class name. For external/shared source packages, configure source discovery with the installed major's mechanism.

## Component behavior
Start with semantic HTML. Implement labels, errors, keyboard behavior, focus and async feedback explicitly. For complex menus/dialogs, evaluate an accessible primitive under the project's dependency policy. If it changes the agreed technology choice, resolve that decision first.

Use one consistent class merge strategy if needed. Verify how utilities conflict before adding `!important`. Keep arbitrary values for justified local exceptions, not repeated substitutes for theme tokens.

## Troubleshooting and verification
| Symptom | Inspect | Fix |
|---|---|---|
| Utility absent from output | Static class detection, source paths, version | Detection/configuration |
| Shared token class missing | Theme namespace/mapping | Native theme |
| Different spacing on each page | Duplicated strings/arbitrary values | Shared scale/component |
| Styling exists but control is unusable by keyboard | Semantic element and interaction implementation | Behavior, not CSS |
| Reset affects existing controls | Preflight/base styles and layering | Deliberate base integration |

Run a production build when detection/build configuration changes. Check generated styles, long content, responsive composition, focus and reduced motion. Record token source and class-composition rules.

## Shared form contract integration
Implement `frontend-forms` using shared field components and semantic theme classes for invalid border, label and error text. Utility classes alone do not implement dirty/touched, validation, focus or ARIA relationships.

Provide labeled controls, required marker, helper/error nodes, placeholder guidance and icon slots. A password icon must be a named non-submit button. Use accessible primitives for custom select/combobox and date dialog if approved; do not invent partial keyboard behavior with styled divs. The selection threshold is 10/11 total options.

Keep form-tool adapters and feature data adapters separate from styled base fields. For masks and phone numbers, implement or adopt real caret/editing/normalization behavior. Verify danger and focus classes coexist, including when disabled or during submission.
