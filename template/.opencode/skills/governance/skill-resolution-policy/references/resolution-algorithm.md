# Algoritmo de resolución

## Entrada y clasificación

1. Lee la solicitud, las instrucciones superiores y, si ya existen, el plan y la lista de archivos objetivo.
2. Clasifica la intención primaria como `pregunta_informativa`, `planificación`, `implementación`, `revisión` u `operación_destructiva`.
3. Extrae señales verificables en cuatro grupos:
   - petición: verbos, tecnologías, comportamientos y restricciones explícitas;
   - artefactos: componente, prueba, migración, pipeline, constitución u otro resultado nombrado;
   - archivos: rutas, extensiones y directorios objetivo;
   - contexto: herramientas o plataformas identificadas, sin inferirlas de `Web` o `API` por sí solos.
4. Ordena evidencia por precedencia: nombre o ruta exactos, artefacto solicitado, archivos afectados, tecnología demostrada, intención y términos genéricos. Resuelve empates con la fuente más concreta y registra ambigüedad solo si cambia la selección.

## Selección por registro

1. Si `.atl/skill-registry.md` existe, lee únicamente su metadata de selección: nombre, trigger/description, scope y ruta. No leas todos los cuerpos.
2. Compara cada entrada con señales concretas. Conserva coincidencias explicables y registra como descartadas solo las alternativas cercanas que ayuden a auditar la decisión.
3. Antes de seleccionar, descarta entradas cuya metadata indique `shim`, `deprecated`/`deprecada` o `normative: false`/`no normativa`. Permite cargarlas únicamente si el usuario nombra exactamente la skill o su ruta, o si un artefacto heredado exige migración. En ese caso, no las trates como autoridad: lee el shim y sigue sus redirecciones canónicas como dependencias obligatorias.
4. Si dependencias o archivos inspeccionados demuestran uso real de MUI, busca entre capacidades instaladas una coincidencia MUI declarada en metadata. Si no existe, reporta `capacidad MUI ausente`; no cargues referencias heredadas de un shim ni inventes una ruta.
5. Aplica los gates por intención:
   - una pregunta conceptual no activa `task-governance` salvo que también pida planificar, registrar, ejecutar, verificar o cerrar trabajo;
   - planificación, implementación y revisión activan contratos cuyos triggers coincidan con la acción o artefacto;
   - una operación destructiva conserva todas las coincidencias específicas y exige los gates de seguridad superiores;
   - `implementation-decision-policy` entra únicamente si implementar requiere elegir un detalle técnico que las instrucciones y contratos no fijan.
6. No uses `Web`, `API`, el idioma, el nombre del repositorio ni una extensión aislada como prueba suficiente de dominio.

## Dependencias y punto fijo

1. Lee el `SKILL.md` de cada coincidencia seleccionada.
2. Extrae solo dependencias declaradas como obligatorias por ruta o contrato inequívoco. Registra la arista `origen → dependencia` y lee cada dependencia nueva.
3. Repite extracción y carga hasta que una iteración no añada rutas.
4. Mantén un conjunto de rutas visitadas y una pila activa. Si una ruta reaparece en la pila, bloquea con el ciclo completo. Si una ruta obligatoria no existe o no puede leerse, bloquea con origen y ruta ausente.
5. No conviertas referencias informativas, recomendaciones opcionales o ejemplos en dependencias.

## Fallback sin registro

Si el registro falta o no puede leerse, busca recursivamente solo archivos `.opencode/skills/**/SKILL.md`, hasta seis niveles bajo la raíz de skills, y escanea únicamente su frontmatter junto con la metadata ya disponible de capacidades instaladas conocidas. Selecciona por `name` y `description`, aplicando también el descarte de shims, entradas deprecadas o no normativas; no cargues cuerpos hasta tener coincidencias. Reporta el fallback. No recorras directorios globales ni inventes capacidades.

## Reevaluación y entrega

Reejecuta desde clasificación cuando cambien la petición, el artefacto, los archivos objetivo, la tecnología, el ámbito o la naturaleza destructiva. Añade y retira skills según la nueva evidencia, vuelve a alcanzar el punto fijo y no continúes con una selección obsoleta.

Si existe delegación o coordinación, entrega a `agent-orchestration` un recibo estable con alcance, rutas exactas seleccionadas y dependencias, bloqueos y condiciones de reevaluación. Sin delegación, aplica la selección y comunica como máximo `skills: [ids]`. Expande señales, motivos, aristas y descartes solo ante bloqueo, ambigüedad, cambio de alcance o auditoría solicitada. Con selección vacía, procede bajo instrucciones superiores y menciona `skill_resolution: none` solo cuando explique una decisión relevante.
