# Nexa Squad · paquete final de marca

Decisiones del usuario (2026-11-08), rondas en `../r1` a `../r7-tipo`:
- Sistema **Huecos** (r5): un bloque 40×40 en lienzo 48, radio 7; el agente es el hueco, sacado de su `skills/<agente>/SKILL.md` en kevinedgm/nexa-squad.
- Color **B Cian** (r6): bloque neutro (tinta #16161B en claro, claro #F3F3EE en oscuro); hueco cian #22C3E6 en claro (8.60:1 contra tinta) y #00728A en oscuro (5.00:1 contra claro).
- Letra **Bricolage Grotesque** (r7), 700 nombre y 400 producto; en las firmas, convertida a trazos.

Por agente, en `<id>/`: `svg/simbolo.svg`, `simbolo-oscuro.svg`, `simbolo-tinta.svg` (currentColor, hueco transparente), `lockup.svg`, `lockup-oscuro.svg`, `app-icon.svg`, `favicon.svg` (cambia con el tema); `png/` app icon 512 y 192, símbolo claro y oscuro 512.
`tema.json` (color, contrastes, construcción, reglas, productos). Regenerar: `python3 gen.py <carpeta con BricolageGrotesque-Bold.ttf y -Regular.ttf>` y `node png.cjs`.
