# Mora · avatar

Elegida: V2 «base» (2026-10-08). Propuestas: `../squad-propuesta/`. Generador común: `../squad-build.py`.

Tres módulos (documento, evidencia, registro) sobre una base: organiza lo que el sistema ya sabe.

## Archivos

Misma estructura en el repo y en el ZIP: `svg/`, `png/`, `manifest.json` (contrato común: `small` / estándar / `large`, colores, animación).

| Archivo | Uso |
|---|---|
| `svg/mora.small.svg` | 16 px · asset mínimo: solo la forma, sin estilos ni animación |
| `svg/mora.svg`, `svg/mora.large.svg` | 20 px en adelante (`large` = estándar: no se añade detalle) |
| `svg/mora-animado-ejemplo.svg` | Interfaz con la animación activada |
| `svg/mora-oscuro.svg` / `svg/mora-claro.svg` / `svg/mora-auto.svg` | `#8468E8` en oscuro, `#7D5FE7` en claro, o automático según el tema |
| `svg/mora-tile.svg`, `png/mora-avatar-{256,512}.png` | Avatar en cuadro `#161616` |
| `svg/mora-tile-animado.svg`, `png/mora-catalogar.gif` | Avatar con la animación |
| `png/mora-{oscuro,claro}-512.png` | PNG transparentes |

## Movimiento «catalogar» (state_transition)

Se traza la base y luego, en orden, documento, evidencia y registro. Dura unos 0.66 s, una vez.
- Se activa con `uva-mora--catalogar`.
- Con «reducir movimiento», aparece completo.

## Nota

A 16–20 px los anillos se cierran y se ven como puntos; la base mantiene el ritmo «tres sobre una línea». Avatares con trazo 2: no cabe más grueso con hueco ≥ 2.

Uso: junto al nombre, icono oculto (`aria-hidden`); solo, avatares con `role="img"` y `aria-label="Mora"`. Simétrico o no direccional: `rtl: fixed`.

## Contraste

| Par | Contraste |
|---|---|
| `#8468E8` sobre `#161616` | 4.42:1 |
| `#8468E8` sobre blanco | 4.10:1 |
| `#7D5FE7` sobre blanco | 4.50:1 |

El violeta da 4.42:1 sobre `#161616`: pasa el mínimo de 3:1 para gráficos, pero queda por debajo del 4.5:1 recomendado.
