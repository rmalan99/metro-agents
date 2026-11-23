# Orden de ejecución

```yaml
task: WEB-001
goal: <resultado observable>
profile: executor-standard
model: <modelo resuelto o inherit>
allowed_files: []
excluded_files: []
depends_on: []
skills: []
activities:
  - id: A1
    action: <acción atómica ordenada>
    produces: <evidencia esperada>
acceptance: []
validation: []
correction_round: 0
```

El Executor completa las actividades como una sola unidad. No crea tareas nuevas ni cambia el Work Brief; reporta al Manager cualquier descubrimiento que requiera replanificación.
