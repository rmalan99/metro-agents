# Flujo jerárquico

1. Manager redacta Work Brief; ninguna ejecución comienza sin aprobación explícita registrada.
2. Planner `delivery-map` crea fases y unidades verificables; Manager valida y registra solo esas unidades en `todo.md`.
3. Cuando una unidad queda preparada, Planner `work-unit-detail` genera sus actividades atómicas just-in-time sin cambiar alcance.
4. Manager elige el perfil mínimo suficiente y lanza unidades independientes dentro del límite.
5. Executor completa las actividades de una unidad y reporta; nunca crea tareas, cierra ni corrige fuera de alcance.
6. Validator independiente evalúa la unidad completa y emite PASS, FAIL o BLOCKED.
7. PASS permite cerrar y preparar la siguiente unidad. Primer FAIL produce una corrección acotada dentro de la misma unidad. Segundo FAIL bloquea y escala al usuario.

Planner y Validator son read-only. Solo Manager cambia gobierno. Todo subagente usa un child session, modelo resuelto y lease; el lease se libera al terminar o interrumpir. Un descubrimiento que amplía el Work Brief detiene el flujo y exige nueva aprobación.

## Granularidad

- Unidad: resultado mínimo aceptable y validable de forma independiente; se registra en `todo.md` y recibe Validator.
- Actividad: paso técnico dentro de una unidad; vive en la orden del Executor y no recibe agente/validator propios por defecto.
- Divide por resultado, dependencia, ámbito, contrato, riesgo o validación; no por cantidad de archivos ni por cada acción técnica.
- Mantén juntas actividades que comparten resultado, archivos y validación, o que dejarían estados intermedios inválidos.
