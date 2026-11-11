# Gates de cierre

## Verificación

Solo el orquestador verifica y marca tareas. Para cerrar una tarea:

1. Confirma que el resultado observable está implementado.
2. Ejecuta las pruebas, comandos y comportamientos declarados en `Validación`.
3. Contrasta la evidencia con todos los criterios de aceptación.
4. Verifica dependencias, alcance y requisitos condicionales: catálogo para componente Web global; migración y consumidores para API, archivo o componente eliminado.

## Resultado del gate

- Si cumple todos los criterios, marca `[x]` inmediatamente y registra evidencia verificable.
- Si no cumple, conserva `[ ]`; si existe impedimento, añade `🚫 Bloqueada`, causa concreta y evidencia.
- Nunca marques una tarea solo por haber escrito código.
- Conserva las tareas completadas durante todo el flujo.
- Solo el usuario puede autorizar eliminar tareas completadas al final.
- Los subagentes no modifican `todo.md`; reportan resultados para que el orquestador verifique y marque.
