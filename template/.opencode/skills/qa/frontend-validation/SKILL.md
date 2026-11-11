---
name: frontend-validation
description: 'Trigger: validar frontend, cerrar tarea Web, lint, typecheck, test, build. Ejecuta la validación escalonada y el gate final de una entrega Web.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.1'
---

## Activation Contract

Activa esta skill durante la implementación y antes de cerrar toda tarea Web. Para cambios UI renderizables, carga `~/.agents/skills/playwright-cli/SKILL.md` y valida el resultado funcional y visual en navegador cuando el entorno esté disponible.

Deriva verificaciones de las skills funcionales ya activadas. La capacidad global de Playwright es condicional a UI renderizable; no autoriza crear tests persistentes.

## Hard Rules

- Valida primero el resultado observable más pequeño y amplía la batería según el alcance.
- Una ejecución previa solo conserva validez si no hubo cambios relevantes después.
- El cierre completo ejecuta los scripts existentes y aplicables de lint, typecheck, pruebas y build, más `git diff --check`; no inventes comandos ni crees pruebas para completar la batería.
- Ejecuta build especialmente ante cambios de rutas, configuración, dependencias, bundle o compilación.
- Un componente compartido no cierra sin catálogo e instrumentación de testabilidad; pruebas nuevas requieren solicitud explícita. Una API eliminada no cierra mientras existan consumidores.
- Todo cambio UI renderizable exige recorrido funcional y revisión visual contra la tarea mediante Playwright cuando servidor, datos y credenciales estén disponibles. Comprueba viewport aplicable, estados, consola y requests relevantes; captura evidencia cuando aporte valor.
- Si falta entorno ejecutable, reporta el bloqueo y la validación no realizada. No sustituyas evidencia visual con una afirmación ni crees snapshots/baselines sin autorización.
- No ocultes fallos ajenos ni los corrijas fuera de alcance: registra comando, salida y relación con el cambio.
- Reporta únicamente comandos realmente ejecutados y distingue éxito, fallo y validación no disponible.

## Decision Gates

| Momento            | Validación mínima                                                     |
| ------------------ | --------------------------------------------------------------------- |
| Iteración          | Prueba/verificación específica, lint/typecheck enfocados y diff check |
| Componente o flujo | Verificación enfocada, lint y typecheck; tests existentes aplicables  |
| UI renderizable    | Playwright funcional + revisión visual contra aceptación              |
| Tarea o fase       | Batería completa y requisitos de skills activadas                     |
| Cambio posterior   | Repite las validaciones afectadas                                     |

## Execution Steps

1. Deriva la matriz de validación desde aceptación, archivos y skills activadas.
2. Ejecuta verificaciones enfocadas durante la implementación.
3. Si hay UI renderizable, usa Playwright para recorrer el flujo afectado y comparar el resultado visual con aceptación, sin crear tests.
4. Ejecuta pruebas existentes aplicables; crea nuevas solo ante solicitud explícita.
5. Ejecuta el gate completo al cierre y revisa diff, consumidores, catálogo, accesibilidad y regresiones.

## Output Contract

Reporta matriz, comandos, resultados, recorrido funcional, evidencia visual, viewports, consola/requests relevantes, pruebas existentes, fallos ajenos y validaciones pendientes. Declara explícitamente si no se crearon tests por falta de solicitud.

## References

- `references/closure-checklist.md` — checklist de cierre según el tipo de cambio.
- `~/.agents/skills/playwright-cli/SKILL.md` — capacidad global para validación funcional y visual en navegador.
