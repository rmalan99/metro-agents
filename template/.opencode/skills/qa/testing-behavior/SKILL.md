---
name: testing-behavior
description: 'Trigger: pruebas Web, Vitest, Testing Library, Playwright, regresión o refactor. Decide frontera, nivel y evidencia desde comportamiento observable.'
license: Apache-2.0
metadata:
  opencode/autoinvoke: false
  author: 'mouseinyl'
  version: '1.1'
---

## Activation Contract

Activa esta skill al diseñar, implementar o revisar pruebas Web solicitadas explícitamente. Úsala como política agnóstica de runner, renderizador y navegador. Carga `../frontend-validation/SKILL.md` al ejecutar validaciones o cerrar; carga `~/.agents/skills/playwright-cli/SKILL.md` para navegador real.

## Hard Rules

- Deriva cada prueba de un contrato, riesgo o defecto observable; verifica salidas, roles, texto, navegación, efectos y estados, no detalles internos ni llamadas incidentales.
- No crees ni modifiques archivos de prueba, specs, fixtures, snapshots o baselines visuales sin una solicitud explícita del usuario. Crear un componente, pantalla, flujo o test ID no concede autorización.
- Distingue validación interactiva de test persistente: explorar un flujo, revisar una captura o comprobar criterios con Playwright no crea una suite ni obliga a guardar código generado.
- Elige la frontera más pequeña que incluya el comportamiento completo. No sustituyas una colaboración esencial por mocks para forzar una prueba unitaria.
- Usa dependencias reales baratas y deterministas. Dobla solo fronteras externas, no determinismo o fallos impracticables; simula el contrato mínimo y evita mocks globales amplios.
- Monta providers, router, permisos, estado y datos que el consumidor usa realmente. Crea builders representativos sin ocultar datos relevantes para el escenario.
- Consulta por semántica accesible y prueba teclado, foco, nombre, estado y anuncios cuando formen parte del contrato; evita selectores estructurales.
- Antes de refactorizar comportamiento incierto o defectuoso, captura una regresión que falle por la causa correcta y pase sin fijar la implementación actual.
- Incluye rutas de error, recuperación y concurrencia cuando el riesgo las haga relevantes; controla resolución, cancelación y respuestas obsoletas de forma determinista.

## Decision Gates

| Frontera necesaria                                            | Nivel                                                      |
| ------------------------------------------------------------- | ---------------------------------------------------------- |
| Regla pura, transformación o schema                           | Unidad                                                     |
| Colaboración entre componente, estado, provider o servicio    | Integración                                                |
| Navegación, plataforma, foco real o flujo crítico entre capas | Navegador                                                  |
| El nivel menor falsea el contrato                             | Sube un nivel; no multipliques mocks                       |
| Ejecuta automatización real de navegador                      | Carga `~/.agents/skills/playwright-cli/SKILL.md` |
| No existe solicitud explícita de crear pruebas                | No escribas archivos de prueba                    |
| Ejecuta validación o cierre                                   | Carga `../frontend-validation/SKILL.md`                    |

## Execution Steps

1. Identifica contrato, riesgo, regresión y resultado observable.
2. Define frontera, nivel, entorno, datos y dependencias reales o dobladas.
3. Cubre camino principal y escenarios aplicables de `references/scenarios.md`.
4. Ejecuta la verificación enfocada y conserva evidencia de que falla por el defecto cuando sea una regresión.
5. Si ejecutas validaciones o cierras, carga `../frontend-validation/SKILL.md` sin duplicar aquí sus comandos. Solo para automatización real de navegador, carga `~/.agents/skills/playwright-cli/SKILL.md`.

## Output Contract

Reporta contrato y riesgo cubiertos, nivel y frontera, providers/datos, dobles usados con justificación, escenarios y accesibilidad verificados, evidencia ejecutada y huecos pendientes.

## References

- `references/scenarios.md` — escenarios mínimos de estado, error, concurrencia, accesibilidad y navegador.
- `../frontend-validation/SKILL.md` — autoridad de comandos, batería y gate de cierre Web.
- `~/.agents/skills/playwright-cli/SKILL.md` — capacidad global condicional para automatización real de navegador.
