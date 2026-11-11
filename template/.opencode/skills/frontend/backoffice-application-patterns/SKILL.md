---
name: backoffice-application-patterns
description: 'Trigger: backoffice, panel administrativo, admin dashboard, listado administrativo o shell de administración. Define rutas, shell y patrones de pantalla reproducibles.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.0'
---

## Activation Contract

Activa esta skill al crear o revisar un backoffice o una pantalla administrativa. Carga obligatoriamente `../product-ui-policy/SKILL.md`, `../frontend-ui-quality/SKILL.md` y `../component-composition/SKILL.md`. Carga solo la referencia del tipo de pantalla actual; no leas todo el catálogo.

## Hard Rules

- Usa por defecto un shell con sidebar, app bar, contenido principal y menú de cuenta; el cierre de sesión vive en el dropdown de cuenta. Una excepción exige un patrón aprobado existente o decisión explícita.
- Antes de diseñar, completa `assets/backoffice-profile.template.md`; antes de implementar una pantalla, completa `assets/screen-contract.template.md`.
- Preserva primero producto, rutas, permisos, componentes, tokens y librería UI existentes. Si hay librería, usa sus componentes y tema; no recrees equivalentes ni mezcles librerías.
- La skill define semántica y composición, no APIs de MUI, shadcn, Tailwind, React ni un router. Resuelve capacidades tecnológicas solo cuando dependencias o archivos las demuestren.
- No inventes módulos, métricas, rutas de negocio, permisos, datos, acciones ni integraciones. Los defaults completan estructura ausente, no requisitos de dominio.
- Implementa carga, vacío, error, permisos y responsive aplicables. Para operaciones remotas carga `../../data/remote-data-behavior/SKILL.md`; para React carga `../../react/react-behavior-implementation/SKILL.md`.

## Decision Gates

| Alcance | Referencia mínima |
| --- | --- |
| Proyecto o shell | `references/shell-and-navigation.md` + `references/route-map.md` |
| Dashboard | `references/dashboard.md` |
| Listado/filtros | `references/listings-and-filters.md` |
| Detalle | `references/detail-pages.md` |
| Crear/editar | `references/forms.md` |
| Login/sesión | `references/authentication.md` |
| Modal/alerta | `references/overlays-and-feedback.md` |
| Responsive o elección de componentes | `references/responsive-and-ui-library.md` |

## Execution

1. Inspecciona producto, rutas, permisos, librería, tokens y componentes existentes.
2. Completa perfil, mapa de rutas si aplica y contrato de pantalla.
3. Carga solo referencias y skills condicionales necesarias.
4. Implementa el patrón mínimo con estados reales y componentes existentes.
5. Verifica contrato, responsive, permisos, navegación, accesibilidad y operaciones remotas.

## Output Contract

Reporta arquetipo, perfil, ruta, patrón de pantalla, componentes reutilizados, capacidad UI detectada, estados, permisos, responsive, referencias cargadas y cualquier excepción autorizada.

## References

- `assets/backoffice-profile.template.md` — decisiones globales.
- `assets/route-map.template.md` — inventario de rutas.
- `assets/screen-contract.template.md` — contrato por pantalla.
