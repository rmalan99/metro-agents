# Mapa de entrega

```yaml
mode: delivery-map
objective: <Work Brief aprobado>
phases:
  - id: phase-1
    result: <resultado comprobable>
    units:
      - id: WEB-001
        result: <resultado observable e independiente>
        scope: []
        depends_on: []
        parallelizable_with: []
        acceptance: []
        validation: []
        risks: []
ready_units: []
blocked_units: []
scope_discoveries: []
```

Registra como unidad solo el resultado más pequeño que pueda aceptarse y validarse independientemente. No incluyas actividades internas en `todo.md`.
