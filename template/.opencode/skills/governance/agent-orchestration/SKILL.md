---
name: agent-orchestration
description: 'Trigger: delegar, coordinar, paralelizar o verificar agentes. Consume la resolución de skills y gobierna aislamiento y verificación.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.1'
---

## Activation Contract

Activa esta skill únicamente cuando exista delegación, coordinación, paralelización o verificación de trabajo de agentes. Recibe del resolver `señales`, `seleccionadas`, `dependencias`, `bloqueos` y `reevaluar_cuando`; una pregunta o tarea sin delegación no la activa.

## Hard Rules

- No selecciones skills por intuición: entrega exactamente las rutas `seleccionadas` y sus `dependencias` resueltas hasta punto fijo. Incluye `../task-governance/SKILL.md` solo cuando forme parte de ese punto fijo.
- Entrega siempre `../skill-resolution-policy/SKILL.md` para que el subagente detecte cambios de alcance y reevalúe; esto no autoriza ampliar el alcance.
- Entrega un recibo resuelto con alcance, rutas seleccionadas, dependencias y condiciones de reevaluación. El subagente confía en ese recibo al iniciar y no relee el registro completo; solo solicita nueva resolución si detecta una condición declarada o una señal nueva que cambie el alcance.
- Delega solo después de validar bloqueos y dependencias, reservar alcance, detectar trabajo ajeno y fijar aceptación y validación.
- Asigna una responsabilidad puntual por subagente, sin solapamientos. El subagente no amplía alcance, no corrige fallos ajenos y nunca modifica `todo.md`.
- Entrega directorio, resultado, comportamiento, alcance, exclusiones, comandos, salida estructurada del resolver y formato de reporte; no presupongas contexto heredado.
- Si cambian intención, artefactos, archivos o alcance, el subagente detiene el trabajo; el orquestador vuelve a resolver antes de autorizar la continuación.
- Mantén un máximo de cuatro subagentes simultáneos y, cuando sea posible, un máximo predeterminado de dos.
- Trata el reporte como insumo: el orquestador verifica personalmente antes de autorizar el cierre.

## Decision Gates

| Condición                                        | Acción                                                      |
| ------------------------------------------------ | ----------------------------------------------------------- |
| No existe delegación                             | No actives esta skill                                       |
| Resolver reporta bloqueos                        | No lances agentes; devuelve la cadena bloqueada             |
| No hay subagente disponible                      | Ejecuta sin delegar; esta skill deja de aplicar             |
| Hay dependencia, conflicto o contrato compartido | Ejecuta secuencialmente                                     |
| Independencia completa demostrada                | Paraleliza dentro de los límites                            |
| Cambia el alcance                                | Detén trabajo, vuelve al resolver y emite un contrato nuevo |
| La verificación falla                            | Mantén pendiente y no avances dependientes                  |

## Execution Steps

1. Valida la salida del resolver y detente si contiene bloqueos.
2. Reserva archivos, módulos y contratos; evalúa independencia con `references/parallelization-rules.md`.
3. Completa `assets/delegation-prompt.template.md` con el recibo compacto y exactamente sus rutas resueltas, más la ruta del resolver; no copies el registro ni cuerpos de skills en el prompt.
4. Ante una señal de cambio de alcance, pausa la asignación y vuelve a resolver antes de emitir un contrato nuevo.
5. Recibe el reporte y revisa personalmente alcance, archivos, trabajo ajeno, aceptación y validaciones.
6. Aplica `references/orchestrator-verification.md`; autoriza el cierre solo si pasa todos los gates aplicables.

## Output Contract

Reporta asignaciones, reservas, rutas entregadas, reevaluaciones, validación independiente, riesgos y bloqueos. Incluye el recibo completo solo si cambió, falló o se solicita auditoría. Confirma que ningún subagente modificó `todo.md`.

## References

- `../skill-resolution-policy/SKILL.md` — reevaluación obligatoria ante cambios de alcance.
- `assets/delegation-prompt.template.md` — contrato de instrucciones.
- `references/parallelization-rules.md` — prueba de independencia y reservas.
- `references/orchestrator-verification.md` — revisión independiente y gates de cierre.
