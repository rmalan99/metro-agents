necesito un ui kit sistem donde se muestre y si incluya la composision visual de los componente, spacions, tipos de input, select, alert, modals, forms, sidebar, appbars, estrutura visual moviles, cards, fontsising, tipos de fuentes, iconos, tamaños de iconos, button, tootils, bordes, colores y variantes de colores, necitaria algo que incluya todo los necesesario para no volver a solicitar ui base 

En este caso sera enfocado para un backoffices

Procesó durante 17s
Lo estructuraría como un Backoffice UI System, pensado para convertirse en la única referencia visual del proyecto. No sería únicamente una librería de botones, inputs y modales: también definiría cómo se combinan para construir formularios, tablas, dashboards, CRUD, configuraciones y vistas móviles.

Backoffice UI System — Base v1
1. Foundations
Esta capa nunca depende de una pantalla específica.

Grid y spacing
Usaría una base de 4 px, con prioridad visual en múltiplos de 8.

Token	Tamaño	Uso
space-0	0	Sin espacio
space-1	4px	Separaciones mínimas
space-2	8px	Icono ↔ texto
space-3	12px	Elementos internos
space-4	16px	Spacing estándar
space-5	20px	Formularios
space-6	24px	Cards / secciones
space-8	32px	Secciones grandes
space-10	40px	Separación estructural
space-12	48px	Bloques de página
space-16	64px	Grandes divisiones
Bordes
Token	Valor
radius-xs	4px
radius-sm	6px
radius-md	8px
radius-lg	12px
radius-xl	16px
radius-full	9999px
Estándar recomendado para backoffice:

Inputs: 8px
Buttons: 8px
Cards: 12px
Modals: 12–16px
Badges: full

2. Tipografía
Recomendaría Inter como fuente principal.

Display
32 / 40 / 600

H1
28 / 36 / 600

H2
24 / 32 / 600

H3
20 / 28 / 600

H4
18 / 26 / 600

Body LG
16 / 24 / 400

Body
14 / 20 / 400

Body Medium
14 / 20 / 500

Small
13 / 18 / 400

Caption
12 / 16 / 400

Overline
11 / 16 / 600
En backoffice evitaría abusar de fuentes grandes. La mayoría de la UI debería moverse entre 12–16 px.

3. Colores
No trabajaría directamente con colores hexadecimales en los componentes. Utilizaría tokens semánticos.

Primary
Variante	Color
50	#EFF6FF
100	#DBEAFE
200	#BFDBFE
300	#93C5FD
400	#60A5FA
500	#3B82F6
600	#2563EB
700	#1D4ED8
800	#1E40AF
900	#1E3A8A
Neutral
50   #F9FAFB
100  #F3F4F6
200  #E5E7EB
300  #D1D5DB
400  #9CA3AF
500  #6B7280
600  #4B5563
700  #374151
800  #1F2937
900  #111827
950  #030712
Colores semánticos
Success
50 → 900
Base: #16A34A

Warning
50 → 900
Base: #F59E0B

Error
50 → 900
Base: #DC2626

Info
50 → 900
Base: #0284C7
Y los componentes consumirían:

bg-default
bg-subtle
bg-muted

text-primary
text-secondary
text-muted
text-disabled

border-default
border-strong

action-primary
action-primary-hover
action-primary-active

status-success
status-warning
status-error
status-info
Eso permite cambiar posteriormente branding o implementar dark mode sin rehacer componentes.

4. Iconografía
Recomendaría una sola familia: Lucide Icons.

Tamaños oficiales:

Tipo	Tamaño
XS	12px
Small	16px
Default	20px
Medium	24px
Large	32px
En interfaces administrativas:

16 px: inputs, tablas, botones pequeños
20 px: navegación y botones normales
24 px: acciones principales
32 px+: empty states

Nunca mezclar arbitrariamente 18, 21, 22, 25 px.

5. Buttons
El componente tendría:

┌───────────────────────────┐
│ [icon]  Button label  [>] │
└───────────────────────────┘
Variantes:

Primary
Secondary
Outline
Ghost
Danger
Link

Estados:

Default · Hover · Pressed · Focus · Disabled · Loading

Tamaños:

Size	Alto
Small	32px
Medium	40px
Large	44px
También:

Button + icon
Icon button
Split button
Button group
Floating action
6. Inputs
Todos los inputs compartirían la misma anatomía.

Label *
┌─────────────────────────────────────┐
│ [prefix/icon] Value           [icon]│
└─────────────────────────────────────┘
Helper / validation message
Estados:

Default
Hover
Focus
Filled
Disabled
Read-only
Success
Warning
Error
Tipos incluidos:

Input
Text
Email
Password
Number
Currency
Percentage
Phone
Search
URL
Date
Time
DateTime
Textarea
Masked input
Altura estándar: 40px.

7. Selects
Label
┌────────────────────────────────────┐
│ Selected value                  ▼ │
└────────────────────────────────────┘

┌────────────────────────────────────┐
│ Search...                          │
├────────────────────────────────────┤
│ ✓ Option 1                         │
│   Option 2                         │
│   Option 3                         │
└────────────────────────────────────┘
Debe existir:

Select
Searchable Select
Multi Select
Grouped Select
Async Select
Autocomplete

Y soporte para:

avatar
icon
description
checkbox
badge
8. Selection controls
Sistema completo:

Checkbox
Radio
Switch
Segmented control
Toggle button
Toggle group
Con estados:

Checked
Unchecked
Indeterminate
Disabled
Error
9. Alerts
Anatomía:

┌─────────────────────────────────────────┐
│ [!]  Alert title                   [×] │
│      Supporting description            │
│                                        │
│                         Optional action │
└─────────────────────────────────────────┘
Variantes:

