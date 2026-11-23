---
name: frontend-loading-performance
description: 'Trigger: lazy loading, carga diferida, code splitting, bundle, chunk, imágenes, módulos o datos bajo demanda. Define fronteras eficientes sin imponer framework.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.0'
---

## Activation Contract

Activa esta skill al crear o revisar carga diferida de código, rutas, assets o datos Web. Carga `../../data/remote-data-behavior/SKILL.md` para datos diferidos y `../../qa/frontend-validation/SKILL.md` durante implementación o cierre. Si React/Next está demostrado y la capacidad existe, carga `~/.agents/skills/vercel-react-best-practices/SKILL.md` para APIs concretas.

## Hard Rules

- Usa lazy loading solo cuando reduce trabajo inicial medible sin retrasar contenido crítico. No fragmentes componentes pequeños, frecuentes o necesarios para la primera interacción.
- Define fronteras por ruta, módulo pesado, integración opcional o interacción explícita; nunca por conveniencia de archivos.
- Toda frontera conserva layout, foco y contexto, y modela carga, error de chunk/recurso, reintento y cancelación cuando aplique.
- Hero, identidad, navegación inicial, CTA principal y datos imprescindibles no se difieren. Assets y contenido bajo el fold pueden diferirse si no degradan descubrimiento o SEO.
- Evita waterfalls: carga en paralelo dependencias conocidas y usa prefetch solo ante intención probable y coste acotado.
- No nombres una API de framework sin evidencia de su instalación. Respeta SSR, hidratación y router existentes.
- Instrumenta región, loading y error con test IDs estables cuando sean observables, sin crear archivos de prueba.

## Decision Gates

| Evidencia | Decisión |
| --- | --- |
| Ruta o módulo pesado y poco frecuente | Divide bajo demanda |
| Componente pequeño o primera interacción | Incluye inicialmente |
| Editor, mapa, gráfico o integración opcional | Carga al solicitar o aproximarse |
| Asset principal above-the-fold | Prioriza; no lazy |
| Tab/panel secundario | Difiere si no es necesario inicialmente |
| Prefetch sin intención o coste desconocido | No precargues |

## Execution

1. Identifica contenido crítico, coste, frecuencia y frontera candidata.
2. Elige la referencia aplicable y declara fallback, error y recuperación.
3. Implementa con la capacidad existente mínima.
4. Verifica red, chunks, layout, foco, consola y viewports mediante validación frontend.
5. Reporta evidencia y cualquier regresión de carga inicial o interacción.

## Output Contract

Reporta frontera, contenido crítico preservado, disparador, fallback/error/reintento, estrategia de prefetch, test IDs, evidencia de red/bundle y validación visual.

## References

- `references/code-splitting.md` — rutas, módulos y chunks.
- `references/assets-and-media.md` — imágenes, video y contenido embebido.
- `references/deferred-data.md` — datos y paneles bajo demanda.
- `references/loading-boundaries.md` — UX, accesibilidad y recuperación.
