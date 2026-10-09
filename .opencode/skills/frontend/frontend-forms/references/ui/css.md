# css — shared form contract integration

Inherits `../../SKILL.md`; this reference supplies the selected UI binding only.

Implement `frontend-forms` with shared semantic markup and classes/data attributes for invalid field state. Apply the danger token to border, label and message; preserve the independent focus-visible rule. Associate helper/error nodes with the control.

CSS does not provide reactive validation, backend mapping, password toggling, masks or date-dialog behavior. Keep those responsibilities in field variants/form adapters. Every required field needs the visible marker and programmatic state, and every variant accepts helper and empty-value guidance.

Custom select and searchable combobox share visual tokens but need their own complete accessible interaction behavior. Use the 10/11 option threshold and an accessible dialog for date selection. Do not replace these requirements with a visually styled native select or noninteractive calendar. If a compatible primitive is needed, follow the agreed dependency process.
