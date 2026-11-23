# Datos diferidos

- Los datos esenciales para la tarea inicial cargan con la pantalla; paneles secundarios, tabs cerrados y expansiones pueden esperar.
- La primera activación deduplica solicitudes; cambios posteriores cancelan o descartan respuestas obsoletas.
- Conserva resultados válidos al volver a una sección según la política de cache existente.
- Pagina o virtualiza colecciones grandes según el contrato; lazy loading no reemplaza paginación remota.
- Prefetch de la siguiente página requiere intención o navegación probable y no puede competir con la operación actual.
- Carga, vacío, error y reintento pertenecen a la región diferida, sin bloquear acciones independientes.
- Aplica `remote-data-behavior` para identidad, cache, concurrencia e invalidación.
