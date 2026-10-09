---
name: backoffice-dashboards
version: 1.0.0
description: Complementary back-office skill for actionable metrics, period comparisons, charts, informative cards, drill-down and dashboard verification.
---

# Back Office Dashboards

## Scope
Load for administrative metrics and monitoring dashboards. Apply the shared frontend contract and the shell conventions from `../backoffice-design/SKILL.md`; do not reload the shell skill for an isolated chart fix if its contract is already available. Tables follow `../frontend-tables/SKILL.md` when needed.

## 1. Define the decision before the chart
For each block specify who uses it, what question it answers and the action it enables. Remove metrics that only fill space. Prioritize exceptions, pending work and relevant trends over arbitrary KPI counts.

Establish a metric contract: definition, aggregation, unit/currency, source, period, time zone, refresh expectations, comparison period and optional drill-down. Distinguish business events such as paid revenue from issued invoices. Do not combine currencies or scopes without an explicit aggregation rule.

If source data cannot supply a metric, explain the gap; do not invent a production value. Mark demonstration datasets clearly.

## 2. Informative cards
Present label, value, unit/period and comparison where useful. Avoid duplicate help. A change has direction and interpretation: an increase in cancellations can be unfavorable. Do not mechanically color every increase green.

Define percentage behavior when the baseline is zero or missing. Example: previous 0/current 12 is not a finite percentage increase; show a suitable new-activity label or absolute difference. Missing is not zero.

A clickable card opens a meaningful filtered detail preserving period/scope. If no destination exists, keep it informational rather than creating fake interaction.

## 3. Choose honest visual encodings
Use lines for ordered time trends, bars for category comparison and composition charts only when proportions are meaningful and categories remain legible. Use a table or textual summary when precision or heterogeneous values matter more than a chart.

- Bar charts use a zero baseline; explain intentional axis choices on other charts where interpretation could change.
- Label units, series, periods and relevant axes. Avoid 3D, decorative perspective and misleading area scaling.
- Show gaps for missing observations; do not silently connect absent data as continuous activity.
- Distinguish data availability from true zero.
- Provide meaningful textual summaries or accessible data tables for important chart information.
- Use colors consistently by meaning/series; do not depend solely on color or hover tooltips.
- Use the project's adopted chart library; assess a new dependency only if capability is missing.

## 4. Composition and filters
Arrange dominant tasks first, then relevant trends, then recent activity or secondary context. Use an adaptive grid and intentional spans rather than forcing every card to equal size.

Declare whether filters affect the entire dashboard or one widget; label local overrides. Align comparisons with the selected period and scope. Guard against mixed old/new period results during refresh; show updating or freshness clearly.

On narrow screens, reorder by task priority and retain readable labels. Do not shrink charts until text is illegible. Define empty, filtered-empty, loading, partial failure and stale-data states per widget where data sources are independent.

## 5. Verify
Check metric calculations with representative values, zero baseline, missing data, date boundaries and relevant time zones. Confirm period/filter propagation, refresh behavior, drill-down and accessible alternatives. Inspect chart labels at supported widths. Report visual checks separately from numeric checks and identify unverifiable source assumptions.
