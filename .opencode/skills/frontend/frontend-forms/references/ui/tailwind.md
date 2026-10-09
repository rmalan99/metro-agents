# tailwind — shared form contract integration

Inherits `../../SKILL.md`; this reference supplies the selected UI binding only.

Implement `frontend-forms` using shared field components and semantic theme classes for invalid border, label and error text. Utility classes alone do not implement dirty/touched, validation, focus or ARIA relationships.

Provide labeled controls, required marker, helper/error nodes, placeholder guidance and icon slots. A password action must be a named non-submit icon button using the project's adopted visibility icon pair, not visible `Show`/`Hide` text; do not add an icon package without approval. Use accessible primitives for custom select/combobox and date dialog if approved; do not invent partial keyboard behavior with styled divs. Selection mode follows the field reference routed by the parent.

Keep form-tool adapters and feature data adapters separate from styled base fields. For masks and phone numbers, implement or adopt real caret/editing/normalization behavior. Verify danger and focus classes coexist, including when disabled or during submission.