Information
Success
Warning
Error
Neutral

Y dos tipos diferentes:

Inline Alert → dentro de contenido.

Toast / Notification → mensajes temporales.

10. Modals
La composición debe estar completamente definida.

████████████ Overlay █████████████████

        ┌─────────────────────────┐
        │ Title               [×] │
        │ Description             │
        ├─────────────────────────┤
        │                         │
        │          Body           │
        │                         │
        ├─────────────────────────┤
        │      Cancel   Continue  │
        └─────────────────────────┘
Tamaños:

SM   400px
MD   560px
LG   720px
XL   960px
Full
Tipos:

Confirmation
Destructive confirmation
Information
Form modal
Preview
Wizard

También debe existir Drawer / Side Panel para formularios o edición rápida.

11. Formularios
Esto es especialmente importante para tu caso.

No basta con tener Input + Select.

El sistema debe definir cómo construir un formulario.

Ejemplo
Información general
────────────────────────────────────────────

Nombre *                    Código *
[____________________]     [______________]

Tipo                        Estado
[Select             ▼]     [Active       ▼]


Información de contacto
────────────────────────────────────────────

Email                       Teléfono
[____________________]     [______________]


                             Cancelar   Guardar
Layouts oficiales:

1 columna
2 columnas
3 columnas
Responsive auto-grid
Sectioned form
Form + sidebar
Wizard
Modal form
Drawer form
Y reglas como:

Label → 8px → Input

Input
↓ 20–24px
Siguiente campo

Section title
↓ 16px
Campos

Sección
↓ 32px
Nueva sección
12. Cards
Anatomía base:

┌────────────────────────────────────────┐
│ Title                         [Action] │
│ Description                            │
├────────────────────────────────────────┤
│                                        │
│                Content                 │
│                                        │
├────────────────────────────────────────┤
│ Footer                                 │
└────────────────────────────────────────┘
Variantes:

Standard
Interactive
Metric
Status
Profile
Chart
Summary

13. Tables
Para backoffice este debe ser uno de los componentes principales.

Usuarios                              [+ Nuevo usuario]

[🔍 Buscar...]    [Estado ▼] [Rol ▼] [Filtros]

┌────┬──────────────┬────────┬──────────┬──────────┬─────┐
│ □  │ Nombre       │ Estado │ Rol      │ Fecha    │ ... │
├────┼──────────────┼────────┼──────────┼──────────┼─────┤
│ □  │ Juan Pérez   │ Active │ Admin    │ Oct 10   │ ... │
│ □  │ María López  │ Active │ Manager  │ Oct 09   │ ... │
└────┴──────────────┴────────┴──────────┴──────────┴─────┘

1–20 de 187                      < 1 2 3 ... 10 >
Debe incluir:

Search
Filters
Sorting
Pagination
Column selector
Sticky header
Row selection
Bulk actions
Inline actions
Context menu
Expandable rows
Loading state
Empty state
Error state
Skeleton
Density
Export
Y densidades:

Compact: 40px
Default: 48px
Comfortable: 56px
14. Badges y Chips
Estados:

Active
Inactive
Pending
Approved
Rejected
Draft
Completed
Cancelled
Pero no deben estar amarrados al texto.

Usar:

badge.success
badge.warning
badge.error
badge.info
badge.neutral
De esta manera el sistema de negocio define qué estado utiliza cada variante.

15. Tooltips
        Tooltip information
             ▼
          [ icon ]
Máximo aproximado:

240–320px

No usar tooltip para información crítica.

También incluir:

Popover
Dropdown Menu
Context Menu

16. Navegación
Debe incluir:

Sidebar
AppBar
Breadcrumb
Tabs
Vertical Tabs
Pagination
Stepper
Menu
Dropdown Menu
Command menu
17. Sidebar
Desktop:

┌─────────────────────┐
│ Logo                │
│                     │
│ ◉ Dashboard         │
│                     │
│ GENERAL             │
│ ◯ Usuarios          │
│ ◯ Solicitudes       │
│ ◯ Reportes          │
│                     │
│ ADMINISTRACIÓN      │
│ ◯ Configuración     │
│ ◯ Auditoría         │
│                     │
│                     │
│─────────────────────│
│ 👤 Alan             │
│    Administrator    │
└─────────────────────┘
Dimensiones:

Expanded: 240–256px
Collapsed: 64–72px
Debe soportar:

Sections
Nested menu
Active state
Badges
Collapsed state
Tooltip
User section
Logout
18. AppBar
┌──────────────────────────────────────────────────────────┐
│ Breadcrumb / Page title     Search      🔔   Help   👤 │
└──────────────────────────────────────────────────────────┘
Altura:

56–64px

Puede contener:

Page title
Breadcrumb
Global search
Notifications
Help
Settings
Profile
Quick actions
19. Shell del backoffice
Esta composición quedaría definida en el kit.

┌──────────────┬───────────────────────────────────────────────┐
│              │ AppBar                                      │
│              ├───────────────────────────────────────────────┤
│              │                                             │
│   SIDEBAR    │ Breadcrumb                                  │
│              │                                             │
│              │ Page Title                     Page actions │
│              │                                             │
│              │ Filters / tabs / toolbar                    │
│              │                                             │
│              │                 CONTENT                     │
│              │                                             │
│              │                                             │
└──────────────┴───────────────────────────────────────────────┘
Base:

Sidebar: 248px
Appbar: 64px

Page padding desktop:
24–32px

Content gap:
24px
20. Estructura móvil
También debe estar incluida, aunque el foco sea backoffice.

Desktop:

Sidebar + AppBar + Content
Tablet:

Collapsible sidebar
        +
AppBar
        +
Content
Mobile:

