# Responsive y librería UI

## Adaptación

| Superficie | Escritorio | Tablet | Móvil |
| --- | --- | --- | --- |
| Navegación | Sidebar persistente/colapsable | Colapsable o drawer | Drawer temporal |
| Dashboard | Grid y panel secundario | Menos columnas | Prioridad en una columna |
| Listado | Filtros y tabla completos | Menos filtros por fila; scroll interno | Búsqueda + filtros en overlay |
| Formulario | Una/dos columnas | Ajuste por contenido | Una columna |
| Detalle | Una/dos columnas | Secundario debajo | Flujo lineal |

- No causes scroll horizontal global ni comprimas contenido hasta volverlo ilegible.
- La adaptación conserva mapa de información, permisos y acciones; no crea una aplicación móvil paralela.

## Selección de componentes

1. Inspecciona dependencias, imports, tema y componentes compartidos.
2. Identifica una librería primaria y sus componentes para navegación, menús, tablas, cards, botones, campos, overlays y feedback.
3. Reutiliza componentes y tokens existentes antes de crear wrappers o primitives.
4. Carga una capacidad tecnológica específica solo con evidencia real. No adivines APIs ni instales otra librería para completar el patrón.
5. Si no hay librería, usa componentes accesibles existentes o crea el mínimo mediante `component-composition`.
6. Registra el mapeo semántico → componente elegido en el contrato de pantalla.
