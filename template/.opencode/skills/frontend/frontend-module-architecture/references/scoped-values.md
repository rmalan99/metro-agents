# Valores por alcance

Esta referencia desarrolla las reglas normativas de `../SKILL.md`; no crea una autoridad adicional.

## Clasificación y ubicación

| Clasificación                                 | Señal verificable                      | Ubicación                          |
| --------------------------------------------- | -------------------------------------- | ---------------------------------- |
| Dominio, catálogo o configuración transversal | Tiene consumidores en varios módulos   | `src/app/shared/models`            |
| Dominio, catálogo o configuración de módulo   | Solo pertenece al dominio de un módulo | `src/app/features/<module>/models` |
| Valor de operación no dominial                | Solo interviene en una operación       | Junto a la operación               |
| Estilo local, ID temporal o valor de render   | Solo sirve a la presentación local     | Junto al consumidor                |

Un submódulo conserva sus modelos en su propio `models` cuando no forman parte del contrato del padre. Si padre e hijos comparten el modelo, ubícalo en la frontera compartida del módulo; no hagas que un hijo importe internals de otro.

## Gate de extracción

Antes de extraer, identifica tipo, alcance, consumidores y fuente de verdad; busca definiciones existentes y compara el costo de archivos, imports, props e indirección con el beneficio. Extrae solo si existe al menos una frontera útil:

- varios consumidores reales;
- comportamiento complejo encapsulado;
- una fuente de verdad compartida;
- una convención de rutas que elimina duplicación real.

Si no existe esa frontera, conserva la definición local. No crees layouts, wrappers, hooks, componentes ni archivos únicamente para reducir unas pocas líneas.

## Escenarios de verificación

1. Un catálogo consumido por dos módulos se resuelve en `app/shared/models`; ningún módulo se convierte en propietario accidental.
2. Una configuración usada solo por facturación se resuelve en `features/billing/models`, aunque tenga varios consumidores internos.
3. Un ID temporal usado por un componente permanece junto al componente y no se publica como modelo.
4. Un modelo compartido por dos submódulos se eleva a la frontera del padre; no se crea un import hermano ni un ciclo.
5. Una constante de una sola petición permanece junto a esa operación si no expresa dominio.

En cada movimiento, actualiza imports directos, revisa todos los consumidores y preserva tipos, contratos e inmutabilidad. No uses barrels.
