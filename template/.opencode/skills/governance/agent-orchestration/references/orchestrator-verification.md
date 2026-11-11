# Verificación independiente del orquestador

El reporte del subagente no constituye evidencia suficiente. Después de cada delegación, el orquestador revisa personalmente:

1. Que las rutas entregadas coincidan exactamente con `seleccionadas` y `dependencias`, más `skill-resolution-policy`, sin adiciones intuitivas.
2. Que `task-governance` solo se haya entregado si pertenece al punto fijo recibido.
3. Archivos modificados, alcance reservado, ausencia de correcciones ajenas y no modificación de `todo.md`.
4. Resultado observable y todos los criterios de aceptación.
5. Validaciones aplicables declaradas en el contrato.
6. Que toda señal de cambio de alcance haya detenido el trabajo y producido una nueva resolución antes de continuar.

Si `task-governance` pertenece al punto fijo, coordina estado y evidencia con sus gates de cierre; no sustituyas ni dupliques su contrato de `todo.md`.

## Autorización de cierre

- Autoriza una microtarea solo si el resultado está implementado, el alcance fue respetado, las validaciones aplicables pasan y el orquestador verificó personalmente.
- Si falla un gate, conserva la tarea pendiente, documenta la evidencia, no avances dependientes y conserva el mismo subagente cuando su contexto aporte valor.
- Autoriza una fase solo cuando todas sus microtareas estén verificadas y no existan dependencias bloqueadas.

El subagente implementa y aporta resultados; el orquestador conserva contexto, revisa, valida y autoriza.
