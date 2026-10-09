# MUI integration for React

Load only for MUI setup, theming, component extension or integration failures. Inspect the installed major and framework first; exact SSR adapters and styling-engine APIs must match those versions.

## Discovery
Inspect `@mui/material`, its styling-engine dependencies, existing theme/provider, global reset and any `@mui/x-*` packages. Material UI and MUI X are distinct; do not assume advanced grid functionality or licensing is included in Material UI.

Locate theme overrides, existing wrappers, portal usage and SSR style integration. If the app uses a custom engine, do not install Emotion merely because it is the default in a new setup.

## Setup sequence
1. Preserve the current engine and dependency versions. For a new setup, use the installed-version official installation instructions and assess only required packages.
2. Put the theme in the existing global configuration location and establish one intended provider boundary. Add narrower providers only for a real scoped theme.
3. Configure baseline styles only once; inspect existing resets before applying `CssBaseline`.
4. In SSR, use the official adapter for the actual React framework/router and version. Validate style insertion order, hydration and theme availability rather than copying a generic cache recipe.
5. Check a control and a portal overlay before proceeding with screens.

## Theme and component ownership
Map shared roles to `palette`, `typography`, `spacing`, `shape` and component configuration where supported. Use defaults for universal props, `styleOverrides` for shared component styling and variants for intentional reusable treatments supported by the installed API. Keep `sx` for local composition and one-off adjustments.

Example using common Material UI theme APIs; adapt values to the agreed design and inspect version compatibility:

```tsx
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Button from '@mui/material/Button';

const theme = createTheme({
  palette: { primary: { main: '#3347B0' } },
  shape: { borderRadius: 8 },
  components: {
    MuiButton: {
      defaultProps: { disableElevation: true },
      styleOverrides: { root: { textTransform: 'none' } },
    },
  },
});

export function SaveAction() {
  return <ThemeProvider theme={theme}>
    <Button variant="contained">Save</Button>
  </ThemeProvider>;
}
```

In an application, place the provider at its intended shared boundary, not around each button. Do not repeat the text-transform fix on every instance. For custom token types, extend the installed theme typings; do not cast away errors.

## Components and overlays
Use public slot/prop APIs from the installed version. Avoid selectors bound to generated class hashes or private DOM structures. Preserve labels, helper text, dialog focus and menu behavior. Do not replace a native link destination with an unrelated click handler.

For async submission, coordinate loading/disabled behavior with the form's actual mutation state. Use loading APIs available in the installed version; do not assume an API shown in a newer example exists.

## Diagnose before patching
| Symptom | Inspect | Correct at |
|---|---|---|
| Theme ignored | Provider boundary/import, nested overrides | Theme integration |
| Server/client style mismatch | Framework adapter, cache/insertion order, nondeterministic initial mode | SSR setup |
| Every button needs same `sx` | Component defaults/overrides | Shared component theme |
| Overlay differs from page | Provider boundary, portal styling, CSS selectors | Theme/overlay integration |
| Advanced grid feature missing | MUI X package, version, tier/license | Capability decision |

Verify affected states, keyboard focus, portal inheritance and representative narrow layouts. Inspect other consumers after changing global overrides. Record theme location and version-specific adapter in the frontend contract.
