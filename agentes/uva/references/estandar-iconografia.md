# Guía y estándar de iconografía accesible

> **Norma de Uva.** Este documento es la fuente normativa de Uva para iconografía; `estandares.md` es la rúbrica operativa que lo aplica. Si discrepan, gana este documento, salvo las decisiones del usuario registradas en `.fruti/runtime/uva.yaml` (`decisions`).
>
> **Alcance en el squad:** solo Uva lo adopta. Las secciones de implementación (botones, teclado, foco, tooltips, toggles, disclosure) Uva las aplica a sus **recomendaciones de uso** en la propuesta y el handoff; no implementa componentes.
>
> **Texto incompleto:** se recibió hasta la sección 34, interrumpida. Las secciones posteriores, si existen, están pendientes.
>
> **Observación (sin modificar el texto):** el ejemplo de §2.1 usa `category: destructive-action`, que no aparece en la taxonomía de §3. Uva lo trata como `action`; pendiente de aclarar por el autor de la norma.

Estándar de diseño, semántica, interacción, movimiento, accesibilidad y gobierno de iconografía para Design Systems.

- Versión: 1.0
- Base visual: Lucide Icons
- Base normativa: WCAG 2.2 + WAI-ARIA Authoring Practices Guide
- Aplicación: Web, PWA, desktop, tablet y mobile

---

## 1. Propósito

Los iconos no deben tratarse simplemente como recursos gráficos.

Dentro de un Design System, un icono es una unidad de comunicación capaz de representar: acciones; objetos; navegación; estados; relaciones; jerarquías; feedback; dirección; controles; información.

Un sistema de iconografía debe establecer reglas para:

1. seleccionar iconos;
2. diseñar iconos nuevos;
3. asignar significado;
4. utilizarlos consistentemente;
5. combinarlos con texto;
6. hacerlos interactivos;
7. animarlos;
8. hacerlos accesibles;
9. adaptarlos a diferentes dispositivos;
10. gobernar su evolución.

El objetivo no es construir una galería de SVG. El objetivo es construir un lenguaje visual consistente.

---

## 2. Principios fundamentales

### 2.1 Diseñar significado antes que apariencia

Antes de elegir un icono debe definirse qué representa.

Incorrecto:

```text
Necesito un icono bonito para este botón.
```

Correcto:

```text
Esta acción elimina permanentemente un registro.
semanticName: delete
category: destructive-action
```

Después se selecciona la representación gráfica.

### 2.2 Claridad antes que originalidad

Un icono familiar suele ser preferible a uno visualmente original.

```text
Search    → magnifying glass
Delete    → trash
Edit      → pencil
Settings  → gear
Close     → X
```

La interfaz no debería obligar al usuario a aprender un nuevo idioma pictográfico para realizar operaciones comunes.

### 2.3 El icono no sustituye automáticamente al texto

Los iconos ayudan principalmente a: reconocimiento; escaneo; orientación; jerarquía; reducción de ruido visual.

Pero algunos conceptos son demasiado abstractos para comunicarse únicamente mediante símbolos. Cuando exista ambigüedad, utilizar `[icon] + Label` en lugar de `[icon]`.

### 2.4 Misma función → mismo icono

Una acción debe representarse consistentemente.

```text
delete   → Trash2
edit     → Pencil
search   → Search
settings → Settings
```

No utilizar alternativamente `Trash`, `Trash2`, `CircleX`, `X`, `MinusCircle` para representar la misma operación.

### 2.5 Funciones diferentes → iconos diferentes

No reutilizar el mismo símbolo para acciones conceptualmente diferentes. Por ejemplo, `Delete`, `Archive`, `Remove`, `Close`, `Cancel` no deberían compartir indiscriminadamente el mismo icono.

---

## 3. Taxonomía de iconos

Todo icono utilizado en el Design System debe pertenecer a una categoría semántica.

### 3.1 Decorative
No transmite información nueva. Ejemplo: `[+] Agregar usuario` — el texto ya comunica la acción; el icono es decorativo. Debe permanecer oculto para tecnologías asistivas.

### 3.2 Action
Representa una operación. Ejemplos: Edit, Delete, Copy, Download, Upload, Share, Save.

