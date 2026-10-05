# Auditoría · logo Manik Impulsa

Archivo auditado: `ManikImpulsaLogoFull.svg` (10 672 bytes; copia en `evidencia/original.svg`). Logo completo: símbolo (globo de conversación con una línea de pulso que forma una «M») + «Manik» (negrita) sobre «Impulsa» (ligera), un solo color `#8f8fc6`.
Etiquetas: **[Hecho]** medido o renderizado · **[Juicio]** lectura visual · **[Recomendación]**.
Alcance: Uva no diseña logotipos; aquí se aplican sus criterios de construcción, contraste y legibilidad.

## Resumen

| # | Hallazgo | Tipo | Gravedad |
|---|---|---|---|
| 1 | Contraste del lila sobre blanco 3.04:1 (justo en el mínimo) y 2.76:1 sobre gris claro | Hecho | media |
| 2 | «Impulsa» deja de leerse con el logo completo por debajo de ~120 px de ancho | Juicio | media |
| 3 | Sin margen lateral en el encuadre (0 / −0.1) y vertical descentrado (17 arriba, 31.6 abajo) | Hecho | baja |
| 4 | 14 `clipPath` idénticas que no recortan nada (0 píxeles de diferencia al quitarlas) | Hecho | baja |
| 5 | Color fijo en `style`, sin versión `currentColor`; sin `role`/`title`; `width`/`height` fijos | Hecho | baja |
| 6 | A 16 px el pulso se vuelve ruido; el globo se lee | Juicio | baja (símbolo) |

## Lo que funciona

- **[Juicio] Idea con doble lectura:** la línea de pulso dentro del globo dice «conversación + vitalidad / impulso» y, a la vez, dibuja la **M** de Manik. Es una buena síntesis.
- **[Hecho] Texto convertido a trazados:** no depende de fuentes instaladas.
- **[Hecho] Un solo color:** funciona en escala de grises y en monocromo sin cambios.
- **[Hecho] Sobre fondo oscuro** el lila llega a 5.4–6.9:1 (#1e1e2e … #000).

## Hallazgos

1. **Contraste en claro [Hecho].** `#8f8fc6` da 3.04:1 sobre blanco y 2.76:1 sobre `#f4f4f4`. WCAG exime a los logotipos del contraste de texto (1.4.3), así que no es un incumplimiento, pero «Impulsa» es de trazo fino y a tamaño pequeño se lava. **[Recomendación]** una variante para fondos claros del mismo tono: `#6e6eb5` (4.6:1 sobre blanco, 4.19:1 sobre `#f4f4f4`). Ver `evidencia/contraste-color.png`.
2. **Tamaño mínimo [Juicio].** A 160 px de ancho todo se lee; a 120 px «Impulsa» empieza a empastarse; a 80 px es ilegible (≈7 px de altura de x). **[Recomendación]** mínimo del logo completo: 140 px; por debajo, usar solo el símbolo.
3. **Encuadre [Hecho].** Medido renderizando sobre un lienzo ampliado: el dibujo ocupa x 129.3→930.3, y 89.9→371.9; el `viewBox` del archivo va de x 129.34→930.21, y 72.9→403.5. Márgenes: 0 a la izquierda, −0.1 a la derecha (la «k» y la «a» tocan el borde), 17 arriba y 31.6 abajo. El logo no queda centrado verticalmente en su caja y no tiene aire lateral. **[Recomendación]** `viewBox` ajustado al dibujo y el área de respeto definida en la guía de marca (p. ej. la altura de la «M» de Manik por lado), no dentro del archivo.
4. **Recortes inútiles [Hecho].** Las 14 `clipPath` recortan el mismo rectángulo de la mesa de trabajo de exportación. Quitándolas, el render es idéntico píxel a píxel (0 de 1 600 000 píxeles distintos con el mismo encuadre). Restos típicos de exportar desde PDF/Illustrator vía Inkscape, como las matrices con escala vertical negativa.
5. **Técnica [Hecho].** El color va en `style="fill:#8f8fc6"` repetido 14 veces; no hay versión que herede el color (`currentColor`) para usarlo en la interfaz con temas; falta nombre accesible (`role="img"` + `<title>`); `width`/`height` fijos (800.87×330.65) impiden que escale solo.
6. **Símbolo pequeño [Juicio].** A 64 px el pulso/M se lee bien; a 32 px aún se intuye; a 16 px el globo se reconoce pero el pulso es ruido y la cola del globo casi desaparece. Para favicon conviene una versión simplificada (pulso más grueso, menos picos) o aceptar que a 16 px solo se lea el globo.
7. **Observación [Juicio, confianza baja].** Donde la línea del pulso sale del globo (izquierda y derecha), el contorno del círculo termina en un tramo recto en lugar de completar la curva. Si se buscaba un círculo perfecto, es un pequeño defecto de trazado; si es intencional (el pulso «corta» el globo), está bien.

## Entregado

- `manik-impulsa.svg` — limpio: sin `clipPath` ni `id` sobrantes, color en un solo `fill`, `viewBox` ajustado al dibujo (+1 de holgura), `role="img"` + `<title>`. 5 540 bytes (−48 %). Mismo dibujo.
- `manik-impulsa-currentcolor.svg` — igual, con `fill="currentColor"` para la interfaz (toma el color del texto o del token del tema).
- `evidencia/` — original, tamaños y fondos, original contra limpio (borde ampliado), contraste del color.

## Pendiente (decisiones de marca, no técnicas)

- Adoptar o no la variante `#6e6eb5` para fondos claros.
- Fijar tamaño mínimo y área de respeto en la guía.
- Favicon: simplificar el símbolo o aceptar solo el globo a 16 px.
