---
name: agents-md-constitution
description: 'Trigger: crear AGENTS.md, auditar AGENTS.md, constitución de agentes. Crea o audita un bootstrap mínimo conectado al resolver de skills.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.0'
---

## Activation Contract

Activa esta skill al crear, reestructurar o auditar un `AGENTS.md`. Opera en modo `crear` para producir una propuesta y en modo `auditar` para diagnosticar una constitución existente.

## Hard Rules

- Conserva en `AGENTS.md` solo precedencia, alcance, seguridad universal y la ruta obligatoria `./.opencode/skills/governance/skill-resolution-policy/SKILL.md` como bootstrap único.
- Mantén catálogos, matrices, triggers, dependencias, propietarios y procedimientos fuera de `AGENTS.md`; el registro es un índice externo y cada `SKILL.md` es fuente de verdad.
- Exige que router, registro y skills sean autosuficientes para seleccionar por señales, resolver dependencias hasta punto fijo y bloquear rutas ausentes o ciclos.
- No exijas ni generes listados de propietarios, ámbitos o skills en `AGENTS.md`.
- Bloquea la generación si la ruta del resolver falta o no puede leerse. No inventes ni sustituyas rutas.
- Reporta duplicaciones, contradicciones o lógica de resolución embebida en la constitución.

## Decision Gates

| Condición                         | Acción                                                  |
| --------------------------------- | ------------------------------------------------------- |
| No existe constitución            | Usa modo `crear` y la plantilla                         |
| Existe constitución               | Usa modo `auditar`; genera cambios solo si se solicitan |
| Falta la ruta del resolver        | Bloquea la salida generada y reporta la brecha          |
| Catálogo o matriz embebidos       | Declara no conformidad y propón retirarlos              |
| Sistema externo no autosuficiente | Declara no conformidad fuera del archivo constitucional |

## Execution Steps

1. Declara modo, alcance, fuentes de verdad y archivo objetivo.
2. Verifica la ruta del resolver y usa `references/concern-mapping.md` para revisar la autosuficiencia de router, registro y skills.
3. Detecta catálogos, matrices, procedimientos, duplicaciones, contradicciones y lógica especializada embebida.
4. En modo `crear`, completa `assets/AGENTS.template.md` solo si no existen bloqueos.
5. En modo `auditar`, aplica `references/audit-checklist.md` y separa hallazgos de cambios propuestos.
6. Revalida que el bootstrap sea mínimo, tecnológico-agnóstico y no replique el índice ni el algoritmo de resolución.

## Output Contract

Devuelve modo, fuentes revisadas, estado del bootstrap, autosuficiencia de router/registro/skills, hallazgos por severidad, bloqueos y archivos propuestos o modificados. Distingue hechos, decisiones pendientes y recomendaciones. Ante un bloqueo, no presentes una constitución como válida.

## References

- `assets/AGENTS.template.md` — plantilla tecnológica agnóstica.
- `references/concern-mapping.md` — comprobación de separación y autosuficiencia.
- `references/audit-checklist.md` — controles para ambos modos.
