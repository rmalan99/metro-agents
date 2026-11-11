---
name: frontend-base-components
description: 'Trigger: frontend base component, reusable field, dialog, table, pagination, component catalog. Decide when and how to create tested, accessible frontend primitives.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'jacobito'
  version: '1.2'
---

## Activation Contract

Use when creating or reviewing reusable frontend components such as fields, dialogs/modals, tables, pagination, or shared interaction primitives. Always load `../component-composition/SKILL.md`. Load `../frontend-module-architecture/SKILL.md` when deciding placement or public boundaries, `../../qa/testing-behavior/SKILL.md` when implementing or reviewing tests, and `../../qa/frontend-validation/SKILL.md` during implementation or closure.

## Hard Rules

- Create a base only for a stable behavior with demonstrated consumers; do not manufacture abstractions for hypothetical reuse or boilerplate reduction alone.
- Preserve layers: `base` owns generic presentation/accessibility, `composed` combines bases, and `specialized` adds feature-specific behavior.
- Expose explicit, typed props and controlled state contracts. Base components must not know business rules, HTTP, domain models, or form-library state.
- Accept and forward `data-testid` or the project-equivalent test identifier to the meaningful root/control; never hardcode one value that collides across instances. Follow `../frontend-ui-quality/references/testability-identifiers.md`.
- Put integration in separate adapters (for example RHF), without duplicating base markup, styling, or behavior.
- Cover accessible names, labels, keyboard/focus behavior, and relevant loading, empty, error, disabled, and permission states. Test behavior, not implementation.
- Add shared components to the development catalog with variants, states, and usage examples.
- Every component under `app/shared/components` requires its catalog entry in the same task. Create or modify test files only when the user explicitly requests tests; testability instrumentation and catalog states do not grant that authorization.
- Keep the catalog for development and visual review, never as product navigation. Do not globalize a component merely to catalog it.
- Place visual form primitives in `app/shared/components/fields/base` and form-library adapters in `app/shared/components/fields/rhf`; consumers use those contracts instead of parallel global field APIs.
- A base field depends on props only and never on RHF, Context, stores, HTTP, remote search, transformation, or business rules. Put those concerns in adapters, hooks, or specialized components.
- Apply the field-specific contracts in `references/field-contracts.md` when working with password or file fields.

## Decision Gates

| Evidence                                      | Action                                           |
| --------------------------------------------- | ------------------------------------------------ |
| Existing component fits                       | Reuse or compose it                              |
| One module owns the behavior                  | Keep it in that module                           |
| Multiple real consumers share stable behavior | Create or adapt a base                           |
| Only data/business differs                    | Use props, composition, or a specialized wrapper |
| Placement or public boundary changes          | Load `../frontend-module-architecture/SKILL.md`  |
| Tests are implemented or reviewed             | Load `../../qa/testing-behavior/SKILL.md`              |
| Component is implemented or closed            | Load `../../qa/frontend-validation/SKILL.md`           |

## Execution Steps

1. Search existing components and record why reuse or adaptation is insufficient.
2. Define scope, explicit props, states, accessibility contract, and consumer examples.
3. Si decides ubicación o fronteras públicas, carga `../frontend-module-architecture/SKILL.md` y coloca la capa mínima; en otro caso conserva la ubicación vigente.
4. Si implementas o revisas pruebas, carga `../../qa/testing-behavior/SKILL.md` y cubre catálogo y comportamiento; si implementas o cierras, carga `../../qa/frontend-validation/SKILL.md`.

## Output Contract

Report consumers, chosen layer, public props, excluded concerns, accessibility/states, tests, catalog entry, and validation results.

## References

- `../component-composition/SKILL.md` — composition and layer boundaries.
- `../frontend-module-architecture/SKILL.md` — canonical placement and dependency boundaries.
- `../../qa/testing-behavior/SKILL.md` — behavior-first testing policy.
- `../../qa/frontend-validation/SKILL.md` — closure gates for shared components.
- `references/field-contracts.md` — specific PasswordField and FileField contracts.
- `../frontend-ui-quality/references/testability-identifiers.md` — stable test identifier contract.
