# Date field

Use the shared field anatomy/state contract from `../../SKILL.md`. Activating the control/trigger opens an accessible date-selection dialog. Use the adopted library's calendar/dialog capability; permit keyboard/manual entry where appropriate and display format/constraint guidance.

Define date-only versus timestamp semantics and time zone. Do not shift date-only selections through UTC conversions. Align min/max/disabled dates with validation. Closing the dialog restores focus to its trigger.

Verify dialog keyboard operation, manual input if supported, bounds and calendar-day preservation across relevant time zones.
