# Ecosistema Manik · IA · ronda 2 (animaciones)

Pedido del usuario (2026-10-31): prefiere la **dirección C** (tinta noche, destello doble) sobre la A; de la A le gusta «la segmentación» [interpretado: el borde segmentado que gira al generar]. Quiere que el ícono tenga animación para que se sepa que es IA, y ver distintos tipos.

Publicado: https://claude.ai/artifact/GAn43o2Akw6ZMtgzXBsD3U

## Seis animaciones (ícono, botón, «Generando…» y botón cuadrado)
1. Titileo: los dos destellos laten a destiempo.
2. Borde segmentado (de A): un segmento cian recorre el borde.
3. Brillo que barre: reflejo cian de lado a lado.
4. Órbita: el destello chico gira alrededor del grande.
5. Respiración: halo cian que crece y se apaga.
6. Trazo: el destello se dibuja y se rellena.

Dos modos para comparar: «En bucle» y «Como en la app»; botón «Pausar animaciones» (WCAG 2.2.2).

## Reglas de movimiento [propuesta]
Quieta en reposo; una vuelta al pasar el cursor o con foco y al aparecer un resultado; en bucle solo mientras genera, siempre con texto «Generando…» y aviso para lector de pantalla; `prefers-reduced-motion` la apaga.

## Verificación
Playwright 1300 y 390 px: sin desbordes ni errores JS; capturas en dos momentos confirman movimiento; modo «como en la app» enciende al pasar el cursor y apaga a los 2.4 s.

[pendiente: elección de animación (o combinación: una para invitar, otra para generar)]
