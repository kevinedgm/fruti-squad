# Reglas de Mango (M1–M8)

Cada regla: **regla → mecanismo → cómo comprobarlo**. Salieron de construir y renderizar escenas reales.

## M1 · Componer con piezas, nunca a mano alzada
- **Regla:** personas, objetos y fondos salen del kit (`scripts/kit.mjs`). Lo que falta se añade al kit como pieza reutilizable.
- **Mecanismo:** colocar puntos a mano produce formas orgánicas toscas y cada ilustración sale de un estilo distinto; las piezas geométricas paramétricas dan formas limpias y una familia coherente.
- **Comprobar:** ¿todas las formas de la escena vienen de una función del kit?

## M2 · La pose cuenta la acción
- **Regla:** la acción («explica», «señala», «saluda», «sostiene») la dice la pose del brazo, no un detalle de la cara (las caras van sin rasgos).
- **Comprobar:** tapa los objetos: ¿la silueta de la persona ya dice qué hace?

## M3 · Superficie clara que puede caer sobre la página lleva borde
- **Regla:** paneles, bocadillos y tarjetas en `superficie` llevan contorno `linea`.
- **Mecanismo:** blanco sobre página blanca desaparece fuera de la mancha de fondo (pasó con el primer bocadillo).
- **Comprobar:** en el banco, fila clara: ¿se ve el borde de cada superficie?

## M4 · Nada tapa la cabeza ni la mano que actúa
- **Regla:** bocadillos, puntos y objetos dejan ≥8 unidades libres alrededor de la cabeza y de la mano activa; los decorativos no se tocan entre sí.
- **Comprobar:** captura de escritorio: ¿hay algún solapamiento entre cabeza/mano y otra pieza?

## M5 · Un foco
- **Regla:** el `acento` va en lo que la sección quiere que se mire (la persona o el dato); el resto en `forma`, `linea`, `tinta-2`. Máximo 2 acentos.
- **Comprobar:** entrecierra los ojos en la captura: ¿lo primero que ves es el foco?

## M6 · Funciona en su tamaño real
- **Regla:** la escena se juzga a 360 px (móvil) además de escritorio; los detalles menores de ~6 unidades del lienzo (480) se pierden en móvil.
- **Comprobar:** captura móvil: ¿se sigue leyendo la acción?

## M7 · El tema pone el color, también en oscuro
- **Regla:** ninguna forma fija su color; todo por roles → tokens. En oscuro, `superficie`, `forma` y `linea` vienen de los tokens oscuros del proyecto.
- **Comprobar:** fila de temas y fila oscura del banco: ¿sigue siendo la misma escena y se distingue todo?

## M8 · Sin texto real dentro
- **Regla:** el texto dentro de la ilustración son barras de relleno, nunca palabras.
- **Mecanismo:** el texto en un SVG no se traduce, no escala con la tipografía del sitio y los lectores de pantalla lo leen fuera de contexto; lo que la escena dice va en el `<title>` o en el texto de la sección.

## Personas
- Una misma serie usa la misma escala de persona (`escala`), para que no cambien de tamaño entre secciones.
- Diversidad por roles: `piel`, `piel-2`, `piel-3` y peinados variados en escenas con varias personas; nunca un tono fijo.
