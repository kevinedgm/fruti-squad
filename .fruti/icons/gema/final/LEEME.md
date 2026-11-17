# GEMA · Gestión de Muestras y Análisis · marca

Identidad congelada el 2026-11-17. Proceso: `../identidad/LEEME.md`. Referencia de estilo: SAM.

## Qué es
- **Símbolo «Pantalla + Resultado»:** el marco de un instrumento con la señal de un análisis; el pico mayor, el del resultado, lleva el color.
- **Color «degradado navy»:** `#052A76 → #3D67AE`, del azul de Nisa Nabani. El degradado solo vive en superficies de marca (pico, icono de la app, panel de inicio de sesión). En la interfaz el color es plano: navy en claro, `#3D67AE` en oscuro, siempre con texto blanco.
- **Letra Onest** (la misma de SAM) en marca e interfaz; JetBrains Mono para folios, valores y unidades.

## Archivos
| Archivo | Para qué |
|---|---|
| `gema-simbolo.svg` | Desde 32 px. En línea hereda `currentColor` y el degradado de `--gema-pico-a/-b` |
| `gema-simbolo-chico.svg` | 16–24 px: marco grueso y solo el pico del resultado |
| `gema-logotipo-{horizontal,vertical,compacto}.svg` | Con variables, para usar en línea |
| `…-sobre-claro.svg`, `…-sobre-oscuro.svg` | Colores fijos, para `<img>`, correos y documentos |
| `favicon.svg`, `favicon-32.png` | Pestaña; el SVG cambia con el tema del navegador |
| `icon-192.png`, `icon-512.png`, `maskable-512.png`, `apple-touch-icon.png` | PWA, sobre el degradado navy |
| `gema-notificacion.svg`, `notificacion-96.png` | Silueta blanca: marco y pico calado |
| `gema-marca.css` | Tokens: `--g-color-brand` (claro y oscuro), degradado, tinta, papel y fuentes |
| `manifest.fragmento.json` | Nombre, colores e iconos de la PWA |

Texto convertido a trazos (Onest, OFL). Regenerar: `python3 -I gen.py <carpeta con onest-500.ttf y onest-700.ttf>` y `node render.cjs`.

## Reglas
- Degradado solo en superficies de marca; botones, chips y enlaces en color plano.
- En oscuro, `#3D67AE` mide 3.5:1 sobre negro: sirve para botones con texto blanco, nunca como texto.
- Por debajo de 32 px, el símbolo chico.

## No verificado
Dispositivos reales (instalación de la PWA, máscara de Android, notificación) y favicon SVG en Safari. Nombre sin verificar en IMPI ni dominios.
**unresolved:** Verdant (skill `nisa`) frente a Grana (resumen de producto).
