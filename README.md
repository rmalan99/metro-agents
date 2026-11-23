# Metro Agents

Distribución centralizada de configuración, prompts, herramientas y skills para OpenCode.

## Instalación y actualización

Desde cualquier directorio dentro del repositorio Git de destino, ejecuta:

```bash
curl -fsSL https://raw.githubusercontent.com/rmalan99/metro-agents/main/install.sh | bash
```

El mismo comando sirve para instalar y actualizar. No requiere Node.js ni clonar este repositorio.

El instalador:

- descarga la versión más reciente del paquete;
- copia únicamente el contenido declarado en `template/`;
- actualiza los archivos administrados sin eliminar archivos locales desconocidos;
- respalda las rutas existentes antes de modificarlas;
- deja los respaldos en `.metro-agents-backups/<fecha>-<proceso>/`.

## Instalar una versión específica

Para obtener instalaciones reproducibles, fija una etiqueta o commit:

```bash
curl -fsSL https://raw.githubusercontent.com/rmalan99/metro-agents/main/install.sh \
  | METRO_AGENTS_REF=v1.0.0 bash
```

También se puede cambiar el repositorio de origen:

```bash
curl -fsSL https://raw.githubusercontent.com/rmalan99/metro-agents/main/install.sh \
  | METRO_AGENTS_REPOSITORY=organizacion/fork METRO_AGENTS_REF=main bash
```

## Contenido distribuido

Todo archivo dentro de `template/` se copia en la raíz del repositorio destino. La estructura inicial instala:

```text
AGENTS.md
.atl/
└── skill-registry.md
.opencode/
└── skills/
    ├── governance/
    ├── frontend/
    ├── react/
    ├── data/
    ├── backend/
    ├── qa/
    └── delivery/
opencode.jsonc
```

Las skills administradas viven en grupos funcionales bajo `template/.opencode/skills/`. Las carpetas de grupo facilitan la revisión, pero el ID de cada skill sigue siendo el nombre de la carpeta que contiene su `SKILL.md`. Para publicar nuevos componentes, agrégalos bajo `template/.opencode/` manteniendo la ruta que deberán tener en los repositorios destino.

Los arquetipos frontend canónicos incluyen `backoffice-application-patterns` para plataformas administrativas y `landing-page-patterns` para páginas públicas de comunicación o conversión. Cada uno carga referencias progresivamente según la pantalla y reutiliza la librería UI detectada en el proyecto.

Toda UI nueva incorpora test IDs estables en pantallas, secciones y componentes relevantes. La validación funcional y visual usa la capacidad global `~/.agents/skills/playwright-cli/SKILL.md`; crear archivos de prueba requiere una solicitud explícita.

La capacidad `frontend-loading-performance` gobierna lazy loading de rutas, módulos, assets y datos. Solo difiere trabajo con beneficio demostrado y conserva contenido crítico, fallback, recuperación, accesibilidad y estabilidad visual.

La extensión configurable `.opencode/extensions/governance-gate` exige una tarea `ejecutando` antes de habilitar herramientas mutantes. Vive fuera de `.opencode/plugins/` para evitar la carga automática duplicada y se activa explícitamente desde `opencode.jsonc`. La configuración `.opencode/governance.json` limita a dos subagentes concurrentes; cada lanzamiento requiere un lease que el orquestador libera al terminar o interrumpir. El Manager conserva el ownership del estado y `todo.md`; el lease de un perfil `executor-*` autoriza temporalmente la mutación de código sin transferir ese ownership. Planner y Validator permanecen read-only.

El modo se controla en `opencode.jsonc` mediante `plugins[].options.orchestration.enabled`. `default_agent` permanece en `build` como fallback seguro: con `true`, una extensión cargada correctamente promueve `manager` y registra el flujo completo; con `false`, selecciona `directAgent` (por defecto `build`) y no registra gates, RPC ni UI de orquestación. Los perfiles orquestados permanecen instalados pero inactivos, mientras las skills funcionales y `usage-meter` siguen disponibles. OpenCode aplica el cambio al guardar; usa `/reload` solo para forzar una recarga completa.

El agente primario `manager` espera aprobación explícita y coordina `planner`, tres perfiles de `executor` y validadores independientes. `.opencode/model-routing.json` acepta candidatos `provider/model#variant` ordenados por rol; el gate usa únicamente candidatos y fallbacks declarados. La distribución usa `fallback: "error"` para impedir cambios silenciosos de modelo o proveedor; `inherit` queda disponible solo como opción explícita.

Un primer `FAIL` de Validator permite volver de `verificando` a `ejecutando` y lanzar un Executor nuevo con su propio lease. Solo los veredictos `FAIL` consumen el límite de correcciones fallidas; `BLOCKED` informa un impedimento de validación o infraestructura sin agotar intentos ni bloquear automáticamente la tarea.

El Planner trabaja en dos pasadas: `delivery-map` registra unidades verificables y `work-unit-detail` detalla actividades atómicas justo antes de ejecutar cada unidad. `todo.md` no se llena con pasos técnicos que no puedan aceptarse de forma independiente.

El mismo plugin incluye una extensión TUI multi-subagente. El sidebar y el footer muestran la fase actual y las plazas ocupadas; `/delivery` abre tareas, agentes, modelos, leases y relaciones Executor→Validator, y `/delivery-refresh` vuelve a leer el estado. El panel muestra actividades verificadas y estados reales, no porcentajes estimados.

El plugin local `usage-meter` agrega el consumo real almacenado por OpenCode para toda la familia de sesiones. `/usage` muestra tokens de entrada, salida, razonamiento y caché, coste por agente/modelo/tarea, coste por unidad validada y alertas de consumo. Desde el panel, `j` exporta JSON y `c` exporta CSV bajo `.opencode/usage/`; ningún dato se envía a servicios externos.

La configuración limita cada resultado de herramienta a 300 líneas o 20 KB y conserva 8.000 tokens recientes durante la compactación automática. Los agentes usan presupuestos de pasos según riesgo, filtran logs y respuestas antes de reportarlos y no repiten una validación aprobada sin evidencia contradictoria. Estos límites reducen contexto enviado al modelo; no representan ni pueden consultar el balance diario del proveedor.

## Restaurar un respaldo

Copia el contenido del respaldo elegido sobre la raíz del repositorio:

```bash
cp -a .metro-agents-backups/<respaldo>/. .
```

El instalador no elimina automáticamente los respaldos.
