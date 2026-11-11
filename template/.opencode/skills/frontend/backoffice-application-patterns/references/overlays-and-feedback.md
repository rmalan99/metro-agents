# Overlays y feedback

| Evento | Patrón |
| --- | --- |
| Éxito no bloqueante | Feedback breve o inline |
| Información contextual | Alert inline |
| Error de campo | Mensaje junto al campo |
| Fallo global recuperable | Alert persistente o dialog si exige decisión |
| Acción irreversible | Dialog de confirmación |
| Edición breve contextual | Side form o dialog según espacio |

- Un toast temporal no es la única explicación de un fallo bloqueante.
- Dialogs nombran objeto, consecuencia y acciones explícitas; no usan confirmación implícita al cerrar.
- Reintentar exige callback real, muestra progreso e impide duplicados.
- Overlays manejan título accesible, foco inicial, teclado, Escape seguro y retorno de foco.
- No uses alertas nativas ni modales improvisados cuando existe un componente de la librería.
