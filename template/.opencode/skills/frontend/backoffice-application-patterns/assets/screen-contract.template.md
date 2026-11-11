# Contrato de pantalla administrativa

```yaml
screen: <id>
route: <ruta>
pattern: <dashboard|listing|detail|form|auth>
goal: <tarea del usuario>
permissions: []
primary_action: <acción|null>
secondary_actions: []
data_source: <contrato existente>
states: [initial-loading, refreshing, empty, error, forbidden, success]
ui_library: <detectada>
component_mapping: {}
responsive:
  desktop: <composición>
  tablet: <adaptación>
  mobile: <adaptación>
references_loaded: []
exceptions: []
```
