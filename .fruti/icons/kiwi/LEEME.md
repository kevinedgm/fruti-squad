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
| `avatar/kiwi-{oscuro,claro}-512.png` | PNG transparentes |

- Los tres SVG base usan `currentColor`, así que toman el color del texto, y pasan `check-icon.mjs`.
- Contraste: `#7FCF5B` da 9.46:1 sobre `#161616`; `#448427` da 4.59:1 sobre blanco.

Evidencia: `evidencia-familia.png` (Fruti Squad, avatar de Kiwi y Kiwi sobre blanco).

## Uso en interfaz

- Junto al nombre «Kiwi»: el icono queda oculto (`aria-hidden="true"`, como viene).
- Solo, como avatar: usar los de `avatar/`, que llevan `role="img"` y `aria-label="Kiwi"`.

## Nota

En el cuadro de avatar, el trazo de Kiwi (2/24) se ve más fino que las cápsulas del icono de Fruti Squad. Si los avatares van a ir al lado del icono principal, conviene un trazo de avatar de 2.5–2.75, solo en `avatar/`, nunca en la versión de interfaz.
