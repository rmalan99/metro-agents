# Password field

Use the shared field anatomy/state contract from `../../SKILL.md`. Implement every password field as a specialized variant composed from the project-owned base field, never as page-local input anatomy.

Every password field has an internal show/hide icon button using the adopted icon set's visible/hidden pair. Do not render `Show`/`Hide` or equivalent visible text in place of the icon unless the product explicitly requires a labeled action. The icon is visual; the keyboard-reachable `type="button"` supplies a state-aware accessible name and pressed state when applicable. Retain the same value, control identity, focus/caret where possible and appropriate autocomplete across visibility changes.

Never expose the secret in identifiers, logs or telemetry. Verify toggling does not submit/clear the form and maintains control identity/focus.
