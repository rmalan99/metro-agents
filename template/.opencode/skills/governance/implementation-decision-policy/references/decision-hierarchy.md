# Jerarquía de decisión

Aplica los niveles en orden. Un nivel inferior solo completa silencios; nunca contradice uno superior.

| Prioridad | Fuente                   | Uso                                                                    |
| --------- | ------------------------ | ---------------------------------------------------------------------- |
| 1         | Usuario                  | Cumple alcance, aceptación y restricciones explícitas.                 |
| 2         | Constitución y skills    | Aplica reglas acumulativas y skills especializadas.                    |
| 3         | Contratos y arquitectura | Preserva interfaces, límites y responsabilidades vigentes.             |
| 4         | Patrones repetidos       | Prefiere el patrón observable y consistente, no una excepción aislada. |
| 5         | Capacidades existentes   | Reutiliza componentes, utilidades y mecanismos disponibles.            |
| 6         | Cambio mínimo reversible | Elige la modificación segura más pequeña y fácil de deshacer.          |

## Protocolo

1. Reúne evidencia concreta por nivel: instrucciones, rutas, contratos o repeticiones verificables.
2. Descarta opciones incompatibles con cualquier nivel superior.
3. Decide sin preguntar cuando quede una opción respaldada, de bajo riesgo, reversible y compatible con el contrato.
4. Si persisten opciones equivalentes, elige la que reutilice más y cambie menos.
5. Declara todo supuesto que pueda afectar el resultado; usa el default que menos amplíe alcance, permisos o compromiso futuro.

## Escenarios

### Decidir

**Hecho:** tres módulos vecinos usan la misma utilidad existente. **Supuesto:** el nuevo caso comparte su contrato documentado. **Decisión:** reutilizarla sin crear otra abstracción. **Escalamiento:** ninguno; la evidencia es repetida, el riesgo bajo y el cambio reversible.

### Default conservador

**Hecho:** el contrato admite un parámetro opcional y no se pidió configurarlo. **Supuesto:** no hay requisito de negocio oculto que exija otro valor. **Decisión:** conservar el default vigente. **Escalamiento:** solo si la elección altera comportamiento contractual o seguridad.
