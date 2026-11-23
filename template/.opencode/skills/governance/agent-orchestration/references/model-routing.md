# Enrutamiento de modelos

El Manager elige primero el perfil por riesgo; `governance_agent_launch` resuelve después el primer candidato disponible de `.opencode/model-routing.json`.

| Perfil | Uso |
| --- | --- |
| planner | Descomposición y dependencias |
| executor-fast | Cambio mecánico, pequeño y reversible |
| executor-standard | Implementación normal localizada |
| executor-deep | Contratos compartidos, concurrencia o migración |
| validator | Validación funcional independiente |
| visual-validator | UI con evidencia visual y modelo con visión |

- Todos los candidatos necesitan herramientas; visual-validator necesita entrada de imagen.
- Usa referencias exactas `provider/model#variant`. No inventes modelos ni variantes.
- `fallback: "error"` bloquea si ningún candidato declarado funciona; es el valor seguro para exigir exactamente la configuración.
- `fallback: "inherit"` hereda el modelo de la sesión y puede cambiar de proveedor; úsalo solo cuando esa herencia sea intencional.
- Un fallback a otro perfil sigue únicamente la lista declarada por ese perfil y bloquea ciclos.
- Cada descarte informa referencia inválida, modelo ausente/deshabilitado/deprecado, variante o capacidad faltante, o exclusión por independencia.
- Para Validator, prefiere un modelo distinto del Executor cuando exista candidato suficiente; registra si no fue posible.
- Cambiar a un perfil de mayor coste o un proveedor no autorizado requiere aprobación si altera el Work Brief.
- El recibo conserva perfil, modelo real, fallback y motivo.
