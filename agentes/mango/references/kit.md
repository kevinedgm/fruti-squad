# Kit de Mango (`scripts/kit.mjs`) · estilo línea de rotulador

Escena = un `.mjs` que importa el kit, fija la semilla y escribe el SVG:

```js
import { semilla, cabezaPerfil as cabeza, torso, brazo, mano, rayitas, objeto, ilustracion } from '<ruta>/scripts/kit.mjs';
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
| `linea(pts, {fina, cerrado, temblor})` / `relleno(rol, pts, {desplaza})` | línea de tinta (gruesa 4.4 o fina 2.6, peso estable) / forma rellena (con desplazamiento opcional, M4) |
| `tf(pts, {x, y, s, rot, flip})` | transforma puntos antes del temblor (el temblor no se escala) |
| `brazo({desde, hasta, ancho, curva, puno})` | manga de papel con puño → `{ svg, muneca, angulo }` |
| `mano({x, y, rot, s, flip, gesto})` | `cuenco` (palma arriba, sostiene), `senala` (índice), `abierta` (saludar, chocar) → `{ svg, apoyo }`. Con el brazo hacia la izquierda: `flip: true, rot: angulo - 180` |
| `cabeza({x, y, s, flip, rot, cara, pelo, expresion})` | **rostro 3/4 de la especificación**: (x, y) = barbilla, s = alto/100 · `cara`: `a`–`d` (`CARAS`) · `pelo`: `short-wave`, `crop`, `curls`, `bob`, `long`, `bun`, `ponytail`, `ninguno` (`PEINADOS`) · `expresion`: `neutral`, `happy`, `focused`, `curious`, `surprised`, `confused`, `concerned`, `relieved`, `proud`, `excited` (`EXPRESIONES`) → `{ atras, cuello, svg }` (pinta `atras`, luego `cuello`, el torso y `svg`) |
| `cabezaPerfil({x, y, s, flip, pelo, cara})` | cabeza de perfil anterior a la especificación (escenas existentes); `pelo`: `corto`, `largo`, `barba`, `ninguno` |
| `torso({x, y, s, flip, rol, alto})` | hombros y pecho de perfil que salen por abajo → `{ svg, hombro }` |
| `figura({x, y, H, dir, pose, cara, pelo, expresion, complexion, camisa, pantalon, zapato, gestos, enfasis})` | **persona 3/4 de cuerpo entero con el canon de la especificación** (M10): (x, y) = suelo bajo la cadera, H = alto de la cabeza; `pose` = nombre de `POSES` (`de-pie`, `camina`, `senala`, `sostiene`, `sentado`, `pulgar`) u objeto con ángulos; `complexion`: `slim`, `average`, `broad`; `gestos` = `{ cerca, lejos }` (`manopla` por defecto, `pulgar`, `senala`, `cuenco`, `abierta`); `enfasis` = escala de las manos (1 neutra, `CANON.enfasis.comunicativo` = 1,25) → `{ svg, manoCerca, manoLejos }`. La línea se afina sola en figuras pequeñas |
| `CANON`, `POSES` | proporciones en cabezas y ángulos de articulación; una pose nueva = solo ángulos |
| `agujero({x, y, rx, ry})` | agujero de tinta del que sale o al que entra algo |
| `rayitas({cx, cy, r, n, de, a, largo})` | rayitas de «¡ta-dá!» en arco |
| `objeto.grana({cx, base, t, rol, desplaza})` | la cochinilla de Grana (objeto de marca) |
| `objeto.laptop({cx, y, w, h, lineas, error, rolError})` | laptop de frente sobre una superficie (y); líneas de código y una línea de error resaltada (`error` = índice, -1 sin error) → `{ svg, error, borde }` |
| `objeto.mesa({x0, x1, y, suelo})` / `objeto.taburete({x, y, suelo, ancho})` | mesa de un pie (no cruza las piernas de quien se sienta a los lados) / taburete |
| `objeto.bicho({x, y, s, rot, rol})` | el «bug»: insecto pequeño con cuerpo de acento |
| `objeto.lupa({x, y, r, rot})` | lupa centrada en lo que examina → `{ svg, mango }` (mango = dónde va la mano, con `alcance`) |
| `figura({…, alcance})` | `alcance: { cerca, lejos }`: la muñeca llega a un punto [x, y] (cinemática inversa, codo abajo), o `{ hacia: [x, y] }` para señalarlo (la mano mira al objetivo). Una pose cuyo muslo va casi horizontal se trata como sentada. El pulgar arriba se dibuja siempre derecho |
| `ilustracion({id, w, h, titulo, decorativa, fondo, partes})` | envuelve: roles → tokens, accesibilidad, oscuro; `fondo` es `false` por defecto (fondo transparente, especificación); `true` pinta el rol `fondo` |

Orden de pintado = orden de `partes`: torso → cabeza → brazo → objeto sostenido → mano (encima, M5) → rayitas.

## Ampliar el kit

- **Gesto de mano nuevo:** añade a `MANOS` el contorno (muñeca en (0,0), mirando a la derecha, de -22 a 22), los pliegues y el `apoyo`. Pruébalo en una hoja de manos que salen de agujeros antes de usarlo.
- **Objeto nuevo:** función en `objeto` que combina `linea` y `relleno` con roles; nunca un color.
- **Rol nuevo:** solo si ninguno sirve; añádelo a `ROLES` (y a `DARK`) y a `references/contrato-svg.md`.
