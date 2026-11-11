# Gates de escalamiento

Detente antes de modificar cuando se cumpla cualquiera de estos gates. No uses un supuesto para atravesarlos.

| Gate                           | Señal                                                                                        | Respuesta                                                                        |
| ------------------------------ | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Destrucción                    | Elimina o vuelve irrecuperables datos, recursos o trabajo ajeno.                             | Explica el impacto y solicita autorización explícita conforme a la constitución. |
| Seguridad o autorización       | Amplía permisos, expone secretos o cambia controles de acceso.                               | Detente y solicita aprobación del responsable autorizado.                        |
| Decisión de negocio            | Define política, prioridad, precio, significado o experiencia no especificada.               | Presenta opciones y pide la decisión de producto mínima.                         |
| Contrato incompatible          | Rompe una interfaz, esquema, aceptación o compatibilidad vigente.                            | No implementes; identifica el conflicto y las alternativas compatibles.          |
| Contradicción normativa        | Usuario, constitución, skills o reglas aplicables se contradicen sin precedencia resolutiva. | Cita las reglas en conflicto y solicita resolución.                              |
| Sin opción segura y reversible | Toda alternativa tiene riesgo relevante o compromiso difícil de revertir.                    | Expón riesgos y espera una elección explícita.                                   |

## Formato de escalamiento

- **Hechos:** evidencia verificable y restricciones aplicables.
- **Supuestos:** inferencias aún no confirmadas.
- **Decisión suspendida:** acción que no se ejecutará.
- **Gate y riesgo:** límite activado y consecuencia concreta.
- **Pregunta mínima:** dato o autorización indispensable para continuar.

## Escenarios

### Contrato incompatible

**Hecho:** la opción solicitada requiere cambiar una interfaz pública que el alcance ordena preservar. **Supuesto:** no existe una ruta compatible demostrada. **Decisión:** suspender la implementación. **Escalamiento:** pedir si se autoriza revisar el contrato o se prefiere una alternativa compatible.

### Seguridad

**Hecho:** continuar exige ampliar permisos. **Supuesto:** el agente no tiene autorización explícita para hacerlo. **Decisión:** no cambiar controles. **Escalamiento:** identificar permiso, recurso y responsable cuya aprobación falta.
