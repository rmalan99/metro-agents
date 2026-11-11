---
name: supabase-delivery-pipeline
description: 'Trigger: pipeline Supabase, CI/CD, despliegue, migraciones en producción. Configura una entrega Web/API normativa, segura y portable.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.2'
---

## Activation Contract

Activa esta skill al crear o modificar CI/CD que valida o promueve recursos Supabase. No la actives para un pipeline Web-only sin mutaciones de recursos Supabase. Es normativa y no depende de un proveedor de CI u hosting.

## Hard Rules

- Cuando esta skill está activa, carga `~/.agents/skills/supabase/SKILL.md` y `../supabase-development-workflow/SKILL.md`.
- Carga `../supabase-backend-architecture/SKILL.md` para SQL/DB y para Edge Functions, webhooks o integraciones, con o sin DB.
- Carga `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` solo para SQL/DB o Edge Functions, webhooks o integraciones con DB.
- Auth o Storage sin DB no añade arquitectura ni prácticas Postgres. Si una ruta obligatoria no existe, detén la tarea.
- Las rutas de `References` son informativas; no añaden dependencias obligatorias.
- Mantén una única autoridad para promover cada entorno. No combines integración automática de Supabase y un workflow que despliegue los mismos recursos.
- Separa CI de PR y CD protegido. PR valida sin tocar producción; CD promueve artefactos y migraciones ya revisados.
- Fija versiones de runtimes, gestor, dependencias, acciones y Supabase CLI; usa lockfile y caché no autoritativa.
- Aplica solo los gates correspondientes a recursos afectados, conservando este orden relativo: configuración → calidad → pruebas → build → migraciones → backend → Web → smoke tests.
- Las migraciones preceden solo a consumidores compatibles con el esquema expandido. Usa expansión/contracción para cambios incompatibles.
- Usa credenciales de mínimo alcance, ambientes protegidos y secretos fuera de logs/artefactos. El frontend recibe únicamente valores públicos.
- En CLI v3, especifica `--remote` y `--yes` en mutaciones remotas no interactivas; descubre la sintaxis real antes de escribir el pipeline.
- No ejecutes resets, reparaciones de historial ni borrados destructivos desde CI/CD.

## Decision Gates

| Recursos validados o promovidos                      | Dependencias obligatorias                                                                                          |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Web-only, sin mutaciones de recursos Supabase        | No activar esta skill                                                                                              |
| Auth o Storage sin cambios de DB                     | Supabase global + `../supabase-development-workflow/SKILL.md`                                                      |
| Edge Function, webhook o integración sin DB          | Supabase global + workflow + `../supabase-backend-architecture/SKILL.md`                                           |
| SQL, esquema, RLS, RPC, índice, trigger, cron o cola | Supabase global + workflow + arquitectura + `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` |
| Edge Function, webhook o integración con DB          | Supabase global + workflow + arquitectura + `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` |

| Evento                 | Resultado                                     |
| ---------------------- | --------------------------------------------- |
| Pull request           | Validación + entorno efímero/preview opcional |
| Merge a rama protegida | Promoción secuencial al entorno autorizado    |
| Migración pendiente    | Dry run/plan, aprobación y aplicación única   |
| Gate fallido           | Detén dependientes; conserva evidencia        |

## Execution Steps

1. Declara entornos, autoridad, permisos, concurrencia y artefactos.
2. Implementa CI reproducible y, solo si afecta DB, validación aislada de migraciones.
3. Implementa CD con exclusión mutua, destino explícito y aprobaciones.
4. Promueve únicamente los recursos afectados —esquema, configuración, funciones o Web— en orden compatible; un pipeline Web-only no ejecuta migraciones ni promoción backend.
5. Ejecuta smoke tests autenticados/no autenticados sin exponer secretos.
6. Publica evidencia, versión desplegada y procedimiento de recuperación.

## Output Contract

Reporta skills leídas, reglas aplicadas, eventos, jobs, dependencias, secretos/variables, gates, comandos con destino, concurrencia, artefactos, smoke tests y recuperación.

## References

- `references/pipeline-rules.md` — etapas, matriz de secretos y recuperación.
