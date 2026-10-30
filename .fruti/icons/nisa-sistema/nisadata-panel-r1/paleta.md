# NisaData · paleta de datos v1

Validada con `validate_palette.js` (skill dataviz), modo claro, superficie #FFFFFF. Modo oscuro: no definido todavía.

| Trabajo | Colores | Regla |
|---|---|---|
| Categórica (identidad) | 1 cobalto `#1d4ed8` · 2 ciruela `#9b3d8f` · 3 turquesa `#14b8a6` | Máximo 3 series; más se agrupa en «Otros» (`#9AA1B1`) o en gráficas separadas. Pasa todos los pares: daltonismo ΔE 11.9, visión normal 21.9. Turquesa 2.5:1 sobre blanco: exige etiqueta directa o tabla. |
| Una sola serie / secuencial | Rampa de cobalto, claro → oscuro | Magnitud de una cosa (carga por área, mapas de calor). |
| Divergente (contra una meta) | cobalto ← gris (meta) → ciruela | Cobalto = mejor que la meta, ciruela = peor. Nunca rojo/verde. |
| Estatus | Colores de NisaLab (amarillo, azul cielo, morado, verde, rojo) | Solo en gráficas de estatus, en orden de etapa; Cancelada aparte. Siempre con texto. |
| Salud / alertas | Ícono + texto con fondos de estatus | Nunca color solo. |

## Decisiones con evidencia
- **Las áreas no se colorean en gráficas.** Sus 8 colores tienen la misma luminosidad a propósito (marca), y por eso fallan como paleta de datos: Farmacia y Bebidas de agave quedan a ΔE 0.6 para deuteranopía (indistinguibles). En gráficas, el área se nombra con su ícono a una tinta y la barra va en cobalto.
- **Rojo y verde de estatus nunca son vecinos.** Terminada y Cancelada fallan para daltonismo (ΔE 5.0); por eso Cancelada va separada.
- **Grafito y mandarina son de marca, no de datos.** Mandarina tampoco es alerta.
- Sin doble eje; tooltip en cada marca; «Ver tabla» en gráficas de líneas.
