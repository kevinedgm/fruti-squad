# Movimiento en iconos (U5)

El movimiento existe para comunicar **estado o proceso** (cargando, fermentando, destilando, sincronizando). Si no comunica algo, no se anima.

## Dos tipos

| Tipo | Qué es | Cuándo |
|---|---|---|
| Interpolado | Una pieza cambia de forma continua (gira, se desplaza, se desvanece) | Procesos continuos |
| Por cuadros | Una forma se sustituye por otra (`steps()`) | Indicadores tipo spinner de glifos, parpadeos de estado |

## Patrones

### Rotación de una pieza
```css
.uva-x .aspas{transform-box:fill-box;transform-origin:center;animation:uva-x-girar 2s linear infinite}
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
.uva-x .vapor{stroke:var(--uva-accent,currentColor);stroke-dasharray:3 30;stroke-dashoffset:33;animation:uva-x-fluir 2.4s linear infinite}
@keyframes uva-x-fluir{to{stroke-dashoffset:0}}
```

### Aparecer y desplazarse (burbujas, gotas)
```css
.uva-x .burbuja{opacity:0;animation:uva-x-subir 1.8s cubic-bezier(.2,.6,.3,1) infinite}
.uva-x .burbuja:nth-of-type(2){animation-delay:-.6s}
.uva-x .burbuja:nth-of-type(3){animation-delay:-1.2s}
@keyframes uva-x-subir{0%{transform:translateY(2px);opacity:0}30%{opacity:1}100%{transform:translateY(-3px);opacity:0}}
```
Retrasos **negativos** para que el ciclo ya esté en marcha desde el primer fotograma.

### Encadenar dos piezas (proceso con causa y efecto)
Misma duración para ambas y la segunda arranca dentro del ciclo con un `0%,60%{opacity:0}` en su keyframe (p. ej. el vapor recorre el tubo y luego cae la gota).

## Valores

| Propósito | Duración | Curva |
|---|---|---|
| Ciclos de proceso | 1.6–2.6s | `linear` (flujo, giro) o `cubic-bezier(.2,.6,.3,1)` (subir/desvanecer) |
| Caída | dentro del ciclo | `cubic-bezier(.5,0,.9,.6)` (acelera) |
| Entrada única (dibujo) | 0.4–0.8s | `cubic-bezier(.2,.6,.3,1)` |

- Anima solo `transform`, `opacity` y `stroke-dashoffset` (baratos, sin reflujo).
- Desplazamientos pequeños: 2–5 unidades de la cuadrícula.
- `infinite` solo mientras el estado es real; el componente que usa el icono decide cuándo quitar la clase o cambiar al icono estático.

## Movimiento reducido (obligatorio)

```css
@media (prefers-reduced-motion:reduce){
  .uva-x .burbuja{animation:none;opacity:1}   /* queda el fotograma que explica el estado */
  .uva-x .vapor{animation:none;opacity:0}     /* lo que solo tiene sentido en movimiento, se oculta */
}
```
Comprueba que el fotograma estático **sigue comunicando** el estado (la tina con burbujas quietas sigue diciendo "fermentando").
