# Backoffice page patterns

Patterns choose composition, not business behavior. All pages live inside the selected shell and keep at most one visually primary action per section.

| Pattern | Required composition | Required states |
|---|---|---|
| List | PageHeader, FilterBar when useful, DataTableLayout | loading, empty, error, loaded |
| Create | PageHeader, FormSection set, form actions | initial, validating, submitting, backend error, success |
| Edit | PageHeader, loaded record, FormSection set, form actions | loading, unavailable, dirty, submitting, backend error, success |
| Detail | PageHeader with status/actions, summary, optional tabs, related content | loading, unavailable, error, loaded |

Create and edit actions follow the canonical operation-feedback contract. Detail tabs exist only for meaningful information groups. On narrow screens, transform unreadable tables into the record representation defined by the table contract rather than compressing every column.
