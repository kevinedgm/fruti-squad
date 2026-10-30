# CLNDA Booking, Shop y Menú · paquete final

Decisiones del usuario (2026-10-30): patrón «CLNDA + palabra clara», familia C de nombres (Booking, Shop, Menú), sistema C de diferenciación (forma + color). La marca del producto la ve solo el negocio; el cliente final ve la marca del negocio y «hecho por CLNDA» (`../final/svg/firma.svg`).

## Sistema
- **Llave índigo constante** (#4338ca en claro, #8b8cf8 sobre tinta): lo que hace familia. Nunca toma el color del producto.
- **El dato es el objeto del oficio**, en el color del producto: Booking = hoja de calendario, Shop = etiqueta de precio, Menú = plato.
- Lockup: símbolo + CLNDA (Space Grotesk 700) + producto (Space Grotesk 400) en color, todo en trazados. Sin el cursor de CLNDA: la palabra del producto ocupa ese lugar.

## Color
| Producto | marca (objeto, palabra ≥ 24 px) | texto (< 24 px) | oscuro (sobre tinta) |
|---|---|---|---|
| Booking | #0891b2 (3.7:1) | #0e7490 (5.4:1) | #22d3ee (10.5:1) |
| Shop | #db2777 (4.6:1) | #be185d (6.0:1) | #f472b6 (7.2:1) |
| Menú | #ea580c (3.6:1) | #c2410c (5.2:1) | #fb923c (8.4:1) |

Validado con el validador de dataviz junto al índigo (PASS en daltonismo y contraste). En el panel, la acción primaria sigue siendo índigo; el color del producto es acento (icono activo, chip, gráfica principal).

## Archivos (por producto en `booking/`, `shop/`, `menu/`)
- `svg/simbolo*.svg`: claro, oscuro, tinta, blanco; `simbolo-16*` para 16–24 px (trazo más grueso, objeto 1.22×).
- `svg/favicon.svg` (cambia con `prefers-color-scheme`), `svg/app-icon*.svg`, `svg/lockup*.svg` (claro, oscuro, una tinta).
- `png/`: app icons 512/192, símbolo 512, favicon 32.
- `tema.json`, `gen.py` (`python3 gen.py <carpeta con SpaceGrotesk[wght].ttf>`), `png.cjs`, `lamina.html` / `lamina.png`.

## Pendiente
- Verificación IMPI de los tres nombres.
- Qué hace CLNDA Menú (menú digital, reservas, pedidos): el plato sirve para los tres.
