---
name: react-hook-form-composition
description: 'Trigger: React Hook Form, RHF, FormProvider, useController o campos con formularios. Define adaptadores RHF composables sobre componentes visuales existentes.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.1'
---

## Activation Contract

Activa esta skill al diseñar, implementar o revisar campos, formularios o adaptadores que integren React Hook Form con componentes React por capas.

Carga obligatoriamente `../../frontend/component-composition/SKILL.md`. Carga condicionalmente `../../frontend/frontend-module-architecture/SKILL.md` al decidir ubicación o fronteras, `../../qa/testing-behavior/SKILL.md` al diseñar o cambiar pruebas y `../../qa/frontend-validation/SKILL.md` durante implementación o cierre.

## Hard Rules

- Carga `../../frontend/component-composition/SKILL.md`; clasifica y conserva las capas `base`, `composed` y `specialized`.
- Define `rhf` como composición/adaptador: reutiliza una pieza visual existente y no duplica su markup, estilos ni comportamiento.
- El formulario proveedor debe usar `FormProvider`; los adaptadores deben leerlo con `useFormContext`.
- Conecta cada campo mediante `useController` o `Controller`; obtiene del contexto `value`, `onChange`, `onBlur`, `ref`, `error`, `touched` y `dirty`.
- El adaptador recibe `name` y las props visuales necesarias; no recibe ni implementa reglas de negocio de validación.
- Prohíbe `rules` y validación inline. Usa exclusivamente schemas Zod con `zodResolver`.
- Mantén los schemas fuera de `fields/rhf`; la página, feature o módulo dueño configura el schema y el `FormProvider`.
- Ubica campos visuales globales en `app/shared/components/fields/base` y adaptadores globales en `app/shared/components/fields/rhf`. No mantengas dos APIs globales para el mismo field.
- Si falta la base, créala y valídala antes del adaptador. Búsqueda remota, transformación y reglas específicas pertenecen a hooks o componentes especializados, nunca al adaptador RHF.

## Decision Gates

| Condición                                                   | Decisión                                                                           |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Existe `base`, `composed` o `specialized` visual compatible | Compónlo desde `rhf`; no crees otro campo visual.                                  |
| Falta una capacidad visual reutilizable                     | Revisa las skills de composición y crea/adapta la capa mínima antes del adaptador. |
| El campo necesita validación                                | Declárala en un schema Zod externo y conecta `zodResolver`; nunca uses `rules`.    |
| No existe `FormProvider` o `useFormContext`                 | Detén la implementación y corrige el contexto del formulario.                      |
| Decide ubicación o fronteras                                | Carga `../../frontend/frontend-module-architecture/SKILL.md`.                                  |
| Diseña o cambia pruebas                                     | Carga `../../qa/testing-behavior/SKILL.md`.                                              |
| Implementa o cierra                                         | Carga `../../qa/frontend-validation/SKILL.md`.                                           |

## Execution Steps

1. Inspecciona el campo visual, sus estados y consumidores; carga las referencias locales.
2. Define la capa visual, la API pública y el contrato `rhf` (`name` más props de presentación).
3. Configura `useForm` con schema Zod y `zodResolver`, y envuelve el árbol con `FormProvider`.
4. Implementa el adaptador con `useFormContext` y `useController` o `Controller`, mapeando todos los estados del campo.
5. Verifica accesibilidad, errores, touched/dirty, foco y estados. Si diseñas o cambias pruebas, carga `../../qa/testing-behavior/SKILL.md`; si implementas o cierras, carga `../../qa/frontend-validation/SKILL.md`. Confirma la ausencia de validación inline o schemas en `fields/rhf`.

## Output Contract

Reporta la pieza visual reutilizada y su capa, API del adaptador, ubicación del schema, configuración de contexto/resolver, archivos afectados, validaciones ejecutadas y riesgos pendientes.

## References

- `../../frontend/component-composition/SKILL.md` — autoridad canónica de capas y composición.
- `../../frontend/frontend-module-architecture/SKILL.md` — ubicación y dependencias por alcance.
- `../../qa/testing-behavior/SKILL.md` — pruebas por comportamiento observable.
- `../../qa/frontend-validation/SKILL.md` — validación escalonada y gate de cierre Web.
