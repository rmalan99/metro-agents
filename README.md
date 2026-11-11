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

## Restaurar un respaldo

Copia el contenido del respaldo elegido sobre la raíz del repositorio:

```bash
cp -a .metro-agents-backups/<respaldo>/. .
```

El instalador no elimina automáticamente los respaldos.