┌─────────────────────────┐
│ ☰   Page title      ⋮ │
├─────────────────────────┤
│                         │
│                         │
│        Content          │
│                         │
└─────────────────────────┘
El Sidebar se convierte en Navigation Drawer.

Tables pueden convertirse en:

┌──────────────────────────┐
│ Juan Pérez        Active │
│ Administrator            │
│ juan@email.com           │
│                          │
│ Oct 10               ⋮ │
└──────────────────────────┘
No simplemente comprimir la tabla desktop.

21. Breakpoints
xs    0–599
sm    600–899
md    900–1199
lg    1200–1535
xl    1536+
El sistema debe documentar el comportamiento de cada componente en:

Desktop / Tablet / Mobile.

22. Otros componentes necesarios
Para que realmente no tengas que volver a solicitar UI base, añadiría también:

Categoría	Componentes
Feedback	Skeleton, Spinner, Progress, Empty State
Navigation	Breadcrumb, Tabs, Stepper
Data	Table, List, Tree, Key-value
Date	Calendar, Date Picker, Date Range
Files	File upload, Drag & Drop, File preview
Identity	Avatar, Avatar group
Actions	Dropdown, Context menu
Organization	Accordion, Collapse
Search	Search input, Search result
Filters	Filter bar, Advanced filter
Dashboard	Metric card, Chart container
Content	Divider, Tooltip, Popover
Process	Timeline, Activity log
Security	Permission selector
Utilities	Copy button, Overflow menu
23. Patrones de Backoffice
Esta capa es la que normalmente falta en un UI Kit tradicional.

El sistema debería mostrar visualmente plantillas para:

CRUD List
CRUD Create
CRUD Edit
CRUD Detail

Dashboard

Settings

User management

Role & permissions

Approval workflow

Activity log

Audit log

Reports

Advanced filters

Import data

Export data

File management

Wizard

Empty state

Error state

Access denied

404 / 500
Por ejemplo:

LIST
Header
↓
Title + primary action
↓
Tabs
↓
Search + Filters
↓
Table
↓
Pagination
Y:

DETAIL

Breadcrumb
↓
Title + Status + Actions
↓
Summary
↓
Tabs
↓
General information
History
Documents
Activity
24. Estados obligatorios
Cada componente relevante debe mostrar:

Default
Hover
Focus
Active
Selected
Disabled
Loading
Empty
Error
Success
Read-only
Esto evitará que el developer tenga que inventar estados.

25. Accesibilidad
El sistema debería obligar a:

Contrast WCAG AA

Focus visible

Keyboard navigation

ARIA labels

Touch target mínimo 40x40

Inputs con labels reales

Errors asociados al campo

No depender solamente del color
26. Cómo organizaría el UI Kit
Para que funcione tanto para diseñadores como para agentes de IA y developers, lo dividiría así:

00 — Overview

01 — Foundations
     Colors
     Typography
     Spacing
     Grid
     Borders
     Shadows
     Icons

02 — Components
     Button
     Input
     Select
     Checkbox
     Radio
     Switch
     Badge
     Alert
     Tooltip
     Dropdown
     Modal
     Drawer
     Card
     Table
     Tabs
     Pagination
     etc.

03 — Forms
     Form structure
     Validation
     Form sections
     Responsive forms

04 — Navigation
     Sidebar
     AppBar
     Breadcrumb
     Tabs

05 — Data Display
     Tables
     Lists
     Cards
     Metrics
     Charts

06 — Feedback
     Alerts
     Toasts
     Loading
     Empty states
     Errors

07 — Patterns
     CRUD
     Dashboard
     Settings
     Approvals
     Logs
     Reports

08 — Layouts
     Desktop
     Tablet
     Mobile

09 — Templates
     Dashboard
     List
     Create
     Edit
     Detail
     Settings

10 — Guidelines
     Do
     Don't
     Accessibility
Lo más importante
Tu futuro requerimiento podría simplemente decir:

Usa Backoffice UI System. Crea una pantalla de administración de usuarios con listado, filtros, creación y edición.

Y el agente ya debería saber automáticamente:

qué fuente utilizar;
tamaños de fuente;
spacing;
altura de inputs;
colores;
botones;
modales;
tablas;
sidebar;
appbar;
estados;
cards;
iconos;
layouts;
responsive;
formularios;
validaciones;
borders;
breakpoints;
comportamiento móvil.
Eso es precisamente lo que conviene construir: un Design System de Backoffice completo, no una colección de componentes aislados.

El siguiente paso que recomiendo es convertir esta especificación en un UI Kit visual real, con una página tipo catálogo donde podamos ver Foundations → Components → Forms → Tables → Navigation → Templates, incluyendo la anatomía y variantes visuales de cada componente. Puedo prepararlo con una línea visual neutral/profesional para reutilizarlo como base de todos tus futuros backoffices.

muestrame una imagen de como quedaria organizado esto

como podemos crear instruciones simples para que la ia siga un patron establecido de composicion y sepa como contruir y seguir un patron de implementacion de esta visual al pie de la letra
La mejor forma es convertir el UI Kit en un contrato de implementación, no en un prompt enorme. La IA debería recibir unas pocas reglas obligatorias y consultar la especificación visual solo cuando necesite valores concretos.

Yo lo dividiría en 3 niveles: UI Core Rules → Component Specs → Page Patterns.

1. UI Core Rules
Este archivo debe ser pequeño y cargarse siempre. Define cómo piensa la IA al construir cualquier pantalla.

Backoffice UI System — Core Rules
Objetivo
Toda interfaz debe construirse utilizando exclusivamente el Backoffice UI System.

La IA no debe inventar estilos, tamaños, colores, componentes o patrones visuales fuera del sistema definido.

