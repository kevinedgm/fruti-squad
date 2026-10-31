# Convia · QR de mesa r3 (kit con el sello Convia)

Pedido del usuario (2026-10-31): desarrollar la propuesta B de r2 (sello Convia) en las piezas reales. Publicado: https://claude.ai/artifact/TGYP9fFFkD5UMiHRiStuNK · generar con `python3 gen.py <dir>`.

**El lugar pone el nombre y el color; Convia pone el sello.** Un solo sello para las tres piezas: anillo del color del lugar con su nombre en el arco, «Menú · Escanea · Scan» abajo, estrellas de Convia a las 3 y a las 9, aro punteado y el QR al centro sobre blanco pleno.

## Cambio respecto a r2
El disco blanco crece (radio 79 → 92 en la caja de 240) y el anillo adelgaza. Motivo: con la proporción de r2, en la tarjeta de barra el QR quedaba en ~2 cm; así llega a 2.5 cm con su margen blanco. El nombre reduce su tamaño solo si es largo (cabe en el arco).

## Piezas (medidas reales en mm, botón «Imprimir a tamaño real»)
| Pieza | Medida | Sello | QR con margen |
|---|---|---|---|
| Calca redonda | 8 cm | 80 mm | 3.9 cm |
| Tarjeta de mesa | 10 × 14 cm | 80 mm arriba; debajo «Escanea / Scan» y «Acerca tu teléfono / Tap your phone»; dirección corta; franja del color con «Mesa N» y «Menú en Convia» | 3.9 cm |
| Tarjeta de barra | 5.5 × 8.5 cm | 51 mm; acción; franja con «Carta en Convia» | 2.5 cm |

Controles: establecimiento, color (muestras o libre), número de mesa, con o sin NFC. En impresión se ocultan los controles y las tarjetas llevan línea de corte punteada.

## Color
- Texto sobre el color: blanco si contraste ≥ 4.5:1, si no tinta.
- QR en el color del lugar solo con contraste ≥ 7:1; si no, tinta y aviso en pantalla.

## Verificación
- Playwright 1300 y 390 px y vista de impresión: sin desbordes ni errores JS; sin choques de texto ni de texto con íconos (medido) con y sin NFC, color oscuro y claro, mesa de dos dígitos.
- El QR local es un simulador; **escaneo con teléfono: no verificado**. Dominio «convia.mx» sin confirmar.
