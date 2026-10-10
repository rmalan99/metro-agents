---
name: ui-system-architect
description: "Trigger: UI architecture, design-system baseline, visual profile, missing theme. Resolve and persist an on-demand UI system before implementation."
license: Apache-2.0
metadata:
  author: "metro-agents"
  version: "1.0.0"
---

# UI System Architect

## Activation Contract
Load for a new frontend, a missing or conflicting visual system, an explicit system migration, or a request to establish shared UI architecture. Do not load for a bounded screen that already has a resolved frontend contract.

## Hard Rules
- Apply [`frontend-developer`](../frontend-developer/SKILL.md), [project discovery](../frontend-developer/references/project-discovery.md), [visual ownership](../frontend-developer/references/design-system.md), and [component contracts](../frontend-developer/references/component-contracts.md); do not restate their rules.
- Classify product surface separately from platform. Mobile is a platform, not an alternative to backoffice or website.
- Preserve an adopted project system by default. Use this skill's tokens only for unresolved values, a new project, or an explicitly approved migration.
- Never invent a visual value or silently mix profile values with conflicting project values. Record mappings, exceptions, and missing extensions.
- Resolve architecture before delegating implementation. A Junior implements the recorded contract and does not redesign it.

## Decision Gates
| Condition | Action |
|---|---|
| Existing coherent system | Use `preserve` mode and map the selected profile to it |
| New project or explicit full adoption | Use `adopt` mode and the profile fallback tokens |
| Several systems coexist | Record ownership boundaries; do not migrate unrelated UI |
| Material conflict or unsupported profile | Return the decision upward before dependent work |

Only `backoffice` is implemented in V1. Marketing website, product web, and native mobile require a profile extension rather than an improvised fallback.

## Execution Steps
1. Inspect the existing theme, tokens, shared components, supported platforms, users, tasks, density, and accessibility constraints.
2. Classify surface, platform, composition, and density using [profile selection](references/profile-selection.md).
3. Select `preserve` or `adopt`, then resolve values with [token resolution](references/token-resolution.md).
4. For backoffice work, load only the applicable files under [`references/profiles/backoffice/`](references/profiles/backoffice/profile.md).
5. Persist the result using [frontend contract output](references/frontend-contract-output.md) before implementation tasks are issued.

## Output Contract
Return the selected profile, classification axes, adoption mode, source paths, token mappings, loaded contracts, exceptions, missing extensions, and unresolved material decisions.

## References
- [`assets/tokens.json`](assets/tokens.json) and [`assets/tokens.schema.json`](assets/tokens.schema.json) - validated fallback source.
- [`references/foundations.md`](references/foundations.md) - fallback foundation roles and accessibility constraints.
- [`references/profiles/backoffice/profile.md`](references/profiles/backoffice/profile.md) - V1 profile router.
