# chakra — shared form contract integration

Read only when this UI system is adopted and form work requires its integration details. Apply `../../SKILL.md`; consult the tool-specific UI setup guide separately when needed.

Apply `frontend-forms` with the installed major's field composition. In v2 inspect FormControl/label/helper/error APIs; in v3 inspect compound Field/recipe APIs. Do not mix their prop names. Bind required/invalid metadata and consistent danger treatment to the whole field anatomy.

Use supported input grouping/adornments for icons and mandatory password visibility. For up to 10 options use an accessible custom popup select compatible with the installed major; a NativeSelect is not the default custom-popup contract. Above 10 options use searchable combobox capability available in that version or a justified compatible primitive.

Map actual input/trigger refs for failed-submit focus. Choose the installed-version dialog/calendar capability for date selection and assess phone/mask integration when missing. Generic base fields consume backend/form state; feature adapters own remote requests and error-path parsing.
