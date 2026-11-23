# Detalle just-in-time de unidad

```yaml
mode: work-unit-detail
task: WEB-001
result: <resultado observable ya aprobado>
readiness:
  dependencies_validated: true
  scope_unchanged: true
profile_recommendation: executor-standard
allowed_files: []
excluded_files: []
contracts: []
skills: []
activities:
  - id: A1
    action: <acción atómica>
    produces: <evidencia o cambio>
  - id: A2
    action: <acción siguiente>
    produces: <evidencia o cambio>
acceptance: []
validation: []
risks: []
reevaluate_when: []
```

Las actividades pertenecen a una sola orden de Executor. Promueve una actividad a nueva unidad únicamente si produce un resultado aceptable por sí mismo y cambia dependencias, propietario, ámbito o validación.
