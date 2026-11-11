---
name: implementation-decision-policy
description: 'Trigger: detalle no especificado, ambigüedad de implementación, decisión técnica. Decide con evidencia, bajo riesgo y escalamiento explícito.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.0'
---

## Activation Contract

Activa esta skill al implementar cuando las instrucciones dejan detalles sin fijar. Úsala para elegir entre opciones compatibles; no sustituye `task-governance` ni ninguna skill especializada aplicable.

## Hard Rules

- Respeta esta precedencia: usuario → constitución/skills → contratos/arquitectura → patrones repetidos → capacidades existentes → cambio mínimo reversible.
- Decide sin preguntar solo con evidencia suficiente, riesgo bajo, reversibilidad y contrato preservado.
- Reutiliza la solución vigente; no introduzcas dependencias, abstracciones ni arquitectura si una capacidad existente resuelve el caso.
- Declara los supuestos relevantes y aplica defaults conservadores.
- Distingue hechos, supuestos, decisión y escalamiento; no presentes inferencias como evidencia.
- Detente ante destrucción, seguridad/autorización, decisión de negocio, contrato incompatible, contradicción normativa o ausencia de una opción segura y reversible.

## Decision Gates

| Condición                                  | Acción                                                                  |
| ------------------------------------------ | ----------------------------------------------------------------------- |
| Evidencia suficiente y opción conservadora | Decide y registra la justificación                                      |
| Varias opciones equivalentes               | Prefiere patrón repetido, capacidad existente y menor cambio reversible |
| Supuesto relevante pero seguro             | Decláralo, usa un default conservador y continúa                        |
| Se activa un límite de escalamiento        | Detente y solicita la decisión mínima necesaria                         |

## Execution Steps

1. Separa hechos de detalles no especificados.
2. Recorre `references/decision-hierarchy.md` sin saltar niveles.
3. Evalúa contrato, riesgo, reversibilidad y evidencia.
4. Comprueba `references/escalation-gates.md` antes de actuar.
5. Ejecuta la opción vigente más pequeña o escala con alternativas acotadas.

## Output Contract

Reporta hechos, supuestos, decisión y evidencia. Si escalas, indica el gate, el riesgo y la decisión mínima requerida. Confirma qué contrato preservaste y si aplicaste un default conservador.

## References

- `references/decision-hierarchy.md` — jerarquía operativa y escenarios de decisión.
- `references/escalation-gates.md` — límites obligatorios y escenarios de escalamiento.
