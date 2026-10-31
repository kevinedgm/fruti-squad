# Convia · QR de mesa r2 (tres propuestas)

Pedido del usuario (2026-10-31): el difuminado de r1.2 «se ve raro y pierde la identidad». Tres propuestas distintas, tomando como referencia la calca tipo sticker de r1.1, para integrar el QR sin que se vea raro. Libertad creativa: estrella, logo o forma de sello de Convia.

Publicado: https://claude.ai/artifact/TAQBWS9iKZWys8DrpR9USr · generar con `python3 gen.py <dir>` (lee `plantilla.html`, `../convia-final/svg/` y los datos de ejemplo de `gen.py`).

## Regla común
El QR nunca se deforma ni se tapa: siempre va sobre blanco pleno con su margen de 4 módulos. La identidad la pone el **marco**, no el código.

| | Pieza | Cómo integra el QR | Fuerza | Riesgo |
|---|---|---|---|---|
| A · Calca estrella | sticker recortado 9 cm | panel blanco punteado encima de la estrella del color del lugar | la estrella entera y reconocible | el panel cubre el centro de la estrella |
| B · Sello Convia | calca redonda / posavasos 8 cm | el QR es el centro de un sello redondo como los sellos de giro; nombre y «Menú · Escanea · Scan» en arco | el QR cabe natural en el círculo; se siente oficial | la estrella es pequeña (separadores) |
| C · Etiqueta con estrella calada | ficha 6.2 × 10 cm | banda del color con la estrella perforada; línea de corte; QR abajo | QR grande y limpio; detalle de imprenta memorable | perforar (suajado) cuesta más |

## Color
- Texto sobre el color del lugar: blanco si el contraste es ≥ 4.5:1, si no tinta.
- Módulos del QR en el color del lugar solo si su contraste con blanco es ≥ 7:1; si no, tinta.
- Corregido en prueba: `#fff` de 3 dígitos rompía el cálculo de contraste (texto oscuro sobre fondo oscuro); ahora se compara con `#ffffff`.

## Verificación
- Playwright 1300 y 390 px: sin desbordes, sin errores JS, ningún texto sale de su pieza.
- El QR de la prueba local es un simulador (no escanea); en el artefacto publicado el QR se genera con qrcode-generator 1.4.4. **Escaneo con teléfono: no verificado.**
- **Elegida por el usuario (2026-10-31): B · Sello Convia.** Siguiente: llevar el sello a las piezas reales (calca, tarjeta de mesa, tarjeta de barra) e impresión a tamaño real.
