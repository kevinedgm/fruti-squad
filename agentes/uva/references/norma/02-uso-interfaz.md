# Norma de Uva · uso en la interfaz

> Parte de la *Guía y estándar de iconografía accesible* v1.0 (secciones §11–26). Índice y notas: `README.md` de esta carpeta. Se carga solo en E5: Uva no implementa estas secciones, las convierte en recomendaciones de uso.

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
