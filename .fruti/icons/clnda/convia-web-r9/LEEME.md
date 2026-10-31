# Convia · demo interna r9 (tarjetas uniformes + perfil)

- Pedido del usuario (2026-10-31): todas las tarjetas del mismo tamaño, solo información básica; rasgos como sellitos de ícono; el detalle va en el perfil del lugar.
- Tarjeta (piezas fijas, siempre en el mismo lugar): foto · giro · nombre (máx. 2 líneas) · zona o fecha + precio (1 línea) · sellitos de rasgos (fila fija, vacía si no hay) · «X de cada 10 volverían» o «Recién llegado» (1 línea) · Quiero ir / ¿Ya fuiste? (apilados).
- Ancho fijo de columna: 5 visibles en escritorio, 3 en tableta, 78 % en celular. Verificado: un solo tamaño de tarjeta por ancho (1440, 820, 390).
- Perfil `#lugar/<id>`: foto, descripción, datos (cuándo, zona, horario y precio, organiza), calificación personal, métrica con puntos y visitas, explicación de Favorito Convia y rasgos con su regla. «Volver» regresa a la misma posición.
- La calificación se mueve de la tarjeta al perfil (y «Calificar» en Mis lugares → Ya fui).
- Lo demás igual que r8: rasgos y métricas solo en «Ejemplo»; fotos de relleno desenfocadas; imágenes fuera del repo. Uso: `python3 gen.py <carpeta con img/>`.
- Publicada: https://claude.ai/artifact/GGWDQM4AP8otPz8vxsoYcy (r8 sigue en https://claude.ai/artifact/5eUmppakGiP5agKK2xJbWr)
