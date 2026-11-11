---
name: supabase-development-workflow
description: 'Trigger: flujo Supabase, migración, RLS, Edge Function, desarrollo local. Ejecuta el método normativo de cambio y validación Supabase.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.3'
---

## Activation Contract

Activa esta skill para cualquier cambio de esquema, datos, RLS, RPC, Storage, Auth, cron, colas, Edge Functions, webhooks o integraciones Supabase.

## Hard Rules

- Carga siempre `~/.agents/skills/supabase/SKILL.md`.
- Carga `../supabase-backend-architecture/SKILL.md` para SQL/DB y para Edge Functions, webhooks o integraciones, con o sin DB.
- Carga `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` solo para SQL/DB o para Edge Functions, webhooks o integraciones con DB.
- Auth o Storage sin cambios de DB no añade arquitectura ni prácticas Postgres. Si una ruta obligatoria no existe, detén la tarea.
- Las rutas de `References` son informativas; no añaden dependencias obligatorias.
- Usa Git como fuente de verdad: ningún cambio remoto manual sustituye migraciones, configuración o funciones versionadas.
- Si el alcance afecta DB, detecta antes el flujo: `supabase/schemas` o `schema_paths` implica declarativo; en otro caso usa migraciones imperativas.
- Si el alcance requiere migraciones, genéralas mediante la CLI; no inventes nombres/versiones. Revisa todo SQL antes de aplicarlo.
- Cuando apliques cambios de DB, hazlo incrementalmente sobre la base local existente. Nunca ejecutes reset, recreación de volúmenes ni borrado masivo sin autorización explícita y respaldo verificable.
- Implementar una migración nunca autoriza destruir datos. Antes de cualquier operación potencialmente destructiva, detente, identifica los datos afectados y solicita autorización explícita en el mismo turno.
- Prueba desde cero solo en un entorno efímero sin datos del usuario.
- Fija versión de CLI, consulta changelog/documentación y descubre sintaxis con `--help`. En CLI v3, toda mutación remota usa destino explícito y consentimiento no interactivo.
- Entrega cada recurso afectado y sus dependientes —esquema, grants, RLS, pruebas, tipos o consumidores— como una unidad compatible; no añadas artefactos DB a cambios que no los requieren.

## Decision Gates

| Alcance                                              | Dependencias adicionales                                                                                             |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Auth o Storage sin cambios de DB                     | Ninguna además de `~/.agents/skills/supabase/SKILL.md`                                                     |
| SQL, esquema, RLS, RPC, índice, trigger, cron o cola | `../supabase-backend-architecture/SKILL.md` + `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` |
| Edge Function, webhook o integración sin DB          | `../supabase-backend-architecture/SKILL.md`                                                                          |
| Edge Function, webhook o integración con DB          | `../supabase-backend-architecture/SKILL.md` + `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` |

| Estado                  | Acción                                                                 |
| ----------------------- | ---------------------------------------------------------------------- |
| Esquema declarativo     | Edita estado deseado y genera migración con el comando vigente         |
| Migraciones imperativas | Crea migración, escribe SQL y aplica incrementalmente                  |
| Remoto diverge          | Detén promoción; diagnostica historial y captura/repara con aprobación |
| Validación destructiva  | Usa proyecto/base efímera                                              |

## Execution Steps

1. Define contrato, alcance, compatibilidad, seguridad y recuperación.
2. Comprueba versión/ayuda de la CLI usada y, solo si afecta DB, el estado de migraciones local/remoto.
3. Si afecta DB, implementa esquema, grants y políticas aplicables; aplica migraciones localmente sin reset.
4. Implementa solo los RPC, funciones, configuración Auth/Storage, tipos o consumidores incluidos en el alcance.
5. Ejecuta únicamente las validaciones aplicables: SQL, RLS, funciones, Auth/Storage, integración, lint o advisors.
6. Revisa diff, secretos, orden de migraciones y estrategia de despliegue.
7. Solo si el alcance incluye promoción, promueve los recursos afectados mediante el pipeline autorizado y verifica el resultado remoto.

## Output Contract

Reporta skills leídas, reglas aplicadas, archivos, contrato, todos los comandos Supabase y destinos, pruebas, estado de migraciones, riesgos y confirmación explícita de que no hubo resets, borrados ni recreación destructiva de volúmenes.

## References

- `references/workflow-rules.md` — ciclo completo, gates y validación mínima.
