# FichaMedico

La ficha del médico en los resultados. **Celular primero** (70 % del uso): la versión compacta es la principal y la amplia sale del ancho del contenedor (container query a 560 px), no del dispositivo.

- **Lo que cabe sin hacer scroll en celular**, en este orden: nombre y especialidad; consultorio y distancia; «Consulta» + precio; calificación y cédula en una línea; cuándo; hasta 3 horarios + «Más horarios»; acción a todo el ancho. Unas dos fichas por pantalla de 390 × 844.
- **Compacta** (< 560 px): avatar de 72 px (`foto-ficha-movil`) junto a la cabecera; el resto ocupa todo el ancho; botones a todo el ancho; radio 24.
- **Amplia** (≥ 560 px): foto de 132 px a la izquierda; precio alineado a la derecha; botones a su ancho; radio `radius-ficha`.
- **Precio y forma de agendar son de cada consultorio** (decisión 2026-11-04): la ficha muestra el consultorio más cercano que cumpla los filtros y nunca mezcla datos de dos. Con más de uno: «Atiende en N consultorios · ver todos».
- **En línea:** horarios + «Agendar». **Por teléfono:** el número visible y **«Llamar»** como acción principal (enlace `tel:` con el número en formato internacional) + «Copiar número» secundario. **Nuevo:** «Nuevo en Manik» en lugar de la calificación.
- Sin foto, avatar de silueta (ver FotoMedico).
- El consumidor provee: médico, especialidad, tipo de avatar o foto, consultorio mostrado (nombre, distancia, precio, forma de agendar, horarios o teléfono), número de consultorios, calificación y verificación. Datos de ejemplo.
