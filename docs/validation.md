# Repository validation and runtime checks

## Offline gate

Run the commands in the [README](../README.md). The validator checks skill identities, local references/fences, exact repeated prose blocks of 25+ words, single-source artifact definitions, registered owners, dispatch/skill targets and intended restricted-read patterns. It supports the JSONC comments/trailing commas used by OpenCode configuration.

The ownership registry is a machine-checkable location catalog, not a copy of the rule text. Update it when adding/removing an owner or canonical artifact. The validator detects exact duplication, not semantic equivalence; reviewers still check that specialties contribute unique behavior.

Unit tests exercise negative configuration/document mutations, relocation, JSONC handling and TODO bootstrap failure cases. Logger tests use temporary files only; production incidents are never manufactured for testing. The logger's append strategy is unchanged because current evidence did not justify a more complex persistence mechanism.

## Selective context

Measure documents actually required by a role/task, not total repository size. Count each file once within an invocation. Separate role/core/schema overhead from code, specialty references and tool output; word counts are not tokenizer measurements. Moving detail to references reduces the compulsory baseline but does not eliminate task-specific costs.

Load delivery core → active role → required artifact/quality/concurrency references. Frontend loads its core → relevant technical contract/tool → selected specialty/variant. Do not preload the catalog or assume another agent's loaded text is already available.

## Runtime smoke test in the installed OpenCode environment

OpenCode is not installed in this execution workspace, so these checks are not claimed as executed:

1. Load the configuration with the target runtime/version and confirm prompt substitution and recursive skill discovery. Check provider access and configured model/options before dispatch.
2. From Orchestrator/Evaluator, read their allowed role/schema documents. Attempt to read a harmless source fixture and confirm denial. Check both relative and normalized absolute paths. Static matching is not proof of runtime enforcement.
3. Run a bounded disposable development/QA fixture through the permitted hierarchy. Confirm returned artifacts include required quality/evidence fields and are reviewed before final acceptance.
4. Exercise sequential fallback and supported parallel dispatch using disjoint temporary scopes. Confirm real active workers, reservations, cancellation and cleanup; instruction limits are not a scheduler.
5. Verify meaningful independent QA and correction/regression routing. Do not infer success from a running process or from configuration parsing.
6. If TODO is needed, follow [TODO setup](todo-mcp.md) and verify tool exposure using the actual installed extension. The bootstrap alone does not supply a TODO server.

These require a real runtime/provider and must produce objective evidence before claiming agent execution, enforced boundaries or latency improvements. Do not change configured models based only on shorter prompts.
