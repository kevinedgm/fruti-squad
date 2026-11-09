# Xila · paquete de marca 2.0 (rediseño)

Decidido con el usuario el 2026-11-09 (`../LEEME.md`, rondas `../rediseno-r1` a `../rediseno-r8`): emblema «la x en el rombo» (Huipil + Letra bordada) con un dibujo por tamaño; color Añil; letra Familjen Grotesk (primaria) + Instrument Sans (secundaria). La identidad anterior (greca bordada) queda en `../final/` como historial.

| Archivo | Uso |
|---|---|
| `svg/simbolo-{grande,mediano,chico,favicon}.svg` | Emblema añil, un dibujo por tamaño (≥ 64 · 32–48 · 20–28 · 16 px) |
| `svg/simbolo-*-claro.svg` | Emblema manta para fondos oscuros o de color |
| `svg/wordmark.svg` / `-oscuro`, `svg/lockup.svg` / `-oscuro` | «xila» en punto de cruz; con el emblema |
| `svg/favicon.svg` | Favicon que cambia con el tema |
| `svg/app-icon.svg`, `app-icon-redondeado.svg`, `png/icon-*.png` | Icono de app |
| `svg/tarjeta-redes.svg`, `png/tarjeta-redes.png` | Vista previa 1200 × 630 (lema en Familjen Grotesk, en trazos) |
| `png/favicon-{16,32,48}.png`, `png/simbolo-*-512.png`, `png/lockup*.png` | Rasterizados |
| `tema.json` | Color, contrastes, tipografía, reglas |
| `guia.html` | Guía de marca (`python3 guia.py`) |

Color: añil #16255C, añil medio #2F4FA8 (6.6:1 sobre manta), añil claro #7FA0E0 (5.5:1 sobre añil), manta #F4F1EA (12.8:1).
Regenerar: `python3 gen.py <carpeta con FamiljenGrotesk-SemiBold.ttf> && node png.cjs && python3 guia.py`.
Pendiente: llevar `tema.json` y los SVG al repositorio de la librería.
