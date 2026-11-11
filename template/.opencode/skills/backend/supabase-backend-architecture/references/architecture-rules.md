# Reglas normativas de arquitectura backend Supabase

## Estructura base

Usa esta estructura conceptual y adáptala únicamente a los nombres ya establecidos por el repositorio:

```text
supabase/
├── config.toml
├── migrations/
├── schemas/                 # solo en flujo declarativo
├── functions/
│   ├── _shared/             # infraestructura compartida real
│   └── <operation>/
│       ├── index.ts         # adaptador HTTP
│       ├── service.ts       # caso de uso, si existe negocio
│       ├── repository.ts    # acceso externo, si se reutiliza o complejiza
│       ├── schema.ts        # entrada/salida pública
│       └── *.test.ts
├── tests/                   # seguridad y contratos SQL
└── fixtures/                # escenarios reproducibles, no datos productivos
```

No crees archivos vacíos para cumplir la estructura. Una operación pequeña puede conservar handler y caso de uso juntos mientras el handler siga siendo legible y no mezcle SQL, HTTP y negocio.

## Dependencias permitidas

```text
handler → caso de uso → puerto/repositorio → Supabase o tercero
                   ↘ dominio/contratos internos
```

- El dominio no depende de HTTP, SDK de Supabase ni variables de entorno.
- Un repositorio no decide respuestas HTTP ni permisos de interfaz.
- `_shared` solo recibe código utilizado por más de una función; un dominio no importa internals de otro.
- La Web consume contratos públicos, nunca tipos de persistencia como fuente de verdad del negocio.

## Contrato obligatorio

Antes de implementar, fija:

| Campo          | Contenido                                              |
| -------------- | ------------------------------------------------------ |
| Operación      | nombre y propósito observable                          |
| Actor          | anónimo, autenticado, rol de aplicación o sistema      |
| Entrada        | tipos, límites y normalización                         |
| Salida         | éxito estable sin columnas internas accidentales       |
| Errores        | código estable, estado HTTP cuando aplique y condición |
| Autorización   | predicado exacto y propietario de su aplicación        |
| Idempotencia   | clave, ventana o motivo explícito para no requerirla   |
| Observabilidad | evento, correlación y datos que deben redactarse       |

## Seguridad

- Trata `anon`/publishable como identificadores públicos, no como autorización.
- Usa `TO` para roles y predicados de propiedad/tenant en RLS.
- En `UPDATE`, define `USING` y `WITH CHECK`; añade política `SELECT` cuando corresponda.
- Mantén funciones privilegiadas fuera de esquemas expuestos, revoca `EXECUTE` público y valida `auth.uid()` cuando `SECURITY DEFINER` sea inevitable.
- Las vistas expuestas usan `security_invoker` cuando esté disponible.
- Valida origen solo como defensa del navegador; nunca sustituye autenticación/autorización.
- No registres JWT, cookies, claves, cuerpos sensibles ni secretos.

## Datos y operaciones

- Constraints expresan invariantes durables; la aplicación mejora mensajes, no reemplaza integridad.
- Índices se justifican por consultas, joins, filtros, RLS y orden reales.
- Todo listado acepta `page`, `pageSize` y `search` validados; añade filtros y orden explícitos cuando apliquen. Responde `items`, `page`, `pageSize`, `total`, `totalPages` y ejecuta búsqueda/filtros/orden en servidor. Cubre página vacía, tamaño máximo y cero resultados.
- Trabajos, webhooks y cron son idempotentes, reclaman trabajo atómicamente y distinguen reintento de fallo permanente.
- Cambios incompatibles usan expansión → migración de consumidores/datos → contracción; no rompas Web y API en un único despliegue.
