# Data, state and integration contract

Load for frontend state, requests, mutations, authorization or performance/integration work. Tools implement the mechanisms. Form/table specialties add their own behavior.

## Data and state

Choose ownership by consumers and lifetime: interaction-local, shared application, remote/server or URL state. The tool skill supplies mechanisms; do not prescribe stores or hooks here.

- Define initial loading, empty data, filtered-empty, recoverable error, success and denied-access states where relevant.
- Prevent duplicate submissions and stale responses from overwriting newer results.
- Confirm destructive actions according to their impact and support recovery when viable.
- Retain useful data during recoverable refresh failures when safe; label freshness when it matters.
- Form-specific behavior is owned by `../../frontend-forms/SKILL.md`; use its router when generating or modifying forms.
- Protect unsaved changes where losing them is consequential.
- Do not invent endpoints or represent demonstration data as production data.
- Hidden controls are not authorization. Enforce permissions at the trusted boundary when a backend exists.

## Integration and performance

Respect the tool's execution/rendering model. Keep secrets out of delivered frontend code. Treat external/user input as untrusted and keep sensitive details out of logs and user-facing errors. Add dependencies only for a demonstrated capability and under existing dependency rules.

Avoid duplicate requests, unnecessarily global modules and disproportionate assets. Use code splitting, virtualization or memoization when scale or measurement warrants it; use the tool's specialized guidance rather than generic optimization rituals.
