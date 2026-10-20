# Conectti · identidad de marca

Plataforma para un laboratorio de control de calidad (bebidas alcohólicas, agua, alimentos, análisis clínicos). Antecedente visual: el logotipo de NisaNabani (azul marino + verde lima, onda/matraz).

Fuente de color y tipografía: el Design System Conectti (artifact `HZXXi7qbLBVxJXySU16efT`): cobalto `#1D52BB` (brand), `#0439A1` (brand-strong), verde azulado `#057F7D` (accent), texto `#111820`, fondo `#F4F7FA`; IBM Plex Sans 600 para el nombre. Tema claro único, como el DS. El propio README del DS dice que Conectti aún no tiene logotipo: esta carpeta lo resuelve.

## Ronda 1 (`ronda-1/`)
- A · nodos y marca de calibración: muestra y resultado conectados, con la rayita del instrumento en medio.
- B · la doble t como eslabón: las dos t de Conectti comparten la barra, que es el enlace.
- C · la onda del resultado: pico sobre línea base dentro de un anillo; hereda la onda de NisaNabani.
- D · la C en red: anillo de nodos conectados que no cierra; el nodo de acento es el resultado que entra.

`python gen.py <carpeta con IBMPlexSans.ttf>` genera `banco.html`; `banco.png` es la captura.
