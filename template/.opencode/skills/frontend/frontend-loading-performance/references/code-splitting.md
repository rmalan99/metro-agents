# Code splitting

- Prefiere fronteras de ruta y feature pesada sobre divisiones por componente interno.
- Editores, gráficos, mapas, exportadores e integraciones opcionales son candidatos cuando no participan en la primera interacción.
- Mantén navegación, shell y error boundary disponibles aunque falle un chunk.
- Carga en paralelo código y datos conocidos; evita cadenas lazy donde cada módulo descubre el siguiente.
- Prefetch al hover, foco, proximidad o inactividad solo si existe intención probable, red adecuada y coste acotado.
- Nombres de chunk, imports dinámicos, SSR y preload siguen la herramienta instalada; no copies APIs de otro bundler.
- Un fallo por despliegue/versionado ofrece recarga o reintento seguro, no un spinner infinito.
