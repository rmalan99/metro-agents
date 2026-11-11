# Clasificación canónica de capas

## Fronteras

| Capa          | Responsabilidad observable                                | No debe                               |
| ------------- | --------------------------------------------------------- | ------------------------------------- |
| `base`        | Capacidad mínima, estable y reutilizable                  | Conocer pantallas o dominio           |
| `composed`    | Combinar bases y coordinar interacción reutilizable       | Duplicar markup o contratos base      |
| `specialized` | Resolver reglas de un módulo o flujo concreto             | Generalizar una necesidad local       |
| `layouts`     | Organizar navegación y regiones compartidas entre páginas | Incluir reglas exclusivas de una ruta |
| `pages`       | Orquestar datos, estados y composición de una pantalla    | Reimplementar piezas inferiores       |

La capa expresa responsabilidad y jerarquía, no una ruta de archivos. Una política arquitectónica puede decidir dónde vive la pieza, pero no reclasificarla.

## Escenarios de control

| Escenario                                                      | Clasificación/decisión esperada                              |
| -------------------------------------------------------------- | ------------------------------------------------------------ |
| Botón con contrato visual e interactivo estable                | `base`                                                       |
| Campo de búsqueda que combina input, icono y limpieza          | `composed`                                                   |
| Buscador con reglas exclusivas del catálogo bíblico            | `specialized`                                                |
| Cabecera y regiones compartidas por varias rutas               | `layouts`                                                    |
| Pantalla que carga datos y compone catálogo, filtros y estados | `pages`                                                      |
| Mismo contrato con densidad o tono distinto                    | Variante explícita en la capa existente                      |
| Variante que requiere reglas y estados incompatibles           | Nueva responsabilidad; reclasificar en vez de acumular flags |
| Átomo, molécula u organismo histórico                          | Evaluar responsabilidad; no traducir por nombre              |

## Comprobación

Para cada pieza, formula una frase de responsabilidad, identifica consumidores reales y verifica que dependa solo de capas inferiores necesarias. Si la clasificación cambia por la carpeta elegida, la decisión mezcla capa con ubicación y debe revisarse.
