# Contrato técnico de la ilustración (I3, I5)

La columna **Verifica** es el código de `scripts/check-ilustracion.mjs`; «manual» se revisa en el banco.

| Regla | Verifica |
|---|---|
| XML válido: ningún comentario contiene `--` (si no, no abre como `<img>`) | X1 (+ banco: «abre como imagen») |
| `viewBox="0 0 w h"` (lienzo base 480×320; otras proporciones según la sección; el grosor de línea escala con el ancho) | A1 |
| Sin `width`/`height` en la raíz: la sección decide el tamaño | A2 |
| Raíz con clases `mango-ilu mango-<id>` | ID |
| Color solo por roles: `.mango-<id>{--m-<rol>:var(--mango-<rol>,<defecto>)}` y formas con `.mango-<id>__<rol>`; ningún color fijo fuera de esos valores por defecto | COL1 |
| Paleta de 2–8 roles | COL2 (recomendado) |
| Dentro de un `<mask>` los colores (`#fff`/`#000`) son luminancia, no color visible: se permiten | COL1 los ignora |
| Una clase por regla, sin combinadores (sobrevive a `<use>` y a empaquetados) | SEL |
| Clases e ids con prefijo `mango-<id>` (dos ilustraciones en una página no chocan) | ID2, ID3 |
| Decorativa: `aria-hidden="true"`. Informativa: `role="img"` + `<title id="mango-<id>-t">` que describe la escena (`aria-labelledby`). Nunca las dos | C1 |
| Peso ≤30 KB (máximo 60) | P1 |
| Todo vectorial: sin `<image>` ni `data:image` | P2 |
| Sin `<filter>` ni `<foreignObject>` | P3 (recomendado) |
| Si se mueve: ≤5 s, termina quieto y bloque `prefers-reduced-motion` | M1 (+ manual) |
| Como `<img src>` no hereda los tokens de la página: sale con los valores por defecto (avisarlo al entregar; para que tome el tema, inline) | manual |

## Roles de color

`fondo` (rectángulo de fondo), `tinta` (líneas, ojos, masas oscuras), `papel` (relleno de personas y objetos claros), `acento` (el foco), `acento-2` (segundo color, opcional). Token: `--mango-<rol>`. Valores por defecto y de modo oscuro: `ROLES` y `DARK` en `scripts/kit.mjs`. Las líneas son formas rellenas de grosor variable con la clase `mango-<id>__trazo` (relleno `tinta`; grosor base 4.8, fina 2.8). El proyecto conecta los roles a sus tokens:

```css
:root { --mango-fondo: var(--color-brand-soft); --mango-acento: var(--color-brand); --mango-tinta: var(--color-ink); }
```
