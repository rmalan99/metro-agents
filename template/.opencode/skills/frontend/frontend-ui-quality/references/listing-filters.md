# Filtros responsive de listados

- No encierres filtros en `Card` o `Paper`.
- En escritorio, reserva cinco columnas para filtros; en tablet, tres.
- En móvil muestra el buscador y, únicamente si existen filtros adicionales, un botón de filtros.
- Presenta filtros adicionales móviles en `Dialog` o `Drawer` accesible.
- Si solo existe búsqueda, no muestres el botón de filtros.
- Conserva valores al abrir/cerrar, expón limpieza/aplicación cuando corresponda y restaura foco al activador.
- El filtrado remoto pertenece al contrato Web/API; esta referencia solo define presentación e interacción.
