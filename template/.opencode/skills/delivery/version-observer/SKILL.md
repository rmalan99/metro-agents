---
name: version-observer
description: 'Trigger: versionado por commit, version.json, versión desplegada, actualización de versión, service worker opcional. Automatiza SemVer patch y observa despliegues sin interrumpir la app.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'franchesca-project'
  version: '1.0'
---

## Activation Contract

Activa esta skill al diseñar, implementar o revisar versionado automático por commit, sincronización de `package.json`/`public/version.json` u observación de versiones desplegadas. Es agnóstica de framework y PWA.

## Hard Rules

- Si modificas el monitor Web, carga `../../qa/testing-behavior/SKILL.md` para sus pruebas y `../../qa/frontend-validation/SKILL.md` para el cierre Web. El versionado por hook o la sincronización de archivos sin cambios al monitor no activa esas skills.
- Carga una capacidad PWA solo si el alcance realmente requiere modificar una PWA existente y el registro ofrece su ruta exacta. Si no existe tal capacidad instalada, no inventes una ruta ni una dependencia.
- Las rutas de `References` son informativas; no añaden dependencias obligatorias.
- En modo versionado/sincronización, incrementa exactamente SemVer `patch` en cada commit mediante hook y sincroniza el valor en `package.json` y `public/version.json`.
- En modo monitor Web, consulta `version.json` sin caché, compara con la versión compilada, notifica una versión nueva y recarga una sola vez.
- Los fallos de red son no bloqueantes: conserva la aplicación operativa y no conviertas el error en bucle de reintentos.
- Evita timers, listeners, notificaciones o recargas duplicados; limpia recursos al desmontar o detener el monitor.
- El service worker es opcional, nunca requisito, y no debe acoplar la solución a una PWA.
- No cambies runtime, configuración PWA ni dependencias fuera del alcance acordado.

## Decision Gates

| Alcance                       | Decisión                                                                                 |
| ----------------------------- | ---------------------------------------------------------------------------------------- |
| Solo hook/sincronización      | Configura SemVer y archivos; no implementes ni pruebes el monitor Web.                   |
| Solo monitor Web              | Implementa y prueba el monitor; no configures ni modifiques el hook.                     |
| Ambos modos                   | Ejecuta ambos caminos y valida su integración sin acoplarlos.                            |
| Existe hook de commits        | Compónlo sin duplicar incrementos; créalo solo cuando el modo de versionado lo requiera. |
| Hay versión remota distinta   | Notifica y programa una única recarga; marca la transición para impedir repeticiones.    |
| Red, respuesta o JSON fallan  | Registra/ignora el fallo y conserva la app; no recargues ni bloquees.                    |
| Se propone service worker     | Trátalo como mejora independiente y opcional; el monitor debe funcionar sin él.          |
| Se modifica una PWA existente | Resuelve una capacidad instalada por su ruta exacta; si no existe, no la inventes.       |

## Execution Steps

1. Clasifica el alcance como `versionado/sincronización`, `monitor Web` o ambos; inspecciona únicamente hooks, scripts, empaquetado y consumidores aplicables.
2. En modo versionado/sincronización, define una única fuente SemVer, sincroniza atómicamente `package.json` y `public/version.json`, y configura el hook para aplicar `patch` sin bucles ni modificaciones ajenas.
3. En modo monitor Web, implementa la consulta con `cache: "no-store"`, la comparación contra la versión compilada y las guardas de ciclo de vida.
4. Valida solo los modos incluidos: prueba sincronización e incremento para versionado; prueba versión nueva/igual, errores, respuesta inválida, desmontaje y ausencia de service worker para el monitor.
5. Si incluye ambos modos, verifica además que el artefacto sincronizado sea compatible con el consumidor Web.

## Output Contract

Reporta el modo aplicado, archivos modificados, fuente/sincronización cuando corresponda, comportamiento del monitor cuando corresponda, decisiones sobre hook/service worker, pruebas ejecutadas y riesgos pendientes.

## References

Consulta la arquitectura, scripts y hooks del proyecto anfitrión antes de modificar cualquier integración.
