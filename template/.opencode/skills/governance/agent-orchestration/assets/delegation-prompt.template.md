# Contrato de delegación

```text
Trabaja en <directorio>.
Antes de planificar o modificar archivos, lee y aplica estas rutas exactas:
- <ruta resuelta de ../skill-resolution-policy/SKILL.md>
- <cada ruta de seleccionadas y dependencias, exactamente como fue resuelta>
Confirma brevemente las skills leídas y los archivos previstos. No recorras `.atl/skill-registry.md`: esta selección ya fue resuelta.

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

Reporta: skills aplicadas; archivos; decisiones y reglas; validaciones/resultados; señales de reevaluación; riesgos/bloqueos; operaciones destructivas no ejecutadas; confirmación de no haber modificado todo.md.
```
