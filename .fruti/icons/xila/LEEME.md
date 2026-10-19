# Xila · identidad

Encargo del usuario (2026-10-19): identidad para Xila, librería de gráficos en TypeScript para dashboards y datos científicos, inspirada en los textiles oaxaqueños (referencia: brocado de rombos y grecas en naranja sobre manta, con costura en zigzag).

## Lo que define al producto (del brief)

- Anatomía editorial: grid solo horizontal, líneas de 2 px con nombre y último valor al final, barras con extremo redondeado y hueco entre vecinas, puntos con anillo de superficie, título que dice el hallazgo. Sin sombras, degradados ni cajas.
- Paleta Cobalto: cobalto principal, categórica de siete validada para daltonismo, heatmap de casi blanco a marino.
- Plugins: tooltip, leyenda, zoom, selección, resumen, anotaciones, sincronización, teclado.

## Ronda 1 (`ronda-1/banco.png`)

Regla de la ronda: cada concepto se dibuja con la anatomía de la librería (2 px, barras redondeadas con hueco, punto con anillo), para que el logo sea una gráfica de Xila.

| Concepto | Del textil | Lectura (Claude) |
|---|---|---|
| A · la X del telar | dos hilos cruzados forman el rombo del brocado; el cruce es la X de Xila y el rombo, el dato | la más propia (inicial + rombo); a 16 px se lee «cerrar» |
| B · la greca que es gráfica | la greca de Mitla como línea escalonada con último valor marcado | se lee «escalera» o «subida»; genérica de analítica |
| C · la franja de barras | la banda de brocado hecha de barras redondeadas con hueco, silueta de rombo | se lee «ecualizador»; a 16 px la silueta se pierde |
| D · la puntada | el zigzag de la costura como serie de tiempo con el pico en color | se lee «gráfica de línea»: cualquier producto de datos |

## Ronda 2 · patrón de hilos (usuario: «más como un patrón, hilos»)

El brocado se teje con hileras horizontales de distinto largo; una barra horizontal es exactamente eso (`ronda-2/banco.png`): A rombo de hilos, B trama y urdimbre, C greca de hileras, D retícula de rombos. Correctas pero quietas: ornamento, no dato.

## Ronda 3 · disruptivo (usuario: «algo innovador, disruptivo»)

El brocado no es ornamento, es dato (`ronda-3/banco.png`):

| Concepto | Idea |
|---|---|
| E · el hilo que se sale | el rombo tejido; un hilo en cobalto abandona la trama y sigue como línea de 2 px hasta su último valor, con punto y anillo y la cifra al final. La tesis de Xila («formas que salen de la línea y la barra») con su propia anatomía |
| F · telar generativo | el rombo es una distribución real: `xila.weave(data)` teje el logo con los datos de cada dashboard; el canónico es una muestra congelada |
| G · xila tejida | el nombre se teje con hileras de hilo; el punto de la i en cobalto; wordmark = patrón |

## Ronda 4 · bordado (usuario: «más como un bordado, como los textiles de la ropa indígena»)

Cambio de técnica: del brocado (telar) al bordado. Hecho clave: el punto de cruz es una X, la inicial de Xila, y una cuadrícula de puntos es una matriz de datos (`ronda-4/banco.png`).

| Concepto | Idea | Lectura (Claude) |
|---|---|---|
| H · rombo en punto de cruz | el motivo mínimo del huipil hecho de X; una X en cobalto es el dato | la más propia: la X es a la vez puntada, inicial y punto de datos; a 16 px se vuelve textura |
| I · flor bordada | flor de ocho puntas en punto de cruz, centro en cobalto | la más «ropa indígena»; a 16 px se confunde con copo de nieve o asterisco |
| J · greca bordada | la greca escalonada de Mitla en punto de cruz; la última X es el último valor | une bordado y anatomía de Xila; a 16 px se lee «escalera» |
| K · cadenilla | el hilo de cadeneta del Istmo como línea que termina en flor de puntos | la más literal; la cadeneta a 16 px es un garabato |
