# Escenarios de verificación

Valida con dobles o pruebas observables, sin acoplar la expectativa a una librería:

1. Dos consultas semánticamente iguales producen una sola identidad aunque cambie el orden incidental de filtros; permisos, orden o página distintos producen identidades distintas.
2. Una mutación de detalle mantiene coherentes detalle, listas y agregados afectados, sin revalidar dominios ajenos.
3. Al cambiar búsqueda, filtros u orden, la paginación reinicia o usa un cursor válido y no presenta resultados anteriores como actuales.
4. Si responde primero una solicitud antigua, su resultado no reemplaza la intención vigente; la cancelación alcanza el transporte cuando este la soporta.
5. Carga inicial, refresco con datos, vacío, error recuperable y éxito parcial tienen representaciones distinguibles y no borran datos válidos prematuramente.
6. Un fallo tras actualización optimista restaura exactamente cache y UI previas; la confirmación remota reconcilia identificadores, versiones y valores autoritativos.
7. Un request serializa y transporta, un service expresa la operación remota y un hook coordina cache/estado; ningún componente ejecuta transporte directamente.
8. Un doble clic o activación repetida de un submit pendiente produce una sola mutación; el control recupera su disponibilidad tanto en éxito como en error.
9. Cambios rápidos de búsqueda o filtros no presentan resultados intermedios como vigentes: se agrupan cuando corresponde y las operaciones obsoletas se cancelan o descartan.
10. Solicitar repetidamente la misma página mientras está pendiente no duplica transporte; una página o acción independiente no queda bloqueada sin necesidad.
11. Una carga inicial comunica espera antes de tener datos; un refresco conserva datos válidos con progreso no bloqueante; una mutación indica exactamente qué acción está pendiente.
12. Tras error o cancelación, el indicador termina, los controles aplicables se rehabilitan y existe una acción de reintento sin duplicar solicitudes residuales.
