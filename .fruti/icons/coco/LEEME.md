# Coco · avatar

Elegida: V2 «lupa» (2026-10-08). Propuestas: `../squad-propuesta/`. Generador común: `../squad-build.py`.

Círculo + tres puntos en diagonal que crecen hacia el foco: construye y observa el resultado visual.

## Archivos

Misma estructura en el repo y en el ZIP: `svg/`, `png/`, `manifest.json` (contrato común: `small` / estándar / `large`, colores, animación).

| Archivo | Uso |
|---|---|
| `svg/coco.small.svg` | 16 px · asset mínimo: solo la forma, sin estilos ni animación |
| `svg/coco.svg`, `svg/coco.large.svg` | 20 px en adelante (`large` = estándar: no se añade detalle) |
| `svg/coco-animado-ejemplo.svg` | Interfaz con la animación activada |
| `svg/coco-oscuro.svg` / `svg/coco-claro.svg` / `svg/coco-auto.svg` | `#C89A68` en oscuro, `#9C6D39` en claro, o automático según el tema |
| `svg/coco-tile.svg`, `png/coco-avatar-{256,512}.png` | Avatar en cuadro `#161616` |
| `svg/coco-tile-animado.svg`, `png/coco-inspeccionar.gif` | Avatar con la animación |
| `png/coco-{oscuro,claro}-512.png` | PNG transparentes |

## Movimiento «inspeccionar» (state_transition)

Se traza el círculo y aparecen los puntos de menor a mayor, hasta el foco (inspección). Dura unos 0.70 s, una vez.
- Se activa con `uva-coco--inspeccionar`.
- Con «reducir movimiento», aparece completo.

## Nota

Los puntos dependen del trazo (2): a 16 px miden unos 1.3 px y en el avatar se ven más ligeros que el contorno. Agrandarlos rompe el hueco mínimo de 2 entre puntos.

Uso: junto al nombre, icono oculto (`aria-hidden`); solo, avatares con `role="img"` y `aria-label="Coco"`. Simétrico o no direccional: `rtl: fixed`.

## Contraste

| Par | Contraste |
|---|---|
| `#C89A68` sobre `#161616` | 7.13:1 |
| `#C89A68` sobre blanco | 2.54:1 |
| `#9C6D39` sobre blanco | 4.51:1 |