1. Regla principal
Antes de implementar una pantalla:

Identificar qué patrón de pantalla corresponde.

Identificar los componentes existentes necesarios.

Construir la pantalla mediante composición de esos componentes.

Utilizar exclusivamente design tokens.

Verificar responsive, estados y consistencia antes de finalizar.

Nunca comenzar estilizando directamente.

2. No inventar UI
Está prohibido crear arbitrariamente:

colores;

font-size;

spacing;

border-radius;

sombras;

tamaños de iconos;

alturas de inputs;

botones;

modales;

cards;

tablas;

layouts.

Si existe un componente del Design System, debe reutilizarse.

Si no existe, informar que es necesario crear un nuevo componente antes de implementarlo dentro de la pantalla.

3. Uso de Design Tokens
Nunca utilizar valores visuales arbitrarios.

Incorrecto:

padding: 17px;
font-size: 15px;
border-radius: 7px;
color: #2374FF;

Correcto:

padding: var(--space-4);
font-size: var(--font-body);
border-radius: var(--radius-md);
color: var(--color-primary-600);

Todos los valores visuales deben provenir de tokens.

4. Composición
Construir siempre desde componentes pequeños hacia estructuras mayores.

Foundation
→ Primitive
→ Component
→ Pattern
→ Page

Ejemplo:

Input + Label + HelperText
→ FormField

FormField + Select + Button
→ FormSection

FormSection + PageHeader
→ CreateFormPattern

CreateFormPattern + AppShell
→ UserCreatePage

No construir una Page como un componente monolítico.

5. Componentes existentes primero
Antes de crear algo nuevo verificar:

Button

IconButton

Input

Select

Checkbox

Radio

Switch

Badge

Alert

Tooltip

Dropdown

Modal

Drawer

Card

Table

Tabs

Pagination

Breadcrumb

Sidebar

AppBar

FormField

FormSection

PageHeader

FilterBar

Reutilizar antes de extender.

Extender antes de crear.

6. Layout
Todas las páginas deben utilizar:

AppShell
→ Sidebar
→ AppBar
→ MainContent

Dentro de MainContent:

Breadcrumb
→ PageHeader
→ PageActions
→ PageContent

PageContent debe usar el sistema de spacing establecido.

7. Formularios
Todos los formularios deben seguir:

Form
→ FormSection
→ FormGrid
→ FormField

Cada FormField contiene:

Label
Control
Helper/Error message

No colocar inputs directamente en la página.

Spacing entre campos y secciones debe provenir del sistema.

8. Tablas
Las páginas de listado deben seguir:

PageHeader
→ Toolbar / FilterBar
→ DataTable
→ Pagination

Nunca construir filtros, búsqueda o paginación de forma independiente si ya existe el patrón.

9. Estados
Cada componente interactivo debe considerar:

default;

hover;

focus;

active;

selected;

disabled;

loading;

error.

Cada pantalla de datos debe considerar:

loading;

empty;

error;

loaded.

10. Responsive
Implementar siempre:

Desktop
Tablet
Mobile

Desktop:
Sidebar expandido + AppBar + Content.

Tablet:
Sidebar colapsable + Content.

Mobile:
Navigation Drawer + AppBar + Content.

Las tablas que no sean legibles en móvil deben utilizar su representación móvil definida por el Design System.

11. Iconos
Usar exclusivamente la librería oficial de iconos.

Tamaños permitidos:

12px
16px
20px
24px
32px

No utilizar tamaños intermedios arbitrarios.

12. Jerarquía visual
Cada pantalla debe responder claramente:

¿Dónde estoy?

¿Qué información estoy viendo?

¿Cuál es la acción principal?

¿Cuáles son las acciones secundarias?

¿Cuál es el estado actual?

No competir visualmente entre acciones primarias y secundarias.

13. Acciones
Cada página debe tener máximo una acción visual primaria principal.

Ejemplo:

Primary:
Crear usuario

Secondary:
Exportar

Ghost:
Filtros

Danger:
Eliminar

No utilizar múltiples botones Primary compitiendo en una misma sección.

14. Consistencia
Si dos elementos cumplen la misma función deben:

verse iguales;

comportarse igual;

utilizar el mismo componente;

utilizar los mismos estados.

No crear variaciones visuales locales sin una razón definida por el Design System.

15. Regla final
La IA implementa el sistema.

La IA no rediseña el sistema.

Cuando exista conflicto entre una decisión local y el Design System, prevalece el Design System.

Eso sería lo que todos los agentes frontend deberían tener siempre disponible.

2. Component Specs
Luego tienes archivos pequeños especializados:

ui-system/
│
├── core.md
│
├── foundations/
│   ├── colors.md
│   ├── typography.md
│   ├── spacing.md
│   ├── radius.md
│   └── icons.md
│
├── components/
│   ├── button.md
│   ├── input.md
│   ├── select.md
│   ├── table.md
│   ├── modal.md
│   ├── card.md
│   ├── sidebar.md
│   └── appbar.md
│
└── patterns/
    ├── list-page.md
    ├── detail-page.md
    ├── create-page.md
    ├── edit-page.md
    ├── dashboard.md
    └── settings-page.md
La IA no carga todo. Si tiene que crear una tabla, lee core.md + table.md + list-page.md.

3. Page Patterns
Esto probablemente sea todavía más importante que los componentes.

Por ejemplo, una instrucción para cualquier CRUD podría ser simplemente:

CRUD LIST PAGE

AppShell
└── MainContent
    ├── Breadcrumb
    ├── PageHeader
    │   ├── Title
    │   ├── Description
    │   └── PrimaryAction
    ├── FilterBar
    │   ├── SearchInput
    │   ├── Filters
    │   └── SecondaryActions
    ├── DataTable
    └── Pagination
