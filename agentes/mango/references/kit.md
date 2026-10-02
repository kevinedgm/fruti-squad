# Kit de Mango (`scripts/kit.mjs`) · estilo línea de rotulador

Escena = un `.mjs` que importa el kit, fija la semilla y escribe el SVG:

```js
import { semilla, cabeza, torso, brazo, mano, rayitas, objeto, ilustracion } from '<ruta>/scripts/kit.mjs';
import { writeFileSync } from 'node:fs';
semilla(23);                                                    // mismo dibujo en cada regeneración
const cuello = [372, 214], s = 1.15;
const t = torso({ x: cuello[0], y: cuello[1], s, flip: true });  // se asoma por la derecha, mira a la izquierda
const c = cabeza({ x: cuello[0], y: cuello[1], s, flip: true, pelo: 'corto' });
const b = brazo({ desde: t.hombro, hasta: [236, 214], ancho: 46, curva: -0.08 });
const m = mano({ x: b.muneca[0], y: b.muneca[1], rot: b.angulo - 180, flip: true, gesto: 'cuenco', s: 1.05 });
writeFileSync('presenta.svg', ilustracion({ id: 'presenta', titulo: 'Una persona se asoma y presenta algo', partes: [
  t.svg, c.svg, b.svg, objeto.grana({ cx: m.apoyo[0], base: m.apoyo[1] + 4, t: 5 }), m.svg,
  rayitas({ cx: m.apoyo[0], cy: m.apoyo[1] - 60, r: 70 }) ] }));
```

## Piezas

| Pieza | Parámetros y retorno |
|---|---|
| `semilla(n)` | fija el temblor (M3) |
| `trazoOrganico(pts, {cerrado, ancho, temblor})` | la línea de mano: cinta rellena con presión variable, grano y extremos que se pasan (M3); `linea()` la usa |
| `trazo(pts, {cerrado, temblor, paso})` | contorno suave con temblor, para los rellenos |
| `linea(pts, {fina, cerrado, temblor})` / `relleno(rol, pts, {desplaza})` | línea de tinta (gruesa 4.8 o fina 2.8) / forma rellena (con desplazamiento opcional, M4) |
| `tf(pts, {x, y, s, rot, flip})` | transforma puntos antes del temblor (el temblor no se escala) |
| `brazo({desde, hasta, ancho, curva, puno})` | manga de papel con puño → `{ svg, muneca, angulo }` |
| `mano({x, y, rot, s, flip, gesto})` | `cuenco` (palma arriba, sostiene), `senala` (índice), `abierta` (saludar, chocar) → `{ svg, apoyo }`. Con el brazo hacia la izquierda: `flip: true, rot: angulo - 180` |
| `cabeza({x, y, s, flip, pelo, cara})` | perfil con cara mínima; (x, y) = base del cuello por delante · `pelo`: `corto`, `largo`, `barba`, `ninguno` · `cara`: `sonrie`, `serio` |
| `torso({x, y, s, flip, rol, alto})` | hombros y pecho de perfil que salen por abajo → `{ svg, hombro }` |
| `figura({x, y, H, dir, pose, pelo, cara, camisa, pantalon, zapato, gestos})` | **persona de cuerpo entero con canon** (M10): (x, y) = suelo bajo la cadera, H = alto de la cabeza; `pose` = nombre de `POSES` (`de-pie`, `camina`, `senala`, `sostiene`, `sentado`) u objeto con ángulos; `gestos` = `{ cerca, lejos }` (`manopla` por defecto, `senala`, `cuenco`, `abierta`) → `{ svg, manoCerca, manoLejos }`. La línea se afina sola en figuras pequeñas |
| `CANON`, `POSES` | proporciones en cabezas y ángulos de articulación; una pose nueva = solo ángulos |
| `agujero({x, y, rx, ry})` | agujero de tinta del que sale o al que entra algo |
| `rayitas({cx, cy, r, n, de, a, largo})` | rayitas de «¡ta-dá!» en arco |
| `objeto.grana({cx, base, t, rol, desplaza})` | la cochinilla de Grana (objeto de marca) |
| `ilustracion({id, w, h, titulo, decorativa, fondo, partes})` | envuelve: fondo, roles → tokens, grosores, accesibilidad, oscuro |

Orden de pintado = orden de `partes`: torso → cabeza → brazo → objeto sostenido → mano (encima, M5) → rayitas.

## Ampliar el kit

- **Gesto de mano nuevo:** añade a `MANOS` el contorno (muñeca en (0,0), mirando a la derecha, de -22 a 22), los pliegues y el `apoyo`. Pruébalo en una hoja de manos que salen de agujeros antes de usarlo.
- **Objeto nuevo:** función en `objeto` que combina `linea` y `relleno` con roles; nunca un color.
- **Rol nuevo:** solo si ninguno sirve; añádelo a `ROLES` (y a `DARK`) y a `references/contrato-svg.md`.