### 3.3 Navigation
Representa desplazamiento o cambio de contexto. Ejemplos: Home, Back, Forward, Previous, Next, External link.

### 3.4 Informative
Comunica información. Ejemplos: Location, Phone, Calendar, Time, Attachment.

### 3.5 Status
Representa un estado. Ejemplos: Success, Warning, Error, Information, Pending, Offline.

### 3.6 Toggle
Representa un estado binario. Ejemplos: Mute, Favorite, Visibility, Pin, Lock.

### 3.7 Disclosure
Controla contenido expandible. Ejemplos: ChevronDown, ChevronUp, ChevronRight.

### 3.8 Directional
Representa dirección. ArrowLeft, ArrowRight, ArrowUp, ArrowDown.

### 3.9 Object
Representa una entidad. Ejemplos: User, Folder, File, Calendar, Building, Database.

### 3.10 Brand
Representa identidad de marca. Los iconos genéricos de Lucide no deben sustituir logotipos cuando la identidad del tercero sea relevante.

---

## 4. Selección de iconos

Antes de incorporar un icono:

1. definir el significado;
2. identificar la categoría;
3. comprobar si existe un símbolo reconocido;
4. verificar si Lucide contiene una representación apropiada;
5. comprobar que el símbolo no tenga otro significado dentro del producto;
6. evaluar si necesita texto;
7. verificar accesibilidad;
8. registrar la decisión.

---

## 5. Semantic Icon Registry

El Design System debería disponer de un registro semántico. En lugar de que cada componente decida `<Trash2 />`, se recomienda conceptualmente `<SemanticIcon name="delete" />`.

El registro resolvería:

```text
add       → Plus
delete    → Trash2
edit      → Pencil
search    → Search
settings  → Settings
warning   → TriangleAlert
error     → CircleAlert
success   → CircleCheck
info      → Info
close     → X
previous  → ChevronLeft
next      → ChevronRight
```

### 5.1 Estructura del registro

Cada entrada debería poder contener:

```yaml
semanticName: delete
icon:
  library: lucide
  name: Trash2
category:
  destructive-action
accessibility:
  defaultLabel: Eliminar
direction:
  rtl: fixed
motion:
  allowed: feedback
status:
  stable
```

---

## 6. Lenguaje visual Lucide

Cuando se creen iconos propios que deban convivir con Lucide, deben respetarse sus características visuales fundamentales.

- **Canvas:** 24 × 24 px
- **Stroke:** 2 px. El stroke se encuentra centrado sobre el path.
- **Safe zone:** los strokes deben mantenerse aproximadamente ≥ 1 px alejados de los límites del canvas.
- **Line caps:** los paths abiertos utilizan `round`.
- **Line joins:** utilizar `round`.
- **Separación:** entre elementos visuales independientes ≥ 2 px. Los espacios internos deberían aproximarse también a ese mínimo cuando sea posible.

---

## 7. Balance óptico

La geometría matemática no siempre produce equilibrio visual. Un icono puede necesitar desplazarse ligeramente para parecer centrado. Por tanto: `geometric center ≠ optical center`. Debe priorizarse el balance perceptual.

---

## 8. Peso visual

Todos los iconos de una colección deben presentar una densidad visual comparable. No deberían coexistir icono extremadamente ligero, icono extremadamente denso o icono excesivamente detallado dentro del mismo nivel jerárquico.

---

## 9. Complejidad

Eliminar detalles que no sean necesarios para reconocer el concepto.

Principio: un icono debe contener la menor cantidad de información gráfica necesaria para comunicar correctamente su significado.

Evitar: microdetalles; texturas; decoración innecesaria; formas redundantes; exceso de líneas; sombras internas.

---

## 10. Tamaños

Tokens recomendados:

| Token | Tamaño | Uso |
|---|---|---|
| icon.xs | 12–14 px | metadata |
| icon.sm | 16 px | inputs / tablas |
| icon.md | 20 px | controles |
| icon.base | 24 px | estándar |
| icon.lg | 28–32 px | acciones prominentes |
| icon.xl | 40–48 px | estados / empty states |

