# SAM · Simple Activity Manager · marca

Identidad congelada el 2026-11-13. Proceso y rondas: `../identidad/LEEME.md`.

## Qué es
- **Símbolo «Tarjetas»:** una tarjeta de actividad pasa adelante y queda completada; la anterior queda detrás, en contorno («ya pasó»). Dice lo que el equipo hace todo el día en SAM.
- **Color Voltaje `#c6f432`:** relleno, nunca texto. Siempre toca tinta: texto oscuro encima y, en tema claro, contorno de tinta. En claro, texto, enlaces y foco van en tinta.
- **Letra Onest** (OFL) en marca e interfaz (400–700); **JetBrains Mono** para folios, horas y datos.

## Archivos
| Archivo | Para qué |
|---|---|
| `sam-simbolo.svg` | Símbolo desde 32 px (C2). Inline hereda `currentColor` (tinta), `--g-color-brand` (lima) y `--sam-tinta` (palomita) |
| `sam-simbolo-chico.svg` | 16–24 px (C4): tarjetas más separadas y trazos más gruesos |
| `sam-logotipo-{horizontal,vertical,compacto}.svg` | Logotipo con variables (inline). Horizontal: barra de la app y documentos; vertical: portada e inicio; compacto: espacios chicos |
| `…-sobre-oscuro.svg`, `…-sobre-claro.svg` | Mismos logotipos con colores fijos, para `<img>`, correos y documentos (una imagen no ve el CSS de la página) |
| `favicon.svg` | Favicon (C4); cambia la tinta con el tema del navegador |
| `favicon-32.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` | Respaldo PNG e iconos de la PWA (fondo noche) |
| `maskable-512.png` | Icono adaptable de Android: símbolo en la zona segura (300 de 512) |
| `sam-notificacion.svg`, `notificacion-96.png` | Icono pequeño de notificación push: silueta blanca de una tinta |
| `sam-marca.css` | Tokens: `--g-color-brand` para Grana, tinta, noche, papel y fuentes |
| `manifest.fragmento.json` | Nombre, colores e iconos para el manifest de la PWA |
| `muestra.html`, `muestra.png` | Todo junto, en oscuro y claro |

El nombre está convertido a trazos: los SVG no dependen de la fuente.

## Reglas
- No deformar, rotar ni recolorear el símbolo; no separar la palomita de la tarjeta lima.
- Lima sobre papel mide 1.1:1: en claro nunca sin contorno de tinta ni como texto.
- Por debajo de 32 px usar `sam-simbolo-chico.svg`.
- Área libre alrededor del logotipo: la altura de la tarjeta lima.

## Regenerar
`python3 -I gen.py <carpeta con onest-500.ttf y onest-700.ttf>` y después `node render.cjs` (PNG con el Chromium de Playwright). Las fuentes se descargan de Google Fonts y no se versionan.

## No verificado
Prueba en celulares reales (instalación de la PWA, máscara de Android, icono de notificación) y renderizado del favicon SVG en Safari.
