# Escenarios de prueba

Selecciona solo los escenarios que pertenezcan al contrato o riesgo; no conviertas esta lista en cobertura ceremonial.

1. **Estado y datos:** representa carga inicial, éxito, vacío, datos parciales y refresco sin reemplazar el modelo real por flags imposibles.
2. **Error y recuperación:** provoca rechazo, permiso insuficiente, dato inválido o indisponibilidad en la frontera responsable; verifica mensaje, estado preservado y acción de recuperación.
3. **Concurrencia:** resuelve operaciones fuera de orden y verifica que prevalece la intención vigente; cubre cancelación, deduplicación, cola o rollback solo cuando el contrato los define.
4. **Providers:** renderiza con providers reales y configuración mínima; prueba también el fallo fuera del provider si forma parte de su contrato público.
5. **Accesibilidad:** opera por rol y nombre; verifica teclado, foco, estado accesible y anuncios dinámicos pertinentes, no solo presencia visual.
6. **Navegador:** reserva el entorno real para navegación crítica, integración con plataforma, layout/foco que el DOM simulado no representa o un flujo cuya confianza depende de varias capas.
7. **Regresión:** reproduce primero el defecto con la entrada mínima; demuestra fallo previo o equivalente controlado y evita expectativas sobre estructura privada.
8. **Evidencia:** registra escenario, nivel, resultado y limitaciones. Un snapshot o cobertura porcentual no demuestra por sí solo el comportamiento.