Entonces si dices:

Crea el listado de usuarios.

La IA no tiene que decidir cómo será la página. Ya existe una composición oficial.

Para un detalle:

DETAIL PAGE

AppShell
└── MainContent
    ├── Breadcrumb
    ├── PageHeader
    │   ├── Title
    │   ├── Status
    │   └── Actions
    ├── Summary
    ├── Tabs
    └── TabContent
Para Create/Edit:

FORM PAGE

AppShell
└── MainContent
    ├── Breadcrumb
    ├── PageHeader
    └── Form
        ├── FormSection
        ├── FormSection
        └── FormActions
La clave: separar diseño de negocio
La IA recibe algo como:

Crear módulo Usuarios.

Necesito:
- listado;
- crear;
- editar;
- detalle;
- activar/desactivar.
Y ella transforma automáticamente:

Listado
→ ListPagePattern

Crear
→ CreatePagePattern

Editar
→ EditPagePattern

Detalle
→ DetailPagePattern
Por lo tanto no debería preguntarte cómo quieres la tabla, dónde va el botón, cuánto padding debe tener o cómo se organiza el formulario.

Ya está definido.

Regla todavía más fuerte para tus agentes
Yo añadiría una instrucción como esta al Frontend Lead:

Antes de crear tasks de interfaz, identifica obligatoriamente:

Page Pattern correspondiente.

Componentes existentes requeridos.

Componentes faltantes.

Estados necesarios.

Comportamiento responsive.

No permitas que un Frontend Junior implemente estilos visuales directamente sin identificar primero los componentes y patterns del Backoffice UI System.

Cuando revises una implementación, valida primero consistencia con el Design System y después lógica funcional.

Y al Junior:

Implementa únicamente la task entregada utilizando el Backoffice UI System.

Antes de escribir código:

Lee el Page Pattern indicado.

Lee únicamente las especificaciones de los componentes utilizados.

Reutiliza componentes existentes.

Utiliza exclusivamente design tokens.

No inventes estilos o variantes locales.

Implementa todos los estados definidos.

Respeta el comportamiento responsive.

Si una necesidad no está cubierta por el Design System, no improvises una solución visual. Repórtala al Frontend Lead como componente o variante faltante.

Ese último punto es muy importante.

Impide cosas como:

sx={{
  padding: '13px',
  color: '#174AFF',
  borderRadius: '11px'
}}

porque el JR piensa que "se ve bien".

En tu sistema sería:

<Button variant="primary" size="md">
  Crear usuario
</Button>

Y se terminó la decisión visual.

El resultado que deberíamos buscar
Una vez creado correctamente, podrías darle a un agente únicamente:

Implementa la gestión de roles y permisos usando el Backoffice UI System.

Y el sistema debería ser capaz de derivar:

AppShell
 ├─ Sidebar
 ├─ AppBar
 └─ RoleListPage
      ├─ Breadcrumb
      ├─ PageHeader
      ├─ FilterBar
      ├─ DataTable
      └─ Pagination

RoleDetailPage
 ├─ PageHeader
 ├─ Tabs
 ├─ RoleInformation
 └─ PermissionMatrix
sin volver a discutir colores, inputs, botones, spacing, tablas, tamaños, modales o estructura base.

La idea central es: el agente puede decidir qué componente necesita, pero no puede decidir cómo debe verse ese componente. Esa decisión pertenece al Design System.

No veo que se mantenga stilos o sinsing de bottones, input , reglas visuales de composicion de un componente .

Si seguimos el patron propuesto tendriamos componentes con tamaños indefindos
Correcto. El patrón anterior define qué componentes usar, pero no define con suficiente precisión cómo deben verse. Si lo dejamos así, dos agentes pueden crear un Button md con alturas, paddings o iconos diferentes.

Para evitarlo, el sistema necesita una capa adicional obligatoria: Visual Component Contract.

La jerarquía debería ser:

Design Tokens
      ↓
Visual Component Contracts
      ↓
Composition Rules
      ↓
Page Patterns
      ↓
Implementation
1. Los tamaños no pueden quedar implícitos
Por ejemplo, Button size="md" no puede significar simplemente "botón mediano".

Debe significar exactamente:

BUTTON / MD

height: 40px
padding-x: 16px
padding-y: 0
gap: 8px

font-size: 14px
font-weight: 500
line-height: 20px

icon-size: 16px

border-width: 1px
border-radius: 8px

min-width: 40px

focus-ring:
  width: 2px
  offset: 2px
Y los tamaños permitidos:

Button	Alto	Padding X	Font	Icon
sm	32px	12px	13px	16px
md	40px	16px	14px	16px
lg	44px	20px	14px	20px
El agente no puede modificar esos valores.

2. Input Contract
Exactamente lo mismo.

INPUT / MD

container-height: 40px

padding-left: 12px
padding-right: 12px

font-size: 14px
line-height: 20px

icon-size: 16px
icon-gap: 8px

border-width: 1px
border-radius: 8px

label:
  font-size: 13px
  line-height: 18px
  font-weight: 500

label → input:
  6px

input → helper:
  6px

helper:
  font-size: 12px
  line-height: 16px
La anatomía queda fijada:

Label
↓ 6px
┌───────────────────────────┐
│ icon  Value          icon │ 40px
└───────────────────────────┘
↓ 6px
Helper / Error
Esto sí le dice a la IA exactamente cómo construirlo.

3. Select Contract
El Select debería heredar la geometría del Input.

SELECT / MD

height: 40px
padding-x: 12px

text:
14 / 20 / 400

selected-value-gap:
8px

chevron:
16px

border:
1px

radius:
8px
Y el dropdown:

SELECT MENU

