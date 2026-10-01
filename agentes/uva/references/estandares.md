# Estándares para evaluar iconos (E3)

Rúbrica que aplica la norma de Uva (`estandar-iconografia.md`, citada como §n) a cada prototipo. Si esta rúbrica y la norma discrepan, gana la norma.

Cada criterio indica **fuente**, **qué se mide** y **cómo se comprueba**. Un criterio `bloqueante` que falla descarta la variante o obliga a iterarla; uno `recomendado` se reporta y se justifica si no se cumple.

Fuentes consultadas (2026-10): guía de diseño de iconos de Lucide, iconos de sistema de Material Design, iconografía de IBM Carbon, Apple HIG (iconos y SF Symbols), investigación de usabilidad de iconos de Nielsen Norman Group y WCAG 2.2.

## S · Selección y semántica (E1)

Nota: el ejemplo de la norma §2.1 usa `category: destructive-action`, que no figura en la taxonomía de §3; Uva lo trata como `action` (subtipo destructivo) y lo señala como pendiente de aclarar en la norma.

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| S1 | `semanticName` (que es también el id del icono) y categoría de la taxonomía definidos antes de dibujar | Norma §2.1, §3 | bloqueante | `brief.md` |
| S2 | Búsqueda en Lucide registrada; si un icono existente sirve, se recomienda ese | Norma §2.2, §4 | bloqueante | `scripts/buscar-lucide.mjs` + brief |
| S3 | Mismo significado → mismo icono; significados distintos → iconos distintos dentro del producto | Norma §2.4–2.5 | bloqueante | brief: conflictos revisados |
| S4 | Una marca de tercero no se sustituye con un icono genérico | Norma §3.10 | bloqueante | categoría ≠ brand |

## A · Construcción (geometría)

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| A1 | Lienzo 24×24 (`viewBox="0 0 24 24"`) | Lucide, Material | bloqueante | `scripts/check-icon.mjs` |
| A2 | Contenido (incluido el trazo) a ≥1 unidad del borde; zona viva recomendada 20×20 (margen 2). El margen de 2 puede ceder para igualar peso óptico (R6); el de 1, nunca | Lucide (≥1), Material (zona viva 20) | bloqueante ≥1 / recomendado 2 | propuesta: margen mínimo |
| A3 | Grosor uniforme en todo el icono (curvas, rectas, interiores y exteriores) | Material, Lucide, Apple | bloqueante | `check-icon` (un solo `stroke-width` raíz, sin sobrescrituras) |
| A4 | Uniones redondas; extremos abiertos con terminación redonda | Lucide | bloqueante (ADN base) | `check-icon` |
| A5 | Esquinas de 90°: radio 2 si el elemento mide ≥8, radio 1 si mide <8 | Lucide; Material (radio 2 por defecto) | recomendado | inspección en el banco a 96px |
| A6 | Separación visible (medida entre los **bordes** de los trazos, no entre sus ejes) entre elementos distintos y huecos interiores ≥ el grosor de la familia (Lucide: 2 con trazo 2; con trazo 1.5, ≥1.5; ver `decisions` en `uva.yaml`) | Lucide, norma §6 | bloqueante | banco a 20–24px: ¿se tocan o empastan? |
| A7 | Formas basadas en las figuras clave (círculo, cuadrado, rectángulos) para proporciones coherentes con la familia | Material (keylines) | recomendado | comparar masa con vecinos (R6) |
| A8 | Centrado óptico, no geométrico, en iconos asimétricos | Apple HIG | recomendado | banco: ¿se ve descentrado junto a sus vecinos? |
| A9 | A 16px: trazo y margen se reducen proporcionalmente (Carbon: 1px de trazo y 1px de margen a 16px; 2 y 2 a 32px) | IBM Carbon | recomendado si se usa a 16px | variante `.small` (R7) |
| A10 | El trazo no aumenta al reducir el tamaño | Norma §10 | bloqueante | `--uva-stroke` único en la familia |

**Nota sobre el grosor:** Lucide usa 2 y el ADN base de Uva usa 1.5, por preferencia de estilo. Si el icono convive con una librería, `--uva-stroke` debe igualar el grosor de esa librería (Lucide acepta `strokeWidth`).

## B · Reconocimiento y significado

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| B1 | **Reconocible:** a su tamaño real se identifica qué objeto es | NN/g (reconocibilidad) | bloqueante | banco a 20–24px; prueba de 5 segundos con una persona sin contexto si la hay; si no, se anota «sin prueba con personas» y el veredicto sale del banco |
| B2 | **Interpretable:** en su contexto se entiende qué *significa* (estado, acción) | NN/g (interpretación ≠ reconocimiento) | bloqueante | E1 define el significado; el movimiento o el modificador lo refuerzan |
| B3 | Silueta clara con la menor información gráfica necesaria: sin microdetalles, texturas, formas redundantes ni sombras internas | Apple HIG, norma §9 | bloqueante | R1: tapar el detalle; ¿la silueta sola basta? |
| B4 | No se confunde con iconos del mismo dominio | Regla R5 de Uva | bloqueante | banco con las confusiones declaradas en E1 y las que aparecieron al renderizar |
| B5 | Lleva **etiqueta de texto** visible salvo que sea universal (solo casa, imprimir y lupa lo son) | NN/g | recomendado (decisión del producto) | E1 pregunta si habrá etiqueta; la propuesta lo indica |
| B6 | Coherente con la familia: mismo trazo, terminaciones, radios y peso óptico | Apple, Lucide, R6 | bloqueante | banco: fila de familia |

