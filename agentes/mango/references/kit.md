# Kit de Mango (`scripts/kit.mjs`)

Escena = un archivo `.mjs` que importa el kit y escribe el SVG:

```js
import { persona, objeto, ilustracion } from '<ruta>/scripts/kit.mjs';
import { writeFileSync } from 'node:fs';
const suelo = 292;
const p = persona({ x: 150, y: suelo, pose: 'senala', pelo: 'largo', piel: 'piel', ropa: 'acento' });
writeFileSync('ayuda-informa.svg', ilustracion({ id: 'ayuda-informa', titulo: 'Una persona señala un panel con una gráfica', partes: [
  objeto.mancha({ x: 40, y: 40, w: 400, h: 250 }), objeto.suelo({ x: 30, y: suelo + 2, w: 420 }),
  objeto.pizarra({ x: 222, y: 70, w: 196, h: 136 }), objeto.planta({ x: 430, y: suelo }),
  p.svg, objeto.burbuja({ x: 30, y: 40, w: 88, h: 50, cola: 'der' }),
]}));
```

## Piezas

| Pieza | Parámetros |
|---|---|
| `persona` | `x`, `y` (suelo), `escala`, `pose` (`de-pie`, `senala`, `saluda`, `sostiene`, `explica`), `pelo` (`corto`, `largo`, `rizado`, `moño`), `piel` (`piel`, `piel-2`, `piel-3`), `ropa`, `pantalon`, `zapato` (roles). Devuelve `{ svg, manoD, manoI }` (posición de las manos para colocar objetos) |
| `objeto.pizarra` | panel con gráfica de barras · `x, y, w, h` |
| `objeto.burbuja` | bocadillo con borde · `x, y, w, h, cola: 'izq'|'der'` |
| `objeto.planta` | maceta con dos hojas · `x, y` (suelo) |
| `objeto.mancha` | forma de fondo orgánica · `x, y, w, h` |
| `objeto.suelo` | línea de suelo · `x, y, w` |
| `objeto.puntos` | 6 puntos decorativos · `x, y` |
| `ilustracion` | `id`, `w`, `h`, `titulo`, `decorativa`, `partes`: envuelve, traduce roles a tokens, accesibilidad y oscuro |

Orden de pintado = orden de `partes`: fondo → suelo → objetos de atrás → personas → objetos de delante.

## Ampliar el kit

- **Pose nueva:** añade a `POSES` los ángulos `[hombro→codo, codo→mano]` de cada brazo (0° = derecha, 90° = abajo) y de cada pierna. Pruébala en una fila de poses antes de usarla.
- **Objeto nuevo:** función en `objeto` que devuelve formas con clases `{c}__<rol>` (relleno) o `{c}__trazo-<rol>` (trazo). Nunca un color.
- **Rol nuevo:** solo si ninguno existente sirve; añádelo a `ROLES` (y a `DARK` si cambia en oscuro) y a `references/contrato-svg.md`.
