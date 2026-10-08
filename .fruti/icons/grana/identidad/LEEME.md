# Grana · identidad

Exploración desde cero (decisión del usuario, 2026-10-08). Tesis de la marca: **estructura fija, color tuyo**. El color de los símbolos lee `--g-color-brand` (por defecto carmín `#a3123a`). El logo de octubre (`../grana.svg`) leía `--grana-color` y su guía citaba `--gr-color-brand`: el prefijo actual de la librería es `--g-*`.

## Ronda 1 · símbolo

| Concepto | Idea | Lo que muestra el banco (`ronda-1/banco.png`) |
|---|---|---|
| **A · Armazón** | Cochinilla vista desde arriba en tinta fija. El tinte del tema va detrás, desplazado como una impresión fuera de registro | Se lee como insecto y la separación estructura/color se entiende sin explicarla. En una tinta se vuelve una mancha: necesita una versión monocroma propia. Riesgo: escarabajo o abeja |
| **B · g-gota** | «g» minúscula: la panza es la cochinilla con bandas y la cola suelta una gota de tinte | Monograma claro, se lee como «g». Pierde el insecto (el lema «bug» se debilita) y la gota desaparece a 16 px |
| **C · Componentes** | El cuerpo son cuatro píldoras apiladas, como botones y campos | Idea ingeniosa, pero se lee como una colmena o una abeja. A 16 px parece un menú de hamburguesa |

## Ronda 2 · afinado de A (elegida por el usuario)

| Prueba | Resultado |
|---|---|
| A2 / A3 / A4 con hueco recortado entre tinta y tinte (`ronda-2/banco.png`) | ❌ El tinte queda en franjas finas entre las bandas y se lee como una pelota rayada. El color, que es el protagonista, desaparece. Además, el primer intento tenía un error: la máscara se movía con el tinte desplazado |
| **A5 · color** (`ronda-2/a5-color.svg`) | Tinte sólido como el original, proporción intermedia (algo más ancha) y antenas más cortas. Sigue siendo insecto y reduce la lectura de abeja |
| **A5 · una tinta, contorno fino** (`ronda-2/a5-tinta-linea.svg`) | El tinte pasa a ser un segundo contorno desplazado: mantiene la idea de «dos capas fuera de registro» sin color |
| A5 · una tinta, punteado | ❌ Los puntos se leen como agujeros o ruido |
| **A5 · 16 px** (`ronda-2/a5-16.svg`, `a5-16-tinta.svg`) | Óvalo, una banda y trazo grueso, sin antenas |

Comparativa: `ronda-2/banco2.png`.
