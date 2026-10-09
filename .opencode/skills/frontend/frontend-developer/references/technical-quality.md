# Frontend technical quality

Read for implementation/review/verification. Delivery evidence and acceptance are owned by coordination.

Run project-required checks and meaningful validation for affected behavior. Include negative/edge states, viewport adaptation and keyboard interaction relevant to the change. Add tests for significant behavior, not assertions that merely reproduce implementation.

Keep names descriptive and business rules explicit. Remove obsolete/debug/commented-out code introduced by the change. Follow the project formatter/linter and keep public APIs proportional. Do not suppress type/lint errors with broad casts or unjustified directives. Add a regression test for a bug fix when practical.

Hand off technical decisions and actual verification evidence under the delivery contract. No visual verification claim from text-only inspection.

Use applicable specialty/selector owners for their additional acceptance checks; do not reproduce their checklists here.

Technical readiness is not delivery completion. The coordination skill owns statuses, independent acceptance and final gates.

## Persistent project decisions

Reuse existing project documentation. When establishing or changing a shared base, record decisions using `frontend-contract.template.md` if necessary. For a small fix, update only affected existing conventions.

Record actual file locations, responsibilities, tokens, component-extension rules, data conventions and verification commands. Never fill unknown fields with invented answers.

Specialty skills consult this contract and update it when an authorized change affects shared decisions. They must not introduce parallel themes or silently change stack, architecture or requirements.
