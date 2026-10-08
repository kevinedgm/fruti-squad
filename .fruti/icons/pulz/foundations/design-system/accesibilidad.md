# Accesibilidad

Objetivo: **WCAG 2.2 AA**, verificable en cada componente.

| Regla | Cómo se comprueba |
|---|---|
| Texto ≥ 4.5:1; controles, iconos y bordes con significado ≥ 3:1 | Medido en la paleta (ver las notas de cada color); se vuelve a medir por componente |
| Objetivos ≥ 44 px con el dedo (`size-touch-min`), ≥ 24 px con ratón (`size-pointer-min`) | Inspección en los dos modos de entrada |
| Foco siempre visible: anillo `focus` de 3 px sólido con 3 px de separación | Recorrer cada pantalla con Tab |
| Ningún estado depende solo del color ni solo del icono | Cada estado lleva texto; prueba en escala de grises |
| `prefers-reduced-motion` respetado | Activar la preferencia y repetir las demos de movimiento |
| `forced-colors` (alto contraste de Windows) | El tanque y los chips conservan borde, no solo relleno |
| Todo operable con teclado | Sin atajos que dependan del ratón |
| Zoom 200 % | Sin scroll horizontal ni texto cortado |

Los iconos decorativos van `aria-hidden`; el nombre accesible lo da la etiqueta o el botón, y describe el propósito, no el dibujo («Registrar medición», no «icono de más»).
