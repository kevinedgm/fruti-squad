# Manik Impulsa · favicon

Prueba de simplificación del símbolo para 16–32 px (hallazgo 6 de `../auditoria.md`).

## Qué se probó

| Variante | Qué conserva | Resultado a 16 px real |
|---|---|---|
| Original reducido | globo + M con línea base | La línea base y los 4 picos se funden en un «peine» gris. |
| V1 · fiel | igual, trazos más gruesos | Mejora poco: sigue habiendo demasiadas piezas para 16 px. |
| V2 · sin línea base | solo la M | Se lee como «lh»: el valle central baja demasiado. |
| V2b | M con valle más corto, globo más grande | Mejor; los picos aún se tocan con el borde. |
| **V2c (elegida)** | M ancha y simétrica, trazo 3.8/32 | Se lee como M a 16 px en claro y oscuro. |
| V3 · mínima | un solo pulso | Muy legible, pero pierde la M: parece un icono de salud. |

Evidencia: `evidencia/variantes-16-32.png`, `evidencia/iteracion-v2.png` (ampliadas con vecino más cercano, 1 px = 1 cuadro), `evidencia/pestanas.png`.

## Mecanismo

A 16 px cada unidad del lienzo de 32 vale medio píxel. Un hueco recortado necesita ~1.5 px (3 unidades) para no desaparecer con el antialias. El original tiene 4 picos + 2 tramos de línea base dentro de ~12 px: no caben huecos de 1.5 px entre ellos. V2c deja 3 trazos y 2 huecos, que sí caben.

## Uso

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
```

A ≥48 px (apple-touch-icon, PWA, splash) usa el símbolo completo de `../manik-impulsa.svg`: ahí la línea base sí se lee.

## Decisiones

- **Aprobado (2026-10-05):** el favicon (16–32 px) va sin la línea base del pulso; a ≥48 px se usa el símbolo completo.

## Notas

- El color `#8f8fc6` sobre blanco da 3.04:1 sobre blanco (hallazgo 1 de la auditoría); en el favicon no bloquea porque la pestaña lleva el nombre en texto.
