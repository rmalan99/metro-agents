---
name: skill-resolution-policy
description: 'Trigger: inicio de solicitud o cambio de alcance. Selecciona contratos aplicables sin cargar skills irrelevantes.'
license: Apache-2.0
metadata:
  author: 'mouseinyl'
  version: '1.1'
---

## Activation Contract

Único bootstrap de resolución. Actívalo al inicio y cuando cambien intención, artefactos, archivos o alcance. Lee primero solo `.atl/skill-registry.md`; no cargues cuerpos sin coincidencia.

## Hard Rules

- Cada `SKILL.md` seleccionado es fuente de verdad; el registro es solo índice.
- Prioriza: nombre o ruta exactos, artefacto solicitado, archivos afectados, tecnología demostrada, intención y términos genéricos. No actives solo por `Web`, `API`, idioma o extensión.
- Descarta entradas `legacy`, shim, deprecadas o no normativas salvo nombre/ruta exactos o migración heredada; sigue entonces su redirección canónica.
- Distingue pregunta, planificación, implementación, revisión y destrucción. Una pregunta informativa no activa `task-governance`; una decisión ya especificada no activa `implementation-decision-policy`.
- Resuelve dependencias obligatorias hasta punto fijo. Bloquea ciclos y rutas ausentes; no promociones referencias opcionales.
- Con delegación entrega a `agent-orchestration` un recibo con alcance, rutas exactas, dependencias, bloqueos y condiciones de reevaluación. Sin delegación aplica directamente la selección.

## Execution

1. Ejecuta `references/resolution-algorithm.md`.
2. Contrasta casos límite con `references/scenarios.md`.
3. Reevalúa solo ante las condiciones declaradas o nuevas señales de alcance.

## Output Contract

En flujo normal comunica como máximo `skills: [ids]`. Expande señales, motivos, rutas, dependencias, descartes y bloqueos solo ante delegación, bloqueo, ambigüedad, cambio de alcance o auditoría solicitada. Menciona `skill_resolution: none` únicamente cuando explique una decisión relevante.

## References

- `references/resolution-algorithm.md` — selección, punto fijo, fallback y recibos.
- `references/scenarios.md` — casos límite.
