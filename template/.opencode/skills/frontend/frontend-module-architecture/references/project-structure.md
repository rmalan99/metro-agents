# Estructura normativa frontend

```text
src/app/
├── router.tsx
├── layouts/
├── shared/{components,models,utils,hooks}
└── features/<module>/
    ├── routes/
    ├── shared/{components,models,utils,hooks}
    └── pages/
        ├── shared/{components,models,utils,hooks}
        └── <page>/{shared/{components,models,utils,hooks},<Page>.tsx}
```

- `app/features/dashboard` posee la ruta raíz; no crees un módulo global `pages` para ella.
- `routes` define rutas del módulo; su `shared` sirve al módulo.
- `pages/shared` sirve a varias páginas; el `shared` de una página solo sirve a esa página.
- Amplía la estructura únicamente por alcance o responsabilidad demostrable.
- Una feature puede depender de `app/shared`; `app/shared` nunca depende de una feature.
- Una feature no importa internals de otra. Mueve el contrato común a la frontera correcta.
- `app/router.tsx` no contiene presentación de feature.
- Los layouts usados por varios módulos o rutas viven en `app/layouts`, no dentro de una página.
- Usa imports directos. Los barrels están prohibidos.
