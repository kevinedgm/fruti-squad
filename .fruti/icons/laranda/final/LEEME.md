# Laranda · paquete de marca

Decisión (2026-10-22): flor dibujada a mano (ronda 4 B, línea media y desfase largo = B2), paleta intensa y neutra en género (ronda 8), Bricolage Grotesque + Onest (ronda 6, par 4). La jacaranda sin la jota: no se ilustra el árbol, se captura el instante de florecer.

## El símbolo

Línea de tinta a mano (cinco lóbulos abiertos, 3.2 de grosor en 128), mancha violeta plana desfasada (8, 7), el lóbulo superior derecho separado y en naranja, garganta vacía con anillo. El desfase es fijo: misma dirección en todas las piezas. De 16 a 32 px se usa la silueta (cinco discos, uno separado, garganta vacía).

## Color

| Token | Valor | Uso |
|---|---|---|
| violeta | #5B3BB5 | marca, acción primaria, mancha |
| violeta-presionado | #4A2DA8 | presionado, texto grande |
| lila / niebla | #C4B5F0 / #ECE7FA | hover, chips, fondos de foco; en oscuro, la marca |
| naranja | #E0611A | acento: lóbulo separado, enlaces, destacados; texto solo grande |
| naranja-tinte / naranja-oscuro | #F2C9B2 / #F2A074 | fondos de sección / acento en oscuro |
| oro | #D9A400 | **solo** Reservar y confirmación de cita; texto en tinta |
| verde / rojo | #0E8F5E / #A8202F | éxito / error, siempre con icono y texto |
| tinta / tinta-suave | #15121C / #4F4B57 | texto |
| hueso / arena | #F6F4EF / #EAE6DE | fondo / tarjetas |

Pruebas en `pruebas.md` y `png/daltonismo.png`.

## Tipografía

Bricolage Grotesque 600 (opsz 96) para wordmark y títulos; Onest 400/500/700 para interfaz y cuerpo; IBM Plex Mono 500 para folios. El wordmark va en trazados, caja baja, sin brote en la l (el brote se probó y se descartó).

## Archivos

| Archivo | Uso |
|---|---|
| `svg/simbolo*.svg` | claro, oscuro (línea hueso, mancha lila), tinta, blanco |
| `svg/silueta*.svg` · `png/favicon-{16,32,48}.png` · `png/favicon.ico` | 16–32 px; `favicon.svg` cambia con el esquema |
| `svg/app-icon*.svg` · `png/icon-{1024,512,192}.png` · `icon-maskable-512.png` | PWA, iOS, Android adaptativo (margen 20 %) |
| `svg/avatar.svg` · `png/avatar-512.png` | redes, recortado en círculo |
| `svg/wordmark*.svg` · `svg/lockup-h*.svg` · `svg/lockup-v*.svg` | nombre y lockups; mínimos 80 / 120 / 80 px |
| `svg/sello.svg` · `sello-emitido.svg` | la flor como estado: folio emitido, verificado |
| `svg/simbolo-bloom.svg` · `png/simbolo-bloom.gif` | animación de 500 ms; con «reducir movimiento», abierta |
| `svg/tarjeta-redes.svg` · `png/tarjeta-redes.png` | 1200×630 |
| `tema.json` | tokens y reglas |
| `gen.py` | `python gen.py <carpeta de fuentes>` |
| `lamina.html` / `lamina.png` | todo en una hoja |

Manual de uso: artifact (ver `../guia/`).