margin-top: 4px
padding-y: 4px

option-height: 36px
option-padding-x: 12px

option-gap: 8px

icon:
16px

radius:
8px

max-height:
320px
Así no ocurre que el input mida 40px y el select 44px.

4. Composición interna
También tienes razón en otra parte: no basta con tamaño.

Hay que definir cómo se compone visualmente cada componente.

Ejemplo Button:

Button
│
├── LeadingIcon   optional
│
├── Label
│
└── TrailingIcon  optional
Reglas:

Icon ↔ label = 8px

Nunca:
icon + 4px + label
icon + 10px + label

Nunca usar:
leading icon + trailing icon
salvo variantes documentadas.
5. FormField
Aquí empezaríamos a tener composición real.

FORM FIELD

Label
↓ 6px
Control
↓ 6px
Helper / Error
Pero también debe definir dimensiones:

field-width:
100% del grid asignado

control-height:
40px

label-height:
18px

helper-height:
16px

min-total-height:
64px sin helper
86px con helper
Y:

Field → Field vertical:
20px

Field → Field horizontal:
16px
6. Form Layout
Una pantalla no debería decidir el spacing arbitrariamente.

Por ejemplo:

FORM SECTION

Section title
↓ 4px
Description
↓ 20px

Form grid
Grid:

desktop:
12 columnas

tablet:
8 columnas

mobile:
4 columnas

column-gap:
16px

row-gap:
20px
Un formulario estándar:

┌───────────────────────────────────────────┐
│ Información general                       │
│ Datos principales del usuario             │
│                                           │
│ Nombre             Apellido               │
│ [──────────────]   [──────────────]        │
│                                           │
│ Email              Teléfono               │
│ [──────────────]   [──────────────]        │
└───────────────────────────────────────────┘
Eso tiene que estar normado, no interpretado.

7. Cards
Contrato concreto:

CARD / DEFAULT

padding:
24px

radius:
12px

border:
1px

header → content:
20px

content → footer:
20px
Header:

title:
16 / 24 / 600

description:
14 / 20 / 400

title → description:
4px
No permitir que un agente cree:

padding: 18px
y otro:

padding: 32px
8. Modal
También completamente definido:

MODAL

SM:
400px

MD:
560px

LG:
720px

XL:
960px

radius:
12px
Composición:

┌────────────────────────────┐
│ Header                X    │ 64px
├────────────────────────────┤
│                            │
│ Body                       │ padding 24px
│                            │
├────────────────────────────┤
│ Footer                     │ 72px
└────────────────────────────┘
Header:

padding-x:
24px

title:
18 / 26 / 600
Footer:

padding:
16px 24px

actions-gap:
8px
9. Table
Esto también necesita medidas estrictas.

DATA TABLE / DEFAULT

header-height:
44px

row-height:
48px

cell-padding-x:
12px

cell-padding-y:
0

font:
13 / 18

header-font:
12 / 16 / 600

checkbox:
16px

row-action-icon:
16px
Densidades oficiales:

compact:
40px

default:
48px

comfortable:
56px
No existe:

row-height: 46px
salvo que se añada formalmente al sistema.

10. Page Layout
También debe existir un sizing contract general.

BACKOFFICE SHELL

sidebar-expanded:
248px

sidebar-collapsed:
72px

appbar:
64px
Página:

desktop:
padding 32px

tablet:
padding 24px

mobile:
padding 16px

max-content-width:
1600px

section-gap:
24px

major-section-gap:
32px
11. Page Header
Otro componente clave:

PAGE HEADER

Breadcrumb
↓ 12px

Title row
    Title
    Actions

↓ 8px

Description
Medidas:

title:
24 / 32 / 600

description:
14 / 20

action-gap:
8px

header → page-content:
24px
12. Sistema de medidas permitido
Otra forma de controlar mucho a la IA es decirle:

Valores permitidos de spacing:

0
4
8
12
16
20
24
32
40
48
64
Es decir, un agente no puede usar:

13px
17px
22px
27px
Lo mismo con radios:

4
6
8
12
16
9999
Y alturas:

Input:
32 / 40 / 44

Button:
32 / 40 / 44

Table row:
40 / 48 / 56

AppBar:
64

Sidebar item:
40
Esto reduce muchísimo la desviación visual.

13. Tokens estructurados
En vez de dejarlo solo en documentación, yo lo expresaría también como tokens.

Por ejemplo:

export const sizing = {
  control: {
    sm: 32,
    md: 40,
    lg: 44,
  },

  icon: {
    xs: 12,
    sm: 16,
    md: 20,
    lg: 24,
    xl: 32,
  },

  sidebar: {
    expanded: 248,
    collapsed: 72,
  },

  appbar: {
    height: 64,
  },

  table: {
    compact: 40,
    default: 48,
    comfortable: 56,
  },
}

Y:

export const spacing = {
  0: 0,
  1: 4,
  2: 8,
  3: 12,
  4: 16,
  5: 20,
  6: 24,
  8: 32,
  10: 40,
  12: 48,
  16: 64,
}

Ahora la IA tiene una fuente concreta.

14. Lo que debería leer el agente
Entonces cambiaría la propuesta anterior.

No sería:

core.md
components/button.md
Nada más.

Sería:

ui-system/

00-foundations/
    tokens.md
    colors.md
    typography.md
    spacing.md
    sizing.md
    radius.md
    icons.md

01-components/
    button.spec.md
    input.spec.md
    select.spec.md
    checkbox.spec.md
    table.spec.md
    card.spec.md
    modal.spec.md

02-compositions/
    form-field.spec.md
    form-section.spec.md
    filter-bar.spec.md
    page-header.spec.md
    data-table-layout.spec.md

