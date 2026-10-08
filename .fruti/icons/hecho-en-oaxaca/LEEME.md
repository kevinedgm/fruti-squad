# Sello «Hecho en Oaxaca / Made in Oaxaca»

Sello para los productos del usuario, inspirado en las marmotas de las calendas: esfera de manta con costillas, banda con texto, papel picado, discos y mástil. Texto en Bricolage Grotesque (SIL OFL), convertido a trazados.

Paleta de partida:
- tinta `#2a1a12`, manta `#fffaf0`, madera `#b0773a`;
- papel picado: rosa mexicano `#e4007c`, turquesa `#00a3a3`, amarillo `#f2b200`, naranja `#f26419`, morado `#7b3fb3`.

## Ronda 1

| Concepto | Idea | Banco (`ronda-1/banco.png`) |
|---|---|---|
| **A · banda** | La marmota completa; «HECHO EN OAXACA» va en su banda, como en la calenda, y «MADE IN OAXACA» debajo | La más fiel y con más carácter. Por debajo de unos 90 px la banda no se lee. Sobre oscuro, «MADE IN OAXACA» desaparece (falta una versión invertida). Riesgo: globo aerostático o farol |
| **B · sello** | Sello circular: texto alrededor (español arriba, inglés abajo) y una marmota pequeña al centro | Se lee como sello de origen. Funciona sobre cualquier fondo porque lleva su disco de manta. Por debajo de unos 64 px el texto no se lee |
| **C · marca + nombre** | Marmota mínima (esfera, una costilla, un triángulo, mástil) junto a «Hecho en Oaxaca» | Legible de 20 a 96 px. Sobre oscuro, el texto desaparece (falta la versión invertida). Riesgo: se puede leer como paleta helada o globo |

## Ronda 2 · abstracciones (la ronda 1 se rechazó por literal)

Se toma la idea estructural de la marmota, no su dibujo: gira, tiene 12 costillas alrededor de un mástil y la llena el papel picado.

| Concepto | Idea | Banco (`ronda-2/banco.png`) |
|---|---|---|
| **K · esfera cinética** | Las 12 costillas se vuelven husos de color que crean volumen, al estilo op-art. Animada, la esfera gira como la marmota en la calenda (`k-giro.gif`, bucle de 1.4 s; con «reducir movimiento», quieta) | El giro funciona y es lo más propio. Quieta, se lee como pelota de playa o paleta |
| **O · la O es la marmota** | Sello tipográfico: la «O» de «Oaxaca» es la marmota (anillo, una costilla en rosa mexicano) y su mástil baja por debajo de la línea | La más moderna y disruptiva: texto y símbolo son lo mismo. La O sola funciona como icono hasta 20 px. Riesgo: leerse como «Φ» o como una piruleta |
| **T · papel picado** | Un círculo hecho solo de triángulos recortados, con huecos entre ellos, sostenido por el mástil | Vibrante y muy de Oaxaca. Por debajo de 32 px los triángulos se vuelven ruido. Riesgo: árbol o piruleta |

### Corrección «parece paleta» (usuario, ronda 2)

Causa común a los tres conceptos: un círculo encima de un palo se lee como paleta, se dibuje como se dibuje. Se probaron dos salidas (`ronda-2/banco-eje.png`):

| | Sin mástil | Eje que atraviesa (discos arriba y abajo, como la espiga real) |
|---|---|---|
| K · cinética | Pelota de playa o esfera de adorno | **Se lee como algo que gira sobre su eje**; deja de ser paleta. Con el giro animado es la marmota en movimiento |
| O · la O | Una «O» con un óvalo; pierde la marmota | Se lee como la letra griega «Φ» |
| T · papel picado | Bola de mosaico, como una bola de discoteca | Adorno o piñata; a 32 px, ruido |

## Ronda 3 · K con eje, banda y manta (el usuario elige K; requisito: que funcione con y sin texto y se entienda la referencia)

Lo que distingue a la marmota de un globo o una pelota, sin dibujarla literal:
- **la banda** horizontal, donde va el nombre del pueblo;
- **la espiga con sus dos discos**, visible solo arriba y abajo: dentro de la esfera, el eje formaba una cruz y la esfera se leía como punto de mira;
- **la manta blanca**, con el color en las costillas.

| Variante | Construcción | Lectura (`ronda-3/banco.png`) |
|---|---|---|
| K1 | Husos de color + banda en tinta + espiga | Fuerte a cualquier tamaño, pero los husos de color la acercan a una pelota de playa |
| **K2** | Manta blanca, 12 costillas finas de colores, banda rosa mexicano, espiga | La que más se lee como marmota; se mantiene clara de 24 a 120 px. Riesgo: farol de papel |
| K3 | K2 + guirnalda de papel picado bajo la banda | Los triángulos casi no se ven; añade ruido sin sumar lectura |

## Ronda 4 · K2 en un solo color + un solo OAXACA (usuario: «sí K2», sin arcoíris; color intercambiable como Grana; juego con hecho/made)

- **Color:** costillas y banda leen `--oaxaca-color` (por defecto rosa mexicano `#e4007c`); la manta lee `--oaxaca-manta` (`#fff8ee`); el contorno y la espiga toman `currentColor`. Probado con rosa mexicano, grana, turquesa, añil y cempasúchil.
- **Un solo OAXACA:**

| Juego | Cómo | Lectura |
|---|---|---|
| L1 · barra | `HECHO / MADE  EN / IN` encima de `OAXACA`; el inglés va en el color del tema | Compacta, en una línea; se lee con un poco de esfuerzo porque empareja palabras sueltas |
| **L2 · apilado** | «HECHO EN» en tinta y «MADE IN» en color, unidos por una llave a un solo OAXACA | La más clara: dos idiomas, una sola Oaxaca |
| **L3 · giro** | «HECHO EN» y «MADE IN» se turnan girando sobre su eje horizontal, como las caras de la marmota; OAXACA no se mueve. Ciclo de 6 s, en bucle (`l3-giro.gif`). Con «reducir movimiento», se queda en «MADE IN» | El juego más propio; sin movimiento depende de L2 |
