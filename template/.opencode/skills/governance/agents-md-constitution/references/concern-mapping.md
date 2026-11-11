# Separación y autosuficiencia

## Fuentes admisibles

Revisa evidencia local: `AGENTS.md`, la ruta del resolver, el registro y los `SKILL.md` seleccionables. No deduzcas rutas ni contratos por nombres de carpetas.

## Fronteras

| Pieza       | Debe contener                                                 | No debe depender de `AGENTS.md` para      |
| ----------- | ------------------------------------------------------------- | ----------------------------------------- |
| `AGENTS.md` | Precedencia, alcance, seguridad y ruta del resolver           | Catálogo, matriz, triggers o dependencias |
| Resolver    | Clasificación, selección, punto fijo, bloqueos y reevaluación | Filas de activación embebidas             |
| Registro    | Metadata de selección y rutas exactas                         | Reglas operativas o resúmenes normativos  |
| Skills      | Trigger, reglas, decisiones, ejecución, salida y dependencias | Un propietario listado en la constitución |

## Comprobación

1. Verifica que `./.opencode/skills/governance/skill-resolution-policy/SKILL.md` exista y pueda leerse.
2. Comprueba que el resolver pueda localizar el registro o aplicar su fallback declarado.
3. Muestrea entradas del registro: cada ruta debe resolver a una skill autosuficiente y su metadata debe permitir selección.
4. Recorre dependencias obligatorias hasta punto fijo; bloquea rutas ausentes y ciclos.
5. Confirma que cambios de intención, artefactos, archivos o alcance disparen reevaluación.

## Defectos

- **Bootstrap duplicado:** `AGENTS.md` contiene catálogo, matriz, triggers o procedimientos.
- **Ruta ausente:** el resolver obligatorio no se puede leer; bloquea creación y conformidad.
- **Índice normativo:** el registro replica reglas en vez de indexar metadata y rutas.
- **Skill incompleta:** necesita reglas copiadas en `AGENTS.md` para activarse u operar.
- **Resolución incompleta:** no hay punto fijo, detección de ciclos/rutas ausentes o reevaluación por cambio de alcance.
