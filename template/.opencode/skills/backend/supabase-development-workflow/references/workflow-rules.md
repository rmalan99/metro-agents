# Flujo normativo de desarrollo Supabase

## Seguridad de datos locales

- Prohíbe `supabase db reset` y equivalentes sobre la base local persistente del usuario, incluidos resets con flags locales/remotos, recreación de volúmenes Docker y borrados masivos.
- La autorización para implementar o aplicar una migración no autoriza un reset.
- Aplica migraciones revisadas incrementalmente con el comando local vigente (`supabase migration up --local` en el flujo actual).
- Si la base existente no es compatible, detén el trabajo; no la conviertas en entorno descartable.
- Valida desde cero únicamente en una base, rama o proyecto efímero sin datos del usuario.
- Una operación destructiva requiere impacto explicado, autorización explícita en el mismo turno y respaldo verificable previo.
- El resultado enumera todos los comandos Supabase ejecutados y confirma que no hubo resets ni borrados destructivos.

## Ciclo obligatorio

### 1. Preparar

- Inventaría consumidores Web/API y contratos afectados.
- Separa contrato transversal, implementación API e implementación Web.
- Define expansión/contracción para cambios incompatibles.
- Comprueba `supabase --version` y la ayuda de cada comando usado.
- Revisa cambios relevantes del changelog antes de modificar configuración o pipeline.

### 2. Implementar datos

**Imperativo:** crea el archivo con `supabase migration new <nombre>`, edita SQL y aplica con el comando incremental local vigente.

**Declarativo:** edita `supabase/schemas`, genera la migración con la operación declarativa vigente y revisa el SQL resultante. No edites únicamente la migración generada dejando el estado declarado desactualizado.

Cada cambio incluye cuando aplique:

- tipos y nullability explícitos;
- constraints y defaults;
- índices justificados;
- grants de acceso al Data API;
- RLS y políticas por operación;
- comentarios o contratos de RPC;
- migración de datos acotada y reanudable;
- camino de compatibilidad y recuperación.

### 3. Implementar comportamiento

- Usa Data API, RPC o Edge Function según `supabase-backend-architecture`.
- Centraliza inicialización del cliente por runtime.
- En navegador usa URL + publishable key; en servidor usa credenciales mínimas necesarias.
- No uses `service_role` para evitar diseñar RLS. Si un proceso de sistema necesita bypass, limita su operación, valida entrada y audita el acceso.
- Genera tipos después de estabilizar el esquema; no mantengas copias manuales divergentes.

### 4. Validar

Ejecuta, según disponibilidad:

1. estado/lista de migraciones;
2. aplicación incremental local;
3. lint y advisors de base de datos;
4. pruebas de constraints, RPC y funciones;
5. pruebas RLS como `anon`, usuario propietario, usuario ajeno y rol de sistema;
6. pruebas de página vacía, límites y concurrencia;
7. generación de tipos y typecheck de consumidores;
8. pruebas Web/API e integración;
9. revisión de diff y secretos.

Un error ajeno se reporta; no se corrige ampliando alcance.

## Entornos

| Entorno           | Propósito                                | Datos                                 |
| ----------------- | ---------------------------------------- | ------------------------------------- |
| Local persistente | desarrollo diario incremental            | del desarrollador; nunca descartables |
| Efímero           | reconstrucción, migración desde cero, PR | sintéticos y eliminables              |
| Preview/Staging   | integración y aceptación                 | anonimizados o sintéticos             |
| Producción        | tráfico real                             | protegidos; solo pipeline autorizado  |

## Recuperación

- No modifiques una migración ya promovida; crea una nueva corrección.
- No uses `migration repair` hasta demostrar si falla el esquema o solo el historial.
- No reviertas automáticamente una migración de datos. Prefiere corrección hacia delante y restauración validada cuando sea necesaria.
- Ante fallo de despliegue, detén consumidores dependientes, conserva evidencia y no repitas ciegamente.
