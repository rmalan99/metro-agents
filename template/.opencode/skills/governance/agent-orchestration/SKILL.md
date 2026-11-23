---
name: agent-orchestration
description: 'Trigger: delegar, coordinar, paralelizar o verificar agentes. Consume la resolución de skills y gobierna aislamiento y verificación.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '2.1'
---

## Activation Contract

Activa esta skill únicamente cuando `plugins[].options.orchestration.enabled` no sea `false` y exista delegación, coordinación, paralelización o verificación de trabajo de agentes. Recibe del resolver `señales`, `seleccionadas`, `dependencias`, `bloqueos` y `reevaluar_cuando`; una pregunta, una tarea sin delegación o el modo directo no la activa.

## Hard Rules

- No selecciones skills por intuición: entrega exactamente las rutas `seleccionadas` y sus `dependencias` resueltas hasta punto fijo. Incluye `../task-governance/SKILL.md` solo cuando forme parte de ese punto fijo.
- Entrega siempre `../skill-resolution-policy/SKILL.md` para que el subagente detecte cambios de alcance y reevalúe; esto no autoriza ampliar el alcance.
- Entrega un recibo resuelto con alcance, rutas seleccionadas, dependencias y condiciones de reevaluación. El subagente confía en ese recibo al iniciar y no relee el registro completo; solo solicita nueva resolución si detecta una condición declarada o una señal nueva que cambie el alcance.
- El Manager presenta un Work Brief y no lanza Planner ni ejecución hasta registrar una aprobación explícita del usuario con `governance_approval_record`.
- Delega solo después de validar bloqueos y dependencias, reservar alcance, detectar trabajo ajeno y fijar aceptación y validación.
- Asigna una responsabilidad puntual por subagente, sin solapamientos. El subagente no amplía alcance, no corrige fallos ajenos y nunca modifica `todo.md`.
- Lanza exclusivamente con `governance_agent_launch`, que resuelve perfil/modelo y adquiere el lease atómicamente; libera la sesión con `governance_agent_release` al terminar o interrumpir.
- Secuencia obligatoria: Manager → Planner → Manager registra tareas → Executor → Validator → Manager decide. PASS permite avanzar; primer FAIL crea una corrección acotada; segundo FAIL bloquea y escala al usuario.
- Selecciona `executor-fast`, `executor-standard` o `executor-deep` según riesgo. Usa `visual-validator` solo con UI y modelo/evidencia visual suficientes; en otro caso no afirmes fidelidad visual.
- Entrega directorio, resultado, comportamiento, alcance, exclusiones, comandos, salida estructurada del resolver y formato de reporte; no presupongas contexto heredado.
- Si cambian intención, artefactos, archivos o alcance, el subagente detiene el trabajo; el orquestador vuelve a resolver antes de autorizar la continuación.
- Mantén un máximo estricto de dos subagentes simultáneos, o el menor valor configurado en `.opencode/governance.json`. El agente primario no cuenta en el límite.
- Trata el reporte como insumo: el orquestador verifica personalmente antes de autorizar el cierre.
- No delegues una búsqueda, lectura o validación mecánica que el Manager pueda resolver con una consulta dirigida. Cada agente recibe solo objetivo, archivos reservados, aceptación, validación, bloqueos y rutas de skills aplicables; nunca el historial completo, el registro completo ni cuerpos de skills copiados.
- Presupuesta la validación: una comprobación estática y una prueba observable por modo o contrato afectado. No ejecutes varias interfaces para demostrar el mismo hecho ni repitas una prueba aprobada sin contradicción concreta.

## Decision Gates

| Condición                                        | Acción                                                      |
| ------------------------------------------------ | ----------------------------------------------------------- |
| No existe delegación                             | No actives esta skill                                       |
| Orquestación desactivada en `opencode.jsonc`     | No actives esta skill; ejecuta con el agente primario directo |
| Resolver reporta bloqueos                        | No lances agentes; devuelve la cadena bloqueada             |
| Work Brief no aprobado                           | Solo analiza y solicita aprobación                          |
| No hay subagente disponible                      | Ejecuta sin delegar; esta skill deja de aplicar             |
| Hay dependencia, conflicto o contrato compartido | Ejecuta secuencialmente                                     |
| Independencia completa demostrada                | Paraleliza dentro de los límites                            |
| Cambia el alcance                                | Detén trabajo, vuelve al resolver y emite un contrato nuevo |
| La verificación falla                            | Mantén pendiente y no avances dependientes                  |
| Validator falla por segunda vez                  | Bloquea y escala al usuario                                 |

## Execution Steps

1. Valida el resolver, redacta `assets/approved-work-brief.template.md`, obtiene y registra aprobación.
2. Lanza Planner en modo `delivery-map`; valida el grafo y registra solo unidades verificables sin delegar propiedad de `todo.md`.
3. Para cada unidad preparada, lanza Planner en modo `work-unit-detail`; valida actividades, reserva archivos/contratos y elige perfil/modelo con `.opencode/model-routing.json`.
4. Emite `assets/execution-work-order.template.md` con actividades atómicas y lanza un Executor mediante el gate.
5. Al terminar el Executor libera su lease y lanza Validator con `assets/validation-report.template.md`.
6. Registra el veredicto con `governance_validation_record` antes de liberar al Validator; cierra, corrige o bloquea según `references/hierarchical-flow.md`.

## Output Contract

Reporta en formato compacto: tarea; perfil/modelo; veredicto; evidencia nueva; riesgos o bloqueos. Omite reglas, alcance y resultados ya registrados salvo que hayan cambiado. Confirma que ningún subagente modificó `todo.md` y que solo PASS cerró tareas.

## References

- `../skill-resolution-policy/SKILL.md` — reevaluación obligatoria ante cambios de alcance.
- `assets/delegation-prompt.template.md` — contrato de instrucciones.
- `assets/approved-work-brief.template.md` — alcance sujeto a aprobación.
- `assets/delivery-map.template.md` — fases y unidades verificables.
- `assets/work-unit-detail.template.md` — actividades atómicas just-in-time.
- `assets/execution-work-order.template.md` — orden única por Executor.
- `assets/validation-report.template.md` — veredicto independiente.
- `references/parallelization-rules.md` — prueba de independencia y reservas.
- `references/hierarchical-flow.md` — secuencia y presupuesto de corrección.
- `references/model-routing.md` — selección de perfil, modelo, variante y fallback.
- `references/orchestrator-verification.md` — revisión independiente y gates de cierre.
