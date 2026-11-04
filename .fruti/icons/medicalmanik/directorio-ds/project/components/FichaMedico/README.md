# FichaMedico

La ficha del médico en los resultados: quién, qué atiende, dónde, cuánto cuesta y cuándo hay lugar. Muestra UN consultorio: el más cercano a donde busca el paciente.

- **Precio y forma de agendar son de cada consultorio** (decisión 2026-11-04). La ficha muestra el precio, la distancia y la forma de agendar del consultorio que enseña; nunca mezcla datos de dos consultorios.
- Si el médico atiende en más de uno: «Atiende en N consultorios · ver todos», que abre la lista en el perfil.
- Orden fijo («primero lo que el paciente necesita saber»): nombre (`nombre`) y especialidad; «Consulta» + precio a la derecha (`precio`); chips (calificación, consultorio y distancia, cédula); cuándo; horarios; acción.
- Foto 3:4 a 132 px (88 px en celular) con `radius-foto`; sin foto, el avatar de silueta (ver FotoMedico).
- Chips: calificación (estrella + número en tinta), distancia, «Cédula verificada» (`exito`), «Nuevo en Manik» (`luz-calida`) en lugar de la calificación cuando aún no hay opiniones.
- Tres variantes por cómo se agenda: **en línea** (horarios + «Agendar»), **por teléfono** (número en `telefono` + «Copiar número»: no se usa `tel:` porque no siempre abre), **nuevo** (primer día libre).
- Tarjeta blanca, borde `linea`, `radius-ficha`; `shadow-hover` al pasar el cursor.
- Filtros: «Cita en línea» y «Hasta $800» se evalúan por consultorio; si el más cercano no cumple pero otro sí, la ficha muestra el que cumple.
- El consumidor provee: médico, especialidad, sexo para el avatar, consultorio mostrado (nombre, distancia, precio, forma de agendar, horarios o teléfono), número de consultorios, calificación y verificación. Datos de ejemplo.
