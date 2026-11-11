# Listados y filtros

## Orden base

1. Breadcrumb si aporta orientación.
2. Título, descripción y acción primaria.
3. Búsqueda contextual y filtros.
4. Resumen, selección masiva y utilidades reales.
5. Tabla o representación móvil.
6. Resumen de resultados y paginación.

- La búsqueda del listado no se confunde con búsqueda global.
- Escritorio: filtros visibles en una banda sin superficie decorativa innecesaria. Tablet reduce columnas. Móvil conserva búsqueda y abre filtros adicionales en drawer/dialog.
- Filtros son combinables, limpiables y sincronizados con URL si existe ese contrato; cambiar consulta valida o reinicia página/cursor.
- Columnas responden a tareas reales. Estado usa texto además de color; orden solo aparece si funciona; selección comunica si afecta página o conjunto filtrado.
- Acciones de fila frecuentes pueden ser visibles; secundarias van en menú. Destrucción exige confirmación y permisos.
- Mantén filtros y orden al paginar. Soporta cero resultados, última página parcial y página inválida tras filtrar.
- Carga inicial usa skeleton/estado estructural; refresco conserva datos válidos; consultas equivalentes pendientes no se duplican.
- En tablet permite scroll dentro del contenedor. En móvil usa tabla desplazable o patrón móvil existente, nunca overflow global.
