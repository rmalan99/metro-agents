---
name: frontend-module-architecture
description: 'Trigger: arquitectura frontend, módulos, submódulos, dependencias, modelos, constantes, catálogos o configuración. Gobierna ubicación y contratos por alcance.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '2.0'
---

## Activation Contract

Activa esta skill antes de crear, mover, dividir o revisar módulos, submódulos, dependencias, contratos públicos, modelos, constantes, catálogos o configuración frontend. Es la única autoridad para su ubicación por alcance.

No tiene dependencias obligatorias ni condicionales dentro de este contrato; sus referencias locales son informativas y no activan otras skills.

## Hard Rules

- Crea un módulo cuando exista un dominio, ruta o flujo con responsabilidades, consumidores o ciclo de evolución propios. Crea un submódulo solo cuando una parte del módulo tenga frontera, rutas o estado claramente cohesionados; no crees carpetas por tamaño.
- Usa `src/app/features/<module>/features/<submodule>/` para submódulos. Dentro de cada feature, usa solo lo necesario: `pages`, `components/shared`, `hooks`, `models`, `requests` y `services`.
- El padre posee composición transversal, navegación y contratos compartidos entre sus hijos; el hijo posee su dominio, UI, estado y acceso a datos. El padre no absorbe reglas internas ni el hijo depende de otro hijo.
- Permite dependencias hacia `app/shared` y de padre a hijo mediante contratos públicos. Prohíbe imports entre features hermanas, imports a internals de otra feature y dependencias circulares; mueve un contrato común a la frontera adecuada.
- Expón únicamente archivos públicos explícitos e importa archivos directamente. No crees ni uses barrels (`index.ts`, `index.tsx` o equivalentes).
- No mezcles reestructuración con cambios funcionales. Antes de mover, inventaría rutas, consumidores, imports, contratos, estado y pruebas; preserva comportamiento y actualiza todos los consumidores.
- Ubica todo el frontend bajo `src/app`; no crees raíces paralelas como `src/features`, `src/pages`, `src/entities` o `src/shared`.
- Reserva `app/router.tsx` para rutas, layouts globales y navegación; la presentación pertenece a la feature. `app/shared` nunca depende de una feature y los layouts transversales viven en `app/layouts`.
- Clasifica cada valor por semántica, alcance, consumidores y fuente de verdad. Ubica dominio, catálogos y configuración reutilizable en `models`: `app/shared/models` si cruzan módulos o `features/<module>/models` si pertenecen a uno; conserva valores no dominiales de una operación, estilos, IDs temporales y valores de render junto a su consumidor.
- Busca fuentes existentes antes de crear o mover. Preserva tipado, inmutabilidad y consumidores; no extraigas sin reducir duplicación, complejidad o acoplamiento mediante una frontera observable.

## Decision Gates

| Señal                                        | Decisión                      |
| -------------------------------------------- | ----------------------------- |
| Dominio/ruta con frontera propia             | Módulo                        |
| Cohesión interna con frontera y ciclo propio | Submódulo                     |
| Uso transversal real                         | `app/shared`                  |
| Una sola operación                           | Mantener junto a la operación |
| Modelo o configuración entre módulos         | `app/shared/models`           |
| Modelo o configuración de un módulo          | `<module>/models`             |

## Execution Steps

1. Mapea dominios, rutas, consumidores, dependencias y contratos actuales.
2. Decide módulo/submódulo, clasifica valores y asigna cada archivo a su ubicación mínima.
3. Define la API pública, dependencias permitidas y migración de imports antes de mover.
4. Reestructura en pasos pequeños, sin cambiar comportamiento; elimina referencias antiguas solo tras migrar consumidores.
5. Verifica límites, ciclos, barrels, rutas, pruebas y regresiones.

## Output Contract

Reporta módulos afectados, mapa antes/después, contratos públicos, consumidores migrados, dependencias prohibidas detectadas, validaciones ejecutadas y riesgos pendientes.

## References

- `references/project-structure.md` — estructura normativa, alcance y dependencias.
- `references/scoped-values.md` — decisiones y escenarios para modelos, constantes, catálogos y configuración.