No aumentar arbitrariamente el stroke al reducir el icono.

---

## 11. Icono visual vs área interactiva

Estos conceptos deben mantenerse separados. Un icono puede medir 16, 20 o 24 px mientras su botón mide 44 × 44 px.

```text
┌──────────────────┐
│                  │
│      [20px]      │ 44px
│                  │
└──────────────────┘
       44px
```

---

## 12. Target size

WCAG 2.2 SC 2.5.8 establece para nivel AA un target mínimo de 24 × 24 CSS px, con determinadas excepciones. WCAG SC 2.5.5 establece como criterio AAA 44 × 44 CSS px. Lucide recomienda también 44 × 44 px para controles iconográficos.

Por tanto, el estándar interno recomendado será: `preferred target size = 44 × 44 px`.

---

## 13. Iconos interactivos

Un SVG no debe convertirse directamente en botón.

Evitar:

```html
<Trash2 @click="remove()" />
```

Preferir:

```html
<button type="button">
    <Trash2 aria-hidden="true" />
    <span class="sr-only">Eliminar</span>
</button>
```

---

## 14. Teclado

Los controles iconográficos deben conservar comportamiento estándar de teclado. Un botón debe poder activarse mediante `Enter` y `Space`. Siempre que sea posible utilizar `<button>` en lugar de `<div role="button">`. El HTML nativo ya incorpora buena parte del comportamiento esperado.

---

## 15. Accessible Name

Un control icon-only necesita un nombre accesible. Visualmente `[ 🔍 ]`; semánticamente `Buscar`; no `Icono de lupa`. El nombre describe el propósito, no la ilustración.

---

## 16. Iconos decorativos

Si existe `[+] Agregar usuario`, el lector de pantalla no debería recibir `Plus Agregar usuario`; debe recibir simplemente `Agregar usuario, botón`. Por tanto:

```html
<button>
    <Plus aria-hidden="true" />
    Agregar usuario
</button>
```

Lucide establece `aria-hidden="true"` por defecto en sus iconos.

---

## 17. Icon-only buttons

Para controles únicamente iconográficos:

```html
<button>
    <Search aria-hidden="true" />
    <span class="sr-only">Buscar</span>
</button>
```

También puede utilizarse un mecanismo apropiado de accessible name, pero el nombre debe pertenecer al control, no al dibujo SVG.

---

## 18. Label in Name

Si visualmente aparece `Descargar`, el accessible name debería contener `Descargar` y no cambiar arbitrariamente a `Obtener archivo`. Esto facilita especialmente tecnologías de control por voz. Relacionado con WCAG 2.5.3 — Label in Name.

---

## 19. Visible labels

Para acciones importantes se recomienda `[Pencil] Editar`, `[Trash] Eliminar`, `[Download] Descargar` frente a `[Pencil] [Trash] [Download]`.

Icon-only debe utilizarse principalmente cuando: el símbolo sea altamente reconocido; el contexto sea evidente; exista poco espacio; el control tenga accessible name; exista mecanismo de descubrimiento apropiado.

---

## 20. Tooltips

Un tooltip puede ayudar a descubrir el significado de un IconButton. Pero: **tooltip ≠ accessible name**. El control debe ser accesible incluso si el tooltip nunca aparece.

Un tooltip debe: funcionar mediante hover; funcionar mediante focus; poder cerrarse con Escape; estar asociado semánticamente; no contener controles interactivos. Para contenido interactivo utilizar otro patrón, como popover.

---

## 21. Color

Nunca utilizar exclusivamente color para comunicar: error; éxito; warning; selección; disponibilidad; prioridad; estado.

Incorrecto: `● verde`, `● rojo`. Mejor: `✓ Correcto`, `✕ Error`, `⚠ Advertencia`.

El color puede reforzar el significado. No debe ser el único portador del significado. Relacionado con WCAG 1.4.1 — Use of Color.

---

## 22. Contraste

Para elementos gráficos necesarios para comprender la interfaz debe evaluarse WCAG 1.4.11 — Non-text Contrast. El umbral habitual aplicable es 3:1. Lucide adopta en su guía una recomendación conservadora de 4.5:1.

