# Calidad UI normativa

## Espaciado y composición

- Usa tokens del tema. En APIs de estilo, prefiere propiedades de composición y breakpoints del sistema sobre píxeles o media queries duplicadas.
- Mantén componentes sin márgenes externos; el padre decide la separación entre piezas.
- Procura áreas táctiles mínimas de `44 × 44 px`.

## Accesibilidad

- Todo control tiene nombre accesible. Asocia label, descripción y error mediante los mecanismos semánticos de la plataforma.
- Mantén foco visible, orden lógico y navegación completa por teclado.
- Menús y diálogos gestionan foco, Escape y restauración al activador cuando corresponda.
- Los iconos decorativos se ocultan de tecnologías asistivas; botones con solo icono reciben nombre contextual.
- No comuniques estado únicamente mediante color; combina texto, forma, icono o semántica.

## Estados

Define explícitamente cuando apliquen:

- carga y progreso;
- éxito o confirmación;
- vacío y cero resultados;
- error recuperable y no recuperable;
- disabled y loading interactivo;
- sin permisos y no disponible.

Cada estado conserva contexto y ofrece la siguiente acción posible. Los formularios muestran errores junto al campo y conservan valores válidos.

## Responsive y movimiento

- Verifica móvil y escritorio; añade tablet cuando la composición cambie.
- Prohíbe scroll horizontal accidental, contenido cortado y controles fuera del viewport.
- Las animaciones son breves y explican transición o causalidad; respeta `prefers-reduced-motion`.
- Revisa cambios visuales globales en el catálogo de desarrollo, no en navegación productiva.

## Iconografía

- Usa solo `@tabler/icons-react` para iconos de interfaz.
- Verifica primero si Tabler contiene una alternativa adecuada.
- Conserva tamaño, contraste, estado y nombre accesible del control.
- Logotipos, isotipos e ilustraciones de marca no se consideran iconos de interfaz.
