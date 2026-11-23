# Contrato de delegación

```text
Trabaja en <directorio>.
Lease de coordinación: <child session y tarea creados por governance_agent_launch>.
Perfil/modelo: <perfil y modelo resueltos>.
Antes de planificar o modificar archivos, lee y aplica estas rutas exactas:
- <ruta resuelta de ../skill-resolution-policy/SKILL.md>
- <cada ruta de seleccionadas y dependencias, exactamente como fue resuelta>
Confirma en una línea las skills leídas y los archivos previstos. No recorras `.atl/skill-registry.md`: esta selección ya fue resuelta.

Recibo de resolución:
- alcance: <intención, artefacto y archivos reservados>
- skills: <rutas seleccionadas y dependencias, en orden>
- reevaluar_cuando: <condiciones>

Implementa únicamente: <resultado observable>.
Comportamiento esperado: <criterios observables>.
Alcance permitido: <archivos o módulo reservados>.
Fuera de alcance: <cambios prohibidos>.
Contratos y dependencias: <reservas y requisitos validados>.

No modifiques todo.md. No amplíes el alcance ni corrijas fallos ajenos; repórtalos.
Si aparece una condición de reevaluación o una señal que cambia intención, artefactos, archivos o alcance, detente y solicita un recibo nuevo. No amplíes la selección ni recorras el registro por iniciativa propia.
Ejecuta: <comandos y validaciones aplicables>. El orquestador los verifica personalmente al cierre.

Filtra toda salida antes de reportarla: entrega coincidencias, errores y resumen, nunca logs, diffs, catálogos, schemas o respuestas API completos. No repitas una validación aprobada sin evidencia contradictoria.

Reporta únicamente: veredicto; archivos; validaciones/resultados nuevos; señales de reevaluación; riesgos/bloqueos; confirmación de no haber modificado todo.md.
```
