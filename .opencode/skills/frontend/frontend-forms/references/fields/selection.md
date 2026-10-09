# Select and combobox

Use the shared field anatomy/state contract from `../../SKILL.md`.

- Up to 10 total options: select with a custom accessible popup from the adopted UI system.
- More than 10: searchable combobox with internal filtering.
- Remote/unknown totals or text-location tasks: prefer a searchable combobox even if the current page contains fewer items.

Select and combobox share visual tokens but have distinct accessible interaction patterns. Use supported primitives for keyboard navigation, active option and Escape. Search text is separate from the selected stable value; unknown text is not a valid option unless explicitly allowed.

For remote sources define loading/empty/error state, debounce search, prevent stale-result replacement, retain selected labels and follow actual paging/query contracts. A page of 10 does not establish the total size.

Verify the 10/11 boundary, keyboard selection/close, no matches, retained selection and outdated remote results.