## C · Accesibilidad

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| C1 | Contraste ≥3:1 contra el fondo cuando el icono transmite información, **para el trazo y para el acento** si el acento lleva significado | WCAG 2.2 · 1.4.11 (AA) | bloqueante | propuesta: contraste del trazo y del acento, en claro y oscuro |
| C1b | Contraste ≥4.5:1 cuando sea viable | Norma §22 (criterio conservador de Lucide) | recomendado | propuesta: aviso si queda entre 3 y 4.5 |
| C2 | **Oculto por defecto** (`aria-hidden="true"`). Nombre accesible (`role="img"` + `aria-label` o `<title>`) **solo** si el icono comunica algo esencial por sí solo; nunca las dos cosas a la vez | Lucide (accesibilidad), WCAG 1.1.1 | bloqueante | `check-icon` |
| C3 | El color no es el único portador del significado (la forma o la etiqueta también lo dicen) | WCAG 1.4.1 | bloqueante | ¿en gris sigue significando lo mismo? |
| C4 | En un botón solo con icono, el nombre accesible va **en el botón** (`aria-label` del `<button>`), y el icono queda oculto | Lucide (accesibilidad), WCAG 4.1.2 | bloqueante | E1 define el uso; la propuesta lo indica |
| C5 | El nombre accesible describe el propósito, no el dibujo, y contiene el texto visible si lo hay | Norma §15, §18; WCAG 2.5.3 | bloqueante | brief y `registro.yaml` (`defaultLabel`) |

## D · Movimiento

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| D1 | Movimiento automático **≤5 s** o con mecanismo para pausar/detener (p. ej. termina en un fotograma estático y se repite solo al entrar en el estado o al pasar el puntero o el foco). Si el estado dura más, el icono queda estático mientras dura | WCAG 2.2 · 2.2.2 (A) | bloqueante | `check-icon`: duración × repeticiones ≤ 5 s, o sin `infinite` |
| D2 | Respeta `prefers-reduced-motion` con cambio instantáneo o de opacidad sutil, nunca la misma animación más lenta; el fotograma estático sigue comunicando | WCAG 2.3.3 (AAA), técnica C39, norma §31 | bloqueante | `check-icon` + `banco.html#reducido` |
| D3 | Sin destellos: nada parpadea más de 3 veces por segundo | WCAG 2.3.1 (A) | bloqueante | revisar keyframes de opacidad |
| D4 | El movimiento pertenece a una categoría: state transition, feedback, progress o attention; nunca decorative | Norma §27–28 | bloqueante | brief / E4 |
| D5 | Los trazos animados con `stroke-dashoffset` llevan `pathLength` explícito | Política de Uva | bloqueante | `check-icon` (D5) |
| D6 | Duraciones dentro de los tokens de movimiento (fast 100–160 ms, base 160–240, slow 240–400; loop solo para progreso real) | Norma §29 | recomendado | revisar `animation` |
| D7 | Con propósito, breve, predecible, sin rebote excesivo, zoom grande, sacudida continua ni varios movimientos simultáneos (dos movimientos **distintos** a la vez; el mismo movimiento en varias partículas, o dos encadenados, cuentan como uno: ver `movimiento.md`) | Norma §30 | bloqueante | revisión en el banco (`#medio`) |

## U · Recomendaciones de uso (Uva las indica; no las implementa)

| # | Recomendación | Fuente |
|---|---|---|
| U1 | Área interactiva de 44×44 aunque el icono mida 16–24 (mínimo AA 24×24) | Norma §11–12; WCAG 2.5.8 / 2.5.5 |
| U2 | El SVG nunca es el botón: va dentro de `<button type="button">`, activable con Enter y Space | Norma §13–14 |
| U3 | Botón solo con icono: nombre en el botón (`sr-only` o `aria-label`); el tooltip no sustituye el nombre | Norma §17, §20 |
| U4 | Etiqueta visible en acciones importantes; solo icono cuando es muy reconocido y hay contexto | Norma §19, §2.3 |
| U5 | Toggle: `aria-pressed` con nombre estable; disclosure: `aria-expanded` (el chevron es solo feedback) | Norma §25–26 |
| U6 | Estados del botón (hover, focus-visible, pressed, disabled, loading) no solo por color; foco visible, nunca `outline: none` sin alternativa | Norma §23–24 |

## Cómo reportarlo

En la propuesta, cada variante lleva una tabla corta: criterio, ✅/❌/➖ (no aplica) y una línea de evidencia ("A6 ❌: a 24px las dos piezas se tocan"). No se presenta como recomendada una variante con un bloqueante en ❌.

## Fuentes

- Norma de Uva — Guía y estándar de iconografía accesible v1.0: `references/estandar-iconografia.md`

- Lucide — Icon design guide / specification: https://lucide.dev/contribute/icons/specification
- Material Design — System icons: https://material.io/design/iconography/system-icons.html
- IBM Carbon — Icons usage: https://carbondesignsystem.com/elements/icons/usage/
- Apple HIG — Icons: https://developer.apple.com/design/human-interface-guidelines/icons
- Nielsen Norman Group — Icon usability: https://www.nngroup.com/articles/icon-usability/
- Lucide — Accessibility: https://lucide.dev/how-to/accessibility
- WCAG 2.2 — 1.4.11 Non-text contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
- WCAG 2.2 — 2.2.2 Pause, Stop, Hide: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide
- WCAG 2.2 — 2.3.3 Animation from Interactions: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions
