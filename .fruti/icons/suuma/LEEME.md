# SUUMA · identidad (segunda propuesta, alternativa a Laranda)

Brief: plataforma de belleza y cuidado personal; nombre SUUMA (evolución gráfica de «suma», la doble U es el rasgo distintivo); narrativa de las hormigas: individuos que conservan su autonomía y juntos llegan más lejos. Dirección visual: formas simples, geometría orgánica, conexiones/crecimiento/colaboración; paleta natural y cálida (verdes suaves, tierras, neutros claros) + un color de contraste funcional; nada de tijeras, rostros, flores ni abejas literales. Gusto del usuario (de Laranda y Libela): abstracto, innovador, trazo orgánico, nada rígido ni literal.

## Ronda 1 · símbolo en blanco y negro (`ronda-1/`)
Trazo de pincel con presión (línea central Catmull-Rom + perfil de ancho; `gen.py`). A Doble U (dos U desfasadas), B Nodos (tres formas orgánicas que hacen una silueta + un punto), C Onda (un solo trazo que escribe «uu»), D Fila (puntos que crecen por una trayectoria), E Encuentro (dos trazos se funden en uno; el punto es el encuentro).

## Ronda 2 · cambiar el mecanismo (`ronda-2/`)
El usuario pidió algo más disruptivo. Cambia el mecanismo del símbolo, no el trazo: A Hueco (masa de tinta con la U vaciada), B Enjambre (nueve lugares, ocho formas: falta una; sistema generativo), C Suma (dos formas superpuestas, la intersección rayada es la tercera), D Bloque (bloque con dos U mordidas), E Fragmentos (una U de piezas desiguales que no se tocan).

## Ronda 3 · ideas desde la narrativa (`ronda-3/`)
Rechazada la ronda 2. A Senda (camino que se abre y se junta), B Une los puntos, C Cuencos (U dentro de U, descentrada), D Trenza (dos hebras que se cruzan), E Eco (anillos abiertos alrededor de un punto). Auditoría propia: A lee como pluma, D como X, E como diana; solo C y B sostienen la idea. Tres rondas sin acierto: se pide al usuario una referencia o el tipo de «disruptivo» que busca antes de seguir.

## Ronda 4 · tipográfico con giro (`ronda-4/`)
El usuario eligió «tipográfico con giro» (AskUserQuestion). Manrope 700 para s, m, a (`/tmp/suuma-manrope700.ttf`, instancia de `fuentes/Manrope[wght].ttf`); la doble U se construye a mano como trazo de línea central con el grosor del tallo de Manrope. A Pegadas (las u se tocan; lee «swma», descartable), B Anidada (u chica dentro de la grande), C Hueca (segunda u en contorno), D Desnivel (segunda u baja de la línea base), E Gesto (las dos u a pincel, cada una distinta).

## Ronda 5 · desarrollo de B Anidada (`ronda-5/`)
El usuario eligió B. Cinco variaciones del encaje y la «uu» sola como símbolo (favicon 16/32/64 e icono de app): B1 Centrada (interior fina), B2 Mismo peso, B3 Descentrada (interior a la derecha), B4 Llena (interior maciza), B5 Cuenco ancho. `*-simbolo.svg` por variante.

## Ronda 6 · la u interior como sonrisa (`ronda-6/`)
El usuario eligió B1 y B4 y pidió que la u interior sea una sonrisa. S1 Línea (trazo afinado), S2 Maciza (media luna), S3 Con ojos (carita completa, mostrada como límite), S4 Comisuras (u chica con puntas abiertas), S5 Asimétrica (media luna más gruesa de un lado). Símbolo solo y app icon por variante.

## Ronda 7 · S3 en color (`ronda-7/`)
El usuario eligió S3 (sonrisa con ojos). Cuatro paletas naturales + contraste funcional, con contrastes WCAG calculados en `gen.py`: P1 Salvia y arcilla (#5E7F63 #B8694A #FAF6EF #E8743C), P2 Oliva y miel (#6B7A3A #C98B2E #F8F4EA #7A3E6E), P3 Bosque y terracota (#2F5D4A #C9633D #F4EFE6 #F2C14E), P4 Menta y cacao (#7FA38E #5C3F33 #F8F5F0 #F06A4E). Wordmark claro/oscuro e icono de app sobre verde, neutro y tierra.

## Ronda 8 · color vivo y editorial (`ronda-8/`)
El usuario pidió colores más vivos, unisex, elegantes y editoriales. Base blanco #FFFFFF y tinta #121212; un cromático intenso (ojos, marca, acciones) y un acento (sonrisa): Q1 Esmeralda #0F8A5F + mandarina #FF6A2B, Q2 Cobalto #1F3BE0 + mandarina, Q3 Ciruela #5A2A86 + coral #FF5A4E, Q4 Petróleo #0E6E7A + ámbar #F5A623. Contrastes en el banco.

## Ronda 9 · B1 en color vivo (`ronda-9/`)
El usuario prefirió la B1 (u interior fina, sin ojos) sobre la S3. Mismas paletas Q1–Q4 de la ronda 8; la u interior lleva el cromático en el wordmark claro y el acento en oscuro y en los iconos.

## Ronda 10 · otras familias de color (`ronda-10/`)
Rechazadas Q1–Q4. Seis parejas sobre blanco y tinta: R1 Bermellón #C8102E + mostaza #E9B824, R2 Índigo noche #2A2A72 + mandarina #FF7A1A, R3 Naranja quemado #D4541A + botella #0B4F3F, R4 Lila eléctrico #6A4CFF + limón #FFD23F, R5 Frambuesa #B5174E + menta #2EC4A6, R6 Cadmio #FFD400 + tinta.

## Ronda 11 · tipografía (`ronda-11/`)
El usuario pidió probar Bricolage Grotesque y Onest. `gen.py` reconstruye la B1 con el tallo y el cuenco de cada fuente (clase `F`): Bricolage 600/700 (opsz 96), Onest 600/700 y Manrope 700 como referencia. Interior: ancho = cuenco − 2 tallos − 0.9 tallo, grosor 0.6 del tallo.

## Decisión tipográfica
Wordmark: Bricolage Grotesque 600, opsz 96, caja baja, tracking −1 %. Interfaz: Onest. (El usuario eligió 600 en la ronda 11.)

## Ronda 12 · color sobre el wordmark definitivo (`ronda-12/`)
Las seis familias R1–R6 aplicadas a la B1 en Bricolage 600, con iconos y contrastes. Color aún sin decidir.

## Decisión de color y cierre
R6 Cadmio y tinta aprobada. Paquete final en `final/` (ver `final/LEEME.md`); manual en `guia/guia.html` → https://claude.ai/artifact/3CdHEhfrwNCkxAo6XkB3j6
