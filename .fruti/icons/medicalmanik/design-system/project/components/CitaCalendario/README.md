# CitaCalendario

Cómo aparece una cita en los espacios del calendario de Expediente y de Agenda.

- **Anatomía:** tarjeta blanca dentro del espacio, con una barra izquierda de 4 px en el color del estado (`exito`, `info`, `aviso` o `error`). El estado siempre lleva icono de Lucide y, si cabe, texto: nunca solo color.
- **Según la duración** (15 min = 24 px): 15 min muestra icono del estado, hora y paciente en una línea; 30 min agrega el estado en texto; 60 min o más agrega horario completo y motivo.
- **Estados** (uno a la vez): Terminada (`exito`, circle-check, sin sombra y nombre en «muted»: ya pasó), Confirmó (`exito`, calendar-check), En sala (`info`, armchair, fondo `info-soft` para que se note quién espera), Sin respuesta (`info`, clock), No confirmó (`aviso`, calendar-x), Cancelada (`error`, circle-x).
- **Cancelada** ocupa solo la mitad izquierda del espacio, con borde punteado y el nombre tachado: el resto del espacio se puede volver a agendar.
- **Signos fuera de rango** es una alerta clínica, no un estado: un círculo `error-soft` con triangle-alert en la esquina superior derecha. Se suma al estado (por ejemplo, En sala + alerta) y no cambia la barra.
- **Accesibilidad:** cada cita es un botón con `aria-label` completo («8:45 a 9:15, Rosa Martínez, Revisión de glucosa. Estado: En sala. Alerta: signos fuera de rango.»). En 15 min el texto del estado no cabe; está en el `aria-label` y en el detalle al abrir la cita.
- **Pendiente de definir:** el plazo de «No confirmó», el estado de una cita recién creada antes del recordatorio, y si «En consulta» y «No asistió» siguen existiendo.
- El consumidor provee: hora de inicio y fin, paciente, motivo, estado y alertas.
