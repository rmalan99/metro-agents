---
name: supabase-backend-architecture
description: 'Trigger: arquitectura backend Supabase, Data API, RPC, Edge Functions, RLS. Aplica una arquitectura backend normativa y segura.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.3'
---

## Activation Contract

Activa esta skill antes de diseñar, implementar, mover o revisar fronteras backend sobre Supabase: Data API, SQL, RLS, RPC, índices, triggers, cron, colas, Edge Functions, webhooks o integraciones.

## Hard Rules

- Carga siempre `~/.agents/skills/supabase/SKILL.md`.
- Carga `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` solo para SQL, esquema, RLS, RPC, índices, triggers, cron, colas o una Edge Function, webhook o integración que acceda a DB.
- Una Edge Function, webhook o integración sin DB no activa prácticas Postgres. Si una ruta requerida por estas condiciones no existe, detén la tarea.
- Las rutas de `References` son informativas; no añaden dependencias obligatorias.
- Modela primero el contrato y la autorización; después el transporte y la persistencia.
- Usa la frontera mínima: Data API para CRUD protegido por RLS; RPC para operación transaccional centrada en datos; Edge Function para secretos, integraciones, webhooks, orquestación o protocolo HTTP propio.
- Separa handler, caso de uso y acceso externo cuando existan esas responsabilidades. El handler valida, autentica, delega y responde; no contiene negocio ni SQL.
- Mantén contratos públicos separados de filas de base de datos. No expongas columnas internas por conveniencia.
- Habilita RLS en todo objeto expuesto y combina rol con autorización por fila. Nunca expongas claves secretas o `service_role` al cliente.
- Ubica lo transversal globalmente, lo compartido dentro del dominio y lo exclusivo junto a la operación. Prohíbe capas genéricas hipotéticas y dependencias entre internals de dominios.
- Todo listado remoto implementa búsqueda, filtros, orden y paginación en servidor.
- Los handlers solo reciben, validan, delegan y construyen la respuesta. Negocio vive en casos de uso; persistencia e integraciones viven en repositorios o puertos existentes cuando la separación aporta una responsabilidad real.

## Decision Gates

| Recurso afectado                                     | Dependencias requeridas                                                                  |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| SQL, esquema, RLS, RPC, índice, trigger, cron o cola | Supabase global + `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` |
| Edge Function, webhook o integración sin DB          | Solo `~/.agents/skills/supabase/SKILL.md`                                      |
| Edge Function, webhook o integración con DB          | Supabase global + `~/.agents/skills/supabase-postgres-best-practices/SKILL.md` |

| Necesidad                                 | Frontera obligatoria               |
| ----------------------------------------- | ---------------------------------- |
| CRUD con políticas por fila               | Data API + RLS                     |
| Escritura atómica o consulta de dominio   | RPC                                |
| Secreto, tercero, webhook o HTTP especial | Edge Function                      |
| Proceso diferido o periódico              | Cola/cron + consumidor idempotente |

## Execution Steps

1. Define actor, entrada, salida, errores, permisos e idempotencia.
2. Selecciona la frontera con la tabla anterior y asigna propietarios por capa.
3. Solo si afecta DB, diseña esquema, constraints, índices, grants y RLS como una unidad.
4. Implementa el camino mínimo sin duplicar reglas entre SQL, función y cliente.
5. Prueba éxito, rechazo, aislamiento entre usuarios, concurrencia y límites.
6. Revisa consumidores, privilegios, observabilidad y compatibilidad.

## Output Contract

Reporta skills leídas, reglas aplicadas, contrato, frontera elegida, capas/archivos, modelo de autorización, pruebas, riesgos y decisiones descartadas.

## References

- `references/architecture-rules.md` — estructura, dependencias y contratos normativos.
