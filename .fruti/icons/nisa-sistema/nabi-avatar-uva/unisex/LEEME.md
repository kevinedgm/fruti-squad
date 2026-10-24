# Nabi · avatar unisex

Una sola figura para todas las personas: la cara de la ronda 4 (A), fiel a la referencia de Notion. La persona solo elige el fondo.

- `user-avatar.svg`: lienzo 128 sin círculo; el componente pone el círculo de color y `color` (blanco o #121826, el de más contraste).
- Excepción a Uva: no usa la retícula 24 (A1) porque a 1.5 de trazo en 24 la cara se desarma. Conserva currentColor, extremos redondos y `aria-hidden` (el nombre va al lado).
- La familia de 4 (`../user-avatar-*`) queda descartada: la persona pidió una sola cara unisex.
- `python3 gen.py <scratchpad>` regenera el SVG y `vista.html`.
