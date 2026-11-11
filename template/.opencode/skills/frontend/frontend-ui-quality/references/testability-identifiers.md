# Identificadores de testabilidad

Instrumentar testabilidad no autoriza crear archivos de prueba.

## Cobertura obligatoria

Añade `data-testid` estable a:

- raíz de cada pantalla o componente relevante;
- secciones funcionales que un flujo deba localizar;
- componentes compartidos y controles de flujo ambiguos;
- estados o contenedores cuya semántica accesible no baste para identificarlos.

No lo añadas a wrappers de layout, iconos decorativos ni cada nodo del DOM.

## Nombres

Usa kebab-case orientado al dominio:

```text
users-list-page
users-list-filters
users-list-table
user-form-drawer
user-form-submit
account-menu-trigger
logout-action
```

- No codifiques clases CSS, estructura DOM, índices, texto traducible, valores aleatorios ni secretos.
- El identificador permanece estable ante cambios visuales.
- En colecciones, prefiere rol/nombre y contexto. Usa una clave pública estable solo cuando el flujo necesite distinguir una instancia; no expongas identificadores sensibles.
- Un componente reutilizable acepta y propaga `data-testid` o una prop equivalente sin imponer un valor duplicado a todas sus instancias.

## Selectores

Al automatizar, prioriza rol, label y texto accesible. Usa test ID para límites estructurales, componentes custom o controles ambiguos. No reemplaces accesibilidad deficiente con un test ID.
