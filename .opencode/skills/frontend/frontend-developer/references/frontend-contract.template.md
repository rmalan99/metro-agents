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
- Theme/token source: <actual path>
- Semantic tokens and modes: <names/roles>
- Component defaults/variants: <actual paths>
- Density, spacing and responsive conventions: <decisions>
- How to add a shared style: <native mechanism and owner>

## Behavior
- State ownership and URL conventions: <rules>
- Loading/empty/error/form feedback: <shared patterns>
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
