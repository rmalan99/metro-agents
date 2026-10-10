# Backoffice layout contracts

## Shell

Desktop uses persistent sidebar, app bar, and main content. Tablet may collapse the sidebar while preserving explicit control and user preference. Mobile uses an app bar and temporary navigation drawer with focus containment, Escape close, and focus return. Resolve shell geometry from `{layout.shell}`.

## Page

Resolve maximum width, responsive padding, and section gaps from `{layout.page}`. Wide data views may use the available workspace; focused forms may use a narrower content measure when that improves completion without hiding context.

## Grid and breakpoints

Use `{grid}` and `{breakpoint}` as fallback values. Breakpoints describe behavior changes rather than device brands. Verify shell navigation, forms, overlays, page actions, and record views at each supported mode; shrinking typography alone is not responsive adaptation.
