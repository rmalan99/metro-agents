# Checklist de cierre Web

## Toda tarea Web

- [ ] El resultado observable y sus límites están cubiertos.
- [ ] Consumidores e imports siguen válidos.
- [ ] No se introdujeron barrels, duplicación ni cambios ajenos.
- [ ] Pruebas existentes y aplicables pasan; no se crearon pruebas sin solicitud explícita.
- [ ] El script existente de lint pasa, si está disponible.
- [ ] El script existente de typecheck pasa, si está disponible.
- [ ] El script existente de test pasa, si está disponible y aplica.
- [ ] El script existente de build pasa, si está disponible y aplica.
- [ ] `git diff --check` pasa.

## UI

- [ ] Se aplicó la jerarquía de reutilización y se justificaron excepciones.
- [ ] Tokens, spacing, estados, teclado, foco y nombres accesibles fueron revisados.
- [ ] No existen cortes o scroll horizontal en viewports relevantes.
- [ ] Loading, error, vacío, disabled y permisos están cubiertos cuando aplican.
- [ ] Pantalla, secciones y componentes relevantes exponen test IDs estables sin instrumentar cada nodo.
- [ ] Playwright recorrió el comportamiento afectado y verificó visualmente la aceptación, o se documentó el bloqueo de entorno.
- [ ] Se revisaron consola y requests relevantes; la evidencia visual corresponde a viewports aplicables.

## Componente global

- [ ] Tiene consumidores reales y alcance global justificado.
- [ ] Catálogo actualizado con API, variantes, estados y ejemplos.
- [ ] Si el usuario pidió pruebas, cubren comportamiento y accesibilidad; en otro caso no se añadieron archivos de prueba.

## Rutas, configuración o dependencias

- [ ] Build ejecutado después del último cambio relevante.
- [ ] Navegación, fallback y carga del bundle fueron comprobados.
- [ ] Lockfile y configuración permanecen coherentes.
