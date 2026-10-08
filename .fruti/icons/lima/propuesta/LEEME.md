# lima · propuestas (E2–E3)

| Variante | Construcción | Banco (`banco.png`) |
|---|---|---|
| **V1 · hexágono** (recomendada) | Hexágono de punta arriba + «I»: barra de entrada, eje y barra de salida | Simétrica y estricta. Clara de 16 a 64 px. La «I» no se confunde con `text-cursor` porque va dentro del contenedor |
| V2 · squircle | Squircle vertical + la misma «I» | A 16–24 px se parece a un móvil o a un campo de texto (`smartphone`, `text-cursor-input`) |
| V3 · compuertas | Hexágono + eje de vértice a vértice + dos barras que lo cruzan | Más «flujo», pero a 16–24 px se lee como el cubo de `box` o como un paquete |

- Separaciones medidas (A6 ≥ 2): V1 2.07, V2 2.23, V3 2.38. Margen: 2.00 en las tres.
- `check-icon.mjs`: las tres pasan.

## Contraste del lima del brief

| Par | Contraste |
|---|---|
| `#C9F36B` sobre `#161616` | 14.23:1 ✅ |
| `#C9F36B` sobre blanco | 1.27:1 ❌ prácticamente invisible |
| `#74A20D` sobre blanco | 3.04:1 (mínimo) |
| `#5D820B` sobre blanco | 4.50:1 (recomendado) |

Aviso: en fondo claro, `#5D820B` (Lima) y `#448427` (Kiwi) tienen la misma luminosidad (1.02:1 entre sí). Solo los distingue el tono, oliva frente a verde, y la forma. En oscuro sí se distinguen: 1.5:1 entre `#C9F36B` y `#7FCF5B`.
