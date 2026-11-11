---
name: task-governance
description: 'Trigger: planificar, registrar, ejecutar, bloquear, verificar o cerrar tareas. Gobierna fases, microtareas y el contrato de todo.md.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.0'
---

## Activation Contract

Activa esta skill al planificar, registrar, ejecutar, bloquear, verificar o cerrar tareas. Selecciona el modo correspondiente y aplica el ciclo completo cuando una solicitud atraviese varios modos.

## Hard Rules

- Evalúa y presenta el plan antes de implementar. Divide funcionalidades en microtareas independientes, pequeñas, comprensibles y verificables.
- Declara `Web`, `API` o `Web/API` en cada plan, fase y tarea; usa `Web/API` solo cuando sea inevitable. Nunca mezcles cambios Web/API en una microtarea: sepáralos y explicita dependencias.
- Registra en `todo.md` toda tarea acordada antes de implementarla con `WEB-###`, `API-###` o `TRV-###` y el contrato de la plantilla.
- Mantén cada tarea independiente y no ambigua; no mezcles implementación con refactorización, documentación ni correcciones ajenas.
- Solo el orquestador modifica `todo.md`, verifica evidencia y marca `[x]`. Los subagentes nunca lo modifican.
- Marca `[x]` inmediatamente después de implementar, verificar y cumplir la aceptación; escribir código no basta. Conserva completadas durante el flujo; solo el usuario puede eliminarlas al final.
- No inicies una fase dependiente hasta validar su requisito previo. La asignación o delegación de responsables queda fuera de esta skill y debe regirse por su contrato específico cuando exista.

## Decision Gates

| Modo       | Acción obligatoria                                |
| ---------- | ------------------------------------------------- |
| Planificar | Evalúa contexto y diseña fases verificables       |
| Registrar  | Crea entradas completas antes de implementar      |
| Ejecutar   | Respeta alcance, orden y dependencias             |
| Bloquear   | Conserva `[ ]` y registra causa y evidencia       |
| Verificar  | Contrasta aceptación y validaciones con evidencia |
| Cerrar     | Marca `[x]`, conserva la entrada y no la elimines |

## Execution Steps

1. Sigue la evaluación y construcción de fases de `references/task-lifecycle.md`.
2. Separa ámbitos y resultados observables; revisa elementos reutilizables.
3. Registra cada microtarea con `assets/todo-entry.template.md`.
4. Ejecuta solo cuando sus dependencias estén validadas.
5. Aplica estados, bloqueos y evidencia según el ciclo de vida.
6. Aplica `references/closure-gates.md`; marca o conserva pendiente inmediatamente según el resultado.

## Output Contract

Devuelve modo, ámbito, fases, tareas con identificadores, dependencias, estado, evidencia y validaciones. Declara bloqueos y criterios pendientes. Confirma que solo el orquestador modificó `todo.md` y que ninguna completada fue eliminada sin autorización final del usuario.

## References

- `assets/todo-entry.template.md` — plantilla obligatoria de entradas.
- `references/task-lifecycle.md` — evaluación, fases, granularidad, ámbitos y estados.
- `references/closure-gates.md` — verificación, marcado, conservación y eliminación.
