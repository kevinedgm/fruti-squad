# Fruti Squad · icono 24 px

Elegida: Espiral con núcleo (2026-10-08). Propuestas: `../squad-propuesta/`. Generador común: `../squad-build.py`.

Cinco módulos en espiral alrededor del núcleo lima: especialistas distintos funcionando como un único sistema.

## Archivos

Misma estructura en el repo y en el ZIP: `svg/`, `png/`, `manifest.json` (contrato común: `small` / estándar / `large`, colores, animación).

| Archivo | Uso |
|---|---|
| `svg/fruti-squad.small.svg` | 16 px · asset mínimo: solo la forma, sin estilos ni animación |
| `svg/fruti-squad.svg`, `svg/fruti-squad.large.svg` | 20 px en adelante (`large` = estándar: no se añade detalle) |
| `svg/fruti-squad-animado-ejemplo.svg` | Interfaz con la animación activada |
| `svg/fruti-squad-oscuro.svg` / `svg/fruti-squad-claro.svg` / `svg/fruti-squad-auto.svg` | `#F8F8F5` en oscuro, `#161616` en claro, o automático según el tema |
| `svg/fruti-squad-tile.svg`, `png/fruti-squad-avatar-{256,512}.png` | Avatar en cuadro `#161616` |
| `svg/fruti-squad-tile-animado.svg`, `png/fruti-squad-orquestar.gif` | Avatar con la animación |
| `png/fruti-squad-{oscuro,claro}-512.png` | PNG transparentes |
| `svg/fruti-squad-multicolor.svg`, `png/fruti-squad-multicolor-512.png` | Un brazo del color de cada integrante; solo sobre fondo oscuro |

## Movimiento «orquestar» (state_transition)

Los cinco módulos se despliegan girando, uno tras otro, y el núcleo se enciende. Dura unos 1.04 s, una vez.
- Se activa con `uva-fruti-squad--orquestar`.
- Con «reducir movimiento», aparece completo.

## Nota

Es la Espiral aprobada (`../fruti-squad.svg`, 512 px), escalada a 24 px con el mismo dibujo: trazo 2.62, hueco entre brazos 2.23 (1.48 px a 16 px), hueco brazo–núcleo 1.64 (1.09 px a 16 px). Es un elemento de marca: los huecos siguen la regla de «≥ 1 px a 16 px» de la marca, no la de iconos (≥ trazo). Versión multicolor: un brazo por integrante.

Uso: junto al nombre, icono oculto (`aria-hidden`); solo, avatares con `role="img"` y `aria-label="Fruti Squad"`. Simétrico o no direccional: `rtl: fixed`.

## Contraste

| Par | Contraste |
|---|---|
| `#F8F8F5` sobre `#161616` | 17.01:1 |
| `#F8F8F5` sobre blanco | 1.06:1 |
| `#161616` sobre blanco | 18.10:1 |
| núcleo `#B7F34D` sobre `#161616` | 13.74:1 |
