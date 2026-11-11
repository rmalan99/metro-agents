# Checklist de creación y auditoría

## Precondiciones

- [ ] El modo es `crear` o `auditar`; ámbito, objetivo y fuentes están declarados.
- [ ] La ruta `./.opencode/skills/governance/skill-resolution-policy/SKILL.md` fue resuelta y leída.

## Bootstrap constitucional

- [ ] `AGENTS.md` contiene solo precedencia, alcance, seguridad y la ruta obligatoria del resolver.
- [ ] No contiene catálogo, matriz, propietarios, triggers, dependencias ni procedimientos especializados.
- [ ] La precedencia y el efecto de constituciones anidadas son inequívocos.
- [ ] La plantilla no presupone tecnología, dominio, herramienta o estructura adicional.

## Sistema externo

- [ ] El registro permanece fuera de `AGENTS.md` y funciona solo como índice de metadata y rutas.
- [ ] El resolver clasifica señales, selecciona skills, resuelve dependencias hasta punto fijo y reevalúa cambios de alcance.
- [ ] Cada skill declara activación, reglas, decisiones, ejecución, salida y dependencias obligatorias.
- [ ] Rutas ausentes y ciclos producen bloqueos; no se inventan sustitutos.
- [ ] Ninguna comprobación exige listar propietarios en `AGENTS.md`.

## Gates por modo

### Crear

- [ ] Completa la plantilla solo si el resolver existe y no hay bloqueos.
- [ ] Sustituye todos los marcadores; no publica ejemplos como hechos.

### Auditar

- [ ] Separa evidencia, hallazgo, severidad y corrección propuesta.
- [ ] No modifica archivos salvo solicitud explícita y alcance autorizado.
- [ ] Clasifica el resultado como `bloqueado`, `no conforme` o `conforme`.

## Bloqueos

Bloquea conformidad si falta el resolver, una dependencia obligatoria o existe un ciclo. Marca como no conforme todo catálogo, matriz o procedimiento embebido, o cualquier router, registro o skill que dependa de contenido retirado de `AGENTS.md`.
