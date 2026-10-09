# shadcn — shared form contract integration

Inherits `../../SKILL.md`; this reference supplies the selected UI binding only.

Apply `frontend-forms` through the locally generated field components, not an assumed latest template API. Inspect whether the project owns Field, Form or another composition; preserve label/control/help/error relationships and connect only the adopted form tool.

Use the local Input plus shared field anatomy for text/password; add the mandatory named non-submit visibility action. Use the generated custom Select up to 10 options and the project's accessible searchable combobox composition above 10. Popover/command-style examples require verification of actual keyboard/combobox semantics; visual similarity alone is insufficient.

Compose the local calendar with an accessible dialog when implementing the requested date modal; a nonmodal popover alone does not satisfy that contract. Phone/mask support requires actual editing and normalization capability, not decorative formatting. Theme invalid label, border and message once, and retain the test-ID/focus contract through all generated primitives.
