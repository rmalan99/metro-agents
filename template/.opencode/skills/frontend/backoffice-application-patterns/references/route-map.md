# Mapa base de rutas

Define equivalentes para estos roles; conserva convenciones y prefijos existentes:

| Rol | Default cuando no existe precedente |
| --- | --- |
| Login | `/login` |
| Recuperación | `/forgot-password`, `/reset-password` |
| Entrada autenticada | `/` con redirect estable o `/dashboard` |
| Listado de recurso | `/<resource>` |
| Creación | `/<resource>/new` |
| Detalle | `/<resource>/:id` |
| Edición | `/<resource>/:id/edit` |
| Acceso denegado | `/unauthorized` |
| No encontrada | fallback `*` |

- No publiques registro, recuperación, detalle o edición si el producto/backend no los soporta.
- Protege rutas privadas y acciones por capacidades reales; ocultar un enlace no reemplaza autorización.
- Sidebar y breadcrumbs enlazan rutas existentes. Mantén retorno, deep links, refresh y parámetros de listado.
- Una ruta desconocida no debe redirigir silenciosamente a una pantalla privilegiada.
