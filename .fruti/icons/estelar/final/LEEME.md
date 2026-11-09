# Estelar · paquete de marca

Decidido con el usuario el 2026-11-09 (`../LEEME.md`): símbolo C1 (marca) + C3 (16–24 px), color Caracol con la estrella en color, letra combinación 3.

| Archivo | Uso |
|---|---|
| `svg/simbolo.svg` / `-oscuro`, `png/simbolo-512.png` / `-oscuro-512.png` | Estrella de 7 × 7 con urdimbre, desde 32 px |
| `svg/simbolo-16.svg` / `-16-oscuro` | Estrella de 5 × 5, para 16–24 px |
| `svg/simbolo-tinta.svg` | Una tinta (`currentColor`) |
| `svg/favicon.svg`, `png/favicon-32.png` | Favicon; el SVG cambia con el tema |
| `svg/app-icon.svg`, `app-icon-redondeado.svg`, `png/icon-192.png`, `icon-512.png`, `icon-redondeado-512.png` | Icono de app |
| `svg/wordmark.svg` / `-oscuro`, `png/wordmark*.png` | Símbolo + «Estelar» (Big Shoulders Display 800) + lema (Instrument Serif cursiva), en trazos |
| `svg/tarjeta-redes.svg`, `png/tarjeta-redes.png` | Vista previa de enlaces 1200 × 630 |
| `tema.json` | Color, contrastes, tipografía, símbolo y reglas |

Color: manta `#F6F1E8` / `#15171F`, tinta `#15171F` / `#F6F1E8` (15.9:1), caracol `#7B2D8E` / `#C98BDB` (7.2:1 · 7.0:1).
Regenerar: `python3 gen.py <carpeta con BigShouldersDisplay-ExtraBold.ttf e InstrumentSerif-Italic.ttf>` y `node png.cjs` (fuentes SIL OFL de Google Fonts; no se versionan).
Guía: `../guia/guia.html` (`python3 ../guia/gen.py`).
