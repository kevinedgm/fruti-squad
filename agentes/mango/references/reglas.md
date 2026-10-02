# Reglas de Mango (M1–M10)

Cada regla: **regla → mecanismo → cómo comprobarlo**. Salieron de construir y renderizar escenas reales en el estilo de línea de rotulador.

## M1 · Componer con piezas del kit
- **Regla:** manos, brazos, cabezas, torsos, agujeros, rayitas y objetos salen del kit (`scripts/kit.mjs`). Lo que falta se añade al kit como pieza reutilizable, con roles de color.
- **Mecanismo:** dibujar cada escena desde cero da formas toscas y estilos distintos en cada ilustración; las piezas probadas dan una familia coherente.

## M2 · Una idea, no una descripción
- **Regla:** la escena cuenta el mensaje con un gesto o una situación con ingenio (alguien que se asoma, un brazo que sale de un agujero, un objeto con vida, rayitas de «¡ta-dá!»). La escena literal es el último recurso.
- **Comprobar:** ¿se entiende el mensaje sin el titular y tiene algo que sorprende?

## M3 · Trazo orgánico, determinista
- **Regla (especificación «Vector Illustrator Skill»: `stroke.variation: subtle`, `texture: false`):** toda línea es un `trazoOrganico()` (vía `linea()`) con `semilla()` fija en la escena: una cinta de **peso estable** (tinta `#111111`, extremos redondeados) que solo afina un poco al entrar y salir, apenas ondula (±5 %) y tiembla despacio; sin grano ni textura de lápiz. Los extremos se pasan apenas.
- **Mecanismo:** la mano se nota en irregularidades sutiles y deliberadas (temblor lento, extremos), no en un borde áspero: el grano y la presión exagerada leen como lápiz falso y ensucian a tamaño pequeño. Temblor escalado con la longitud: un gesto corto (rayita, antena) es firme.
- **Comprobar:** regenera dos veces: ¿sale idéntico? En la captura, ¿el grosor se ve constante en los contornos largos y el borde limpio?

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

## M10 · Orgánico es el trazo, no la proporción
- **Regla:** toda persona sale de `figura()` y `cabeza()`: canon de la especificación (`CANON`): cabeza/torso ≈ 0,65 (rango 0,55–0,75), ~5,6 cabezas de alto, hombros compactos, extremidades alargadas y suaves que se adelgazan del hombro a la muñeca y de la cadera al tobillo; manos 1,0 neutras y 1,15–1,35 (`CANON.enfasis.comunicativo`) solo en la mano que hace la acción importante. Rostro 3/4 con el ADN de la hoja: nariz lineal angular, ojos con marcas simples, boca breve, oreja visible, mandíbula y cuello separados; pelo como masa negra sólida (`PEINADOS`); variantes de cara a–d (`CARAS`) para una población coherente; expresiones de la lista (`EXPRESIONES`), leídas primero en el giro de cabeza y la postura.
- **Mecanismo:** el temblor y la presión hacen el trazo humano; si además las proporciones fallan (cabeza grande, brazo que sale del pecho, cuello largo), la ilustración se lee como dibujo infantil. Separar canon (fijo) de trazo (orgánico) permite el estilo suelto sin perder el oficio.
- **Comprobar:** pon la figura junto a la guía de cabezas (`examples/fundamentos.mjs`): ¿mide ~5,6 cabezas, la muñeca cae bajo la cadera, el codo a la cintura? ¿La pose se lee sin intersecciones ambiguas?
