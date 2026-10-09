# mui — shared form contract integration

Inherits `../../SKILL.md`; this reference supplies the selected UI binding only.

Apply the shared `frontend-forms` behavior through the installed MUI controls. For text fields, bind label, required, placeholder, error state and helper/error content using supported props; keep helpful instructions when an error appears. Default invalid label/border/message treatment belongs in the component theme.

Use supported adornment/slot APIs for leading icons and the mandatory password visibility button. Bind refs to the actual input. Map select mode to the MUI custom popup and searchable mode to Autocomplete with stable option identity and intentional value/inputValue mapping. Do not make search text the selected backend value.

If date/phone/mask capabilities are absent, evaluate an appropriate compatible package rather than importing an unrelated UI library. Date pickers must expose the requested accessible date-selection dialog behavior. Check MUI X package/version/tier for any chosen picker features. Connect form-library state through a thin adapter and verify error IDs, focus targets and portal scope in rendered DOM.
