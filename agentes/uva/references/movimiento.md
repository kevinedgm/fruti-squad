# Movimiento en iconos (E4)

El movimiento existe para comunicar **estado o proceso** (cargando, sincronizando, un proceso de producción en curso). Si no comunica algo, no se anima. La norma (§27–34 de `estandar-iconografia.md`) manda; este archivo da los patrones CSS. En los ejemplos, `x` es el `semanticName` del icono.

## Categorías y tokens (norma §28–29)

| Categoría | Ejemplo | Duración |
|---|---|---|
| State transition | chevron que gira al expandir | `motion.base` 160–240 ms |
| Feedback | guardar → check | `motion.fast` 100–160 ms |
| Progress | proceso real en curso | `motion.loop`: ciclos de 1.6–2.4 s, máximo 2 (límite de 5 s) |
| Attention | campana | con extrema moderación |
| Decorative | brillos, rebotes, flotación | **no se propone** |

Los tokens `fast`, `base` y `slow` (§29) rigen transiciones y feedback; el progreso usa `motion.loop`, cuya duración la norma deja variable. Para progreso, Uva usa ciclos de 1.6–2.4 s.

Principios (§30): con propósito, breve, predecible, reversible, interrumpible, sin bloquear. Evitar rebote excesivo, zoom grande, sacudida continua, oscilación y varios movimientos simultáneos.

**Qué cuenta como "varios movimientos simultáneos" (interpretación de Uva):** dos movimientos **distintos** a la vez (algo gira mientras otra cosa rebota). El **mismo** movimiento repetido en varias partículas escalonadas (varias burbujas que suben igual) es un solo movimiento. Un efecto encadenado (un flujo que recorre un camino y, al terminar, cae una gota) también cuenta como uno, porque no se superponen en el tiempo.

## Límites (WCAG, bloqueantes)

- **≤5 s en total** (2.2.2 Pause, Stop, Hide): repeticiones finitas (`… 2` en vez de `infinite`) y al final un **fotograma estático con significado**. Un `infinite` solo es aceptable si la interfaz ofrece pausar o detener.
- **Movimiento reducido** (2.3.3, técnica C39): `@media (prefers-reduced-motion: reduce)` deja el fotograma estático.
- **Sin destellos** (2.3.1): nada cambia de opacidad de forma brusca más de 3 veces por segundo.

`scripts/check-icon.mjs` calcula la duración total (retraso + duración × repeticiones) y falla si supera 5 s o si hay `infinite`.

## Estados que duran mucho (horas o días)

Un proceso real puede durar mucho más que 5 s. El icono **no** acompaña todo el estado con movimiento:

1. **Mientras el estado dura, el icono es estático**: su fotograma final ya dice el estado.
2. **El movimiento se reproduce al entrar en el estado** (el lote pasa a "en proceso") y, si el producto lo necesita, al volver a mostrarlo (al abrir la vista, o al pasar el puntero o el foco por la fila). Para repetirlo, el componente vuelve a montar el icono o le cambia la clase.
3. Si la interfaz necesita indicar actividad continua (un proceso que el usuario está esperando), eso es un indicador de progreso con control para pausar, y le corresponde al componente, no al icono.

Uva lo indica en las recomendaciones de uso del handoff.

## Dos tipos

| Tipo | Qué es | Cuándo |
|---|---|---|
| Interpolado | Una pieza cambia de forma continua (gira, se desplaza, se desvanece) | Procesos continuos |
| Por cuadros | Una forma se sustituye por otra (`steps()`) | Indicadores tipo spinner de glifos, parpadeos de estado |

## Patrones

Convención: cada pieza animada lleva su propia clase con prefijo (`uva-x__pieza`) y cada regla usa una sola clase.

### Rotación de una pieza
```css
.uva-x__aspas{transform-box:fill-box;transform-origin:center;animation:uva-x-girar 2s linear 0s 2}
@keyframes uva-x-girar{to{transform:rotate(360deg)}}
```
`transform-box: fill-box` hace que `center` sea el centro de la pieza, no del SVG.

### Trazo que se dibuja
```html
<path class="uva-x__linea" pathLength="1" d="…"/>
```
```css
.uva-x__linea{stroke-dasharray:1;stroke-dashoffset:1;animation:uva-x-dibujar .6s cubic-bezier(.2,.6,.3,1) forwards}
@keyframes uva-x-dibujar{to{stroke-dashoffset:0}}
```

### Flujo a lo largo de un camino
Duplica el camino, dale un guion corto y desplázalo. `pathLength` hace que los números no dependan de la longitud real; el guion se oculta al terminar.
```html
<path class="uva-x__flujo" pathLength="33" d="(mismo d que el camino)"/>
```
```css
.uva-x__flujo{opacity:0;stroke:var(--uva-accent,currentColor);stroke-dasharray:3 30;animation:uva-x-fluir 2.2s linear 0s 2}
@keyframes uva-x-fluir{from{opacity:1;stroke-dashoffset:33}to{opacity:1;stroke-dashoffset:0}}
```

### Partículas que aparecen, se desplazan y se asientan
```css
.uva-x__particula{opacity:0;animation:uva-x-subir 1.6s cubic-bezier(.2,.6,.3,1) 0s 2,uva-x-asentar .4s ease-out 3.2s forwards}
.uva-x__particula:nth-of-type(2){animation:uva-x-subir 1.6s cubic-bezier(.2,.6,.3,1) .6s 2,uva-x-asentar .4s ease-out 3.8s forwards}
@keyframes uva-x-subir{0%{transform:translateY(2px);opacity:0}30%{opacity:1}100%{transform:translateY(-3px);opacity:0}}
@keyframes uva-x-asentar{to{opacity:1}}
```
Dos animaciones encadenadas: la segunda empieza cuando termina la primera (retraso = retraso + duración × repeticiones) y con `forwards` deja la pieza visible. El escalonado va en el shorthand de cada regla para que `check-icon` calcule el total exacto.

### Causa y efecto (dos piezas encadenadas)
Misma duración y repeticiones para ambas; la segunda arranca dentro del ciclo con un `0%,60%{opacity:0}` en su keyframe, para que aparezca cuando la primera termina su recorrido.

## Valores

| Propósito | Duración | Curva |
|---|---|---|
| Ciclos de progreso (×2) | 1.6–2.4 s | `linear` (flujo, giro) o `cubic-bezier(.2,.6,.3,1)` (subir/desvanecer) |
| Caída | dentro del ciclo | `cubic-bezier(.5,0,.9,.6)` (acelera) |
| Entrada única (dibujo) | 0.4–0.8 s | `cubic-bezier(.2,.6,.3,1)` |

- Anima solo `transform`, `opacity` y `stroke-dashoffset` (baratos, sin reflujo).
- Desplazamientos pequeños: 2–5 unidades de la cuadrícula.

## Movimiento reducido (obligatorio)

Movimiento reducido **no** es la misma animación más lenta (prolonga la exposición, §31). Se sustituye por un cambio instantáneo de estado o un cambio sutil de opacidad, conservando la información.

```css
@media (prefers-reduced-motion:reduce){
  .uva-x__particula,.uva-x__particula:nth-of-type(n){animation:none;opacity:1}  /* queda el fotograma que explica el estado */
  .uva-x__flujo{animation:none;opacity:0}                                      /* lo que solo tiene sentido en movimiento, se oculta */
}
```
`:nth-of-type(n)` iguala la especificidad de las reglas escalonadas. Comprueba en `banco.html#reducido` que el fotograma estático **sigue comunicando** el estado; es el mismo que queda al terminar la animación normal (`banco.html#final`).
