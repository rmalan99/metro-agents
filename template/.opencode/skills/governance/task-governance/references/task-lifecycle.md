# Ciclo de vida de tareas

## Evaluación y planificación

Antes de implementar:

1. Evalúa estado actual y contexto.
2. Identifica objetivo, alcance, restricciones, riesgos y dependencias.
3. Revisa elementos reutilizables.
4. Define pasos concretos.
5. Organízalos en fases verificables.
6. Presenta el plan al usuario.

Cada fase declara propósito, resultado comprobable y criterios de término. No inicies una fase dependiente hasta validar su requisito previo. La selección, límite y coordinación de subagentes pertenecen al gobierno de delegación, no a esta skill.

## Ámbitos y granularidad

- Declara `Web`, `API` o `Web/API` en cada plan, fase y tarea. Usa `Web/API` solo cuando sea inevitable.
- No mezcles cambios Web/API en una microtarea. Si una funcionalidad afecta ambos, crea tareas independientes con dependencias explícitas y conserva separadas estructura, convenciones y responsabilidades.
- Divide cada funcionalidad en microtareas independientes, pequeñas, comprensibles y verificables.
- Da a cada microtarea un único resultado observable, dependencias y orden explícitos. No la cierres sin implementar y verificar ese resultado.
- Usa como límite la unidad mínima aceptable y verificable, no la acción técnica mínima. Mantén sus actividades atómicas en la orden de ejecución para evitar sobrefragmentación.

## Registro y estados

Registra toda tarea y microtarea acordada en `todo.md` antes de implementarla. Cada entrada debe ser independiente y no ambigua, sin mezclar implementación con refactorización, documentación o correcciones ajenas. Incluye resultado observable, alcance, dependencias, criterios verificables y pruebas o comandos aplicables.

Si afecta un componente Web global, incluye actualizar el catálogo. Si elimina API, archivo o componente, incluye migración y verificación de todos sus consumidores.

Usa identificadores `WEB-###`, `API-###` o `TRV-###` y el ciclo:

```text
pendiente → preparada → ejecutando → bloqueada | verificando → completada
```

- `preparada`: contrato completo y dependencias validadas.
- `ejecutando`: habilita mutaciones dentro del alcance reservado.
- `bloqueada`: detiene mutaciones hasta resolver y volver a `preparada`/`ejecutando`.
- `verificando`: implementación detenida salvo corrección autorizada; el orquestador contrasta evidencia.
- `completada`: aceptación y validaciones verificadas, checkbox `[x]`.

Representación:

- `[ ]`: pendiente, bloqueada o en ejecución.
- `[x]`: completada y verificada por el orquestador.

Una bloqueada permanece `[ ]` y documenta causa concreta y evidencia: error, comando o dependencia pendiente. Solo el agente primario responsable modifica el registro, verifica evidencia y marca tareas; los subagentes nunca modifican `todo.md`.
