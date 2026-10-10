# Backoffice data and content contracts

## Identity and summaries

Resolve avatar sizes from `{component.avatar}`. Provide a textual fallback and accessible name when identity matters. Avatar groups expose hidden-count context. Key-value views align labels and values for scanning; summary cards use the shared Card contract and do not invent local metric styling.

## Lists, trees, and activity

Lists provide stable item anatomy, clear record navigation, local actions, and loading/empty/error states. Trees are limited to genuinely hierarchical data and expose expansion semantics and keyboard behavior. Timeline, activity, and audit views distinguish actor, action, target, time, and metadata without encoding meaning solely through icons.

## Dates and files

Date, time, range, and calendar controls use locale-aware display while preserving canonical values from the form contract. File upload, dropzone, item, progress, error, and preview geometry resolves from `{component.file}`. Validate type and size, make removal explicit, and never use drag-and-drop as the only upload mechanism.

## Disclosure and utilities

Accordion and collapse patterns expose expanded state and keep headings meaningful. Copy and overflow controls use real icon buttons, accessible names, visible focus, and operation feedback. Charts and metric containers defer meaning, legends, comparisons, and drill-down to the dashboard specialty while retaining shared surface and typography tokens.
