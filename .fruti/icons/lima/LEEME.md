# Lima · avatar

Elegida la V1 «hexágono» (2026-10-08). Propuestas, banco y contraste: `propuesta/`. Generador: `gen.py`.

Hexágono de punta arriba con una «I» dentro: barra de entrada, eje (la regla) y barra de salida. Es simétrico, así que no se refleja en idiomas de derecha a izquierda (`rtl: fixed`).

## Archivos

Misma estructura en el repo y en el ZIP: `svg/`, `png/`, `manifest.json` (contrato común de la squad: `small` / estándar / `large`, colores, animación).

`svg/lima.small.svg` es el asset mínimo: solo la forma, sin estilos, variables ni animación.


| Archivo | Uso |
|---|---|
| `svg/lima.small.svg` | 16 px: contenedor + eje |
| `svg/lima.svg`, `svg/lima.large.svg` | 20 px en adelante. A 48 px o más no se añade nada (brief: «estricta y limpia») |
| `svg/lima-animado-ejemplo.svg` | Interfaz con la animación activada |
| `svg/lima-oscuro.svg` / `svg/lima-claro.svg` / `svg/lima-auto.svg` | `#C9F36B` en oscuro, `#5D820B` en claro, o automático según el tema |
| `svg/lima-tile.svg`, `png/lima-avatar-{256,512}.png` | Avatar en cuadro `#161616` |
| `svg/lima-tile-animado.svg`, `png/lima-validar.gif` | Avatar con la animación |
| `png/lima-{oscuro,claro}-512.png` | PNG transparentes |

## Medidas

| Versión | Trazo | Hueco barra–hexágono | Hueco entre barras | Margen |
|---|---|---|---|---|
| Interfaz | 2 | 2.07 | 4.00 | 2.00 |
| Avatares | 2.25 | 2.27 | 2.25 | 2.03 |

- **Límite geométrico:** Kiwi usa trazo 2.5 en los avatares, pero en Lima no cabe. Con 2.5, la «I» no entra en el hexágono con huecos de al menos un trazo: si las barras se alejan de los bordes, se pegan entre sí. El máximo posible es unos 2.3; se usa 2.25.
- En el cuadro, el hexágono va a escala 0.92, para acercarse al peso visual de Kiwi (2.07 frente a 2.26 unidades).
- Contraste: `#C9F36B` sobre `#161616` da 14.23:1; `#5D820B` sobre blanco da 4.50:1.
- `check-icon.mjs`: todos los SVG de interfaz pasan.

## Movimiento «validar» (categoría: state_transition)

Significado: Lima evalúa una pieza.
1. Se traza el hexágono (360 ms).
2. Se abre la barra de entrada (160 ms).
3. Baja el eje (220 ms).
4. La barra de salida cierra la compuerta (160 ms).

Dura unos 0.80 s, una vez.

- Se activa con la clase `uva-lima--validar`.
- Con «reducir movimiento», el icono aparece completo.

## Uso

- Junto al nombre «Lima»: el icono queda oculto (`aria-hidden`).
- Solo, como avatar: usar `svg/` (avatares), que lleva `role="img"` y `aria-label="Lima"`.

Evidencia: `evidencia-familia.png` (Fruti Squad, Kiwi y Lima en cuadro; Kiwi y Lima sobre blanco).
