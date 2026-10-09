# Password field

Use the shared field anatomy/state contract from `../../SKILL.md`. Every password field has an internal show/hide button. It is a keyboard-reachable non-submit button with a state-aware accessible name (and pressed state when applicable). Retain the same value, focus/caret where possible and appropriate autocomplete across visibility changes.

Never expose the secret in identifiers, logs or telemetry. Verify toggling does not submit/clear the form and maintains control identity/focus.
