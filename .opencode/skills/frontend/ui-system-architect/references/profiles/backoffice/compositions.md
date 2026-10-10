# Backoffice composition contracts

## FormField

Compose label, control, and optional helper/error message. Resolve vertical gaps and type from `{composition.formField}`. Reserve message space only when the project contract requires stable layout; otherwise let the field grow without overlapping adjacent content.

## FormSection

Compose title, optional description, and a responsive field grid. Resolve heading gaps and grid geometry from `{composition.formSection}`. Use one, two, or three field spans according to content length and supported width, never merely to fill columns.

## PageHeader

Compose optional breadcrumb, title row, one primary action, secondary actions, and optional description. Resolve spacing and action gap from `{composition.pageHeader}`. Do not duplicate a title already owned by the app bar.

## FilterBar

Compose search, task-relevant filters, and secondary actions. Resolve geometry from `{composition.filterBar}`. Advanced filters may move to a popover or drawer; active criteria remain visible and removable.

## DataTableLayout

Compose FilterBar, table state/content, bulk-action region when selection exists, and pagination. Resolve section gaps from `{composition.dataTableLayout}`. Loading, empty, error, and loaded states occupy the same semantic content region.
