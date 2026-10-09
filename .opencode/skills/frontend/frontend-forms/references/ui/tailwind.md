# tailwind — shared form contract integration

Read only when this UI system is adopted and form work requires its integration details. Apply `../../SKILL.md`; consult the tool-specific UI setup guide separately when needed.

Implement `frontend-forms` using shared field components and semantic theme classes for invalid border, label and error text. Utility classes alone do not implement dirty/touched, validation, focus or ARIA relationships.

Provide labeled controls, required marker, helper/error nodes, placeholder guidance and icon slots. A password icon must be a named non-submit button. Use accessible primitives for custom select/combobox and date dialog if approved; do not invent partial keyboard behavior with styled divs. The selection threshold is 10/11 total options.

Keep form-tool adapters and feature data adapters separate from styled base fields. For masks and phone numbers, implement or adopt real caret/editing/normalization behavior. Verify danger and focus classes coexist, including when disabled or during submission.
