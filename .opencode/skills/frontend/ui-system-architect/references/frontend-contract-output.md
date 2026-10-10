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

The Frontend Lead owns this architecture decision and hands the recorded paths to implementation tasks. Material product ambiguity returns to the Orchestrator; the Junior does not resolve it locally.
