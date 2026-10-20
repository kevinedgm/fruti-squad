# Conectti · paquete C: la ligadura tt

Decisión: dirección C de la ronda 2. Las dos t de «conectti» comparten una barra en verde azulado que sobresale como marca de calibración; el punto de la i repite el acento. El símbolo es la tt sola.

Colores y tipografía vienen del Design System Conectti (sin tema oscuro): cobalto `#1D52BB`, cobalto fuerte `#0439A1`, verde azulado `#057F7D`; sobre cobalto la barra usa `#5FD6CF`. Nombre en IBM Plex Sans 600 convertido a trazados.

| Archivo | Uso |
|---|---|
| `svg/simbolo.svg`, `simbolo-tinta.svg`, `simbolo-inverso.svg` | Símbolo a color, en una tinta, sobre cobalto. |
| `svg/simbolo-16.svg` | Versión para 16–24 px: trazos más gruesos. |
| `svg/favicon.svg` | Favicon con `prefers-color-scheme` (cobalto / blanco). `png/favicon.ico` 16·32·48. |
| `svg/app-icon.svg`, `app-icon-redondeado.svg` | App icon 512: bloque cobalto, tt blanca. `png/icon-512.png`, `icon-192.png`. |
| `svg/wordmark*.svg`, `lockup*.svg` | Logotipo en minúsculas y lockup horizontal (color, tinta, inverso). |
| `login.html` | Pantalla de acceso según el DS (7fr/5fr, arte con degradado y vidrio, cromatograma). Capturas en `png/login-*.png`. |
| `lamina.html` / `lamina.png` | App icon en pantalla de inicio, favicon en pestaña clara y oscura, logotipo. |
| `gen.py` | Genera los SVG: `python gen.py <carpeta con IBMPlexSans.ttf>` |

Pendiente: aprobación del usuario; después, actualizar la línea «Conectti aún no tiene logotipo» del README del DS y subir los assets al artifact.
