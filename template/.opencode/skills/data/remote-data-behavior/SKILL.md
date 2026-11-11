---
name: remote-data-behavior
description: 'Trigger: datos remotos, cache, consulta, mutación, paginación, filtros o concurrencia Web. Gobierna comportamiento remoto sin imponer librerías.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.1'
---

## Activation Contract

Activa esta skill al crear o revisar lectura, cache, mutación o sincronización de datos remotos en Web. Aplícala sin depender de React Query, SWR ni otra librería.

No tiene dependencias obligatorias. Carga `../../backend/web-api-contract-workflow/SKILL.md` solo si creas, cambias o coordinas un contrato Web/API; carga `../../frontend/frontend-module-architecture/SKILL.md` solo si decides ubicación, propiedad modular o fronteras físicas.

## Hard Rules

- Asigna cada dato remoto a una única feature propietaria; comparte acceso mediante su contrato público y no dupliques caches ni estado servidor en estado local.
- Deriva una identidad estable de operación, parámetros normalizados, filtros, orden, página y contexto de autorización. Identidades distintas no comparten entradas; entradas equivalentes no se fragmentan.
- Define frescura, retención y revalidación según volatilidad y coste. Tras mutar, actualiza o invalida todas y solo las vistas afectadas, incluidas listas, detalle y agregados.
- Delega filtrado, búsqueda, orden y paginación remotos al servidor. Conserva página previa solo si no presenta resultados como actuales; reinicia o valida el cursor cuando cambie la consulta.
- Propaga cancelación cuando sea posible e ignora respuestas obsoletas. La última intención vigente gobierna; evita escrituras tardías después de desmontaje, cambio de identidad o cancelación.
- Modela carga inicial, refresco, vacío, éxito parcial y error como estados distinguibles. Preserva datos válidos durante refrescos cuando no induzca engaño y ofrece recuperación accionable.
- Toda operación iniciada por formulario, listado o evento expone progreso perceptible mientras está pendiente. Distingue carga inicial bloqueante, refresco con datos válidos y mutación localizada; no reemplaces contenido útil con un loader global durante un refresco.
- Evita solicitudes duplicadas por identidad de operación: mientras una mutación no conmutativa esté pendiente, deshabilita o ignora su activador equivalente. Deduplica consultas equivalentes, pero no bloquees operaciones independientes ni toda la interfaz sin una dependencia real.
- En búsqueda, filtros, orden y paginación, agrupa cambios rápidos cuando corresponda y cancela o descarta trabajo obsoleto. No solicites repetidamente la misma página o intención pendiente; la última intención válida gobierna.
- Libera siempre el estado pendiente al completar, fallar o cancelar. Un error conserva entradas recuperables, comunica una acción útil y permite reintentar sin dejar controles bloqueados.
- Usa actualización optimista solo si existe snapshot suficiente, rollback determinista y reconciliación con la respuesta autoritativa; en otro caso espera confirmación.
- Mantén `requests` para transporte, serialización y cancelación; `services` para operaciones y reglas de acceso remoto; `hooks` para ciclo de vida, cache y estado consumible. No pongas reglas de UI en requests/services ni transporte directo en componentes.
- No inventes ni redefinas contratos Web/API. Al crear, cambiar o coordinar uno, carga `../../backend/web-api-contract-workflow/SKILL.md` como su autoridad; al consumir un contrato estable existente, respétalo sin cargar esa skill. Carga `../../frontend/frontend-module-architecture/SKILL.md` solo al decidir ubicación o fronteras.

## Decision Gates

| Situación                               | Decisión                                         |
| --------------------------------------- | ------------------------------------------------ |
| Mutación identifica efectos completos   | Actualiza exactamente o invalida selectivamente  |
| Efectos inciertos o agregados derivados | Invalida y revalida desde autoridad remota       |
| Escrituras concurrentes no conmutativas | Serializa o exige control de versión             |
| Rollback incompleto o efectos externos  | No optimista                                     |
| Consulta cambia durante una solicitud   | Cancela o descarta la respuesta obsoleta         |
| Submit equivalente mientras está pendiente | Ignora o deshabilita el activador duplicado    |
| Consulta equivalente ya pendiente       | Reutiliza o deduplica la operación                |
| Búsqueda o filtro cambia rápidamente    | Agrupa cambios y conserva la última intención     |
| Refresco conserva datos válidos         | Mantén contenido e indica progreso no bloqueante  |
| Crea/cambia/coordina contrato Web/API   | Carga `../../backend/web-api-contract-workflow/SKILL.md`    |
| Decide ubicación o frontera modular     | Carga `../../frontend/frontend-module-architecture/SKILL.md` |

## Execution Steps

1. Identifica propietario, consumidores, contrato aprobado y fuente autoritativa.
2. Define identidad, política de frescura, estados de carga y frontera request/service/hook.
3. Define paginación/filtros, deduplicación, controles afectados, concurrencia, cancelación e impacto de mutaciones.
4. Implementa la opción mínima compatible con la librería existente, sin exponerla como contrato de dominio.
5. Verifica los escenarios de `references/scenarios.md` y las vistas relacionadas.

## Output Contract

Reporta propietario, identidad, política de cache, invalidaciones, estrategia de deduplicación/concurrencia/cancelación, representación de progreso, controles afectados, estados, fronteras y escenarios verificados. Declara si hubo optimismo y demuestra rollback; enlaza el contrato Web/API sin duplicarlo.

## References

- `references/scenarios.md` — escenarios mínimos de verificación conductual.
- `../../backend/web-api-contract-workflow/SKILL.md` — autoridad del contrato Web/API.
- `../../frontend/frontend-module-architecture/SKILL.md` — autoridad de ubicación y dependencias frontend.
