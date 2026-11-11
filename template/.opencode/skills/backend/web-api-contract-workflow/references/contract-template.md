# Contrato transversal Web/API

## Campos obligatorios

| Campo               | Definición                                         |
| ------------------- | -------------------------------------------------- |
| Operación           | nombre, propósito y propietario                    |
| Transporte          | método, ruta, RPC, evento o función                |
| Actor               | anónimo, autenticado, rol o sistema                |
| Autorización        | permiso y predicado exacto                         |
| Entrada             | tipos, restricciones, defaults y normalización     |
| Éxito               | estado y estructura estable                        |
| Errores             | código estable, condición y recuperabilidad        |
| Compatibilidad      | versiones soportadas y secuencia de migración      |
| Responsabilidad API | validación, negocio, persistencia y autorización   |
| Responsabilidad Web | consulta, presentación, interacción y estados      |
| Ejemplos            | éxito, rechazo, vacío y límites                    |
| Fixtures/dobles     | datos suficientes para validar cada ámbito aislado |

## Listados

Todo listado acepta `page`, `pageSize` y `search` validados, además de filtros y orden explícitos cuando apliquen. Responde:

```text
items
page
pageSize
total
totalPages
```

La API ejecuta búsqueda, filtros, orden y paginación. Web no descarga la colección completa para procesarla localmente. Cubre página vacía, tamaño máximo, cero resultados y parámetros inválidos.

## Secuencia de tareas

```text
TRV: definir/aprobar contrato
  ├─ API: implementar y validar con fixtures
  └─ WEB: implementar y validar con dobles
TRV: validar integración
```

Ante cualquier cambio, detén las tareas consumidoras, actualiza contrato/fixtures/aceptación y revalida ambos ámbitos antes de integración.
