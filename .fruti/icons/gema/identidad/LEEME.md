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

**Elegidos de la ronda 4 (usuario, 2026-11-17):** B (Mira con pico), A2 (Pico en pantalla) y C (Resultado).

## Ronda 5 (`ronda-5/banco.html`, `banco.png`) · combinaciones
- R1 · Pantalla + Resultado (A2 + C): doble pico en el marco del instrumento; el más sólido como icono; a 16 px el pico menor casi desaparece.
- R2 · Mira + Resultado (B + C): doble pico entre las esquinas de la medición; el más fino.
- R3 · Resultado (C sola): sin marco, la más simple; ancha y baja en icono cuadrado.

**Elegido (usuario, 2026-11-17): R1 · Pantalla + Resultado.**

## Ronda 6 (`ronda-6/banco.html`, `banco.png`) · prueba en contexto
Versión chica (`gema-chica.svg`, 16–24 px): marco 3.6 y solo el pico del resultado. Silueta de notificación (`gema-notificacion.svg`).
| Contexto | Resultado (observación de Claude, a 1x y ampliado a 3x) |
|---|---|
| Pestaña, chica a 16 px | Se lee marco + pico; el acento es pequeño pero visible |
| Icono PWA (Android círculo, iOS) | Dentro de la zona segura; no se recorta |
| Barra superior, R1 a 28 px | Se lee en claro y oscuro; el pico menor se distingue |
| Notificación, silueta a 16 px | Se reconoce el marco; el pico relleno puede leerse como triángulo o «subir» |
No verificado: dispositivos reales.

**CONGELADO (usuario, 2026-11-17): símbolo R1 (Pantalla + Resultado) + versión chica + silueta de notificación.** Pulido pendiente: en la silueta, pico calado en vez de relleno.

## Ronda 7 (`ronda-7/banco.html`, `banco.png`) · color
Regla de SAM desde el inicio: acento = relleno, mismo valor en claro y oscuro, texto de tinta encima, contorno de tinta en claro; texto, enlaces y foco en tinta. Fuera: lima (SAM), carmín (Grana), teal (MedicalManik).
| Color | Valor | Tinta sobre color · color sobre noche · color sobre papel | Lectura |
|---|---|---|---|
| Celeste | `#38bdf8` | 9.2 · 9.2 · 1.9 | agua y precisión; pariente del celeste del laboratorio (#00B4D8); común en software científico |
| Ámbar | `#f5b52e` | 10.9 · 10.9 · 1.6 | industrial, instrumento encendido; se asocia a «precaución» |
| Coral | `#ff8466` | 8.2 · 8.2 · 2.1 | energía; cerca del rojo de error |

**Ronda 7 rechazada (usuario, 2026-11-17):** quiere un azul navy como el de Nisa Nabani, o un degradado de ese azul.

## Ronda 8 (`ronda-8/banco.html`, `banco.png`) · azul navy
Hecho: navy `#052A76` mide 1.5:1 sobre negro (no se ve en oscuro); 13.1:1 con texto blanco; 11.7:1 sobre papel.
- N1 · Navy del laboratorio: claro navy + texto blanco; oscuro «noche navy» (`#071633`) con azul claro `#8fb3ff` y texto navy (8.6:1). El color cambia de valor entre modos.
- N2 · Degradado navy: `#052A76 → #3D67AE` solo en superficies de marca (pico, icono, panel de login); botones planos (navy en claro; `#3D67AE` en oscuro, texto blanco 5.6:1, 3.5:1 sobre negro).
- N3 · Navy + celeste: navy de base; pico y estado activo en el celeste del laboratorio `#00B4D8` (5.3:1 con texto navy). Dos colores de la paleta del laboratorio.

**Color elegido (usuario, 2026-11-17): N2 · Degradado navy** (`#052A76 → #3D67AE` en superficies de marca; botones planos: navy en claro, `#3D67AE` en oscuro con texto blanco).

## Ronda 9 (`ronda-9/banco.html`, `banco.png`) · tipografía
Probadas en logotipo y en una pantalla de resultados (folios, parámetros, unidades, decimales, subíndices). Datos ficticios.
- A · Onest (+ JetBrains Mono): la de SAM; familia común entre herramientas internas.
- B · IBM Plex Sans (+ IBM Plex Mono): técnica e industrial; distingue I/l/1 y O/0; la más «instrumento».
- C · Instrument Sans (+ JetBrains Mono): la de Grana; compacta.

**Tipografía elegida (usuario, 2026-11-17): A · Onest** (la misma de SAM).

## Final (`../final/`)
Símbolo, logotipos, favicon, iconos de PWA, silueta de notificación (pico calado), tokens `gema-marca.css` y fragmento de manifest. Guía en `../final/LEEME.md`.

## Manual de marca (`../manual/manual.html`, generado con `gen.py` desde `../final/`)
Publicado como artifact el 2026-11-17.
