# Shell y navegación

## Composición base

```text
AppShell
├── Sidebar: identidad, navegación principal y configuración
├── AppBar: menú móvil, contexto, utilidades y cuenta
└── Main: breadcrumb opcional, encabezado, acciones y contenido
```

- Escritorio: sidebar persistente o colapsable y app bar estable.
- Móvil: sidebar convertido en drawer temporal; app bar conserva activador, contexto y cuenta.
- La navegación y el router derivan de una fuente coherente con permisos; no mantengas menús paralelos divergentes.
- El ítem activo es perceptible sin depender solo del color. Grupos, orden y labels reflejan tareas reales.
- El encabezado de página contiene contexto, un título único, descripción opcional y como máximo una acción primaria destacada.
- El menú de cuenta es un dropdown con identidad, perfil/configuración cuando existan y cerrar sesión. Logout comunica progreso, evita doble activación y termina la sesión real antes de afirmar éxito.
- Sidebar, app bar y main son regiones compartidas; no las dupliques dentro de cada página.
- No fijes dimensiones o colores universales: usa tokens y densidad existentes. Controles interactivos mantienen tamaño táctil y foco visible.
