# Reglas de paralelización

## Límites

- No excedas cuatro subagentes simultáneos.
- Cuando el trabajo lo permita, limita el plan por defecto a dos subagentes.
- Paraleliza únicamente tareas independientes. Si no puedes demostrar independencia, ejecuta en secuencia.

## Prueba de independencia

Antes de lanzar más de un subagente, compara archivos, módulos, contratos, migraciones, configuración, pruebas, comportamiento y validación.

- Los subagentes no comparten archivos; reserva cada archivo o módulo compartido a uno solo.
- Un contrato compartido modificado por ambas tareas obliga a secuencia.
- Una dependencia directa, un conflicto o un comportamiento o validación no independientes obliga a secuencia.
- No concluyas independencia solo porque no existan archivos comunes.

## Registro de coordinación

Registra o comunica antes del lanzamiento:

| Tarea  | Responsable | Archivos/módulos reservados | Contratos     | Dependencias     | ¿Paralela?         |
| ------ | ----------- | --------------------------- | ------------- | ---------------- | ------------------ |
| `<id>` | `<agente>`  | `<rutas>`                   | `<contratos>` | `<dependencias>` | `<sí/no y motivo>` |

Cada agente recibe una responsabilidad puntual y reservas sin solapamiento. Los conflictos detectados después del lanzamiento detienen el trabajo afectado y se reportan al orquestador.
