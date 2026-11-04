# FichaMedico

La ficha del médico en los resultados: quién, qué atiende, cuánto cuesta, qué tan lejos y cuándo hay lugar.

- Orden fijo (la voz: «primero lo que el paciente necesita saber»): nombre (`nombre`) y especialidad; precio a la derecha (`precio`); chips de datos; cuándo; horarios; acción.
- Foto 3:4 a 132 px (88 px en celular) con `radius-foto`; sin foto, iniciales en Urbanist 300 sobre el degradado `foto-inicio` → `foto-fin` (ver FotoMedico).
- Chips: calificación (estrella + número en tinta), distancia, «Cédula verificada» (`exito`), «Nuevo en Manik» (`luz-calida`) en lugar de la calificación cuando aún no hay opiniones.
- Tres variantes por cómo se agenda: **en línea** (horarios + «Agendar»), **por teléfono** (número en `telefono` + «Copiar número»: no se usa `tel:` porque no siempre abre), **nuevo** (primer día libre).
- Tarjeta blanca, borde `linea`, `radius-ficha`; `shadow-hover` al pasar el cursor.
- El consumidor provee: médico, especialidad, precio, calificación y número de opiniones, distancia, verificación, próxima fecha y horarios o teléfono. Datos de ejemplo.
