# Frontend contract

Use existing documentation instead if it already owns these decisions. Replace placeholders with observed facts; mark unresolved decisions explicitly. Keep this file brief and update only changed responsibilities.

## Technical base
- Tool/framework and version: <observed>
- UI system and version: <selected/adopted>
- Styling and rendering model: <observed>
- Existing constraints: <requirements>

## Locations and boundaries
- Entry/navigation: <path and responsibility>
- Layouts/features: <paths and dependency direction>
- Shared components: <path; when to extend or extract>
- Data access and validation: <paths and rules>

## Shared visual system
- Product surface, platform, composition and density: <observed/selected>
- Visual profile and version: <profile or existing system>
- Adoption mode: <preserve/adopt>
- Theme/token source: <actual path>
- Profile-to-project token mappings: <semantic role to native token/API>
- Semantic tokens and modes: <names/roles>
- Component defaults/variants: <actual paths>
- Density, spacing and responsive conventions: <decisions>
- How to add a shared style: <native mechanism and owner>
- Visual exceptions and missing extensions: <bounded gaps, owners and scope>

## Behavior
- State ownership and URL conventions: <rules>
- Loading/empty/error/form feedback: <shared patterns; ModalAlert location/owner and operation-result mapping>
- Form fields/adapters: <base, variants, form-tool binding locations>
- Reactive validation: <dirty/touched exposure, debounce/async rules>
- Backend field errors and reveal/focus: <mapping and mechanism>
- Canonical phone/mask/date values and option search threshold: <contracts>
- Accessibility and focus patterns: <rules>
- Authentication/permission boundary, if relevant: <contract>

## Test-identifier contract
- Attribute: data-testid (or explicit mapping to existing runner configuration)
- Naming and instance scopes: <stable convention>
- Repeated-record selectors and portal scopes: <patterns>
- Shared component forwarding: <locations/mechanism>
- Known library/legacy exceptions: <bounded gaps and reasons>
- Selector changes: <consumers/migration if relevant>

## Specialized guidance
- Active tool skill: <existing skill>
- UI references needed for current stack: <references>
- Product skills, loaded only as needed: <skills>

## Verification
- Required commands and working directory: <actual commands>
- Behavioral/visual checks: <scope>
- Known limitations: <facts, or none observed>
