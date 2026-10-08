# Kiwi · avatar

Elegida la V1 «columna» (2026-10-08). Propuestas, banco y contraste: `propuesta/`.

Óvalo + eje vertical a un tercio + fila hacia la derecha. Se lee como un layout con jerarquía (columna lateral, cabecera, contenido).

## Archivos

| Archivo | Uso |
|---|---|
| `kiwi.small.svg` | 16 px: óvalo + eje |
| `kiwi.svg` | 20–32 px: versión estándar |
| `kiwi.large.svg` | 48 px o más: añade la división secundaria |
| `avatar/kiwi-oscuro.svg` | `#7FCF5B`, para fondo oscuro |
| `avatar/kiwi-claro.svg` | `#448427`, para fondo claro |
| `avatar/kiwi-auto.svg` | Elige el color según el tema del sistema (`prefers-color-scheme`) |
| `avatar/kiwi-tile.svg`, `avatar/kiwi-avatar-{256,512}.png` | Avatar en cuadro `#161616`, de la misma familia que el icono de Fruti Squad |
| `avatar/kiwi-tile-animado.svg`, `avatar/kiwi-organizar.gif` | Avatar con la animación «organizar» activada |
| `kiwi-animado-ejemplo.svg` | Versión de interfaz con la animación activada (ejemplo de uso de la clase) |
| `avatar/kiwi-{oscuro,claro}-512.png` | PNG transparentes |

- Los tres SVG base usan `currentColor`, así que toman el color del texto, y pasan `check-icon.mjs`.
- Contraste: `#7FCF5B` da 9.46:1 sobre `#161616`; `#448427` da 4.59:1 sobre blanco.

Evidencia: `evidencia-familia.png` (Fruti Squad, avatar de Kiwi y Kiwi sobre blanco).

## Uso en interfaz

- Junto al nombre «Kiwi»: el icono queda oculto (`aria-hidden="true"`, como viene).
- Solo, como avatar: usar los de `avatar/`, que llevan `role="img"` y `aria-label="Kiwi"`.

## Grosor de los avatares (corregido 2026-10-08)

- `avatar/kiwi-{oscuro,claro,auto}.svg`: trazo 2.5, con el óvalo reducido (rx 8.75, ry 7.05) para conservar el margen de 2.
- `avatar/kiwi-tile.svg`: trazo 2.75 y escala 0.82 dentro del cuadro. Así su peso visual queda cerca de las cápsulas del icono de Fruti Squad.
- La versión de interfaz (`kiwi*.svg`) sigue con trazo 2, como pide el brief.

## Idiomas de derecha a izquierda

- Los SVG llevan `.uva-kiwi:dir(rtl){transform:scaleX(-1)}`: dentro de una página en árabe o hebreo, la columna pasa al lado derecho.
- Probado en Chromium. `:dir()` funciona en Chrome 120+, Firefox y Safari 16.4+.
- Con `<img>`, el SVG no hereda la dirección de la página. Se hace en el CSS de la página: `img.kiwi:dir(rtl){transform:scaleX(-1)}`.

## Movimiento «organizar» (categoría: state_transition)

Significado: Kiwi empieza a estructurar.
1. Se dibuja el óvalo (380 ms).
2. Cae el eje de arriba abajo (240 ms).
3. Se traza la fila hacia la derecha (220 ms).
4. En la versión grande, después baja la división secundaria.

Dura unos 0.92 s en total y queda quieto mientras dure el estado.

- El componente añade la clase `uva-kiwi--organizar` al entrar en el estado y puede quitarla en el `animationend` de la última pieza.
- Con «reducir movimiento», el icono aparece completo sin trazarse.
- Sin destellos ni bucles. `check-icon.mjs` pasa D1, D2 y D5.
- Detalle técnico: `stroke-dasharray: 1 1.1` evita el punto que dejaba el trazo de longitud cero con terminación redonda antes de empezar a dibujarse.
