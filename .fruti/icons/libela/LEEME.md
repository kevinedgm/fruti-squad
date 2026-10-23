# Libela · identidad (segunda propuesta, alternativa a Laranda)

Idea madre: la libélula no persigue; calcula, se detiene y acierta. Libela es el taller donde esa precisión se vuelve negocio. El símbolo no ilustra una libélula: es la huella de su vuelo. Dos alas asimétricas que forman una L y un punto negativo que es el foco del sistema.

## Ronda 1 · símbolo en blanco y negro (`ronda-1/`)
`gen.py` construye el ala con un perfil de libélula (estrecha en la base, más ancha hacia la punta, redondeada) y genera cinco rutas sobre la misma anatomía: A Huella (sólidas), B Contorno (línea + anillo), C Tinta (ala a mano abierta + ala llena), D Ala mínima (una ala + línea de vuelo punteada), E Posada (alas finas que se cruzan en el punto). `banco.png` muestra cada una a 200, 32 y 16 px y en negativo.

## Ronda 2 · gesto abstracto, trazo orgánico (`ronda-2/`)
El usuario rechazó la ronda 1 (demasiado literal). `gen.py` dibuja trazos de pincel con ancho variable (línea central Catmull-Rom + perfil de presión): A Pausa (gesto con rizo y punto), B Cuatro vientos (cuatro trazos desde un vacío), C Posarse (un solo trazo que dobla y se afina), D Mirada (arco abierto y punto descentrado), E Aleteo (tres trazos desiguales y un punto).

## Ronda 3 · desarrollo de E y B (`ronda-3/`)
El usuario eligió E (Aleteo) y B (Cuatro vientos). Cuatro variaciones de cada una: E1 Aleteo, E2 Abanico (trazos desde el punto), E3 Suelto (trazos rectos, punto al lado), E4 Cuatro alas; B1 Cuatro vientos, B2 Giro (mismo sentido), B3 Punto (centro lleno), B4 Tres y uno (el punto ocupa el cuarto rumbo).

## Estado
Descartada por el usuario tras la ronda 3; la segunda propuesta pasa a SUUMA (`.fruti/icons/suuma/`).