Para este Design System:
- Objetivo recomendado: ≥ 4.5:1 cuando sea viable.
- Nunca incumplir el criterio WCAG aplicable.

---

## 23. Estados de interacción

Todo IconButton debería contemplar: default; hover; focus-visible; active; pressed; selected; disabled; loading. Los estados no deben depender exclusivamente de color.

---

## 24. Focus

El foco debe ser claramente perceptible. Nunca `outline: none;` sin proporcionar un indicador alternativo adecuado.

El indicador debe: contrastar; rodear o identificar claramente el control; no quedar recortado; mantenerse visible sobre diferentes fondos.

---

## 25. Toggle icons

Ejemplo: Mute. Un toggle puede utilizar `aria-pressed="true"` o `aria-pressed="false"`. Cuando se utiliza `aria-pressed`, WAI-ARIA APG recomienda mantener estable el nombre del botón: `Mute` con `aria-pressed=false` y posteriormente `Mute` con `aria-pressed=true`. El estado ya comunica la diferencia.

---

## 26. Disclosure icons

Un chevron puede representar expansión (`▶ collapsed`, `▼ expanded`), pero el estado real debe existir programáticamente: `aria-expanded="false"` o `aria-expanded="true"`. El chevron es feedback visual. No es el estado semántico.

---

## 27. Animación de iconos

La animación debe utilizarse con intención. Un icono puede animarse para comunicar: cambio de estado; feedback; progreso; causalidad; transición; atención temporal. No debe animarse simplemente para hacer la interfaz más llamativa.

---

## 28. Categorías de motion

- **State transition.** Ejemplo: `ChevronDown → ChevronUp`. Puede utilizar rotación.
- **Feedback.** Ejemplo: `Save → Check`. Comunica que una acción terminó.
- **Progress.** Ejemplo: `LoaderCircle`. Indica procesamiento real.
- **Attention.** Ejemplo: `Bell`. Debe utilizarse con extrema moderación.
- **Decorative motion.** Ejemplo: `Sparkles`, bounce, floating. Debe evitarse por defecto.

---

## 29. Motion tokens

| Token | Duración | Uso |
|---|---|---|
| motion.instant | 0–80 ms | cambio inmediato |
| motion.fast | 100–160 ms | feedback |
| motion.base | 160–240 ms | transición |
| motion.slow | 240–400 ms | cambio espacial |
| motion.loop | variable | progreso real |

Estos rangos son una decisión del Design System, no requisitos WCAG.

---

## 30. Principios de movimiento

Una animación debería ser: purposeful; brief; predictable; reversible; interruptible; non-blocking.

Evitar: excessive bounce; large zoom; continuous shake; parallax innecesario; oscillation; multiple simultaneous motions.

---

## 31. Reduced Motion

Debe respetarse:

```css
@media (prefers-reduced-motion: reduce) {
    .icon-motion {
        animation: none;
        transition: none;
    }
}
```

Importante: reduced motion no significa reproducir exactamente la misma animación más lentamente. En algunos casos eso puede incluso prolongar la exposición al movimiento.

Preferir `movement ↓ instant state change` o `movement ↓ subtle opacity change`, siempre conservando la información.

---

## 32. Animación iniciada por interacción

WCAG 2.3.3 aborda animaciones disparadas por interacción. Cuando el movimiento no sea esencial debe existir una forma de evitarlo o respetarse la preferencia correspondiente.

Ejemplos: expand, collapse, open, close, switch, navigation transition — deben disponer de una variante reducida cuando utilicen movimiento significativo.

---

## 33. Animaciones automáticas

WCAG 2.2.2 aborda contenido que: comienza automáticamente; contiene movimiento; dura más de cinco segundos; aparece junto a otro contenido. Cuando aplica, debe poder: pause, stop, hide — salvo que sea esencial.

Política recomendada: no utilizar loops decorativos automáticos persistentes.

---

## 34. Flashing

No utilizar flashing para llamar la atención. Especialmente evitar: rapid brightness changes; alternating high contrast; strobe effects; rapid blinking.

WCAG contiene criterios específicos destinados a reducir el riesgo de conv… *(texto recibido incompleto a partir de aquí)*