03-patterns/
    list-page.md
    create-page.md
    detail-page.md
    edit-page.md

04-layout/
    app-shell.md
    desktop.md
    tablet.md
    mobile.md
Aquí aparece una diferencia importante:

Component
Input
Button
Card
Select
Composition
FormField
PageHeader
FilterBar
SearchToolbar
TableContainer
Pattern
ListPage
DetailPage
EditPage
Ese nivel de Composition es precisamente lo que faltaba en mi propuesta anterior.

15. Regla de implementación que yo usaría
Una instrucción muy corta para el agente podría ser:

Toda interfaz debe respetar exactamente el Backoffice UI System.

No inventes dimensiones.

Para cualquier elemento visual:

1. Usa exclusivamente los design tokens definidos.
2. Respeta las medidas del Component Contract.
3. Respeta la anatomía definida del componente.
4. Usa únicamente las Composition Specs existentes.
5. Usa el Page Pattern correspondiente.
6. No introduzcas spacing, sizing, font-size, radius o icon-size que no exista en el sistema.
7. Si una dimensión o variante no está especificada, detén esa decisión visual y repórtala como una extensión requerida del UI System.
Esto es mucho más estricto.

16. Ejemplo práctico
Si el requerimiento dice:

Agrega un campo Estado y un botón Guardar.

El agente no debería pensar visualmente.

Simplemente resuelve:

Estado
→ FormField
→ Select
→ size md
Por lo tanto automáticamente obtiene:

Label:
13px

Label gap:
6px

Select:
40px

Border:
1px

Radius:
8px

Horizontal padding:
12px

Chevron:
16px
Y:

Guardar
→ Button
→ primary
→ md
Obtiene:

height:
40px

padding-x:
16px

font:
14px / 20px / 500

radius:
8px
No hay decisión visual libre.

El modelo que te recomiendo
Lo definiría así:

DESIGN SYSTEM
│
├── Tokens
│
│   └── valores exactos
│
├── Components
│
│   └── geometría + estados
│
├── Compositions
│
│   └── cómo se relacionan componentes
│
├── Patterns
│
│   └── cómo se construyen pantallas
│
└── Templates
    └── referencias visuales completas
Ese modelo sí permitiría que distintos agentes implementen pantallas y que Button, Input, Select, Card, Modal, Table y Forms mantengan exactamente el mismo sizing y composición.

Y yo iría incluso un poco más lejos: además de los .md, crearía un archivo tokens.json o theme.ts como fuente única de verdad. La documentación explica la regla; el código contiene el valor real.

Si me parece mejor un tokers.json con este se guia el sistema en caso de que theme.ts, o sistem definido por el usuario no esta disponible
Sí. Esa estructura es más robusta porque tokens.json puede funcionar como fuente visual mínima obligatoria y agnóstica de tecnología. Luego, si el proyecto ya tiene theme.ts, variables CSS, MUI Theme, Tailwind config o algún sistema propio, el agente lo detecta y lo usa como implementación real sin perder las reglas del Design System.

Yo definiría esta prioridad:

1. Sistema visual existente del proyecto
   ↓
2. theme.ts / theme.js / CSS variables / MUI theme / Tailwind theme
   ↓
3. tokens.json del Backoffice UI System
   ↓
4. NUNCA inventar valores
Es decir, tokens.json sería el fallback oficial.

Por ejemplo:

