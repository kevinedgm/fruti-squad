# Convia · demo interna r11 (agenda, seguir y avisos)

Lleva el modelo aprobado **perfil + actividad + sede** (`../convia-final/modelo-datos.md`) al directorio.

- **Pestañas**: Todo · Cafés · Restaurantes · Hoteles · Museos y galerías · **Agenda**. Talleres y recorridos dejan de ser giros.
- **Agenda**: actividades por día desde el sáb 31 oct 2026 (fecha fija de la demo): «En curso» (exposiciones), un bloque por día, y «Fecha por confirmar» (talleres reales del Museo Textil, según sus carteles). Cada renglón: hora, tipo con su color, nombre, «Organiza X · En Y» (o «En Y · lo organiza el lugar»), precio.
- Filtros: Todo · Talleres · Recorridos · Eventos · Exposiciones · **Solo lo que sigo**.
- **Quiénes organizan**: todos los organizadores (colectivos, estudios, operadores, personas y lugares) con **Seguir**.
- **Avisos** (campana): actividades de quienes sigues; «Nuevo» si se publicaron después de tu última visita. Al abrir, se marcan como vistos. Canal del aviso: pendiente de decisión.
- Inicio («Todo»): «Próximos días» con las 4 siguientes actividades y «Ver toda la agenda».
- Perfil interno de un lugar: **Actividades aquí** (las suyas y las de otros con sede ahí) y «Ver el perfil completo ↗» si ya existe la página (café, restaurante, hotel, museo).
- Los organizadores con perfil completo (colectivo, taller, recorridos, museo, café) **enlazan a esas páginas**: la demo se recorre de punta a punta.
- Fechas verificadas con el calendario 2026; el generador valida que todas sean fechas reales.
- Pendiente: el pasaporte sigue contando insignias de talleres y recorridos, pero en la agenda todavía no se puede marcar «Ya fui».
- Publicada: https://claude.ai/artifact/5BuddSKv1ogLapyRRfoCc5. Uso: `python3 gen.py <carpeta con img/>`.
