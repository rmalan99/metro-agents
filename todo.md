# TODO

- [x] **TRV-001 — Mostrar el estado multi-subagente en la TUI**
  - Estado: completada
  - Ámbito: Web
  - Alcance: Extender governance-gate con estado estructurado, RPC y contribuciones TUI para sidebar, footer y panel de entrega.
  - Criterios de aceptación: Mostrar tareas, agentes activos, modelos, leases, validación, correcciones y capacidad 2/2 sin porcentajes ficticios.
  - Validación: Sintaxis del plugin, contratos RPC, configuración JSON, instalador y diff.
  - Responsable: Orquestador
  - Evidencia: RPC real respondió estado estructurado; TUI real mostró `ENTREGA Implementando · 0/2`; TS/JSON/bash/diff y bundle TSX válidos.

- [x] **TRV-002 — Medir consumo local por sesión, agente y tarea**
  - Estado: completada
  - Ámbito: Web
  - Alcance: Crear usage-meter con agregación local de tokens/coste, atribución de gobierno, panel TUI y exportación JSON/CSV.
  - Criterios de aceptación: Mostrar consumo real por familia, perfil, modelo y tarea; calcular coste por unidad validada; no estimar datos ausentes ni enviar telemetría externa.
  - Validación: RPC real, carga TUI, exportación local, sintaxis TypeScript/TSX, JSON, instalador y diff.
  - Responsable: Orquestador
  - Evidencia: Plugin activo en OpenCode V2; RPC real atribuyó sesión/agente/modelo/tarea; exportaciones JSON/CSV reales; TUI cargó sin errores; TS/TSX/JSON/bash/diff válidos.

- [x] **TRV-003 — Alternar orquestación desde OpenCode**
  - Estado: completada
  - Ámbito: Web
  - Alcance: Incorporar un selector en `opencode.jsonc` que active el flujo Manager/Planner/Executor/Validator o use un agente primario directo sin retirar las skills funcionales ni `usage-meter`.
  - Criterios de aceptación: Un único valor de configuración selecciona ambos modos; `build` queda como fallback si la extensión falla; el modo directo no registra gates, RPC ni UI de orquestación; las skills describen correctamente el fallback directo.
  - Validación: Configuración JSONC, tipos/sintaxis del plugin, comportamiento de ambos modos, instalador y diff enfocado.
  - Responsable: Agente primario
  - Evidencia: Ambos valores fueron cargados por OpenCode V2 desde copias aisladas; la extensión se cargó una sola vez fuera del descubrimiento automático, `build` quedó como fallback base, y los bundles TS/TSX, JSON, Bash y diff pasaron validación.

- [x] **TRV-004 — Reducir consumo de contexto y validación**
  - Estado: completada
  - Ámbito: Web
  - Alcance: Limitar resultados de herramientas, compactar sesiones largas, reducir ciclos máximos y exigir consultas y reportes enfocados en los flujos directo y orquestado.
  - Criterios de aceptación: La configuración acota outputs; los agentes evitan documentos/logs completos, validaciones duplicadas y reportes repetitivos; los límites de pasos conservan margen según riesgo.
  - Validación: Configuración OpenCode V2, frontmatter de agentes, JSONC, carga de agentes y diff enfocado.
  - Responsable: Agente primario
  - Evidencia: OpenCode V2 cargó límites de 300 líneas/20 KB, compactación con retención de 8.000 tokens y buffer de 20%; los siete perfiles cargaron los nuevos presupuestos de pasos; bundle, Bash y diff pasaron validación.

- [x] **TRV-005 — Corregir fallback heredado de modelos**
  - Estado: completada
  - Ámbito: Web
  - Alcance: Distinguir un fallback explícito y válido a `inherit` de una ruta de modelos realmente irresoluble.
  - Criterios de aceptación: `planner → manager → inherit` puede lanzar el agente; perfiles o fallbacks ausentes siguen bloqueando cuando `strict` está activo.
  - Validación: Bundle TypeScript y casos dirigidos de resolución disponibles, heredados e irresolubles.
  - Responsable: Agente primario
  - Evidencia: `planner → manager → inherit` resolvió como herencia válida; un modelo disponible conservó su referencia y un fallback ausente quedó marcado como irresoluble. Bundle TypeScript y diff pasaron validación.

- [x] **TRV-006 — Endurecer leases y transiciones del gate**
  - Estado: completada
  - Ámbito: Web
  - Alcance: Vincular mutaciones a la sesión propietaria, recuperar leases obsoletos, validar transiciones y aplicar `requireAgentLease`.
  - Criterios de aceptación: Una sesión no puede mutar tareas ajenas; leases de sesiones inexistentes se liberan al iniciar; saltos de estado inválidos se rechazan; los subagentes sin lease no reciben herramientas mutantes.
  - Validación: Bundle TypeScript, diff y casos dirigidos de routing/estado.
  - Responsable: Agente primario
  - Evidencia: Manager y Executor con lease resolvieron la misma tarea activa; una sesión ajena quedó bloqueada; OpenCode cargó Manager/Planner; bundle TypeScript y `git diff --check` pasaron. La migración reclama tareas sin propietario solo desde una sesión aprobada y los leases terminales se reconcilian según outcome.

- [x] **TRV-007 — Hacer autoritativo el routing configurado**
  - Estado: completada
  - Ámbito: Web
  - Alcance: Usar únicamente candidatos y fallbacks declarados, sin heredar silenciosamente otro proveedor.
  - Criterios de aceptación: `fallback: error` bloquea si ningún candidato funciona; `inherit` y perfiles alternos solo se usan cuando están explícitos; el error explica cada descarte.
  - Validación: Bundle TypeScript, configuración JSON y casos dirigidos de candidato, variante, herencia y error.
  - Responsable: Agente primario
  - Evidencia: OpenCode V2 expuso los candidatos OpenAI configurados con variantes y tools; el resolver acepta respuestas planas o `{data}`, valida strings/objetos de variante y bloquea con `fallback: error`. Bundle TypeScript, JSON y `git diff --check` pasaron.
