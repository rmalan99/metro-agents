---
name: landing-page-patterns
description: 'Trigger: landing page, página de marketing, página de conversión, hero, pricing o CTA comercial. Define narrativa, secciones y responsive sin imponer librería.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.0'
---

## Activation Contract

Activa esta skill para páginas públicas de comunicación o conversión. Carga obligatoriamente `../product-ui-policy/SKILL.md`, `../frontend-ui-quality/SKILL.md` y `../component-composition/SKILL.md`. No la uses para dashboards o flujos administrativos.

## Hard Rules

- Completa `assets/landing-contract.template.md` antes de implementar. No inventes audiencia, propuesta de valor, testimonios, métricas, clientes, precios ni afirmaciones.
- Construye una narrativa con un CTA primario consistente; cada sección debe resolver una objeción o apoyar esa acción.
- Usa identidad, assets, tokens, componentes y librería existentes. No recrees primitives ni mezcles librerías.
- Prioriza semántica, lectura, rendimiento, SEO técnico y accesibilidad. Decoración y animación nunca bloquean contenido o acción.
- No agregues todas las secciones del catálogo: carga `references/composition.md` y selecciona solo las respaldadas por contenido real.

## Execution

1. Identifica audiencia, objetivo, evidencia, CTA y contenido aprobado.
2. Completa contrato y selecciona secciones mínimas.
3. Define jerarquía desktop/móvil con `references/responsive-and-performance.md`.
4. Implementa con componentes existentes y contenido real.
5. Verifica CTA, navegación, lectura, metadatos, rendimiento y accesibilidad.

## Output Contract

Reporta audiencia, objetivo, CTA, narrativa, secciones elegidas/omitidas, evidencia usada, componentes reutilizados y verificaciones responsive, accesibles y de rendimiento.

## References

- `references/composition.md` — narrativa y catálogo condicional.
- `references/responsive-and-performance.md` — adaptación, SEO y rendimiento.
- `assets/landing-contract.template.md` — contrato de contenido.
