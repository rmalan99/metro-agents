# Frontend contract output

Record UI architecture in the project's existing frontend contract or create one from [`../../frontend-developer/references/frontend-contract.template.md`](../../frontend-developer/references/frontend-contract.template.md). Keep decisions concise and point to implementation sources.

Required UI-system fields:

| Field | Required value |
|---|---|
| Product surface | selected surface and evidence |
| Platform | runtime and supported viewport/input model |
| Composition and density | selected values and rationale |
| Visual profile | profile name and version |
| Adoption mode | `preserve` or `adopt` |
| Theme/token source | actual project path or fallback asset path |
| Token mappings | profile role to native token/API path |
| Component defaults | actual shared component and variant paths |
| Loaded contracts | only references needed by current implementation |
| Exceptions | intentional deviations, owner, and scope |
| Missing extensions | unresolved tokens, components, patterns, or profiles |

## Decision and persistence handoff

The Frontend Lead owns the architecture decision but never writes files. First resolve the profile, adoption mode, token mappings, variants and outstanding decisions. Return material product ambiguity to the Orchestrator before proceeding.

Then issue one bounded documentation task to Frontend Junior containing those exact decisions, the contract destination and the permitted write scope. The Junior creates or updates only that project contract, preserves unrelated conventions and reports its path and changes. It does not redesign the system or edit production components in this task.

The Lead reads the saved contract and accepts it or requests a bounded correction. Only after acceptance may the Lead issue dependent implementation tasks, each referencing the saved contract and applicable profile files. A report without the persisted contract is not a completed handoff. New decisions return to the Lead rather than becoming local Junior assumptions.
