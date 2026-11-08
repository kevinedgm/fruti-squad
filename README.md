<div align="center">

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/fruti-squad-oscuro.svg"><img src="assets/marca/fruti-squad.svg" alt="Fruti Squad" width="112"></picture>

# Fruti Squad

**Agentes especialistas que diseñan, gobiernan, implementan, auditan y documentan interfaces.**

Cada agente hace una sola clase de trabajo y entrega evidencia al siguiente. Para Codex, Kiro y Claude Code.

<picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/kiwi-oscuro.svg"><img src="assets/marca/kiwi.svg" alt="Kiwi" width="40"></picture>&nbsp;&nbsp;<picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/lima-oscuro.svg"><img src="assets/marca/lima.svg" alt="Lima" width="40"></picture>&nbsp;&nbsp;<picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/coco-oscuro.svg"><img src="assets/marca/coco.svg" alt="Coco" width="40"></picture>&nbsp;&nbsp;<picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/bruno-oscuro.svg"><img src="assets/marca/bruno.svg" alt="Bruno" width="40"></picture>&nbsp;&nbsp;<picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/mora-oscuro.svg"><img src="assets/marca/mora.svg" alt="Mora" width="40"></picture>

**Kiwi** → **Lima** → **Coco** → **Bruno** → **Mora**

</div>

---

## Qué es

Fruti Squad es un conjunto portable de agentes y skills para trabajar sobre sistemas de diseño e interfaces desde lenguaje natural.

La idea es sencilla: tú describes el trabajo, no el protocolo interno.

```text
"Rediseña este formulario"
"Ahora haz el de registro"
"Audítalo"
"Promuévelo a estable"
```

El Squad resuelve internamente quién debe actuar, qué contexto necesita y qué debe entregar al siguiente agente.

