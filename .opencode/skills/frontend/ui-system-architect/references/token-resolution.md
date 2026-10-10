# Visual token resolution

## Modes

| Mode | Use when | Effect |
|---|---|---|
| `preserve` | An existing system is coherent and no migration was requested | Existing values and native APIs remain authoritative; profile tokens fill only unresolved roles |
| `adopt` | A new project or an approved migration adopts the profile | The profile fallback becomes the visual baseline and is translated into the chosen stack |

## Resolution order

1. Read the recorded frontend contract and explicit user decisions.
2. Locate the implemented theme, CSS variables, design tokens, component defaults, and icon/font sources.
3. Map profile roles to native project tokens and component variants. Record actual source paths, not copied values.
4. Resolve remaining roles from [`../assets/tokens.json`](../assets/tokens.json) only when the active mode permits it.
5. Stop the affected visual decision when no source exists or when sources conflict materially.

Use the project's native expression. If the project resolves 16px as `theme.spacing(2)`, use that API rather than embedding `16px`. A mapping proves semantic and state equivalence; matching one raw color or dimension is insufficient.

Profile specifications reference token paths such as `{component.button.md}`. Those references are validated against the fallback token file. Do not duplicate resolved numbers in component or pattern specifications.