{
  "$schema": "./tokens.schema.json",

  "meta": {
    "name": "Backoffice UI System",
    "version": "1.0.0",
    "baseUnit": 4
  },

  "spacing": {
    "0": "0px",
    "1": "4px",
    "2": "8px",
    "3": "12px",
    "4": "16px",
    "5": "20px",
    "6": "24px",
    "8": "32px",
    "10": "40px",
    "12": "48px",
    "16": "64px"
  },

  "radius": {
    "xs": "4px",
    "sm": "6px",
    "md": "8px",
    "lg": "12px",
    "xl": "16px",
    "full": "9999px"
  },

  "typography": {
    "fontFamily": {
      "sans": "Inter, sans-serif"
    },

    "display": {
      "fontSize": "32px",
      "lineHeight": "40px",
      "fontWeight": 600
    },

    "h1": {
      "fontSize": "28px",
      "lineHeight": "36px",
      "fontWeight": 600
    },

    "h2": {
      "fontSize": "24px",
      "lineHeight": "32px",
      "fontWeight": 600
    },

    "h3": {
      "fontSize": "20px",
      "lineHeight": "28px",
      "fontWeight": 600
    },

    "body": {
      "fontSize": "14px",
      "lineHeight": "20px",
      "fontWeight": 400
    },

    "bodyMedium": {
      "fontSize": "14px",
      "lineHeight": "20px",
      "fontWeight": 500
    },

    "small": {
      "fontSize": "13px",
      "lineHeight": "18px",
      "fontWeight": 400
    },

    "caption": {
      "fontSize": "12px",
      "lineHeight": "16px",
      "fontWeight": 400
    }
  },

  "icon": {
    "xs": "12px",
    "sm": "16px",
    "md": "20px",
    "lg": "24px",
    "xl": "32px"
  },

  "control": {
    "height": {
      "sm": "32px",
      "md": "40px",
      "lg": "44px"
    }
  },

  "button": {
    "sm": {
      "height": "32px",
      "paddingX": "12px",
      "gap": "8px",
      "fontSize": "13px",
      "iconSize": "16px",
      "radius": "8px"
    },

    "md": {
      "height": "40px",
      "paddingX": "16px",
      "gap": "8px",
      "fontSize": "14px",
      "iconSize": "16px",
      "radius": "8px"
    },

    "lg": {
      "height": "44px",
      "paddingX": "20px",
      "gap": "8px",
      "fontSize": "14px",
      "iconSize": "20px",
      "radius": "8px"
    }
  },

  "input": {
    "sm": {
      "height": "32px",
      "paddingX": "10px",
      "fontSize": "13px",
      "iconSize": "16px"
    },

    "md": {
      "height": "40px",
      "paddingX": "12px",
      "fontSize": "14px",
      "iconSize": "16px"
    },

    "lg": {
      "height": "44px",
      "paddingX": "14px",
      "fontSize": "14px",
      "iconSize": "20px"
    },

    "radius": "8px",
    "borderWidth": "1px",
    "labelGap": "6px",
    "helperGap": "6px"
  },

  "select": {
    "height": {
      "sm": "32px",
      "md": "40px",
      "lg": "44px"
    },

    "optionHeight": "36px",
    "menuPaddingY": "4px",
    "menuOffset": "4px",
    "maxMenuHeight": "320px"
  },

  "card": {
    "padding": {
      "sm": "16px",
      "md": "24px",
      "lg": "32px"
    },

    "radius": "12px",
    "borderWidth": "1px",
    "headerGap": "20px",
    "footerGap": "20px"
  },

  "modal": {
    "width": {
      "sm": "400px",
      "md": "560px",
      "lg": "720px",
      "xl": "960px"
    },

    "radius": "12px",
    "headerHeight": "64px",
    "footerMinHeight": "72px",
    "padding": "24px",
    "actionGap": "8px"
  },

  "table": {
    "headerHeight": "44px",

    "rowHeight": {
      "compact": "40px",
      "default": "48px",
      "comfortable": "56px"
    },

    "cellPaddingX": "12px",
    "fontSize": "13px",
    "headerFontSize": "12px",
    "actionIconSize": "16px"
  },

  "layout": {
    "sidebar": {
      "expanded": "248px",
      "collapsed": "72px"
    },

    "appbar": {
      "height": "64px"
    },

    "page": {
      "maxWidth": "1600px",

      "padding": {
        "desktop": "32px",
        "tablet": "24px",
        "mobile": "16px"
      },

      "sectionGap": "24px",
      "majorSectionGap": "32px"
    }
  },

  "grid": {
    "columns": {
      "desktop": 12,
      "tablet": 8,
      "mobile": 4
    },

    "columnGap": "16px",
    "rowGap": "20px"
  },

  "breakpoints": {
    "sm": "600px",
    "md": "900px",
    "lg": "1200px",
    "xl": "1536px"
  }
}

Lo importante es que aquí ya estamos definiendo tokens de foundation y también tokens específicos de componentes. Eso es mejor para agentes de IA que dejar únicamente:

{
  "spacing": {
    "4": "16px"
  }
}

porque el agente tendría que decidir cuánto spacing necesita un botón. En cambio:

"button": {
  "md": {
    "height": "40px",
    "paddingX": "16px"
  }
}

elimina esa decisión.

Cómo debería comportarse el agente
La regla podría ser muy simple:

VISUAL TOKEN RESOLUTION

Antes de implementar UI:

1. Detecta si el proyecto posee un sistema visual existente.

Busca, entre otros:

- theme.ts
- theme.js
- createTheme(...)
- ThemeProvider
- CSS variables
- :root
- tailwind.config
- design tokens
- variables.scss
- tokens existentes

2. Si existe:
   - úsalo como fuente de implementación;
   - no reemplaces sus valores automáticamente;
   - mapea el Backoffice UI System hacia los tokens existentes.

3. Si no existe:
   - usa ui-system/tokens.json como fuente de verdad.

4. Nunca inventes un valor visual si este no existe en:
   - el sistema visual del proyecto; o
   - tokens.json.

5. Si falta un token necesario:
   - repórtalo como token faltante;
   - no introduzcas un valor arbitrario.
Hay una distinción importante aquí.

Supongamos que el proyecto tiene:

theme.spacing(2)

y eso produce:

16px
Nuestro sistema dice:

"button.md.paddingX": "16px"

La IA debería utilizar:

px: 2

si esa es la convención del proyecto.

No:

px: '16px'

Así respetamos simultáneamente el Design System y la arquitectura existente.

También haría que cada component.spec.md referencie tokens en lugar de repetir números. Por ejemplo:

BUTTON / MD

height:
{button.md.height}

padding-inline:
{button.md.paddingX}

gap:
{button.md.gap}

font-size:
{button.md.fontSize}

icon-size:
{button.md.iconSize}

radius:
{button.md.radius}
Eso evita dos fuentes de verdad.

Si mañana cambias:

"button.md.height": "42px"

no tienes que editar button.spec.md.

El .spec.md define:

cómo se compone el botón.

El tokens.json define:

cuánto mide el botón.

Y eso nos deja una arquitectura bastante limpia:

ui-system/
│
├── tokens.json                ← valores visuales
│
├── tokens.schema.json         ← valida tokens
│
├── core.md                    ← reglas del agente
│
├── components/
│   ├── button.spec.md         ← anatomía
│   ├── input.spec.md
│   ├── select.spec.md
│   └── ...
│
├── compositions/
│   ├── form-field.spec.md
│   ├── page-header.spec.md
│   ├── filter-bar.spec.md
│   └── ...
│
└── patterns/
    ├── list-page.md
    ├── create-page.md
    ├── edit-page.md
    └── detail-page.md
Y establecería una regla clave para tu orquestador:

tokens.json es la especificación visual de referencia, pero el theme existente del proyecto es la implementación preferida.

Así puedes usar el mismo sistema con React + MUI, Tailwind, CSS Modules, SCSS, Chakra, Ant Design o cualquier otra tecnología, sin obligar a todos los proyectos a implementar exactamente el mismo theme.ts.

