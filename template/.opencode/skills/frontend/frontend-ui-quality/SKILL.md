---
name: frontend-ui-quality
description: 'Trigger: UI, UX, accesibilidad, responsive, spacing, estados visuales, filtros o iconos. Aplica la calidad visual e interactiva normativa del frontend.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.2'
---

## Activation Contract

Activa esta skill para cualquier cambio visual o interactivo Web. Carga obligatoriamente `../component-composition/SKILL.md`. Carga condicionalmente `../frontend-base-components/SKILL.md` cuando el componente sea compartido y `../../qa/frontend-validation/SKILL.md` durante implementación o cierre.

## Hard Rules

- Usa tokens del tema y la escala `0, 4, 8, 16, 24, 32, 40, 48, 64`; justifica cualquier excepción.
- El layout controla separación externa; el componente controla su espacio interno. Prefiere `gap`, stack o grid frente a márgenes dispersos.
- Define nombres accesibles, relaciones label/descripción/error, foco visible, orden lógico y operación completa por teclado.
- Implementa los estados aplicables: loading, success, empty, error, disabled, sin permisos y no disponible. El color nunca es el único indicador.
- Toda acción remota ofrece feedback de progreso cercano a su origen: conserva una etiqueta comprensible, usa indicador visual y comunica el estado mediante texto accesible o `aria-busy` cuando aplique. Un spinner sin contexto no es suficiente.
- Mientras una acción equivalente esté pendiente, evita activaciones repetidas deshabilitando o ignorando solo los controles afectados. No bloquees navegación, lectura ni acciones independientes; durante refrescos conserva contenido válido con un indicador no bloqueante.
- Verifica móvil y escritorio sin cortes ni scroll horizontal; respeta `prefers-reduced-motion`.
- Usa exclusivamente `@tabler/icons-react` para iconos de interfaz. No uses SVG manual, Unicode, emojis u otras librerías; marca iconos decorativos y nombra los interactivos.
- Las acciones irreversibles requieren distinción visual y confirmación. Formularios conservan datos cuando sea posible y muestran el error junto al control.
- Toda pantalla, sección funcional y componente relevante implementado expone identificadores estables según `references/testability-identifiers.md`. Instrumentar testabilidad no implica crear pruebas.

## Decision Gates

| Cambio                | Obligación                              |
| --------------------- | --------------------------------------- |
| Control interactivo   | Teclado, foco y estados                 |
| Menú o diálogo        | Foco contenido/restaurado y Escape      |
| Componente compartido | Catálogo, estados e identificadores     |
| Pantalla/sección/componente | Test IDs estables sin instrumentar cada nodo |
| Listado con filtros   | Patrón responsive de la referencia      |
| Acción remota pendiente | Progreso accesible y bloqueo localizado |
| Refresco con datos válidos | Conserva contenido; indica actualización |
| Animación             | Funcional, breve y reducible            |
| Implementación/cierre | Carga `../../qa/frontend-validation/SKILL.md` |

## Execution Steps

1. Inventaría tokens, componentes y patrones existentes.
2. Define estados, progreso remoto, controles afectados, accesibilidad, responsive e interacción antes del estilo.
3. Implementa con el componente y alcance mínimos, incluidos los identificadores de testabilidad aplicables.
4. Verifica teclado, foco, contraste, tamaños táctiles y viewports relevantes.
5. Ejecuta la skill de validación Web antes de cerrar.

## Output Contract

Reporta skills aplicadas, tokens, estados, progreso remoto, alcance del bloqueo, accesibilidad, responsive, iconos, catálogo/pruebas y riesgos pendientes.

## References

- `references/quality-rules.md` — reglas detalladas de interacción, accesibilidad y responsive.
- `references/listing-filters.md` — patrón obligatorio de filtros responsive.
- `references/testability-identifiers.md` — contrato de test IDs estables.
- `../component-composition/SKILL.md` — selección y composición de componentes.
- `../frontend-base-components/SKILL.md` — requisitos de componentes compartidos.
- `../../qa/frontend-validation/SKILL.md` — gate de cierre para cambios Web.
