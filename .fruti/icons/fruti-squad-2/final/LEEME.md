# Fruti Squad · paquete final de marca (identidad nueva)

Decisiones del usuario (2026-10-30), rondas en `../r1` a `../r20-tipo`:
- Nombre «Fruti Squad», para Codex, Kiro y Claude Code (sin «for Kiro»). Identidad desde cero; la anterior queda en `../../fruti-squad/`.
- Sistema abstracto «Átomos»: marcos redondeados en trazo 3.5 y un punto lleno, la evidencia que cada agente produce y entrega.
- Símbolos (uno por uno, desde el nombre de producto):

| Id | Producto | Símbolo | Color vivo (oscuro) · claro |
|---|---|---|---|
| squad | Fruti Squad Workflow Pack | Espiral (marcos anidados girando) | degradado de los cinco |
| kiwi | Kiwi UX Architect | Tres tamaños (compact, medium, expanded) | #34e0a1 · #0f9e6e |
| lima | Lima Design System Governance | Biblioteca (marcos apilados) | #d4ff3a · #6f8c00 |
| coco | Coco UI Audit | Visor (esquinas que encuadran) | #ff9f1c · #c26a00 |
| bruno | Bruno Frontend Implementation Engineer | Cierre (diagonal tipo </>, plano punteado → pieza sólida) | #4361ee · #3a54d6 |
| mora | Mora Documentation & Knowledge Engineer | Red de conocimiento | #f72585 · #d0156e |

- Color: duotono. Trazo neutro (tinta #18181b en claro, blanco en oscuro); el punto en el color de quien firma la evidencia.
- Letra: Bricolage Grotesque (OFL), 700 nombre y 400 producto; en los SVG, convertida a trazos.

## Archivos (por integrante, en `<id>/`)
- `svg/simbolo.svg` (claro), `simbolo-oscuro.svg`, `simbolo-tinta.svg` (currentColor), `favicon.svg` (cambia con el tema).
- `svg/lockup.svg`, `lockup-oscuro.svg`: símbolo + nombre + producto.
- `svg/app-icon.svg` (cuadro oscuro). `png/`: app icon 512 y 192, símbolo claro y oscuro 512.
- `tema.json` (colores, reglas, contrastes), `gen.py` (`python3 gen.py <carpeta con BricolageGrotesque[opsz,wdth,wght].ttf>`), `png.cjs`, `lamina.html` / `lamina.png`.

## Contraste del punto (elemento gráfico, mínimo 3:1)
Vivo sobre #0f0f12: Kiwi 11.2, Lima 16.6, Coco 9.3, Bruno 3.8, Mora 5.1. Claro sobre blanco: Kiwi 3.4, Lima 3.9, Coco 3.9, Bruno 6.1, Mora 5.2.

## Pendiente
- Guía de marca y kit de marketplace (portada, banner, capturas, textos cortos).
- Precios iniciales por producto.
- Sustituir los avatares del paquete (`.fruti/assets/avatars/`) cuando se apruebe la guía.
