# Formularios administrativos

## Elección del contenedor

| Situación | Patrón |
| --- | --- |
| Formulario largo, enlazable o multisección | Página |
| Alta/edición breve conservando contexto | Side form/drawer |
| Acción corta y atómica | Dialog |
| Confirmación o destrucción | Dialog de confirmación |

- Estructura: título/contexto, secciones lógicas, campos, error global y acciones finales.
- Labels son visibles; ayuda y error se asocian al control. Placeholder no sustituye label.
- Grid de hasta dos columnas en escritorio cuando mejora lectura; móvil usa una. Campos compuestos ocupan el ancho necesario.
- Acción primaria describe el resultado; cancelar no descarta silenciosamente cambios. Advierte cambios sin guardar cuando exista pérdida real.
- Submit pendiente muestra progreso, impide duplicados y conserva valores. Error de campo es inline; error global ofrece recuperación.
- Fechas, teléfonos, rangos, mapas y archivos usan componentes/infraestructura existentes; no inventes servicios, máscaras ni reglas de negocio.
- Side form y dialog manejan foco, Escape seguro, scroll interno y retorno de foco. Formularios que ya no caben cómodamente migran a página.
