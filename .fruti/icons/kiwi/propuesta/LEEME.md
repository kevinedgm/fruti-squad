# kiwi · propuestas (E2–E3)

| Variante | Construcción | Hipótesis | Banco (`banco.png`) |
|---|---|---|---|
| **V1 · columna** (recomendada) | Óvalo + eje vertical a 1/3 (x=9) + fila desde el eje hasta el borde derecho (y=11) | Asimétrica: se lee como un layout real (columna lateral + cabecera + contenido) con jerarquía, no como un símbolo | Clara de 16 a 64 px; no se confunde con `globe` ni con `panel-left` |
| V2 · cruz | Óvalo + cruz centrada (la referencia literal del brief) | Simetría = orden | ❌ B4: se confunde con `circle-plus`, punto de mira o globo. Simétrica = sin jerarquía |
| V3 · flotante | Óvalo + «├» que no toca el contorno | La estructura se está organizando dentro | A 16–20 px el «├» mide unos 3 px y parece un botón de reproducir o expulsar |

Tamaños de V1:
- `v1-columna.small.svg` (16 px): óvalo + eje.
- `v1-columna.svg` (20–32 px).
- `v1-columna.large.svg` (48 px en adelante): añade una división secundaria vertical en la zona de contenido; la silueta no cambia.

`check-icon.mjs`: las 5 piezas pasan todos los criterios.

## Contraste del verde del brief (WCAG 1.4.11 pide 3:1 para gráficos que informan)

| Par | Contraste | Veredicto |
|---|---|---|
| `#7FCF5B` sobre `#161616` | 9.46:1 | ✅ |
| `#7FCF5B` sobre blanco | 1.91:1 | ❌ C1 bloqueante en fondo claro |
| `#56A731` sobre blanco | 3.01:1 | ✅ mínimo |
| `#448427` sobre blanco | 4.59:1 | ✅ recomendado (norma §22) |

Propuesta: `#7FCF5B` en fondos oscuros y el mismo tono oscurecido (`#448427`) en fondos claros. Pendiente de decisión del usuario.
