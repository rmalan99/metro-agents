# shadcn/ui integration for React

Load for project-owned UI generation, tokens, variants or primitive behavior. Inspect actual generated code and configuration; shadcn installations can differ by generation date, registry, styling version and primitive library.

## Discovery
Read `components.json` when present: aliases, component location, style, base color, CSS variables and relevant server-component settings. Inspect shared utilities such as `cn`, the Button source, global CSS and lockfile. Determine which primitives implement dialogs/menus; do not assume every installation uses the same primitive library.

## Setup sequence
1. Verify the React framework, aliases and Tailwind integration.
2. Reuse existing generated components. Do not rerun initialization over an established configuration.
3. For a new setup, use the official initializer matching the framework; review generated file paths and dependencies.
4. Add only required components. Inspect changes before accepting overwrites to existing code.
5. Put semantic theme values in the existing global token source and check mappings to utility classes.
6. Verify one form control and one overlay before extending the application.

## Theme representation
Inspect how variables are consumed before editing values. Some setups use HSL channels and `hsl(var(...))`; newer templates may use complete color values such as OKLCH and different mapping syntax. Do not paste one representation into the other.

Use semantic pairs for background/foreground, card/card-foreground, primary/primary-foreground, muted/muted-foreground, border, input and ring as present in the project. Add navigation tokens only when there is a distinct shared role. Update every supported mode coherently; a new mode is not implied by a dark sidebar.

## Component extension
Generated components are owned source. For repeated style changes, modify their shared implementation/variant rather than overriding every call site. Preserve public props and primitive behavior when adjusting markup.

Example call-site composition when those variants exist in the local Button:

```tsx
<Button variant="destructive" onClick={requestDelete}>
  Delete record
</Button>
<Button variant="outline" asChild>
  <a href={detailUrl}>View details</a>
</Button>
```

Check `asChild` or alternative composition support in the local implementation first. Its child must accept the forwarded props/ref required by the primitive; do not nest an interactive element inside another interactive element. Confirmation and actual deletion are separate behaviors.

If adding a reusable variant, update the component's variant definition and inferred typing together. Do not globally change the primary button to solve one destructive action.

## Updating and troubleshooting
| Symptom | Inspect | Fix |
|---|---|---|
| Tokens do not affect controls | Variable representation and utility mapping | Shared CSS/theme mapping |
| Classes unexpectedly lose | `cn` merge behavior and conflicting utilities | Variant/composition |
| Dialog/menu loses keyboard behavior | Primitive markup, forwarded props/ref, trigger composition | Shared component |
| Generator overwrote customization | Actual diff against prior source | Reconcile generated changes |
| Alias import fails | Generator aliases and framework/compiler resolution | Consistent alias configuration |

Treat updates as code changes: compare upstream patterns with local modifications and merge deliberately. Check keyboard interaction, close/focus return, tokens in overlays and existing component consumers. Do not claim upstream updates automatically propagate to project-owned components.
