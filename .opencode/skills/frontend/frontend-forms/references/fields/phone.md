# Phone field

Use the shared field anatomy/state contract from `../../SKILL.md`. Support a locale/country-aware mask and area/country codes; distinguish international dialing code from local area code. Derive country from explicit product/default selection, not UI language.

Validate the actual number, not mask length. Define formatted display and canonical payload separately. Accept paste, leading zeros, deletion and caret editing; check supported mobile input. Adopt a compatible phone library only when current tooling lacks the capability.

Verify partial/complete numbers, country/area changes, paste and payload normalization.
