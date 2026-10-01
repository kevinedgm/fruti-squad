# Estándares para evaluar iconos (E3)

Rúbrica que Uva aplica a cada prototipo. Cada criterio indica **fuente**, **qué se mide** y **cómo se comprueba**. Un criterio `bloqueante` que falla descarta la variante o obliga a iterarla; uno `recomendado` se reporta y se justifica si no se cumple.

Fuentes consultadas (2026-10): guía de diseño de iconos de Lucide, iconos de sistema de Material Design, iconografía de IBM Carbon, Apple HIG (iconos y SF Symbols), investigación de usabilidad de iconos de Nielsen Norman Group y WCAG 2.2.

## A · Construcción (geometría)

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| A1 | Lienzo 24×24 (`viewBox="0 0 24 24"`) | Lucide, Material | bloqueante | `scripts/check-icon.mjs` |
| A2 | Contenido (incluido el trazo) a ≥1 unidad del borde; zona viva recomendada 20×20 (margen 2) | Lucide (≥1), Material (zona viva 20) | bloqueante ≥1 / recomendado 2 | banco: panel de medidas |
| A3 | Grosor uniforme en todo el icono (curvas, rectas, interiores y exteriores) | Material, Lucide, Apple | bloqueante | `check-icon` (un solo `stroke-width` raíz, sin sobrescrituras) |
| A4 | Uniones redondas; extremos abiertos con terminación redonda | Lucide | bloqueante (ADN base) | `check-icon` |
| A5 | Esquinas de 90°: radio 2 si el elemento mide ≥8, radio 1 si mide <8 | Lucide; Material (radio 2 por defecto) | recomendado | inspección en el banco a 96px |
| A6 | Separación ≥2 unidades entre elementos distintos y huecos interiores ≥2 | Lucide | bloqueante | banco a 24px: ¿se tocan o empastan? |
| A7 | Formas basadas en las figuras clave (círculo, cuadrado, rectángulos) para proporciones coherentes con la familia | Material (keylines) | recomendado | comparar masa con vecinos (R6) |
| A8 | Centrado óptico, no geométrico, en iconos asimétricos | Apple HIG | recomendado | banco: ¿se ve descentrado junto a sus vecinos? |
| A9 | A 16px: trazo y margen se reducen proporcionalmente (Carbon: 1px de trazo y 1px de margen a 16px; 2 y 2 a 32px) | IBM Carbon | recomendado si se usa a 16px | variante `.small` (R7) |

**Nota sobre el grosor:** Lucide usa 2 y el ADN base de Uva usa 1.5, por preferencia de estilo. Si el icono convive con una librería, `--uva-stroke` debe igualar el grosor de esa librería (Lucide acepta `strokeWidth`).

## B · Reconocimiento y significado

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| B1 | **Reconocible:** a su tamaño real se identifica qué objeto es | NN/g (reconocibilidad) | bloqueante | banco a 22–24px; prueba de 5 segundos con una persona sin contexto, si es posible |
| B2 | **Interpretable:** en su contexto se entiende qué *significa* (estado, acción) | NN/g (interpretación ≠ reconocimiento) | bloqueante | E1 define el significado; el movimiento o el modificador lo refuerzan |
| B3 | Silueta clara con formas reducidas a lo esencial | Apple HIG | bloqueante | R1: tapar el detalle; ¿la silueta sola basta? |
| B4 | No se confunde con iconos del mismo dominio | Regla R5 de Uva | bloqueante | banco con 2–3 confusiones declaradas |
| B5 | Lleva **etiqueta de texto** visible salvo que sea universal (solo casa, imprimir y lupa lo son) | NN/g | recomendado (decisión del producto) | E1 pregunta si habrá etiqueta; la propuesta lo indica |
| B6 | Coherente con la familia: mismo trazo, terminaciones, radios y peso óptico | Apple, Lucide, R6 | bloqueante | banco: fila de familia |

## C · Accesibilidad

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| C1 | Contraste ≥3:1 contra el fondo cuando el icono transmite información | WCAG 2.2 · 1.4.11 (AA) | bloqueante | propuesta: lectura de contraste para cada color/fondo |
| C2 | **Oculto por defecto** (`aria-hidden="true"`). Nombre accesible (`role="img"` + `aria-label` o `<title>`) **solo** si el icono comunica algo esencial por sí solo; nunca las dos cosas a la vez | Lucide (accesibilidad), WCAG 1.1.1 | bloqueante | `check-icon` |
| C4 | En un botón solo con icono, el nombre accesible va **en el botón** (`aria-label` del `<button>`), y el icono queda oculto | Lucide (accesibilidad), WCAG 4.1.2 | bloqueante | E1 define el uso; la propuesta lo indica |
| C3 | El color no es el único portador del significado (la forma o la etiqueta también lo dicen) | WCAG 1.4.1 | bloqueante | ¿en gris sigue significando lo mismo? |

## D · Movimiento

| # | Criterio | Fuente | Nivel | Cómo comprobar |
|---|---|---|---|---|
| D1 | Movimiento automático **≤5 s** o con mecanismo para pausar/detener (p. ej. termina en un fotograma estático y se repite solo al cambiar de estado o al pasar el puntero) | WCAG 2.2 · 2.2.2 (A) | bloqueante | `check-icon`: duración × repeticiones ≤ 5 s, o sin `infinite` |
| D2 | Respeta `prefers-reduced-motion`; el fotograma estático sigue comunicando | WCAG 2.3.3 (AAA), técnica C39 | bloqueante (política de Uva) | `check-icon` + captura con `--force-prefers-reduced-motion` |
| D3 | Sin destellos: nada parpadea más de 3 veces por segundo | WCAG 2.3.1 (A) | bloqueante | revisar keyframes de opacidad |
| D4 | El movimiento expresa un estado o proceso, no decoración | Política de Uva | bloqueante | E1: ¿qué significa el movimiento? |

## Cómo reportarlo

En la propuesta, cada variante lleva una tabla corta: criterio, ✅/❌/➖ (no aplica) y una línea de evidencia ("A6 ❌: a 24px el serpentín toca la olla"). No se presenta como recomendada una variante con un bloqueante en ❌.

## Fuentes

- Lucide — Icon design guide / specification: https://lucide.dev/contribute/icons/specification
- Material Design — System icons: https://material.io/design/iconography/system-icons.html
- IBM Carbon — Icons usage: https://carbondesignsystem.com/elements/icons/usage/
- Apple HIG — Icons: https://developer.apple.com/design/human-interface-guidelines/icons
- Nielsen Norman Group — Icon usability: https://www.nngroup.com/articles/icon-usability/
- Lucide — Accessibility: https://lucide.dev/how-to/accessibility
- WCAG 2.2 — 1.4.11 Non-text contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
- WCAG 2.2 — 2.2.2 Pause, Stop, Hide: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide
- WCAG 2.2 — 2.3.3 Animation from Interactions: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions
