# css — shared form contract integration

Inherits `../../SKILL.md`; this reference supplies the selected UI binding only.

Implement `frontend-forms` with shared semantic markup and classes/data attributes for invalid field state. Apply the danger token to border, label and message; preserve the independent focus-visible rule. Associate helper/error nodes with the control.

CSS does not provide reactive validation, backend mapping, password toggling, icons, masks or date-dialog behavior. Keep those responsibilities in project-owned field variants/form adapters. A password action uses the project's adopted visibility icon pair inside a named non-submit button, not visible `Show`/`Hide` text; dependency choice follows the agreed process. Every required field needs the visible marker and programmatic state, and every variant accepts helper and empty-value guidance.

Custom select and searchable combobox share visual tokens but need their own complete accessible interaction behavior. Apply the selection mode from the parent's field reference and an accessible dialog for date selection. Do not replace these requirements with a visually styled native select or noninteractive calendar. If a compatible primitive is needed, follow the agreed dependency process.