> **Si el proyecto también tiene Nexa Squad** (existe `.nexa-squad/`), Fruti diseña solo piezas: componentes, variantes, patrones, tokens y el Design Hub. Las pantallas del producto, las que usa un rol con datos y reglas reales, son de Nexa. Ver [Con Nexa Squad](#con-nexa-squad).

## El equipo

Cinco especialistas. Cada uno es dueño de una sola clase de decisión y entrega evidencia al siguiente; si encuentra algo que no le toca, lo devuelve a su dueño.

| | Agente | Lema | Qué decide | Qué entrega |
|---|---|---|---|---|
| <picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/kiwi-oscuro.svg"><img src="assets/marca/kiwi.svg" alt="Kiwi" width="32"></picture> | **Kiwi** · UX Architect | Define la estructura antes que la apariencia. | Brief funcional, user flow, jerarquía, estados y comportamiento en compact, medium y expanded | Wireframes F0–F2 neutrales y contrato geométrico |
| <picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/lima-oscuro.svg"><img src="assets/marca/lima.svg" alt="Lima" width="32"></picture> | **Lima** · Design System Governance | Una fuente, muchas piezas coherentes. | Si una pieza se reutiliza, extiende, es nueva o local; contrato, tokens, registry y lifecycle | Contrato de la pieza, registro y compuertas de promoción |
| <picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/coco-oscuro.svg"><img src="assets/marca/coco.svg" alt="Coco" width="32"></picture> | **Coco** · UI Audit | Construye la capa visual y la audita contra el contrato. | Cómo se ve la pieza con el sistema real (F3) y si lo implementado cumple (R0) | F3 con su CSS, y el reporte de cumplimiento con evidencia |
| <picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/bruno-oscuro.svg"><img src="assets/marca/bruno.svg" alt="Bruno" width="32"></picture> | **Bruno** · Frontend Implementation Engineer | Convierte la pieza aprobada en comportamiento frontend real. | Cómo funciona la pieza (R3): props, eventos, slots, estado, teclado, foco y ARIA | Componente funcional, build en verde y lo verificado y no verificado |
| <picture><source media="(prefers-color-scheme: dark)" srcset="assets/marca/mora-oscuro.svg"><img src="assets/marca/mora.svg" alt="Mora" width="32"></picture> | **Mora** · Documentation & Knowledge Engineer | Documenta solo lo que existe y fue verificado. | Qué se publica en el Design Hub y cómo se conecta | Páginas del Design Hub, navegación y cobertura |

Lo que ninguno hace:

- Kiwi no decide color, tipografía ni implementación.
- Lima no audita: consume la auditoría de Coco.
- Coco no programa comportamiento ni cambia la estructura aprobada.
- Bruno no escribe valores visuales ni cambia CSS, tokens, contratos o el registry.
- Mora no documenta nada que no esté implementado y verificado.

Regla principal:

```text
Kiwi estructura → Lima gobierna → Coco construye la capa visual → Bruno implementa el comportamiento → Coco audita → Lima decide el estado → Mora documenta
```

No hay dos auditores ni dos propietarios del lifecycle. Si una pieza no tiene comportamiento más allá del HTML nativo, el paso de Bruno se salta y queda anotado.

---

# Instalación

## Requisitos

- Git
- Node.js 16 o superior
- Un entorno compatible: Claude Code, Codex o Kiro

## Instalación guiada

Desde el proyecto donde quieras utilizar Fruti Squad:

```bash
npx github:kevinedgm/fruti-squad setup --target codex
```

También puedes usar:

```bash
npx github:kevinedgm/fruti-squad setup --target claude
npx github:kevinedgm/fruti-squad setup --target kiro
```

`setup` instala el Squad y ejecuta el asistente para crear el perfil del proyecto.

Si ya tienes la configuración preparada y solo quieres instalar:

```bash
npx github:kevinedgm/fruti-squad install --target codex
```

Cambia `codex` por `claude` o `kiro` según corresponda.

Para probar el instalador después de un cambio: `npm test` (instala en proyectos temporales para los tres destinos y comprueba que el estado del proyecto no se sobrescribe).

### Kiro

Con `--target kiro` el instalador deja:

- `.agents/skills/lima/` y `.kiro/agents/{kiwi,coco,bruno,mora}/` — los miembros.
- `.kiro/agents/{kiwi,lima,coco,bruno,mora}.md` — un agente de Kiro por miembro, con sus herramientas, los recursos compartidos (`.fruti/policy.md`, estado y handoff) y permisos: lee todo, pregunta antes de escribir y tiene prohibidos `rm -rf`, `sudo`, `git push`, `git reset --hard` y `git clean`.
- `.kiro/steering/fruti-squad.md` — apunta a la política.

### Claude Code

Con `--target claude` el instalador deja:

- `.claude/skills/{kiwi,lima,coco,bruno,mora-docs}/` — cada miembro como Skill.
- `CLAUDE.md` — bloque del Squad que importa `.fruti/policy.md` (la política de ruteo, la misma que usa Codex vía `AGENTS.md`).
- `.fruti/paths.yaml` — mapa de rutas para resolver las referencias de `.fruti/runtime/*.yaml`.
  Para resolver una ruta desde scripts o desde el agente: `fruti path skills/lima/reference/quality-gates.md` imprime la ruta real en el proyecto.

Después basta con pedir en lenguaje natural ("rediseña este formulario") o invocar `kiwi`, `lima`, `coco`, `bruno` o `mora-docs`.

---

# Configuración del proyecto

Fruti Squad usa un perfil de proyecto compartido. Ahí viven las decisiones que no deben inventarse en cada ejecución: design system, tokens, tipografía, breakpoints, rutas, stack, accesibilidad y fuentes de verdad.

Lima gobierna el perfil. Coco puede mantener su contrato de datos y campos específicos de construcción. Los demás agentes consumen esa verdad sin crear configuraciones paralelas.

El perfil es persistente: si cambias un dato del sistema en lenguaje natural, debe actualizarse ahí en lugar de depender de la memoria de la conversación.

## Fundamentos de un sistema nuevo

Si el perfil dice `design_system: NEW`, antes de aprobar visualmente cualquier componente hace falta una propuesta de fundamentos (color, tipografía, geometría, movimiento…). Hay dos formas de crearla:

```bash
fruti foundations                                             # asistente de 8 pasos, en terminal
fruti foundations --marca '#0B6E4F' --fuente Inter --radio 6  # entradas cortas, sin preguntas
```

Entradas cortas disponibles: `--marca`, `--acento`, `--fuente`, `--fuente-display`, `--radio` (0–24 px), `--densidad` (`compacta`, `equilibrada`, `amplia`), `--sentir` y `--evitar`. Con `--preguntar` el asistente arranca con esos valores ya puestos.

Lo que no das se calcula o se toma por omisión, y la propuesta lo dice campo por campo en `origin`: `input` (lo dijiste tú), `derived` (por ejemplo, el radio de paneles es tu radio + 6 y la altura de controles sale de la densidad) o `default`. También mide el contraste del color de marca y avisa si el texto blanco sobre él no llega a 4.5:1.

En ambos casos el resultado es solo una **propuesta** en `.fruti/foundations/proposal.yaml`. `.fruti/tokens.json` sigue siendo la única fuente de los tokens: Lima lo genera cuando apruebas la propuesta y antes te muestra qué valores quedaron por omisión.

---

# Cómo funciona una petición

Ejemplo:

```text
"Rediseña el formulario de registro y ejecuta todo el flujo"
```

El recorrido conceptual es:

```text
PETICIÓN NATURAL
      │
      ▼
KIWI
brief · flujo · estructura · adaptación
      │
      ▼ handoff compacto
LIMA
reuse/extend/new/local · contrato · registry
      │
      ▼ handoff compacto
COCO
F3 · capa visual con el sistema real · CSS
      │
      ▼ handoff compacto
BRUNO
R3 · API · eventos · estado · teclado · foco · ARIA
      │
      ▼ handoff compacto
COCO
R0 · auditoría de lo implementado
      │
      ▼ compliance report
LIMA
gates · lifecycle · registry
      │
      ▼
MORA
documentación del delta verificado
```

Si después dices:

```text
"Ahora haz el formulario de recuperación"
```

el sistema parte del estado persistido y de las fuentes canónicas. No debería reconstruir indiscriminadamente toda la documentación anterior.

---


# Rediseño de una aplicación existente

Fruti Squad puede entrar a un producto ya construido sin asumir que debe reescribirlo ni que su UI actual es correcta.

Cuando detecta intención de rediseño, el flujo es:

```text
UNDERSTANDING
  ↓
REFERENCES (opcional)
  ↓
DESIGN INVENTORY
  ↓
USER SCOPE APPROVAL
  ↓
DESIGN DIRECTION
  ↓
REDESIGN PLAN
  ↓
Kiwi → Lima → Coco → Bruno → Coco (R0) → Lima → Mora
```

## Understanding

Puedes describir la intención en lenguaje natural:

```text
"Quiero que se vea moderno, pulcro, profesional, claro y nada genérico.
El 90% del uso será móvil."
```

Kiwi comprime esa intención en fuentes aprobadas dentro de `.fruti/design/`, de modo que los agentes posteriores no tengan que reconstruir la conversación.

Las referencias también pueden expresarse naturalmente, por ejemplo: "me gusta la claridad de Notion y la precisión de Linear". Fruti extrae cualidades; no copia componentes, layouts ni estilos de esos productos.

## Design Inventory + checklist

Antes de rediseñar, Kiwi realiza una inspección rápida y agrupa todo lo que puede implicar diseño: foundations, navegación, controles, componentes/patrones, vistas, estados y visualización de datos.

El resultado se presenta como alcance revisable. Cada superficie puede quedar como:

```text
not-reviewed · proposed · approved · excluded · preserve · completed
```

Lo marcado como `excluded` se ignora. Lo marcado como `preserve` conserva su estructura/comportamiento salvo cambio explícito posterior. Solo `approved` entra al plan de rediseño.

## Design Direction

La síntesis aprobada vive en:

```text
.fruti/design/design-direction.yaml
```

Describe cómo debe sentirse el producto (por ejemplo moderno, refinado, claro, mobile-first, no genérico) y qué evitar. Es dirección, no tokens. Los valores visuales concretos siguen perteneciendo a `.fruti/tokens.json`.

## Plan de rediseño

Fruti ordena el trabajo por dependencias, no por capricho de archivos:

```text
Foundations → Primitives → Patterns → Domain components → Views → Polish
```

La aplicación existente sirve para entender funcionalidad y restricciones. No se usa como autoridad de la nueva identidad visual, salvo decisiones que el usuario marque explícitamente como preservadas.



# Probar el Squad de punta a punta

El comando `test` prepara una prueba reproducible del flujo completo sin obligarte a escribir flags internos de Kiwi/Lima/Coco/Bruno/Mora.

```bash
fruti test --prompt "Diseña un card que muestre tina, día, horas desde la última medición, temperatura y Brix"
```

También puedes entregar una implementación existente como evidencia del estado actual:

```bash
fruti test --file ./src/components/LegacyCard.vue --prompt "Rediseña este componente"
```

Con `npx`:

```bash
npx github:kevinedgm/fruti-squad test \
  --prompt "Diseña un card de tina con prioridad de medición"
```

### Casos fijos para medir cambios al squad

Para saber si un cambio a Kiwi, Lima, Coco, Bruno o Mora mejora o empeora el resultado, corre los mismos casos antes y después:

```bash
fruti test --case evals/casos/03-tabla-de-cuentas.md
```

La ronda queda marcada con su caso. Corre cada caso dos veces y compara caso por caso; ver [evals/README.md](evals/README.md) y el análisis en [docs/arquitectura-agentes.md](docs/arquitectura-agentes.md).

El comando crea `.fruti/tests/<round>/request.md`. Después pide al agente del entorno:

```text
Ejecuta .fruti/tests/<round>/request.md completo de Kiwi a Mora y
muéstrame result.md y la página final del Design Hub.
```

La prueba exige:

```text
KIWI
  F2 neutral en grises
  geometry contract
  compact / medium / expanded
  estados + decision records
        ↓
LIMA
  reuse / extend / new / local
  validación contra contratos y estándares realmente configurados
        ↓
COCO
  F3 + CSS con el sistema real
  fidelidad F2 → F3 (FID-GEOMETRY-001)
        ↓
BRUNO
  comportamiento R3 sobre el F3, sin cambiarlo
  SKIPPED si la pieza no tiene comportamiento propio
        ↓
COCO
  auditoría R0 + compliance report
        ↓
LIMA
  gate usando la evidencia de Coco
        ↓
MORA
  página canónica del Design Hub
  Preview = componente verificado real
        ↓
result.md
  PASS / PARTIAL / FAIL por etapa
```

Si una guía normativa configurada no está disponible, la prueba debe marcarla como evidencia faltante. No se permite inventarla desde memoria.

## Fidelidad estructural F2 → F3

Kiwi marca cada pieza del F2 con `data-piece`; Coco conserva las marcas en F3. Este comando compara la geometría de ambos en cada viewport de verificación y falla si una pieza cambia de grupo, de orden o de fila, si otra pieza se mete entre sus miembros, o si su separación o tamaño se desvían más de lo tolerado:

```bash
fruti fidelity --f2 .fruti/tests/r01/kiwi-f2.html --f3 http://localhost:5173/usuarios \
  --round r01 --out .fruti/tests/r01/fidelity.json
```

Un `fail` bloquea la dimensión estructural; un `blocked` (sin Playwright o sin marcas) deja la prueba en PARTIAL. Ejemplo completo y tabla de chequeos en [`docs/fidelidad/`](docs/fidelidad/README.md).


# Arquitectura de contexto eficiente

La regla central está en `AGENTS.md` (en un proyecto instalado: `.fruti/policy.md`):

```text
route first → read second
```

Primero se identifica la intención, artefacto, fase y agente propietario. Después se carga únicamente el contexto necesario.

Fruti Squad divide el conocimiento en tres niveles:

```text
L0  Router / runtime contract
    pequeño y barato de interpretar

L1  Contratos ejecutables
    estado, handoffs, manifests y reportes JSON/YAML

L2  Referencias profundas
    documentación Markdown; se consulta bajo demanda
```

Una referencia mencionada en un manual no significa que deba cargarse automáticamente.

La documentación profunda sigue siendo normativa cuando existe ambigüedad, conflicto o una regla que el contrato compacto no puede resolver.

---

# Carpeta `.fruti`

La capa runtime se organiza así:

```text
.fruti/
├── audit-manifest.yaml
├── runtime/
│   ├── kiwi.yaml
│   ├── lima.yaml
│   ├── coco.yaml
│   ├── bruno.yaml
│   └── mora.yaml
├── state/
│   └── current.json
├── handoffs/
│   └── current.json
└── reports/
    └── compliance-current.json
```

## `runtime/*.yaml`

Son contratos compactos por agente. Indican qué consume, qué produce y cuándo necesita abrir referencias profundas.

## `state/current.json`

Es memoria operativa compacta: artefacto activo, ronda, propietario, decisiones y punteros relevantes.

No reemplaza las fuentes de verdad. Si contradice el perfil, registry o código real, se repara.

## `handoffs/current.json`

Transporta únicamente lo necesario entre agentes:

- artefacto y ronda;
- agente origen y siguiente propietario;
- decisiones congeladas;
- piezas y clasificación conocida;
- estados requeridos;
- comportamiento adaptativo;
- preguntas abiertas;
- rutas de evidencia;
- delta respecto al handoff anterior.

Nunca debe copiar documentos enteros.

## `audit-manifest.yaml`

Define las reglas de auditoría con identificadores estables.

Los checks deterministas deben ejecutarse mediante scripts/herramientas cuando sea posible. Por ejemplo: fidelidad estructural F2 → F3 (`FID-GEOMETRY-001`, con `fruti fidelity`), DOM inválido, IDs duplicados, overflow horizontal, tokens prohibidos, semántica interactiva, targets táctiles o inconsistencias del registry.

Coco reserva razonamiento para lo que realmente requiere juicio: jerarquía, claridad, densidad, affordance, consistencia, composición adaptativa y regresiones visuales.

## `reports/compliance-current.json`

Es la salida estructurada de Coco. Lima puede usarla para gates y Mora para documentación sin volver a interpretar toda la auditoría.

---

# Qué carga cada agente

## Kiwi

Empieza desde estado/perfil y carga únicamente las referencias estructurales necesarias para la fidelidad actual.

Produce brief, flujo/wireframe, evidencia y handoff hacia Lima.

No hace F3, implementación ni auditoría final.

## Lima

Consume el handoff de Kiwi, perfil y entrada relevante del registry.

Clasifica cada pieza como `reuse`, `extend`, `new` o `local`, fija contratos y gobierna lifecycle.

Carga referencias de lifecycle, gates, adaptación o promoción únicamente cuando la operación actual las necesita.

## Coco

No rehace el brief ni la gobernanza cuando Kiwi/Lima ya entregaron evidencia vigente.

Construye la capa visual con el sistema real (F3 y CSS) y es el auditor canónico: después de Bruno audita lo implementado.

Para auditoría empieza por `audit-manifest.yaml` y evidencia automática. Además de jerarquía, densidad y affordance, revisa que no haya patrones engañosos (`UX-DECEPTIVE-001`): rechazos que avergüenzan, consentimientos premarcados o costos que aparecen al final. Abre estándares extensos únicamente para reglas ambiguas, fallidas o no deterministas.

Produce `compliance-current.json`.

## Bruno

Parte del handoff, el contrato aprobado, el F3 y el CSS de Coco, y solo los archivos que va a modificar con sus imports directos.

Implementa la API pública (props, eventos, slots, estado controlado), la semántica nativa, el teclado, el foco y el ARIA funcional. Conserva las clases que usa el CSS de Coco y no escribe valores visuales.

Implementa cada transición tal como la define la tabla del contrato de Lima (qué la dispara, qué regla sigue y qué feedback ve el usuario); no inventa un debounce, un timeout ni un mensaje de error. Si el componente ya existe, antes de cambiarlo fija su comportamiento actual con pruebas de caracterización.

Corre el build y las pruebas disponibles. Lo que no pudo correr lo marca como no verificado. Si falta una entrega o dos fuentes se contradicen, lo devuelve a su dueño en lugar de inventarlo.

## Mora

Parte de registry + compliance report + código/API real + diff afectado.

Documenta el delta implementado y verificado, con las reglas de redacción de `agentes/mora/redaccion.md`. No reconstruye todo el historial de diseño para escribir una ficha.

---

# Con Nexa Squad

**Fruti Squad fabrica las piezas; Nexa Squad arma los módulos con ellas.** Usa Fruti cuando el resultado es algo que se reutiliza en muchas pantallas (un componente, una variante, un patrón, un token) y vive en el Design Hub. Usa Nexa cuando el resultado es una funcionalidad del producto que usa un rol, con sus datos, reglas de negocio y servidor.

Ejemplo con la misma palabra:

- "Necesito un autocomplete que busque mientras escribo y se pueda usar con teclado" → **Fruti**: es una pieza.
- "En Cuentas, la recepcionista busca la muestra pendiente y la paga" → **Nexa**: es un módulo que usa esa pieza.

Cuando los dos están en el mismo proyecto:

- **Las pantallas del producto son de Nexa.** Si existe `.nexa-squad/`, Kiwi no wireframea una pantalla o un módulo del producto: responde en una línea con la frase para Nexa (`/orka …`). Si la petición también nombra un patrón reutilizable ("el formulario de alta estándar"), Fruti diseña solo ese patrón. En un rediseño, Fruti planea fundamentos, primitivas, patrones y componentes; las vistas quedan con `owner: nexa`.
- Sin Nexa en el proyecto, Fruti sigue diseñando pantallas como siempre.
- Nexa lee el registro, los contratos y los tokens de Fruti, y nunca los modifica.
- Si a Nexa le falta una pieza, su curador (Kura) escribe un pedido en `docs/componentes/pedidos/<id>.md`. Pídele a Fruti "diseña el componente de `docs/componentes/pedidos/<id>.md`": Kiwi arma su brief desde ese pedido y su tabla de estados alimenta la tabla de transiciones de Lima.
- Cuando el componente queda en el registro, Nexa lo toma con `/orka continúa <módulo>`.

La guía completa, con qué pedirle a cada uno, los cinco casos en que trabajan juntos y quién manda cuando no coinciden, está en [docs/nexa-y-fruti.md](docs/nexa-y-fruti.md). El instalador la copia a `.fruti/nexa-y-fruti.md`.

---

# Fuentes de verdad

La carpeta `.fruti` no pretende convertirse en otra religión documental. Cada dato conserva un propietario:

| Información | Fuente canónica |
|---|---|
| Configuración del proyecto | perfil activo de Lima |
| Lifecycle, status, versión y QA | registry |
| API y comportamiento implementado | código/tipos reales |
| Evidencia de auditoría | compliance report + evidencia runtime |
| Estado operativo temporal | `.fruti/state/current.json` |

Cuando el cache contradice una fuente canónica, gana la fuente canónica.

---

# Ejemplos de uso

No necesitas comandos internos ni flags de fase.

```text
"Rediseña esta pantalla"
```

Kiwi comienza por estructura cuando existe incertidumbre estructural y el flujo continúa por el Squad.

```text
"Ahora haz que funcione mejor en móvil"
```

Se reutiliza el artefacto activo y se carga únicamente el contexto de adaptación necesario.

```text
"Haz que el selector se pueda usar con teclado y avise cuando cambie"
```

Bruno implementa el comportamiento sobre el F3 aprobado, sin tocar su CSS, y después Coco audita el resultado.

```text
"Audítalo"
```

Coco usa el manifest y evidencia automática primero; después revisa los criterios que requieren juicio.

```text
"Ya está bien, promuévelo a estable"
```

Lima evalúa los gates con la evidencia existente y solicita aprobación cuando el lifecycle la exige.

---

# Principios de diseño del Squad

1. **Lenguaje natural es la interfaz.** El usuario no administra el runtime.
2. **Route first, read second.** No se precargan directorios de referencias.
3. **Persistir decisiones, no conversaciones.** El estado guarda hechos compactos y punteros.
4. **Un propietario por responsabilidad.** Evita auditorías y decisiones duplicadas.
5. **Automatizar lo determinista.** No gastar razonamiento en comprobar lo que un script puede medir.
6. **Documentar el delta.** Mora no reinterpreta todo el proyecto en cada cambio.
7. **Las referencias profundas siguen disponibles.** Optimizar contexto no significa eliminar conocimiento.

---

# Desarrollo

Para trabajar sobre el proyecto:

```bash
git clone https://github.com/kevinedgm/fruti-squad.git
cd fruti-squad
```

Antes de integrar cambios, compara contra `main` y prueba al menos estos escenarios:

```text
1. Nueva pantalla → Kiwi → Lima → Coco → Bruno → Coco (R0) → Lima → Mora
2. Segunda pantalla del mismo proyecto → verificar reutilización de estado
3. Auditoría → comprobar que Coco usa manifest antes de referencias profundas
4. Cambio pequeño → comprobar que Mora documenta solo el delta
5. Promoción → comprobar que Lima usa compliance + registry
```

La métrica útil no es solo si el resultado final funciona. También importa observar cuántos archivos y referencias se leen para producirlo.

La identidad visual (símbolos, colores, tipografía y reglas de uso) está en [docs/marca.md](docs/marca.md); los archivos, en `assets/marca/`.

---

## Licencia

MIT. Consulta `LICENSE`.
