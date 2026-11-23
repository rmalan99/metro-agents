# Assets y contenido multimedia

- Imagen principal, logo y contenido visual necesario para comprender el primer viewport se priorizan.
- Imágenes inferiores pueden usar carga nativa diferida y `srcset`/sizes equivalentes disponibles.
- Reserva ancho, alto o aspect ratio para evitar layout shift.
- Video, iframe, mapa y visualización pesada cargan tras intención, proximidad o consentimiento cuando corresponda.
- Placeholder representa el espacio y ofrece acción accesible; no simula que el recurso ya está disponible.
- Respeta texto alternativo, reduced motion, formatos soportados y fallos de recurso.
- No uses lazy loading para ocultar assets sin optimizar o descargar luego variantes innecesarias.
