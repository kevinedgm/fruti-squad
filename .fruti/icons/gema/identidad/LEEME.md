# GEMA · Gestión de Muestras y Análisis · identidad

Encargo del usuario (2026-11-17): nueva identidad para el sistema del laboratorio Nisa Nabani; todas las anteriores (Conectti, Nisalab, Nabi) descartadas. Referencia de estilo: SAM (`../sam/manual/`): simplicidad, contorno de tinta, un solo acento como relleno.

## Nombre (usuario, 2026-11-17): GEMA
Arriba el nombre corto, abajo el nombre completo que define el sistema: «Gestión de Muestras y Análisis». Usa el vocabulario del resumen de producto («registra las muestras… los análisis que se les hacen»). Sin verificar en IMPI ni dominios.

## Hechos del resumen de producto que condicionan
- Interno: 48 usuarios del laboratorio, dos sucursales (Oaxaca, CDMX); sin portal de clientes.
- Frontend con Grana (ADR-002/005): el color de marca entra en `--g-color-brand`, como en SAM.
- **unresolved:** la skill `nisa` define la interfaz con Verdant (acento esmeralda); el resumen dice Grana. Confirmar con el dueño de la decisión.

## Ronda 1 (`ronda-1/banco.html`, `banco.png`) · símbolo, acento cian provisional
| Concepto | Idea | Lectura (Claude) |
|---|---|---|
| A · Muestra | frasco con tapa; el líquido en acento es la muestra | el más claro y literal; puede leerse como frasco de medicina o bebida |
| B · Gema | piedra tallada; el pabellón en acento es la gota de muestra | une nombre y oficio; riesgo: joyería, y el logo de Sketch (app de diseño) es una gema |
| C · G con gota | la barra de la G desemboca en una gota | letra y oficio; se parece a logos de empresas de agua; a 16 px se empasta |

**Ronda 1 rechazada (usuario, 2026-11-17):** «las formas no tienen nada que ver con el laboratorio»; laboratorio de análisis de muestras industriales; pide forma abstracta, diferente.

## Ronda 2 (`ronda-2/banco.html`, `banco.png`) · formas abstractas del análisis
| Concepto | Idea | Lectura (Claude) |
|---|---|---|
| A · Pico | señal de un instrumento (cromatograma/espectro): pico sobre línea base, área en acento = resultado | la más propia del análisis; ligera visualmente; puede leerse como gráfica o pulso |
| B · Capas | muestra separada en componentes (destilación, decantación); capa central en acento | abstracta y sólida a 16 px; puede leerse como embudo o filtro |
| C · Mira | encuadre de medición con la muestra en acento al centro | precisión y control; se parece al icono de escanear de las cámaras |

**Ronda 2 sin elegir (usuario, 2026-11-17):** pide «una forma abstracta, disruptiva, una geometría nueva».

## Ronda 3 (`ronda-3/banco.html`, `banco.png`) · geometrías construidas
| Concepto | Idea | Lectura (Claude) |
|---|---|---|
| A · Intersección | círculo (muestra) cruza cuadrado (método); el cruce en acento es el análisis | limpia y legible; riesgo: diagrama de Venn |
| B · Cristal | hexágono en seis piezas; una en acento se desprende (la fracción que se analiza); gema = cristal | la más dinámica; hexágono común en ciencia |
| C · Estratos | círculo en franjas desplazadas (núcleo de muestra, bandas de espectro); franja en acento | la más disruptiva; puede leerse como glitch |
| D · Módulos | cuatro cuartos de retícula, uno en acento cierra el ciclo | abstracto puro; su significado hay que contarlo |
En «una tinta» las piezas en acento desaparecen: falta la versión monocroma de la elegida.

**Ronda 3 rechazada (usuario, 2026-11-17):** «no le encuentro sentido»; las de la ronda 2 (Pico, Capas, Mira) sí tenían sentido. Debe referirse al análisis de muestras y a sus resultados.

## Ronda 4 (`ronda-4/banco.html`, `banco.png`) · desarrollo de la ronda 2
- A1 · Pico sólido: más peso; a 16 px se lee como «^».
- A2 · Pico en pantalla: marco de instrumento; el mejor como icono de app; riesgo «monitor/estadísticas».
- B · Mira con pico: une Mira y Pico; a 16 px el pico se pierde.
- C · Resultado: pico menor en tinta y pico del resultado, mayor, en acento; el más propio (una señal real tiene varios picos).
- D · Capas de señal: capas alineadas; parece menú o barras.
Criterio de salida propuesto: elegir una dirección en esta ronda y validarla en contexto (pestaña, icono PWA, barra), como SAM.
