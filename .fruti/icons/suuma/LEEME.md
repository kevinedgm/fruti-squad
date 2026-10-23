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
