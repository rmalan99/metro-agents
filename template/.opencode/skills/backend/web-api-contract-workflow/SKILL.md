---
name: web-api-contract-workflow
description: 'Trigger: contrato Web/API, integración frontend backend, endpoint, fixture o cambio transversal. Define y protege el contrato antes de implementar consumidores.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.0'
---

## Activation Contract

Activa esta skill cuando una funcionalidad afecta Web y API, modifica un contrato consumido remotamente o requiere coordinación entre responsables independientes.

## Hard Rules

- Para planificar, registrar, ejecutar, verificar o cerrar las tareas del contrato, carga `../../governance/task-governance/SKILL.md`.
- Solo si delegas, coordinas o paralelizas trabajo entre agentes, carga además `../../governance/agent-orchestration/SKILL.md`.
- Estas rutas son dependencias obligatorias bajo su condición. Las rutas de `References` son informativas y no activan otras skills.
- Separa siempre contrato, implementación API, implementación Web y validación integral en tareas distintas.
- Aprueba el contrato antes de iniciar consumidores. Ningún agente lo modifica unilateralmente.
- Define operación, transporte, autenticación, permisos, entrada, salida, errores, compatibilidad y ejemplos.
- Web y API solo avanzan en paralelo con contrato estable, archivos separados, sin dependencia del resultado contrario y con fixtures/dobles para validación aislada.
- La API posee filtrado, búsqueda, orden y paginación remotos; Web envía la consulta y representa la respuesta.
- Un cambio de contrato detiene consumidores afectados, reabre impacto y exige revalidación por ámbito e integración.
- La integración nunca sustituye las validaciones Web y API independientes.

## Decision Gates

| Situación                           | Decisión                           |
| ----------------------------------- | ---------------------------------- |
| Contrato sin aprobar                | No implementar consumidores        |
| Web/API independientes con fixtures | Pueden paralelizarse               |
| Contrato o prueba compartida cambia | Ejecutar secuencialmente           |
| Cambio incompatible                 | Expansión, migración y contracción |

## Execution Steps

1. Crea la tarea transversal del contrato y define ejemplos de éxito/error.
2. Aprueba responsabilidades exclusivas, compatibilidad y fixtures.
3. Crea tareas API y Web separadas con dependencias explícitas.
4. Valida cada ámbito de forma aislada.
5. Ejecuta integración y verifica observabilidad, errores y compatibilidad.

## Output Contract

Reporta contrato aprobado, tareas/dependencias, responsables, fixtures, estrategia de compatibilidad y evidencia Web, API e integral.

## References

- `references/contract-template.md` — campos y secuencia normativa del contrato.
