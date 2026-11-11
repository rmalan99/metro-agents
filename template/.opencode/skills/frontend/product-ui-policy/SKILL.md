---
name: product-ui-policy
description: 'Trigger: identidad visual, nueva pantalla, shell, navegación, densidad o jerarquía UI. Preserva y extiende las decisiones visuales del producto.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.0'
---

## Activation Contract

Activa esta skill al diseñar, implementar o revisar identidad, shell, navegación, jerarquía, densidad o una pantalla Web nueva. Carga obligatoriamente `../frontend-ui-quality/SKILL.md` y `../component-composition/SKILL.md`. `../../governance/implementation-decision-policy/SKILL.md` es informativa aquí: solo se activa por su propio contrato ante una decisión técnica no especificada.

## Hard Rules

- Trata como fuentes de verdad, en orden: producto renderizado y aprobado; shell, layouts y navegación vigentes; tokens globales y assets de marca; componentes compartidos y catálogos; patrones repetidos en pantallas reales. Una ocurrencia aislada no crea política.
- Conserva lenguaje visual, estructura y comportamiento reconocibles. No inventes marca, paleta, tipografía, iconografía, decoración ni paradigma de navegación.
- Usa semántica de producto y capacidades existentes; no expreses la política mediante APIs o nombres de Tailwind, Radix, MUI u otra librería.
- Mantén una jerarquía sobria: contexto y título primero, contenido primario después, acciones secundarias y metadatos al final. Usa énfasis con moderación y una acción primaria clara cuando exista.
- Mantén densidad media por defecto; aumenta densidad solo en superficies operativas o comparativas con evidencia, y redúcela solo cuando lectura, orientación o tarea enfocada lo requieran.
- Preserva el shell del ámbito: navegación persistente y regiones estables en escritorio; adaptación móvil del mismo mapa de información, sin crear destinos ni jerarquías paralelas.
- Delega spacing, responsive, accesibilidad, estados, foco e interacción a `frontend-ui-quality`; no los redefinas aquí. Delega capas y reutilización a `component-composition`.

## Decision Gates

| Condición                                                                   | Decisión                                                                            |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Patrón vigente equivalente                                                  | Reutilízalo sin reinterpretar la identidad                                          |
| Pantalla nueva sin precedente directo                                       | Extiende el shell y la jerarquía predominantes con tokens y componentes vigentes    |
| Evidencia inconsistente                                                     | Prefiere el patrón repetido y el cambio mínimo reversible; registra la discrepancia |
| Cambia marca, navegación global, densidad del ámbito o prioridad de negocio | Detente y solicita decisión de producto                                             |
| Requiere un componente o patrón nuevo                                       | Aplica `component-composition` antes de proponerlo                                  |

## Execution Steps

1. Inspecciona fuentes de verdad y separa patrón repetido de excepción local.
2. Declara ámbito, shell, jerarquía, densidad y precedentes que conservarás.
3. Aplica el default más cercano sin introducir identidad nueva.
4. Verifica consistencia contra pantallas vecinas y activa `frontend-ui-quality` para sus garantías.
5. Escala con evidencia, alternativas acotadas e impacto cuando un gate de producto se active.

## Output Contract

Reporta fuentes inspeccionadas, patrón preservado, defaults aplicados, decisiones de shell/jerarquía/densidad, skills delegadas y cualquier escalamiento o inconsistencia pendiente.

## References

- `../frontend-ui-quality/SKILL.md` — autoridad de calidad visual e interactiva.
- `../component-composition/SKILL.md` — autoridad de capas, reutilización y componentes.
- `../../governance/implementation-decision-policy/SKILL.md` — referencia informativa; se carga solo por su propio trigger.
