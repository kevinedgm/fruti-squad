# Movimiento en iconos (E4)

El movimiento existe para comunicar **estado o proceso** (cargando, fermentando, destilando, sincronizando). Si no comunica algo, no se anima.

## Límites (WCAG, bloqueantes)

- **≤5 s en total** (2.2.2 Pause, Stop, Hide): repeticiones finitas (`… 2` en vez de `infinite`) y al final un **fotograma estático con significado**. Para repetir, el componente vuelve a montar el icono o cambia de estado. Un `infinite` solo es aceptable si la interfaz ofrece pausar/detener.
- **Movimiento reducido** (2.3.3, técnica C39): `@media (prefers-reduced-motion: reduce)` deja el fotograma estático.
- **Sin destellos** (2.3.1): nada cambia de opacidad de forma brusca más de 3 veces por segundo.

`scripts/check-icon.mjs` calcula la duración total (retraso + duración × repeticiones) y falla si supera 5 s o si hay `infinite`.

## Dos tipos

| Tipo | Qué es | Cuándo |
|---|---|---|
| Interpolado | Una pieza cambia de forma continua (gira, se desplaza, se desvanece) | Procesos continuos |
| Por cuadros | Una forma se sustituye por otra (`steps()`) | Indicadores tipo spinner de glifos, parpadeos de estado |

## Patrones

### Rotación de una pieza
```css
.uva-x .aspas{transform-box:fill-box;transform-origin:center;animation:uva-x-girar 2s linear 2}
@keyframes uva-x-girar{to{transform:rotate(360deg)}}
```
`transform-box: fill-box` hace que `center` sea el centro de la pieza, no del SVG.

### Trazo que se dibuja
```html
<path class="linea" pathLength="1" d="…"/>
```
```css
.uva-x .linea{stroke-dasharray:1;stroke-dashoffset:1;animation:uva-x-dibujar .6s cubic-bezier(.2,.6,.3,1) forwards}
@keyframes uva-x-dibujar{to{stroke-dashoffset:0}}
```

### Flujo a lo largo de un camino (vapor por un tubo)
Duplica el camino, dale un guion corto y desplázalo. `pathLength` hace que los números no dependan de la longitud real.
```html
<path class="vapor" pathLength="33" d="(mismo d que el tubo)"/>
```
```css
.uva-x .vapor{opacity:0;stroke:var(--uva-accent,currentColor);stroke-dasharray:3 30;animation:uva-x-fluir 2.2s linear 0s 2}
@keyframes uva-x-fluir{from{opacity:1;stroke-dashoffset:33}to{opacity:1;stroke-dashoffset:0}}
```

### Aparecer y desplazarse, y asentarse al final (burbujas, gotas)
```css
.uva-x .burbuja{opacity:0;animation:uva-x-subir 1.6s cubic-bezier(.2,.6,.3,1) 0s 2,uva-x-asentar .4s ease-out 3.2s forwards}
.uva-x .burbuja:nth-of-type(2){animation:uva-x-subir 1.6s cubic-bezier(.2,.6,.3,1) .6s 2,uva-x-asentar .4s ease-out 3.8s forwards}
@keyframes uva-x-subir{0%{transform:translateY(2px);opacity:0}30%{opacity:1}100%{transform:translateY(-3px);opacity:0}}
@keyframes uva-x-asentar{to{opacity:1}}
```
Dos animaciones encadenadas: la segunda empieza cuando termina la primera (retraso = retraso + duración × repeticiones) y con `forwards` deja la pieza visible. El escalonado va en el shorthand de cada regla para que `check-icon` calcule el total exacto.

### Encadenar dos piezas (proceso con causa y efecto)
Misma duración y repeticiones para ambas; la segunda arranca dentro del ciclo con un `0%,60%{opacity:0}` en su keyframe (el vapor recorre el tubo y luego cae la gota). Ver `examples/alambique.svg`.

## Valores

| Propósito | Duración | Curva |
|---|---|---|
| Ciclos de proceso (×2) | 1.6–2.4s | `linear` (flujo, giro) o `cubic-bezier(.2,.6,.3,1)` (subir/desvanecer) |
| Caída | dentro del ciclo | `cubic-bezier(.5,0,.9,.6)` (acelera) |
| Entrada única (dibujo) | 0.4–0.8s | `cubic-bezier(.2,.6,.3,1)` |

- Anima solo `transform`, `opacity` y `stroke-dashoffset` (baratos, sin reflujo).
- Desplazamientos pequeños: 2–5 unidades de la cuadrícula.

## Movimiento reducido (obligatorio)

```css
@media (prefers-reduced-motion:reduce){
  .uva-x .burbuja,.uva-x .burbuja:nth-of-type(n){animation:none;opacity:1}   /* queda el fotograma que explica el estado; :nth-of-type(n) iguala la especificidad de las reglas escalonadas */
  .uva-x .vapor{animation:none;opacity:0}     /* lo que solo tiene sentido en movimiento, se oculta */
}
```
Comprueba que el fotograma estático **sigue comunicando** el estado (la tina con burbujas quietas sigue diciendo "fermentando"). El mismo fotograma es el que queda al terminar la animación normal.
