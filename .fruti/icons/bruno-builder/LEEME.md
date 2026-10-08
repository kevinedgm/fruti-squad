# Bruno · avatar

Elegida: V1 «pines» (2026-10-08). Propuestas: `../squad-propuesta/`. Generador común: `../squad-build.py`.

Módulo redondeado + dos puertos: props entra, events sale. Conecta las piezas y hace que funcionen.

## Archivos

Misma estructura en el repo y en el ZIP: `svg/`, `png/`, `manifest.json` (contrato común: `small` / estándar / `large`, colores, animación).

| Archivo | Uso |
|---|---|
| `svg/bruno-builder.small.svg` | 16 px · asset mínimo: solo la forma, sin estilos ni animación |
| `svg/bruno-builder.svg`, `svg/bruno-builder.large.svg` | 20 px en adelante (`large` = estándar: no se añade detalle) |
| `svg/bruno-builder-animado-ejemplo.svg` | Interfaz con la animación activada |
| `svg/bruno-builder-oscuro.svg` / `svg/bruno-builder-claro.svg` / `svg/bruno-builder-auto.svg` | `#E5A447` en oscuro, `#A46A17` en claro, o automático según el tema |
| `svg/bruno-builder-tile.svg`, `png/bruno-builder-avatar-{256,512}.png` | Avatar en cuadro `#161616` |
| `svg/bruno-builder-tile-animado.svg`, `png/bruno-builder-conectar.gif` | Avatar con la animación |
| `png/bruno-builder-{oscuro,claro}-512.png` | PNG transparentes |

## Movimiento «conectar» (state_transition)

Se traza el módulo, la entrada sube hacia él y la salida baja desde él. Dura unos 0.66 s, una vez.
- Se activa con `uva-bruno-builder--conectar`.
- Con «reducir movimiento», aparece completo.

## Nota

Riesgo de lectura: recuerda al enchufe (`plug`) de Lucide, que lleva las patas arriba. Avatares con trazo 2.5 (cuadro 2.75): el módulo baja y los pines se acortan para mantener el margen 2.

Uso: junto al nombre, icono oculto (`aria-hidden`); solo, avatares con `role="img"` y `aria-label="Bruno"`. Simétrico o no direccional: `rtl: fixed`.

## Contraste

| Par | Contraste |
|---|---|
| `#E5A447` sobre `#161616` | 8.39:1 |
| `#E5A447` sobre blanco | 2.16:1 |
| `#A46A17` sobre blanco | 4.51:1 |
