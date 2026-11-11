---
name: component-composition
description: 'Trigger: composición de componentes, base, composed, specialized, variantes o diseño por capas. Define decisiones agnósticas de framework para reutilizar y especializar componentes.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '2.1'
---

## Activation Contract

Activa esta skill al diseñar, implementar o revisar jerarquías de UI, componentes reutilizables, composiciones, wrappers, layouts, páginas, variantes o especializaciones, sin asumir un framework concreto. Es la única autoridad para `base`/`composed`/`specialized`/`layouts`/`pages`, composición, variantes y jerarquía.

No tiene dependencias obligatorias. Consulta `../frontend-module-architecture/SKILL.md` solo si debes decidir o cambiar ubicación física; la referencia a convenciones del proyecto es informativa y no activa otra skill.

## Hard Rules

- Clasifica cada pieza como `base`, `composed`, `specialized`, `layouts` o `pages` antes de implementarla.
- `base` define una capacidad mínima y estable; no incorpora reglas de una pantalla o dominio.
- `composed` combina bases existentes y coordina comportamiento; no duplica su markup ni contratos.
- `specialized` resuelve un caso concreto componiendo capas inferiores; no convierte reglas locales en base global.
- `layouts` compone navegación y regiones compartidas entre pantallas; no contiene reglas exclusivas de una página.
- `pages` orquesta datos, estados y composición de una ruta o pantalla; no duplica responsabilidades inferiores.
- Decide aquí la capa y la jerarquía. La arquitectura modular decide después la ubicación física; ninguna decisión de ubicación redefine la capa ni exige cargar una skill arquitectónica para clasificarla.
- Prefiere composición sobre duplicación, herencia, flags booleanos acumulativos o variantes implícitas.
- Mantén una única responsabilidad, API explícita y estados observables; no introduzcas una abstracción sin consumidor real.
- Toda pieza implementada que represente pantalla, sección funcional o componente relevante expone un identificador estable según `../frontend-ui-quality/references/testability-identifiers.md`; no instrumentes wrappers incidentales.
- No cambies la responsabilidad de una capa para evitar una decisión de diseño; registra el impacto y los consumidores.
- Sigue esta jerarquía sin saltos: componente propio existente → adaptación/composición propia en el alcance mínimo → primitiva directa de la librería visual → componente nuevo.
- Antes de usar una librería visual directamente, documenta por qué ningún componente propio resuelve el caso. Antes de crear uno nuevo, documenta además por qué tampoco sirven composición o primitivas directas.
- Crea un componente genérico de forma autónoma solo con consumidores reales en más de un módulo, un patrón existente y el cambio mínimo seguro; no generalices un caso exclusivo. Escala únicamente si introduce una API global nueva o una decisión arquitectónica sin precedente seguro.

## Decision Gates

| Condición                                         | Decisión                                                       |
| ------------------------------------------------- | -------------------------------------------------------------- |
| Existe un componente con la misma responsabilidad | Reutilízalo o compónlo; no crees otro equivalente.             |
| Solo cambia presentación o configuración          | Usa una variante explícita mediante props, tema o composición. |
| Cambia comportamiento y reglas del caso           | Crea `specialized` sobre una base o `composed` existente.      |
| Comparte estructura entre páginas                 | Usa `layouts`; mantén fuera las reglas exclusivas de ruta.     |
| Orquesta una ruta o pantalla                      | Usa `pages`; delega UI y comportamiento a capas inferiores.    |
| Se necesitan muchos flags o excepciones           | Divide responsabilidades y revisa la frontera entre capas.     |
| No hay consumidor concreto                        | No crees la abstracción todavía.                               |
| Existe alternativa propia adaptable               | Adáptala; no la eludas con JSX o librería directa.             |
| Debes decidir o cambiar ubicación física          | Carga `../frontend-module-architecture/SKILL.md`.              |

## Execution Steps

1. Inspecciona componentes, contratos, consumidores y estados existentes; registra alternativas descartadas.
2. Define responsabilidad, capa y API pública con `references/layer-classification.md`.
3. Elige reutilización, composición o nueva pieza según los decision gates.
4. Implementa variantes explícitas sin duplicar estructura ni reglas, y añade los identificadores de testabilidad aplicables.
5. Verifica estados, accesibilidad, consumidores y ausencia de regresiones.

## Output Contract

Reporta clasificación de cada pieza, decisiones de composición y variantes, archivos afectados, consumidores verificados, validaciones ejecutadas y riesgos pendientes.

## References

- `references/layer-classification.md` — criterios y escenarios verificables de capas, jerarquía y variantes.
- `../frontend-ui-quality/references/testability-identifiers.md` — contrato de test IDs estables; no autoriza crear pruebas.
- Convenciones locales del proyecto anfitrión — referencia informativa para ubicación, nombres y APIs; no es una dependencia.
