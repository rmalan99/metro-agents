---
name: task-governance
description: 'Trigger: planificar, registrar, ejecutar, bloquear, verificar o cerrar tareas. Gobierna fases, microtareas y el contrato de todo.md.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.2'
---

## Activation Contract

Activa esta skill al planificar, registrar, ejecutar, bloquear, verificar o cerrar tareas. Selecciona el modo correspondiente y aplica el ciclo completo cuando una solicitud atraviese varios modos.

## Hard Rules

- Evalúa y presenta el plan antes de implementar. Divide funcionalidades en microtareas independientes, pequeñas, comprensibles y verificables.
- Declara `Web`, `API` o `Web/API` en cada plan, fase y tarea; usa `Web/API` solo cuando sea inevitable. Nunca mezcles cambios Web/API en una microtarea: sepáralos y explicita dependencias.
- Registra en `todo.md` toda tarea acordada antes de implementarla con `WEB-###`, `API-###` o `TRV-###` y el contrato de la plantilla.
- Con orquestación activa, ninguna herramienta mutante se usa hasta que la tarea esté registrada y en estado `ejecutando`; usa `governance_task_register` y `governance_task_status` y no evadas el gate mediante shell. En modo directo, el agente primario registra y mantiene el estado con las herramientas de edición disponibles antes de implementar.
- Mantén cada tarea independiente y no ambigua; no mezcles implementación con refactorización, documentación ni correcciones ajenas.
- Registra en `todo.md` unidades de trabajo verificables, no cada actividad técnica. Las actividades atómicas viven en la orden del Executor y se promueven a tarea solo si pueden aceptarse independientemente.
- Solo el agente primario responsable modifica `todo.md`, verifica evidencia y marca `[x]`: es el Manager con orquestación activa y el agente directo cuando está desactivada. Los subagentes nunca lo modifican.
- Marca `[x]` inmediatamente después de implementar, verificar y cumplir la aceptación; escribir código no basta. Conserva completadas durante el flujo; solo el usuario puede eliminarlas al final.
- No inicies una fase dependiente hasta validar su requisito previo. La asignación o delegación de responsables queda fuera de esta skill y debe regirse por su contrato específico cuando exista.
- Respeta las transiciones declaradas por el gate: no saltes fases ni cierres una tarea sin la evidencia y el PASS requeridos.

## Decision Gates

| Modo       | Acción obligatoria                                |
| ---------- | ------------------------------------------------- |
| Planificar | Evalúa contexto y diseña fases verificables       |
| Registrar  | Crea entrada `preparada` antes de implementar     |
| Ejecutar   | Mueve a `ejecutando`; respeta alcance y dependencias |
| Bloquear   | Conserva `[ ]` y registra causa y evidencia       |
| Verificar  | Mueve a `verificando` y contrasta evidencia       |
| Cerrar     | Mueve a `completada`, marca `[x]` y conserva      |

## Execution Steps

1. Sigue la evaluación y construcción de fases de `references/task-lifecycle.md`.
2. Separa ámbitos y resultados observables; revisa elementos reutilizables.
3. Registra cada microtarea con `assets/todo-entry.template.md`.
4. Ejecuta solo cuando sus dependencias estén validadas.
5. Aplica estados, bloqueos y evidencia según el ciclo de vida.
6. Aplica `references/closure-gates.md`; marca o conserva pendiente inmediatamente según el resultado.

## Output Contract

Devuelve modo de ejecución, ámbito, fases, tareas con identificadores, dependencias, estado, evidencia y validaciones. Declara bloqueos y criterios pendientes. Confirma que solo el agente primario responsable modificó `todo.md` y que ninguna completada fue eliminada sin autorización final del usuario.

## References

- `assets/todo-entry.template.md` — plantilla obligatoria de entradas.
- `references/task-lifecycle.md` — evaluación, fases, granularidad, ámbitos y estados.
- `references/closure-gates.md` — verificación, marcado, conservación y eliminación.
