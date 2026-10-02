# Reglas de Mango (M1–M9)

Cada regla: **regla → mecanismo → cómo comprobarlo**. Salieron de construir y renderizar escenas reales en el estilo de línea de rotulador.

## M1 · Componer con piezas del kit
- **Regla:** manos, brazos, cabezas, torsos, agujeros, rayitas y objetos salen del kit (`scripts/kit.mjs`). Lo que falta se añade al kit como pieza reutilizable, con roles de color.
- **Mecanismo:** dibujar cada escena desde cero da formas toscas y estilos distintos en cada ilustración; las piezas probadas dan una familia coherente.

## M2 · Una idea, no una descripción
- **Regla:** la escena cuenta el mensaje con un gesto o una situación con ingenio (alguien que se asoma, un brazo que sale de un agujero, un objeto con vida, rayitas de «¡ta-dá!»). La escena literal es el último recurso.
- **Comprobar:** ¿se entiende el mensaje sin el titular y tiene algo que sorprende?

## M3 · Temblor de rotulador, determinista
- **Regla:** todo contorno pasa por `trazo()` con `semilla()` fija en la escena; amplitud 0.8 en trazos largos, 0.2–0.4 en cortos y detalles. Los extremos de un trazo abierto no tiemblan, para que las uniones encajen.
- **Mecanismo:** el temblor lento (no ruido) imita el pulso de la mano y hace que las imperfecciones parezcan intención; la semilla fija hace que el dibujo no cambie al regenerarlo.
- **Comprobar:** regenera dos veces: ¿sale idéntico? ¿Alguna unión se abre?

## M4 · Relleno desplazado solo en el foco
- **Regla:** el relleno de `acento` del objeto foco va desplazado ~6 unidades del contorno (impresión mal registrada); el resto de rellenos (`papel`) coinciden con su contorno.
- **Comprobar:** ¿hay un único elemento con el color fuera de la línea?

## M5 · Lo que se sostiene, se apoya
- **Regla:** un objeto en la mano se apoya centrado en el `apoyo` de la mano (cuenco), y la mano se pinta encima para que los dedos lo abracen; nunca tocando por su borde.
- **Mecanismo:** apoyado en el borde, el objeto parece flotar como un globo.

## M6 · Nada tapa la cabeza ni la mano que actúa
- **Regla:** ≥8 unidades libres alrededor de la cara y de la mano activa; el brazo no cruza la cara (adelántalo o súbelo).
- **Comprobar:** captura de escritorio: ¿algún solapamiento?

## M7 · Funciona en su tamaño real
- **Regla:** se juzga a 360 px además de escritorio. El grosor de línea escala con el lienzo; detalles menores de ~6 unidades se pierden en móvil.

## M8 · El tema pone el color, también en oscuro
- **Regla:** ninguna forma fija su color. En oscuro se invierten `fondo`, `tinta` y `papel`: las masas de tinta (pelo, agujeros) pasan a claro; revisa en el banco que la escena siga leyéndose.

## M9 · Sin texto real dentro
- **Regla:** el texto dentro de la ilustración son trazos de relleno, nunca palabras (no se traduce ni escala con la tipografía; lo que la escena dice va en `<title>` o en el texto de la sección).
