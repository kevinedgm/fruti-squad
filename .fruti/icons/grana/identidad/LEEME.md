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

## Ronda 3 · wordmark (Instrument Sans, texto convertido a trazados)

Símbolo aprobado: A5, con la versión de contorno fino para una tinta (2026-10-08).

| Composición | Construcción | Banco (`ronda-3/banco.png`) |
|---|---|---|
| **W1 · limpio** | «grana» en minúsculas, peso 600, espaciado −1 % | Legible a 20 px; neutra. La identidad la pone el símbolo |
| **W2 · fuera de registro** | Peso 700 en tinta, con su tinte del tema desplazado detrás: la firma del símbolo llevada al nombre | La más propia. A 20–32 px el desplazamiento parece sombra o borrosidad |
| W3 · semicondensado + lema | Ancho 85 y peso 650, con el lema debajo | Compacta y técnica. El lema solo se lee a partir de unos 48 px de alto; por debajo, es ruido |

Recomendación: un solo wordmark con dos modos. W1 en tamaños de interfaz (por debajo de 48 px de alto) y W2 en tamaños de exhibición (portada de docs, tarjetas, README). El lema va como texto aparte, no fijado al logotipo.

**Aprobado (2026-10-08):** W1 en tamaños de interfaz (menos de 48 px de alto), W2 en tamaños de exhibición; el lema va aparte.

## Color de marca (`color/`)

La paleta es de Grana: docs, README, sitio y valor por defecto del logo. No es el tema de `@grana/vue`: cada proyecto pone su color en `--g-color-brand` y el logo lo sigue.

| Nombre | Claro | Oscuro | Historia | Uso |
|---|---|---|---|---|
| Carmín | `#a3123a` · oklch(46.2% .175 13.9) | `#d74b63` · oklch(61.1% .175 13.9) | El tinte que sale del insecto | Color principal; en pantallas P3, `color(display-p3 .62 .05 .2)` |
| Nopal | `#2f6a3d` | `#4e895a` | La planta donde vive | Acento escaso |
| Cera | `#f7f2ea` | `#151012` (noche) | La cera blanca que cubre a la cochinilla | Fondo |
| Tinta | `#1d1517` | `#efe7dd` | — | Texto y estructura del símbolo |

Contraste (mínimos de la propia Grana: texto 4.5:1, controles 3:1):
- Claro: carmín 6.97, nopal 5.80, tinta 16.08 sobre cera.
- Oscuro: carmín 4.55, nopal 4.53, tinta 15.38 sobre noche.
- En oscuro, el carmín se aclara (mismo tono y croma en OKLCH, más luz) hasta pasar 4.5:1. Un botón carmín en oscuro lleva texto oscuro.
- Carmín y nopal tienen luminosidad parecida: con deuteranopía se confunden. Regla: nunca distinguir dos estados solo por carmín frente a nopal.

Archivos: `color/grana-marca.css` (variables listas), `color/paleta.json`, `color/color.py` (cálculo reproducible), `color/muestra.png` (paleta y cabecera de docs en claro y oscuro).
